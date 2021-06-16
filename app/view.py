from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.uix.modalview import ModalView
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.animation import Animation

from kivy.garden.circulardatetimepicker import CircularTimePicker as CTP

from kivy.properties import StringProperty, ObjectProperty

from kivy.metrics import sp, dp
from app.storage.db import Database


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
                        color=[0, .3, 0, .7], background_color=[1, 1, 1, 1], size_hint_y=.15)
        submit.bind(on_release=lambda x: self.update_time(cl.time, mv))
        box.add_widget(cl)
        box.add_widget(submit)
        mv.open()

    def set_time(self, inst, value):
        print(value)

    def update_time(self, time, mv):
        mv.dismiss()
        self.ids.task_time.text = str(time)


class NewItem(ModalView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class NewButton(ButtonBehavior, BoxLayout):
    pass


class Task(BoxLayout):
    """this class represent each new task added by the user"""
    name = StringProperty('')
    details = StringProperty('')
    time = StringProperty('')
    date = StringProperty('')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ItemToBuy(BoxLayout):
    name = StringProperty('')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MainWindow(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = Database()
        self.init_view()
        Clock.schedule_interval(self.pulsating_button, 5)

    def init_view(self):
        all_tasks = self.db.get_tasks()
        scroll_parent = Window
        uw = self.ids.upcoming_wrapper

        for t in all_tasks:
            task = Task()
            task.name = t[1]
            task.details = t[2]
            date, time = t[3].rsplit(' ', 1)
            task.time = time
            task.date = date
            task.size_hint = [None, 1]
            task.size = [scroll_parent.width / 1.5, 45]

            uw.add_widget(task)

    def pulsating_button(self, dtx):
        before = dp(45)
        after = dp(55)
        anim = Animation(btn_size=(before, before), t='in_quad', duration=.5) + Animation(btn_size=(after, after),
                                                                                          t='in_quad', duration=.5)
        target = self.ids.cta
        anim.start(target)

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
            print('za krótka informacja o zadaniu')
        else:
            task = Task()
            task.name = xtask[0].text
            task.details = xtask[1].text
            task.time = xtask[2].text
            task.date = xtask[3].text
            task.size_hint = [None, None]
            task.size = [scroll_parent.width / 1.5, scroll_parent.height -
                         (.05 * scroll_parent.height)]

            datetime = ' '.join([xtask[2].text, xtask[3].text])
            task_ = (xtask[0].text, xtask[1].text, datetime)
            if self.db.add_task(task_):
                uw.add_widget(task)
            mv.dismiss()

            if len(uw.children) > 1:
                for child in uw.children:
                    if type(child) == NewButton:
                        uw.remove_widget(child)
                        break

    def delete_task(self, task: Task):
        name = task.name
        uw = self.ids.upcoming_wrapper

        if self.db.delete_task(name):
            task.parent.remove_widget(task)

    def add_new_item(self):
        ni = NewItem()
        ni.open()

    def add_item(self, mv, shopping_item):
        error = False
        scroll_parent = Window
        sw = self.ids.shopping_wrapper

        if len(shopping_item.text) < 3:
            shopping_item.hint_text = '**Pole wymagane**'
            shopping_item.hint_text_color = [1, 0, 0, 1]
            error = True
        if error:
            print('za krótka informacja o zadaniu')
        else:
            product = ItemToBuy()
            product.name = shopping_item.text

            product.size_hint = [None, None]
            product.size = [scroll_parent.width, scroll_parent.height -
                            (.85 * scroll_parent.height)]

            product_ = shopping_item.text

            if self.db.add_item(product_):
                sw.add_widget(product)
            mv.dismiss()

    def delete_item(self, product: ItemToBuy):
        name = product.name
        # sw = self.ids.shopping_wrapper

        if self.db.delete_item(name):
            product.parent.remove_widget(product)
