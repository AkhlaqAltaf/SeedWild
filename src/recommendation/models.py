from django.db import models


# Create your models here.


class RecommendationAiModel(models.Model):
    model_file = models.FileField(default=None, upload_to="ai/recommendation")
    model_name = models.CharField(default="knn", max_length=50)

    def __str__(self):
        return self.model_name
