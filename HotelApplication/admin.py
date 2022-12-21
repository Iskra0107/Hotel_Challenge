from .models import Hotel, Review, Favourite
from django.contrib import admin


# Register your models here.

class ReviewAdmin(admin.StackedInline):
    model = Review
    extra = 0

    def has_add_permission(self, request, obj=None):
        return True

    readonly_fields = ('user',)


class HotelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False;

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False;

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False;

    inlines = [ReviewAdmin, ]


admin.site.register(Hotel, HotelAdmin)

admin.site.register(Favourite)
