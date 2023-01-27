from django.shortcuts import render
# from django.views import View 
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import BoyBand
from django.urls import reverse

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"
    # def get(self, request):
    #     # Here we are returning a generic response
    #     return HttpResponse("Collector Home")
   

class About(TemplateView):
     template_name = "about.html"
    # def get(self, request):
    #     return HttpResponse("Collector About")

# class BoyBand:
#     def __init__(self,group_name, image, member, bio):
#         self.group_name = group_name
#         self.image = image
#         self.member = member
#         self.bio = bio

# boybands = [
#     BoyBand("Bts","https://d3tvwjfge35btc.cloudfront.net/Assets/GalleryImage/79/303/L_g0158730379.jpg","Consists of 7 members", "BTS (방탄소년단) is a South Korean boy group that consists of 7 members: RM, Jin, Suga, J-Hope, Jimin, V and Jungkook. They are under Big Hit Music (part of HYBE Labels). BTS debuted on June 13, 2013 with the lead single ‘No More Dream‘ on album ‘2 Cool 4 Skool‘. On June 15, 2022 BigHit Music released an announcement stating that BTS would not go on hiatus, but will focus on releasing solo music for a while."),
#     BoyBand("Seventeen","https://ae01.alicdn.com/kf/Se0d1c0799453478daafbe90f43ad2945w/Korean-Boy-Group-Kpop-Seventeen-5D-DIY-Diamond-Painting-Full-Square-Round-Drill-Embroidery-Rhinestones-Cross.jpg_640x640.jpg","Consists of 13 members","Seventeen (세븐틴) is a K-Pop boy group that consists of 13 members: S.coups, Wonwoo, Mingyu, Vernon (the hip-hop unit); Woozi, Jeonghan, Joshua, DK, Seungkwan (the vocal unit); Hoshi, Jun, The8, Dino (the performance unit). Seventeen debuted on May 26, 2015, with the mini album “17 Carat” and title track “Adore You“, under Pledis Entertainment."),
#     BoyBand("MonstaX","https://imageio.forbes.com/specials-images/imageserve/610b04efa4cd487bef8a6113/0x0.jpg?format=jpg&width=1200","Consists of 6 members","MONSTA X (몬스타엑스) consists of 6 members: Shownu, Minhyuk, Kihyun, Hyungwon, Joohoney, and I.M. They were created through the survival program NO.MERCY. MONSTA X debuted on May 14, 2015, under Starship Entertainment. Monsta X is also under the US label Maverick Agency as of February 26th 2019. On October 31, 2019 following the recent controversies, Wonho announced his departure from the group."),
#     BoyBand("Got7","http://kpopgotmyseoul.weebly.com/uploads/2/5/6/0/25604243/9987248_orig.jpg","Consist of 7 members","GOT7 (갓세븐) consists of 7 members: Jay B, Mark, Jackson, Jinyoung, Youngjae, BamBam and Yugyeom. They debuted on January 16th 2014, under JYP Entertainment. JYP Entertainment released a statement that the group will be officially leaving the agency on January 19th, 2021 following the expiration of their contract. On February 20, 2021 GOT7 released its 1st single after leaving JYP Ent., called “Encore“, and it seems the group has signed under Warner Music Korea.")
# ]

class BoyBandList(TemplateView):
    template_name = "boyband_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
         # to get the query parameter we have to acccess it in the request.GET dictionary object        
        name = self.request.GET.get("group_name")
        # if/else statement to filter through name
        if name != None:
            context["boybands"] = BoyBand.objects.filter(group_name__icontains = name)
            context["header"] = f"Searching for {name}"
        else:
             context["boybands"] = BoyBand.objects.all()
             context["header"] = "Trending BoyBands"
        # Below is the fake db
        # context["boybands"] = boybands
        return context

class BoyBandCreate(CreateView):
    model = BoyBand
    fields = ['group_name', 'img', 'member', 'bio', 'verified_artist']
    template_name = "boyband_create.html"
# this will get the pk from the route and redirect to artist view
    def get_success_url(self):
        return reverse ('boyband_detail', kwargs={'pk': self.object.pk})
    # before we modify it
    # success_url = "/boybands/"

class BoyBandDetail(DetailView):
    model = BoyBand
    template_name = "boyband_detail.html"

class BoyBandUpdate(UpdateView):
    model = BoyBand
    fields = ['group_name', 'img', 'member', 'bio', 'verified_artist']
    template_name = "boyband_update.html"
    # After we modify it
    def get_success_url(self):
        return reverse('boyband_detail', kwargs={'pk': self.object.pk})
    # Before we modify it
    # success_url = "/boybands/"

class BoyBandDelete(DeleteView):
    model = BoyBand
    template_name = "boyband_delete.html"
    success_url = "/boybands/"

class Albums:
    def __init__(self, album_name, artist, image, year):
        self.album_name = album_name
        self.artist = artist
        self.image = image
        self.year = year

albums = [
    Albums("Map of the Soul 7","Bts","https://upload.wikimedia.org/wikipedia/en/thumb/2/21/BTS_-_Map_of_the_Soul_7.png/220px-BTS_-_Map_of_the_Soul_7.png", "2020"),
    Albums("Face the Sun", "Seventeen","https://pbs.twimg.com/media/FRJ3iKCaQAE2Y0-.jpg", "2022"),
    Albums("The Dreaming", "MonstaX","https://i.redd.it/1mybeahzomu71.jpg","2021"),
    Albums("Breath of Love: Last Pieace","Got7", "http://cdn.shopify.com/s/files/1/0253/6400/4911/products/got7-4th-album-breath-of-love-last-piece-jyp-entertainment-cd-22953531343024.jpg?v=1644643642" ,"2020")
]

class AlbumList(TemplateView):
    template_name = "album_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Below is the fake db
        context["albums"] = albums
        return context

