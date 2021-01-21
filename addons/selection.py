from talon import Context, Module, actions, app

mod = Module()
mod.mode("arrow_selection")

arrow_direction = ''

def press_arrow_key(n: int):
    direction_callable = None
    if arrow_direction.startswith('u'):
        direction_callable = actions.edit.up
    elif arrow_direction.startswith('d'):
        direction_callable = actions.edit.down
    elif arrow_direction.startswith('l'):
        direction_callable = actions.edit.left
    elif arrow_direction.startswith('r'):
        direction_callable = actions.edit.right
    else:
        app.notify('selection.py', 'Unknown direction: ' + repr(arrow_direction))
    # This is indexed by 1, so subtract here
    for i in range(max(0, n-1)):
        direction_callable()


@mod.action_class
class Actions:

    def enable_arrow_selection(direction: str='right'):
        """Enable arrow selection mode"""
        global arrow_direction
        arrow_direction = direction.lower()
        actions.mode.enable('user.arrow_selection')

    def disable_arrow_selection():
        """Disable arrow selection mode"""
        actions.mode.disable('user.arrow_selection')

    def do_arrow_selection(n: int, do_enter: bool=True):
        """Do arrow selection"""
        press_arrow_key(n)
        if do_enter:
            actions.key('enter')
            actions.user.disable_arrow_selection()

    def do_arrow_selection_no_commit(n: int):
        """Do arrow selection but do not press enter"""
        press_arrow_key(n)
