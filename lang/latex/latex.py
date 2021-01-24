from talon import Module, Context, actions

import csv, os

LATEX_EXTENSIONS = ('.tex',)

LATEX_DICTIONARY_DIRECTORY = 'user\\zachohara_talon\\lang\\latex\\latex_dictionary'

LATEX_DICTIONARY_LISTS = {
    'document_class': 'latex common document classes',
    'package': 'latex common packages',
    'environment': 'latex common environments',
    'environment_argumented': 'latex common environments requiring arguments',
    'command': 'latex common commands',
    'command_argumented': 'latex common commands requiring arguments',
    'text_style': 'latex common text styles',
    'greek_letter': 'latex Greek alphabet',
    'shortcut': 'latex common notation figures',
    'function': 'latex common functions',
    'symbol': 'latex common symbols without arguments',
    'symbol_argumented': 'latex common symbols requiring 1 argument',
    'symbol_argumented_double': 'latex common symbols requiring 2 arguments',
    'formatter': 'latex formatters'
}

directory_path = os.path.join(os.getcwd(), LATEX_DICTIONARY_DIRECTORY)
def get_dictionary_path(name):
    return os.path.join(directory_path, name + '.csv')

module = Module()
context = Context()

# Initial setup and loading of latex dictionaries
for name, description in LATEX_DICTIONARY_LISTS.items():
    filepath = get_dictionary_path(name)
    with open(filepath) as dictionary_file:
        dictionary = {}
        csv_list = [i for i in csv.reader(dictionary_file)]
        csv_list = csv_list[1:] # ignore the heading line
        for line in csv_list:
            if len(line) == 0:
                continue
            item = line[0]
            pronunciations = line[1:] if len(line)>1 else [item]
            for p in pronunciations:
                dictionary[p] = item
        list_name = 'latex_' + name
        module.list(list_name, desc=description)
        context.lists['user.' + list_name] = dictionary

# Create a master list of the dictionaries
# dictionary_master_list = [s.replace('_',' ') for s in LATEX_DICTIONARY_LISTS.keys()]
module.list('latex_dictionary', desc='latex dictionaries')
context.lists['user.latex_dictionary'] = {i:i.replace('_',' ') for i in LATEX_DICTIONARY_LISTS.keys()}

@module.action_class
class Actions:

    def latex_edit_dictionary(name: str):
        """Edit a latex dictionary"""
        filepath = get_dictionary_path(name)
        actions.user.dictionary_open_editor(filepath)

    def latex_dictionary_menu():
        """Show the latex dictionary menu"""
        actions.user.show_gui_picker(
            'Choose a dictionary to edit',
            LATEX_DICTIONARY_LISTS.keys(),
            actions.user.latex_edit_dictionary
        )

    def latex_apply_text_style(text_style: str):
        """Apply a latex text style"""
        selected = actions.edit.selected_text()
        actions.edit.delete()
        actions.insert('\\'+text_style+'{')
        actions.insert(selected)
        actions.insert('}')

    def latex_apply_formatter(formatter: str):
        """Apply a latex formatter"""
        before, after = formatter.split('@')
        selected = actions.edit.selected_text()
        actions.edit.delete()
        actions.insert(before)
        actions.insert(selected)
        actions.insert(after)
