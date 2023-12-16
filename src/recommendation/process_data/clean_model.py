from collections import defaultdict

import matplotlib.pyplot as plt
import pandas as pd

file_path = "../data/collected_data/corrected_seed_features.csv"
train_set = "../data/collected_data/TrainSet.csv"

def read_csv(file_path):
    """
    Read a CSV file into a Pandas DataFrame and convert it to a list of lists.
    """
    df = pd.read_csv(file_path)
    print(df.columns)
    data = df.values.tolist()
    return data


def create_csv(file, data):
    """
    Create a CSV file from a list of lists, adding a 'seedId' column with indices.
    """
    # Assuming data is a list of lists
    num_cols = len(data[0])  # Get the number of columns in the data
    if not all(len(row) == num_cols for row in data):
        raise ValueError("Inconsistent number of columns in the data.")

    # Create column names for DataFrame
    columns = ['seedId'] + [f'col_{i}' for i in range(1, num_cols)]

    # Create DataFrame from data
    df = pd.DataFrame(data, columns=columns)

    # Add seedId column with indices
    df['seedId'] = range(1, len(df) + 1)

    # Write DataFrame to CSV file
    df.to_csv(file, index=False)
def display_duplicates(file_path):
    """
    Display rows with duplicate content in a CSV file.
    """
    df = pd.read_csv(file_path)

    duplicate_rows = df[df.duplicated()]

    print("Duplicate Rows:")
    print(duplicate_rows)

def display_duplicate_data(file_path):
    """
    Display rows with duplicate data based on all columns in a CSV file.
    """
    df = pd.read_csv(file_path)
    duplicate_rows = df[df.duplicated()]
    print("Duplicate Rows:")
    print(duplicate_rows)

def display_duplicate_by_column(file_path, columns):
    """
    Display rows with duplicate data based on specific columns in a CSV file.
    """
    df = pd.read_csv(file_path)
    duplicate_rows_subset = df[df.duplicated(subset=columns)]
    print("Duplicate Rows Based on Subset:")
    print(duplicate_rows_subset)

def display_missing_data(file_path):
    """
    Display columns with missing values in a CSV file.
    """
    df = pd.read_csv(file_path)
    missing_values = df.isna()
    missing_counts = missing_values.sum()
    print("Columns with Missing Values:")
    print(missing_counts[missing_counts > 0])

def display_missing_data_by_columns(file_path, columns):
    """
    Display rows with missing values in specific columns in a CSV file.
    """
    df = pd.read_csv(file_path)
    missing_values_subset = df[columns].isna()
    print("Rows with Missing Values in Subset of Columns:")
    print(df[missing_values_subset.any(axis=1)])

def display_null_data(file_path):
    """
    Display columns with null values in a CSV file.
    """
    df = pd.read_csv(file_path)
    null_values = df.isnull()
    null_counts = null_values.sum()
    print("Columns with Null Values:")
    print(null_counts[null_counts > 0])

def display_null_data_by_columns(file_path, columns):
    """
    Display rows with null values in specific columns in a CSV file.
    """
    df = pd.read_csv(file_path)
    null_values_subset = df[columns].isnull()
    print("Rows with Null Values in Subset of Columns:")
    print(df[null_values_subset.any(axis=1)])

def get_duplicate_seed_ids(file_path):
    """
    Get a list of 'seedId' for rows with duplicate content in a CSV file.
    """
    df = pd.read_csv(file_path)

    rows_by_content = defaultdict(list)

    for i, row in df.iloc[:, 1:].iterrows():
        rows_by_content[tuple(row)].append(df.at[i, 'seedId'])

    duplicate_seed_ids = []
    for content, ids in rows_by_content.items():
        if len(ids) > 1:
            duplicate_seed_ids.extend(ids)

    return duplicate_seed_ids

def get_duplicate_seed_ids(file_path):
    """
    Get a list of sets, where each set contains 'seedId' for rows with duplicate content in a CSV file.
    """
    df = pd.read_csv(file_path)
    rows_by_content = defaultdict(list)
    for i, row in df.iterrows():
        rows_by_content[tuple(row.drop('seedId'))].append(row['seedId'])

    duplicate_seed_ids_sets = []
    for ids in rows_by_content.values():
        if len(ids) > 1:
            duplicate_seed_ids_sets.append(set(ids))

    return duplicate_seed_ids_sets

