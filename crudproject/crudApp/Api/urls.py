from django.urls import path,include
from crudApp.Api import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('stuinfo',views.StudentInfo,basename='stuinfo')

urlpatterns = [
    path('',include(router.urls))
]
