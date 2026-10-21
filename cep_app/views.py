import csv
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny

from .models import QuoteSubmission, ContactMessage, Project, BlogPost
from .serializers import (
    QuoteSubmissionSerializer, 
    ContactMessageSerializer, 
    ProjectSerializer, 
    BlogPostSerializer
)

# --- Projects & Blogs Views ---
class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'

class BlogPostListView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogPostDetailView(generics.RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'


# --- Contact Message ViewSet ---
class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all().order_by('-created_at')
    serializer_class = ContactMessageSerializer
    permission_classes = [AllowAny]


# --- Quote Submission ViewSet (Public Submit + Admin CRM Protection) ---
class QuoteSubmissionViewSet(viewsets.ModelViewSet):
    queryset = QuoteSubmission.objects.all().order_by('-created_at')
    serializer_class = QuoteSubmissionSerializer

    def get_permissions(self):
        # Agar koi naya quote submit kar raha hai (Public), toh allow karo
        if self.action == 'create':
            return [AllowAny()]
        # Agar koi CRM se data dekh raha hai ya manage kar raha hai, toh sirf Admin allow hai
        return [IsAdminUser()]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            print("DJANGO VALIDATION ERROR:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)


# --- CSV Export Function for CRM ---
def export_quotes_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="cep_leads_export.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['ID', 'Full Name', 'Email', 'Phone', 'Project Type', 'Service', 'Status', 'Date'])
    
    quotes = QuoteSubmission.objects.all().values_list('id', 'full_name', 'email', 'phone', 'project_type', 'service', 'status', 'created_at')
    for q in quotes:
        writer.writerow(q)
    return response