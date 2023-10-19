from django.shortcuts import render, redirect
from .models import Users
from .forms import UsersForm
from django.views.generic import UpdateView, DetailView, DeleteView


class UserRedacting(UpdateView):
    model = Users
    template_name = 'main/create.html'
    form_class = UsersForm

# class UserDetailView(DetailView):
#     model = Users
#     template_name = 'main/user_view.html'
#     context_object_name = 'user'

class UserDeleteView(DeleteView):
    model = Users
    template_name = 'main/delete_user.html'
    success_url = '/'


def index(request):
    all_data = Users.objects.all()
    return render(request, 'main/index.html', {"data": all_data})


def create(request):
    error = ''
    
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Invalid data'

    form = UsersForm()
    
    data = {
        'form': form,
        'error': error
    }
    
    return render(request, 'main/create.html', data)

