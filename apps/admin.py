from django.contrib import admin

from apps.models import Course, CourseCategory, StudentProxyUser, TeacherProxyUser, AdminProxyUser
from apps.models import User


# Register your models here.
# class ProductImageStackedInline(StackedInline):
#     model = ProductImage
#     extra = 1
#
#
# @admin.register(Product)
# class ProductAdmin(ModelAdmin):
#     autocomplete_fields = ['category']
#     inlines = [ProductImageStackedInline]
#
#
# @admin.register(Category)
# class CategoryAdmin(ModelAdmin):
#     search_fields = ['title']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'image']


@admin.register(StudentProxyUser)
class StudentProxyUserAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(status='student')


@admin.register(TeacherProxyUser)
class TeacherProxyUserAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(status='teacher')


@admin.register(AdminProxyUser)
class AdminProxyUserAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(status='admin')
