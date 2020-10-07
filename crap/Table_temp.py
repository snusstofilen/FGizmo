from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


class TableApp(MDApp):

    def build(self):
        self.datatable = MDDataTable(
            use_pagination=True,
            column_data=[
                ("Name", dp(30)),
                ("Value", dp(30)),
                ("Date", dp(30)),
                ("Label", dp(30)),
                ("Debit/Credit", dp(30)),
            ],
            row_data=[
                (f"{i + 1}", f"{(i+1) * 2}", "2020-09-"+f"{i+1}".rjust(2, '0'), "Pastry", "Debit")
                for i in range(30)
            ],
        )
        return self.datatable

table = TableApp()
table.run()
