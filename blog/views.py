from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import forms, models
from django.shortcuts import get_object_or_404


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
