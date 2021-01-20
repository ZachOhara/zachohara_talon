import re

from talon import Context, Module, actions, settings

mod = Module()
ctx = Context()
ctx.matches = r"""
mode: user.python
mode: command
and code.language: python
"""
ctx.lists["user.code_functions"] = {
    # Small list, prepackaged with the default
    '''
    "enumerate": "enumerate",
    "integer": "int",
    "length": "len",
    "list": "list",
    "print": "print",
    "range": "range",
    "set": "set",
    "split": "split",
    "string": "str",
    "update": "update",
    '''
    # Large list, contains all built-in functions
    "ABS": "abs",
    "absolute": "abs",
    "all": "all",
    "any": "any",
    "ascii": "ascii",
    "ask E": "ascii",
    "bin": "bin",
    "bool": "bool",
    "breakpoint": "breakpoint",
    "bites": "bytes",
    "callable": "callable",
    "char": "chr",
    "character": "chr",
    "class method": "classmethod",
    "compile": "compile",
    "complex": "complex",
    "Dell at her": "delattr",
    "delete attribute": "delattr",
    "dict": "dict",
    "dictionary": "dict",
    "dir": "dir",
    "div mod": "divmod",
    "enumerate": "enumerate",
    "eval": "eval",
    "exec": "exec",
    "execute": "exec",
    "filter": "filter",
    "float": "float",
    "format": "format",
    "frozen set": "frozenset",
    "get at her": "getattr",
    "get attribute": "getattr",
    "globals": "globals",
    "has at her": "hasattr",
    "has attribute": "hasattr",
    "hash": "hash",
    "help": "help",
    "hex": "hex",
    "hexadecimal": "hex",
    "id": "id",
    "input": "input",
    "int": "int",
    "integer": "int",
    "is instance": "isinstance",
    "is subclass": "issubclass",
    "iter": "iter",
    "iterator": "iter",
    "len": "len",
    "length": "len",
    "list": "list",
    "locals": "locals",
    "map": "map",
    "max": "max",
    "maximum": "max",
    "memory view": "memoryview",
    "min": "min",
    "minimum": "min",
    "next": "next",
    "object": "object",
    "oct": "oct",
    "octal": "oct",
    "open": "open",
    "ord": "ord",
    "ordinal": "ord",
    "pow": "pow",
    "power": "pow",
    "print": "print",
    "property": "property",
    "range": "range",
    "repr": "repr",
    "representation": "repr",
    "reversed": "reversed",
    "round": "round",
    "set": "set",
    "set at her": "setattr",
    "set attribute": "setattr",
    "slice": "slice",
    "sorted": "sorted",
    "static method": "staticmethod",
    "string": "str",
    "some": "sum",
    "super": "super",
    "tuple": "tuple",
    "type": "type",
    "vars": "vars",
    "variables": "variables",
    "zip": "zip",
    "import": "__import__",
}

"""a set of fields used in python docstrings that will follow the
reStructuredText format"""
docstring_fields = {
    "class": ":class:",
    "function": ":func:",
    "parameter": ":param:",
    "raise": ":raise:",
    "returns": ":return:",
    "type": ":type:",
    "return type": ":rtype:",
    # these are sphinx-specific
    "see also": ".. seealso:: ",
    "notes": ".. notes:: ",
    "warning": ".. warning:: ",
    "todo": ".. todo:: ",
}

mod.list("python_docstring_fields", desc="python docstring fields")
ctx.lists["user.python_docstring_fields"] = docstring_fields

type_list = {
    "boolean": "bool",
    "integer": "int",
    "string": "str",
    "none": "None",
    "dick": "Dict",
    "float": "float",
    "any": "Any",
    "tuple": "Tuple",
    "union": "UnionAny",
    "iterable": "Iterable",
    "vector": "Vector",
    "bytes": "bytes",
    "sequence": "Sequence",
    "callable": "Callable",
    "list": "List",
    "no return": "NoReturn",
}

mod.list("python_type_list", desc="python types")
ctx.lists["user.python_type_list"] = type_list

exception_list = [
    "BaseException",
    "SystemExit",
    "KeyboardInterrupt",
    "GeneratorExit",
    "Exception",
    "StopIteration",
    "StopAsyncIteration",
    "ArithmeticError",
    "FloatingPointError",
    "OverflowError",
    "ZeroDivisionError",
    "AssertionError",
    "AttributeError",
    "BufferError",
    "EOFError",
    "ImportError",
    "ModuleNotFoundError",
    "LookupError",
    "IndexError",
    "KeyError",
    "MemoryError",
    "NameError",
    "UnboundLocalError",
    "OSError",
    "BlockingIOError",
    "ChildProcessError",
    "ConnectionError",
    "BrokenPipeError",
    "ConnectionAbortedError",
    "ConnectionRefusedError",
    "ConnectionResetError",
    "FileExistsError",
    "FileNotFoundError",
    "InterruptedError",
    "IsADirectoryError",
    "NotADirectoryError",
    "PermissionError",
    "ProcessLookupError",
    "TimeoutError",
    "ReferenceError",
    "RuntimeError",
    "NotImplementedError",
    "RecursionError",
    "SyntaxError",
    "IndentationError",
    "TabError",
    "SystemError",
    "TypeError",
    "ValueError",
    "UnicodeError",
    "UnicodeDecodeError",
    "UnicodeEncodeError",
    "UnicodeTranslateError",
    "Warning",
    "DeprecationWarning",
    "PendingDeprecationWarning",
    "RuntimeWarning",
    "SyntaxWarning",
    "UserWarning",
    "FutureWarning",
    "ImportWarning",
    "UnicodeWarning",
    "BytesWarning",
    "ResourceWarning",
]
mod.list("python_exception", desc="python exceptions")
ctx.lists["user.python_exception"] = {
    " ".join(re.findall("[A-Z][^A-Z]*", exception)).lower(): exception
    for exception in exception_list
}


@ctx.action_class("user")
class user_actions:
    def code_insert_function(text: str, selection: str):
        if selection:
            text = text + "({})".format(selection)
        else:
            text = text + "()"
        actions.user.paste(text)
        actions.edit.left()

    def code_private_function(text: str):
        """Inserts private function declaration"""
        result = "def _{}():".format(
            actions.user.formatted_text(
                text, settings.get("user.code_private_function_formatter")
            )
        )

        actions.user.paste(result)
        actions.edit.left()
        actions.edit.left()

    def code_public_function(text: str):
        result = "def {}():".format(
            actions.user.formatted_text(
                text, settings.get("user.code_public_function_formatter")
            )
        )
        actions.user.paste(result)
        actions.edit.left()
        actions.edit.left()


@mod.action_class
class module_actions:
    # TODO this could go somewhere else
    def insert_cursor(text: str):
        """Insert a string. Leave the cursor wherever [|] is in the text"""
        if "[|]" in text:
            end_pos = text.find("[|]")
            s = text.replace("[|]", "")
            actions.insert(s)
            actions.key(f"left:{len(s) - end_pos}")
        else:
            actions.insert(text)
