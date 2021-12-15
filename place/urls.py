from rest_framework.routers import SimpleRouter
from place.views import TourViewSet,CompanyViewSet,TourPhotoViewSet,\
    AboutUsViewSet,CheapestTours,TourAbroadViewSet,TourDetailAPIView,CategoryDetailView,CategoryListView
from django.urls import path

router = SimpleRouter()

router.register('tour/', TourViewSet)
router.register('company/', CompanyViewSet)
router.register('tour_abroad/', TourAbroadViewSet)
# router.register('category/', CategoryViewSet)
router.register('tour_photo/', TourPhotoViewSet)
router.register('about_us/', AboutUsViewSet)

urlpatterns = [
    path('<int:pk>/least-price-tours/', CheapestTours.as_view()),
    path('tour/<str:pk>/', TourDetailAPIView.as_view()),
    path('category/<str:pk>/', CategoryListView.as_view()),
]

urlpatterns += router.urls