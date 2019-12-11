import datetime
from django.http import HttpRequest
def index(request):
	now=datetime.datetime.now()
	return("<h1>now time is %s</h1>")