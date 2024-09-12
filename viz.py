import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

class VZN:
    def __init__(self):
        pass

    def b_plot(self, data, x, y, title='', theme='default'):
        """Creates a bar plot with customizable themes."""
        if theme == 'dark':
            plt.style.use('dark_background')
        else:
            plt.style.use('default')

        plt.figure(figsize=(12, 8))
        sns.barplot(data=data, x=x, y=y)
        plt.title(title)
        plt.show()

    def s_plot(self, data, x, y, title='', interactive=False):
        """Generates a scatter plot; interactive if specified."""
        if interactive:
            fig = px.scatter(data, x=x, y=y, title=title)
            fig.show()
        else:
            plt.figure(figsize=(12, 8))
            sns.scatterplot(data=data, x=x, y=y)
            plt.title(title)
            plt.show()

    def hmap(self, data, title=''):
        """Creates a heatmap from a correlation matrix or 2D data."""
        plt.figure(figsize=(12, 8))
        sns.heatmap(data, annot=True, cmap='coolwarm')
        plt.title(title)
        plt.show()

    def hist(self, data, title=''):
        """Generates a histogram."""
        plt.figure(figsize=(12, 8))
        sns.histplot(data=data)
        plt.title(title)
        plt.show()

    