from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.clock import Clock

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.open_file_chooser_button = Button(text="Open File Chooser")
        self.open_file_chooser_button.bind(on_press=self.show_file_chooser)
        self.add_widget(self.open_file_chooser_button)

        self.selected_file_label = Label(text="Selected file path will appear here.")
        self.add_widget(self.selected_file_label)

    def show_file_chooser(self, instance):
        file_selector_layout = BoxLayout(orientation='vertical')
        file_chooser = FileChooserListView()
        file_selector_layout.add_widget(file_chooser)

        select_button = Button(text="Select")
        file_selector_layout.add_widget(select_button)

        popup = Popup(title="File Chooser", content=file_selector_layout, size_hint=(0.9, 0.9))

        def select_file(instance):
            # Display the spinner
            spinner = Spinner(text='Loading...', values=('Loading...',))
            self.add_widget(spinner)

            def update_label(dt):
                selected_file = file_chooser.selection
                if selected_file:
                    self.selected_file_label.text = f"Selected file: {selected_file[0]}"
                else:
                    self.selected_file_label.text = "No file selected."
                popup.dismiss()
                # Remove the spinner
                self.remove_widget(spinner)

            # Simulate a delay to show the spinner (replace this with actual processing time)
            Clock.schedule_once(update_label, 1)

        select_button.bind(on_press=select_file)

        popup.open()

class FileSelectorApp(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    FileSelectorApp().run()
