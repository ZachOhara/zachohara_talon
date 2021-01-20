from talon import Context, Module

import os
import subprocess

# Change the string to the path of your preferred text editor
EDITOR_PATH = 'C:\\Program Files\\Sublime Text 3\\sublime_text.exe'

WORD_LIST_PATH = 'user\\zachohara_talon\\settings\\additional_words.csv'
REPLACEMENT_LIST_PATH = 'user\\zachohara_talon\\settings\\words_to_replace.csv'
HOMOPHONE_LIST_PATH = 'user\\zachohara_talon\\code\\homophones.csv'
EXTENSION_LIST_PATH = 'user\\zachohara_talon\\misc\\extensions.talon'

mod = Module()

def open_editor(filepath):
    subprocess.Popen('%s %s' % (EDITOR_PATH, filepath))

@mod.action_class
class Actions:

    def dictionary_edit_words():
        """Open a text editor to edit additional_words.csv"""
        open_editor(WORD_LIST_PATH)
    
    def dictionary_edit_replacements():
        """Open a text editor to edit words_to_replace.csv"""
        open_editor(REPLACEMENT_LIST_PATH)
    
    def dictionary_edit_homophones():
        """Open a text editor to edit homophones.csv"""
        open_editor(HOMOPHONE_LIST_PATH)
    
    def dictionary_edit_extensions():
        """Open a text editor to edit extensions.talon"""
        open_editor(EXTENSION_LIST_PATH)
