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

    style_prefix "input"

    add "notebook.png"

    text "[my_name]"
    

    frame:
        xalign 0.5
        yalign 0.7
        xpadding 20
        ypadding 20

        background None

        fixed:
            xsize 800
            ysize 600

            input:
                value VariableInputValue("journal_text")
                length 250

                multiline True
                xmaximum 750
                pixel_width 750
                
                color "#000000"

            textbutton "Confirm":
                xalign 0.5
                yalign 1.00

                text_idle_color  "#271515"
                text_hover_color  "#642121"
                text_selected_color  "#398bce"
                action Return()


    
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
        

    