def get_duplicate_by_column_seed_ids_sets(file_path, columns):
    """
    Get a list of sets, where each set contains 'seedId' for rows with duplicate data based on specific columns in a CSV file.
    """
    df = pd.read_csv(file_path)
    rows_by_content = defaultdict(list)
    for i, row in df.iterrows():
        rows_by_content[tuple(row[columns])].append(row['seedId'])
    duplicate_seed_ids_sets = []
    for ids in rows_by_content.values():
        if len(ids) > 1:
            duplicate_seed_ids_sets.append(set(ids))

    return duplicate_seed_ids_sets


def get_missing_data_seed_ids(file_path):
    """
    Get a list of 'seedId' for rows with missing values in a CSV file.
    """
    df = pd.read_csv(file_path)
    missing_values = df.isna()
    missing_seed_ids = list(df[missing_values.any(axis=1)]['seedId'])
    return missing_seed_ids

def get_missing_data_by_columns_seed_ids(file_path, columns):
    """
    Get a list of 'seedId' for rows with missing values in specific columns in a CSV file.
    """
    df = pd.read_csv(file_path)
    missing_values_subset = df[columns].isna()
    missing_seed_ids = list(df[missing_values_subset.any(axis=1)]['seedId'])
    return missing_seed_ids

def get_null_data_seed_ids(file_path):
    """
    Get a list of 'seedId' for rows with null values in a CSV file.
    """
    df = pd.read_csv(file_path)
    null_values = df.isnull()
    null_seed_ids = list(df[null_values.any(axis=1)]['seedId'])
    return null_seed_ids

def get_null_data_by_columns_seed_ids(file_path, columns):
    """
    Get a list of 'seedId' for rows with null values in specific columns in a CSV file.
    """
    df = pd.read_csv(file_path)
    null_values_subset = df[columns].isnull()
    null_seed_ids = list(df[null_values_subset.any(axis=1)]['seedId'])
    return null_seed_ids


def delete_rows_by_seed_ids(file_path, seed_ids):
    """
    Delete rows from a CSV file based on a list of 'seedId'.
    """

    df = pd.read_csv(file_path)
    df = df[~df['seedId'].isin(seed_ids)]
    df.reset_index(drop=True, inplace=True)
    df.to_csv(file_path, index=False)


def delete_duplicates_by_sets(file_path, duplicate_seed_ids_sets):
    """
    Delete rows from a CSV file based on a list of sets, where each set contains 'seedId' for rows with duplicate content.
    Remove the first element from each set and delete the corresponding rows from the DataFrame.
    """
    df = pd.read_csv(file_path)
    rows_to_delete = set()
    for duplicate_set in duplicate_seed_ids_sets:
        duplicate_set.discard(next(iter(duplicate_set)))
        rows_to_delete.update(duplicate_set)
    df = df[~df['seedId'].isin(rows_to_delete)]
    df.reset_index(drop=True, inplace=True)
    df.to_csv(file_path, index=False)


def update_value_by_seed_id(file_path, seed_id, column_name, new_value):
    """
    Add or replace a new value in the row where 'seedId' matches the specified value in the given column.
    """

    df = pd.read_csv(file_path)

    if seed_id in df['seedId'].values:

        df.loc[df['seedId'] == seed_id, column_name] = new_value
    else:
        new_row = {'seedId': seed_id, column_name: new_value}
        df = df.append(new_row, ignore_index=True)

    df.to_csv(file_path, index=False)


def find_ids_by_columns_and_values(file_path, columns, values):
    """
    Find 'seedId' for rows where the specified columns match the given values in a CSV file.
    """
    df = pd.read_csv(file_path)
    condition = True
    for col, val in zip(columns, values):
        condition = condition & (df[col] == val)
    filtered_rows = df[condition]

    return list(filtered_rows['seedId'])

def add_values_by_id(file_path, columns, values, seed_id):
    """
    Add or replace values in specified columns for a row with a given 'seedId' in a CSV file.
    """
    df = pd.read_csv(file_path)

    row_index = df.index[df['seedId'] == seed_id].tolist()

    if not row_index:
        print(f"'seedId' {seed_id} not found in the CSV file.")
        return
    for col, val in zip(columns, values):
        df.at[row_index[0], col] = val
    df.to_csv(file_path, index=False)
    print(f"Values updated for 'seedId' {seed_id}.")



