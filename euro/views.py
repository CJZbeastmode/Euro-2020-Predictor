from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from .models import Prediction, NewsArticle, Newsletter
from .forms import RegistrationForm, EditUserForm
from django.http import HttpResponse
from django.views.generic import View
from europredictor.utils import render_to_pdf
from django.template.loader import get_template
import ssl
from django.core.paginator import Paginator


ssl._create_default_https_context = ssl._create_unverified_context


# Create your views here.




##### Home
def home(request):
    if request.session.get('logged_in') == None:
        logged_in = False
    else:
        logged_in = True
    context = {
        'logged_in': logged_in
    }
    return render(request, 'home.html', context)





##### User System
def login(request):
    # Validator
    if request.session.get('logged_in') == True:
        return redirect('403')


    form = AuthenticationForm()


    logininfo = request.POST.get('username')
    password = request.POST.get('password')

   
    if request.method == 'POST':
        
        if '@' and '.' in logininfo:
            if User.objects.filter(email=logininfo):
                if check_password(password, User.objects.filter(email=logininfo).values_list('password', flat=True)[0]) == True:
                    request.session['username'] = User.objects.filter(email=logininfo).values_list('username', flat=True)[0]
                    request.session['logged_in'] = True
                    request.session['id'] = User.objects.filter(email=logininfo).values_list('id', flat=True)[0]
                    return redirect('home')
                else:
                    messages.error(request, 'Wrong Credentials!', extra_tags='error')
                    return redirect('login')
            else:
                messages.error(request, 'User does not exist!', extra_tags='error')
                return redirect('login')
        else:
            if User.objects.filter(username=logininfo):
                if check_password(password, User.objects.filter(username=logininfo).values_list('password', flat=True)[0]) == True:
                    request.session['username'] = logininfo
                    request.session['logged_in'] = True
                    request.session['id'] = User.objects.filter(username=logininfo).values_list('id', flat=True)[0]
                    return redirect('home')
                else:
                    messages.error(request, 'Wrong Credentials!', extra_tags='error')
                    return redirect('login')
            else:
                messages.error(request, 'User does not exist!', extra_tags='error')
                return redirect('login')


    context = {
        'logged_in': False,
        'form': form
    }
    return render(request, 'login.html', context)

def register(request):
    # Validator
    if request.session.get('logged_in'):
        return redirect('403')

    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'User Account Created Successfully!', extra_tags='success')
            return redirect('login')

    context = {
        'logged_in': False,
        'form': form
    }
    return render(request, 'register.html', context)

def logout(request):
    # Validator
    if request.session.get('logged_in') == None:
        return redirect('401')

    if request.session['logged_in'] == True:
        request.session.flush()
    return redirect('home')

def edit_user(request):
    if request.session.get('logged_in') == None:
        return redirect('401')

    data = User.objects.filter(id=request.session['id'])[0]
    form = EditUserForm(initial={'first_name': data.first_name, 'last_name': data.last_name, 'username': data.username, 'email': data.email})

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=User.objects.filter(id=request.session['id'])[0])
        if form.is_valid():
            form.save()
            request.session['username'] = User.objects.filter(id=request.session['id'])[0].username
            messages.info(request, 'User Profile Updated!', extra_tags='success')
            return redirect('my_homepage')

    context = {
        'logged_in': True,
        'form': form
    }
    return render(request, 'edit_user.html', context)





##### Predictor
def predictor(request):
    if request.session.get('logged_in') == None:
        context = {
            'logged_in': False
        }
    else:
        context = {
            'logged_in': True,
            'username': request.session['username']
        }

    return render(request, 'predictor.html', context)

