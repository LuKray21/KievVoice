from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

class MainWindow(App):
  def build(self):
    self.set_config()
    mainBox = BoxLayout(orientation = 'horizontal')
    # mainBox.add_widget(Button(size = (100, 10)))
    return mainBox
  
  def set_config(self):
    Config.set('graphics', 'width', '412')
    Config.set('graphics', 'height', '732')


