from django.shortcuts import render
from django.http import HttpResponse
import qrcode
import io
import base64

# Create your views here.
def home(request):
    return render(request,'app/home.html')

def qr_generator(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        if text:
            # Create QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(text)
            qr.make(fit=True)
            
            # Create image
            img = qr.make_image(fill_color="black", back_color="white")
            
            # Convert to base64 for display in HTML
            buffer = io.BytesIO()
            img.save(buffer, format='PNG')
            img_str = base64.b64encode(buffer.getvalue()).decode()
            
            context = {
                'qr_code': img_str,
                'text': text
            }
            return render(request, 'app/qr_generator.html', context)
    
    return render(request, 'app/qr_generator.html')