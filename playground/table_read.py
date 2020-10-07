from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

import pandas as pd

def read_and_convert_csv(file):
    data_frame = pd.read_csv(file)
    column_names = [(x,dp(30)) for x in data_frame.columns]
    values = [tuple(x) for x in data_frame.values]
    return data_frame, column_names, values

class DemoApp(MDApp):

    def __init__(self):
        self.data_frame = read_and_convert_csv(
        'dataset.csv')
        super().__init__()

    def build(self):
        column_names = self.data_frame[1]
        values = self.data_frame[2]

        screen = Screen()
        data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                 size_hint=(0.9, 0.6),
                                 check=True,
                                 rows_num=20,
                                 column_data=column_names,
                                 row_data=values
                                 )
        data_table.bind(on_row_press=self.on_row_press)
        data_table.bind(on_check_press=self.on_check_press)
        screen.add_widget(data_table)
        return screen

    def on_row_press(self, instance_table, instance_row):
        print(instance_table, instance_row)

    def on_check_press(self, instance_table, current_row):
        print(instance_table, current_row)




if __name__ == '__main__':
    DemoApp().run()
