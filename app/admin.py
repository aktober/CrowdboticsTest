from django.contrib import admin
from app import models


@admin.register(models.Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday', 'owner')

    def get_queryset(self, request):
        qs = super(CatAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner__user=request.user)


@admin.register(models.Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday', 'owner')

    def get_queryset(self, request):
        qs = super(DogAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner__user=request.user)


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', )
    fields = ['name', ]


admin.site.register(models.Owner, OwnerAdmin)
