from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import forms, models
from django.db import IntegrityError
from django.contrib import messages
from authentication.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.template.defaulttags import register


@login_required
def home(request):
    users = [u.followed_user for u in models.UserFollows.objects.filter(user=request.user)]
    users.append(request.user)
    reviews = models.Review.objects.filter(user__in=users)
    reviews_ticket_id = []
    for r in reviews:
        if r.ticket is None:  # cas d'une critique spontanée sans ticket
            pass
        else:
            reviews_ticket_id.append(r.ticket.id)
    try:
        tickets_with_review = models.Ticket.objects.filter(
            Q(user__in=users) & Q(id__in=reviews_ticket_id))
    except UnboundLocalError:  # cas d'un nouvel utilisateur qui n'a encore ni abonné ni ticket
        tickets_with_review = []
    try:
        tickets = models.Ticket.objects.filter(user__in=users).exclude(
            id__in=tickets_with_review)
    except UnboundLocalError:  # cas d'un nouvel utilisateur qui n'a encore ni abonné ni ticket
        tickets = []
    except ValueError:  # cas d'un nouvel utilisateur qui n'a encore ni abonné ni ticket
        tickets = []

    return render(request, 'blog/home.html', context={'tickets': tickets,
                                                      'reviews': reviews,
                                                      'tickets_with_review': tickets_with_review
                                                      })


@login_required
def posts(request):
    tickets = models.Ticket.objects.filter(user=request.user)
    reviews = models.Review.objects.filter(user=request.user)
    return render(request, 'blog/posts.html', context={'tickets': tickets,
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
    return render(request, 'blog/ticket.html', context={'form': form})


@login_required
def ticket_review_upload(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
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
    return render(request, 'blog/ticket_review.html', context={'form': form,
                                                               'ticket': ticket})


@login_required
def review_upload(request):
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
    return render(request, 'blog/review.html', context={'form': form})


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
            edit_form = forms.TicketForm(request.POST, request.FILES, instance=ticket)
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
        'delete_form': delete_form}
    return render(request, 'blog/edit_ticket.html', context=context)


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    edit_form = forms.TicketReviewForm(instance=review)
    delete_form = forms.DeleteTicketReviewForm()
    if request.method == 'POST':
        if 'edit_review' in request.POST:
            edit_form = forms.TicketReviewForm(request.POST, instance=review)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('home')
        if 'delete_review' in request.POST:
            delete_form = forms.DeleteTicketReviewForm(request.POST, request.FILES)
            if delete_form.is_valid():
                review.delete()
                return redirect('home')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
        'review': review, }
    return render(request, 'blog/edit_review.html', context=context)


@login_required
def follow_users(request):
    form = forms.UserFollowsForm()
    context = {'form': form}

    # display subscriptions
    followed_users = models.UserFollows.objects.filter(user=request.user)
    context['followed_users'] = followed_users

    # display 'subscribers'
    followers = models.UserFollows.objects.filter(followed_user=request.user)
    context['followers'] = followers

    if request.method == 'POST':
        # get the searched user
        try:
            new_followed_user = User.objects.get(username=request.POST['followed_user'])
        except ObjectDoesNotExist:
            error_message = f"<strong>{request.POST['followed_user'].lower()}" \
                            f"</strong> n'existe pas dans la base de donnée."
            messages.add_message(request, messages.ERROR, message=error_message)
            return render(request,
                          "blog/follow_users_form.html",
                          context=context)
        except None:
            error_message = f"<strong>{request.POST['followed_user'].lower()}" \
                            f"</strong> n'existe pas dans la base de donnée."
            messages.add_message(request, messages.ERROR, message=error_message)
            return render(request,
                          "blog/follow_users_form.html",
                          context=context)
        else:
            # case where the user is looking for himself
            if new_followed_user.username == request.user.username:
                error_message = " --- Vous ne pouvez pas vous suivre vous même! --- "
                messages.add_message(request, messages.ERROR, message=error_message)
                return render(request, "blog/follow_users_form.html",
                              context=context)

            # new followed_user registration
            new_subscription = models.UserFollows(user=request.user, followed_user=new_followed_user)
            try:
                new_subscription.save()
            except IntegrityError:
                error_message = f"Vous suivez déjà <strong>{new_followed_user}</strong>."
                messages.add_message(request, messages.ERROR, message=error_message)
                return render(request,
                              "blog/follow_users_form.html",
                              context=context)
            else:
                success_message = f"Vous suivez désormais <strong>{new_subscription.followed_user}</strong>."
                messages.add_message(request, messages.SUCCESS, message=success_message)
                return render(request,
                              "blog/follow_users_form.html",
                              context=context)
    return render(request, "blog/follow_users_form.html", context=context)


@login_required
def delete_subscription(request, followed_user_id):
    subscription = models.UserFollows.objects.get(id=followed_user_id)
    subscription.delete()
    return redirect('follow_users')


@login_required  # fonction pour l'affichage en étoile du rating des livres
@register.simple_tag
def range_rating(number):
    return [*range(1, number+1)]


@login_required  # fonction pour l'affichage en étoile du rating des livres
@register.simple_tag
def range_not_rating(number):
    return [*range(number, 5)]
