from pathlib import Path

import pandas as pd
from pandas.api.types import is_numeric_dtype
from sklearn.preprocessing import OrdinalEncoder, StandardScaler


def load_dataset(input_path: Path) -> pd.DataFrame:
    if not input_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {input_path}\n"
            "Place Customer-Segmentation_raw.csv in the parent folder of this script."
        )
    return pd.read_csv(input_path)


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    numerical_cols = ['Age', 'AnnualIncome', 'AverageTransactionValue']
    scaler = StandardScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    for col in ['AnnualIncome', 'AverageTransactionValue']:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df[col] = df[col].clip(lower=lower_bound, upper=upper_bound)

    discount_sensitivity_order = ['Low', 'Medium', 'High']
    shopping_frequency_order = ['Rare', 'Occasional', 'Frequent']
    categorical_cols = ['DiscountSensitivity', 'ShoppingFrequency']

    if not all(is_numeric_dtype(df[col]) for col in categorical_cols):
        encoder = OrdinalEncoder(categories=[discount_sensitivity_order, shopping_frequency_order])
        df[categorical_cols] = encoder.fit_transform(df[categorical_cols])

    age_bins = [df['Age'].min() - 1, -0.5, 0.5, df['Age'].max() + 1]
    age_labels = ['Young', 'Adult', 'Senior']
    df['AgeGroup'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels, right=True)

    age_group_encoder = OrdinalEncoder(categories=[age_labels])
    df['AgeGroup'] = age_group_encoder.fit_transform(df[['AgeGroup']])

    return df


def main() -> None:
    script_folder = Path(__file__).resolve().parent
    input_path = script_folder.parent / 'Customer-Segmentation_raw.csv'
    output_path = script_folder / 'Customer-Segmentation_preprocessing.csv'

    print(f"Loading dataset from: {input_path}")
    df = load_dataset(input_path)

    print("Preprocessing data...")
    df_preprocessed = preprocess_data(df)

    df_preprocessed.to_csv(output_path, index=False)
    print(f"Saved preprocessed dataset to: {output_path}")


if __name__ == '__main__':
    main()
