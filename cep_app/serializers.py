from rest_framework import serializers
from .models import Project, BlogPost, QuoteSubmission, QuoteFile, ContactMessage

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
        


class QuoteFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteFile
        fields = ['id', 'file']

class QuoteSubmissionSerializer(serializers.ModelSerializer):
    files = QuoteFileSerializer(many=True, read_only=True)

    class Meta:
        model = QuoteSubmission
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        quote = QuoteSubmission.objects.create(**validated_data)
        
        # Multiple files handle karna
        if request:
            files_data = request.FILES.getlist('files')
            for file_data in files_data:
                QuoteFile.objects.create(quote=quote, file=file_data)
                
        return quote
    
    
class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'