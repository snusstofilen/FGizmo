from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.gridlayout import GridLayout
from kivymd.uix.screen import Screen
from kivymd.uix.button import Button
<<<<<<< HEAD

import pdb

=======
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,disable_multitouch')
>>>>>>> 5032b84cd3ded91893e6817c619ceda3806a3ed7
from kivy.metrics import dp

from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

class Table(GridLayout):

    def __init__(self):
        super().__init__(cols=1)

        self.table = MDDataTable(use_pagination=True,
            column_data=[
                ("Name", dp(30)),
                ("Value", dp(30)),
                ("Date", dp(30)),
                ("Label", dp(30)),
                ("Debit/Credit", dp(30))],
            row_data=[
                (f"{i + 1}", f"{(i+1) * 2}", "2020-09-"+f"{i+1}".rjust(2, '0'), "Pastry", "Debit")
                for i in range(30)])

        self.add_widget(self.table)
        self.button = Button(text="Remove")
        self.add_widget(self.button)

        self.button.bind(on_touch_down=self.on_pressed)
        self.table.bind(on_touch_down=self.on_pressed)
        self.table.bind(on_row_press=self.on_row_press)
        # self.remove_button.bind(on_press=callback)

    def on_row_press(self, instance_table, instance_row):
        print(instance_table, instance_row)

    def on_pressed(self, instance, touch):
        if touch.button == 'right':
            print('right mouse button clicked!')


class TestApp(MDApp):

    def build(self):
        self.datatable = Table()
        self.screen = Screen()
        self.screen.add_widget(self.datatable)
        return self.screen

table = TestApp()
table.run()
