from django import forms
from gallery.models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image', 'title')
        labels = {'image':"",'user':""}
        extra_kwargs = {'user': {'required': False}}
    image = forms.ImageField(label='Select a file', widget=forms.FileInput(attrs={'class':'block w-full text-sm text-slate-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-violet-50 file:text-violet-700 hover:file:bg-violet-100'}))

    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class':'mt-1 px-3 py-2 bg-white border shadow-sm border-slate-300 placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-sky-500 block w-full rounded-md sm:text-sm focus:ring-1" placeholder="you@example.com'}))



