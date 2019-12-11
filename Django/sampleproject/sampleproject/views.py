from django.http import HttpRequest
def hello(request):
	return HttpResponse("<h1>hello world</h1>")