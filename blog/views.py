from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import forms, models
from django.db import IntegrityError
from django.contrib import messages


@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    reviews = models.Review.objects.all()
    return render(request, 'blog/home.html',context={'tickets': tickets,
                                                     'reviews': reviews})

@login_required
def ticket_upload(request):
    form = forms.TicketForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            # set the uploader to the user before saving the model
            ticket.user = request.user
            # now we can save
            ticket.save()
            return redirect('home')
    return render(request, 'blog/ticket.html',context={'form': form})

@login_required
def ticket_review_upload(request):
    form = forms.TicketReviewForm()
    if request.method == 'POST':
        form = forms.TicketReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            # set the uploader to the user before saving the model
            review.user = request.user
            # now we can save
            review.save()
            return redirect('home')
    return render(request, 'blog/ticket_review.html', context={'form': form})

@login_required
def view_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    return render(request, 'blog/view_ticket.html', {'ticket': ticket})

@login_required
def view_review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    return render(request, 'blog/view_review.html', {'review': review})

@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    edit_form = forms.TicketForm(instance=ticket)
    delete_form = forms.DeleteTicketForm()
    if request.method == 'POST':
        if 'edit_ticket' in request.POST:
            edit_form = forms.TicketForm(request.POST, request.FILES,instance=ticket)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('home')
        if 'delete_ticket' in request.POST:
            delete_form = forms.DeleteTicketForm(request.POST, request.FILES)
            if delete_form.is_valid():
                ticket.delete()
                return redirect('home')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,}
    return render(request, 'blog/edit_ticket.html', context=context)

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    edit_form = forms.TicketReviewForm(instance=review)
    delete_form = forms.DeleteTicketForm()
    if request.method == 'POST':
        if 'edit_review' in request.POST:
            edit_form = forms.TicketReviewForm(request.POST, instance=review)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('home')
        if 'delete_review' in request.POST:
            delete_form = forms.DeleteTicketForm(request.POST, request.FILES)
            if delete_form.is_valid():
                review.delete()
                return redirect('home')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,}
    return render(request, 'blog/edit_review.html', context=context)


@login_required
def follow_users(request):
    form = forms.UserFollowsForm(instance=request.user)
    if request.method == 'POST':
        form = forms.UserFollowsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            try:
                """userfollows = form.save(commit=False)
                # set the uploader to the user before saving the model
                userfollows.user = request.user
                # now we can save
                userfollows.save()"""
                return redirect('home')
            except IntegrityError:
                error_message = f"<strong>vous suivez déjà " \
                            f"{request.POST['followed_user']}.</strong> "
                messages.add_message(request, messages.ERROR, message=error_message)
    # display subscriptions
    followed_users = models.UserFollows.objects.filter(user=request.user)

    # display subscribers
    followers = models.UserFollows.objects.filter(followed_user=request.user)

    return render(request, 'blog/follow_users_form.html',
                  context={'form': form,
                           'followed_users': followed_users,
                           'followers': followers})