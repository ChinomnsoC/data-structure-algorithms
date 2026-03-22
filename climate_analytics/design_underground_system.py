# Design Underground System (LC 1396)
# Implement a system that tracks customer travel times between stations and calculates average travel times.
# undergroundSystem.checkIn(45, "Leyton", 3)
# undergroundSystem.checkIn(32, "Paradise", 8)
# undergroundSystem.checkOut(45, "Waterloo", 15)
# undergroundSystem.checkOut(32, "Cambridge", 22)
# undergroundSystem.getAverageTime("Leyton", "Waterloo") → 12.0
# Implement:

# checkIn(id, stationName, t) — customer id checks in at stationName at time t
# checkOut(id, stationName, t) — customer id checks out at stationName at time t
# getAverageTime(startStation, endStation) — return average time between the two stations


class UndergroundSystem:
    def __init__(self):
        self.route_map = {}
        self.check_in_map = {}

    def checkIn(self, id: int, stationName: str, t: int):
        # {id : (stationName, t)}

        self.check_in_map[id] = (stationName, t)

        

    def checkOut(self, id, stationName, t):
        # route_map = {("Leyton", "Waterloo"): [total_time, count]}
        
        checkInStation, checkInTime = self.check_in_map[id]
        del self.check_in_map[id]
        
        key = (checkInStation, stationName)
        total_time = t - checkInTime
        
        if key in self.route_map:
            self.route_map[key][0] += total_time
            self.route_map[key][1] += 1
        else:
            self.route_map[key] = [total_time, 1]
        
        

    def getAverageTime(self, startStation, endStation):
        key = (startStation, endStation)
        
        return self.route_map[key][0] / self.route_map[key][1]
