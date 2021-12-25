from rest_framework.routers import SimpleRouter
from place.views import TourViewSet,CompanyListView,TourPhotoView,\
    AboutUsView,CheapestTours,TourAbroadListView,TourDetailAPIView,CategoryDetailView,CategoryListView,\
    ReviewCreateView,AddStarRatingView,ProgramView,OrderDetail,AllTourOrderView
from django.urls import path

router = SimpleRouter()

router.register('tour', TourViewSet)


urlpatterns = [
    path('<int:pk>/least-price-tours/', CheapestTours.as_view()),
    path('tour/<str:pk>/', TourDetailAPIView.as_view()),
    path('category/', CategoryListView.as_view()),
    path('company/',CompanyListView.as_view()),
    path('tour_abroad/',TourAbroadListView.as_view()),
    path('tour_image/',TourPhotoView.as_view()),
    path("review/", ReviewCreateView.as_view()),
    path("rating/", AddStarRatingView.as_view()),
    path("program/",ProgramView.as_view()),
    path("about_us/",AboutUsView.as_view()),
    path("order/",OrderDetail.as_view()),
    path("all_order/",AllTourOrderView.as_view()),
]

urlpatterns += router.urls