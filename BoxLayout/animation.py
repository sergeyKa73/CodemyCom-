from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.animation import Animation

# Designate Our .kv design file
Builder.load_file('animation.kv')


class MyLayout(Widget):
    def animate_it(self, widget, *args):
        # define the animation
        animate = Animation(
            background_color=(0, 0, 1, 1),
            duration=3
        )

        # Do second animation
        animate += Animation(
            size_hint=(1, 1))

        # Do Third animation
        animate += Animation(
            size_hint=(.5, .5))

        animate += Animation(
            pos_hint={"center_x": 0.1})

        animate += Animation(
            pos_hint={"center_x": 0.5})

        animate += Animation(
            pos_hint={"center_x": 0.9})

        animate += Animation(
            pos_hint={"center_x": 0.5})

        animate += Animation(
            opacity=0,
            duration=.5
        )

        # Start The Animation
        animate.start(widget)

        # Create a callback
        animate.bind(on_complete=self.my_callback)

    def my_callback(self, *args):
        self.ids.my_label.text = "Wow! Look You Did It!"


class MyAnimationApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    MyAnimationApp().run()
