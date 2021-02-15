from django.shortcuts import render



# Create your views here.
def index_view(request):
  return render( request, 'index.html')
def home_view(request):
  return render( request, 'home.html')

def article_create_view(request):
  if request.method is "GET":
    return render(request, 'GET')
  elif request.method == "POST":
    context= {title: request.POST.get('title')
              content: request.POST.get('content')
              author: request.POST.get('author')
              user: request.POST.get('user')
    
    
    
    }
    print(request)


  
  
