from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.uix.modalview import ModalView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.garden.circulardatetimepicker import CircularTimePicker as CTP

from kivy.properties import ObjectProperty, StringProperty, NumericProperty

from kivy.metrics import sp, dp
from kivy.utils import rgba

class NewTask(ModalView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_time(self):
        mv = ModalView(size_hint=[.8, .6])
        box = BoxLayout(orientation='vertical')
        mv.add_widget(box)

        cl = CTP(color=[1, 1, 1, 1])
        cl.bind(time=self.set_time)

        submit = Button(text='Zapisz', background_normal='',
                        color=[0, .3, 0, .7], background_color=[1, 1, 1, 1], size_hint_y=.2)
        submit.bind(on_release=lambda x: self.update_time(cl.time, mv))
        box.add_widget(cl)
        box.add_widget(submit)
        mv.open()

    def set_time(self, inst, value):
        print(value)

    def update_time(self, time, mv):
        mv.dismiss()
        self.ids.task_time.text = str(time)


class NewButton(ButtonBehavior, BoxLayout):
    pass


class Task(ButtonBehavior, BoxLayout):
    """this class represent each new task added by the user"""
    name = StringProperty('')
    details = StringProperty('')
    time = StringProperty('')
    date = StringProperty('')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ItemToBuy(ButtonBehavior, BoxLayout):
    """this class represent each new task added by the user"""
    item_name = StringProperty('')
    quantity = NumericProperty('')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MainWindow(BoxLayout):
    pass


class TaskScreen(Screen):
    def __init__(self, **kwargs):
        super(TaskScreen, self).__init__(**kwargs)

    def add_new(self):
        nt = NewTask()
        nt.open()

    def add_task(self, mv, xtask: tuple):
        error = False
        scroll_parent = self.ids.scroll_parent
        uw = self.ids.upcoming_wrapper
        for t in xtask:
            if len(t.text) < 3:
                t.hint_text = '**Pole wymagane**'
                t.hint_text_color = [1, 0, 0, 1]
                error = True

        if error:
            pass
        else:
            task = Task()
            task.name = xtask[0].text
            task.details = xtask[1].text
            task.time = xtask[2].text
            task.date = xtask[3].text
            task.size_hint = [None, None]
            task.size = [scroll_parent.width / 1.5, scroll_parent.height -
                         (.050 * scroll_parent.height)]

            uw.add_widget(task)
            mv.dismiss()


class ShoppingScreen(Screen):
    pass
