from django.urls import path
from src.AI.apps.recommendation.views import *
app_name = "recommendation"
urlpatterns = [
    path('', home_page, name="home"),
    path('recommend', recommend, name='recommend'),
    path('trainmodel', train_model_view, name="trainmodel"),
    path('remove', remove_model, name="remove")
]
