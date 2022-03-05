from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

# Designate Our .kv design file
Builder.load_file('button_image.kv')


class MyLayout(Widget):
    def hello_on(self):
        self.ids.my_image.source = 'Images/button_of.png'
        self.ids.my_label.text = "You Pressed The Button!"

    def hello_off(self):
        self.ids.my_image.source = 'Images/button_on.png'
        self.ids.my_label.text = "Button not pressed!"


class MyButtonApp(App):
    def build(self):
        Window.clearcolor = (1, 0.5, 1, 1)
        return MyLayout()


if __name__ == '__main__':
    MyButtonApp().run()
