import pandas as pd
from viz import VZN

data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [23, 45, 56, 78]
}
df = pd.DataFrame(data)
viz = VZN()

# Create a bar plot with a custom theme
viz.b_plot(df, x='Category', y='Values', title='Custom Bar Plot', theme='dark')

# Create an interactive scatter plot
viz.s_plot(df, x='Category', y='Values', title='Interactive Scatter Plot', interactive=True)
