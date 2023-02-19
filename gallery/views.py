from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from gallery.models import Photo
from gallery.forms import PhotoForm
# Create your views here.
@login_required(login_url='/login/')
def upload_image(request):
    user = request.user
    images = Photo.objects.filter(user=user)
    context = {'images':images}
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES,user)
        if form.is_valid():
            form.instance.user = user
            form.save()

            return redirect(upload_image)

        else:
            errors = form.errors
            context['errors'] = errors
    form = PhotoForm()
    context['form']=form
    
    return render(request, 'images.html', context)

@login_required(login_url='/login/')
def delete(request, id):
    image = Photo.objects.get(id=id)
    image.delete()
    return redirect('images')