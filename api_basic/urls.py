from django.urls import path
from .views import article_list, article_detial, ArticleAPIView, ArticleDetails, GenericAPIView

urlpatterns = [
    # path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    # path('detail/<int:pk>', article_detial),
    path('detail/<int:id>', ArticleDetails.as_view()),
    path('generic/article/<int:id>', GenericAPIView.as_view()),

]
