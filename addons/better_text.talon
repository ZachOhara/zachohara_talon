-
jump start: key(ctrl-home)
jump end: key(ctrl-end)

jump: key(ctrl-right)
jump back: key(ctrl-left)

push: key(end)
push back: key(home)

slap back: key(home enter)
subsequent: key(end enter enter)

select that: edit.select_word()
select jump: edit.extend_word_right()
select jump back: edit.extend_word_left()
select push: edit.extend_line_end()
select push back: edit.extend_line_start()

wipe that:
    edit.select_word()
    edit.delete()
wipe line:
    edit.select_line()
    edit.delete()
wipe jump:
    edit.extend_word_right()
    edit.delete()
wipe jump back:
    edit.extend_word_left()
    edit.delete()
wipe push:
    edit.extend_line_end()
    edit.delete()
wipe push back:
    edit.extend_line_start()
    edit.delete()

tap out: user.editing_tap_out()
back tap out: user.editing_tap_out_back()
tap in: user.editing_tap_in()
back tap in: user.editing_tap_in_back()
