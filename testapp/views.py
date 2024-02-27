
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import PDFDocumentForm
from django.views.decorators.csrf import requires_csrf_token
@requires_csrf_token
def upload_pdf(request):
    if request.method == 'POST':
        form = PDFDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to a success page
    else:
        form = PDFDocumentForm()

    return render(request, 'pdf.html', {'form': form})

