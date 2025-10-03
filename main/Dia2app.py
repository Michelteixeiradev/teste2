from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder

Builder.load_file("dia2app.kv")

class Muda_Label(BoxLayout):
    mensagem_string_property = StringProperty('Olá')
    
    def mudar_mensagem(self): 
        self.mensagem_string_property = 'Você clicou!'

class Dia2app(App):
    def build(self):
        return Muda_Label() 

if __name__ == "__main__":
    Dia2app().run()
