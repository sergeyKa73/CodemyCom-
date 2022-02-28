from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.spelling import Spelling

# Designate Our .kv design file
Builder.load_file('spellchecker.kv')

class MyLayout(Widget):
	def press(self):
		# create instance of Spelling
		s = Spelling()

		# select the language
		s.select_language('ru_Ru')

		# see the language options
		#print(s.list_languages())

		# Grab the word from the textbox
		word = self.ids.word_input.text

		options = s.suggest(word)
		x = ''
		for item in options:
			x = f'{x} {item}'
		# update our label
		self.ids.word_label.text = f'{x}'

		# clear input box
		self.ids.word_input.text = ''


class SpellApp(App):
	def build(self):
		return MyLayout()


if __name__ == '__main__':
	SpellApp().run()