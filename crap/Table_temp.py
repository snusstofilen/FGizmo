from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

class Table(MDDataTable):

    def __init__(self):
        super().__init__(use_pagination=True,
        column_data=[
            ("Name", dp(30)),
            ("Value", dp(30)),
            ("Date", dp(30)),
            ("Label", dp(30)),
            ("Debit/Credit", dp(30))],
        row_data=[
            (f"{i + 1}", f"{(i+1) * 2}", "2020-09-"+f"{i+1}".rjust(2, '0'), "Pastry", "Debit")
            for i in range(30)])

class TableApp(MDApp):

    def build(self):
        self.datatable = Table()
        self.datatable.bind(on_row_press=self.on_row_press)
        return self.datatable

    def on_row_press(self, instance_table, instance_row):
        print(instance_table, instance_row)

table = TableApp()
table.run()
