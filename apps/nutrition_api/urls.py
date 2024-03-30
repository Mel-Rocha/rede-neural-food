from django.urls import path

from apps.nutrition_api.views import ExcelUpload


urlpatterns = [
    path('excel/upload/', ExcelUpload.as_view(), name='excel_upload'),

]