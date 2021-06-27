from kivy.app import App
from kivy.animation import Animation
from .view import MainWindow
from kivy.core.window import Window

# the purpose of this is to simulate smartphone screen size
Window.size = (320, 545)


class MainApp(App):
    title = 'Kivy To-do and Shopping List app'

    def build_config(self, config):
        config.setdefaults('kivy', {'keyboard_mode': ''})
        config.read('main.ini')

    def build(self):
        return MainWindow()

    def animate_menu_widget(self, widget, *args):
        anim = Animation(color=[1, 1, 1, 1], duration=.5)
        anim.bind(on_complete=self.reset)
        anim.start(widget)

    def reset(self, *args):
        widget = args[1]
        widget.background_color = background_color=(0,.35,0,.8)

    def on_pause(self):
        return True

    def on_resume(self):
        pass
