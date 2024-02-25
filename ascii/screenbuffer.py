import pygame

CELL_WIDTH = 16
CELL_HEIGHT = 24
CELL_COLUMNS = 32
CELL_ROWS = 16
CELL_COUNT = CELL_ROWS * CELL_COLUMNS
BORDER_X = 64
BORDER_Y = 48
SCREEN_WIDTH = CELL_WIDTH * CELL_COLUMNS + BORDER_X * 2
SCREEN_HEIGHT = CELL_HEIGHT * CELL_ROWS + BORDER_Y * 2

AREAS = [pygame.Rect((i % 32) * CELL_WIDTH, (i // 32) * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT) for i in range(256)]
DESTINATIONS = [((i % 32) * CELL_WIDTH + BORDER_X, (i // 32) * CELL_HEIGHT + BORDER_Y) for i in range(CELL_COUNT)]
CHARACTER_TABLE = {
    "@": 64,
    "A": 65,
    "B": 66,
    "C": 67,
    "D": 68,
    "E": 69,
    "F": 70,
    "G": 71,
    "H": 72,
    "I": 73,
    "J": 74,
    "K": 75,
    "L": 76,
    "M": 77,
    "N": 78,
    "O": 79,
    "P": 80,
    "Q": 81,
    "R": 82,
    "S": 83,
    "T": 84,
    "U": 85,
    "V": 86,
    "W": 87,
    "X": 88,
    "Y": 89,
    "Z": 90,
    "[": 91,
    "\\": 92,
    "]": 93,
    " ": 96,
    "!": 97,
    "\"": 98,
    "#": 99,
    "$": 100,
    "%": 101,
    "&": 102,
    "'": 103,
    "(": 104,
    ")": 105,
    "*": 106,
    "+": 107,
    ",": 108,
    "-": 109,
    ".": 110,
    "/": 111,
    "0": 112,
    "1": 113,
    "2": 114,
    "3": 115,
    "4": 116,
    "5": 117,
    "6": 118,
    "7": 119,
    "8": 120,
    "9": 121,
    ":": 122,
    ";": 123,
    "<": 124,
    "=": 125,
    ">": 126,
    "?": 127,
}
screen_buffer = [CHARACTER_TABLE[" "] for i in range(CELL_COUNT)]


def clear(value):
    for index in range(CELL_COUNT):
        screen_buffer[index] = value


def clear_character(character):
    clear(CHARACTER_TABLE[character])


def put(index, value):
    screen_buffer[index] = value


def put_block(column, row, color, flags):
    put(column + row * CELL_COLUMNS, 128 + color * 16 + flags)


def write(index, text):
    for char in text:
        put(index, CHARACTER_TABLE[char])
        index += 1
        index %= CELL_COUNT


clear_character(" ")