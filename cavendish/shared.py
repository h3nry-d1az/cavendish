from typing import Tuple


def cartesian_to_pygame(
    x: float,
    y: float,
    scale: float = 1
) -> Tuple[float, float]:
    return (x*scale + 320, 240 - y*scale)

def pygame_to_cartesian(
    x: float,
    y: float,
    scale: float = 1
) -> Tuple[float, float]:
    return ((x - 320)/scale, (240 - y)/scale)