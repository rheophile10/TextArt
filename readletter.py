import os

font_file = os.path.join(os.getcwd(), 'TextArt\\alphabet.txt')

with open(font_file, 'r') as f:
    alphabet_txt = f.read().replace('\n', '').replace('_', ' ')

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '

lw = 8  # letter width is 8 (includes space)
lh = 7  # letter height is 7

line_width = len(alphabet)*lw


def start(letter):
    return alphabet.find(letter.upper()) * lw


def bracket(l, lstart):
    line_start = lstart + l * line_width
    line_end = line_start + lw
    return line_start, line_end


def line(line_start, line_end):
    return alphabet_txt[line_start:line_end]+'\n'


def read_letter(letter):
    if letter.upper() not in alphabet:
        print("uppercase character \'"+letter+"\' is not in "+alphabet)
    else:
        lstart = start(letter)
        art_letter = ''
        for l in range(0, lh):
            line_start, line_end = bracket(l, lstart)
            art_letter += line(line_start, line_end)
        return art_letter



