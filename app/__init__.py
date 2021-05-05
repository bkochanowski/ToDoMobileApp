from kivy.app import App
from .view import MainWindow
from kivy.core.window import Window

#the purpose of this is to simulate smartphone screen size
Window.size = (320, 545)


class MainApp(App):
    title = 'Kivy To-do and Shopping List app'

    def build(self):
        return MainWindow()
