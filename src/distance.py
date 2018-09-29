from math import (
    pi,
    sin,
    cos,
    acos)
from typing import Tuple


def check_lon(lon: float) -> bool:
    if lon > 180 or lon < -180:
        raise ValueError(
            f'Longitude value shoule be between +/- 180, got: {lon}')
    return True


def check_lat(lat: float) -> bool:
    if lat > 90 or lat < -90:
        raise ValueError(
            f'Longitude value shoule be between +/- 90, got: {lat}')
    return True


def to_radian(*, lon: float, lat: float) -> Tuple[float, float]:
    lon, lat = map(
        lambda degree: float(degree) / (180 / pi),
        (lon, lat))
    return lon, lat


def get_central_angle(
        radian_1: Tuple[float, float],
        radian_2: Tuple[float, float]) -> float:
    """get central angle
    ref: https://en.wikipedia.org/wiki/Great-circle_distance
    """
    lon_1, lat_1 = radian_1
    lon_2, lat_2 = radian_2
    delta_lambda = abs(lon_1 - lon_2)
    term_1 = sin(lat_1) * sin(lat_2)
    term_2 = cos(lat_1) * cos(lat_2) * cos(delta_lambda)
    return acos(term_1 + term_2)


def cal_distance(
        earth_radius: float = 6_371,
        *,
        pin_lon: float,
        pin_lat: float,
        lon: float,
        lat: float) -> float:
    pin = to_radian(lon=pin_lon, lat=pin_lat)
    loc = to_radian(lon=lon, lat=lat)
    return earth_radius * get_central_angle(pin, loc)


def get_distance(**kwargs) -> float:
    check_lon(kwargs['pin_lon'])
    check_lon(kwargs['lon'])
    check_lat(kwargs['pin_lat'])
    check_lat(kwargs['lat'])
    return cal_distance(**kwargs)
