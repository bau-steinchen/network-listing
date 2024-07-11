from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.button import Button
from kivy.uix.label import Label

class FileSelector(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.file_chooser = FileChooserListView()
        self.add_widget(self.file_chooser)

        self.label = Label(text="Selected file path will appear here.")
        self.add_widget(self.label)

        self.select_button = Button(text="Select File")
        self.select_button.bind(on_press=self.select_file)
        self.add_widget(self.select_button)

    def select_file(self, instance):
        selected_file = self.file_chooser.selection
        if selected_file:
            self.label.text = f"Selected file: {selected_file[0]}"
        else:
            self.label.text = "No file selected."

class FileSelectorApp(App):
    def build(self):
        return FileSelector()

if __name__ == '__main__':
    FileSelectorApp().run()