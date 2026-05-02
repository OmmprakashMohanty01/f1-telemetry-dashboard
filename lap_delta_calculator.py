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


def calculate_sector_average_speed(sector_times: List[float]) -> float:
    if not sector_times:
        raise ValueError("List of sector times cannot be empty")

    return sum(sector_times) / len(sector_times)


from typing import List


def calculate_lap_average_speed(total_sector_times: List[List[float]]) -> float:
    def calculate_sector_average_speed(sector_times: List[float]) -> float:
        sector_time_sum = sum(sector_times)
        sector_time_count = len(sector_times)

        if sector_time_count == 0:
            raise ValueError("List of sector times cannot be empty")

        return sector_time_sum / sector_time_count

    lap_average_speed = 0
    lap_sector_time_sum = 0
    lap_sector_time_count = 0
    for sector_times in total_sector_times:
        lap_sector_average_speed = calculate_sector_average_speed(sector_times)
        lap_average_speed += lap_sector_average_speed
        lap_sector_time_sum += sector_times[-1]
        lap_sector_time_count += 1

    if lap_sector_time_count == 0:
        raise ValueError("List of sector times cannot be empty")

    return lap_average_speed / lap_sector_time_count
