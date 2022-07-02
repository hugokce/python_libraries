from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.template import loader
from .models import Author

# Create your views here.
def index(request):
    return HttpResponse("Anasayfa")
def authors(request):
 #   template=loader.get_template('authors.html') render yapınca ihtiyaç kalmadı
    context={
        'authors_list' :Author.objects.all()
    }
 # değişti      return HttpResponse(template.render(context,request))
    return render(request,'authors.html',context)
def books(request):
    return HttpResponse("Kitaplar")
def authorDetails(request,authorId):
    try:
        context={
            'author_detail' :Author.objects.get(pk=authorId)
        }
    except Author.DoesNotExist:
        raise Http404("Yazar bulunamadı")
#    return HttpResponse("Yazar detayı :"+str(authorId))
    return render(request,'authorDetail.html',context)