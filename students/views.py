from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.db.models import Q,Avg 

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def feedback(request, username):
    # Get the profile owner
    profile_owner = get_object_or_404(User, username=username)
    profile = get_object_or_404(StudentProfile, user=profile_owner)
    
    # Debug: Print the logged-in user and profile owner
    print(f"Sender (logged-in user): {request.user.username}")
    print(f"Receiver (profile owner): {profile_owner.username}")

    # Fetch feedback data
    feedbacks_received = Feedback.objects.filter(request__receiver=profile_owner)
    feedbacks_given = Feedback.objects.filter(request__sender=profile_owner)

    # Fetch accepted request (only if logged-in user != profile owner)
    accepted_request = None
    if request.user != profile_owner:
        accepted_request = SkillRequest.objects.filter(
            sender=request.user,
            receiver=profile_owner,
            status='Accepted'
        ).first()

    # Debug: Print the accepted request
    print(f"Accepted request: {accepted_request}")

    return render(request, 'feedback.html', {
        'profile': profile,
        'feedbacks_received': feedbacks_received,
        'feedbacks_given': feedbacks_given,
        'has_accepted_request': accepted_request is not None,
        'accepted_request_id': accepted_request.id if accepted_request else None,
    })


def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(StudentProfile, user=user)
    
    # Check if the logged-in user has an accepted request with the profile owner
    has_accepted_request = SkillRequest.objects.filter(
    Q(sender=request.user, receiver=user) | Q(sender=user, receiver=request.user),
    status='Accepted'
).exists()
    
    return render(request, 'profile.html', {
        'profile': profile,
        'has_accepted_request': has_accepted_request,
    })

def profile_redirect(request):
    return redirect('profile', username=request.user.username)

def edit_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user.studentprofile)
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)
    else:
        form = ProfileEditForm(instance=request.user.studentprofile)
    return render(request, 'edit_profile.html', {'form': form})

def search(request):
    query = request.GET.get('q')
    if query:
        keywords = query.split()  # Split the query into individual keywords
        results = StudentProfile.objects.filter(skills__icontains=query).annotate(
            avg_rating=Avg('user__received_requests__feedback__rating')
        ).order_by('-avg_rating')
        for keyword in keywords[1:]:  # Filter by additional keywords
            results = results.filter(skills__icontains=keyword)
    else:
        results = []
    return render(request, 'search.html', {'results': results, 'query': query})


def send_request(request, username):
    receiver = get_object_or_404(User, username=username)
    if request.method == 'POST':
        form = SkillRequestForm(request.POST)
        if form.is_valid():
            skill_request = form.save(commit=False)
            skill_request.sender = request.user
            skill_request.receiver = receiver
            skill_request.save()
            return redirect('profile', username=username)
    else:
        form = SkillRequestForm()
    return render(request, 'send_request.html', {'form': form, 'receiver': receiver})

def view_requests(request):
    received_requests = SkillRequest.objects.filter(receiver=request.user)
    return render(request, 'view_requests.html', {'received_requests': received_requests})

def accept_request(request, request_id):
    skill_request = get_object_or_404(SkillRequest, id=request_id, receiver=request.user)
    skill_request.status = 'Accepted'
    skill_request.save()
    return redirect('view_requests')

def decline_request(request, request_id):
    skill_request = get_object_or_404(SkillRequest, id=request_id, receiver=request.user)
    skill_request.status = 'Declined'
    skill_request.save()
    return redirect('view_requests')

def submit_feedback(request, request_id):
    skill_request = get_object_or_404(SkillRequest, id=request_id)

    # Ensure only the sender of the request can submit feedback
    if request.user != skill_request.sender:
        return redirect('home')  # Redirect unauthorized users

    # Ensure the request is accepted
    if skill_request.status != 'Accepted':
        return redirect('home')  # Redirect if the request is not accepted

    # Prevent duplicate feedback
    if Feedback.objects.filter(request=skill_request).exists():
        return redirect('feedback', username=skill_request.receiver.username)  # Redirect to prevent duplicate feedback

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.request = skill_request
            feedback.save()
            return redirect('feedback', username=skill_request.receiver.username)  # Redirect to feedback page after submission
    else:
        form = FeedbackForm()

    return render(request, 'submit_feedback.html', {
        'form': form,
        'skill_request': skill_request,
    })


def confirm_logout(request):
    return render(request, 'logout.html')



    # def submit_feedback(request, request_id):
    # # Get the skill request
    # skill_request = get_object_or_404(SkillRequest, id=request_id)
    
    # # Ensure the logged-in user is the sender of the request
    # if request.user != skill_request.sender:
    #     return redirect('home')  # Redirect unauthorized users
    
    # # Ensure the request is accepted
    # if skill_request.status != 'Accepted':
    #     return redirect('home')  # Redirect if the request is not accepted
    
    # if request.method == 'POST':
    #     form = FeedbackForm(request.POST)
    #     if form.is_valid():
    #         feedback = form.save(commit=False)
    #         feedback.request = skill_request
    #         feedback.save()
    #         return redirect('view_requests')
    # else:
    #     form = FeedbackForm()
    
    # return render(request, 'submit_feedback.html', {
    #     'form': form,
    #     'skill_request': skill_request,
    # })

    