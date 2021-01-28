mode: user.latex
mode: command
and code.language: latex
-
# Settings
settings():
    insert_wait = 30
# Dictionary commands
latex dictionary:
    user.latex_dictionary_menu()
# Basic latex formatting
inline [math]:
    insert('$$')
    key(left)
display math:
    insert('\\[\\]')
    key(left left enter enter left)
break line:
    insert('\\\\\n')
# Commands with captures / special commands
(sub|subscript|from):
    insert('_{}')
    key(left)
(sub|subscript) <number>:
    insert('_')
    insert(number)
(power|power of|super|superscript|going to):
    insert('^{}')
    key(left)
(power|power of) <number>:
    insert('^')
    insert(number)
root <number>:
    insert('\\sqrt[')
    insert(number)
    insert(']{}')
    key(left)
(cube|cubed) root:
    insert('\\sqrt[3]{}')
    key(left)
integral:
    insert('\\int\\,d')
    key(left left left)
double integral:
    insert('\\iint\\,d\\,d')
    key(left left left left left left)
triple integral:
    insert('\\iiint\\,d\\,d\\,d')
    key(left left left left left left left left left)
open integral:
    insert('\\oint\\,d')
    key(left left left)
# Commands from config files
document class:
    insert('\\documentclass{}')
    key(left)
document class {user.latex_document_class}:
    insert('\\documentclass{')
    insert(user.latex_document_class)
    insert('}')
use package:
    insert('\\usepackage{}')
    key(left)
use package {user.latex_package}:
    insert('\\usepackage{')
    insert(user.latex_package)
    insert('}')
begin:
    insert('\\begin{}')
    key(left)
begin {user.latex_environment}:
    insert('\\begin{')
    insert(user.latex_environment)
    insert('}')
end:
    insert('\\end{}')
    key(left)
end {user.latex_environment}:
    insert('\\end{')
    insert(user.latex_environment)
    insert('}')
# TODO: Environments with arguments
{user.latex_command}:
    insert('\\')
    insert(user.latex_command)
{user.latex_command_argumented}:
    insert('\\')
    insert(user.latex_command_argumented)
    insert('{}')
    key(left)
{user.latex_text_style}:
    insert('\\')
    insert(user.latex_text_style)
    insert('{}')
    key(left)
{user.latex_text_style} that:
    user.latex_apply_text_style(user.latex_text_style)
greek {user.latex_greek_letter}:
    insert('\\')
    insert(user.latex_greek_letter)
{user.latex_shortcut}:
    insert(user.latex_shortcut)
{user.latex_function}:
    insert('\\')
    insert(user.latex_function)
    insert('()')
    key(left)
{user.latex_symbol}:
    insert('\\')
    insert(user.latex_symbol)
{user.latex_symbol_argumented}:
    insert('\\')
    insert(user.latex_symbol_argumented)
    insert('{}')
    key(left)
{user.latex_symbol_argumented_double}:
    insert('\\')
    insert(user.latex_symbol_argumented_double)
    insert('{}')
    insert('{}')
    key(left left left)
{user.latex_symbol_boundable}:
    insert('\\')
    insert(user.latex_symbol_boundable)
{user.latex_formatter} that:
    user.latex_apply_formatter(user.latex_formatter)
