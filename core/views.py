from rest_framework import generics
from .models import Product, Lesson, ViewHistory
from .serializers import ProductSerializer, LessonSerializer, ViewHistorySerializer
import logging


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class LessonListCreateView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class ViewHistoryListCreateView(generics.ListCreateAPIView):
    queryset = ViewHistory.objects.all()
    serializer_class = ViewHistorySerializer


# Получите логгер для вашего модуля

logger = logging.getLogger(__name__)

# Пример использования логгера для записи сообщения


def some_function():
    logger.debug('Это отладочное сообщение')
    logger.info('Это информационное сообщение')
    logger.warning('Это предупреждение')
    logger.error('Это ошибка')

