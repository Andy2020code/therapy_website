from django.shortcuts import render, redirect

# Create your views here.
def home(request):
	return render(request, 'home.html')


def link_1(request):
	return render(request, 'link_1.html')

def link_2(request):
	return render(request, 'link_2.html')

def link_3(request):
	return render(request, 'link_3.html')

def link_4(request):
	return render(request, 'link_4.html')


#Home_Page "Hmmm, I Need ..." option links
def i_need_option_01(request):
	return render(request, 'i_need_option_01.html')