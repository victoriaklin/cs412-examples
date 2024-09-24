from django.shortcuts import render
import random


# Create your views here.
quotes = [
    "Your victory is right around the corner. Never give up.",
    "You should never feel afraid to become a piece of art. It's exhilarating.",
    "My happiness doesn't come from money or fame. My happiness comes from seeing life without struggle."
]

images = [
    "https://static01.nyt.com/images/2023/03/03/arts/03playlist/03playlist-superJumbo.jpg",
    "https://i.pinimg.com/736x/8d/e3/8b/8de38b60dca4ac6aafb590debc36b3ca.jpg",
    "https://thumbs.dreamstime.com/b/nicki-minaj-nicki-minaj-mtv-video-music-awards-held-forum-inglewood-usa-august-99080536.jpg"
]

def quote(request):
    template_name = 'quotes/quote.html'

    context = {
        "quote" : random.choice(quotes),
        "image" : random.choice(images),
    }

    return render(request, template_name, context)

def show_all(request):
    template_name = 'quotes/show_all.html'

    context = {
        'quotes': quotes,
        'images': images
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'quotes/about.html'

    return render(request, template_name)