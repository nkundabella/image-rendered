# 🖼️ Django Model Image Renderer (`image-rendered`)

A clean, minimalist Django reference project demonstrating how to use a **Django Model** to upload, store, and display images.

---

## 🌟 Overview

In Django's Model-View-Template (MVT) architecture, rendering images stored in a database model involves a few essential parts working together:
1. **The Model (`models.ImageField`)**: Stores the file path in the database and uploads the file to `MEDIA_ROOT`.
2. **Media Configuration (`settings.py`)**: Defines `MEDIA_URL` (the public web path) and `MEDIA_ROOT` (the filesystem directory).
3. **URL Routing (`urls.py`)**: Exposes media files during development using `static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)`.
4. **The Template**: Accesses the model attribute `{{ photo.image.url }}` inside an `<img>` tag.

---

## 🚀 Quick Start

### 1. Clone the repository and navigate into the folder:
```bash
git clone https://github.com/nkundabella/image-rendered.git
cd image-rendered
```

### 2. Create and activate a virtual environment:
```bash
# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install requirements:
```bash
pip install -r requirements.txt
```

### 4. Run database migrations:
```bash
python manage.py migrate
```

### 5. Seed the initial demo photo (optional):
```bash
python manage.py seed_demo
```

### 6. Start the local server:
```bash
python manage.py runserver
```

Open your browser at:
👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 📂 Project Architecture

```
image-rendered/
│
├── manage.py                          # Django management CLI
├── requirements.txt                   # Django & Pillow dependencies
├── .gitignore                         # Ignores venv, db.sqlite3, cache
├── README.md                          # Documentation
│
├── config/                            # Project settings & URL routing
│   ├── __init__.py
│   ├── settings.py                   # Configures MEDIA_URL, MEDIA_ROOT & apps
│   ├── urls.py                       # Connects routes & serves media files
│   ├── wsgi.py
│   └── asgi.py
│
├── gallery/                           # Core application
│   ├── models.py                     # Photo model with models.ImageField
│   ├── forms.py                      # PhotoForm (ModelForm)
│   ├── views.py                      # List, upload, detail, and delete views
│   ├── urls.py                       # App URL definitions
│   ├── admin.py                      # Admin configuration with thumbnail preview
│   ├── tests.py                      # Unit tests for model & rendering
│   │
│   ├── management/commands/
│   │   └── seed_demo.py              # Command to seed an initial photo
│   │
│   └── templates/gallery/
│       ├── base.html                 # Dark modern glassmorphic layout
│       ├── index.html                # Gallery grid + upload form
│       ├── detail.html               # Full resolution inspector
│       └── confirm_delete.html       # Delete confirmation
│
├── media/                             # User uploaded media
│   └── uploads/                      # Upload destination for images
│       ├── .gitkeep
│       └── sample.png                # Seed sample photo
│
└── static/
    └── css/
        └── style.css                 # Responsive modern styling
```

---

## 🔍 How It Works (Step-by-Step)

### 1. The Model (`gallery/models.py`)
```python
from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=120)
    caption = models.TextField(blank=True, max_length=500)
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

### 2. Media Settings (`config/settings.py`)
```python
# The URL prefix for media files in the browser
MEDIA_URL = '/media/'

# The absolute filesystem path where Django saves uploaded files
MEDIA_ROOT = BASE_DIR / 'media'
```

### 3. URL Media Serving (`config/urls.py`)
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gallery.urls')),
]

# In development, tell Django to serve files from MEDIA_ROOT
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### 4. Rendering in Template (`gallery/templates/gallery/index.html`)
```html
{% for photo in photos %}
  <div class="photo-card">
    <!-- Render the image from the model instance -->
    <img src="{{ photo.image.url }}" alt="{{ photo.title }}">
    <h3>{{ photo.title }}</h3>
    <p>{{ photo.caption }}</p>
  </div>
{% endfor %}
```

### 5. Uploading via Form
When rendering a form that uploads images to the model, ensure `enctype="multipart/form-data"` is set:
```html
<form method="post" enctype="multipart/form-data">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Upload</button>
</form>
```
And in your view:
```python
form = PhotoForm(request.POST, request.FILES)
if form.is_valid():
    form.save()
```

---

## 🧪 Running Automated Tests

Run the test suite to verify model creation, view responses, and image URL rendering:
```bash
python manage.py test
```

---

## 👤 Django Admin Access

To create an administrator account and inspect images in the Django Admin:
```bash
python manage.py createsuperuser
```
Then visit: **[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)**

---

## 📜 License
MIT License. Free to use for study, assignments, and production templates.
