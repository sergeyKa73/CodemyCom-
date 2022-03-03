from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

#Define our different screen
class FirstWindow(Screen):
	pass

class SecondWindow(Screen):
	pass

class WindowManager(ScreenManager):
	pass


# Designate Our .kv design file
kv = Builder.load_file('new_window.kv')



class MyWindowApp(App):
	def build(self):
		return kv

if __name__ == '__main__':
	MyWindowApp().run()