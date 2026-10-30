from django.db import models


class Photo(models.Model):
    """
    A simple model that stores an image file alongside metadata (title, caption, timestamp).
    Uses Django's ImageField which stores the relative path in the database while saving
    the actual file to the MEDIA_ROOT directory.
    """
    title = models.CharField(
        max_length=120,
        help_text="A friendly name or title for the image."
    )
    caption = models.TextField(
        blank=True,
        max_length=500,
        help_text="Optional description or note about this picture."
    )
    image = models.ImageField(
        upload_to='uploads/',
        help_text="The image file (PNG, JPG, WebP, GIF, etc.)."
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the photo was added."
    )

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    def __str__(self):
        return self.title
