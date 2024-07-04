from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import BookingForm

@csrf_exempt
def bookroom(request):
    print("Request Method:", request.method)
    if request.method == 'POST':
        print("POST Data:", request.POST)
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html', {'form': form})
        else:
            print("Form errors:", form.errors)
    else:
        form = BookingForm()

    context = {'form': form}
    return render(request, 'BookingForm.html', context)
