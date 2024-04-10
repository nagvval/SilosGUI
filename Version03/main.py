import time
from kivy.app import App
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.graphics import Color, Ellipse, Rectangle, RoundedRectangle
from kivy.graphics.texture import Texture
from kivy.uix.label import Label
from kivy.uix.switch import Switch
from kivy.clock import Clock
from datetime import datetime
from threading import Thread

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

            #Шнек на котельню
            Color(1, 1, 1, 1)
            Rectangle(pos=(327, 115), size=(164, 20))
            Color(0, 0, 0, 1)
            Line(points=[327, 115, 327, 135, 491, 135, 491, 115, 327, 115], width=1.5)

            #Клапан на котельню
            Color(1, 1, 1, 1)
            Rectangle(pos=(327, 95), size=(40, 20))
            Color(0, 0, 0, 1)
            Line(points=[327, 95, 327, 115, 367, 115, 367, 95, 327, 95], width=1.5)

            #Шнек на пілету
            Color(1, 1, 1, 1)
            Rectangle(pos=(532, 115), size=(164, 20))
            Color(0, 0, 0, 1)
            Line(points=[532, 115, 532, 135, 696, 135, 696, 115, 532, 115], width=1.5)

            #Старт/стоп котельні
            Color(1, 1, 1, 1)
            Rectangle(pos=(319, 16), size=(56, 72))

            #Зображення котельні
            Rectangle(pos=(307, 9), size=(80, 80), source='3395582.png')

            #Старт/стоп пілети
            Color(1, 1, 1, 1)
            Rectangle(pos=(667, 24), size=(47, 37))

            #Зображення пілети
            Rectangle(pos=(636, -12), size=(120, 120), source='8395064.png')

            #Датчик підпору на шнеку котельні
            Color(1, 1, 1, 1)
            Ellipse(pos=(327, 141), size=(20, 20))
            Color(0, 0, 0, 1)
            Line(circle=(337, 151, 10), width=1.5)

            #Датчик підпору на шнеку пілети
            Color(1, 1, 1, 1)
            Ellipse(pos=(676, 141), size=(20, 20))
            Color(0, 0, 0, 1)
            Line(circle=(686, 151, 10), width=1.5)

            #Сигнал "STOP"
            Color(0, 1, 0, 1)
            Ellipse(pos=(161, 429), size=(75, 75))
            Color(0, 0, 0, 1)
            Line(circle=(198.5, 466.5, 37.5), width=1.5)
            Label(pos=(149, 417), text="STOP", font_size=25, color=(1, 1, 1, 1))

            #Напис "Останні 5 подій"
            last5process = Label(pos=(90, 300), text="Останні 5 подій", font_size=30, color=(0, 0, 0, 1))

            #Напис "Подія 1"
            self.process1 = Label(pos=(60, 250), text=" ", font_size=15, color=(0, 0, 0, 1))

            #Напис "Подія 2"
            self.process2 = Label(pos=(60, 225), text=" ", font_size=15, color=(0, 0, 0, 1))

            #Напис "Подія 3"
            self.process3 = Label(pos=(60, 200), text=" ", font_size=15, color=(0, 0, 0, 1))

            #Напис "Подія 4"
            self.process4 = Label(pos=(60, 175), text=" ", font_size=15, color=(0, 0, 0, 1))

            #Напис "Подія 5"
            self.process5 = Label(pos=(60, 150), text=" ", font_size=15, color=(0, 0, 0, 1))

            #Напис "Початок процесу"
            startProcess = Label(pos=(745, 424), text="Початок процесу", font_size=30, color=(0, 0, 0, 1))

            #Перемикач "Початок процесу"
            self.switch = Switch(active=False, pos=(750, 355))
            self.add_widget(self.switch)
            self.switch.bind(active=self.on_switch_active)

            self.switch.bind(active=self.on_switch_active)
            self.is_process_running = False

    def on_switch_active(self, instance, value):
        if value:
            # Виконати дії, коли відкладка увімкнена
            print("Switch is ON")
            current_time = datetime.now().strftime("%H:%M:%S")
            self.process5.text = self.process4.text
            self.process4.text = self.process3.text
            self.process3.text = self.process2.text
            self.process2.text = self.process1.text
            self.process1.text = f"{current_time} - Початок процесу"
            if not self.is_process_running:
                self.is_process_running = True
                t = Thread(target=self.run_process)
                t.start()
        else:
            # Виконати дії, коли відкладка вимкнена
            print("Switch is OFF")
            self.is_process_running = False

    def run_process(self):
        while self.is_process_running:
            # Ваш код для процесу, який повинен виконуватись у циклі
            print("1 sec")           
            time.sleep(.5)  # Затримка 1 секунда між ітераціями циклу

        # Код, що виконується після вимкнення процесу
        current_time = datetime.now().strftime("%H:%M:%S")
        self.process5.text = self.process4.text
        self.process4.text = self.process3.text
        self.process3.text = self.process2.text
        self.process2.text = self.process1.text
        self.process1.text = f"{current_time} - Кінець процесу"

            
            


class DrawRoundedRectanglesApp(App):
    def build(self):
        

        widget = RoundedRectangleWidget()
        widget.prepare()
        #kvrect = Builder.load_string(kv)
        #widget.add_widget(kvrect)
        return widget

if __name__ == "__main__":
    DrawRoundedRectanglesApp().run()