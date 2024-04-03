from kivy.app import App
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.graphics import Color, Ellipse, Rectangle, RoundedRectangle
from kivy.graphics.texture import Texture
from kivy.lang import Builder

Config.set('graphics', 'borderless', '1')
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'always_on_top', '1')
#Config.set('graphics', 'fullscreen', 'auto')

class RoundedRectangleWidget(Widget):
    def prepare(self):
        with self.canvas:
            #Фон
            Color(0.97, 0.89, 0.5)
            Rectangle(pos=(0, 0), size=(1024, 600))
            
            #Корпус
            Color(0.3333333333333333, 0.5607843137254, 0.5490196078431373, 1)
            Rectangle(pos=(436, 149), size=(150, 300))
            Color(0, 0, 0, 1)
            Line(points=[436, 149, 436, 449, 586, 449, 586, 149, 436, 149], width=2)

            #Дах
            Color(0.3333333333333333, 0.5607843137254, 0.5490196078431373, 1)
            Triangle(points=[436, 449, 511, 555, 586, 449])
            Color(0, 0, 0, 1)
            Line(points=[436, 449, 511, 555, 586, 449, 436, 449], width=2)

            #Вібратори
            Color(1, 1, 1, 1)
            RoundedRectangle(pos=((1024/2)-(85/2), 449), radius=[20, 20, 0, 0], size=(85, 40))
            Color(0, 0, 0, 1)
            Line(points=[(1024/2)-(85/2), 449, (1024/2)-(85/2), 469], width=1.5)
            Line(circle=((1024/2)-((85/2)-20), 469, 20, 360, 270), width=1.5)
            Line(points=[(1024/2)-(85/2-20), 489, (1024/2)+(85/2-20), 489], width=1.5)
            Line(circle=((1024/2)+((85/2)-20), 469, 20, 90, 0), width=1.5)
            Line(points=[(1024/2)+(85/2), 449, (1024/2)+(85/2), 469], width=1.5)

            #Рівень силоса верхній
            Color(1, 1, 1, 1)
            Ellipse(pos=(491, 376), size=(40, 40))
            Color(0, 0, 0, 1)
            Line(circle=((1024/2), 396, 20), width=1.5)

            #Рівень силоса сереній
            Color(1, 1, 1, 1)
            Ellipse(pos=(491, 299), size=(40, 40))
            Color(0, 0, 0, 1)
            Line(circle=((1024/2), 319, 20), width=1.5)

            #Рівень силоса нижній
            Color(1, 1, 1, 1)
            Ellipse(pos=(491, 222), size=(40, 40))
            Color(0, 0, 0, 1)
            Line(circle=((1024/2), 242, 20), width=1.5)

            #Готвальд 1
            Color(1, 1, 1, 1)
            Rectangle(pos=(491, 111), size=(41, 81))
            Color(0, 0, 0, 1)
            Line(points=[491, 111, 491, 192, 532, 192, 532, 111, 491, 111], width=1.5)

            #Готвальд 2 шнек
            Color(1, 1, 1, 1)
            Rectangle(pos=(443, 156), size=(68, 12))
            Color(0, 0, 0, 1)
            Line(points=[443, 156, 443, 168, 511, 168, 511, 156, 443, 156], width=1.5)

            #Готвальд 2 вигрузка
            Color(1, 1, 1, 1)
            Triangle(points=[491, 111, 532, 111, (1024/2), 70])
            Color(0, 0, 0, 1)
            Line(points=[491, 111, 532, 111, (1024/2), 70, 491, 111], width=1.5)

            


class DrawRoundedRectanglesApp(App):
    def build(self):
        

        widget = RoundedRectangleWidget()
        widget.prepare()
        #kvrect = Builder.load_string(kv)
        #widget.add_widget(kvrect)
        return widget

if __name__ == "__main__":
    DrawRoundedRectanglesApp().run()