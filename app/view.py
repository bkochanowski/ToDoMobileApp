from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.modalview import ModalView
from kivy.garden.circulardatetimepicker import CircularTimePicker as CTP

from kivy.properties import StringProperty, NumericProperty

from kivy.metrics import sp, dp
from kivy.utils import rgba


class NewTask(ModalView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_time(self):
        mv = ModalView(.6, .7)
        cl = CTP()
        cl.bind(time=set_time)
        mv.add_widget(cl)
        mv.open()

    def set_time(self, inst, value):
        print(value)


class Task(ButtonBehavior, BoxLayout):
    """this class represent each new task added by the user"""
    name = StringProperty('')
    time = StringProperty('')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add_new(self):
        nt = NewTask()
        nt.open()
