from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.theming import ThemeManager
from kivy.uix.screenmanager import Screen, NoTransition, CardTransition
from kivy.clock import Clock
from kivymd.uix.button import MDRoundFlatButton

class Accueil(Screen):
    def __init__(self, **kwargs):
        super(Accueil, self).__init__(**kwargs)
        Clock.schedule_once(self.changer)

    def changer(self, dt):
        self.ids.bouton.text="je change"
        self.ids.float.add_widget(MDRoundFlatButton(text="nouveau"))
class Parametre(Screen):
    pass

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.theme_cls=ThemeManager()
        self.theme_cls.primary_palette="BlueGray"


    def build(self):
        return Builder.load_file("main.kv")

    def change_fenetre(self, nom_fenetre , direction='avant', mode="", duration="8.5"):
        screen_manager = self.root.ids["screen_manager"]
        if direction == "avant":
            mode = "push"
            direction = "left"

        elif direction == "arriere":
            mode = "pop"
            direction = "right"
        elif direction == "None":
            screen_manager.transition=NoTransition
            screen_manager.current=nom_fenetre

        screen_manager.transition=CardTransition(direction=direction, mode=mode, duration=duration)
        screen_manager.current=nom_fenetre

MainApp().run()
