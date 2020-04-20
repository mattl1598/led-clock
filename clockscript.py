import time
import backgrounds

def colour_number(circles, place, number, colour):
    first = [0, 1, 1, 1, 1, 1, 0]
    second = [4, 5, 5, 5, 5, 5, 4]
    third = [10, 11, 11, 11, 11, 11, 10]
    fourth = [14, 15, 15, 15, 15, 15, 14]
    if place == 1:
        start = first
    elif place == 2:
        start = second
    elif place == 3:
        start = third
    else:
        start = fourth

    one = [[0, 0, 0], [0, 1, 0], [0, 1, 0], [0, 0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 0, 0]]
    two = [[0, 0, 0], [1, 1, 0], [0, 0, 1], [0, 1, 1, 0], [1, 0, 0], [1, 1, 0], [0, 0, 0]]
    three = [[0, 0, 0], [1, 1, 0], [0, 0, 1], [0, 1, 1, 0], [0, 0, 1], [1, 1, 0], [0, 0, 0]]
    four = [[0, 0, 0], [1, 0, 1], [1, 0, 1], [0, 1, 1, 0], [0, 0, 1], [0, 1, 0], [0, 0, 0]]
    five = [[0, 0, 0], [1, 1, 0], [1, 0, 0], [0, 1, 1, 0], [0, 0, 1], [1, 1, 0], [0, 0, 0]]
    six = [[0, 0, 0], [1, 1, 0], [1, 0, 0], [0, 1, 1, 0], [1, 0, 1], [1, 1, 0], [0, 0, 0]]
    seven = [[0, 0, 0], [1, 1, 1], [0, 0, 1], [0, 1, 1, 1], [0, 1, 0], [1, 0, 0], [0, 0, 0]]
    eight = [[0, 0, 0], [1, 1, 0], [1, 0, 1], [0, 1, 1, 0], [1, 0, 1], [1, 1, 0], [0, 0, 0]]
    nine = [[0, 0, 0], [1, 1, 0], [1, 0, 1], [0, 1, 1, 0], [0, 0, 1], [1, 1, 0], [0, 0, 0]]
    zero = [[0, 0, 0], [1, 1, 0], [1, 0, 1], [1, 0, 0, 1], [1, 0, 1], [1, 1, 0], [0, 0, 0]]

    numbers = {1: one, 2: two, 3: three, 4: four, 5: five, 6: six, 7: seven, 8: eight, 9: nine, 0: zero}
    pattern = numbers[number]

    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            if pattern[i][j] == 1:
                circles[i][j + start[i]] = colour

    return circles


def colour_colon(circles, colour):
    circles[2][9] = colour
    circles[4][9] = colour

    return circles

def colour_background(circles):
    for x in range(len(circles)):
        for y in range(len(circles[x])):
            circles[x][y] = "#bbbbbb"

    img = backgrounds.make_rainbow()
    circles[0] = backgrounds.row_zero(img)
    circles[1] = backgrounds.row_one(img)
    circles[2] = backgrounds.row_two(img)
    circles[3] = backgrounds.row_three(img)
    circles[4] = backgrounds.row_four(img)
    circles[5] = backgrounds.row_five(img)
    circles[6] = backgrounds.row_six(img)

    return circles


def colour_clock(circles, colour, bg, last_time):
    hours = str(time.localtime(time.time())[3]).zfill(2)
    mins = str(time.localtime(time.time())[4]).zfill(2)
    if last_time != hours + mins:
        circles = colour_background(circles)

        last_time = hours + mins

        circles = colour_colon(circles, colour)

        circles = colour_number(circles, 1, int(hours[0]), colour)
        circles = colour_number(circles, 2, int(hours[1]), colour)
        circles = colour_number(circles, 3, int(mins[0]), colour)
        circles = colour_number(circles, 4, int(mins[1]), colour)

    return circles, last_time
