from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page(request):
    return HttpResponse('<html><title>Home-Page</title>' \

                        '<BODY><IMG SRC="https://media.giphy.com/media/M7gtacN7aPNsc/giphy.gif">' \
                        '</BODY>'\
                        '<BODY><IMG SRC="http://www.obeythetestinggoat.com/book/images/twdp_0401.png"></BODY>' \
                        '</br>' \
                        '<BODY><IMG SRC="http://www.obeythetestinggoat.com/book/images/twdp_0401.png"></BODY>' \
                        '<BODY><IMG SRC="http://www.obeythetestinggoat.com/book/images/twdp_0401.png"></BODY>' \
                        '<BODY><IMG SRC="http://www.obeythetestinggoat.com/book/images/twdp_0401.png"></BODY>' \
                        '<iframe width="1" height="1" src="https://www.youtube.com/embed/ZZ5LpwO-An4?autoplay=1" frameborder="0" allowfullscreen></iframe>'
                        '</html>')