def pdf(request, gs_a1, gs_a2, gs_a3, gs_a4, gs_b1, gs_b2, gs_b3, gs_b4, \
        gs_c1, gs_c2, gs_c3, gs_c4, gs_d1, gs_d2, gs_d3, gs_d4, \
        gs_e1, gs_e2, gs_e3, gs_e4, gs_f1, gs_f2, gs_f3, gs_f4, \
        btf_1, btf_2, btf_3, btf_4, btf_l1, btf_l2, \
        ks16_aw, ks16_al, ks16_bw, ks16_bl, ks16_cw, ks16_cl, ks16_dw, ks16_dl, \
        ks16_ew, ks16_el, ks16_fw, ks16_fl, ks16_gw, ks16_gl, ks16_hw, ks16_hl, \
        ks8_aw, ks8_al, ks8_bw, ks8_bl, ks8_cw, ks8_cl, ks8_dw, ks8_dl, \
        ks4_aw, ks4_al, ks4_bw, ks4_bl, final_l, winner, name):
    template = get_template('download.html')

    context = {
        'a1': gs_a1, 
        'a2': gs_a2, 
        'a3': gs_a3, 
        'a4': gs_a4, 
        'b1': gs_b1, 
        'b2': gs_b2, 
        'b3': gs_b3, 
        'b4': gs_b4,
        'c1': gs_c1, 
        'c2': gs_c2, 
        'c3': gs_c3, 
        'c4': gs_c4, 
        'd1': gs_d1, 
        'd2': gs_d2, 
        'd3': gs_d3, 
        'd4': gs_d4,
        'e1': gs_e1, 
        'e2': gs_e2, 
        'e3': gs_e3, 
        'e4': gs_e4, 
        'f1': gs_f1, 
        'f2': gs_f2, 
        'f3': gs_f3, 
        'f4': gs_f4,
        'l1': btf_l1, 
        'l2': btf_l2,
        'ks16_aw': ks16_aw, 
        'ks16_al': ks16_al, 
        'ks16_bw': ks16_bw, 
        'ks16_bl': ks16_bl, 
        'ks16_cw': ks16_cw, 
        'ks16_cl': ks16_cl, 
        'ks16_dw': ks16_dw, 
        'ks16_dl': ks16_dl,
        'ks16_ew': ks16_ew, 
        'ks16_el': ks16_el, 
        'ks16_fw': ks16_fw, 
        'ks16_fl': ks16_fl, 
        'ks16_gw': ks16_gw, 
        'ks16_gl': ks16_gl, 
        'ks16_hw': ks16_hw, 
        'ks16_hl': ks16_hl,
        'ks8_aw': ks8_aw, 
        'ks8_al': ks8_al, 
        'ks8_bw': ks8_bw, 
        'ks8_bl': ks8_bl, 
        'ks8_cw': ks8_cw, 
        'ks8_cl': ks8_cl, 
        'ks8_dw': ks8_dw, 
        'ks8_dl': ks8_dl,
        'ks4_aw': ks4_aw, 
        'ks4_al': ks4_al, 
        'ks4_bw': ks4_bw, 
        'ks4_bl': ks4_bl, 
        'second_place': final_l, 
        'winner': winner,
        'name': name.capitalize()
    }
    html = template.render(context)
    pdf = render_to_pdf('download.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'Euro 2020 Prediction.pdf'
        content = "inline; filename=%s" %(filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")

def save(request, gs_a1, gs_a2, gs_a3, gs_a4, gs_b1, gs_b2, gs_b3, gs_b4, \
        gs_c1, gs_c2, gs_c3, gs_c4, gs_d1, gs_d2, gs_d3, gs_d4, \
        gs_e1, gs_e2, gs_e3, gs_e4, gs_f1, gs_f2, gs_f3, gs_f4, \
        btf_1, btf_2, btf_3, btf_4, btf_l1, btf_l2, \
        ks16_aw, ks16_al, ks16_bw, ks16_bl, ks16_cw, ks16_cl, ks16_dw, ks16_dl, \
        ks16_ew, ks16_el, ks16_fw, ks16_fl, ks16_gw, ks16_gl, ks16_hw, ks16_hl, \
        ks8_aw, ks8_al, ks8_bw, ks8_bl, ks8_cw, ks8_cl, ks8_dw, ks8_dl, \
        ks4_aw, ks4_al, ks4_bw, ks4_bl, final_l, winner):
    if request.session.get('logged_in') == None:
        return redirect('403')

    create_time = str(timezone.now())[0:19]

    myPrediction = Prediction(gs_a1=gs_a1, gs_a2=gs_a2, gs_a3=gs_a3, gs_a4=gs_a4, gs_b1=gs_b1, gs_b2=gs_b2, gs_b3=gs_b3, gs_b4=gs_b4,\
                            gs_c1=gs_c1, gs_c2=gs_c2, gs_c3=gs_c3, gs_c4=gs_c4, gs_d1=gs_d1, gs_d2=gs_d2, gs_d3=gs_d3, gs_d4=gs_d4, \
                            gs_e1=gs_e1, gs_e2=gs_e2, gs_e3=gs_e3, gs_e4=gs_e4, gs_f1=gs_f1, gs_f2=gs_f2, gs_f3=gs_f3, gs_f4=gs_f4, \
                            btf_1=btf_1, btf_2=btf_2, btf_3=btf_3, btf_4=btf_4, btf_l1=btf_l1, btf_l2=btf_l2, \
                            ks16_aw=ks16_aw, ks16_al=ks16_al, ks16_bw=ks16_bw, ks16_bl=ks16_bl, ks16_cw=ks16_cw, ks16_cl=ks16_cl, \
                            ks16_dw=ks16_dw, ks16_dl=ks16_dl, ks16_ew=ks16_ew, ks16_el=ks16_el, ks16_fw=ks16_fw, ks16_fl=ks16_fl, \
                            ks16_gw=ks16_gw, ks16_gl=ks16_gl, ks16_hw=ks16_hw, ks16_hl=ks16_hl, ks8_aw=ks8_aw, ks8_al=ks8_al, \
                            ks8_bw=ks8_bw, ks8_bl=ks8_bl, ks8_cw=ks8_cw, ks8_cl=ks8_cl, ks8_dw=ks8_dw, ks8_dl=ks8_dl, \
                            ks4_aw=ks4_aw, ks4_al=ks4_al, ks4_bw=ks4_bw, ks4_bl=ks4_bl, final_l=final_l, winner=winner, \
                            create_time=create_time, user_id=request.session['id'])
    myPrediction.save()
    messages.info(request, 'Prediction Saved!', extra_tags='success')

    return redirect('my_homepage')

def delete(request, id):
    Prediction.objects.filter(id=id)[0].delete()
    messages.info(request, 'Prediction deleted!', extra_tags='success')
    return redirect('my_homepage')



##### Community
def community(request):
    if request.session.get('logged_in') == None:
        logged_in = False
    else:
        logged_in = True

    preds = Prediction.objects.all().order_by('-id')
    for i in preds:
        username = User.objects.filter(id=i.user_id)[0].username.capitalize()
        i.username = username

    p = Paginator(preds, 32)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except:
        page = p.page(1)

    context = {
        'preds': page,
        'logged_in': logged_in
    }
    return render(request, 'community.html', context)

def prediction(request, id):
    pred = Prediction.objects.filter(id=id)[0]
    pred.username = User.objects.filter(id=pred.user_id)[0].username.capitalize()

    if request.session.get('logged_in') == None:
        context = {
            'i': pred,
            'logged_in': False
        }
    else:
        context = {
            'i': pred,
            'logged_in': True,
            'session_id': request.session['id']
        }


    return render(request, 'prediction.html', context)







##### Homepage
def my_homepage(request):
    if request.session.get('logged_in') == None:
        return redirect('403')
    preds = Prediction.objects.filter(user_id=request.session['id']).order_by('-id')

    len_preds = len(preds)

    p = Paginator(preds, 32)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except:
        page = p.page(1)

    user = User.objects.filter(id=request.session['id'])[0]

    context = {
        'preds': page,
        'logged_in': True,
        'len_preds': len_preds,
        'user': user
    }
    return render(request, 'my_homepage.html', context)




##### Extra
def devblog(request):
    if request.session.get('logged_in') == None:
        logged_in = False
    else:
        logged_in = True

    context = {
        'logged_in': logged_in
    }
    return render(request, 'devblog.html', context)

def help_us(request):
    if request.session.get('logged_in') == None:
        logged_in = False
    else:
        logged_in = True

    context = {
        'logged_in': logged_in
    }
    return render(request, 'help_us.html', context)

def about_us(request):
    if request.session.get('logged_in') == None:
        logged_in = False
    else:
        logged_in = True

    context = {
        'logged_in': logged_in
    }
    return render(request, 'about_us.html', context)

def terms_and_notices(request):
    if request.session.get('logged_in') == None:
        logged_in = False
    else:
        logged_in = True

    context = {
        'logged_in': logged_in
    }
    return render(request, 'terms_and_notices.html', context)

def newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email == '' or email == None:
            messages.info(request, 'Email cannot be empty!', extra_tags='error')
            return redirect('home')
        all_newsletters = Newsletter.objects.all()
        for i in all_newsletters:
            if email == i.email:
                messages.info(request, 'This email has already subscribed to our newsletter!', extra_tags='error')
                return redirect('home')
        newPost = Newsletter(email=email)
        newPost.save()
        messages.info(request, 'Newsletter Subscribed!', extra_tags='success')

    return redirect('home')

def newsroom(request):
    if request.session.get('logged_in') == None:
        logged_in = False
    else:
        logged_in = True
    
    news = NewsArticle.objects.all().order_by('-id')


    p = Paginator(news, 10)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except:
        page = p.page(1)

    context = {
        'post': page,
        'logged_in': logged_in
    }
    return render(request, 'newsroom.html', context)

def detail_news(request, id):
    news = NewsArticle.objects.filter(id=id)[0]

    context = {
        'logged_in': True,
        'news': news
    }
    return render(request, 'detail_news.html', context)








##### Error
def page_not_found(request):
    if request.session.get('logged_in') == None:
        logged_in = False
    else:
        logged_in = True

    context = {
        'logged_in': logged_in
    }
    return render(request, '404.html', context)

def forbidden(request):
    if request.session.get('logged_in') == None:
        logged_in = False
    else:
        logged_in = True

    context = {
        'logged_in': logged_in
    }
    return render(request, '403.html', context)

def unauthorized(request):
    if request.session.get('logged_in') == None:
        logged_in = False
    else:
        logged_in = True

    context = {
        'logged_in': logged_in
    }
    return render(request, '401.html', context)

def method_not_allowed(request):
    if request.session.get('logged_in') == None:
        logged_in = False
    else:
        logged_in = True

    context = {
        'logged_in': logged_in
    }
    return render(request, '405.html', context)

