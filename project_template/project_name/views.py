from django import shortcuts


def home(request):
    return shortcuts.render(request, 'home.html')
