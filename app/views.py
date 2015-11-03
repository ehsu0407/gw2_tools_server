from views_builders import home as view_home

# Create your views here.
def home(request):
    return view_home.get_response(request)