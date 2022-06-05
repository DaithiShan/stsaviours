from django.shortcuts import render

# ---- Landing Page View -----


def home(request):
    """
    Landing/Welcome page for website
    """
    return render(request, 'store/index.html')
