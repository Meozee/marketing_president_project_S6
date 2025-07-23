# apps/core/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def about_us_view(request):
    """
    View untuk menampilkan halaman About Us.
    """
    return render(request, 'core/about_us.html')
