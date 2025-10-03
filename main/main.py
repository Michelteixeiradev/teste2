from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyLayout(BoxLayout):
    def troca_texto(self):
        self.ids.troca_label.text = 'Estou fazendo um teste'

    def troca_texto2(self): 
        self.ids.troca_label2.text = 'Esse daqui é outro teste'

class MyApp(App): 
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()
