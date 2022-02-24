from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

# Designate Uur .kv design file
Builder.load_file('label_color.kv')

class MyLayout(Widget):
    pass

class SomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    SomeApp().run()
