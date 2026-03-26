# **Bus Tracker (IDB)**

# Implement a class with:
# - `constructor(stationList, busLocations)` — `stationList` is stations separated by `-`
# e.g. `"1-2-3-4-5"`. `busLocations` is a list of `(busId, stationId)` pairs. Buses move left to right only.
# - `nearestBusToStation(stationId)` — return how many stops away the nearest bus is to the given station
# - `getBusLocation(busId)` — return the station the bus is currently at

# ```python
# stationList = "1-2-3-4-5"
# busLocations = [(1, "3"), (2, "1")]

# getBusLocation(1) → "3"
# nearestBusToStation("4") → 1  # bus 1 is at station 3, one stop away
# ```


class BusTracker:
    def __init__(self, stationList, busLocations):
        # split string by -
        self.listOfStations = []
        # {bus_id: "location"}
        self.busLocationsMap = {}
        # {"station_id": index in list}
        self.stationIndexMap = {}

        if not stationList or not busLocations:
            return

        self.listOfStations = stationList.split("-")

        for i, station in enumerate(self.listOfStations):
            self.stationIndexMap[station] = i

        for busLocation in busLocations:
            busId, stationId = busLocation[0], busLocation[1]

            self.busLocationsMap[busId] = stationId
    
    def getBusLocation(self, busId):
        if not busId or busId not in self.busLocationsMap:
            return
        
        return self.busLocationsMap[busId]
    
    def nearestBusToStation(self, stationId):
        if not stationId or stationId not in self.stationIndexMap:
            return
        
        position_of_station = self.stationIndexMap[stationId]
        
        smallest_positive_difference = float('inf')
        bus_with_smallest_positive_difference = float('inf')
        
        for bus, station in self.busLocationsMap.items():
            bus_position_index_in_station_map = self.stationIndexMap[station]
            
            if bus_position_index_in_station_map <= position_of_station:
                distance = position_of_station - bus_position_index_in_station_map
                
                if distance < smallest_positive_difference:
                    smallest_positive_difference = distance
                    bus_with_smallest_positive_difference = bus
        
        return bus_with_smallest_positive_difference
        
stationList = "1-2-3-4-5"
busLocations = [(1, "3"), (2, "1")]

# getBusLocation(1) → "3"
# nearestBusToStation("4") → 1  # bus 1 is at station 3, one stop away

bus_tracker = BusTracker(stationList, busLocations)

print(bus_tracker.getBusLocation(1))
print(bus_tracker.nearestBusToStation("4"))