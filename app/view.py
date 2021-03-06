from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.modalview import ModalView
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty
from kivy.clock import Clock
from libs.garden.circulardatetimepicker import CircularTimePicker as CTP
from kivy.metrics import dp
from app.storage.db import Database
from datetime import date as Dt, datetime as Dte


class NewTask(ModalView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.set_name_focus, 1)

    def set_name_focus(self, *args):
        self.ids.task_name.focus = True

    def get_time(self):
        mv = ModalView(size_hint=[0.8, 0.6])
        box = BoxLayout(orientation="vertical", size_hint=[0.9, 0.9])
        mv.add_widget(box)

        ctp_settings = (
            "[color={am_color}][ref=am]RANO[/ref][/color]\n[color={pm_color}][ref=pm]POPOŁUDNIE[/ref]["
            "/color] "
        )
        cl = CTP(
            color=[1, 1, 1, 1], selector_color=[0, 0.6, 0], ampm_format=ctp_settings
        )
        cl.bind(time=self.set_time)

        submit = Button(
            text="Zapisz",
            background_normal="",
            color=[0, 0.3, 0, 0.7],
            background_color=[1, 1, 1, 1],
            size_hint_y=0.2,
        )
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

    name = StringProperty("")
    details = StringProperty("")
    time = StringProperty("")
    date = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ItemToBuy(BoxLayout):
    """this class represent each new shopping list item added by the user"""

    is_done = BooleanProperty(False)
    name = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = Database()
        self.init_task()
        self.init_shopping()

    def init_task(self):
        """getting all tasks from DB on APP initialization"""
        all_tasks = self.db.get_tasks()
        scroll_parent = Window
        uw = self.ids.upcoming_wrapper

        if not all_tasks:
            new_btn = NewButton()
            new_btn.size_hint = [None, None]
            new_btn.size = [
                scroll_parent.width / 1.9,
                scroll_parent.height - (0.45 * scroll_parent.height),
            ]
            new_btn.bind(on_release=self.add_new)
            uw.add_widget(new_btn)
        else:
            for t in all_tasks:
                task = Task()
                task.name = t[1]
                task.details = t[2]
                date, time = t[3].rsplit(" ", 1)
                x = self.compare_date(date)
                if x == "today":
                    task.tsk_clr = (0.7, 0.45, 0.1, 0.6)
                elif x == "past":
                    task.tsk_clr = (0.7, 0, 0, 0.6)

                task.time = time
                task.date = date

                task.size_hint = [None, None]
                task.size = [
                    scroll_parent.width / 1.9,
                    scroll_parent.height - (0.45 * scroll_parent.height),
                ]

                uw.add_widget(task)

    def init_shopping(self):
        """getting all products to buy from DB on APP initialization"""
        all_items = self.db.get_items()
        scroll_parent = Window
        sw = self.ids.shopping_wrapper
        for t in all_items:
            item = ItemToBuy()
            state = self.string_to_bool(t[1])
            if t[1] == "True":
                item.bcg_clr = [0.5, 0.5, 0.5, 0.5]
                item.is_done.active = 1

            item.name = t[2]
            item.size_hint = [None, None]
            item.size = [scroll_parent.width / 1.35, dp(65)]

            sw.add_widget(item)

    def string_to_bool(self, string):
        if string == "True":
            return True
        else:
            return False

    def change_to_shopping(self):
        """shopping screen is currently displayed, it turns tasks menu button slightly darker"""
        self.ids["tsk_btn"].color = 1, 1, 1, 0.5

    def change_to_tasks(self):
        """task screen is currently displayed, it turns shopping menu button slightly darker"""
        self.ids["shp_btn"].color = 1, 1, 1, 0.5

    def pulsating_button(self, dtx):
        """it animates button which adds new product to buy during on_press event"""
        before = dp(55)
        after = dp(65)
        anim = Animation(
            btn_size=(before, before), t="in_quad", duration=0.3
        ) + Animation(btn_size=(after, after), t="in_quad", duration=0.3)
        target = self.ids.cta
        anim.start(target)

    def add_new(self, instance):
        nt = NewTask()
        nt.open()

    def add_task(self, mv, xtask: tuple):
        error = False
        scroll_parent = Window
        uw = self.ids.upcoming_wrapper

        for t in xtask:
            if len(t.text) < 3:
                t.hint_text = "**Pole wymagane**"
                t.hint_text_color = [1, 0, 0, 1]
                error = True
        if error:
            print("za krótka informacja o zadaniu")
        else:
            task = Task()
            task.name = xtask[0].text
            task.details = xtask[1].text
            task.time = xtask[3].text
            task.date = str(Dte.strptime(xtask[2].text, "%d-%m-%Y").date())
            print(f"test {task.date}")
            task.size_hint = [None, None]
            task.size = [
                scroll_parent.width / 1.5,
                scroll_parent.height - (0.35 * scroll_parent.height),
            ]

            date_and_time = " ".join([task.date, xtask[3].text])
            task_ = (xtask[0].text, xtask[1].text, date_and_time)
            if self.db.add_task(task_):
                uw.clear_widgets()
                self.init_task()
            mv.dismiss()

            if len(uw.children) > 1:
                for child in uw.children:
                    if type(child) == NewButton:
                        uw.remove_widget(child)
                        break

    def get_update_task(self, instance):
        nt = NewTask()
        nt.ids.task_name.text = instance.name
        nt.ids.task_details.text = instance.details
        nt.ids.task_date.text = instance.date
        nt.ids.task_time.text = instance.time
        nt.ids.submit_wrapper.clear_widgets()

        submit = Button(
            text="Aktualizuj",
            bold=True,
            background_normal="",
            background_color=(1, 0, 0, 1),
        )
        submit.bind(on_release=lambda x: self.update_task(nt, instance))
        nt.ids.submit_wrapper.add_widget(submit)

        nt.open()

    def update_task(self, task_data, task):
        uw = self.ids.upcoming_wrapper
        xtask = [
            task_data.ids.task_name.text,
            task_data.ids.task_details.text,
            str(Dte.strptime(task_data.ids.task_date.text, "%d-%m-%Y").date()),
            task_data.ids.task_time.text,
        ]
        error = None
        for t in xtask:
            if len(t) < 3:
                t.hint_text = "**Pole wymagane**"
                t.hint_text_color = [1, 0, 0, 1]
                error = True
        if error:
            pass
        else:
            xtask = [
                xtask[0],
                xtask[1],
                " ".join(
                    xtask[2:],
                ),
                task.name,
            ]
            if self.db.update_task(xtask):
                task.name = task_data.ids.task_name.text
                task.details = task_data.ids.task_details.text
                task.time = task_data.ids.task_time.text
                task.date = task_data.ids.task_date.text
            task_data.dismiss()

            uw.clear_widgets()
            self.init_task()

    def compare_date(self, date: str):
        today = Dt.today()

        today_date = Dte.strftime(today, "%Y-%m-%d")
        print(f"today date: {today_date}")
        task_date = str(Dte.strptime(date, "%Y-%m-%d").date())
        print(f"task date: {task_date}")

        if today_date > task_date:
            return "past"
        elif today_date == task_date:
            return "today"
        else:
            return "future"

    def delete_task(self, task: Task):
        name = task.name
        scroll_parent = Window
        uw = self.ids.upcoming_wrapper

        if self.db.delete_task(name):
            task.parent.remove_widget(task)

        all_tasks = self.db.get_tasks()
        if not all_tasks:
            new_btn = NewButton()
            new_btn.size_hint = [None, None]
            new_btn.size = [
                scroll_parent.width / 1.9,
                scroll_parent.height - (0.45 * scroll_parent.height),
            ]
            new_btn.bind(on_release=self.add_new)
            uw.add_widget(new_btn)

    def add_new_item(self):
        ni = NewItem()
        ni.open()

    def add_item(self, mv, shopping_item):
        error = False
        scroll_parent = Window
        sw = self.ids.shopping_wrapper

        if len(shopping_item.text) < 3:
            shopping_item.hint_text = "**Pole wymagane**"
            shopping_item.hint_text_color = [1, 0, 0, 1]
            error = True
        if error:
            print("za krótka nazwa produktu")
        else:
            product = ItemToBuy()
            product.name = shopping_item.text

            product.size_hint = [None, None]
            product.size = [scroll_parent.width / 1.35, dp(65)]

            product_ = shopping_item.text

            if self.db.add_item(product_):
                sw.clear_widgets()
                self.init_shopping()
                mv.dismiss()

    def checkbox_status(self, instance, xitem: tuple):
        sw = self.ids.shopping_wrapper

        item = ItemToBuy()
        item.is_done = str(xitem[0])
        item.name = xitem[1]
        _item = [item.is_done, item.name]
        if self.db.update_item_status(_item):
            sw.clear_widgets()
            self.init_shopping()

    def delete_item(self, product: ItemToBuy):
        name = product.name

        if self.db.delete_item(name):
            product.parent.remove_widget(product)
