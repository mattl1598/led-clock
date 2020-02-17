import tkinter
import clockscript


class Clock:

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Test")
        self.root.geometry("1000x400")

        self.bg = "#bbbbbb"
        self.fg = "#dd0000"
        self.colours = gen_solid_bg(self.bg)
        self.back = gen_solid_bg(self.bg)

        # circles
        self.root.canvas = tkinter.Canvas(self.root, width=1000, height=400)
        self.root.canvas.pack()

        self.r = 22
        self.last_time = "0000"
        # r = self.r
        self.circles = [[], [], [], [], [], [], []]
        self.draw_circles2()

        self.run_clock()

        self.root.mainloop()

    def draw_circles2(self):
        r = self.r
        array = [17, 18, 19, 20, 19, 18, 17]

        row = 0 - (len(array) // 2)
        for i in range(len(array)):
            y = 200 + (38 * row)
            x = 500
            if row % 2 != 0:
                circle = 0 - (array[i] // 2)
                for j in range(array[i]):
                    self.circles[i].append(tkinter.Canvas.create_oval(self.root.canvas, gen_bbox((circle * 45) + x, y, r)))
                    circle += 1
            else:
                circle = 0 - array[i] // 2
                for k in range(array[i]):
                    self.circles[i].append(tkinter.Canvas.create_oval(self.root.canvas, gen_bbox((circle * 45) + x + 23, y, r)))
                    circle += 1
            row += 1

    def run_clock(self):
        self.get_colours()
        self.apply_colours()

        self.root.after(1000, self.run_clock)

    def get_colours(self):
        self.colours, self.last_time = clockscript.colour_clock(self.colours, self.fg, self.back, self.last_time)

    def apply_colours(self):
        for i in range(len(self.circles)):
            for j in range(len(self.circles[i])):
                self.root.canvas.itemconfig(self.circles[i][j], fill=self.colours[i][j])


def gen_solid_bg(bg):
    array = [17, 18, 19, 20, 19, 18, 17]
    colours = []
    for i in array:
        list = []
        for j in range(i):
            list.append(bg)
        colours.append(list)

    return colours


def gen_bbox(x, y, r):
    x1 = x - r
    y1 = y - r
    x2 = x + r
    y2 = y + r
    return x1, y1, x2, y2


if __name__ == '__main__':
    window = Clock()
    a = 0
    for i in [17, 18, 19, 20, 19, 18, 17]:
        a += i
        print(a)

