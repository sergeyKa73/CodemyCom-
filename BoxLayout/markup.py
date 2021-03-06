from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder


# Designate Our .kv design file
Builder.load_file('markup.kv')

class MyLayout(Widget):
    pass


class MyMarkupApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyMarkupApp().run()