# encoding = utf-8


from tkinter import *
import random

# 一個座標
class Point(object):
    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def ps(self):
        print("(%.2lf, %.2lf)" % (self.x, self.y))

class Box(object):

	def __init__(self, mean, boxUpper, boxlower, lineupper, linelower, canvas, width = 10):
		self.mean = mean
		self.boxUpper = boxUpper
		self.boxlower = boxlower
		self.lineupper = lineupper
		self.linelower = linelower
		self.canvas = canvas
		self.width = width

	def draw(self):
		lup = Point(self.mean.x - self.width,self.mean.y - self.boxUpper)
		# box 右下
		ldp = Point(self.mean.x + self.width, self.mean.y + self.boxlower)
		# box
		self.canvas.create_rectangle(lup.x, lup.y, ldp.x, ldp.y)

		# 上面那條線
		self.canvas.create_line(lup.x, lup.y - self.lineupper, lup.x + 2 * self.width, lup.y - self.lineupper)
		# 下面那條線
		self.canvas.create_line(ldp.x - 2 * self.width, ldp.y + self.linelower, ldp.x, ldp.y + self.linelower)

		# 上面那條線跟box距離
		self.canvas.create_line(self.mean.x, lup.y, self.mean.x, lup.y - self.lineupper)

		# 下面那條線跟box 距離
		self.canvas.create_line(self.mean.x, ldp.y, self.mean.x, ldp.y + self.linelower)

class BoxPlot(object):

	# 1 p = 50
	def __init__(self, scale = 50):
		self.cartori = Point(50,650)
		self.scale = scale
		#self.initCanvas()

	def locationTranslation(self, target):
		return Point( self.cartori.x + target.x  * self.scale, self.cartori.y - target.y * self.scale)

	def initCanvas(self, root):
		#self.root = root
		#self.root.geometry("1000x1000")
		self.canvas = Canvas(root)
		self.canvas['width'] = 1000
		self.canvas['height'] = 1000
		self.canvas.pack()


	def draw(self):
		# y 軸
		self.canvas.create_line((50, 50, 50, 650),width = 2)
		xmax = 100
		splitx = 10
		ymax = 100
		splity = 10

		for x in range(0, 110 , int(xmax / splitx)):
			lat = self.locationTranslation(Point(-0.5, x / self.scale * 5.8))
			self.canvas.create_text(lat.x,lat.y ,text=str(float(x)))

		for y in range(0, 110 , int(ymax / splity)):
			lat = self.locationTranslation(Point(y / self.scale * 5.8, -0.5))
			self.canvas.create_text(lat.x, lat.y ,text=str(float(y)))

		# x 軸
		self.canvas.create_line((50, 650, 650, 650),width = 2)
		for i in range(1, 10):
			Box(self.locationTranslation(Point(i, i)), random.random() * 40, random.random() * 40, random.random() * 40, random.random() * 40, self.canvas, 10).draw()




def main():
	root = Tk()
	root.geometry("1000x1000")

	bp = BoxPlot()
	bp.initCanvas(root)
	bp.draw()

	root.mainloop()






if __name__ == "__main__":
	main()