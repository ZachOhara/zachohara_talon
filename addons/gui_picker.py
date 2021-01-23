from talon import Module, Context, actions, app, imgui, ui
from collections.abc import Callable

module = Module()
module.mode('gui_picker')

main_screen = ui.main_screen()

menu_title = None
option_list = None
selection_callback = None

@imgui.open(y=0, x=main_screen.width / 2.6, software=app.platform == 'linux')
def gui(gui: imgui.GUI):
    global menu_title
    global option_list
    gui.text(menu_title)
    gui.line()
    i = 1
    for option in option_list:
        gui.text('Pick ' + str(i) + ': ' + option)
        i += 1
    gui.line()
    gui.text('(Or say \"hide\" to cancel)')

def construct_gui_picker(title, options, sort_alphabetical):
    global menu_title
    global option_list
    menu_title = str(title)
    option_list = [str(i) for i in options]
    if sort_alphabetical:
        option_list = option_list.sort()
    gui.show()
    actions.mode.enable('user.gui_picker')

def deconstruct_gui_picker():
    gui.hide()
    actions.mode.disable('user.gui_picker')

@module.action_class
class Actions:

    def test_gui_picker():
        """Test the GUI picker"""
        def test_callback(n):
            actions.insert(str(n))
        actions.user.show_gui_picker(
            'Test menu title',
            ['option one','option two','option three','option four'],
            test_callback
        )

    def show_gui_picker(title: str, options: list, callback: Callable[[int],None], sort_alphabetical: bool=False):
        """Show the GUI picker with the given options"""
        global selection_callback
        selection_callback = callback
        construct_gui_picker(title, options, sort_alphabetical)

    def picker_select(n: int):
        """Respond to the user picking from the options"""
        global selection_callback
        global option_list
        selection_callback(option_list[n-1])
        deconstruct_gui_picker()

    def hide_gui_picker():
        """Hide the picker without choosing an option"""
        deconstruct_gui_picker()
