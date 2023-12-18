import os
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render
from sklearn.preprocessing import LabelEncoder
from seeds_wild_ai_system.settings import BASE_DIR
from src.AI.apps.recommendation.recommendations.recommend_content_based import predict
from src.AI.machine_learning.recommendation.knn_train import train_model
STATIC_DIR = os.path.join(BASE_DIR, 'static')


def home_page(request):
    return render(request, 'templates/test_model.html')


def train_model_view(request):
    train_model()

    return HttpResponse("Model trained successfully!")


def recommend(request):
    if request.method == 'POST':
        temperature = float(request.POST.get('temperature'))
        humidity_rate = float(request.POST.get('humidity_rate'))
        sunshine_rate = float(request.POST.get('sunshine_rate'))
        rainfall_rate = float(request.POST.get('rainfall_rate'))
        moisture = int(request.POST.get('moisture'))
        soil_type = request.POST.get('soil_type')
        country = request.POST.get('country')
        labelencoder = LabelEncoder()

        country_encode = labelencoder.fit_transform([country])[0]
        print(country_encode)
        input_data = {
            'temperature': temperature,
            'soil_num': soil_type,
            'moisture': moisture,
            'humidity_rate_tens': humidity_rate,
            'rainfall_tens': rainfall_rate,
            'sunshine_rate_tens': sunshine_rate,


        }
        prediction = predict(input_data)
        if prediction:

            return render(request, 'templates/recommended_seeds.html', {'seeds': prediction})
        else:
            return HttpResponse("There is No model yet...")
    return render(request, 'templates/test_model.html')


def remove_model(request):
    model_file_path = 'trained_model.pkl'
    if os.path.exists(model_file_path):
        os.remove(model_file_path)
    model_cache_key = 'trained_model'
    cache.delete(model_cache_key)

    return HttpResponse("Trained model removed from cache and deleted from disk!")
