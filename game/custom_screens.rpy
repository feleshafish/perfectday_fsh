#########################
## Ask useer their name
#########################
screen name(prompt=Null):
    style_prefix "name"
    modal True

    frame:
        background Frame("gui/overlay/confirm.png", Borders(25, 25, 25, 25))
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30

        vbox:
            spacing 10
            text prompt style "name_prompt"
            input id "name"

style name_prompt is default

style name_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("name_prompt")
    color '#c19d9d'

style name:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width



screen journal():
    modal True

    add "notebook.png"

    text "[my_name]"

    textbutton "Close Journal":
        action Return()
    

    frame:
        xalign 0.5
        yalign 0.5
        background Frame("images/notebook.png", Borders(25, 25, 25, 25))

    


