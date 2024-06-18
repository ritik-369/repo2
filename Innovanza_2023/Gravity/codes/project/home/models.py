from django.db import models

# Create your models here.

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
class intern(models.Model):
    internship_name=models.CharField(max_length=122 , default="")
    company_name=models.CharField(max_length=122 , default="")
    location=models.CharField(max_length=122 , default="")
    category=models.CharField(max_length=122 , default="")
    CTC=models.CharField(max_length=122 , default="")
    type=models.CharField(max_length=122 , default="")
    apply_link=models.CharField(max_length=122 , default="")
    duration=models.CharField(max_length=122 , default="")
    upload_duration=models.CharField(max_length=122 , default="")











