from django.shortcuts import render,  HttpResponse, redirect
from .models import Video_Post, Picture_slide, Product_details, Order_info, Newsletter, Stay_Updated_subscribtion, Product_Brand, Category, contact_table
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password


def index(request):
    user_visit = request.session.get('user_visit')
    if user_visit:
        k = ''
    else:
        k = 'New lok'
        request.session['user_visit'] = 'a visitor'


    kop = Picture_slide.objects.first()
    kjo = kop.id
    # ko = Picture_slide.objects.all()
    all_prod = Product_details.objects.all().order_by('-id')
    all_prod_8 = Product_details.objects.all().order_by('-id')[:8]
    # all_brand = Cosmetics_brand_image.objects.all()[:3]
    all_brand = Product_Brand.objects.all()

    all_You_May_Also_Like = Product_details.objects.filter(Product_show_type = 'You May Also Like').order_by('-id')
    all_Trandy_Products = Product_details.objects.filter(Product_show_type = 'Trandy Products').order_by('-id')[:8]
    all_Just_Arrived = Product_details.objects.filter(Product_show_type=None).order_by('-id')[:8]


    ko = Picture_slide.objects.all().exclude(id=kjo)
    
    category_all = Category.objects.all()
    contex  ={
        'kop':kop,
        'ko':ko,
        'all_prod':all_prod,
        'all_brand':all_brand,
        'all_You_May_Also_Like':all_You_May_Also_Like,
        'all_Trandy_Products':all_Trandy_Products,
        'all_Just_Arrived':all_Just_Arrived,
        'all_prod_8':all_prod_8,
        'k':k,
        'category_all':category_all,
    }
    return render(request, 'index.html', contex)


def Live_Video(request):
    foooo = Video_Post.objects.last()
    fwe = foooo.id
    f = Video_Post.objects.all().order_by("-id").exclude(id=fwe)
    fo = Video_Post.objects.all().last()

    print('foooo')
    print(foooo)
    contex = {
        'f':f,
        'fo':fo,
    }
    return render(request, 'Live_Video.html', contex)

def checkout(request):
    if request.user.is_authenticated:
        return render(request, 'checkout.html')
    else:
        messages.success(request, "For Checkout you have to login first !")
        return redirect('login_func')




def login_func(request):
    return render(request, 'login.html')


def reg(request):
    return render(request, 'reg.html')



def regis(request):
    sign_username = request.POST.get('Reg_email')
    sign_email = request.POST.get('Reg_email')
    sign_password = request.POST.get('Reg_Password')
    confirm_sign_password = request.POST.get('Reg_Confirm_password')
    sign_first_name = request.POST.get('Reg_first_Name')
    sign_last_name = request.POST.get('Reg_last_Name')

    # chech the error inputs

    user_username_info = User.objects.filter(username=sign_username)
    user_email_info = User.objects.filter(email=sign_email)

    erorr_message = ""

    if user_username_info:
        # messages.error(request, "Username Already Exist")
        erorr_message = "Username Already Exist"

    elif user_email_info:
        # messages.error(request, "Email Already Exist")
        erorr_message = "Email Already Exist"

    elif sign_password != confirm_sign_password:
        # messages.error(request, "Passwords are not match")
        erorr_message = "Passwords are not match"

    elif len(sign_password) < 7:
        # messages.error(request, "Passwords Must be Al least 7 Digits")
        erorr_message = "Passwords Must be At least 7 Digits"

    if not erorr_message:
        # create user
        myuser = User.objects.create_user(sign_username, sign_email, sign_password)
        myuser.first_name = sign_first_name
        myuser.last_name = sign_last_name
        myuser.is_active = True
        myuser.save()

        login(request, myuser)

        messages.success(request, f'You Are Login as a {myuser.first_name} {myuser.last_name} !!!')
        return redirect('index')

    context = {'sign_username': sign_username, 'sign_email': sign_email, 'sign_first_name': sign_first_name,
                         'sign_last_name': sign_last_name, 'erorr_message':erorr_message}
    return render(request, 'reg.html', context)

def Log_in(request):
    login_Email = request.POST.get('login_Email')
    login_pass = request.POST.get('login_pass')

    user = authenticate(username=login_Email, password=login_pass)
    erorr_message_2 = ""

    if user is not None:
        login(request, user)
        # messages.success(request, "Successfully Logged In !!")
        return redirect('index')
    else:
        erorr_message_2 = "Invalid Credentials, Please Try Again !!"

        value_func2 = {'erorr_message_2': erorr_message_2, 'login_Email': login_Email}
        return render(request, 'login.html', value_func2)





@csrf_exempt
def Log_out(request):
    request.session.clear()
    return redirect('index')


