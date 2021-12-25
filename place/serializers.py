from rest_framework import serializers
from place.models import Tour,Company,Tour_abroad,Category,TourPhoto,\
    About_us,Program,Review,Rating,Orders

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields=['name','price','company','tour_features','category',
                'included','date_of_departure','arrival_date','take_with_you','image','book_your_place']


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
        fields=['name','image','tour_id', ]


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model=About_us
        fields=['company','body', ]

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ['tour','program',]



class ReviewCreateSerializer(serializers.ModelSerializer):
    """Добавление отзыва"""

    class Meta:
        model = Review
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    """Вывод отзыво"""

    class Meta:
        model = Review
        fields = ("name", "text", "parent")


class CreateRatingSerializer(serializers.ModelSerializer):
    """Добавление рейтинга пользователем"""
    class Meta:
        model = Rating
        fields = ("star", "tour")

    def create(self, validated_data):
        rating = Rating.objects.update_or_create(
            tour=validated_data.get('tour', None),
            defaults={'star': validated_data.get("star")}
        )
        return rating
#

class OrderSerializer(serializers.ModelSerializer):
    tour = TourSerializer(read_only=True)
    class Meta:
        model = Orders
        fields = ['id','tour','owner','total_amount','created_at','is_active','is_finish']

class AllOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id','tour','owner','total_amount','created_at','is_active','is_finish']

class AddTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id','tour','owner','total_amount','created_at','is_active','is_finish']