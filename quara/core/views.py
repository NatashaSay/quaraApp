from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from .forms import *
from quaraDB.queries import *
from quaraDB.models import *
from django.template.context_processors import csrf
from datetime import datetime
from .statistic import createset
from .type import createparameter
import qrcode



def index(request):
    if request.method == 'POST':
        print('Post')
        print(request.POST)
    return render(request, 'index.html')


@login_required
def home(request):
    current_user = request.user.id
    username = request.user.username
    statistic = get_all_statistic()
    print(statistic)
    if isShop(current_user):
        exp = get_for_shop(current_user)
        print(exp)
        return render(request, 'shop/shophome.html', {'username': username, 'exp':exp})

    else:
        return render(request, 'main.html', {'username': username, 'statistic':statistic})


@login_required
def profile(request):
    emulator = 0
    if request.method == 'POST':
        print('Post')
        print(request.POST)
        print(request.POST['text'])
        emulator = request.POST['text']

        emulator = createparameter(int(emulator), 200, 20, 1,0)
        #Profile.objects.filter(pk=request.user.id).update(percent=emulator)
    current_user = request.user
    username = request.user.username
    context = get_profile(current_user.id)
    # context.percent = emulator
    # context.save()
    image = request.user.profile.image.url

    # print(profile.img)
    # print(profile.id)
    # print(profile.id)
    info ={
        'date': current_user.date_joined,
        'email': current_user.email,
        'emulator': str(emulator)
    }
    return render(request, 'profile.html',  {'context': context, 'info': info, 'username': username, 'image':image} )


@login_required
def edit(request):
    username = request.user.username
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'username': username
    }
    return render(request, 'edit.html', context)


@login_required
def health(request):
    username = request.user.username
    if request.method == 'POST':
        form = ControlForm(request.POST)
        if form.is_valid():
            current_user = request.user

            profile = Profile.objects.get(user_id=current_user.id)
            form.instance.userprofile_id = profile.id
            form.save()
            #request.session['vote_id'] = form.save().id
            return render(request, 'main.html')
        else:
            print('not valid')
    else:
        model = Control
        form = ControlForm(instance=request.user)
        return render(request, 'health.html', {'form' : form, 'username':username})


@login_required
def monitoring(request):
    username = request.user.username
    current_user_id = get_profile_id(request.user.id)
    context = get_control(current_user_id)

    dataset = createset(request.user.id)

    return render(request, 'monitoring.html', {'dataset': dataset,'context': context, 'username':username })


@login_required
def deletemonitoring(request, pk):
    deletemon(pk)
    return redirect('monitoring')


@login_required
def call(request):
    if request.method == 'POST':
        form = CallForm(request.POST)
        if form.is_valid():
            profile = get_profile_id(request.user.id)
            form.instance.userprofile_id = profile
            form.save()
            return redirect('home')
        else:
            print('not valid')
    else:
        model = Call
        form = CallForm(instance=request.user)
        return render(request, 'call.html', {'form' : form})


@login_required
def mycalls(request):
    username = request.user.username
    current_user_id = get_profile_id(request.user.id)
    context = get_calls(current_user_id)
    return render(request, 'mycalls.html', {'context': context, 'username':username})


@login_required
def cancellcall(request, pk):
    call = get_call(pk)
    call.status = True
    call.save()
    return redirect('mycalls')


@login_required
def shops(request):

    username = request.user.username
    shops = get_shops()
    #status = request.session['status']
    current_user_id = get_profile_id(request.user.id)
    exp = get_expedition(current_user_id)

    return render(request, 'shops.html', {'shops':shops, 'username':username, 'exp':exp})


@login_required
def book(request, pk):
    if request.POST:
        print('It s post')
        time = request.POST.get('inputTime', '')
        check_duplications(request.user.id, pk)
        data = str(time)+str(request.user.username)
        #request.session['status'] = 'Reserved'
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=3,
            border=0,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save('core/static/qr/one.png')


        Expedition.objects.create(userprofile_id=request.user.id, shop_id=pk, status='Awaiting confirmation', expected=time)

    return redirect('shops')


@login_required
def confirm(request, pk=1):
    if request.POST:
        print('It s confirm')
        expedition = get_expedition_for(get_shop_id(request.user.id), pk)
        print(expedition)


    return redirect('home')


def statistics(request):
    username = request.user.username
    return render(request, 'home.html', {'username':username})
