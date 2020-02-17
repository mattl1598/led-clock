import tkinter
from random import randint
import time

class Clock:

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Test")
        self.root.geometry("1000x400")

        self.bg = "#ff0000"
        self.fg = "black"

        # circles
        self.root.canvas = tkinter.Canvas(self.root, width=1000, height=400)
        self.root.canvas.pack()

        self.r = 20
        self.last_time = "0000"
        # r = self.r
        self.circles = [[], [], [], [], [], [], []]
        self.draw_circles2()
        self.colour_clock()

        self.root.mainloop()

    def draw_circles(self):
        r = self.r
        array = [17, 18, 19, 20, 19, 18, 17]
        row = 0 - (len(array) // 2)
        for i in range(len(array)):
            y = 200 + (50 * row)
            x = 500
            if row % 2 != 0:
                circle = 0 - (array[i] // 2)
                for j in range(array[i]):
                    self.root.canvas.create_oval(gen_bbox((circle * 50) + x, y, r))
                    circle += 1
            else:
                circle = 0 - array[i] // 2
                for k in range(array[i]):
                    self.root.canvas.create_oval(gen_bbox((circle * 50) + x + 25, y, r), fill="red")
                    circle += 1
            row += 1

    def draw_circles2(self):
        r = self.r
        array = [17, 18, 19, 20, 19, 18, 17]

        row = 0 - (len(array) // 2)
        for i in range(len(array)):
            y = 200 + (50 * row)
            x = 500
            if row % 2 != 0:
                circle = 0 - (array[i] // 2)
                for j in range(array[i]):
                    self.circles[i].append(tkinter.Canvas.create_oval(self.root.canvas, gen_bbox((circle * 50) + x, y, r), fill=self.bg))
                    circle += 1
            else:
                circle = 0 - array[i] // 2
                for k in range(array[i]):
                    self.circles[i].append(tkinter.Canvas.create_oval(self.root.canvas, gen_bbox((circle * 50) + x + 25, y, r), fill=self.bg))
                    circle += 1
            row += 1

    def colour_colon(self):
        self.root.canvas.itemconfig(self.circles[2][9], fill=self.fg)
        self.root.canvas.itemconfig(self.circles[4][9], fill=self.fg)


    def colour_number(self, place, number):

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

        one = [[0,0,0], [0,1,0], [0,1,0], [0,0,1,0], [0,1,0], [0,1,0], [0,0,0]]
        two = [[0,0,0], [1,1,0], [0,0,1], [0,1,1,0], [1,0,0], [1,1,0], [0,0,0]]
        three = [[0,0,0], [1,1,0], [0,0,1], [0,1,1,0], [0,0,1], [1,1,0], [0,0,0]]
        four = [[0,0,0], [1,0,1], [1,0,1], [0,1,1,0], [0,0,1], [0,1,0], [0,0,0]]
        five = [[0,0,0], [1,1,0], [1,0,0], [0,1,1,0], [0,0,1], [1,1,0], [0,0,0]]
        six = [[0,0,0], [1,1,0], [1,0,0], [0,1,1,0], [1,0,1], [1,1,0], [0,0,0]]
        seven = [[0,0,0], [1,1,1], [0,0,1], [0,1,1,1], [0,1,0], [1,0,0], [0,0,0]]
        eight = [[0,0,0], [1,1,0], [1,0,1], [0,1,1,0], [1,0,1], [1,1,0], [0,0,0]]
        nine = [[0,0,0], [1,1,0], [1,0,1], [0,1,1,0], [0,0,1], [1,1,0], [0,0,0]]
        zero = [[0,0,0], [1,1,0], [1,0,1], [1,0,0,1], [1,0,1], [1,1,0], [0,0,0]]

        numbers = {1: one, 2: two, 3: three, 4: four, 5: five, 6: six, 7: seven, 8: eight, 9: nine, 0: zero}
        pattern = numbers[number]

        for i in range(len(pattern)):
            for j in range(len(pattern[i])):
                if pattern[i][j] == 1:
                    self.root.canvas.itemconfig(self.circles[i][j+start[i]], fill=self.fg)
                else:
                    self.root.canvas.itemconfig(self.circles[i][j+start[i]], fill=self.bg)

    def colour_clock(self):

        hours = str(time.localtime(time.time())[3]).zfill(2)
        mins = str(time.localtime(time.time())[4]).zfill(2)
        if self.last_time != hours + mins:

            self.last_time = hours + mins

            self.colour_colon()

            self.colour_number(1, int(hours[0]))
            self.colour_number(2, int(hours[1]))
            self.colour_number(3, int(mins[0]))
            self.colour_number(4, int(mins[1]))

        self.root.after(1000, self.colour_clock)




def gen_bbox(x, y, r):
    x1 = x - r
    y1 = y - r
    x2 = x + r
    y2 = y + r
    return x1, y1, x2, y2


if __name__ == '__main__':
    window = Clock()


"""
[17, 18, 19, 20, 19, 18, 17]
# 7 high
17
18
19
20
19
18
17

"""