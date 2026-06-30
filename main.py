from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)
        lbl_status = Label(
            text="Sistema Inicializado com Sucesso\nCompilacao Homologada via Buildozer",
            halign="center",
            valign="middle",
            font_size="18sp"
        )
        lbl_status.bind(size=lbl_status.setter('text_size'))
        layout.add_widget(lbl_status)
        return layout

if __name__ == '__main__':
    MainApp().run()
