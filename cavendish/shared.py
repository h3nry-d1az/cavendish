from typing import Tuple


def cartesian_to_pygame(
    x: float,
    y: float
) -> Tuple[float, float]:
    return (x/1e9 + 320, 240 - y/1e9)