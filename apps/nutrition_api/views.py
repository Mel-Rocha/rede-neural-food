import requests
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

from config.settings import API_ENDPOINT, API_TOKEN


class ExcelUpload(APIView):
    """
     Chama o endpoint da api para fazer o upload da planilha Nutrition.

     Obrigatório fornecer:

     @File: Multipart/FormData {"file": arquivo.xlsx} (fornecer em body)
     @access_token: string (Bearer Token) (fornecer em header)
     """
    #permission_classes = (IsAuthenticated,)

    @staticmethod
    def post(request):
        file = request.FILES.get('file')
        if not file:
            return JsonResponse(request, {"message": "Envie a planilha "
                                                          "para prosseguir."},
                                     status_code=400)
        files = {'file': file}

        url = f"{API_ENDPOINT}/nutrition/upload/"
        headers = {
            "Authorization": f"Bearer {API_TOKEN}"
        }
        response = requests.post(url, files=files, headers=headers)

        api_response = response.json()

        if response.status_code == 201:
            return JsonResponse({
                "message": "Upload realizado com sucesso!",
                "api_response": api_response
            }, status=201)
        else:
            return JsonResponse({
                "message": "Erro no upload do arquivo.",
                "api_response": api_response
            }, status=400)
