import math
import logging

logger = logging.getLogger(__name__)


def estimate_tire_degradation(current_temp, max_temp, laps_completed, laps_total):
    temperature_change = (max_temp - current_temp) / laps_total
    temperature_change_per_lap = temperature_change / laps_total
    temperature_difference = current_temp - max_temp
    if temperature_difference < 0:
        return 0
    tire_degradation = (temperature_difference / max_temp) * 100
    return max(0, tire_degradation - laps_completed * temperature_change_per_lap * 100)


def estimate_tire_wear(
    current_temp, max_temp, laps_completed, laps_total, tire_condition
):
    optimal_temp_range = (max_temp - 10, max_temp + 10)
    current_temp_range = (current_temp - 5, current_temp + 5)
    temperature_difference = (
        max(optimal_temp_range[0], current_temp_range[0])
        - min(optimal_temp_range[1], current_temp_range[1])
    ) / 2
    tire_wear = (
        (temperature_difference / 10)
        * (laps_completed / laps_total)
        * (tire_condition / 100)
    )
    return max(0, tire_wear * 100)


def calculate_avg_laps_per_degradation(laps_total, tire_degradation_values):
    return sum(
        laps_completed
        for laps_completed, tire_degradation in zip(laps_total, tire_degradation_values)
        if tire_degradation > 0
    ) / sum(
        1
        for laps_completed, tire_degradation in zip(laps_total, tire_degradation_values)
        if tire_degradation > 0
    )


def calculate_degradation_over_time(tire_degradation_intervals, intervals_duration):
    return sum(
        laps_total[i] - laps_total[i - 1]
        for i, laps_completed in enumerate(laps_total)
        if i > 0 and tire_degradation_intervals[i - 1] > 0
    ) / sum(intervals_duration[i] for i in range(1, len(intervals_duration)))
