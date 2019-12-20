from plotly.offline import plot
import plotly.graph_objs as go

class DataPlotter(object):
    """ Plot charts to the web page. """
    def __init__(self):
        pass

    def plot_line_chart(self, x_data, y_data, title):
        """ Plot a line chart. """
        data = [
            go.Scatter(
                x=x_data,
                y=y_data
            )
        ]
        layout = go.Layout(title=title)
        return plot(go.Figure(data=data, layout=layout), output_type='div')
