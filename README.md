# Django Image Renderer

Minimal Django example: upload an image with `models.ImageField`, store it under `MEDIA_ROOT`, and display it with `{{ photo.image.url }}`.

## Quick start

```bash
python -m venv .venv
# Windows: .\.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/

## How it works

1. **Model** — `image = models.ImageField(upload_to='uploads/')`
2. **Settings** — `MEDIA_URL` + `MEDIA_ROOT`
3. **URLs** — `static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)` in DEBUG
4. **Template** — `<img src="{{ photo.image.url }}">` and form `enctype="multipart/form-data"`

## Project layout

```
config/          # settings + root urls
gallery/         # Photo model, form, views, template
media/uploads/   # uploaded files
static/css/      # basic styles
```
