from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder


# Designate Our .kv design file
Builder.load_file('switch.kv')

class MyLayout(Widget):
    def switch_click(self, switchObject, switchValue):
        if (switchValue):
            self.ids.label_text.text = 'The Switch Is On!'
        else:
            self.ids.label_text.text = "You clicked the switch Off!"
            #self.ids.my_switch.disabled = True

class MySwitchApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MySwitchApp().run()