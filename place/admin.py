from django.contrib import admin
from place.models import Tour,Company,Tour_abroad,Category,TourPhoto,\
    About_us


admin.site.register(Tour)
admin.site.register(Company)
admin.site.register(Category)
admin.site.register(Tour_abroad)
admin.site.register(TourPhoto)
# admin.site.register(Favorable_prices)
admin.site.register(About_us)
