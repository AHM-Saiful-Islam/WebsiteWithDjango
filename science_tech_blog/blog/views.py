from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Contact
from django.contrib import messages
import re


# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('-date_posted')[:5]  # Display latest 5 posts
    return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def blog(request):
    posts = Post.objects.all().order_by('-date_posted')
    return render(request, 'blog/blog.html', {'posts': posts})


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # check email validity
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if (bool(re.match(pattern, email)) is True):
            # Save the data to the Contact model
            Contact.objects.create(name=name, email=email, message=message)
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact_view')  # Adjust with your contact URL name
        else:
            messages.error(request, "There was an error with your submission. Please try again.")
            return render(request, 'contact.html')
        
    return render(request, 'contact.html')
'''
def contact_view(request):
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            form.save()  # Save the form data
            messages.success(request, "Thank you for contacting us! Your message has been sent.")
            return redirect('contact_view')  # Redirect back to the contact form page
        else:
            messages.error(request, "There was an error with your submission. Please try again.")
            return render(request, 'contact.html', {'form': form})

    form = Contact()
    return render(request, 'contact.html', {'form': form})
'''