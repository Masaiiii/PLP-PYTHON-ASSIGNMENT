import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset
def load_and_explore_dataset():
    # Load Iris dataset
    iris = load_iris()
    df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                      columns=iris['feature_names'] + ['target'])
    
    # Map target numbers to species names
    target_names = iris.target_names
    df['species'] = df['target'].map(dict(enumerate(target_names)))
    
    # Display first few rows
    print("Dataset Head:")
    print(df.head())
    
    # Check data types and missing values
    print("\nDataset Info:")
    print(df.info())
    
    # Check for missing values
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    return df

# Task 2: Basic Data Analysis
def perform_data_analysis(df):
    # Compute basic statistics
    print("\nBasic Statistics:")
    print(df.describe())
    
    # Group analysis by species
    print("\nMean Values by Species:")
    grouped_stats = df.groupby('species').mean()
    print(grouped_stats)
    
    return grouped_stats

# Task 3: Data Visualization
def create_visualizations(df):
    plt.figure(figsize=(16, 12))
    
    # 1. Line Chart (using sepal length over index)
    plt.subplot(2, 2, 1)
    plt.plot(df['sepal length (cm)'], label='Sepal Length')
    plt.title('Sepal Length Over Index')
    plt.xlabel('Index')
    plt.ylabel('Length (cm)')
    plt.legend()
    
    # 2. Bar Chart (mean sepal length by species)
    plt.subplot(2, 2, 2)
    df.groupby('species')['sepal length (cm)'].mean().plot(kind='bar')
    plt.title('Average Sepal Length by Species')
    plt.xlabel('Species')
    plt.ylabel('Average Length (cm)')
    plt.xticks(rotation=45)
    
    # 3. Histogram (distribution of sepal width)
    plt.subplot(2, 2, 3)
    df['sepal width (cm)'].hist(bins=20)
    plt.title('Distribution of Sepal Width')
    plt.xlabel('Sepal Width (cm)')
    plt.ylabel('Frequency')
    
    # 4. Scatter Plot (sepal length vs sepal width)
    plt.subplot(2, 2, 4)
    sns.scatterplot(data=df, x='sepal length (cm)', y='sepal width (cm)', hue='species')
    plt.title('Sepal Length vs Sepal Width')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Sepal Width (cm)')
    
    plt.tight_layout()
    plt.show()

# Main Execution
def main():
    try:
        # Load and explore dataset
        iris_df = load_and_explore_dataset()
        
        # Perform data analysis
        perform_data_analysis(iris_df)
        
        # Create visualizations
        create_visualizations(iris_df)
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()