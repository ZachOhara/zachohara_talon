from talon import Module, Context, actions

module = Module()

delimiter_pairs = ('()', '[]', '{}', '<>', '""', '\'\'')
delimiter_singles = ('%', '$')

def do_tap_out(is_forward):
    # Calculate the number of characters to move
    search_string = get_search_string(is_forward)
    if not is_forward:
        search_string = search_string[::-1]
    delimiter_index = 1 if is_forward else 0
    delimiter_index_opposite = 0 if is_forward else 1
    delimiters = [s[delimiter_index] for s in delimiter_pairs]
    delimiters_opposite = [s[delimiter_index_opposite] for s in delimiter_pairs]
    delimiters += delimiter_singles
    move = 0
    opposite_stack = []
    for c in search_string:
        move += 1
        if c in delimiters:
            if len(opposite_stack) == 0 or c != opposite_stack[-1]:
                break
        if c in delimiters_opposite:
            i = delimiters_opposite.index(c)
            opposite_stack.append(delimiters[i])
    # Cap the movement at the beginning or end of line
    move = min(move, len(search_string))
    # Do cursor movement
    do_cursor_movement(is_forward, move)

def do_tap_in(is_forward):
    # Calculate the number of characters to move
    search_string = get_search_string(is_forward)
    if not is_forward:
        search_string = search_string[::-1]
    delimiter_index = 0 if is_forward else 1
    delimiters = [s[delimiter_index] for s in delimiter_pairs]
    delimiters += delimiter_singles
    move = 0
    for c in search_string:
        move += 1
        if c in delimiters:
            break
    # Cap the movement at the beginning or end of line
    move = min(move, len(search_string))
    # Do cursor movement
    do_cursor_movement(is_forward, move)

def get_search_string(is_forward):
    if is_forward:
        actions.edit.extend_line_end()
    else:
        actions.edit.extend_line_start()
    return actions.edit.selected_text()

def do_cursor_movement(is_forward, movement):
    directions = {
        True: actions.edit.right,
        False: actions.edit.left
    }
    # Exit the selection in the opposite direction
    directions[not is_forward]()
    # Do the cursor movement
    for i in range(movement):
        directions[is_forward]()

@module.action_class
class Actions:

    def editing_tap_in():
        """Tap in"""
        do_tap_in(True)

    def editing_tap_out():
        """Tap out"""
        do_tap_out(True)

    def editing_tap_in_back():
        """Tap in back"""
        do_tap_in(False)

    def editing_tap_out_back():
        """Tap out back"""
        do_tap_out(False)


