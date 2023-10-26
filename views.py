from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from .forms import SignUpForm
from .forms import ContactForm



def index(request):
        return render(request, 'aiconnectwebsite/index.html')

def about(request):
        return render(request, 'aiconnectwebsite/about.html')

def contact(request):
    return render(request, 'aiconnectwebsite/contact.html')




def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                'Contact form submission',
                form.message,
                form.email,
                ['answers@aiconnectsale.com'],
                fail_silently=False
            )
            return redirect('success')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, 'aiconnectwebsite/contact_form.html', context)

def faq(request):
    return render(request, 'aiconnectwebsite/faq.html')

def feedback(request):
    return render(request, 'aiconnectwebsite/feedback.html')

def prompt(request):
    return render(request, 'aiconnectwebsite/prompt.html')

def client_interface(request):
        """
        Renders the client interface page.

        Args:
            request: The HTTP request object.

        Returns:
            A rendered HTML template for the client interface page.
        """
        # Function code goes here
def client_interface(request):
        
        # Function code goes here
    return render(request, 'aiconnectwebsite/Client_Interface.html')



 


from .forms import SignUpForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Process the form data
            # Create new user, save to database, etc.
            # Redirect to success page
            return redirect('success')
    else:
        form = SignUpForm()

    return render(request, 'aiconnectwebsite/signup.html', {'form': form})



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired URL
        else:
            error = 'Invalid login credentials. Please try again.'
            return render(request, 'aiconnectwebsite/login.html', {'error': error})
    else:
        return render(request, 'aiconnectwebsite/login.html')
    

    

'''
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send an email with the contact form information to the recipient.

            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

'''





 