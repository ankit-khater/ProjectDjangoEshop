
from django.shortcuts import render,redirect
from store.models import Customer
from django.contrib.auth.hashers import make_password
from django.views import View





class Signup(View):
    def validateCustomer(self,customer_object):
        error_message = None
        if not customer_object.first_name:
            error_message = 'First Name Required'
        elif len(customer_object.first_name) < 4:
            error_message = 'First Name Required atleast 4 charecter'
        elif not customer_object.last_name:
            error_message = 'Last Name Required'
        elif len(customer_object.last_name) < 4:
            error_message = 'Last Name Required atleast 4 charecter'
        elif not customer_object.phone:
            error_message = 'Phone Number Required'
        elif len(customer_object.phone) < 11:
            error_message = 'Phone Number Required atleast 11 digit'
        elif not customer_object.password:
            error_message = 'Password Required'
        elif len(customer_object.password) < 6:
            error_message = 'Password Required atleast 6 Charecter'
        elif len(customer_object.email) < 5:
            error_message = 'Email required atleast 5 charecter'
        elif customer_object.isExists():
            error_message = 'Email Address Already Registered'
        # ---------#
        return error_message

    def get(self,request):
        return render(request, 'signup.html')

    def post(self,request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        customer_objec = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email,
                                  password=password)
        error_message = self.validateCustomer(customer_objec)

        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer_objec.password = make_password(customer_objec.password)
            customer_objec.register()
            return redirect('homepage')

        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)