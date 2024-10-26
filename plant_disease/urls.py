from django.urls import path
from . import views

from  plant_disease.view import TypeView, plantView ,chatbotView, symptomeView , preventionView
from .views import dashboard_view

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),  # Home page URL
    path('predict/', views.predict, name='predict'),  # Predict page URL
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('backoffice/', views.backoffice_view, name='backoffice'),
    # *************

    path('typePlantes/', TypeView.TypePlanteListView.as_view(), name='typePlantes-list'),
    path('typePlantes/<int:pk>/', TypeView.TypePlanteDetailView.as_view(), name='typePlantes-detail'),
    path('typePlantes/create/', TypeView.TypePlanteCreateView.as_view(), name='typePlantes-create'),
    path('typePlantes/<int:pk>/update/', TypeView.TypePlanteUpdateView.as_view(), name='typePlantes-update'),
    path('typePlantes/<int:pk>/delete/', TypeView.TypePlanteDeleteView.as_view(), name='typePlantes-delete'),

    #**********************
    path('plantes/', plantView.PlanteListView.as_view(), name='plante-list'),
    path('plantes/<int:pk>/', plantView.PlanteDetailView.as_view(), name='plante-detail'),
    path('plantes/create/', plantView.PlanteCreateView.as_view(), name='plante-create'),
    path('plantes/<int:pk>/update/', plantView.PlanteUpdateView.as_view(), name='plante-update'),
    path('plantes/<int:pk>/delete/', plantView.PlanteDeleteView.as_view(), name='plante-delete'),
    #******************************
 
      path('chatbot/', chatbotView.chat_interface, name='chat_interface'),  # GET request for the chat interface
    path('chatbot/api/', chatbotView.chat, name='chatbot_api'),  # POST request for handling chat messages


     # URLs for Symptôme
   path('symptomes/', symptomeView.SymptomeListView.as_view(), name='symptome-list'),  # Corrected: Use .as_view()
    path('symptomes/<int:pk>/', symptomeView.SymptomeDetailView.as_view(), name='symptome-detail'),  # Detail view
    path('symptomes/add/', symptomeView.SymptomeCreateView.as_view(), name='symptome-create'),  # Create view
    path('symptomes/<int:pk>/edit/', symptomeView.SymptomeUpdateView.as_view(), name='symptome-update'),  # Update view
    path('symptomes/<int:pk>/delete/', symptomeView.SymptomeDeleteView.as_view(), name='symptome-delete'),  # Delete view
    # URLs for Prevention
    path('preventions/', preventionView.PreventionListView.as_view(), name='prevention-list'),  # List view
    path('preventions/<int:pk>/', preventionView.PreventionDetailView.as_view(), name='prevention-detail'),  # Detail view
    path('preventions/add/', preventionView.PreventionCreateView.as_view(), name='prevention-create'),  # Create view
    path('preventions/<int:pk>/edit/', preventionView.PreventionUpdateView.as_view(), name='prevention-update'),  # Update view
    path('preventions/<int:pk>/delete/', preventionView.PreventionDeleteView.as_view(), name='prevention-delete'),  # Delete view
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    