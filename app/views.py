from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import UploadForm
import pytesseract
from PIL import Image
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.contrib import messages
from django.urls import reverse

# Create your views here.

# Change this according to your computers location
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class Image_Upload(CreateView):
    form_class = UploadForm
    template_name = "index.html"
    success_url = "/"


@csrf_exempt
def process_image(request):
    if request.method == 'POST':
        response_data = {}
        upload = request.FILES['file']
        content = pytesseract.image_to_string(Image.open(upload))
        response_data['content'] = content
        messages.success(request, response_data)

        return HttpResponseRedirect(reverse("app:home"))
