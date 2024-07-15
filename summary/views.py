from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import nltk
import os

# NLTK 다운로드
nltk.download('punkt')

# 모델과 토크나이저 로드
model = AutoModelForSeq2SeqLM.from_pretrained('eenzeenee/t5-base-korean-summarization')
tokenizer = AutoTokenizer.from_pretrained('eenzeenee/t5-base-korean-summarization')

prefix = "summarize: "
save_directory = ""

@api_view(['POST'])
def summarize(request):
    text = request.data.get('text', '')

    if not text:
        return Response({'error': 'No text provided'}, status=status.HTTP_400_BAD_REQUEST)

    inputs = [prefix + text]
    inputs = tokenizer(inputs, max_length=512, truncation=True, return_tensors="pt")
    output = model.generate(**inputs, num_beams=3, do_sample=True, min_length=10, max_length=64)
    decoded_output = tokenizer.batch_decode(output, skip_special_tokens=True)[0]
    result = nltk.sent_tokenize(decoded_output.strip())[0]

    with open(os.path.join(save_directory, 'original_text.txt'), 'w', encoding='utf-8') as f:
        f.write(text)
    with open(os.path.join(save_directory, 'summary_text.txt'), 'w', encoding='utf-8') as f:
        f.write(result)

    return Response({'summary': result})

@api_view(['GET'])
def index(request):
    return Response({'message': 'Welcome to the summarizer API'})

