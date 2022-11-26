from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock

class Ex(Widget):
    score = NumericProperty(0)

class Oh(Widget):
    score = NumericProperty(0)

class TicTacToeGame(Widget):
    Ex = ObjectProperty(None)
    Oh = ObjectProperty(None)

    def on_touch_move(self, touch):
        if touch.x < self.width / 3 and touch.y < self.height / 3:
            self.Ex.center_y = touch.y

class TicTacToeApp(App):
    def build(self):
        game = TicTacToeGame()
        return game

if __name__ == '__main__':
    TicTacToeApp().run()