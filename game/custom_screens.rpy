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
    

    frame:
        xalign 0.5
        yalign 0.5
        background Frame("images/notebook.png", Borders(25, 25, 25, 25))

    textbutton "Close Journal":
        yalign 0.95
        xalign 0.5

        # text colors
        text_idle_color  "#271515"
        text_hover_color  "#642121"
        text_selected_color  "#398bce"

        if not main_menu:
            action Return()
        else:
            action Hide("journal")
        

    


