from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Rectangle, Color
from kivy.uix.button import ButtonBehavior
from kivy.uix.label import Label


class ScreenManager(ScreenManager):
    pass


class WelcomeScreen(Screen):
    pass


class ActiveTasksScreen(Screen):
    pass


class ShoppingListScreen(Screen):
    pass


class MainScreen(BoxLayout):
    pass


class ToDoApp(App):
    title = 'Kivy To-do and Shopping List app'

    def build(self):
        return MainScreen()


if __name__ == '__main__':
    ToDoApp().run()
