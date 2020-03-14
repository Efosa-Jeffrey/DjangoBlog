from django.shortcuts import render


def register(request):

	#form validation

	return render(request, 'users/register.html')