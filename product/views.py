import imghdr
# from socket import SO_VM_SOCKETS_BUFFER_MIN_SIZE
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from product.models import User, Product, ProductImg, Cart, CartItem, Store, FileUploded
from product.serializers import Userserializer, Productserializer, ProductImgserializer, Cartserializer, CartItemSerializer, FileUplodedserializer, Storeserializer
from rest_framework import generics, filters

import os


@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Userserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    return JsonResponse({}, status=400)

# @csrf_exempt
# def check_login(request):
#     if request.method == 'POST':


@csrf_exempt
def create_login(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            print(data)
            user = User.objects.filter(email=data['email'])
            return JsonResponse({'status': 200}, safe=False)
        except:
            return HttpResponse(status=404)

    if request.method == 'GET':
        # serializer = Userserializer(user, many=True)
        return JsonResponse({}, safe=False)


@csrf_exempt
def get_user(request, id):
    try:
        user = User.objects.get(pk=id)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Userserializer(user)
        return JsonResponse(serializer.data)


@csrf_exempt
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all().order_by('created_at').reverse()
        serializer = Productserializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Productserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def product_by_id(request, id):
    try:
        products = Product.objects.get(pk=id)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = Productserializer(request)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JsonResponse().parse(request)
        serializer = Productserializer(products, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        products.delete()
        return HttpResponse(status=201)


@csrf_exempt
def product_seller(request, storeId):
    try:
        product = Product.objects.get(storeId=storeId)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = Productserializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def productImg_list(request):
    if request.method == 'GET':
        productImg = ProductImg.objects.all()
        serializer = ProductImgserializer(productImg, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductImgserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def productImg_product_id(request, productId):
    try:
        productImg = ProductImg.objects.filter(productId=productId)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ProductImgserializer(productImg, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def productImg_by_id(request, id):
    try:
        productImg = ProductImg.objects.get(pk=id)

    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ProductImgserializer(productImg)
        return JsonResponse(serializer.data)
    elif request.method == 'DELETE':
        productImg.delete()
        return HttpResponse(status=201)


@csrf_exempt
def productImg_by_category(request, category):
    try:
        product = Product.objects.filter(category=category)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = Productserializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def cart_list(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Cartserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def cart_by_user(request, UserId):
    try:
        cart = Cart.objects.get(UserId=UserId)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = Cartserializer(cart, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        data = JsonResponse().parse(request)
        serializer = Cartserializer(cart, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        cart.delete()
        return HttpResponse(status=201)


@csrf_exempt
def cart_item_list(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CartItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def cartItem_by_id(request, pk):
    try:
        catrItem = CartItem.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CartItemSerializer(catrItem)
        if serializer.is_valid():
            serializer.save()
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CartItemSerializer(catrItem, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        catrItem.delete()
        return HttpResponse(status=201)


@csrf_exempt
def cartItem_by_cart_id(request, cartId):
    try:
        cartItem = CartItem.objects.filter(cartId=cartId)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CartItemSerializer(cartItem, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def cartItem_detect_same_product(request, cartId, productId):
    try:
        cartItem = CartItem.objects.filter(
            cartId=cartId).filter(productId=productId)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = CartItemSerializer(cartItem, many=True)
        return JsonResponse(serializer.data, safe=False)


class search_product(generics.ListAPIView):
    search_fields = ('title', 'category', 'discription')
    filter_backends = (filters.SearchFilter)
    queryset = Product.objects.all()
    serializer_class = ProductImgserializer


@csrf_exempt
def cart_store(request):
    if request.method == 'POST':
        print('kksjksjdks')
        data = JSONParser().parse(request)
        serializer = Storeserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def get_store(request, userId):
    try:
        store = Store.objects.filter(userId=userId)

    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = Storeserializer(store, many=True)
        return JsonResponse(serializer.data, safe=False)
    return JsonResponse({}, safe=False)


class uplode_file(generics.CreateAPIView):
    queryset = FileUploded.objects.all()
    serializer = FileUplodedserializer


@csrf_exempt
def delete_file(request, filename):
    if request.method == 'GET':
        ext = filename.split('.')[-1]
        filenameExt = filename.replace(f'{ext}', "")
        fileDir = "%s/%s.%s"("img", filenameExt.now(), ext)
        if os.path.isfile(f"img/{filename}"):
            os.remove(fileDir)
            return HttpResponse(f"{filename} deleted")
        return HttpResponse("file not found")


def filter_price(request, minprice, maxprice):
    try:
        product = Product.objects.filter(price__range=(minprice, maxprice))
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = Productserializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)


def filter_min_price(request, minprice):
    try:
        product = Product.objects.filter(price__get=minprice)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = Productserializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)


def filter_min_price(request, maxprice):
    try:
        product = Product.objects.filter(price__lte=maxprice)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = Productserializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)


def filter_rating(request, rating):
    try:
        product = Product.objects.filter(rating__get=rating)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = Productserializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)


def filter_condition(request, condition):
    try:
        product = Product.objects.filter(condition=condition)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = Productserializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)


def filter_price_and_rating(request, minprice, maxprice, rating):
    try:
        product = Product.objects.filter(price__range=(
            minprice, maxprice)).filter(rating_get=rating)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = Productserializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)


def filter_price_and_condition(request, minprice, maxprice, condition):
    try:
        product = Product.objects.filter(price__range=(
            minprice, maxprice)).filter(condition=condition)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = Productserializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)


def filter_rating_and_condition(request, rating, condition):
    try:
        product = Product.objects.filter(
            rating=rating).filter(condition=condition)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = Productserializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)


def filter_all(request, minprice, maxprice, rating, condition):
    try:
        product = Product.objects.filter(
            rating=rating).filter(condition=condition).filter(price__range=(minprice, maxprice))
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = Productserializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def get_cart_item_by_cart_id(request, cartId):
    try:
        cartItem = CartItem.objects.filter(cartId=cartId).prefetch_related(
            "productId").order_by('created_at')
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = CartItemSerializer(cartItem, many=True)
        return JsonResponse(serializer.data, safe=False)
