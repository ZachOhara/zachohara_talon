-
settings():
    insert_wait = 30
latex dictionary:
    user.latex_dictionary_menu()
inline math:
    insert('$$')
    key(left)
display math:
    insert('\\[\\]')
    key(left left enter enter left)
break line:
    insert('\\\\\n')
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
# TODO: Text styles
