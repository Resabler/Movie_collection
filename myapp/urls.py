from django.urls import path
from .views import Registerationview,Collectionlistcreateview,Collectiondestroyupdateview,Moviedestroyupdateview,Movielistcreateview

urlpatterns = [
    path('register/', Registerationview.as_view(), name='register'),
      path('collection/',Collectionlistcreateview.as_view()),
    path('collection/<int:pk>/',Collectiondestroyupdateview.as_view()),
    path('movies/',Movielistcreateview.as_view()),
    path('movies/<int:pk>/',Moviedestroyupdateview.as_view()),
]
