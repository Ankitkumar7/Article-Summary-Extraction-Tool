from django.shortcuts import render
from .utils import newsTitle, newsSummary, newsPublishedDate, imageUrl
from .models import URL
from  .forms import urlForm

def index(request):
	getUrl = URL.objects.filter().order_by('-id')[:1]
	forms = urlForm(request.POST or None)
	if forms.is_valid():
		instance = forms.save(commit=False)
		instance.save()
		instance = forms.cleaned_data
	content = []
	for i in getUrl:
		content.append(i)
	strContent = str(content)
	myStr = strContent[7:]
	myStr = myStr[:-2]
	print myStr
	context =  {
	'form':forms,
	'title': newsTitle(myStr),
	'summary':  newsSummary(myStr),
	'published': newsPublishedDate(myStr),
	'image':  imageUrl(myStr),
	
	}

	return render(request, 'index.html',context)