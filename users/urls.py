from django.urls import path
from .views import UserListView, UserDetail

urlpatterns = [
    path('', UserListView.as_view()),
    path('<int:pk>', UserDetail.as_view()),
]
