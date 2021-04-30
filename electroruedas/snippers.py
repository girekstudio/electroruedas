import uuid
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.mail import EmailMultiAlternatives


def Attr(cls):
    model= cls.__name__
    return cls.__doc__.replace(model,"").replace("(","").replace(")","").replace(" ","").split(",")

class ResizeImageMixin:
    def resize(self, imageField, size:tuple):
        im = Image.open(imageField)  # Catch original
        source_image = im.convert('RGB')
        source_image=source_image.resize(size)  # Resize to size
        output = BytesIO()
        source_image.save(output, format='JPEG',optimize=True, quality=55) # Save resize image to bytes
        output.seek(0)
        content_file = ContentFile(output.read())  # Read output and create ContentFile in memory
        file = File(content_file)
        random_name = f'{uuid.uuid4()}.jpeg'
        imageField.save(random_name, file, save=False)

def enviar_email(asunto, from_email, to, mensaje):
    text_content = 'This is an important message.'
    html_content = '<p>This is an <strong>important</strong> message.</p>' \
                   '<img src="http://girekstudio.com/static/img/girekstudio/favi%20girek-02.png"><br>' + mensaje
    msg = EmailMultiAlternatives(asunto, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    # print from_email