from src.datasets_utils import load_dataset, map_boolean_to_real
import pandas as pd


def main():
    pd.set_option('display.max_colwidth', 5000)
    df = load_dataset()

    # Rename the columns to more understanble names
    col_names = {'DGN': 'Diagnosis', 'PRE4': 'FVC', 'PRE5': 'FEV1', 'PRE6': 'Performance',
                 'PRE7': 'Pain', 'PRE8': 'Haemoptysis', 'PRE9': 'Dyspnoea', 'PRE10': 'Cough',
                 'PRE11': 'Weakness', 'PRE14': 'Tumor_Size', 'PRE17': 'Diabetes_Mellitus',
                 'PRE19': 'MI_6mo', 'PRE25': 'PAD', 'PRE30': 'Smoking', 'PRE32': 'Asthma',
                 'AGE': 'Age', 'Risk1Yr': 'Death_1yr'}

    df = df.rename(index=str, columns=col_names)

    print(df.head())

    print(df['Age'] == df.Age)

    # Check that there are no null values
    null_values = df.isnull().sum()

    print("The number of missing values for each column is: ")
    print(null_values)

    print()
    if null_values[1].sum() == 0:
        print("There are no missing values")
    else:
        print("There are missing values")

    df = map_boolean_to_real(df, ['Smoking'])
    print(df)


if __name__ == '__main__':
    main()
