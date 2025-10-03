from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import StringProperty, ListProperty

class MusicControl(BoxLayout):
    devices = ([])
    connected_device = ListProperty()


