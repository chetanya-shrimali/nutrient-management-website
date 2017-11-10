from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.views import View
from drop_a_note.forms import ContactForm
from drop_a_note.models import Note


def feedbacks(request):
    all_feedbacks = Note.objects.all()
    return render(request, 'feedbacks.html', {'all_feedbacks': all_feedbacks})


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
            email_address = form.cleaned_data['email']
            note_content = form.cleaned_data['note']
            form.save()

            if note is not None:
                email = EmailMessage('Regarding feedback',
                                     email_address + "\n\n" + note_content,
                                     to=['chetanyashrimalie5@gmail.com',
                                         'nkchoudhary696@gmail.com'])
                email.send()

                email = EmailMessage('Regarding feedback',
                                     "Hey " + name + ",\n\n" + "We have successfully recieved your note!!",
                                     to=[email_address])
                email.send()
                print('reached')
                return redirect('contact:contact')
        return render(request, self.template_name, {'form': form})
