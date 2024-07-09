import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.properties import StringProperty, BooleanProperty

from helper.border import BorderBoxLayout


class SelectableLabel(RecycleDataViewBehavior, Label):
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            self.selected = not self.selected
            if self.selected:
                rv = self.parent.parent
                rv.data.append({'text': f'Selected {self.text}'})
            return True

    def apply_selection(self, rv, index, is_selected):
        self.selected = is_selected


class MyRecycleView(RecycleView):
    def __init__(self, **kwargs):
        super(MyRecycleView, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(20)]


class MyApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')

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
        root.add_widget(menu_bar)

        # Hauptlayout
        main_layout = BoxLayout()
        
        # Linker Bereich (1/3)
        left_layout = BoxLayout(orientation='vertical', size_hint_x=0.33)
        scan_button = Button(text='Scannen', size_hint_y=None, height=30, on_press=self.on_scan)
        
        # top list bar so scanning
        list_bar = BoxLayout(orientation='vertical')
        config_bar = BoxLayout(size_hint_y=0.2, height=30)
        config_name = Label(text='Configfile:')
        config_file = Label(text='network.json')
        config_bar.add_widget(config_name)
        config_bar.add_widget(config_file)

        # list view to display network
        network_list = BoxLayout(orientation='vertical',size_hint_y=0.8, padding=10, spacing=10)

        # Erstellen des ScrollView und der Liste
        scrollview = ScrollView()
        list_layout = BorderBoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None)
        list_layout.bind(minimum_height=list_layout.setter('height'))
        for i in range(50):
            item = Label(text=f"Item {i+1}", size_hint_y=None, height=30)
            list_layout.add_widget(item)

        scrollview.add_widget(list_layout)
        network_list.add_widget(scrollview)

        list_bar.add_widget(config_bar)
        list_bar.add_widget(network_list)

        left_layout.add_widget(scan_button)
        left_layout.add_widget(list_bar)
        
        # Liste
        self.item_list = MyRecycleView()
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
        root.add_widget(main_layout)
        
        return root

    def on_scan(self, instance):
        # Hier wird die Logik für das Scannen implementiert
        # self.name_label.text = 'Scannen gedrückt'
        # Beispielhaftes Hinzufügen eines Elements zur Liste
        # self.item_list.data.append({'text': 'New Item'})
        print('Scannen button clicked')

if __name__ == '__main__':
    MyApp().run()
