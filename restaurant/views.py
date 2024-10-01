from django.shortcuts import render, redirect
from datetime import datetime, timedelta
import random

def main(request):
    return render(request, 'restaurant/main.html')

def main_view(request):
    return render(request, 'restaurant/main.html') 


def order_view(request):
    specials = [
        {'name': 'Crunchwrap Supreme', 'price': 6},
        {'name': 'Grilled Cheese Burrito', 'price': 7},
        {'name': 'Mexican Pizza', 'price': 6}
    ]
    daily_special = random.choice(specials)
    context = {
        'daily_special': daily_special
    }
    return render(request, 'restaurant/order.html', context)

def confirmation(request):
    if request.method == 'POST':
        order_items = []
        total_price = 0

        if request.POST.get('daily_special'):
            order_items.append(request.POST.get('daily_special_name'))
            total_price += float(request.POST.get('daily_special_price'))

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        special_instructions = request.POST.get('special_instructions')

        ready_time = datetime.now() + timedelta(minutes=random.randint(30, 60))

        context = {
            'order_items': order_items,
            'total_price': total_price,
            'name': name,
            'phone': phone,
            'email': email,
            'ready_time': ready_time.strftime("%I:%M %p")
        }

        return render(request, 'restaurant/confirmation.html', context)
    else:
        return redirect('order')