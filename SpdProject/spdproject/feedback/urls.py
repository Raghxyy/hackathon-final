from django.urls import path
from .views import feedback_view, thank_you_view, feedback_graph, feedback_dashboard

urlpatterns = [
    path('', feedback_view, name='feedback'),
    path('thank-you/', thank_you_view, name='thank_you'),
    path('feed', feedback_graph, name='feedback_graph'),
    path('dashboard',feedback_dashboard, name='feedback_dashboard'),

]
