from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    scope = models.CharField(max_length=250)
    timeline = models.CharField(max_length=100)
    accuracy = models.CharField(max_length=50)
    image = models.URLField(max_length=500) # Pexels image link ke liye
    description = models.TextField()
    challenge = models.TextField()
    solution = models.TextField()
    deliverables = models.JSONField(default=list) # List of deliverables store karne ke liye
    client_feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=100)
    excerpt = models.TextField()
    author = models.CharField(max_length=150)
    date = models.CharField(max_length=100)
    read_time = models.CharField(max_length=50)
    image = models.URLField(max_length=500)
    body = models.JSONField(default=list)

    def __str__(self):
        return self.title

STATUS_CHOICES = [
    ('new', 'New'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
    ('cancelled', 'Cancelled'),
]
    
class QuoteSubmission(models.Model):
    # Location Step
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    postal = models.CharField(max_length=20)
    
    # Project Info Step
    project_type = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    description = models.TextField()
    estimated_value = models.CharField(max_length=50, blank=True, null=True)
    project_location = models.CharField(max_length=200, blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    
    # Contact Info Step
    full_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    preferred_contact = models.CharField(max_length=20, default='Email')
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    admin_notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.full_name} - {self.project_type}"

class QuoteFile(models.Model):
    quote = models.ForeignKey(QuoteSubmission, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='quote_files/')

    def __str__(self):
        return f"File for {self.quote.full_name}"
    
    
class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    postal = models.CharField(max_length=20)
    project_type = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    description = models.TextField()
    preferred_contact = models.CharField(max_length=20, default='Email')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.email}"