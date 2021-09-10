from django.shortcuts import render,redirect,HttpResponse
from store.models import Product
from store.models import Categories
from django.views import View

class Index(View):
    #for handelling session
    def post(self,request):
        product=request.POST.get('product')
        print(product)
        cart=request.session.get('cart')
        remove = request.POST.get('remove')
        #if cart exists then check quantiy
        if cart:
            #get quantity by product_id
            quantity=cart.get(product)
            #check wheather quantity is available or not
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity+1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1

        request.session['cart']=cart
        print("Cart",request.session['cart'])
        return redirect('homepage')

    def get(self,request):
        # print(product)
        cart=request.session.get('cart')
        if not cart:
            request.session.cart={}
        categories = Categories.get_all_categories()

        categoryId = request.GET.get('category')

        if categoryId:
            product = Product.get_all_product_by_categoryid(categoryId)
        else:
            product = Product.get_all_product()

        data = {}
        data['products'] = product
        data['categories'] = categories
        return render(request, 'index.html', data)
        # return HttpResponse('helloooooooo')





