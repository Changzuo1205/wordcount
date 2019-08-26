# from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, "home.html")

def count(request):
	count = len(request.GET['text'])
	text = request.GET['text']

	word_dict = {}
	
	for word in text:
		if word not in word_dict:
			word_dict[word] = 1
		else:
			word_dict[word] += 1

	word_dict = sorted(word_dict.items(), key=lambda w:w[1], reverse=True)

	return render(request, "count.html", {'word_count': count, 'text': text, 'dict': word_dict})

def about(request):
	return render(request, "about.html")