def get_row_by_id(file_path, seed_id):
    """
    Get the entire row for a given 'seedId' in a CSV file.
    """
    df = pd.read_csv(file_path)
    row = df[df['seedId'] == seed_id]
    if row.empty:
        print(f"'seedId' {seed_id} not found in the CSV file.")
        return None

    return row



def get_rows_by_ids(file_path, seed_ids):
    """
    Get a DataFrame containing rows for the specified 'seedIds' in a CSV file.
    """
    df = pd.read_csv(file_path)
    rows = df[df['seedId'].isin(seed_ids)]
    not_found_ids = set(seed_ids) - set(rows['seedId'])
    if not_found_ids:
        print(f"Warning: 'seedIds' {not_found_ids} not found in the CSV file.")

    return rows




def get_rows_by_indices(file_path, indices):
    """
    Get a DataFrame containing rows for the specified indices in a CSV file.
    """
    df = pd.read_csv(file_path)
    rows = df.iloc[indices]
    invalid_indices = [idx for idx in indices if idx < 0 or idx >= len(df)]
    if invalid_indices:
        print(f"Warning: Invalid indices {invalid_indices} detected.")
    return rows



def get_total_rows(file_path):
    """
    Get the total number of rows in a CSV file.
    """
    df = pd.read_csv(file_path)
    total_rows = len(df)
    return total_rows


def add_column(file_path, column_name):
    """
    Add a new column with the specified name to a CSV file.
    """
    df = pd.read_csv(file_path)
    df[column_name] = None
    df.to_csv(file_path, index=False)


def add_values_at_index(file_path, columns, values, index):
    """
    Add specific values at a given index in columns of a CSV file.
    """
    df = pd.read_csv(file_path)
    for col, val in zip(columns, values):
        df.at[index, col] = val

    df.to_csv(file_path, index=False)


def add_values_at_indexes(file_path, column, values, indexes):
    """
    Add specific values at given indexes in a column of a CSV file.
    """
    df = pd.read_csv(file_path)
    for val, idx in zip(values, indexes):
        df.at[idx, column] = val
    df.to_csv(file_path, index=False)



def get_distinct_column_values(file_path, column_name):
    """
    Get all distinct values in a specific column of a CSV file.
    """
    df = pd.read_csv(file_path)
    distinct_values = df[column_name].unique()
    return distinct_values



def describe_dataset(file_path):
    """
    Describes the dataset present in a CSV file.
    """
    df = pd.read_csv(file_path)
    description = df.describe()

    return description


def calculate_column_variances(file_path, columns):
    """
    Calculate the variance for specified columns in a CSV file.
    """
    df = pd.read_csv(file_path)

    column_variances = df[columns].var()

    return column_variances




def filter_seeds_by_thresholds(file_path, current_values):
    """
    Filter 'seedId' based on given thresholds for numeric features and partial categorical matching for certain columns.
    """
    df = pd.read_csv(file_path)

    categorical_columns = ['water_level', 'soil_type', 'moisture', 'suitable_plantation_location']

    filtered_seeds = df.copy()

    for col in current_values:
        if col in categorical_columns:
            current_value = current_values[col]['current_value']
            if col == 'water_level' or col == 'soil_type' or col == 'moisture' or col == 'suitable_plantation_location':
                filtered_seeds = filtered_seeds[
                    filtered_seeds[col].str.contains(f'.*{current_value}.*', case=False, na=False, regex=True)
                ]
            else:
                filtered_seeds = filtered_seeds.loc[filtered_seeds[col] == current_value]

        elif col != 'threshold':
            min_threshold = current_values[col]['threshold']
            filtered_seeds = filtered_seeds[
                (filtered_seeds[col] >= current_values[col]['current_value'] - min_threshold) &
                (filtered_seeds[col] <= current_values[col]['current_value'] + min_threshold)
                ]

    filtered_seeds.to_csv("file_data.csv", index=False)

    if len(filtered_seeds)>0:
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.axis('off')
        table = ax.table(cellText=filtered_seeds.values, colLabels=filtered_seeds.columns, loc='center', cellLoc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(7)
        table.scale(1.3, 1.3)
        plt.show()
    else:
        print("No seeds found for your specific location......")

    return filtered_seeds

