input.onButtonPressed(Button.A, function () {
    if (Math.randomBoolean()) {
        if (true) {
            for (let index = 0; index <= 3; index++) {
                basic.showNumber(3 - index)
                basic.showLeds(`
                    . . . . .
                    . . . . .
                    . . # . .
                    . . . . .
                    . . . . .
                    `)
                basic.showLeds(`
                    . . . . .
                    . . # . .
                    . # . # .
                    . . # . .
                    . . . . .
                    `)
                basic.showLeds(`
                    . . # . .
                    . # . # .
                    # . . . #
                    . # . # .
                    . . # . .
                    `)
                basic.showLeds(`
                    . # . # .
                    # . . . #
                    . . . . .
                    # . . . #
                    . # . # .
                    `)
                basic.showLeds(`
                    # . . . #
                    . . . . .
                    . . . . .
                    . . . . .
                    # . . . #
                    `)
            }
        }
        if (false) {
            led.stopAnimation()
        }
    }
})
input.onButtonPressed(Button.B, function () {
    while (true) {
        basic.showNumber(0)
    }
})
