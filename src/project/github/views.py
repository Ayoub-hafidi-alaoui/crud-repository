from django.shortcuts import render
from .models import Repository
from .forms import RepositoryForm
from django.shortcuts import redirect
# Create your views here.



def all_repositories(request):
    repositories = Repository.objects.all()
    return render(request, 'index.html',  {"repositories": repositories})


def show_repository(request, id):
    repository = Repository.objects.get(id=id)
    return render(request, 'show.html', {'repository': repository})

def new_repository(request):
    if request.method == 'POST':
        form = RepositoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_repositories')
    else:
        form = RepositoryForm()
    return render(request, 'new.html', {'form': form})

def edit_repository(request, id):
    repository = Repository.objects.get(id=id)
    if request.method == 'POST':
        form = RepositoryForm(request.POST, instance=repository)
        if form.is_valid():
            form.save()
            return redirect('all_repositories')
    else:
        form = RepositoryForm(instance=repository)
    return render(request, 'edit.html', {'form': form})

def delete_repository(request, id):
    repository = Repository.objects.get(id=id)
    repository.delete()
    return redirect("all_repositories")

