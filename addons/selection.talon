mode: user.arrow_selection
-
pick (that|it):
    user.do_arrow_selection(0)
pick <number>:
    user.do_arrow_selection(number)
(maybe|hover|however) <number>:
    user.do_arrow_selection_no_commit(number)
(escape|hide):
    key(esc)
    user.disable_arrow_selection()
(enter|slap):
    key(enter)

