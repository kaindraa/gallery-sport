from django.shortcuts import render
def show_main(request):
    context = {
        'name' : 'Jersey Timnas',
        'price': '150000',
        'description': 'Jersey Timnas, Ukuran XL, Original',
        'quantity' : 10,
        'discount' : 0.0
    }

    return render(request, "main.html", context)
