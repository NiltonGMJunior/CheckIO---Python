FONT = ("--X--XXX-XXX-X-X-XXX--XX-XXX-XXX--XX-XX--"
        "-XX----X---X-X-X-X---X-----X-X-X-X-X-X-X-"
        "--X---XX--X--XXX-XX--XXX--X--XXX-XXX-X-X-"
        "--X--X-----X---X---X-X-X-X---X-X---X-X-X-"
        "--X--XXX-XXX---X-XX---XX-X---XXX-XX---XX-")

import numpy


def recognize(image):
    font_list = list(FONT)
    ref = numpy.zeros([len(font_list), len(font_list[0])])

    for i in range(len(font_list)):
        for j in range(len(font_list[0])):
            if font_list[i][j] == '-':
                ref[i][j] = 0
            else:
                ref[i][j] = 1

    ref_0 = ref[::, 36:40]
    ref_1 = ref[::, 0:4]
    ref_2 = ref[::, 4:8]
    ref_3 = ref[::, 8:12]
    ref_4 = ref[::, 12:16]
    ref_5 = ref[::, 16:20]
    ref_6 = ref[::, 20:24]
    ref_7 = ref[::, 24:28]
    ref_8 = ref[::, 28:32]
    ref_9 = ref[::, 32:36]

    print(ref_0)

    list_ref = [ref_0, ref_1, ref_2, ref_3, ref_4, ref_5, ref_6, ref_7, ref_8, ref_9]

    ref_image = numpy.asarray(image)

    msg = ''

    for i in range((len(image[0]) - 1) // 4):
        digit_start = 4 * i
        digit_end = 4 * i + 3
        ref_digit = ref_image[::, digit_start:digit_end + 1]
        min_error = 20
        curr = ''
        print(ref_digit)
        for j in list_ref:
            print(j)
            # diff = j - ref_digit
            # test = numpy.sum(diff)
            # if abs(test) < min_error:
            #    curr = str(i)

        msg += curr

    return msg


if __name__ == '__main__':
    image = [[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
             [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
             [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
             [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
             [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]

    print(recognize(image))
'''
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert recognize([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
                      [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                      [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                      [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                      [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "394 clear"
    assert recognize([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
                      [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                      [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                      [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                      [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "again 394 but with noise"

    print("Earn cool rewards by using the 'Check' button!")
'''