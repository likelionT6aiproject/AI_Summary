from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import nltk
import os
from .serializers import TextSerializer
from .utils import save_text_file
from .models import Summary

# NLTK 다운로드
nltk.download('punkt')

# 모델과 토크나이저 로드
model = AutoModelForSeq2SeqLM.from_pretrained('eenzeenee/t5-base-korean-summarization')
tokenizer = AutoTokenizer.from_pretrained('eenzeenee/t5-base-korean-summarization')

prefix = "summarize: "
save_directory = ""

class SummarizeView(APIView):
    def post(self, request):
        serializer = TextSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            #user_id = request.user.id
            #user_id = 1
            inputs = [prefix + text]
            inputs = tokenizer(inputs, max_length=512, truncation=True, return_tensors="pt")
            output = model.generate(**inputs, num_beams=3, do_sample=True, min_length=10, max_length=64)
            decoded_output = tokenizer.batch_decode(output, skip_special_tokens=True)[0]
            summary_text = nltk.sent_tokenize(decoded_output.strip())[0]

            original_url = save_text_file(text,'original_text')
            summary_url = save_text_file(summary_text,'summary_text')

            summary = Summary.objects.create(original_text_path=original_url, summary_text_path=summary_url)

            return Response({'summary': summary_text}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IndexView(APIView):
    def get(self, request):
        return render(request, 'index.html')
    

