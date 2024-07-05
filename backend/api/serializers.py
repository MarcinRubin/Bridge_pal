from .models import Player, Deal, Score, Pairing, Game, Movement
from rest_framework import serializers
from bridge_tools.game import GameCreator


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        exclude = ["game"]


class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        exclude = ["game"]


class PairingSerializer(serializers.ModelSerializer):
    # n = PlayerSerializer()
    # s = PlayerSerializer()
    # e = PlayerSerializer()
    # w = PlayerSerializer()

    class Meta:
        model = Pairing
        fields = "__all__"


class ScoreSerializer(serializers.ModelSerializer):
    deal = serializers.SlugRelatedField(read_only=True, slug_field='deal_number')
    pairing = PairingSerializer()

    class Meta:
        model = Score
        exclude = ["game"]


class MovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movement
        exclude = ["path"]


class GameSerializer(serializers.ModelSerializer):
    movement = MovementSerializer(read_only=True)

    class Meta:
        model = Game
        exclude = ("owner",)


class GameSerializerCreate(GameSerializer):
    movement = serializers.PrimaryKeyRelatedField(queryset=Movement.objects.all())

    class Meta:
        model = Game
        exclude = ("date", "owner")


class GameSerializerLoadAll(GameSerializer):
    movement = MovementSerializer(read_only=True)
    deals = DealSerializer(many=True, read_only=True)
    scores = ScoreSerializer(many=True, read_only=True)
    players = PlayerSerializer(many=True, read_only=True)
