import logging
from typing import List

logger = logging.getLogger(__name__)


def compare_sector_times(sector_times_1, sector_times_2):
    if len(sector_times_1) != len(sector_times_2):
        raise ValueError("Sector times must have the same length")

    performance_delta = []
    for i in range(len(sector_times_1)):
        delta = (sector_times_2[i] - sector_times_1[i]) / sector_times_1[i] * 100
        performance_delta.append(delta)

    return performance_delta


def calculate_total_performance_delta(performance_deltas: List[float]):
    if not performance_deltas:
        raise ValueError("List of performance deltas cannot be empty")

    return sum(performance_deltas) / len(performance_deltas)
