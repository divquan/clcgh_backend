"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.urls import include
from .views import createUser
from rest_framework.decorators import api_view, permission_classes


from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def test_authorization(request):
#     # This will only be executed if the user is authenticated
#     return JsonResponse({"message": f"Hello, {request.user.username}. You are authenticated!"})


urlpatterns = [
    # path('create-user', createUser ),
    # path('authorize', test_authorization ),
]