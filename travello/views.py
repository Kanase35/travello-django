from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):

    # dest1 = Destination()
    # dest2 = Destination()
    # dest3 = Destination()

    # dest1.name = "Mumbai"
    # dest2.name = "Pune"
    # dest3.name = "Nagpur"

    # dest1.price = 750
    # dest2.price = 600
    # dest3 .price= 500


    # dest1.desc = "Capital of Maharashtra"
    # dest2.desc = "Vidya cha maher ghar"
    # dest3.desc = "2nd Capial of Maharashtra"

    # dest1.img = "destination_1.jpg"
    # dest2.img = "destination_2.jpg"
    # dest3.img = "destination_3.jpg"

    # dest1.offer = True
    # dest2.offer = False
    # dest3.offer = False



    # dests  = [dest1, dest2, dest3]

    dests = Destination.objects.all()

 


    return render(request, 'index.html', {"dests": dests})