@csrf_exempt
def cheak_email_from_def(request):
    k = request.POST.get('k')
    print('kk')
    print(k)
    email_here = User.objects.filter(username=k)
    print('email_here')
    print(email_here)
    if email_here:
        return HttpResponse('exist')
    else:
        return HttpResponse('Not exist')







@csrf_exempt
def details(request, pk):
    one_prod = Product_details.objects.get(id=pk)
    # e = one_prod.Product_SUB_category
    # if e:
    #     all_You_May_Also_Like = Product_details.objects.filter(Product_SUB_category=e).order_by('-id')
    # else:


    all_You_May_Also_Like = Product_details.objects.filter(Product_show_type = 'You May Also Like').order_by('-id')
    contex = {
        'one_prod':one_prod,
        'all_You_May_Also_Like':all_You_May_Also_Like,

    }
    return render(request, 'details.html', contex)


@csrf_exempt
def Previous_order(request):
    user_id = request.user
    if user_id:
        user_get = request.user
        all_order = Order_info.objects.filter(User_Connect_with_order=user_get)
        all_order_last = Order_info.objects.filter(User_Connect_with_order=user_get).last()
        contex = {
            'all_order':all_order,
            'all_order_last':all_order_last,

        }
        return render(request, 'Previous_order.html', contex)
    else:
        return redirect('index')

@csrf_exempt
def order_No_show(request, pk):
    user_id = request.user
    if user_id:
        user_get = request.user
        all_order = Order_info.objects.filter(User_Connect_with_order=user_get)
        all_order_last = Order_info.objects.get(id=pk)
        contex = {
            'all_order':all_order,
            'all_order_last':all_order_last,

        }
        return render(request, 'Previous_order.html', contex)
    else:
        return redirect('index')

@csrf_exempt
def Change_Password(request):
    if request.user.is_authenticated:
        return render(request, 'Change_Password.html')
    else:
        return redirect('index')

@csrf_exempt
def save_change_pass(request):
    if request.user.is_authenticated:
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')

        user = request.user

        check_my_old_password = check_password(old_password, user.password)

        print(check_my_old_password)

        if check_my_old_password:
            user.password = make_password(new_password)
            user.save()
            login(request, user)
            messages.success(request, "Password Successfully Updated !")
        else:
            messages.success(request, "Old Password is incorrect !")
        return redirect('Change_Password')
    else:
        return redirect('index')


