from django.db import models
from django.urls import reverse
from scripts import functions

class Metric(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    name = models.CharField(max_length=50, unique=True)
    definition = models.TextField(blank=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("metric-detail", args=[str(self.id)])
    
    
class Feature(models.Model):
    class DType(models.TextChoices):
        BOOL = "bool"
        LABEL = "label"
        RANK = "rank"
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    name = models.CharField(max_length=50, unique=True)
    dtype = models.TextField(choices=DType.choices, blank=True)
    metric = models.ManyToManyField(Metric, related_name="feature", help_text="Select a metric for this column")
    definition = models.TextField(null=True)
    notes = models.TextField(blank=True)
    def __str__(self) -> str:
        return self.name
    def transform(self):
        return functions.to_list(self.notes)
    
class Example(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    feature = models.ForeignKey(Feature, related_name="example", null=True, on_delete=models.SET_NULL)
    body = models.ImageField(upload_to="examples/")
    def __str__(self) -> str:
        return f"Example {str(self.id)}"

class Intro(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    def __str__(self) -> str:
        return f"Intro {str(self.id)}"
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("metric-intro")
    