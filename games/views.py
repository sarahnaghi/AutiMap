from django.shortcuts import render,redirect
from . import views
from django.http import HttpRequest,HttpResponse
from .models import DigitalGame,Toy

# Create your views here.


def add_game_apps_view(request: HttpRequest):

 if request.user.is_superuser:

    if request.method == "POST":
        new_book = DigitalGame(game_name=request.POST["game_name"], game_image=request.FILES["game_image"], game_description=request.POST["game_description"], game_url_appstore=request.POST["game_url_appstore"],game_play_store=request.POST["game_play_store"])
        new_book.save()
        redirect("games/all_games_view")
    return render(request, 'games/add_digital_game.html')


def all_games_view(request: HttpRequest):

    games = DigitalGame.objects.all()

    return render(request, "games/all_digital_games.html", {"games" : games})


def add_toy_view(request: HttpRequest):

 if request.user.is_superuser:

    if request.method == "POST":
        new_toy = Toy(game_name=request.POST["game_name"], game_image=request.FILES["game_image"], game_description=request.POST["game_description"], game_url=request.POST["game_url"])
        new_toy.save()
        redirect("games/all_toys_view")


    return render(request, 'games/add_toy.html')


def all_toys_view(request: HttpRequest):

    toys = Toy.objects.all()

    return render(request, "games/all_toys.html", {"toys" : toys})


def game_view(request: HttpRequest):
    
    return render(request, "games/games.html")



def digital_game_update_view(request:HttpRequest, game_id):
    if request.user.is_superuser:

        game = DigitalGame.objects.get(id= game_id)

        if request.method == "POST" and request.user.is_superuser:
            game.game_name = request.POST["game_name"]
            game.game_description = request.POST["game_description"]
            if "game_image" in request.FILES:
                game.game_image = request.FILES["game_image"]
            game.game_url_appstore = request.POST["game_url_appstore"]
            game.game_play_store = request.POST["game_play_store"]
            game.save()

            return redirect("games:all_game_view")
        return render(request, "games/update_games.html", {"game": game })


def digital_game_delete_view(request: HttpRequest,game_id):
 if request.user.is_superuser:

    game = DigitalGame.objects.get(id= game_id)
    game.delete()

    return redirect("games:all_game_view")


def toy_update_view(request:HttpRequest, toy_id):
     if request.user.is_superuser:

        toy = Toy.objects.get(id= toy_id)

        if request.method == "POST" and request.user.is_superuser:
            toy.game_name = request.POST["game_name"]
            toy.game_description = request.POST["game_description"]
            if "game_image" in request.FILES:
                toy.game_image = request.FILES["game_image"]
            toy.game_url = request.POST["game_url"]
            toy.save()

            return redirect("games:all_toys_view")
        return render(request, "games/update_toys.html", {"toy": toy })


def toy_delete_view(request: HttpRequest,toy_id):
 if request.user.is_superuser:

    toy = Toy.objects.get(id= toy_id)
    toy.delete()

    return redirect("games:all_toys_view")



