from django.shortcuts import render
from django.views import View


class ShopHome(View):

    def get(self, request):
        return render(request, 'home.html')

class ShopAbout(View):

    def get(self, request):
        return render(request, 'about.html')
