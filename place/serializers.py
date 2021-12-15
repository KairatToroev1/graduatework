from rest_framework import serializers
from place.models import Tour,Company,Tour_abroad,Category,TourPhoto,\
    About_us,Program

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields=['name','price','company','tour_features','category',
                'included','date_of_departure','arrival_date','take_with_you',]


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields = ['name','phone_number','grade', ]


class TourAbroadSerializer(serializers.ModelSerializer):
    class Meta:
        model= Tour_abroad
        fields=['name','price','tour_features', 'company','required_documents','places_of_visit','date']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields= ['name', ]

class TourPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model=TourPhoto
        fields=['name','image','tour', ]

# class FavorablePricesSerializer(serializers.Serializer):
#     model=Favorable_prices
#     fields=['name','price',]

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model=About_us
        fields=['company','body', ]

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ['tour','program',]