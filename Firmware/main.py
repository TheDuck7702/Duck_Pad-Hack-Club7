import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.RGB import RGB

keyboard = KMKKeyboard()

#define switch pins
button_pins = [
    board.GP1,  # Switch 1
    board.GP2,  # Switch 2
    board.GP4,  # Switch 3
    board.GP3,  # Switch 4
    board.GP0,  # Switch 5
    board.GP7,  # Switch 6
]
keyboard.matrix = KeysScanner(pins=button_pins, value_when_pressed=False)

# Rotary encoder
encoder = EncoderHandler()
keyboard.modules.append(encoder)
encoder.pins = [(board.GP28, board.GP29)]  # CLK, DT
encoder.map = [(KC.VOLD, KC.VOLU)]         # counterclockwise, clockwise

#lights
rgb = RGB(
    pixel_pin=board.GP6,
    num_pixels=2,
    hue_default=0,
    sat_default=255,
    val_default=80
)
keyboard.extensions.append(rgb)

# Keymap
keyboard.keymap = [[

    KC.A,
    KC.B,
    KC.C,

    KC.D,
    KC.E,
    KC.F,
    
]]

# im so confuzed
if __name__ == '__main__':
    keyboard.go()
