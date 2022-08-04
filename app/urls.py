from django.urls import path
from django.views.i18n import JavaScriptCatalog
from . import views

urlpatterns = [
    path('', views.new_appointment),
    path('js118n',JavaScriptCatalog.as_view(),name = 'js-catlog')
]