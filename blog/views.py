from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import forms, models


@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    return render(request, 'blog/home.html',context={'tickets': tickets})

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
def follow_users(request):
    form = forms.FollowUsersForm(instance=request.user)
    if request.method == 'POST':
        form = forms.FollowUsersForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'blog/follow_users_form.html', context={'form': form})