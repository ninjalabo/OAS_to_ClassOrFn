from enum import Enum


class WeathercamPresetDirectionV1(str, Enum):

    UNKNOWN = "UNKNOWN"
    INCREASING_DIRECTION = "INCREASING_DIRECTION"
    DECREASING_DIRECTION = "DECREASING_DIRECTION"
    CROSSING_ROAD_INCREASING_DIRECTION = "CROSSING_ROAD_INCREASING_DIRECTION"
    CROSSING_ROAD_DECREASING_DIRECTION = "CROSSING_ROAD_DECREASING_DIRECTION"
    SPECIAL_DIRECTION = "SPECIAL_DIRECTION"
