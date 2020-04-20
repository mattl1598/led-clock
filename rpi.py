import clockscript
import neopixel
import board
import itertools
import webcolors as webcolours
import time

def gen_solid_bg(bg):
	array = [17, 18, 19, 20, 19, 18, 17]
	colours = []
	for i in array:
		list = []
		for j in range(i):
			list.append(bg)
		colours.append(list)

	return colours


def setup():
	last_time = "0000"
	bg = "#bbbbbb"
	fg = "#ffffff"

	colours = gen_solid_bg(bg)
	back = gen_solid_bg(bg)

	pixels = neopixel.NeoPixel(board.D18, 128, auto_write=False)

	return last_time, bg, fg, colours, back, pixels


if __name__ == '__main__':
	last_time, bg, fg, colours, back, pixels = setup()
	while True:
		t1 = time.perf_counter()
		colours, last_time = clockscript.colour_clock(colours, fg, back, last_time)
		colours_list = list(itertools.chain.from_iterable(colours))
		for i in range(len(colours_list)):
			pixels[i] = webcolours.hex_to_rgb(colours_list[i])
		pixels.show()
		print(time.perf_counter() - t1)
		time.sleep(1000)