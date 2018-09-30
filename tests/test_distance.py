import pytest

from src.distance import (
    check_lon,
    check_lat,
    to_radian,
    get_central_angle,
    cal_distance,
    get_distance
)


@pytest.mark.parametrize('lon', [
    (180), (-180), (0)])
def test_check_lon_pass(lon):
    assert check_lon(lon)


@pytest.mark.parametrize(
    'lon, error',
    [(180.1, ValueError),
     (-180.1, ValueError),
     ('100', TypeError),
     ('number', TypeError)])
def test_check_lon_raise(lon, error):
    with pytest.raises(error):
        check_lon(lon)


@pytest.mark.parametrize('lat', [
    (90), (-90), (0)])
def test_check_lat_pass(lat):
    assert check_lat(lat)


@pytest.mark.parametrize(
    'lat, error',
    [(90.1, ValueError),
     (-90.1, ValueError),
     ('10', TypeError),
     ('number', TypeError)])
def test_check_lat_raise(lat, error):
    with pytest.raises(error):
        check_lat(lat)


@pytest.mark.parametrize(
    'lon, lat, radian',
    [(50.123, 21, (0.8748113, 0.36651914)),
     (-10, -123.222, (-0.1745329, -2.1506296))])
def test_to_radian(lon, lat, radian):
    assert radian == pytest.approx(
        to_radian(lon=lon, lat=lat))


@pytest.mark.parametrize(
    'radian_1, radian_2, angle',
    [((0.87, 1.3), (-2, -1), 2.8241562),
     ((1, 2), (0.3, 0.97), 0.9641210)])
def test_get_central_angle(radian_1, radian_2, angle):
    assert angle == pytest.approx(get_central_angle(radian_1, radian_2))


@pytest.mark.parametrize(
    'pin, loc, dist',
    [((11, 22), (11, 22), 0.0),
     ((13.22, 15.22), (13.21, 15.22), 1.0729475),
     ((40, 50), (60, -70), 13441.3663699)])
def test_cal_distance(pin, loc, dist):
    (pin_lon, pin_lat), (lon, lat) = pin, loc
    assert dist == pytest.approx(cal_distance(
        pin_lon=pin_lon,
        pin_lat=pin_lat,
        lon=lon,
        lat=lat
    ))


@pytest.mark.parametrize(
    'pin, loc, dist',
    [((11, 22), (11, 22), 0.0),
     ((13.22, 15.22), (13.21, 15.22), 1.0729475),
     ((40, 50), (60, -70), 13441.3663699)])
def test_get_distance(pin, loc, dist):
    (pin_lon, pin_lat), (lon, lat) = pin, loc
    assert dist == pytest.approx(get_distance(
        pin_lon=pin_lon,
        pin_lat=pin_lat,
        lon=lon,
        lat=lat
    ))


@pytest.mark.parametrize(
    'pin, loc, error',
    [((180.1, 22), (11, 22), ValueError),
     (('13.22', 15.22), (13.21, 15.22), TypeError),
     ((40, 50), (60, -90.1), ValueError)])
def test_get_distance_raise(pin, loc, error):
    (pin_lon, pin_lat), (lon, lat) = pin, loc
    with pytest.raises(error):
        get_distance(
            pin_lon=pin_lon,
            pin_lat=pin_lat,
            lon=lon,
            lat=lat
        )
