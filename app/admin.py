from django.contrib import admin
from app import models


admin.site.register(models.Cat)

admin.site.register(models.Dog)


class OwnerAdmin(admin.ModelAdmin):

    def queryset(self, request):
        qs = super(OwnerAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


admin.site.register(models.Owner, OwnerAdmin)