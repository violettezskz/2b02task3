def on_button_pressed_a():
    if Math.random_boolean():
        if True:
            for index in range(4):
                basic.show_number(3 - index)
                basic.show_leds("""
                    . . . . .
                                        . . . . .
                                        . . # . .
                                        . . . . .
                                        . . . . .
                """)
                basic.show_leds("""
                    . . . . .
                                        . . # . .
                                        . # . # .
                                        . . # . .
                                        . . . . .
                """)
                basic.show_leds("""
                    . . # . .
                                        . # . # .
                                        # . . . #
                                        . # . # .
                                        . . # . .
                """)
                basic.show_leds("""
                    . # . # .
                                        # . . . #
                                        . . . . .
                                        # . . . #
                                        . # . # .
                """)
                basic.show_leds("""
                    # . . . #
                                        . . . . .
                                        . . . . .
                                        . . . . .
                                        # . . . #
                """)
        if False:
            led.stop_animation()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    while True:
        basic.show_number(0)
input.on_button_pressed(Button.B, on_button_pressed_b)
