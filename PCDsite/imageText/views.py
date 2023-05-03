import cv2
import numpy as np
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

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
                # Write the processed image to a text file
                with open('processed_image.txt', 'w') as f:
                    f.write(str(uploaded_image))

                if selected_option == '1':
                    # Run the algorithme for the cin card
                    return HttpResponse('Image processed and saved to text file plus the selected option was CIN.')
                
                elif selected_option == '2':
                    # Run the algorithme for the football card
                    return HttpResponse('Image processed and saved to text file plus the selected option was Football card.')
                
        elif 'uploadFileDnD' in request.FILES:
            uploaded_images_DnD = request.FILES.getlist('uploadFileDnD')
            for uploaded_image_DnD in uploaded_images_DnD:
                # Write the processed image to a text file
                with open('processed_image.txt', 'w') as f:
                    f.write(str(uploaded_image_DnD))

                if selected_option == '1':
                    # Run the algorithme for the cin card
                    return HttpResponse('Image processed and saved to text file plus the selected option was CIN.')
                
                elif selected_option == '2':
                    # Run the algorithme for the football card
                    return HttpResponse('Image processed and saved to text file plus the selected option was Football card.')
        
        else:
            return HttpResponse('no image')