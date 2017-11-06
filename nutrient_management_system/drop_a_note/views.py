from django.shortcuts import render, redirect
from django.views import View
from drop_a_note.forms import ContactForm


class ContactFormView(View):
    form_class = ContactForm
    template_name = 'contact.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        print(self.request.user)
        if form.is_valid():
            note = form.save(commit=False)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            form.save()

            if note is not None:
                return redirect('contact:contact')
        return render(request, self.template_name, {'form': form})
