import joblib
import pandas as pd

from src.recommendation.models import RecommendationAiModel
from src.recommendation.process_data.process import get_processed_data
import sklearn
print("scikit-learn version:", sklearn.__version__)
print("joblib version:", joblib.__version__)

def predict(input_data):
    _file = RecommendationAiModel.objects.last()
    input_data = get_processed_data(input_data)

    model_file = _file.model_file
    print(model_file)

    knn_model = joblib.load(model_file)


    if knn_model:
        # print("Classes:", knn_model.classes_)
        features = ['temperature', 'soil_num', 'water_level', 'moisture', 'humidity_rate_tens', 'rainfall_tens',
                    'hydrometry_rate_tens', 'sunshine_rate_tens']

        input_df = pd.DataFrame([input_data], columns=features)
        prediction = knn_model.predict(input_df)
        print("Indices:", prediction)

        return prediction
    else:
        return None
