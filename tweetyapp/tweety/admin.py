from django.contrib import admin
from .models import Tweety, Profile, Predicted_Tweets

# Register your models here.
admin.site.register(Tweety)
admin.site.register(Profile)
admin.site.register(Predicted_Tweets)
