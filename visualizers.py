'''Bla bla

'''
from bokeh.charts import Bar, output_file, show 
import pandas as pd

class Visualizer:
    '''Bla bla

    '''
    def stacked_bars(self, df, x_axis, y_axis, stack, title=None):
        '''Bla bla

        '''
        df_columnwise = df.reset_index()
        df_columnwise[y_axis] = df_columnwise[y_axis].astype(float)
        p = Bar(df_columnwise, label=x_axis, stack=stack, values=y_axis, title=title)
        self.graph_object = p

    def make_html(self, fileout_path):
        '''Bla bla

        '''
        output_file(fileout_path)
        show(self.graph_object)

    def __init__(self, legend='top_right'):
        '''Bla bla

        '''
        self.legend = legend

        self.graph_object = None