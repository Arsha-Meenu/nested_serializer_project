import imp
from pyexpat import model
from rest_framework import serializers

from .models import BookDetails,Book

class BookDetailsSerializer(serializers.ModelSerializer):
    summary = serializers.CharField(max_length = 100)

    class Meta:
        model = BookDetails
        fields =('id','summary')

class BookSerializer(serializers.ModelSerializer):
    rbook = BookDetailsSerializer(many = True)

    def create(self, validated_data):
        temp_book_details = validated_data.pop('rbook')
        new_book = Book.objects.create(**validated_data)
        for i in temp_book_details:
            BookDetails.objects.create(**i,bok = new_book)
            
        return new_book


    class Meta:
        model = Book
        fields = ('id','rbook','title','author')