"""
arquivo onde é definido as rotas da aplicacao
"""
from django.contrib import admin
from django.urls import path, include
# from cursos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('curso/', include('cursos.urls')),

    path('', include('cursos.urls')),
]
