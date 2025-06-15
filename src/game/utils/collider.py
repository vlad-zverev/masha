from ..types import Area, Coordinates


def check_in_area(point: Coordinates, area: Area) -> bool:
    x_point, y_point = point
    (x_area, y_area), (x_size, y_size) = area

    return x_area < x_point < x_area + x_size and y_area < y_point < y_area + y_size
