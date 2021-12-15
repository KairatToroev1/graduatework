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

# class Gid(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     phone_number = models.TextField()
#
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Гид'
#         verbose_name_plural = 'Гиды'
class Company(models.Model):
    name = models.CharField(max_length=128)
    # tour = models.ForeignKey(Place, on_delete=models.CASCADE, null=True,related_name='tour')
    # our_team = models.TextField()
    phone_number = models.TextField()
    grade = models.IntegerField()
    # discounts = models.ForeignKey(Place, on_delete=models.CASCADE, null=True,related_name='discounts')


    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name

class Tour(models.Model):
    # class StatusType(models.TextChoices):
    #     REGISTRATION = 'registration'
    #     LVL1 = 'lvl1'
    #     LVL2 = 'lvl2'
    #
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='place')
    # worker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
    #                            related_name='handled_place')
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='tourcompany')
    name = models.CharField(max_length=128)
    price = models.IntegerField()
    included = models.TextField()
    # places_of_visit = models.TextField()
    date_of_departure = models.DateTimeField()
    arrival_date = models.DateTimeField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categorytour')
    take_with_you = models.TextField()
    tour_features = models.TextField()
    # gid = models.ForeignKey(Gid, on_delete=models.CASCADE,null=True,related_name='gid')
    # discounts = models.ForeignKey(Place, on_delete=models.CASCADE, null=True,related_name='discounts')





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
    name = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='tourphoto')
    image = models.ImageField(upload_to='pictures/%Y/%m/%d/',null=True)
    tour = models.ForeignKey(Tour,on_delete=models.SET_NULL, related_name='photos',null=True)

    class Meta:
        verbose_name = 'Фото туров'
        verbose_name_plural = verbose_name


    # def __str__(self):
    #     return self.name
#выгодные цены моделька

# class Favorable_prices(models.Model):
#     name = models.ForeignKey(Tour,on_delete=models.CASCADE,related_name='tourname')
#     price = models.IntegerField()
#


class About_us(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='about_us')
    body = models.TextField()

    def __str__(self):
        return self.body

    