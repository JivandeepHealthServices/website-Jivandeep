from django.shortcuts import render

# Create your views here.

# Index or Home page
def index(request):
    """
    This returns the "index.html" in the templates which is our home page.
    We can add context = {}, a dict for passing some variables.
    """
    return render(request, "index.html")



# About Us page
def about(request):
    """
    This returns the "about.html" in the templates which is our about page.
    """
    return render(request, "about.html")

# Contact Us page
def contact(request):
    """
    This returns the "contact.html" in the templates which is our contact page.
    """
    return render(request, "contact.html")