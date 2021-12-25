from django.urls import path
from accounts.views import RegistrationAPIView, LoginAPIView,UserViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('all_accounts', UserViewSet)



urlpatterns = [
    path('register/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),

]


urlpatterns += router.urls
