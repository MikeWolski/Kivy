from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class Grid(GridLayout):
    def __init__(self,**kwargs):
        super(Grid,self).__init__(**kwargs)
        self.cols = 3
        self.add_widget(Button(text=''))
        self.add_widget(Button(text=''))
        self.add_widget(Button(text=''))
        self.add_widget(Button(text=''))
        self.add_widget(Button(text=''))
        self.add_widget(Button(text=''))
        self.add_widget(Button(text=''))
        self.add_widget(Button(text=''))
        self.add_widget(Button(text=''))

class TicTacToeApp(App):
    def build(self):
        return Grid()

if __name__ == '__main__':
    TicTacToeApp().run()