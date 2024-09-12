import seaborn as sns
from viz import vzn

def main():
    iris = sns.load_dataset('iris')

    viz = vzn()

    print("Iris Dataset:")
    print(iris.head())

    # Bar Plot: Average petal length by species
    print("Generating Bar Plot of Average Petal Length by Species...")
    avg_petal_length = iris.groupby('species')['petal_length'].mean().reset_index()
    viz.b_plot(avg_petal_length, x='species', y='petal_length', title='Average Petal Length by Species', theme='dark')

    # Scatter Plot: Petal Length vs. Petal Width
    print("Generating Scatter Plot of Petal Length vs. Petal Width...")
    viz.s_plot(iris, x='petal_length', y='petal_width', title='Scatter Plot of Petal Length vs. Petal Width', interactive=False)

    # Heatmap: Correlation matrix of the features
    print("Generating Heatmap of Correlation Matrix...")
    correlation_matrix = iris.corr()
    viz.hmap(correlation_matrix, title='Heatmap of Iris Dataset Correlation Matrix')

    # Histogram: Distribution of Petal Length
    print("Generating Histogram of Petal Length...")
    viz.hist(iris['petal_length'], title='Histogram of Petal Length')

if __name__ == "__main__":
    main()