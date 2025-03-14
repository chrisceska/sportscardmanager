from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Card
from .forms import CardForm

@login_required
def card_list(request):
    cards = Card.objects.filter(owner=request.user)
    return render(request, 'cards/card_list.html', {'cards': cards})

@login_required
def card_detail(request, pk):
    card = Card.objects.get(pk=pk, owner=request.user)
    return render(request, 'cards/card_detail.html', {'card': card})

@login_required
def card_create(request):
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            card = form.save(commit=False)
            card.owner = request.user
            card.save()
            return redirect('card_detail', pk=card.pk)
    else:
        form = CardForm()
    return render(request, 'cards/card_form.html', {'form': form})

@login_required
def card_edit(request, pk):
    card = Card.objects.get(pk=pk, owner=request.user)
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES, instance=card)
        if form.is_valid():
            form.save()
            return redirect('card_detail', pk=card.pk)
    else:
        form = CardForm(instance=card)
    return render(request, 'cards/card_form.html', {'form': form})

@login_required
def card_delete(request, pk):
    card = Card.objects.get(pk=pk, owner=request.user)
    if request.method == 'POST':
        card.delete()
        return redirect('card_list')
    return render(request, 'cards/card_confirm_delete.html', {'card': card})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('card_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('card_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
