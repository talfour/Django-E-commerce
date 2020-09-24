from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import csrf
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .forms import AuctionForm, ImageForm, BidForm, AddBidForm, CommentForm
from django.contrib import messages
import datetime
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


from .models import User, Auction, Image, Bid, Comment


def index(request):
    object_list = Auction.objects.all().order_by('-time')
    paginator = Paginator(object_list, 8)
    page = request.GET.get('page')
    try:
        auctions = paginator.page(page)
    except PageNotAnInteger:
        auctions = paginator.page(1)
    except EmptyPage:
        auctions = paginator.page(paginator.num_pages)

    return render(request, "auctions/index.html",{"auctions":auctions, "page":page})
    

def detail_view(request, pk):
    auction = get_object_or_404(Auction, pk=pk)
    images = Image.objects.filter(auction=auction)
    bid = Bid.objects.get(auction=auction)
    user = request.user
    comments = auction.comments.filter(active=True)
    new_comment = None
    new_bid = None

    if request.method == "POST" and 'comment_button' in request.POST:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.auction = auction
            new_comment.user = user
            new_comment.save()
    else:
        comment_form = CommentForm()
   
    if request.method == "POST" and 'bid_button' in request.POST:
        bid_form = AddBidForm(request.POST, instance=bid)
        bid_number = bid_form.data['starting_bid']
        if float(bid_number) > bid.starting_bid:
            if bid_form.is_valid:
                new_bid = bid_form.save(commit=False)
                new_bid.highest_bidder = request.user
                new_bid.auction = auction
                new_bid.save()
                auction_to_watchlist = Auction.objects.get(id=pk)
                auction_to_watchlist.watch_list.add(user)
                auction.save()
        else:
            messages.error(request,'Your bid must be higher than the actual bid.')
    else:
        bid_form = BidForm()

    return render(request, "auctions/detail.html", {
        "auction":auction,
        "images":images,
        "bid":bid,
        'bid_form':bid_form,
        'comments':comments,
        'new_comment':new_comment,
        'comment_form':comment_form,
        'new_bid':new_bid
    })


def mark_listing_as_inactive(request, pk):
    auction = Auction.objects.get(pk=pk)
    auction.is_active = False
    auction.save()

    return redirect('auctions:index')


def add_watch_listing(request, pk):
    user = request.user
    auction = Auction.objects.get(id=pk)
    auction.watch_list.add(user)
    auction.save()

    return HttpResponseRedirect(reverse("auctions:detail",kwargs={"pk":auction.pk}))

def delete_watch_listing(request, pk):
    user = request.user
    auction = Auction.objects.get(id=pk)
    auction.watch_list.remove(user)
    auction.save()

    return HttpResponseRedirect(reverse("auctions:detail",kwargs={"pk":auction.pk}))
    
def list_watching_listings(request):
    user = request.user
    followed_auction = user.follow.all()
    return render(request, 'auctions/watch_list.html', {'followed_auction':followed_auction})

def new_listing(request):
    if request.method == "POST":
        auction_form = AuctionForm(request.POST)
        bid_form = BidForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)
        current_user = request.user
        images = request.FILES.getlist('image')
        if auction_form.is_valid and bid_form.is_valid and image_form.is_valid:
            auction = auction_form.save(commit=False)
            auction.user = current_user
            auction.image = images[0]
            auction.time = datetime.datetime.now(tz=timezone.utc)
            auction.save()
            bid = bid_form.save(commit=False)
            bid.auction = auction
            bid.save()            
            for i in images:
                instance = Image(image=i, user=current_user, auction=auction)
                instance.save()
            return HttpResponseRedirect(reverse('auctions:detail', kwargs={"pk":auction.pk}))
    else:
        auction_form = AuctionForm()
        bid_form = BidForm()
        image_form = ImageForm()
    context = {}
    context.update(csrf(request))
    context['auction_form'] = auction_form
    context['bid_form'] = bid_form
    context['image_form'] = image_form
    return render(request, "auctions/auction_form.html", context)


def search_by_categories(request):
    query = request.GET.get('q')

    results = Auction.objects.filter(category__icontains=query)

    paginator = Paginator(results, 8)
    page = request.GET.get('page')
    try:
        auctions = paginator.page(page)
    except PageNotAnInteger:
        auctions = paginator.page(1)
    except EmptyPage:
        auctions = paginator.page(paginator.num_pages)

    context = {
        'auctions':auctions, 'page':page
    }
    return render(request, "auctions/search.html" , context)

def categories_list(request):
    categories = Auction._meta.get_field('category').choices
    categories_list = []
    for category in categories:
        categories_list.append(category[1])
    return render(request, "auctions/categories.html", {'categories':categories_list})

def categories_requested(request, category):
    auctions = Auction.objects.filter(category__icontains=category)
    return render(request, "auctions/categories_requested.html",{'auctions':auctions})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("auctions:index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("auctions:index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("auctions:index"))
    else:
        return render(request, "auctions/register.html")
