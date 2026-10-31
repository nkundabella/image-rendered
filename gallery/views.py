from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo
from .forms import PhotoForm


def photo_list(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = PhotoForm()

    return render(request, 'gallery/index.html', {
        'photos': Photo.objects.all(),
        'form': form,
    })


def photo_delete(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == 'POST':
        if photo.image:
            photo.image.delete(save=False)
        photo.delete()
    return redirect('list')