@csrf_exempt
def save_order(request):
    Name_get_n = request.POST.get('Name_get_n')
    Mobile_get_n = request.POST.get('Mobile_get_n')
    Address_get_n = request.POST.get('Address_get_n')
    City_get_n = request.POST.get('City_get_n')
    ZIP_get_n = request.POST.get('ZIP_get_n')

    user = request.user

    total_money = request.POST.get('total_money')
    Sub_money = request.POST.get('Sub_money')
    ship_money = request.POST.get('ship_money')

    upoo = Order_info(User_Connect_with_order=user, order_User_Name=Name_get_n, order_User_Mobile=Mobile_get_n, order_User_Address=Address_get_n, order_User_City=City_get_n, order_User_ZIP=ZIP_get_n, order_User_shipping_charge=ship_money, order_User_Sub_total=Sub_money, order_User_total=total_money)

    upoo.save()
    id_of_it = upoo.id
    upo = Order_info.objects.get(id=id_of_it)

    upo.order_No = 30000 + upo.id



    qun_1 = request.POST.get('qun_1')
    qun_2 = request.POST.get('qun_2')
    qun_3 = request.POST.get('qun_3')
    qun_4 = request.POST.get('qun_4')
    qun_5 = request.POST.get('qun_5')
    qun_6 = request.POST.get('qun_6')
    qun_7 = request.POST.get('qun_7')
    qun_8 = request.POST.get('qun_8')
    qun_9 = request.POST.get('qun_9')
    qun_10 = request.POST.get('qun_10')
    qun_11 = request.POST.get('qun_11')
    qun_12 = request.POST.get('qun_12')
    qun_13 = request.POST.get('qun_13')
    qun_14 = request.POST.get('qun_14')
    qun_15 = request.POST.get('qun_15')
    qun_16 = request.POST.get('qun_16')
    qun_17 = request.POST.get('qun_17')
    qun_18 = request.POST.get('qun_18')
    qun_19 = request.POST.get('qun_19')
    qun_20 = request.POST.get('qun_20')
    qun_21 = request.POST.get('qun_21')
    qun_22 = request.POST.get('qun_22')
    qun_23 = request.POST.get('qun_23')
    qun_24 = request.POST.get('qun_24')
    qun_25 = request.POST.get('qun_25')
    qun_26 = request.POST.get('qun_26')
    qun_27 = request.POST.get('qun_27')
    qun_28 = request.POST.get('qun_28')
    qun_29 = request.POST.get('qun_29')
    qun_30 = request.POST.get('qun_30')





    name_1 = request.POST.get('name_1')
    name_2 = request.POST.get('name_2')
    name_3 = request.POST.get('name_3')
    name_4 = request.POST.get('name_4')
    name_5 = request.POST.get('name_5')
    name_6 = request.POST.get('name_6')
    name_7 = request.POST.get('name_7')
    name_8 = request.POST.get('name_8')
    name_9 = request.POST.get('name_9')
    name_10 = request.POST.get('name_10')
    name_11 = request.POST.get('name_11')
    name_12 = request.POST.get('name_12')
    name_13 = request.POST.get('name_13')
    name_14 = request.POST.get('name_14')
    name_15 = request.POST.get('name_15')
    name_16 = request.POST.get('name_16')
    name_17 = request.POST.get('name_17')
    name_18 = request.POST.get('name_18')
    name_19 = request.POST.get('name_19')
    name_20 = request.POST.get('name_20')
    name_21 = request.POST.get('name_21')
    name_22 = request.POST.get('name_22')
    name_23 = request.POST.get('name_23')
    name_24 = request.POST.get('name_24')
    name_25 = request.POST.get('name_25')
    name_26 = request.POST.get('name_26')
    name_27 = request.POST.get('name_27')
    name_28 = request.POST.get('name_28')
    name_29 = request.POST.get('name_29')
    name_30 = request.POST.get('name_30')

    price_1 = request.POST.get('price_1')
    price_2 = request.POST.get('price_2')
    price_3 = request.POST.get('price_3')
    price_4 = request.POST.get('price_4')
    price_5 = request.POST.get('price_5')
    price_6 = request.POST.get('price_6')
    price_7 = request.POST.get('price_7')
    price_8 = request.POST.get('price_8')
    price_9 = request.POST.get('price_9')
    price_10 = request.POST.get('price_10')
    price_11 = request.POST.get('price_11')
    price_12 = request.POST.get('price_12')
    price_13 = request.POST.get('price_13')
    price_14 = request.POST.get('price_14')
    price_15 = request.POST.get('price_15')
    price_16 = request.POST.get('price_16')
    price_17 = request.POST.get('price_17')
    price_18 = request.POST.get('price_18')
    price_19 = request.POST.get('price_19')
    price_20 = request.POST.get('price_20')
    price_21 = request.POST.get('price_21')
    price_22 = request.POST.get('price_22')
    price_23 = request.POST.get('price_23')
    price_24 = request.POST.get('price_24')
    price_25 = request.POST.get('price_25')
    price_26 = request.POST.get('price_26')
    price_27 = request.POST.get('price_27')
    price_28 = request.POST.get('price_28')
    price_29 = request.POST.get('price_29')
    price_30 = request.POST.get('price_30')

    image_1 = request.POST.get('image_1')
    image_2 = request.POST.get('image_2')
    image_3 = request.POST.get('image_3')
    image_4 = request.POST.get('image_4')
    image_5 = request.POST.get('image_5')
    image_6 = request.POST.get('image_6')
    image_7 = request.POST.get('image_7')
    image_8 = request.POST.get('image_8')
    image_9 = request.POST.get('image_9')
    image_10 = request.POST.get('image_10')
    image_11 = request.POST.get('image_11')
    image_12 = request.POST.get('image_12')
    image_13 = request.POST.get('image_13')
    image_14 = request.POST.get('image_14')
    image_15 = request.POST.get('image_15')
    image_16 = request.POST.get('image_16')
    image_17 = request.POST.get('image_17')
    image_18 = request.POST.get('image_18')
    image_19 = request.POST.get('image_19')
    image_20 = request.POST.get('image_20')
    image_21 = request.POST.get('image_21')
    image_22 = request.POST.get('image_22')
    image_23 = request.POST.get('image_23')
    image_24 = request.POST.get('image_24')
    image_25 = request.POST.get('image_25')
    image_26 = request.POST.get('image_26')
    image_27 = request.POST.get('image_27')
    image_28 = request.POST.get('image_28')
    image_29 = request.POST.get('image_29')
    image_30 = request.POST.get('image_30')

    id_1 = request.POST.get('id_1')
    id_2 = request.POST.get('id_2')
    id_3 = request.POST.get('id_3')
    id_4 = request.POST.get('id_4')
    id_5 = request.POST.get('id_5')
    id_6 = request.POST.get('id_6')
    id_7 = request.POST.get('id_7')
    id_8 = request.POST.get('id_8')
    id_9 = request.POST.get('id_9')
    id_10 = request.POST.get('id_10')
    id_11 = request.POST.get('id_11')
    id_12 = request.POST.get('id_12')
    id_13 = request.POST.get('id_13')
    id_14 = request.POST.get('id_14')
    id_15 = request.POST.get('id_15')
    id_16 = request.POST.get('id_16')
    id_17 = request.POST.get('id_17')
    id_18 = request.POST.get('id_18')
    id_19 = request.POST.get('id_19')
    id_20 = request.POST.get('id_20')
    id_21 = request.POST.get('id_21')
    id_22 = request.POST.get('id_22')
    id_23 = request.POST.get('id_23')
    id_24 = request.POST.get('id_24')
    id_25 = request.POST.get('id_25')
    id_26 = request.POST.get('id_26')
    id_27 = request.POST.get('id_27')
    id_28 = request.POST.get('id_28')
    id_29 = request.POST.get('id_29')
    id_30 = request.POST.get('id_30')

    color_1 = request.POST.get('color_1')
    color_2 = request.POST.get('color_2')
    color_3 = request.POST.get('color_3')
    color_4 = request.POST.get('color_4')
    color_5 = request.POST.get('color_5')
    color_6 = request.POST.get('color_6')
    color_7 = request.POST.get('color_7')
    color_8 = request.POST.get('color_8')
    color_9 = request.POST.get('color_9')
    color_10 = request.POST.get('color_10')
    color_11 = request.POST.get('color_11')
    color_12 = request.POST.get('color_12')
    color_13 = request.POST.get('color_13')
    color_14 = request.POST.get('color_14')
    color_15 = request.POST.get('color_15')
    color_16 = request.POST.get('color_16')
    color_17 = request.POST.get('color_17')
    color_18 = request.POST.get('color_18')
    color_19 = request.POST.get('color_19')
    color_20 = request.POST.get('color_20')
    color_21 = request.POST.get('color_21')
    color_22 = request.POST.get('color_22')
    color_23 = request.POST.get('color_23')
    color_24 = request.POST.get('color_24')
    color_25 = request.POST.get('color_25')
    color_26 = request.POST.get('color_26')
    color_27 = request.POST.get('color_27')
    color_28 = request.POST.get('color_28')
    color_29 = request.POST.get('color_29')
    color_30 = request.POST.get('color_30')

    if qun_1:
        upo.product_1_quantity=qun_1
        upo.Name_of_product_1=name_1
        upo.product_1_Price = price_1
        upo.product_1_image_link = image_1
        upo.product_1_color = color_1

        product = Product_details.objects.get(id=id_1)

        upo.product_1_brand = product.Product_brand.Product_Brand_name
        upo.product_1_size = product.Product_Size_Get



    if qun_2:
        upo.product_2_quantity=qun_2
        upo.Name_of_product_2 = name_2

        upo.product_2_Price = price_2
        upo.product_2_image_link = image_2
        upo.product_2_color = color_2

        product = Product_details.objects.get(id=id_2)

        upo.product_2_brand = product.Product_brand.Product_Brand_name
        upo.product_2_size = product.Product_Size_Get

    if qun_3:
        upo.product_3_quantity=qun_3
        upo.Name_of_product_3 = name_3

        upo.product_3_Price = price_3
        upo.product_3_image_link = image_3
        upo.product_3_color = color_3

        product = Product_details.objects.get(id=id_3)

        upo.product_3_brand = product.Product_brand.Product_Brand_name
        upo.product_3_size = product.Product_Size_Get

    if qun_4:
        upo.product_4_quantity=qun_4
        upo.Name_of_product_4 = name_4
        upo.product_4_Price = price_4
        upo.product_4_image_link = image_4
        upo.product_4_color = color_4

        product = Product_details.objects.get(id=id_4)

        upo.product_4_brand = product.Product_brand.Product_Brand_name
        upo.product_4_size = product.Product_Size_Get

    if qun_5:
        upo.product_5_quantity=qun_5
        upo.Name_of_product_5 = name_5
        upo.product_5_Price = price_5
        upo.product_5_image_link = image_5
        upo.product_5_color = color_5

        product = Product_details.objects.get(id=id_5)

        upo.product_5_brand = product.Product_brand.Product_Brand_name
        upo.product_5_size = product.Product_Size_Get

    if qun_6:
        upo.product_6_quantity=qun_6
        upo.Name_of_product_6 = name_6
        upo.product_6_Price = price_6
        upo.product_6_image_link = image_6
        upo.product_6_color = color_6

        product = Product_details.objects.get(id=id_6)

        upo.product_6_brand = product.Product_brand.Product_Brand_name
        upo.product_6_size = product.Product_Size_Get

    if qun_7:
        upo.product_7_quantity=qun_7
        upo.Name_of_product_7 = name_7
        upo.product_7_Price = price_7
        upo.product_7_image_link = image_7
        upo.product_7_color = color_7

        product = Product_details.objects.get(id=id_7)

        upo.product_7_brand = product.Product_brand.Product_Brand_name
        upo.product_7_size = product.Product_Size_Get

    if qun_8:
        upo.product_8_quantity=qun_8
        upo.Name_of_product_8 = name_8
        upo.product_8_Price = price_8
        upo.product_8_image_link = image_8
        upo.product_8_color = color_8

        product = Product_details.objects.get(id=id_8)

        upo.product_8_brand = product.Product_brand.Product_Brand_name
        upo.product_8_size = product.Product_Size_Get

    if qun_9:
        upo.product_9_quantity=qun_9
        upo.Name_of_product_9 = name_9
        upo.product_9_Price = price_9
        upo.product_9_image_link = image_9
        upo.product_9_color = color_9

        product = Product_details.objects.get(id=id_9)

        upo.product_9_brand = product.Product_brand.Product_Brand_name
        upo.product_9_size = product.Product_Size_Get

    if qun_10:
        upo.product_10_quantity=qun_10
        upo.Name_of_product_10 = name_10
        upo.product_10_Price = price_10
        upo.product_10_image_link = image_10
        upo.product_10_color = color_10

        product = Product_details.objects.get(id=id_10)

        upo.product_10_brand = product.Product_brand.Product_Brand_name
        upo.product_10_size = product.Product_Size_Get

    if qun_11:
        upo.product_11_quantity=qun_11
        upo.Name_of_product_11 = name_11
        upo.product_11_Price = price_11
        upo.product_11_image_link = image_11
        upo.product_11_color = color_11

        product = Product_details.objects.get(id=id_11)

        upo.product_11_brand = product.Product_brand.Product_Brand_name
        upo.product_11_size = product.Product_Size_Get

    if qun_12:
        upo.product_12_quantity=qun_12
        upo.Name_of_product_12 = name_12
        upo.product_12_Price = price_12
        upo.product_12_image_link = image_12
        upo.product_12_color = color_12

        product = Product_details.objects.get(id=id_12)

        upo.product_12_brand = product.Product_brand.Product_Brand_name
        upo.product_12_size = product.Product_Size_Get

    if qun_13:
        upo.product_13_quantity=qun_13
        upo.Name_of_product_13 = name_13
        upo.product_13_Price = price_13
        upo.product_13_image_link = image_13
        upo.product_13_color = color_13

        product = Product_details.objects.get(id=id_13)

        upo.product_13_brand = product.Product_brand.Product_Brand_name
        upo.product_13_size = product.Product_Size_Get

    if qun_14:
        upo.product_14_quantity=qun_14
        upo.Name_of_product_14 = name_14
        upo.product_14_Price = price_14
        upo.product_14_image_link = image_14
        upo.product_14_color = color_14

        product = Product_details.objects.get(id=id_14)

        upo.product_14_brand = product.Product_brand.Product_Brand_name
        upo.product_14_size = product.Product_Size_Get

    if qun_15:
        upo.product_15_quantity=qun_15
        upo.Name_of_product_15 = name_15
        upo.product_15_Price = price_15
        upo.product_15_image_link = image_15
        upo.product_15_color = color_15

        product = Product_details.objects.get(id=id_15)

        upo.product_15_brand = product.Product_brand.Product_Brand_name
        upo.product_15_size = product.Product_Size_Get

    if qun_16:
        upo.product_16_quantity=qun_16
        upo.Name_of_product_16 = name_16
        upo.product_16_Price = price_16
        upo.product_16_image_link = image_16
        upo.product_16_color = color_16

        product = Product_details.objects.get(id=id_16)

        upo.product_16_brand = product.Product_brand.Product_Brand_name
        upo.product_16_size = product.Product_Size_Get

    if qun_17:
        upo.product_17_quantity=qun_17
        upo.Name_of_product_17 = name_17
        upo.product_17_Price = price_17
        upo.product_17_image_link = image_17
        upo.product_17_color = color_17

        product = Product_details.objects.get(id=id_17)

        upo.product_17_brand = product.Product_brand.Product_Brand_name
        upo.product_17_size = product.Product_Size_Get

    if qun_18:
        upo.product_18_quantity=qun_18
        upo.Name_of_product_18 = name_18
        upo.product_18_Price = price_18
        upo.product_18_image_link = image_18
        upo.product_18_color = color_18

        product = Product_details.objects.get(id=id_18)

        upo.product_18_brand = product.Product_brand.Product_Brand_name
        upo.product_18_size = product.Product_Size_Get

    if qun_19:
        upo.product_19_quantity=qun_19
        upo.Name_of_product_19 = name_19
        upo.product_19_Price = price_19
        upo.product_19_image_link = image_19
        upo.product_19_color = color_19

        product = Product_details.objects.get(id=id_19)

        upo.product_19_brand = product.Product_brand.Product_Brand_name
        upo.product_19_size = product.Product_Size_Get

    if qun_20:
        upo.product_20_quantity=qun_20
        upo.Name_of_product_20 = name_20
        upo.product_20_Price = price_20
        upo.product_20_image_link = image_20
        upo.product_20_color = color_20

        product = Product_details.objects.get(id=id_20)

        upo.product_20_brand = product.Product_brand.Product_Brand_name
        upo.product_20_size = product.Product_Size_Get

    if qun_21:
        upo.product_21_quantity=qun_21
        upo.Name_of_product_21 = name_21
        upo.product_21_Price = price_21
        upo.product_21_image_link = image_21
        upo.product_21_color = color_21

        product = Product_details.objects.get(id=id_21)

        upo.product_21_brand = product.Product_brand.Product_Brand_name
        upo.product_21_size = product.Product_Size_Get

    if qun_22:
        upo.product_22_quantity=qun_22
        upo.Name_of_product_22 = name_22
        upo.product_22_Price = price_22
        upo.product_22_image_link = image_22
        upo.product_22_color = color_22

        product = Product_details.objects.get(id=id_22)

        upo.product_22_brand = product.Product_brand.Product_Brand_name
        upo.product_22_size = product.Product_Size_Get

    if qun_23:
        upo.product_23_quantity=qun_23
        upo.Name_of_product_23 = name_23
        upo.product_23_Price = price_23
        upo.product_23_image_link = image_23
        upo.product_23_color = color_23

        product = Product_details.objects.get(id=id_23)

        upo.product_23_brand = product.Product_brand.Product_Brand_name
        upo.product_23_size = product.Product_Size_Get

    if qun_24:
        upo.product_24_quantity=qun_24
        upo.Name_of_product_24 = name_24
        upo.product_24_Price = price_24
        upo.product_24_image_link = image_24
        upo.product_24_color = color_24

        product = Product_details.objects.get(id=id_24)

        upo.product_24_brand = product.Product_brand.Product_Brand_name
        upo.product_24_size = product.Product_Size_Get

    if qun_25:
        upo.product_25_quantity=qun_25
        upo.Name_of_product_25 = name_25
        upo.product_25_Price = price_25
        upo.product_25_image_link = image_25
        upo.product_25_color = color_25

        product = Product_details.objects.get(id=id_25)

        upo.product_25_brand = product.Product_brand.Product_Brand_name
        upo.product_25_size = product.Product_Size_Get

    if qun_26:
        upo.product_26_quantity=qun_26
        upo.Name_of_product_26 = name_26
        upo.product_26_Price = price_26
        upo.product_26_image_link = image_26
        upo.product_26_color = color_26

        product = Product_details.objects.get(id=id_26)

        upo.product_26_brand = product.Product_brand.Product_Brand_name
        upo.product_26_size = product.Product_Size_Get

    if qun_27:
        upo.product_27_quantity=qun_27
        upo.Name_of_product_27 = name_27
        upo.product_27_Price = price_27
        upo.product_27_image_link = image_27
        upo.product_27_color = color_27

        product = Product_details.objects.get(id=id_27)

        upo.product_27_brand = product.Product_brand.Product_Brand_name
        upo.product_27_size = product.Product_Size_Get

    if qun_28:
        upo.product_28_quantity=qun_28
        upo.Name_of_product_28 = name_28
        upo.product_28_Price = price_28
        upo.product_28_image_link = image_28
        upo.product_28_color = color_28

        product = Product_details.objects.get(id=id_28)

        upo.product_28_brand = product.Product_brand.Product_Brand_name
        upo.product_28_size = product.Product_Size_Get

    if qun_29:
        upo.product_29_quantity=qun_29
        upo.Name_of_product_29 = name_29
        upo.product_29_Price = price_29
        upo.product_29_image_link = image_29
        upo.product_29_color = color_29

        product = Product_details.objects.get(id=id_29)

        upo.product_29_brand = product.Product_brand.Product_Brand_name
        upo.product_29_size = product.Product_Size_Get

    if qun_30:
        upo.product_30_quantity=qun_30
        upo.Name_of_product_30 = name_30
        upo.product_30_Price = price_30
        upo.product_30_image_link = image_30
        upo.product_30_color = color_30

        product = Product_details.objects.get(id=id_30)

        upo.product_30_brand = product.Product_brand.Product_Brand_name
        upo.product_30_size = product.Product_Size_Get

    upo.save()
    return redirect('index')





