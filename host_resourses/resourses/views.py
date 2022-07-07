from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ResourseForm
from .models import Resourse


@login_required
def index(request):
    resourses = Resourse.objects.filter(host_user=request.user)
    context = {
        'page_obj': resourses
    }
    return render(request, 'resourses/index.html', context)


@login_required
def resourse_create(request):
    form = ResourseForm(request.POST or None)
    if form.is_valid():
        resourse = form.save(commit=False)
        resourse.host_user = request.user
        resourse.save()
        return redirect('resourses:index')
    return render(request, 'resourses/create_resourse.html', {'form': form})


@login_required
def resourse_edit(request, resourse_id):
    resourse = get_object_or_404(Resourse, pk=resourse_id)
    is_edit = True
    form = ResourseForm(
        request.POST or None,
        instance=resourse)
    if form.is_valid():
        form.save()
        return redirect('resourses:index')

    context = {
        'form': form,
        'is_edit': is_edit
    }
    return render(request, 'resourses/create_resourse.html', context)
