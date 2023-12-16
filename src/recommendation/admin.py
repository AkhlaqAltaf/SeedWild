from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import (
    RecommendationAiModel
)


@admin.register(RecommendationAiModel)
class RecommendationAiModel(admin.ModelAdmin):
    list_display = ['model_name']
    search_fields = ['model_name']
