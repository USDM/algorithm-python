import tkinter as tk
class Point:
  def __init__(self, x,y):
    self.x=x
    self.y=y

class BresenhamCircle:

  def draw_circle(self, canvas, center=Point(0,0), radius=1):
    self._canvas = canvas
    self._center = center
    self._radius = radius
    x=0
    y=radius
    d_current = 3 - 2*radius
    point_current = Point(x,y)
    while point_current.x < point_current.y:
      if d_current < 0:
        d_current = d_current + 4*point_current.x + 6
        point_current.x += 1
      elif 0 <= d_current:
        d_current = d_current + 4*(point_current.x-point_current.y)+10
        point_current.x += 1
        point_current.y -= 1
      self._plot_point(Point(center.x+point_current.x, center.y+point_current.y)); 
      self._plot_point(Point(center.x-point_current.x, center.y+point_current.y)); 
      self._plot_point(Point(center.x+point_current.x, center.y-point_current.y)); 
      self._plot_point(Point(center.x-point_current.x, center.y-point_current.y)); 
      self._plot_point(Point(center.x+point_current.y, center.y+point_current.x)); 
      self._plot_point(Point(center.x-point_current.y, center.y+point_current.x)); 
      self._plot_point(Point(center.x+point_current.y, center.y-point_current.x)); 
      self._plot_point(Point(center.x-point_current.y, center.y-point_current.x)); 

  def _plot_point(self, point):
    self._canvas.create_line(point.x, point.y, point.x + 1, point.y, fill="black")


ventana = tk.Tk()
ventana.title("CIRCULO")
canvas = tk.Canvas(ventana, width=400, height=400)
canvas.pack()
bresenhamCircle = BresenhamCircle() 
bresenhamCircle.draw_circle(canvas,center=Point(200,200), radius=100)
ventana.mainloop()
