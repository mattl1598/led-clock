from PIL import Image, ImageDraw, ImageFilter
import colorsys as colour_sys
import numpy


def hsv_to_rgb(h, s, v):
	return tuple(round(i * 255) for i in colour_sys.hsv_to_rgb(h/360, s, v))


def rgb_to_hex(rgb: numpy.ndarray) -> str:
	rgb = rgb.reshape(3)
	return '#{:02X}{:02X}{:02X}'.format(*rgb)


def make_rainbow():
	points = []

	for i in range(0, 361):
		points.append(i)

	colours = []

	for point in points:
		colours.append(hsv_to_rgb(point, 0.65, 1))

	img = Image.new(mode="RGB", size=(3600, 1260,))

	draw = ImageDraw.Draw(img, mode="RGB")

	for x in range(len(colours)):
		draw.rectangle([x*10, 0, x*10 + 10, 1260], fill=colours[x], width=0)

	img1 = img.filter(ImageFilter.GaussianBlur)

	# img1.show()

	return img1


def row_zero(img):
	d = img.width // 20
	r = img.width // 40
	y = r
	start_x = (img.width // 2) - 8*d

	row = []

	for i in range(0, 17):
		imgx = img.crop((start_x + (i*d), y-r, start_x + (i+1)*d, y+r))
		array = numpy.asarray(imgx)
		avg_color_per_row = numpy.average(array, axis=0)
		avg_color = numpy.average(avg_color_per_row, axis=0).astype(numpy.int64)
		new_hex = rgb_to_hex(avg_color)
		row.append(new_hex)

	return row


def row_one(img):
	d = img.width // 20
	r = img.width // 40
	y = 3*r
	start_x = (img.width // 2) - 8*d - r

	row = []

	for i in range(0, 18):
		imgx = img.crop((start_x + (i*d), y-r, start_x + (i+1)*d, y+r))
		array = numpy.asarray(imgx)
		avg_color_per_row = numpy.average(array, axis=0)
		avg_color = numpy.average(avg_color_per_row, axis=0).astype(numpy.int64)
		new_hex = rgb_to_hex(avg_color)
		row.append(new_hex)

	return row


def row_two(img):
	d = img.width // 20
	r = img.width // 40
	y = 5*r
	start_x = (img.width // 2) - 9*d

	row = []

	for i in range(0, 19):
		imgx = img.crop((start_x + (i*d), y-r, start_x + (i+1)*d, y+r))
		array = numpy.asarray(imgx)
		avg_color_per_row = numpy.average(array, axis=0)
		avg_color = numpy.average(avg_color_per_row, axis=0).astype(numpy.int64)
		new_hex = rgb_to_hex(avg_color)
		row.append(new_hex)

	return row


def row_three(img):
	row = []
	d = img.width // 20
	r = img.width // 40
	middle = 7*r

	for i in range(0, 20):
		imgx = img.crop(((i*d), middle-r, (i+1)*d, middle+r))
		array = numpy.asarray(imgx)
		avg_color_per_row = numpy.average(array, axis=0)
		avg_color = numpy.average(avg_color_per_row, axis=0).astype(numpy.int64)
		hex = rgb_to_hex(avg_color)
		row.append(hex)
		# print(hex)

	return row


def row_four(img):
	d = img.width // 20
	r = img.width // 40
	y = 9*r
	start_x = (img.width // 2) - 9*d

	row = []

	for i in range(0, 19):
		imgx = img.crop((start_x + (i*d), y-r, start_x + (i+1)*d, y+r))
		array = numpy.asarray(imgx)
		avg_color_per_row = numpy.average(array, axis=0)
		avg_color = numpy.average(avg_color_per_row, axis=0).astype(numpy.int64)
		new_hex = rgb_to_hex(avg_color)
		row.append(new_hex)

	return row


def row_five(img):
	d = img.width // 20
	r = img.width // 40
	y = 11*r
	start_x = (img.width // 2) - 8*d - r

	row = []

	for i in range(0, 18):
		imgx = img.crop((start_x + (i*d), y-r, start_x + (i+1)*d, y+r))
		array = numpy.asarray(imgx)
		avg_color_per_row = numpy.average(array, axis=0)
		avg_color = numpy.average(avg_color_per_row, axis=0).astype(numpy.int64)
		new_hex = rgb_to_hex(avg_color)
		row.append(new_hex)

	return row


def row_six(img):
	d = img.width // 20
	r = img.width // 40
	y = 13*r
	start_x = (img.width // 2) - 8*d
	print(y+r)

	row = []

	for i in range(0, 17):
		imgx = img.crop((start_x + (i*d), y-r, start_x + (i+1)*d, y+r))
		array = numpy.asarray(imgx)
		avg_color_per_row = numpy.average(array, axis=0)
		avg_color = numpy.average(avg_color_per_row, axis=0).astype(numpy.int64)
		new_hex = rgb_to_hex(avg_color)
		row.append(new_hex)

	return row
