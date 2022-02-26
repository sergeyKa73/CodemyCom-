from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

# Designate Uur .kv design file
Builder.load_file('label_update.kv')


class MyLayout(Widget):
    def press(self):
        # Create variables for our widget
        name = self.ids.name_input.text
        # print(name)

        # Update thr label
        self.ids.name_label.text = f' Hello {name}!'

        # Clear input box
        self.ids.name_input.text = ''


class AwesomeApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()
