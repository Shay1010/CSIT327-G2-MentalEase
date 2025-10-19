from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .forms import StudentSignUpForm, StudentLoginForm
from .supabase_client import supabase  # make sure you have supabase_client.py configured
from django.contrib.auth.decorators import login_required


# 📝 Student Sign Up
def signup_view(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            full_name = form.cleaned_data['full_name']  # use full_name everywhere
            password = form.cleaned_data['password']

            hashed_password = make_password(password)

            data = {
                "username": username,
                "email": email,
                "full_name": full_name,  # use full_name
                "password": hashed_password
            }

            response = supabase.table("students").insert(data).execute()
            print(response)  # Add this line to see the response in your terminal

            if response.data:
                messages.success(request, "✅ Account created successfully! Please log in.")
                return redirect('login')
            else:
                messages.error(request, f"❌ Failed to register. {response.error}")
    else:
        form = StudentSignUpForm()
    return render(request, 'students/signup.html', {'form': form})


# Student Login
def login_view(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)  # Remove 'request, data='
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            response = supabase.table("students").select("*").eq("email", email).execute()
            if response.data:
                student = response.data[0]
                if check_password(password, student['password']):
                    request.session['student'] = {
                        'id': student['id'],
                        'username': student['username'],
                        'email': student['email']
                    }
                    messages.success(request, f"👋 Welcome back, {student['username']}!")
                    return redirect('dashboard')
            messages.error(request, "❌ Incorrect email or password.")
    else:
        form = StudentLoginForm()
    return render(request, 'students/login.html', {'form': form})


#Logout
def logout_view(request):
    if 'student' in request.session:
        del request.session['student']
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')


#Student Dashboard
def student_dashboard(request):
    student = request.session.get('student', None)
    if not student:
        return redirect('login')
    return render(request, 'students/dashboard.html', {'student': student})

#Student Profile View
def profile_view(request):
    student_session = request.session.get('student', None)
    if not student_session:
        return redirect('login')

    # Fetch the student's data from Supabase
    response = supabase.table("students").select("*").eq("id", student_session['id']).execute()
    if not response.data:
        messages.error(request, "❌ Could not load your profile.")
        return redirect('dashboard')

    student = response.data[0]

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        year_program = request.POST.get('year_program')

        # Update student info in Supabase
        update_response = supabase.table("students").update({
            "full_name": full_name,
            "year_program": year_program
        }).eq("id", student['id']).execute()

        if update_response.data:
            messages.success(request, "✅ Profile updated successfully!")
            return redirect('profile')
        else:
            messages.error(request, "❌ Failed to update profile.")
    
    return render(request, 'students/profile.html', {'student': student})

#AboutUs
def about_us(request):
    return render(request, 'students/aboutus.html')