@csrf_exempt
def Newsletter_get(request):
    Subscrib_nane = request.POST.get('Subscrib_nane')
    Subscrib_moble_number = request.POST.get('Subscrib_moble_number')

    k = Newsletter.objects.filter(Newsletter_mobile_number=Subscrib_moble_number)
    if k or Subscrib_moble_number == '':
        pass
    else:
        Newsletter_get = Newsletter(Newsletter_name=Subscrib_nane, Newsletter_mobile_number=Subscrib_moble_number)
        Newsletter_get.save()
    return redirect('index')



@csrf_exempt
def Stay_Updated_get(request):
    Stay_Updated_mobile = request.POST.get('Stay_Updated_mobile')
    k = Stay_Updated_subscribtion.objects.filter(Stay_Updated_mobile_number=Stay_Updated_mobile)
    if k or Stay_Updated_mobile == '':
        pass
    else:
        Newsletter_get = Stay_Updated_subscribtion(Stay_Updated_mobile_number=Stay_Updated_mobile)
        Newsletter_get.save()
    return redirect('index')





@csrf_exempt
def search_button_def(request):
    popo = request.POST.get('popo')


    # product_here = Product_details.objects.filter(Product_Title__iexact = popo)
    if popo !='':
        product_here = Product_details.objects.filter(Product_Title__icontains = popo)[:6]
    else:
        product_here=''

    query_search_product = serializers.serialize('json', product_here)
    return JsonResponse(query_search_product, safe=False)









