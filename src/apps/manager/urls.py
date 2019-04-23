from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'teams', views.TeamView, base_name='Team')
router.register(r'matches', views.MatchView, base_name='Match')
router.register(r'statistic', views.StatisticView, base_name='Statistic')
router.register(r'country', views.CountryView, base_name='Country')
router.register(r'tournaments', views.TournamentView, base_name='Tournament')


schema_view = get_swagger_view(title='API')
app_name = "manager"

urlpatterns = [
    path('', include(router.urls)),
    path('docs/', schema_view)
]



