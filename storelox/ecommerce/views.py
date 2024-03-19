from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

# Create your views here.
def my_view(request):
    # Access the CSRF token from the request object
    csrf_token = request.META.get("CSRF_COOKIE", "")
    
    # Print the CSRF token to the console
    print("CSRF Token:", csrf_token)

    # You can also return the CSRF token in a JSON response if needed
    return JsonResponse({"csrf_token": csrf_token})

@csrf_exempt
def home(request):
    return HttpResponse("Welcome to Storelox!")
    

@csrf_exempt
def Login_View(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            # Authenticate user using email and password
            user = authenticate(email=email, password=password)

            if user is not None:
                # User is authenticated, generate JWT tokens
                refresh = RefreshToken.for_user(user)

                return JsonResponse({
                    'message': 'Login successful',
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                })
            else:
                # Authentication failed, return error message
                return JsonResponse({'error': 'Invalid email or password'}, status=400)
       
    except Exception as e:
        # Handle any exceptions and return error response
        return JsonResponse({'error': str(e)}, status=500)
    

    
# Registration
# @csrf_exempt
# def Register_View(request):
#     if request.method == 'POST':
#         # Retrieve data from the request
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         phone_Number = request.POST.get('phone_number')
#         password = request.POST.get('password')

#         # Check if all required fields are present
#         # if not (username and email and phone_Number and password):
#         #     return JsonResponse({'error': 'All fields are required'}, status=400)

#         try:
#             # Check if a user with the provided email or username already exists
#             if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
#                 return JsonResponse({'error': 'User with this email or username already exists'}, status=400)

#             # Create a new user instance
#             user = User.objects.create_user(username=username, email=email, phone_Number=phone_Number, password=password)
#             user.save()
#             return JsonResponse({'message': 'User registered successfully'})
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)
    
# def create_user(username, email, phone_Number, password):
#     try:
#         user = User.objects.create(
#             username=username,
#             email=email,
#             phone_Number=phone_Number,
#             password=password
#         )
#         return user
#     except Exception as e:
#         return None


@csrf_exempt
# def Register_View(request):
#     if request.method == 'POST':
#         # Retrieve data from the request
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         phone_Number = request.POST.get('phone_Number')
#         password = request.POST.get('password')

#         try:
#             # Check if username, email, phone number, and password are provided
#             if not (username and email and phone_Number and password):
#                 return JsonResponse({'error': 'All fields are required'}, status=400)

#             # Check if a user with the provided email already exists
#             if User.objects.filter(email=email).exists():
#                 return JsonResponse({'error': 'User with this email already exists'}, status=400)

#             # Check if a user with the provided username already exists
#             if User.objects.filter(username=username).exists():
#                 return JsonResponse({'error': 'User with this username already exists'}, status=400)

#             # Create a new user instance using the create_user function
#             # new_user = create_user(username, email, phone_Number, password)
#             new_user = create_user(username=username, email=email, phone_Number=phone_Number, password=password)

#             if new_user:
#                 return JsonResponse({'message': 'User registered successfully'})
#             else:
#                 return JsonResponse({'error': 'Failed to register user'}, status=500)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)

def Register_View(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)

            # Extract data from the request
            username = data.get('username')
            email = data.get('email')
            phone_Number = data.get('phone_Number')
            password = data.get('password')

            print("Received data:", data)

            # Check if username, email, phone number, and password are provided
            if not (username and email and phone_Number and password):
                return JsonResponse({'error': 'All fields are required'}, status=400)

            # Check if a user with the provided email already exists
            if User.objects.filter(email=email).exists():
                return JsonResponse({'error': 'User with this email already exists'}, status=400)

            # Check if a user with the provided username already exists
            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'User with this username already exists'}, status=400)

            # Create a new user instance
            user = User.objects.create(username=username, email=email, phone_Number=phone_Number, password=password)
            
            # Save the user object
            user.save()

            refresh = RefreshToken.for_user(user)

            return JsonResponse({
                'message': 'User registered successfully',
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            })

            return JsonResponse({'message': 'User registered successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)