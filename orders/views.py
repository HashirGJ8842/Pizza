from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth import login, logout, user_logged_in, user_logged_out, authenticate
from django.contrib.auth.models import User
from .models import Pizza, SubsPlatters, SaladsPasta, Toppings, FinalPizza, FinalSalads, FinalSubs, FinalToppings, Receipt


def logout_view(request):
    logout(request)
    return render(request, 'orders/index.html', context={'type': 'success', 'message': 'Successfully Logged Out', 'username': request.user.username})


def index(request):
    return render(request, 'orders/index.html', context={'username': request.user.username})


def register(request):
    if request.POST.get('username') == None:
        return render(request, 'orders/register.html')

    try:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user = User.objects.create_user(username, email, password)
        if password != confirm_password:
            return render(request, 'orders/register.html', context={'type': 'danger', 'message': 'Please match the passwords first!', 'username': request.user.username})
    except:
        return render(request, 'orders/register.html', context={'type': 'danger', 'message': 'This username is already taken', 'username': request.user.username})
    user.last_name = last_name
    user.first_name = first_name
    user.save()
    i = authenticate(request, username=username, password=password)
    login(request, i)
    return render(request, 'orders/index.html', context={'type': 'success', 'message': 'Successfully Logged In', 'username': request.user.username})


def login_view(request):
    if request.POST.get('username') == None:
        return render(request, 'orders/login.html')
    username = request.POST['username']
    password = request.POST['password']
    i = authenticate(request, username=username, password=password)
    if i:
        login(request, i)
        return render(request, 'orders/index.html', context={'type': 'success', 'message': 'Successfully Logged In', 'username': request.user.username})
    else:
        return render(request, 'orders/login.html', context={'type': 'success', 'message': 'Invalid Credentials, please try again', 'username': request.user.username})


def shopping_list(request):
    if request.session.get('cart'):
        del request.session['cart']
    if not request.session.get('cart'):
        request.session['cart'] = {}
        t = Receipt(username=request.user.username)
        t.save()
        request.session['cart']['username'] = request.user.username
        request.session['cart']['id'] = t.id
        request.session['cart']['op'] = "Hashir"
        request.session['cart']['pizza'] = []
        request.session['cart']['subs'] = []
        request.session['cart']['salads'] = []
    context = {
        'pizzas': Pizza.objects.all(),
        'toppings': Toppings.objects.all(),
        'salads': SaladsPasta.objects.all(),
        'subs': SubsPlatters.objects.all(),
        'username': request.user.username
    }
    pizza_list = []
    if request.POST.get('main'):
        x = request.POST['main'].split(',')
        for i in x:
            try:
                pizza = Pizza.objects.get(pk=int(i))
                pizza_list.append(pizza.id)
            except ValueError:
                u = i.split('||')
                if u[0] == 'S':
                    t = FinalSubs(subs=SubsPlatters.objects.get(pk=int(u[1])), user=Receipt.objects.get(pk=request.session['cart']['id']))
                    t.save()
                    request.session['cart']['subs'].append(int(u[1]))
                if u[0] == 'P':
                    t = FinalSalads(salads=SaladsPasta.objects.get(pk=int(u[1])), user=Receipt.objects.get(pk=request.session['cart']['id']))
                    t.save()
                    request.session['cart']['salads'].append(int(u[1]))

        request.session['cart']['pizza'] = pizza_list
        print(request.session['cart']['pizza'])
        return HttpResponseRedirect('toppings')
    return render(request, 'orders/shop.html', context=context)


def toppings(request):
    print(request.session['cart'])
    pizzas = []
    for i in request.session['cart']['pizza']:
        pizzas.append(Pizza.objects.get(pk=i))
    context = {
        'toppings': Toppings.objects.all(),
        'pizzas': pizzas,
        'username': request.user.username
    }
    dic = {}
    if request.POST.get('main'):
        for i in pizzas:
            t = FinalPizza(pizza=i, user=Receipt.objects.get(pk=request.session['cart']['id']))
            t.save()
            dic[i.id] = t.id
        x = request.POST['main'].split(',')
        for i in x:
            y = i.split('||')
            z = FinalPizza.objects.get(pk=dic[int(y[0])])
            x = FinalToppings(topping=Toppings.objects.get(pk=int(y[1])), pizza=z)
            x.save()
        return HttpResponseRedirect('shop')
    return render(request, 'orders/toppings.html', context=context)