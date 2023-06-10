from django.contrib import admin
from .models import Submit

# Register your models here.


class productAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    list_display = ("title", "id")


admin.site.register(Submit)
