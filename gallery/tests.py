import io
from PIL import Image
from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Photo


class PhotoModelTests(TestCase):
    def setUp(self):
        self.client = Client()

    def generate_test_image(self, name="test.png"):
        file_obj = io.BytesIO()
        image = Image.new('RGB', (100, 100), color=(73, 109, 137))
        image.save(file_obj, format='PNG')
        file_obj.seek(0)
        return SimpleUploadedFile(name, file_obj.read(), content_type='image/png')

    def test_create_and_render_photo(self):
        uploaded = self.generate_test_image()
        photo = Photo.objects.create(
            title="Test Photo Title",
            caption="A simple test caption",
            image=uploaded
        )
        self.assertEqual(str(photo), "Test Photo Title")
        self.assertTrue(photo.image.url.startswith('/media/uploads/'))

        # Check gallery page renders the image url
        response = self.client.get(reverse('gallery:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, photo.title)
        self.assertContains(response, photo.image.url)

    def test_upload_photo_via_post(self):
        test_file = self.generate_test_image("upload_test.png")
        response = self.client.post(
            reverse('gallery:list'),
            {
                'title': 'Form Uploaded Picture',
                'caption': 'Uploaded via multipart form',
                'image': test_file,
            },
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Photo.objects.filter(title='Form Uploaded Picture').exists())

    def test_detail_view(self):
        photo = Photo.objects.create(
            title="Inspect Me",
            caption="Testing details",
            image=self.generate_test_image("detail.png")
        )
        response = self.client.get(reverse('gallery:detail', kwargs={'pk': photo.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, photo.title)
        self.assertContains(response, photo.image.url)
