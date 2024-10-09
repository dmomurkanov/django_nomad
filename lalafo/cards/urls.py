from django.urls import path

from . import views

urlpatterns = [
    path("category", views.CategoryViewSet.as_view()),
    path("item", views.ItemViewSet.as_view()),
    path("item_detail", views.ItemDetailViewSet.as_view()),

]