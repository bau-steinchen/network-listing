from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle


class BorderBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(BorderBoxLayout, self).__init__(**kwargs)
        with self.canvas.before:
            Color(1, 1, 0, 1)  # Farbe des Rahmens (schwarz)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size