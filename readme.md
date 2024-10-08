
# vzn

  

`vzn` is a Python package designed to extend the capabilities of existing visualization libraries like Matplotlib, Seaborn and Plotly. It provides customizable templates, interactive plots, and makes visualization simple & quick.


## Features

  

-  **Bar Plots**: Create customizable bar plots with dark or default themes.

-  **Scatter Plots**: Generate both static and interactive scatter plots using `seaborn` or `plotly`.

-  **Heatmaps**: Visualize data with annotated heatmaps and various color maps.

-  **Histograms**: Easily generate histograms for data distribution analysis.

  

## Installation
  

You can install `vzn` using pip:

  

```bash

pip  install  vzn

```

## Usage

  
### Bar Plot
```python
v = vzn()
v.b_plot(data, x='Category', y='Values', title='Bar Plot Example', theme='dark')
```

  
### Scatter Plot
```python
# Static Scatter Plot
v.s_plot(data, x='Category', y='Values', title='Static Scatter Plot')

# Interactive Scatter Plot
v.s_plot(data, x='Category', y='Values', title='Interactive Scatter Plot', interactive=True)
```

  
### Heatmap
```python
v.hmap(data.corr(), title='Heatmap Example')
```
### Histogram
```python
v.hist(data['Values'], title='Histogram Example')
```