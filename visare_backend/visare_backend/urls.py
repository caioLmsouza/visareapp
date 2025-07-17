"""
URL configuration for visare_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import login_page
from core.views import dashboard, pacientes, clinicas, consultas, fichas, relatorios, configuracoes, forgot_password
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from consultas.views import agenda_consultas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_page, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('pacientes/', pacientes, name='pacientes'),
    path('clinicas/', clinicas, name='clinicas'),
    path('consultas/', consultas, name='consultas'),
    path('fichas/', fichas, name='fichas'),
    path('relatorios/', relatorios, name='relatorios'),
    path('configuracoes/', configuracoes, name='configuracoes'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('api/', include('core.urls')),
    path('api/', include('pacientes.urls')),
    path('api/', include('clinicas.urls')),
    path('api/', include('agendamentos.urls')),
    path('api/', include('receitas.urls')),
    path('api/consultas/agenda/', agenda_consultas, name='agenda_consultas'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
