from django.http import HttpResponse
from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
import os
from django.conf import settings

def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            url = form.cleaned_data['url']

            # Generate QR Code
            qr = qrcode.make(url)
            file_name = title.replace(" ", "_").lower() + '.png'
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            qr.save(file_path)

            # Create Image URL
            qr_url = os.path.join(settings.MEDIA_URL, file_name)

            context = {
                'title': title,
                'qr_url': qr_url,
                "file_name": file_name,
            }
            return render(request, 'qr_result.html', context)

    else:
        form = QRCodeForm()
        context = {
            'form': form,
        }
        return render(request, 'generate_qr_code.html', context)