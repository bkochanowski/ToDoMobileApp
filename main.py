from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class ScreenManager(ScreenManager):
    pass


class WelcomeScreen(Screen):
    pass


class ActiveTasksScreen(Screen):
    pass


class ShoppingListScreen(Screen):
    pass


class ActiveTasks(BoxLayout):
    pass


class ToDoApp(App):
    title = 'Kivy To-do and Shopping List app'

    def build(self):
        return ActiveTasks()


if __name__ == '__main__':
    ToDoApp().run()
