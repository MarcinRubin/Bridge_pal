from api.models import Player

summarized_players_scores = '''
select api_player.id, name,
sum(CASE
	when api_pairing.n_id = api_player.id then result
	when api_pairing.s_id = api_player.id then result
	when api_pairing.e_id = api_player.id then -result
	when api_pairing.w_id = api_player.id then -result
end) as final
from api_player
left join api_pairing
on api_player.id in (api_pairing.e_id, api_pairing.w_id, api_pairing.s_id, api_pairing.n_id)
left join api_score
on api_score.pairing_id = api_pairing.id
group by api_player.id
'''

def get_players_scores():
    scores = Player.objects.raw(summarized_players_scores)
    data = [{"name": i.name, "final": i.final} for i in scores]
    return data