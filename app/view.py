from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty, NumericProperty

from kivy.metrics import sp, dp
from kivy.utils import rgba


class Task(BoxLayout):
    """this class represent each new task added by the user"""
    name = StringProperty('')
    time = StringProperty('')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MainWindow(BoxLayout):
    pass
