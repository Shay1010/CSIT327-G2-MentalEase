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

#Student Profile
def student_profile(request):
    """
    Renders the student profile page (which the dashboard template links to).
    """
    # Assuming the profile_modal.html file is also located in 'students/templates/students/'
    # You might pass student data here later, but for now, just render the template.
    
    # You mentioned the target file was profile_modal.html, so use that:
    return render(request, 'students/profile_modal.html', {})