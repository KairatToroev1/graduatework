from django.contrib import admin
from place.models import Tour,Company,Tour_abroad,Category,TourPhoto,\
    About_us,Program,Rating,RatingStar,Review,Orders

class TourImageAdmin(admin.StackedInline):
    model = TourPhoto
@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    inlines = [TourImageAdmin]
    class Meta:
       model = Tour
@admin.register(TourPhoto)
class TourImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Company)
admin.site.register(Category)
admin.site.register(Tour_abroad)
admin.site.register(About_us)
admin.site.register(Program)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Review)
admin.site.register(Orders)
