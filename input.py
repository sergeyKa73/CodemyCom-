import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs) :
        # Call  grid layout constructor
        super(MyGridLayout,self).__init__(**kwargs)

        # Set columns
        self.cols = 1
        self.row_force_default = True
        self.row_default_height = 120
        self.col_force_default = True
        self.col_default_width = 200


        # Create a second gridlayout
        self.top_grid = GridLayout(
            row_force_default=True,
            row_default_height=50,
            col_force_default=True,
            col_default_width=200)

        # Set number of columns in our new top
        self.top_grid.cols = 2

        # Add widgets
        self.top_grid.add_widget(Label(text='Name: '))
        # Add Input Box
        self.name = TextInput(multiline=False)
        self.top_grid.add_widget((self.name))

        self.top_grid.add_widget(Label(text='Favorite Pizza: '))
        self.pizza = TextInput(multiline=False)
        self.top_grid.add_widget((self.pizza))

        self.top_grid.add_widget(Label(text='Favorite Thickness: '))
        self.thickness  = TextInput(multiline=False)
        self.top_grid.add_widget((self.thickness ))

        # Add the new top_grid to our app
        self.add_widget(self.top_grid)


        # Create a Submit Button
        self.sumbit = Button(text='Submit',
                             font_size=32,
                             size_hint_y=None,
                             height=50,
                             size_hint_x =None,
                             width=400)
        # Bind the button
        self.sumbit.bind(on_press=self.press)
        self.add_widget(self.sumbit)

    def press(self, instanse):
        name = self.name.text
        pizza = self.pizza.text
        thickness = self.thickness.text

        # print(f'Hello {name}, you like {pizza} pizza, and your favorite thickness {thickness}! ')
        # Print it to the screen
        self.add_widget(Label(text=f'Hello {name}, you like {pizza} pizza, and your favorite thickness {thickness}! '))

        # Clear the input boxes
        self.name.text = ''
        self.pizza.text = ''
        self.thickness.text = ''

class MyApp(App):
    def build(self):
        return MyGridLayout()



if __name__ == '__main__':
    MyApp().run()


