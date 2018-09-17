# Allows us to return back HttpResponse
from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    
    wordlist = fulltext.split()
    
    wordDict = {}
    for word in wordlist:
        if word in wordDict:
            #Increase
            wordDict [word] += 1
        else:
            #Add to dict
            wordDict [word] = 1

    sortedWords = sorted(wordDict.items(), key = operator.itemgetter(1), reverse = True)



    return render(request, "count.html", {'fulltext':fulltext,'count':len(wordlist),'sortedWords':sortedWords} )