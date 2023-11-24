from django.db import models
from django.urls import reverse
from scripts import module
from django.core.validators import RegexValidator
class Metric(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    name = models.CharField(max_length=50, unique=True)
    definition = models.TextField(blank=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("metric-detail", args=[str(self.id)])
    
    
class Feature(models.Model):
    class DType(models.TextChoices):
        BOOL = "bool"
        LABEL = "label"
        RANK = "rank"
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    name = models.CharField(max_length=30, unique=True)
    dtype = models.TextField(choices=DType.choices, blank=True)
    metric = models.ManyToManyField(Metric, related_name="feature", help_text="Select a metric for this column")
    definition = models.TextField(null=True)
    notes = models.TextField(blank=True)
    def __str__(self) -> str:
        return self.name
    def transform(self):
        return module.to_list(self.notes)
    def get_absolute_url(self):
        
        return reverse("feature-detail", args=[module.to_slug(self.name)])
    
    
    


class Intro(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    def __str__(self) -> str:
        return f"Intro {str(self.id)}"
    def get_absolute_url(self):
        return reverse("metric-intro")



class Conversation(models.Model):
    feature = models.ForeignKey(Feature, on_delete=models.SET_NULL, null=True, related_name="conversation")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Conversation {self.id} - Feature {self.feature.name}"
    
class Turn(models.Model):
    class Speaker(models.TextChoices):
        USER = "user"
        MODEL = "model"
    number = models.PositiveIntegerField(null=True)
    conversation = models.ForeignKey(Conversation, on_delete=models.SET_NULL, null=True, related_name="turn")
    speaker_type = models.TextField(choices=Speaker.choices, default=Speaker.MODEL)
    speaker_label = models.CharField(max_length=20, blank=True)
    body = models.TextField()
    def __str__(self):
        return f"Turn {self.number} - Conversation {self.conversation.id}"
    
    
    
        