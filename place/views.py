from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView,ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import status,viewsets
from django_filters.rest_framework import DjangoFilterBackend






from place.models import Tour,Company,Tour_abroad,Category,TourPhoto,\
    About_us,Program,Review,Rating,Orders
from place.serializers import TourSerializer,CompanySerializer,TourAbroadSerializer,TourPhotoSerializer,\
    CategorySerializer,AboutUsSerializer,ProgramSerializer,ReviewCreateSerializer,CreateRatingSerializer,\
    OrderSerializer,AddTourSerializer,AllOrderSerializer
from place.permissions import IsOwnerOrReadOnly


class AllPagination(PageNumberPagination):
    page_size= 10
    page_size_query_param = 'page_size'
    max_page_size = 100



class TourViewSet(ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes= [AllowAny]
    pagination_class = AllPagination
    filter_backends=[DjangoFilterBackend,SearchFilter]
    filter_fields = ['id', 'price']
    search_filters = ['name','price','category']

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)




class TourDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes= [IsOwnerOrReadOnly,]




class CompanyListView(APIView):
    pagination_class = AllPagination
    permission_classes = [AllowAny]
    filter_backends=[DjangoFilterBackend]
    filter_fields = ['id']

    def get(self, request):
        queryset = Company.objects.all()
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyDetailView(APIView):
    permission_classes = [AllowAny ]


    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        queryset = self.get_object(pk)
        serializer = CompanySerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk):
        queryset = self.get_object(pk)
        serializer = CompanySerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TourAbroadListView(APIView):
    pagination_class = AllPagination
    permission_classes = [AllowAny]
    filter_backends=[DjangoFilterBackend]
    filter_fields = ['id']

    def get(self, request):
        queryset = Tour_abroad.objects.all()
        serializer = TourAbroadSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TourAbroadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TourAbroadDetailView(APIView):
    permission_classes = [AllowAny ]



    def get_object(self, pk):
        try:
            return Tour_abroad.objects.get(pk=pk)
        except Tour_abroad.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        queryset = self.get_object(pk)
        serializer = TourAbroadSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk):
        queryset = self.get_object(pk)
        serializer = TourAbroadSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryListView(APIView):
    pagination_class = AllPagination
    permission_classes = [AllowAny ]

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
    permission_classes = [AllowAny ]


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


class TourPhotoView(APIView):
    permission_classes = [AllowAny ]


    def get(self, request):
        queryset = TourPhoto.objects.all()
        serializer = TourPhotoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TourPhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



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


class AboutUsView(APIView):
    permission_classes = [IsOwnerOrReadOnly ]

    def get(self, request):
        queryset = About_us.objects.all()
        serializer = AboutUsSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AboutUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ProgramView(APIView):
    permission_classes = [AllowAny ]

    def get(self, request):
        queryset = Program.objects.all()
        serializer = ProgramSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProgramSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = ProgramSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewCreateView(APIView):
    permission_classes = [AllowAny ]


    def get(self, request):
        queryset = Review.objects.all()
        serializer = ReviewCreateSerializer(queryset, many=True)
        return Response(serializer.data)


    def post(self, request):
        review = ReviewCreateSerializer(data=request.data)
        if review.is_valid():
            review.save()
        return Response(status=201)

    def delete(self, request, pk):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AddStarRatingView(APIView):
    permission_classes = [AllowAny ]


    def get(self, request):
        queryset = Rating.objects.all()
        serializer = CreateRatingSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreateRatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ip=self.request.user)
            return Response(status=201)
        else:
            return Response(status=400)

    def delete(self, request, pk):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AddTourOrderView(APIView):
    permission_classes = [AllowAny ,IsAuthenticatedOrReadOnly]

    def post(self, request):
        serializer = AddTourSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner_id=request.user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AllTourOrderView(APIView):
    permission_classes = [AllowAny ,IsAuthenticatedOrReadOnly]

    def get(self,request):
        queryset = Orders.objects.filter(owner_id = request.user.id)
        serializer = AllOrderSerializer(queryset, many=True)
        return Response(serializer.data)


class OrderDetail(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        queryset = Orders.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)


    def put(self, request, pk):
        queryset = Orders.objects.all()
        serializer = OrderSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
