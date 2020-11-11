import pandas as pd
import matplotlib.pyplot as plt

def create_graph(dictionary, columns):
    # Get a new pandas
    df = create_pandas(dictionary, columns)

    # Set index from column
    df = df.set_index(columns[0]).rename_axis(None)

    # Sorting values
    df = df.sort_values(columns[1], ascending=True)

    df.plot.barh(figsize=(18, 8))
    plt.show()

def create_vertical_graph(dictionary):
    plt.bar(dictionary.keys(), dictionary.values())
    plt.show()

def create_pandas(dictionary, columns):
    df = pd.DataFrame(list(dictionary.items()), columns=columns)

    # Print the dataframe
    print(df)

    return df