from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.gridlayout import GridLayout
from kivymd.uix.screen import Screen
from kivymd.uix.button import Button

import pdb

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
        self.add_widget(Button(text="Remove"))

        self.table.bind(on_row_press=self.on_row_press)

    def on_row_press(self, instance_table, instance_row):
        print(instance_table, instance_row)

class TestApp(MDApp):

    def build(self):
        self.datatable = Table()
        self.screen = Screen()
        self.screen.add_widget(self.datatable)
        return self.screen

table = TestApp()
table.run()
