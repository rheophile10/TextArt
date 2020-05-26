from readletter import read_letter, alphabet


def parse_input(input_text):
    text_array=['', '', '', '', '', '', '']
    for text in input_text:
        big_char = read_letter(text).replace('\n', '')
        for line in range(0, 7):
            text_array[line] += big_char[line*8:(line+1)*8]
    return text_array


def parse_text_array(text_array):
    final_text = ''
    for text in text_array:
        final_text += text + '\n'
    return final_text


def main():
    x = 'welcome to text parser!\nenter text in '+alphabet+'and it will convert to ascii art\nenter \'quit\' to quit'
    print(x)
    while x.upper() != 'QUIT':
        x = input('enter text in '+alphabet+':')
        print(parse_text_array(parse_input(x)))
    print(parse_text_array(parse_input('Goodbye')))


if __name__ == '__main__':
    main()
