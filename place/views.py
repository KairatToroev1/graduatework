from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
# from django.db.models import Min
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import status


from place.models import Tour,Company,Tour_abroad,Category,TourPhoto,\
    About_us,Program
from place.serializers import TourSerializer,CompanySerializer,TourAbroadSerializer,TourPhotoSerializer,\
    CategorySerializer,AboutUsSerializer,ProgramSerializer

class AllPagination(PageNumberPagination):
    page_size= 2
    page_size_query_param = 'page_size'
    max_page_size = 18


class TourViewSet(ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes=[IsAuthenticated, ]
    pagination_class = AllPagination
    filter_backends=[SearchFilter]
    search_filters = ['name','price','category']

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

class TourDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = AllPagination
    permission_classes = [IsAuthenticated, ]


class TourAbroadViewSet(ModelViewSet):
    queryset = Tour_abroad.objects.all()
    serializer_class = TourAbroadSerializer
    permission_classes = [IsAuthenticated, ]

class CategoryListView(APIView):
    pagination_class = AllPagination
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        snippets = Category.objects.all()
        serializer = CategorySerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CategoryDetailView(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = CategorySerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = CategorySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TourPhotoViewSet(ModelViewSet):
    queryset = TourPhoto.objects.all()
    serializer_class = TourPhotoSerializer
    pagination_class = AllPagination
    permission_classes = [IsAuthenticated, ]
#
# class FavorablePricesViewSet(ModelViewSet):
#     queryset = Favorable_prices.


class CheapestTours(APIView):

    def get(self, request, pk):
        company = get_object_or_404(Company, id=pk)
        tours = company.tourcompany.all()
        prices_lst = []
        for tour in tours:
            other_tours = Tour.objects.filter(name=tour.name).exclude(id=tour.id)
            for other_tour in other_tours:
                company_tour_dict = {}
                company_tour_dict['company'] = other_tour.company.name
                company_tour_dict['price'] = other_tour.price
                prices_lst.append(company_tour_dict)
        return Response({'price_list': prices_lst})


class AboutUsViewSet(ModelViewSet):
    queryset = About_us.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsAuthenticated, ]

class ProgramViewSet(ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [IsAuthenticated, ]