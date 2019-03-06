from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return  HttpResponse('hello world')
    return  render(request,'index.html')


def count(request):
    count = (len(request.GET['text']))
    inp = request.GET['text']
    word_dict = {}
    for word in inp:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] +=1
    #字典排序
    sor_dict = sorted(word_dict.items(),key=lambda w:w[1],reverse=True)

    return  render(request,'count.html',{'count':count,'inp':inp,
                                         'dict':word_dict,'sor': sor_dict})


