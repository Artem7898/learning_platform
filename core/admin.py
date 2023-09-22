from django.contrib import admin
from .models import Product, Lesson, ViewHistory


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration_seconds',)
    filter_horizontal = ('products',)


@admin.register(ViewHistory)
class ViewHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'status', 'viewed_at',)

