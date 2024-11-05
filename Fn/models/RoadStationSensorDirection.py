from enum import Enum


class RoadStationSensorDirection(str, Enum):

    UNKNOWN = "UNKNOWN"
    INCREASING_DIRECTION = "INCREASING_DIRECTION"
    DECREASING_DIRECTION = "DECREASING_DIRECTION"
