from django.urls import include, path
from rest_framework import routers

from .views import QuestionViewSet
# from IceBreakerProj.IceBreakers import views
from . import views
# from django.views import RandomQuestion
from .views import RandomQuestion

router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewSet)
# router.register(r'randomQuestions', views.RandomQuestion)

urlpatterns = [
    # path('', views.QuestionViewSet.as_view(), name='questions'),
    path('', include(router.urls)),
    path('questions', views.getData, name='getData'),
    # path('random', views.getRandom, name='getRandom')
    path('random/', RandomQuestion.as_view(), name='random'),
    path('test/', views.my_test, name='my_test')
]