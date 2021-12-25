from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=128)


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=128)
    phone_number = models.TextField()
    grade = models.IntegerField()


    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name

class Tour(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='tourcompany')
    name = models.CharField(max_length=128)
    price = models.IntegerField()
    individual_tour = models.BooleanField(default=True)
    general_tour = models.BooleanField(default=True)
    included = models.TextField()
    date_of_departure = models.DateTimeField()
    arrival_date = models.DateTimeField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categorytour')
    take_with_you = models.TextField()
    tour_features = models.TextField()
    image = models.ImageField(upload_to='pictures', null=True, blank=True, verbose_name='Изображение')
    book_your_place= models.URLField(max_length=200,null=True)
    amount = models.PositiveIntegerField(
        default=18,
        verbose_name='Количество мест',
        null=True)



    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'

    def __str__(self):
        return self.name

class Program(models.Model):
    tour = models.ForeignKey(Tour,on_delete=models.CASCADE,related_name='programtour')
    program = models.TextField()

    class Meta:
        verbose_name = 'Программа'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.program

class Tour_abroad(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='companyabroad')
    price = models.IntegerField()
    required_documents = models.TextField()
    date = models.DateTimeField()
    tour_features = models.TextField()
    places_of_visit = models.TextField()

    class Meta:
        verbose_name = 'За границей'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class TourPhoto(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pictures/%Y/%m/%d/',null=True)
    tour_id = models.ForeignKey(Tour,on_delete=models.SET_NULL, related_name='tour_photo',null=True)

    class Meta:
        verbose_name = 'Фото туров'
        verbose_name_plural = verbose_name




class About_us(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='about_us')
    body = models.TextField()

    def __str__(self):
        return self.body


class RatingStar(models.Model):
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Rating(models.Model):
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        verbose_name="Тур",
        related_name="ratings"
    )

    def __str__(self):
        return f"{self.star} - {self.tour}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Review(models.Model):
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    tour = models.ForeignKey(Tour, verbose_name="Тур", on_delete=models.CASCADE, related_name="reviews")
    company = models.ForeignKey(Company,verbose_name="Компания",on_delete=models.CASCADE,null=True,related_name="review")

    def __str__(self):
        return f"{self.name} - {self.tour}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


# class AddTourOrder(models.Model):
#

class Orders(models.Model):
    tour = models.ForeignKey(Tour,on_delete=models.CASCADE,related_name='orderproduct')
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='owner')
    total_amount = models.PositiveIntegerField(verbose_name='Общая сумма',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_finish = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Заказ тура"
        verbose_name_plural = verbose_name