from django.urls import path

from apps.nutrition_api.views import ExcelUpload, NutritionList


urlpatterns = [
    path('excel/upload/', ExcelUpload.as_view(), name='excel_upload'),
    path('nutrition/list/', NutritionList.as_view(), name='nutrition_list'),

]