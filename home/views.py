import requests
from django.shortcuts import redirect
from wagtail.admin import messages
from .models import HomePage, ChildPage

def my_custom_view(request):
    # Perform the HTTP GET request
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1')

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response
        title = data.get('title', 'Default Title')

        # Find the HomePage instance
        try:
            home_page = HomePage.objects.first()
            if home_page:
                # Check if a ChildPage with the same title already exists
                if ChildPage.objects.child_of(home_page).filter(title=title).exists():
                    messages.warning(request, f"A child page with the title '{title}' already exists.")
                else:
                    # Create a new ChildPage
                    child_page = ChildPage(
                        title=title,
                        custom_title=title  # Assuming you have a custom_title field
                    )
                    # Add the child page under the HomePage
                    home_page.add_child(instance=child_page)
                    # Save the page as a draft
                    child_page.save_revision()

                    messages.success(request, f"Child page '{title}' created successfully as a draft!")
            else:
                messages.error(request, "HomePage not found.")
        except HomePage.DoesNotExist:
            messages.error(request, "HomePage does not exist.")
    else:
        messages.error(request, "Failed to fetch data.")

    # Redirect back to the admin home page or render a template
    return redirect('wagtailadmin_home')
