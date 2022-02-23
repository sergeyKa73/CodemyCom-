from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('design.kv')

class MyGridLayout(Widget):

    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    thickness = ObjectProperty(None)

    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        thickness = self.thickness.text

        print(f'Hello {name}, you like {pizza} pizza, and your favorite thickness {thickness}! ')
        # Print it to the screen
        #self.add_widget(Label(text=f'Hello {name}, you like {pizza} pizza, and your favorite thickness {thickness}! '))

        # Clear the input boxes
        self.name.text = ''
        self.pizza.text = ''
        self.thickness.text = ''


class InputApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    InputApp().run()