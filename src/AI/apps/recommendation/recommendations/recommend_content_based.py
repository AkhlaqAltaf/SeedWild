import joblib
import pandas as pd

from src.AI.apps.recommendation.models import RecommendationAiModel
from src.AI.data_process.post_process.recommend_input_process import get_processed_data


def predict(input_data):
    _file = RecommendationAiModel.objects.last()
    input_data = get_processed_data(input_data)

    model_file = _file.model_file
    print(model_file)

    knn_model = joblib.load(model_file)

    if knn_model:

        features = ['temperature', 'soil_num', 'moisture', 'humidity_rate_tens', 'rainfall_tens',
                    'sunshine_rate_tens']

        input_df = pd.DataFrame([input_data], columns=features)
        prediction = knn_model.predict(input_df)
        print("Indices:", prediction)

        return prediction
    else:
        return None
