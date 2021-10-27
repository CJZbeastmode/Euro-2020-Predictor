from django.db import models
from django.contrib.auth.models import User
from django.db.models.aggregates import Max

# Make User Email Unique
User._meta.get_field('email')._unique = True

# Create your models here.

##### Prediction
class Prediction(models.Model):
    user_id = models.IntegerField()
    create_time = models.CharField(max_length=120)
    gs_a1 = models.CharField(max_length=120)
    gs_a2 = models.CharField(max_length=120)
    gs_a3 = models.CharField(max_length=120)
    gs_a4 = models.CharField(max_length=120)
    gs_b1 = models.CharField(max_length=120)
    gs_b2 = models.CharField(max_length=120)
    gs_b3 = models.CharField(max_length=120)
    gs_b4 = models.CharField(max_length=120)
    gs_c1 = models.CharField(max_length=120)
    gs_c2 = models.CharField(max_length=120)
    gs_c3 = models.CharField(max_length=120)
    gs_c4 = models.CharField(max_length=120)
    gs_d1 = models.CharField(max_length=120)
    gs_d2 = models.CharField(max_length=120)
    gs_d3 = models.CharField(max_length=120)
    gs_d4 = models.CharField(max_length=120)
    gs_e1 = models.CharField(max_length=120)
    gs_e2 = models.CharField(max_length=120)
    gs_e3 = models.CharField(max_length=120)
    gs_e4 = models.CharField(max_length=120)
    gs_f1 = models.CharField(max_length=120)
    gs_f2 = models.CharField(max_length=120)
    gs_f3 = models.CharField(max_length=120)
    gs_f4 = models.CharField(max_length=120)
    btf_1 = models.CharField(max_length=120)
    btf_2 = models.CharField(max_length=120)
    btf_3 = models.CharField(max_length=120)
    btf_4 = models.CharField(max_length=120)
    btf_l1 = models.CharField(max_length=120)
    btf_l2 = models.CharField(max_length=120)
    ks16_aw = models.CharField(max_length=120)
    ks16_al = models.CharField(max_length=120)
    ks16_bw = models.CharField(max_length=120)
    ks16_bl = models.CharField(max_length=120)
    ks16_cw = models.CharField(max_length=120)
    ks16_cl = models.CharField(max_length=120)
    ks16_dw = models.CharField(max_length=120)
    ks16_dl = models.CharField(max_length=120)
    ks16_ew = models.CharField(max_length=120)
    ks16_el = models.CharField(max_length=120)
    ks16_fw = models.CharField(max_length=120)
    ks16_fl = models.CharField(max_length=120)
    ks16_gw = models.CharField(max_length=120)
    ks16_gl = models.CharField(max_length=120)
    ks16_hw = models.CharField(max_length=120)
    ks16_hl = models.CharField(max_length=120)
    ks8_aw = models.CharField(max_length=120)
    ks8_al = models.CharField(max_length=120)
    ks8_bw = models.CharField(max_length=120)
    ks8_bl = models.CharField(max_length=120)
    ks8_cw = models.CharField(max_length=120)
    ks8_cl = models.CharField(max_length=120)
    ks8_dw = models.CharField(max_length=120)
    ks8_dl = models.CharField(max_length=120)
    ks4_aw = models.CharField(max_length=120)
    ks4_al = models.CharField(max_length=120)
    ks4_bw = models.CharField(max_length=120)
    ks4_bl = models.CharField(max_length=120)
    final_l = models.CharField(max_length=120)
    winner = models.CharField(max_length=120)





##### Extra
class Newsletter(models.Model):
    email = models.CharField(max_length=120)

    def __str__(self):
        return self.email

class NewsArticle(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    author = models.CharField(max_length=120)
    datetime = models.CharField(max_length=120, default='2000-01-01 00:00:00')

    def __str__(self):
        return self.title

