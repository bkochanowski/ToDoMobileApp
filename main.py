from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.screenmanager import Screen


class MainScreen(BoxLayout):
    pass


class WelcomeScreen(Screen):
    pass


# needs to be reconstructed to gridLayout
class ActiveTasks(Screen):
    pass


class ShoppingList(Screen):
    pass


class ShowcaseScreen(Screen):
    fullscreen = BooleanProperty(False)

    def add_widget(self, *args, **kwargs):
        if 'content' in self.ids:
            return self.ids.content.add_widget(*args, **kwargs)
        return super(ShowcaseScreen, self).add_widget(*args, **kwargs)


class ToDoApp(App):
    title = 'Kivy To-do and Shopping List app'

    def build(self):
        return MainScreen()


if __name__ == '__main__':
    ToDoApp().run()
