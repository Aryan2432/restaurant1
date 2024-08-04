from django.contrib import admin
from book.models import one

class one2(admin.ModelAdmin):
    a=('a1','a2','a3','a4','a5','a6')
admin.site.register(one,one2)

# Register your models here.
