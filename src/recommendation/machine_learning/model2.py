import os

import pandas as pd
from django.conf import settings
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

from seeds_wild_ai_system.settings import BASE_DIR

STATIC_DIR = os.path.join(BASE_DIR, 'static')

def model():

    file_path = os.path.join(STATIC_DIR , 'data2.csv')
    df = pd.read_csv(file_path)

    df_subset = df
    df_subset = df_subset.dropna()

    label_encoder = LabelEncoder()
    df_subset['soil_type'] = label_encoder.fit_transform(df_subset['soil_type'])
    df_subset['moisture'] = label_encoder.fit_transform(df_subset['moisture'])
    df_subset['water_level'] = label_encoder.fit_transform(df_subset['water_level'])
    df_subset['suitable_plantation_location'] = label_encoder.fit_transform(df_subset['suitable_plantation_location'])

    X = df_subset[
        ['season', 'soil_num', 'water_level', 'moisture', 'humidity_rate_tens', 'rainfall_tens', 'hydrometry_rate_tens',
         'sunshine_rate_tens']]
    y = df_subset['seed_name']

    knn_model = KNeighborsClassifier()

    param_grid = {
        'n_neighbors': [5, 7, 9],
        'weights': ['uniform', 'distance'],
        'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute']
    }
    grid_search = GridSearchCV(knn_model, param_grid, cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=None))
    grid_search.fit(X, y)

    best_model = grid_search.best_estimator_

    predictions = best_model.predict(X)

    accuracy = accuracy_score(y, predictions)
    print(f'Best Model Accuracy: {accuracy}')
    print(classification_report(y, predictions))
