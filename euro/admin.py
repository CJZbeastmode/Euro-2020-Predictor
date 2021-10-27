from django.contrib import admin
from .models import Prediction, NewsArticle, Newsletter

# Register your models here.

admin.site.register(Prediction)
admin.site.register(NewsArticle)
admin.site.register(Newsletter)
