class Internship(models.Model):
    internship_name=models.CharField(max_length=122)
    company_name=models.CharField(max_length=122)
    location=models.CharField(max_length=122)
    CTC=models.CharField(max_length=122)
    type=models.CharField(max_length=122)
    apply_link=models.CharField(max_length=122)
    duration=models.CharField(max_length=122)
    upload_duration=models.CharField(max_length=122)