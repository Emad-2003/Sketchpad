from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.core.files.base import ContentFile
from .forms import *
from .models import *
import base64

# Create your views here.
def notes_index(request):
    return render(request,'notes_index.html')

@login_required
def notes_list(request):
    notes = NotesModel.objects.all().order_by('-created_at')
    return render(request,"notes_list.html",{"notes":notes})

@login_required
def notes_create(request):
    if request.method == 'POST':
        image_data = request.POST.get('imageData')
        format, imgstr = image_data.split(';base64,')
        ext = format.split('/')[-1]
        image_data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        drawing = NotesModel(user=request.user, notes=image_data)  # Create new drawing
        drawing.save()
        return redirect('notes_list')
    else:
        form = NotesForm()
        
    return render(request, 'notes_form.html', {'form': form})

@login_required
def notes_edit(request,note_id):
    note_instance = get_object_or_404(NotesModel, id=note_id, user=request.user)

    if request.method == 'POST':
        image_data = request.POST.get('imageData')
        format, imgstr = image_data.split(';base64,')
        ext = format.split('/')[-1]
        image_data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        note_instance.notes = image_data
        note_instance.save()
        return redirect('notes_list')
    
    return render(request,"notes_form.html",{"note_instance":note_instance})

@login_required
def notes_delete(request,note_id):
    notes_instance=get_object_or_404(NotesModel,pk=note_id, user=request.user)
    
    if request.method == "POST":
        notes_instance.delete()
        messages.info(request,"successfully deleted")
        return redirect("notes_list")
    return render(request,"notes_delete_confirm.html")

def register(request):
    if request.method=='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect("notes_list")
    else:
        form = UserRegistrationForm()
        
    
    return render(request,'registration/register.html',{'form':form})