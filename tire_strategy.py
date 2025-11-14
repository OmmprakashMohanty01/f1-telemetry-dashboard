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
