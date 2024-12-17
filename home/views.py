from django.shortcuts import render
from wagtail.admin import messages

def my_custom_view(request):
    # Perform any logic you need here
    messages.success(request, "This is a custom admin view!")
    return render(request, 'my_custom_template.html')
