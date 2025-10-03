from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label 
from jnius import autoclass
from kivy.properties import ListProperty, StringProperty
from kivy.uix.button import Button

BluetoothDevice = autoclass('android.bluetooth.BluetoothDevice')
#ajuda a ver outros dispositivos.

BluetoothSocket = autoclass('android.bluetooth.BluetoothSocket')
#é como um telefone virtual que conversa com outros telefones.

UUID = autoclass('java.util.UUID')
#aqui é a forma que vamos transformar a linguagem python em algo decifravel para o android.

class MusicControl(BoxLayout):
    device = ListProperty([]) #sacola vazia que guardamos o nome do disp.
    connected_device = StringProperty("") #onde escrevemos o nome do disp.

    
    def __init__(self, **kwargs):
        super(MusicControl, self).__init__(**kwargs)
        self.bluetooth_on = False
        self.bluetooth_adapter = None
        self.socket = None
        self.device_buttons = []
#Vou utilizar o __ini__ porque eu preciso configurar valores iniciais.
#Precisa executar alguma configuração quando obj é criado.

    def turn_bluetooth_on(self):
        try:
            self.bluetooth_adapter = BluetoothAdapter.getDefaultAdapter
#"Pegue o adaptador padrão bluetooth"
#colocamos o "self.bluetooth_adapter" como None inicialmente no def__init__

            if not self.bluetooth_adapter.isEnabled():
#Se caso o bluetooth não estiver habilitado
                self.bluetooth_adapter.enable()
#Habilite, então!
            self.bluetooth_on = True
#colocamos como "self.bluetooth_on = False" no def__init__
            print("Bluetooth ligado!")
        except Exception as e:
            print("Ops! Não foi possível ligar o bluetooth: {e}")

    def turn_bluetooth_off(self):
        try:
            if self.bluetooth_adpater and self.bluetooth_adapter.isEnabled():
                self.bluetooth_adapter.disable()
            self.bluetooth_on = False
            print("Bluetooth desligado!")
        except Exception as e:
            print(f"Ops! Não consegui desligar o bluetooth: {e}")

    def discover_devices(self):
        if not self.bluetooth_on:
            print("Ligue o bluetooth primeiro!")
            return
        try:
            print("Procurando amigos...")
            self.devices = []
#começou vazia a lista, colocamos na classe principal chamada MusicControl
            self.ids.device_list.clear_widgets() 
#vai limpar o widget que mostra as conexoes anteriores
            paired_devices = self.bluetooth_adapter.getBondedDevices().toArray()
#pega dispositivos já pareados do dispositivos.

            for device in paired_devices:
                device_name = device.getName()
                device_adress = device.getAddress()
                self.devices.append((device_name, device_address))
#pega o nome e endereço MAC e coloca em uma lista chamada self.devices
            btn = Button(text=f"Conectar a: {device_name}", size_hint_y=None, height='50dp')
            btn.device = device
            btn.bind(on_press=self.connect_to_device)
            self.ids.device_list.add_widget(btn)
#adiciona um botão na tela do usuario
            self.device_buttons.append(btn)
            if not self.devices:
                self.ids.device_list.add_widget(
                    Label(text="Nenhum dispositivo encontrado. Faça o pareamento primeiro"), size_hint_y=None, height='50dp'))
        except Exception as e:
            print(f"Erro ao procurar dispositivos: {e}")
       

    def connect_to_device(self, button): 
        device = button.device
        try:
            uuid= UUID.fromString("00001101-0000-1000-8000-00805F9B34FB")
            
            self.socket = device.createRfcommSocketToServiceRecord(uuid)
            self.socket.connect()
            
            self.connected_device = device.getName() 
            print(f"Conectado ao: {self.connected_device}") 
            
            self.ids.connection_status.text = f"Conectado a: {self.connected_device}"

        except Exception as e: 
            print(f"Não consegui conectar: {e}") 
            self.ids.connection_status.text = "Não consegui conectar :("

    def play_music(self): 
        if not self.connected_device:
            print("Precisa conectar alguém primeiro!")
            return
 
        try:
            if self.socket
                command = "PLAY\n" 
                self.socket.getOutputStream().write(command.encode('utf-8'))
#acessa o canal com o self.socket
#.getOutputStream() obtem o tubo de saida para os dados
#.write() escreve os dados no tubo
#command.encode('utf-8') converte o texto em bytes para o bluetooth

                print(f"Tocando música: {self.connected_device}") 
        except Exception as e:
            print(f"Erro ao tocar música: {e}")

     def pause_music(self):
         if not self.connected_device:
             print("Primeiro conectar alguém primeiro!") 
             return

         try:
            if self.socket
                command = "PAUSE\n" 
                self.socket.getOutputStream().write(command.encode('utf-8'))
                print(f"Pausando música: {self.connected_device}") 
         except Exception as e: 
            print(f"Erro ao pausar música: {e}")

     def stop_music(self):
         if not self.connected_device:
             print("Primeiro conectar alguém primeiro!")
             return

         try:
            if self.socket
                command = "STOP\n"
                self.socket.getOutputStream().write(command.encode('utf-8'))
                print(f"Parando a música: {self.connected_device}") 
         except Exception as e:
            print(f"Erro ao parar música: {e}") 
         if not self.connected_device:
             print("Primeiro conectar alguém primeiro!") 
             return

         try:
            if self.socket
                command = "STOP\n"
                self.socket.getOutputStream().write(command.encode('utf-8'))
                print(f"Parando  música: {self.connected_device}") 
         except Exception as e:
            print(f"Erro ao parar música: {e}")  
 

     def on_stop(self): 
         if self.socket:
             try:
                 self.socket.close()
             except:
                 pass

class MusicApp(App): 
    def build(self):
        return MusicControl()

if __name__ =='__main__':
    MusicApp().run()       
