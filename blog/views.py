from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Post
from .models import Contact

def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/index.html',{'posts':posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,status='published', publish__year=year, publish__month=month, publish__day=day)

    return render(request, 'blog/post/detail.html', {'post':post})

def contactView(request):
    if request.method == "GET":
        form  = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            #newContact = form.save()
            form.save(commit=True)
            return post_list(request)
        else:
            print("FORM IS INVALID")
            #Name = form.cleaned_data['Name']
            #Email_Address = form.cleaned_data['Email_Address']
            #Phone_Number = form.cleaned_data['Phone_Number']
            #message = form.cleaned_data['message']

            #try:
            #    send_email(subject,message,from_email,['jyoti.nayak@sigmancomp.com'])
            #except BadHeaderError:
            #    return HttpResponse('Invalid header found.')
            #return redirect('success')
    return render(request, 'blog/post/contact.html', {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your patience')


    

# Create your views here. 