@csrf_exempt
def Trandy_Products_See_More(request):
    range_1 = request.GET.get('range_1')
    range_2 = request.GET.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_show_type='Trandy Products', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_show_type='Trandy Products').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Trandy_Products_See_More.html', contex)




@csrf_exempt
def Shop_Now(request):
    range_1 = request.GET.get('range_1')
    range_2 = request.GET.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Product_Discount_Prize__range=[range_1, range_2]).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.all().order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Shop_Now.html', contex)



@csrf_exempt
def You_May_Also_Like(request):
    range_1 = request.GET.get('range_1')
    range_2 = request.GET.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_show_type='You May Also Like', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_show_type='You May Also Like').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'You_May_Also_Like.html', contex)




@csrf_exempt
def brand_product(request):
    brandId = request.GET.get('brandId')
    get_brand = Product_Brand.objects.get(id=brandId)


    range_1 = request.GET.get('range_1')
    range_2 = request.GET.get('range_2')

    if range_1 and range_2:
        result_product_here = Product_details.objects.filter(Q(Product_brand=get_brand, Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        result_product_here = Product_details.objects.filter(Product_brand=get_brand).order_by('-id')


    print('result_product_here')
    print(result_product_here)

    p = Paginator(result_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
        'brandId': brandId,
    }

    return render(request, 'brand_product.html', contex)



@csrf_exempt
def Face_Care(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_SUB_category='Face Care', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_SUB_category='Face Care').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Face_Care.html', contex)



@csrf_exempt
def Body_Care(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_SUB_category='Body Care', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_SUB_category='Body Care').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Body_Care.html', contex)



@csrf_exempt
def Soothing_Gel(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_SUB_category='Soothing Gel', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_SUB_category='Soothing Gel').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Soothing_Gel.html', contex)


@csrf_exempt
def Serum(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_SUB_category='Serum', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_SUB_category='Serum').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Serum.html', contex)


@csrf_exempt
def Night_Cream_And_Day_Cream(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_SUB_category='Night Cream And Day Cream', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_SUB_category='Night Cream And Day Cream').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Night_Cream_And_Day_Cream.html', contex)


@csrf_exempt
def Sunscreen(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_SUB_category='Sunscreen', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_SUB_category='Sunscreen').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Sunscreen.html', contex)




@csrf_exempt
def Face_Pack(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_SUB_category='Face Pack', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_SUB_category='Face Pack').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Face_Pack.html', contex)



@csrf_exempt
def Massage_Cream(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_SUB_category='Massage Cream', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_SUB_category='Massage Cream').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Massage_Cream.html', contex)



@csrf_exempt
def Scrub(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_SUB_category='Scrub', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_SUB_category='Scrub').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Scrub.html', contex)





@csrf_exempt
def Face_Wsah(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_SUB_category='Face Wsah', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_SUB_category='Face Wsah').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Face_Wsah.html', contex)



@csrf_exempt
def Bath_Salt(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_SUB_category='Bath Salt', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_SUB_category='Bath Salt').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Bath_Salt.html', contex)



@csrf_exempt
def Hear_Remover(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_SUB_category='Hear Remover', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_SUB_category='Hear Remover').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Hear_Remover.html', contex)


@csrf_exempt
def Foot_Cream(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_SUB_category='Foot Cream', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_SUB_category='Foot Cream').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Foot_Cream.html', contex)





@csrf_exempt
def Moisturizing_Cream(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_SUB_category='Moisturizing Cream', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_SUB_category='Moisturizing Cream').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Moisturizing_Cream.html', contex)




@csrf_exempt
def Toner(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_SUB_category='Toner', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_SUB_category='Toner').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Toner.html', contex)



@csrf_exempt
def Lip_Care(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_SUB_category='Lip Care', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_SUB_category='Lip Care').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Lip_Care.html', contex)


@csrf_exempt
def Eye_Care(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_SUB_category='Eye Care', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_SUB_category='Eye Care').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Eye_Care.html', contex)



@csrf_exempt
def Skin_Concern(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_SUB_category='Skin Concern', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_SUB_category='Skin Concern').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Skin_Concern.html', contex)



@csrf_exempt
def Shampoo(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_SUB_category='Shampoo', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_SUB_category='Shampoo').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Shampoo.html', contex)






@csrf_exempt
def Hear_Oil(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_SUB_category='Hear Oil', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_SUB_category='Hear Oil').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Hear_Oil.html', contex)




@csrf_exempt
def Hear_Tonic(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_SUB_category='Hear Tonic', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_SUB_category='Hear Tonic').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Hear_Tonic.html', contex)




@csrf_exempt
def Hear_Mask(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_SUB_category='Hear Mask', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_SUB_category='Hear Mask').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Hear_Mask.html', contex)




@csrf_exempt
def Hear_Treatment(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_SUB_category='Hear Treatment', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_SUB_category='Hear Treatment').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Hear_Treatment.html', contex)



@csrf_exempt
def Hear_Serum(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_SUB_category='Hear Serum', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_SUB_category='Hear Serum').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Hear_Serum.html', contex)




@csrf_exempt
def Conditioner(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_SUB_category='Conditioner', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_SUB_category='Conditioner').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Conditioner.html', contex)



@csrf_exempt
def Face(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_SUB_category='Face', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_SUB_category='Face').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Face.html', contex)






@csrf_exempt
def Eyes(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_SUB_category='Eyes', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_SUB_category='Eyes').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Eyes.html', contex)



@csrf_exempt
def Lips(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_SUB_category='Lips', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_SUB_category='Lips').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Lips.html', contex)


@csrf_exempt
def Nails(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_SUB_category='Nails', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_SUB_category='Nails').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Nails.html', contex)




@csrf_exempt
def Brushes_and_Accessories(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_SUB_category='Brushes & Accessories', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_SUB_category='Brushes & Accessories').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Brushes_and_Accessories.html', contex)





@csrf_exempt
def Health_care(request):
    range_1 = request.POST.get('range_1')
    range_2 = request.POST.get('range_2')
    if range_1 and range_2:
        Trandy_Products_product_here = Product_details.objects.filter(Q(Product_category='Health care', Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        Trandy_Products_product_here = Product_details.objects.filter(Product_category='Health care').order_by('-id')
    print('Trandy_Products_product_here')
    print(Trandy_Products_product_here)

    p = Paginator(Trandy_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {

        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
    }

    return render(request, 'Health_care.html', contex)




@csrf_exempt
def Category_product(request, pk):
    range_1 = request.GET.get('range_1')
    range_2 = request.GET.get('range_2')

    get_cat = Category.objects.get(id=pk)

    if range_1 and range_2:
        category_Products_product_here = Product_details.objects.filter(Q(Product_Category=get_cat, Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        category_Products_product_here = Product_details.objects.filter(Product_Category=get_cat).order_by('-id')
    print('category_Products_product_here')
    print(category_Products_product_here)

    p = Paginator(category_Products_product_here, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {
        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
        'pk': pk,
    }
    return render(request, 'Product.html', contex)



@csrf_exempt
def Contact(request):
    if request.method == "POST":
        contact_email = request.POST.get('contact_email')
        contact_subject = request.POST.get('contact_subject')
        contact_message = request.POST.get('contact_message')

        var_contact_info = contact_table(Email=contact_email, Subject=contact_subject, Message=contact_message)
        var_contact_info.save()
        messages.success(request, "Successfully Sent message to admin !")
    return render(request, 'Contact.html')




def searchbar(request):
    searchbox = request.GET.get('searchbox')

    range_1 = request.GET.get('range_1')
    range_2 = request.GET.get('range_2')

    if range_1 and range_2:
        product_search = Product_details.objects.filter(
            Q(Product_Title__icontains=searchbox, Product_Discount_Prize__range=[range_1, range_2])).order_by('-id')
    else:
        product_search = Product_details.objects.filter(Product_Title__icontains=searchbox).order_by('-id')

    print('product_search')
    print(product_search)

    p = Paginator(product_search, 15)
    number_of_pages = p.num_pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(page)
    print('page')
    print(list)
    contex = {
        'Trandy_Products_product_here': page,
        'list': list,
        'range_1': range_1,
        'range_2': range_2,
        'searchbox': searchbox,
    }
    return render(request, 'Search_Product.html', contex)


