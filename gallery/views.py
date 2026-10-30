from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Photo
from .forms import PhotoForm


def photo_list(request):
    """
    Renders the gallery page showing all photos stored in the database model.
    Also handles new uploads directly via the embedded form.
    """
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()
            messages.success(request, f'Photo "{photo.title}" was successfully uploaded and saved to the model!')
            return redirect('gallery:list')
    else:
        form = PhotoForm()

    photos = Photo.objects.all()
    return render(request, 'gallery/index.html', {
        'photos': photos,
        'form': form,
    })


def photo_detail(request, pk):
    """
    Renders a single photo with full resolution and model details.
    """
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'gallery/detail.html', {'photo': photo})


def photo_delete(request, pk):
    """
    Deletes a photo from the database and redirects back to the list.
    """
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == 'POST':
        title = photo.title
        # Delete the actual file from disk if desired
        if photo.image:
            photo.image.delete(save=False)
        photo.delete()
        messages.info(request, f'Photo "{title}" was deleted.')
        return redirect('gallery:list')
    return render(request, 'gallery/confirm_delete.html', {'photo': photo})
