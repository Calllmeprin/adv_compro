class Sensor:
    def __init__(self, sensor_type, distance):
        self.sensor_type = sensor_type
        self.distance = distance

s = Sensor("LiDAR", 5.0)
print(s.sensor_type, s.distance)
