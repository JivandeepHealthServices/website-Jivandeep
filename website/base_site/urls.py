from django.contrib import admin
from django.urls import path, include
"""
The above code we've copied form the website folder's urls.py file
"""


from base_site import views
"""
This is to import the view.py file which is in base_site folder.
"""

# Creating
urlpatterns = [
    """
    If someone comes with a blank path, ient it to the index function in views.py in base_site and name the path "home"
    """
    path("", views.index, name="home"),


    # Url for about.html
    path("about", views.about, name="about"),


    # Url for contact.html
    path("contact", views.contact, name="contact")


]


