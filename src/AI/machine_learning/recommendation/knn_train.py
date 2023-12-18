import os

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

from seeds_wild_ai_system.settings import BASE_DIR
from src.AI.data_process.clean_data.clean_model import get_duplicate_by_column_seed_ids_sets_df
from src.AI.data_process.pre_process_data.process import processed_duplicate_data

STATIC_DIR = os.path.join(BASE_DIR, 'static')

def train_model(file_path):
    df = pd.read_csv(file_path)
    df_subset = df
    df_subset = df_subset.dropna()

    label_encoder = LabelEncoder()
    df_subset['suitable_plantation_location'] = label_encoder.fit_transform(df_subset['suitable_plantation_location'])

    features = ['temperature', 'soil_num', 'water_level', 'moisture', 'humidity_rate_tens', 'rainfall_tens',
                'hydrometry_rate_tens', 'sunshine_rate_tens']

    seeds_ids_set = get_duplicate_by_column_seed_ids_sets_df(df_subset, features)
    processed_data = processed_duplicate_data(df_subset, seeds_ids_set)

    X = processed_data[features]
    y = processed_data['seedId_seedName']

    knn_model = KNeighborsClassifier()

    param_grid = {
        'n_neighbors': [1, 2, 3],
        'weights': ['uniform', 'distance'],
        'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute']
    }

    grid_search = GridSearchCV(knn_model, param_grid, cv=KFold(shuffle=True, random_state=None))
    grid_search.fit(X, y)

    best_model = grid_search.best_estimator_

    predictions = best_model.predict(X)

    accuracy = accuracy_score(y, predictions)

    print(f'Best Model Accuracy: {accuracy}')

    return best_model

