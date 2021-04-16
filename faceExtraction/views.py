from django.http import FileResponse
import face_extraction.getFace as face
from PIL import Image


def face_extraction_view(request):
    url = request.GET.get('url')
    c = face.getFace(url)
    image = Image.fromarray(c)
    image.save("extracted_face.jpg")
    img = open('extracted_face.jpg', 'rb')
    response = FileResponse(img)
    return response
