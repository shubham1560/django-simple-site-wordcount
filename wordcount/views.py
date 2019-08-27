from django.http import HttpResponse
from django.shortcuts import render


def func(request):
    return render(request, "home.html")
    # return render(request, "home.html", {"request": request   })


def eggs(request):
    print(request)
    return HttpResponse("Eggs are great!!")


def wordcount(request):
    text = request.GET["fulltext"]
    a = text.split(" ")
    frequency = {}
    # print(a)
    for i in a:
        if i != " ":
            if i not in frequency:
                frequency[i] = 1
            else:
                frequency[i] += 1

    result = {'fullText': text, 'frequencyTab': frequency.items()}
    return render(request, "wordCount.html", result)


def about(request):
    return render(request, 'about.html')
