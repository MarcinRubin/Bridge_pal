"""
This module provides various scoring methods for deal scoring.
"""

from api.models import Score
from api.serializers import ScoreSerializer
from abc import ABC, abstractmethod

IMP = [
    [10, 0], [40, 1], [80, 2], [120, 3], [160, 4], [210, 5], [260, 6], [310, 7],
    [360, 8], [420, 9], [490, 10], [590, 11], [740, 12], [890, 13], [1090, 14],
    [1290, 15], [1490, 16], [1740, 17], [1990, 18], [2240, 19], [2490, 20],
    [2990, 21], [3490, 22], [3990, 23], [9999, 24]
]


def to_imp(score: int) -> int:
    """
        Convert the given score to the IMP points.
    """
    for row in IMP:
        if abs(score) < row[0]:
            return row[1] if score > 0 else -row[1]


class BaseScorer(ABC):
    """
        Base scorer that provides all the basic scorer functionality. Every other
        scores should inherit from this class and provide the impelementation of
        calculate_result_list functio
    """

    def __init__(self, instance: Score):
        self._score_objects = Score.objects.filter(deal=instance.deal).order_by("id")
        self._score_objects_scores = list(self._score_objects.values("score"))
        self._n_filled_scores = self._get_n_filled_scores()

        self._result_list = self._calculate_result_list()
        self._updated_list = self._update()

    @abstractmethod
    def _calculate_result_list(self) -> list[dict]:
        pass

    def _get_n_filled_scores(self) -> int:
        """
        Checks the number of filled scores. All scoring method are dependent on
        single contract scores, so it is relevant to know this number regardless of
        the scoring method
        """
        return sum([1 for item in self._score_objects_scores if item.get("score")])

    def _update(self):
        updated_data = []
        for (obj, update) in zip(self._score_objects, self._result_list):
            serializer = ScoreSerializer(obj, data=update, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            updated_data.append(serializer.data)
        return updated_data

    @property
    def data(self):
        return self._updated_list


class ImpScorer(BaseScorer):
    def _calculate_result_list(self) -> list[dict]:
        if self._n_filled_scores < 2:
            return [
                {**score, "result": None}
                for score in self._score_objects_scores
            ]

        results = []
        for score in self._score_objects_scores:
            if score.get('score') is None:
                results.append({**score, "result": None})
                continue

            cross_imp = sum(
                [
                    to_imp(score.get('score') - item.get('score'))
                    for item in self._score_objects_scores
                    if item.get('score') is not None
                ]
            ) / (self._n_filled_scores - 1)
            results.append({**score, "result": cross_imp})
        return results
