from django.shortcuts import render, redirect
from .forms import UserForm
from django.views.generic.edit import CreateView, UpdateView

def register(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = UserForm()
	return render(request, 'users/register.html', {'form': form})
