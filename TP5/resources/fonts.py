import numpy as np

symbols1 = [
   # ' ', '!', '\"', '#', '$', '%', '&',
   #  '\'', '(', ')', '*', '+', ',', '-', '.',
     '/',
   '0', '1', '2', '3', '4', '5'
   # , '6', '7', '8', '9', ':', ';', '<', '=', '>', '?'
   ]

font1 = [
   #  [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],  # 0x20, space
   #  [0x04, 0x04, 0x04, 0x04, 0x04, 0x00, 0x04],  # 0x21, !
   #  [0x09, 0x09, 0x12, 0x00, 0x00, 0x00, 0x00],  # 0x22, "
   #  [0x0a, 0x0a, 0x1f, 0x0a, 0x1f, 0x0a, 0x0a],  # 0x23, #
   #  [0x04, 0x0f, 0x14, 0x0e, 0x05, 0x1e, 0x04],  # 0x24, $
   #  [0x19, 0x19, 0x02, 0x04, 0x08, 0x13, 0x13],  # 0x25, %
   # [0x04, 0x0a, 0x0a, 0x0a, 0x15, 0x12, 0x0d],  # 0x26, &
   #  [0x04, 0x04, 0x08, 0x00, 0x00, 0x00, 0x00],  # 0x27,
   #  [0x02, 0x04, 0x08, 0x08, 0x08, 0x04, 0x02],  # 0x28, (
   #  [0x08, 0x04, 0x02, 0x02, 0x02, 0x04, 0x08],  # 0x29, )
   #  [0x04, 0x15, 0x0e, 0x1f, 0x0e, 0x15, 0x04],  # 0x2a, *
   #  [0x00, 0x04, 0x04, 0x1f, 0x04, 0x04, 0x00],  # 0x2b, +
   #  [0x00, 0x00, 0x00, 0x00, 0x04, 0x04, 0x08],  # 0x2c, ,
   #  [0x00, 0x00, 0x00, 0x1f, 0x00, 0x00, 0x00],  # 0x2d, -
   #  [0x00, 0x00, 0x00, 0x00, 0x00, 0x0c, 0x0c],  # 0x2e, .
    [0x01, 0x01, 0x02, 0x04, 0x08, 0x10, 0x10],  # 0x2f, /
    [0x0e, 0x11, 0x13, 0x15, 0x19, 0x11, 0x0e],  # 0x30, 0
    [0x04, 0x0c, 0x04, 0x04, 0x04, 0x04, 0x0e],  # 0x31, 1
    [0x0e, 0x11, 0x01, 0x02, 0x04, 0x08, 0x1f],  # 0x32, 2
    [0x0e, 0x11, 0x01, 0x06, 0x01, 0x11, 0x0e],  # 0x33, 3
    [0x02, 0x06, 0x0a, 0x12, 0x1f, 0x02, 0x02],  # 0x34, 4
    [0x1f, 0x10, 0x1e, 0x01, 0x01, 0x11, 0x0e],  # 0x35, 5
   #  [0x06, 0x08, 0x10, 0x1e, 0x11, 0x11, 0x0e],  # 0x36, 6
   #  [0x1f, 0x01, 0x02, 0x04, 0x08, 0x08, 0x08],  # 0x37, 7
   #  [0x0e, 0x11, 0x11, 0x0e, 0x11, 0x11, 0x0e],  # 0x38, 8
   #  [0x0e, 0x11, 0x11, 0x0f, 0x01, 0x02, 0x0c],  # 0x39, 9
   #  [0x00, 0x0c, 0x0c, 0x00, 0x0c, 0x0c, 0x00],  # 0x3a, :
   #  [0x00, 0x0c, 0x0c, 0x00, 0x0c, 0x04, 0x08],  # 0x3b, ;
   #  [0x02, 0x04, 0x08, 0x10, 0x08, 0x04, 0x02],  # 0x3c, <
   #  [0x00, 0x00, 0x1f, 0x00, 0x1f, 0x00, 0x00],  # 0x3d, =
   #  [0x08, 0x04, 0x02, 0x01, 0x02, 0x04, 0x08],  # 0x3e, >
   #  [0x0e, 0x11, 0x01, 0x02, 0x04, 0x00, 0x04]   # 0x3f, ?
]


def get_parsed_fonts():
    fonts_parsed = []
    for i in range(len(font1)):
        current_font_list = []
        for j in range(len(font1[i])):
            num = font1[i][j]
            current_font_list.append([(num // 16) % 2, (num // 8) % 2, (num // 4) % 2, (num // 2) % 2, num % 2])
        current_font_np = np.array(current_font_list)
        fonts_parsed.append(current_font_np.flatten())
    return np.array(fonts_parsed)

rows = 7
cols = 5

def print_letters(alphabet):
   for i in range(len(alphabet)):
      for row in range(rows):
         row_str = '';
         for col in range(cols):
            if round(alphabet[i][row * cols + col]) == 1:
               row_str = row_str + '* '
            else:
               row_str = row_str + '  '
         print(row_str)
      print('--------------')

