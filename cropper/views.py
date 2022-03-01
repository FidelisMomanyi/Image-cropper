from django.shortcuts import render, redirect
# from .models import Photo
# from .forms import PhotoForm
from django.shortcuts import render
from django.http import Http404
from .models import Location, Category, Image
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
