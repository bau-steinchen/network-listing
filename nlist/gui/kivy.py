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
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.clock import Clock

from helper.border import BorderBoxLayout
from network.network import Network
from network.NetworkHandler import NetworkHandler

import os
import threading


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


class GUI(App):
    def __init__(self, default_config, **kwargs):
        super(GUI, self).__init__(**kwargs)
        self.default_config = default_config  

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
        self.list_bar = list_bar
        config_bar = BoxLayout(size_hint_y=None, height=30)
        config_name = Label(text='Configfile:')
        self.config_name = config_name
        config_file = Button(text=self.default_config, on_press=self.show_configfile_chooser)
        self.config_file = config_file
        config_bar.add_widget(config_name)
        config_bar.add_widget(config_file)

        # list view to display network
        network_list = BoxLayout(orientation='vertical', size_hint_y=0.8, padding=10, spacing=10)

        # Erstellen des ScrollView und der Liste
        scrollview = ScrollView()
        list_layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None)
        list_layout.bind(minimum_height=list_layout.setter('height'))
        self.list_layout = list_layout
        # self.populate_networklist()
        update_button = Button(text='Update', size_hint_y=None, height=30, on_press=self.on_update)
        

        scrollview.add_widget(list_layout)
        network_list.add_widget(scrollview)

        list_bar.add_widget(config_bar)
        list_bar.add_widget(network_list)

        left_layout.add_widget(scan_button)
        left_layout.add_widget(list_bar)
        left_layout.add_widget(update_button)

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
        print('Scannen button clicked')

    def on_update(self, instance):
        self.populate_networklist()

    def populate_networklist(self):
        self.list_layout.clear_widgets()
        self.network = Network(self.default_config)

        for device in self.network.network['devices']:
            item = BorderBoxLayout(orientation='horizontal', size_hint_y=None, height=60)
            name = Button(text=f"Name: {device['name']}\nIP: {device['ip']}")
            name.bind(on_press=lambda instance: self.on_device_clicked(device))
            active = Label(text="Status", size_hint_x=None, width=60)
            if self.get_device_status(device):
                active.text = "Online"
            else:
                active.text = "Offline"
            item.add_widget(name)
            item.add_widget(active)

            self.list_layout.add_widget(item)
            self.config_file.text = self.default_config

        
    
    def show_configfile_chooser(self, instance):
        file_selector_layout = BoxLayout(orientation='vertical')
        file_chooser = FileChooserListView()
        file_selector_layout.add_widget(file_chooser)

        select_button = Button(text="Select")
        file_selector_layout.add_widget(select_button)

        popup = Popup(title="File Chooser", content=file_selector_layout, size_hint=(0.9, 0.9))

        def select_file(instance):
            
            selected_file = file_chooser.selection
            
            if selected_file:
                if selected_file[0].endswith(".json"):  
                    self.config_file.text = f"Loading..."
                    self.config_name = os.path.basename(selected_file[0])
                    self.default_config = selected_file[0]
                else:
                    print("No valid config File selected!")
            else:
                # self.config_name.text = "No file selected."
                print("No file selected using default!")
            popup.dismiss()
            Clock.schedule_once(lambda dt: self.populate_networklist(), 1)
            # self.populate_networklist()
            

        select_button.bind(on_press=select_file)

        popup.open()

    def on_device_clicked(self, device):
        print("show data for device: ")
        print(device)

    def get_device_status(self, device):
        device_ip = device['ip']
        return NetworkHandler().check_device_status(device_ip)