from kivy.app import App
from kivy.config import Config
from kivy.uix.button import Button

Config.set('graphics', 'borderless', '1')
Config.set('graphics', 'fullscreen', 'auto')



class MyApp(App):
    def build(self):
        return Button(text = "Кнопка 12",
                      font_size = 30,
                      background_color = [0, 1, 0, 1],
                      border = (20, 20, 20, 20)
                       )

if __name__ == "__main__":
    MyApp().run()
    
    