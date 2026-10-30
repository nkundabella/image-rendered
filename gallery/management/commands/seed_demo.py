import os
from django.core.management.base import BaseCommand
from django.conf import settings
from gallery.models import Photo


class Command(BaseCommand):
    help = 'Populates the database with an initial sample photo if none exist.'

    def handle(self, *args, **kwargs):
        if Photo.objects.exists():
            self.stdout.write(self.style.WARNING("Photos already exist in the database. Skipping seeding."))
            return

        sample_rel_path = 'uploads/sample.png'
        sample_abs_path = os.path.join(settings.MEDIA_ROOT, sample_rel_path)

        if not os.path.exists(sample_abs_path):
            self.stdout.write(self.style.ERROR(f"Sample image not found at {sample_abs_path}"))
            return

        photo = Photo.objects.create(
            title="Twilight Mountain Horizon",
            caption="A modern geometric vector landscape rendered directly from the Django Photo model instance.",
            image=sample_rel_path,
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully seeded demo photo '{photo.title}' (ID: #{photo.id}) using {photo.image.url}!"
            )
        )
