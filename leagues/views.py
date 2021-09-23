from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count
from . import team_maker

def index(request):
	context = {
		'q1': League.objects.get(name = 'Pacific Basketball Conference').teams.all(),
		'q2': Team.objects.get(team_name='Cavaliers').curr_players.all(),
		'q3': Player.objects.filter(curr_team__league__name='Transamerican Amateur Baseball Federation').order_by('curr_team'),
		'q4': Player.objects.filter(curr_team__league__name = 'American Football Federation').filter(last_name = 'Morris'),
		'q5': Player.objects.filter(curr_team__league__sport='Football'),
		'q6': Player.objects.filter(first_name='Sophia').order_by('curr_team__league'),
		# 'q7': Team.objects.filter(location = 'Dallas'),
		'q8': Player.objects.exclude(curr_team__team_name__contains='nicks').filter(last_name = 'Sanchez'),
		'q9': Team.objects.filter(all_players__first_name='Samuel', all_players__last_name = 'Ramirez'),
		'q10': Player.objects.filter(all_teams__team_name = 'Celtics').order_by('curr_team'),
		'q11': Player.objects.filter(all_teams__team_name = 'Vikings').exclude(curr_team__team_name = 'Vikings'),
		'q12': Team.objects.filter(all_players__first_name = 'Matthew', all_players__last_name = 'Allen').exclude(team_name = 'Diamondbacks'),
		'q13': Player.objects.filter(all_teams__league__name = 'Atlantic Basketball League').filter(first_name = 'Olivia'),
		'q14': Team.objects.annotate(Count('curr_players')).annotate(Count('all_players')).filter(all_players__count__gte = 35).filter(curr_players__count__gte = 35).order_by('id'),
		'q15': Player.objects.all().annotate(Count('all_teams')).order_by('-all_teams__count'),
}

	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")