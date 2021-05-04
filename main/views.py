from django.shortcuts import render
from django.http import HttpResponse
from .forms import GeneratorOptions
import random
import string


# Create your views here.

def index(response):    
    return render(response, 'main/home.html')



def generator(response):    
    if response.method == "POST":
        form = GeneratorOptions(response.POST)
        if form.is_valid():
            password_length                = form.cleaned_data["Length"]
            must_contain_upper_case        = form.cleaned_data["ContainsUpper"]
            must_contain_number            = form.cleaned_data["ContainsNumber"]
            must_contain_special_character = form.cleaned_data["ContainsSpecial"]

            password = []
            chars = []
            if must_contain_upper_case == True:
                password += random.choice(string.ascii_lowercase)
                password += random.choice(string.ascii_uppercase)
                password_length -= 2
                chars += string.ascii_letters
            else:
                chars += string.ascii_lowercase
            if must_contain_number == True:
                password += random.choice(string.digits)
                password_length -= 1
                chars += string.digits
            if must_contain_special_character == True:    
                password += random.choice('#@')
                password_length -= 1
                chars += '#@'
            for _ in range(int(password_length)):
                password += random.choice(chars)
            random.shuffle(password)

            return render(response, 'main/generator.html', {"form":form, "pw":''.join(password)})
    else:
        pass
    form = GeneratorOptions()
    return render(response, 'main/generator.html', {"form":form})


