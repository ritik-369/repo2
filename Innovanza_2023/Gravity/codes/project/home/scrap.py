import requests
from bs4 import BeautifulSoup
import html5lib

def filter_string(string,frs=0):
    res=""
    st=0
    for i in range(len(string)):
        if string[i]=='\n' and frs==0:
            continue
        if string[i]==' ' and st==0:
            continue
        st=1
        res=res+string[i]
    length=len(res)
    res2=""
    st=0
    for i in range(length-1,-1,-1):
        if st==0 and res[i]==' ':
            continue
        st=1
        res2=res2+res[i]
    res2=res2[::-1]
    return res2

class Internshala:
    url="https://internshala.com/internships/"
    

    def get_data_from_content(self,content):
        """
        internship_name:Inside Sales Specialist
        company_name:Skill-Lync
        location: Hyderabad, Chennai, Delhi, Bangalore
        upload_duration:6 days ago
        CTC:3 - 4.5 LPA
        type: Fresher Job
        apply_link: "/job/detail/inside-sales-specialist-fresher-jobs-in-multiple-locations-at-skill-lync1676529765"
        """
        data=dict()
        data["internship_name"]=filter_string(content.find("a",class_="view_detail_button").get_text())
        data["company_name"]=filter_string(content.find("a",class_="link_display_like_text view_detail_button").get_text())
        data["location"]=filter_string(content.find("a",class_="location_link view_detail_button").get_text())
        data["upload_duration"]=filter_string(content.find("div",class_="posted_by_container").get_text())
        data["CTC"]=filter_string(content.find("span",class_="stipend").get_text())
        data["type"]=filter_string(content.find("div",class_="status status-small status-inactive").get_text())
        # data["apply_link"]="https://internshala.com/"+filter_string(content.find_all("div",class_="btn btn-primary b2b_apply_now")[0].get("data-redirect_url"))
        data["apply_link"]="https://internshala.com/"
        data["duration"]=filter_string(content.find_all("div",class_="item_body")[1].get_text())
        return data
    

    
    def get_container(self,url):
        r=requests.get(url)
        soup=BeautifulSoup(r.content,"html.parser") 
        container=soup.find("div",id="internship_list_container_1")
        return container
    
    def get_internship_data(self,category="0",location="0",home="0"):
        """
        https://internshala.com/internships/mba-internship/
        https://internshala.com/internships/internship-in-adilabad/
        https://internshala.com/internships/work-from-home-internships/
        https://internshala.com/internships/3d-printing-internship-in-bangalore/
        https://internshala.com/internships/work-from-home-3d-printing-internships/
        """
        url=self.url
        """
        https://internshala.com/internships/mba-internship/
        https://internshala.com/internships/internship-in-adilabad/
        https://internshala.com/internships/work-from-home-internships/
        https://internshala.com/internships/3d-printing-internship-in-bangalore/
        https://internshala.com/internships/work-from-home-3d-printing-internships/
        """
        url=self.url
        if category=="0" and location=="0" and home=="0":
            url="https://internshala.com/internships/"

        if category=="0" and location=="0" and home!="0":
            url="https://internshala.com/internships/work-from-home-internships/"

        if category=="0" and location!="0" and home=="0":
            url="https://internshala.com/internships/internship-in-"
            url=url+location

        if category=="0" and location!="0" and home!="0":
            url="https://internshala.com/internships/work-from-home-internships-in-"
            url=url+location

        if category!="0" and location=="0" and home=="0":
            #https://internshala.com/internships/.net-development-internship/
            url="https://internshala.com/internships/"
            url=url+category+"-internship"

        if category!="0" and location=="0" and home!="0":
            #https://internshala.com/internships/work-from-home-.net-development-internships/
            url="https://internshala.com/internships/work-from-home-"
            url=url+category
            url=url+"-internships"

        if category!="0" and location!="0" and home=="0":
            url="https://internshala.com/internships/"
            url=url+category+"-internship-in-"
            url=url+location
            

        if category!="0" and location!="0" and home!="0":
            url="https://internshala.com/internships/work-from-home-"
            url=url+category+"-internships-in-"
            url=url+location
            

        container=self.get_container(url)
        # print(url)
        contents=container.find_all("div",class_="container-fluid")  
        data=list()
        start=1
        end=len(contents)
        for i in range(1,end,1):
            try:
                cont=contents[i]
                # print(self.get_data_from_content(cont))
                data.append(self.get_data_from_content(cont))
                # print("Hellllloooooooo")
            except:
                continue
        return data

class Scrap:
    #variables
    #methods
    def scrap_from_internshala(self,category="0",location="0",home="0"):
        inter=Internshala()
        # print(inter.get_internship_data())
        return inter.get_internship_data(category,location,home)


sc=Scrap()
sc.scrap_from_internshala()

        







'''
import requests
from bs4 import BeautifulSoup
import html5lib

def filter_string(string):
    res=""
    for i in range(len(string)):
        if string[i]=='\n':
            continue
        if string[i]==' ':
            continue
        res=res+string[i]
    return res

class Internshala:
    url="https://internshala.com/internships/"

    def get_data_from_content(self,content):
        """
        internship_name:Inside Sales Specialist
        company_name:Skill-Lync
        location: Hyderabad, Chennai, Delhi, Bangalore
        upload_duration:6 days ago
        CTC:3 - 4.5 LPA
        type: Fresher Job
        apply_link: "/job/detail/inside-sales-specialist-fresher-jobs-in-multiple-locations-at-skill-lync1676529765"
        """
        data=dict()
        data["internship_name"]=filter_string(content.find("a",class_="view_detail_button").get_text())
        data["company_name"]=filter_string(content.find("a",class_="link_display_like_text view_detail_button").get_text())
        data["location"]=filter_string(content.find("a",class_="location_link view_detail_button").get_text())
        data["upload_duration"]=filter_string(content.find("div",class_="posted_by_container").get_text())
        data["CTC"]=filter_string(content.find("span",class_="stipend").get_text())
        data["type"]=filter_string(content.find("div",class_="status status-small status-inactive").get_text())
        data["apply_link"]=filter_string(content.find_all("div",class_="btn btn-primary b2b_apply_now")[0].get("data-redirect_url"))
        return data
    

    
    def get_container(self,url):
        r=requests.get(url)
        soup=BeautifulSoup(r.content,"html.parser") 
        container=soup.find("div",id="internship_list_container_1")
        return container
    
    def get_internship_data(self):
        container=self.get_container(self.url)
        contents=container.find_all("div",class_="container-fluid")  
        data=list()
        start=1
        end=len(contents)
        for i in range(1,end,1):
            try:
                data.append(self.get_data_from_content(contents[i]))
            except:
                continue
        return data

class Scrap:
    #variables
    #methods
    def scrap_from_internshala(self):
        inter=Internshala()
        print(inter.get_internship_data())


sc=Scrap()
sc.scrap_from_internshala()

        
'''