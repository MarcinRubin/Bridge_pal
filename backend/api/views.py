from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, \
    UpdateModelMixin, CreateModelMixin
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from .models import Player, Deal, Pairing, Score, Game, Movement
from .serializers import PlayerSerializer, DealSerializer, PairingSerializer, \
    ScoreSerializer, GameSerializer, \
    GameSerializerCreate, GameSerializerLoadAll, MovementSerializer
from bridge_tools.parsers import ContractParser
from bridge_tools.deals_scorers import ImpScorer
from bridge_tools.get_players_scores import get_players_scores


class GameViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin,
                  GenericViewSet):
    """
        This view set is responsible for listing, creating and retrieving games.
        Only logged-in user can interact with this view and all operations are
        restricted to games owned by a particular user.

        Creation of game object generates the post_save signal that
        is captured and the whole game creation step is performed then
    """
    queryset = Game.objects.all()
    serializer_classes = {
        "create": GameSerializerCreate,
        "load_game": GameSerializerLoadAll
    }
    default_serializer_class = GameSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)

    def get_serializer_class(self, *args, **kwargs):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=["GET"])
    def load_game(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class PlayerViewSet(UpdateModelMixin, ListModelMixin, GenericViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    @action(detail=False, methods=["GET"])
    def scores(self, request):
        return Response(get_players_scores(), status=status.HTTP_200_OK)


class ScoreViewSet(UpdateModelMixin, ListModelMixin, RetrieveModelMixin,
                   GenericViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

    @action(detail=True, methods=["POST"])
    def score_update(self, request, pk=None):
        instance = self.get_object()
        parser = ContractParser(request.data.get("score"), instance.deal.vul)
        parser.is_valid(raise_exception=True)

        # score = SingleDealScorer(parser)
        serializer = self.get_serializer(instance, data=score,
                                         partial=True)
        serializer.is_valid(raise_exception=True)
        updated_instance = serializer.save()

        imp_scorer = ImpScorer(updated_instance)
        return Response(imp_scorer.data, status=status.HTTP_200_OK)


class PairingViewSet(RetrieveModelMixin, UpdateModelMixin, ListModelMixin,
                     GenericViewSet):
    queryset = Pairing.objects.all()
    serializer_class = PairingSerializer

    def get_serializer_class(self):
        print(self.action)
        if self.action == "partial_update":
            return PairingSerializerUpdateOnly
        return super().get_serializer_class()

    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        instance = self.get_object()
        serializer = PairingSerializer(instance)
        return Response(serializer.data)


class DealViewSet(ListModelMixin, GenericViewSet):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer


class MovementViewSet(ListModelMixin, GenericViewSet):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer
