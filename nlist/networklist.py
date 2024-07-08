import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.listview import ListView
from kivy.uix.listview import ListItemButton
from kivy.uix.gridlayout import GridLayout

class MyApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical')

        # Menüleiste
        menu_bar = BoxLayout(size_hint_y=None, height=30)
        file_button = Button(text='File')
        config_button = Button(text='Config')
        data_button = Button(text='Data')
        help_button = Button(text='Help')
        menu_bar.add_widget(file_button)
        menu_bar.add_widget(config_button)
        menu_bar.add_widget(data_button)
        menu_bar.add_widget(help_button)
        self.root.add_widget(menu_bar)

        # Hauptlayout
        main_layout = BoxLayout()
        
        # Linker Bereich (1/3)
        left_layout = BoxLayout(orientation='vertical', size_hint_x=0.33)
        scan_button = Button(text='Scannen', on_press=self.on_scan)
        self.name_label = Label(text='Name:')
        left_layout.add_widget(scan_button)
        left_layout.add_widget(self.name_label)
        
        # Liste
        self.item_list = ListView()
        left_layout.add_widget(self.item_list)

        # Rechter Bereich (2/3)
        right_layout = BoxLayout(orientation='vertical', size_hint_x=0.67)
        
        # Button-Leiste
        button_bar = BoxLayout(size_hint_y=None, height=30)
        add_button = Button(text='Add')
        remove_button = Button(text='Remove')
        save_button = Button(text='Save')
        button_bar.add_widget(add_button)
        button_bar.add_widget(remove_button)
        button_bar.add_widget(save_button)
        right_layout.add_widget(button_bar)
        
        # Tabelle
        self.data_table = GridLayout(cols=2, row_force_default=True, row_default_height=40)
        right_layout.add_widget(self.data_table)

        main_layout.add_widget(left_layout)
        main_layout.add_widget(right_layout)
        self.root.add_widget(main_layout)
        
        return self.root

    def on_scan(self, instance):
        # Hier wird die Logik für das Scannen implementiert
        self.name_label.text = 'Scannen gedrückt'
        # Beispielhaftes Hinzufügen eines Elements zur Liste
        print('Scannen button clicked')

if __name__ == '__main__':
    MyApp().run()