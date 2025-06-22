from django.utils import timezone
from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator, MaxValueValidator

class About(models.Model):
    content = RichTextField(help_text="You can enter plain text or HTML. HTML will be rendered as HTML.")
    image = models.ImageField(upload_to='about_images/', blank=True, null=True)

    def is_html_content(self):
        return '<' in self.content and '>' in self.content

    def __str__(self):
        return "About Me"


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    year = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name}"


class Profile(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile/')

    def __str__(self):
        return self.name


class Section(models.Model):
    SECTION_TYPE_CHOICES = [
        ('content', 'Content Section'),
        ('gallery', 'Gallery Section'),
        ('skills', 'Skills Section'),
        ('projects', 'Projects Section'),
    ]
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    section_type = models.CharField(max_length=20, choices=SECTION_TYPE_CHOICES)
    content = RichTextField(blank=True, null=True)  # For intro text or content
    image = models.ImageField(upload_to='section_images/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class ProjectItem(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='project_items')
    title = models.CharField(max_length=200)
    description = RichTextField(blank=True)
    link = models.URLField(blank=True, null=True)
    pdf_file = models.FileField(upload_to='project_pdfs/', blank=True, null=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='gallery_images/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.caption or "Gallery Image"


class SkillItem(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='skill_items')
    name = models.CharField(max_length=100)
    level = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Enter a value between 0 and 100"
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
    

ICON_CHOICES = [
    ('linkedin', 'LinkedIn'),
    ('github', 'GitHub'),
    ('email', 'Email'),
    ('website', 'Website'),
]

class FooterLink(models.Model):
    label = models.CharField(max_length=100)
    url = models.URLField()
    icon = models.CharField(max_length=50, choices=ICON_CHOICES)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.label