from django.urls import path, include
from rest_framework import routers
from Escuela import views

router = routers.DefaultRouter()

router.register('school', views.EscuelaView)
router.register('profesor', views.ProfesorView)

urlpatterns = [
    path('', include(router.urls)),
]
