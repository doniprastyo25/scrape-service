from mongoengine import Document , fields
# Create your models here.

class DataScrape(Document):
    job = fields.StringField()
    link = fields.URLField()
    additional_info = fields.DictField()

    def __str__(self):
        return self.job