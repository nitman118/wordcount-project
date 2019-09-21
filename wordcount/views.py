from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')


def count(request):
    fulltext=request.POST['fulltext'] # GET or POST depending on form method
    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            #Increase word count
            worddictionary[word]+=1
        else:
            #add to dict
            worddictionary[word]=1
    sortedwords=sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request,'count.html', {'fulltext':fulltext, 'count': len(wordlist), 'sortedwords':sortedwords})

def about(request):
    return render(request, 'about.html')


