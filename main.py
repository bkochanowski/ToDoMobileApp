import kivy

from app import MainApp
from libs.garden.iconfonts import register

from os.path import dirname, join

if __name__ == "__main__":
    register(
        "MatIcons",
        join(dirname(__file__), "app/assets/fonts/Material-Design-Iconic-Font.ttf"),
        join(dirname(__file__), "app/assets/fonts/zmd.fontd"),
    )
    MainApp().run()
