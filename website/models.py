
from django.db import models
from django.utils.text import slugify
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    travel_dates = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} - {self.email}"



class Service(models.Model):
    order = models.PositiveIntegerField(
        default=0,
        help_text="Controls display order on the site (lower numbers first). Also used to generate the displayed 01/02/03 service number.",
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="services/", blank=True, null=True)
    is_active = models.BooleanField(
        default=True,
        help_text="Untick to hide this service from the site without deleting it.",
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title

    @property
    def display_number(self):
        """Renders the order as a zero-padded number, e.g. 1 -> '01'."""
        return f"{self.order:02d}"


class Destination(models.Model):
    order = models.PositiveIntegerField(
        default=0,
        help_text="Controls display order on the site (lower numbers first).",
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(
        max_length=120,
        unique=True,
        blank=True,
        help_text="Used in the destination's URL, e.g. /destinations/osaka/. Leave blank to auto-generate from the name.",
    )
    region = models.CharField(
        max_length=100,
        blank=True,
        help_text="e.g. Kansai, Kanto, Kyushu — shown as the small label above the destination name.",
    )
    short_description = models.CharField(
        max_length=200,
        blank=True,
        help_text="Short teaser shown on destination cards (home page and destinations grid).",
    )
    description = models.TextField(
        help_text="Longer description shown on the destination's own detail page.",
    )
    image = models.ImageField(upload_to="destinations/", blank=True, null=True)
    is_active = models.BooleanField(
        default=True,
        help_text="Untick to hide this destination from the site without deleting it.",
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Destination.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                counter += 1
                slug = f"{base_slug}-{counter}"
            self.slug = slug
        super().save(*args, **kwargs)