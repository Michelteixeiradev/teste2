from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class TextInputDem(BoxLayout):
    def enviar_mensagem(self):
        mensagem = self.ids.entrada_texto.text

        if mensagem:
            print(f"Mensagem enviada com sucesso: {mensagem}")
        else:
            print(f"Por favor, digite alguma coisa")

        self.ids.entrada_texto.text = ""

class Dia1App(App):
    def build(self):
        return TextInputDem()

if __name__ == "__main__":
    Dia1App().run() 
