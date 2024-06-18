from django.shortcuts import render,HttpResponse
from home.models import intern
from home.scrap import *


"""
    internship_name:models.CharField(max_length=122)
    company_name:models.CharField(max_length=122)
    location:models.CharField(max_length=122)
    CTC:models.CharField(max_length=122)
    type:models.CharField(max_length=122)
    apply_link:models.CharField(max_length=122)
"""

"""
        data["internship_name"]=filter_string(content.find("a",class_="view_detail_button").get_text())
        data["company_name"]=filter_string(content.find("a",class_="link_display_like_text view_detail_button").get_text())
        data["location"]=filter_string(content.find("a",class_="location_link view_detail_button").get_text())
        data["upload_duration"]=filter_string(content.find("div",class_="posted_by_container").get_text())
        data["CTC"]=filter_string(content.find("span",class_="stipend").get_text())
        data["type"]=filter_string(content.find("div",class_="status status-small status-inactive").get_text())
        data["apply_link"]=filter_string(content.find_all("div",class_="btn btn-primary b2b_apply_now")[0].get("data-redirect_url"))
        data["duration"]=filter_string(content.find_all("div",class_="item_body")[1].get_text())
"""

def index(request):
    return render(request,"obj/index.html")


def search_page(request):
    category="0"
    location="0"
    home="0"
    fetch=1
    if request.method=="POST":
        category=request.POST.get("category")
        location=request.POST.get("location")
        home=(request.POST.get("radio")=="true")
        if len(category)==0:
            category="0"
        if len(location)==0:
            location="0"
        if home==0:
            home="0"
        if fetch==1:
            sc=Scrap()
            data=sc.scrap_from_internshala(category,location,home)
            intern.objects.all().delete()
            for obj in data:
                if location!="0":
                    obj["location"]=location.capitalize()
                if home!="0":
                    obj["location"]="Work From Home"
                inter=intern(upload_duration=obj["upload_duration"],internship_name=obj["internship_name"],company_name=obj["company_name"],location=obj["location"],CTC=obj["CTC"],type=obj["type"],apply_link=obj["apply_link"],duration=obj["duration"])
                inter.save()

    elif fetch==1:
        sc=Scrap()
        data=sc.scrap_from_internshala(category,location,home)
        intern.objects.all().delete()
        for obj in data:
            inter=intern(upload_duration=obj["upload_duration"],internship_name=obj["internship_name"],company_name=obj["company_name"],location=obj["location"],CTC=obj["CTC"],type=obj["type"],apply_link=obj["apply_link"],duration=obj["duration"])
            inter.save()

    context={
         "context":intern.objects.all(),
         "location":location,
         "category":category,
         "home":home,
    }
    if home!="0":
        location="Work From Home"
    lst=list()
    obj=intern.objects.all()
    for elem in intern.objects.all():
        lst.append(elem)
    context["context"]=lst
    return render(request,"search_page/index.html",context)





