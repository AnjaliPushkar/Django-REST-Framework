from django.urls import path
from .views import article_list, article_detial

urlpatterns = [
    path('article/', article_list),
    path('detail/<int:pk>', article_detial),

]
