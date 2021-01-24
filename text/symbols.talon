at symbol: "@"
question [mark]: "?"
(downscore | underscore): "_"
double dash: "--"
(bracket | brack | left bracket): "{"
(rbrack | are bracket | right bracket): "}"
triple quote: "'''"
(dot dot | dotdot): ".."
#ellipses: "…"
ellipses: "..."
(comma and | spamma): ", "
plus: "+"
arrow: "->"
dub arrow: "=>"
new line: "\\n"
carriage return: "\\r"
line feed: "\\r\\n"
empty dubstring:
    '""'
    key(left)
empty escaped (dubstring|dub quotes):
    '\\"\\"'
    key(left)
    key(left)
empty string:
    "''"
    key(left)
empty escaped string:
    "\\'\\'"
    key(left)
    key(left)
(inside parens | args):
	insert("()")
	key(left)
inside (squares | list): 
	insert("[]") 
	key(left)
inside bracket: 
	insert("{}") 
    key(left)
inside angle:
    insert("<>")
    key(left)
inside percent: 
	insert("%%") 
	key(left)
inside (double|dub) quotes:
	insert('""')
    key(left)
inside single quotes:
    insert("''")
    key(left)
(parens | args) that:
    text = edit.selected_text()
    user.paste("({text})")
square that:
    text = edit.selected_text()
    user.paste("[{text}]")
bracket that: 
    text = edit.selected_text()
    user.paste("{{{text}}}")
angle that: 
    text = edit.selected_text()
    user.paste("<{text}>")
percent that: 
    text = edit.selected_text()
    user.paste("%{text}%")
(double) quote that:
    text = edit.selected_text()
    user.paste('"{text}"')
single quote that:
    text = edit.selected_text()
    user.paste("'{text}'")
