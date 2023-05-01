import cv2
import numpy as np
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


@csrf_exempt
def index(request):
    if request.method == 'POST':
        # Get the uploaded image
        #image = request.FILES['image'].read()
        # Process the image using the Python algorithm
        #processed_image = cv2.cvtColor(np.frombuffer(image, np.uint8), cv2.COLOR_BGR2GRAY)
        
        # Convert the processed image back to bytes
        # _, processed_image_bytes = cv2.imencode('.png', processed_image)
        
        # Return a response
        return HttpResponse('Image processed and saved to text file.')
    else:
        return render(request, 'index.html')


@method_decorator(csrf_exempt, name='dispatch')
class IndexView(TemplateView):
    templateName = 'index.html'

    def get(self, request):
        return render(request, self.templateName)
    
    def post(self, request):
        if 'uploadFile' in request.FILES:
            selected_option = request.POST.get('checkbox')
            uploaded_images = request.FILES.getlist('uploadFile')
            for uploaded_image in uploaded_images:
                # Process the image
                #processed_image = cv2.cvtColor(uploaded_image, cv2.COLOR_BGR2GRAY)

                # Write the processed image to a text file
                with open('processed_image.txt', 'w') as f:
                    f.write(str(uploaded_image))

                if selected_option == '1':
                    return HttpResponse('Image processed and saved to text file plus the selected option was CIN.')
                
                elif selected_option == '2':
                    return HttpResponse('Image processed and saved to text file plus the selected option was Football card.')
                
        elif 'uploadFileDnD' in request.FILES:
            uploaded_images_DnD = request.FILES.getlist('uploadFileDnD')
            for uploaded_image_DnD in uploaded_images_DnD:
                # Process each uploaded image
                #processed_image = cv2.cvtColor(uploaded_image, cv2.COLOR_BGR2GRAY)

                # Write the processed image to a text file
                with open('processed_image.txt', 'w') as f:
                    f.write(str(uploaded_image_DnD))

            return HttpResponse('Image processed and saved to text file.')
        
        else:
            return HttpResponse('no image')