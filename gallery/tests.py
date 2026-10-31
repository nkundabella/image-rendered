import io
from PIL import Image
from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Photo


def make_image(name='test.png'):
    buf = io.BytesIO()
    Image.new('RGB', (100, 100), color=(73, 109, 137)).save(buf, format='PNG')
    buf.seek(0)
    return SimpleUploadedFile(name, buf.read(), content_type='image/png')


class PhotoTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_and_render(self):
        photo = Photo.objects.create(title='Test', image=make_image())
        self.assertTrue(photo.image.url.startswith('/media/uploads/'))

        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, photo.title)
        self.assertContains(response, photo.image.url)

    def test_upload(self):
        response = self.client.post(
            reverse('list'),
            {'title': 'Uploaded', 'image': make_image('up.png')},
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Photo.objects.filter(title='Uploaded').exists())
