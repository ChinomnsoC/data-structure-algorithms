from collections import deque
from typing import Optional


class Station:
    def __init__(self, name: str):
        self.name = name
        self.neighbours = []

    def add_neighbour(self, station: "Station"):
        self.neighbours.append(station)

    def __eq__(self, other):
        return isinstance(other, Station) and self.name == other.name

    def __hash__(self):
        return hash(self.name)


class TrainMap:
    def __init__(self):
        self.stations = {}

    def add_station(self, name: str) -> "TrainMap":
        if name not in self.stations:
            self.stations[name] = Station(name)
        return self

    def get_station(self, name: str) -> Optional[Station]:
        return self.stations.get(name)

    def connect_stations(
        self, from_station: Station, to_station: Station
    ) -> "TrainMap":
        if from_station is None:
            raise ValueError("from_station is None")
        if to_station is None:
            raise ValueError("to_station is None")
        from_station.add_neighbour(to_station)
        to_station.add_neighbour(from_station)
        return self

    def shortest_path(self, from_name: str, to_name: str) -> list:
        # TODO: Implement
        start_station = self.get_station(from_name)
        end_station = self.get_station(to_name)
        
        if not start_station or not end_station:
            return []
        queue = deque([start_station])
        visited = set()
        came_from = {start_station: None}

        while queue:
            current_station = queue.popleft()
            if current_station == end_station:
                train_map = []
                current = end_station
                while current is not None:
                    train_map.append(current)
                    current = came_from[current]
                train_map.reverse()

                return train_map
            # If current == end_station → reconstruct and return path
            visited.add(current_station)
            for neighbour in current_station.neighbours:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
                    came_from[neighbour] = current_station
                    # update came from dictionary

        return []

    @staticmethod
    def convert_path_to_string(path: list) -> str:
        if not path:
            return ""
        return "->".join(station.name for station in path)


def do_tests_pass() -> bool:
    train_map = TrainMap()

    for name in [
        "King's Cross St Pancras",
        "Angel",
        "Old Street",
        "Moorgate",
        "Farringdon",
        "Barbican",
        "Russel Square",
        "Holborn",
        "Chancery Lane",
        "St Paul's",
        "Bank",
    ]:
        train_map.add_station(name)

    connections = [
        ("King's Cross St Pancras", "Angel"),
        ("King's Cross St Pancras", "Farringdon"),
        ("King's Cross St Pancras", "Russel Square"),
        ("Russel Square", "Holborn"),
        ("Holborn", "Chancery Lane"),
        ("Chancery Lane", "St Paul's"),
        ("St Paul's", "Bank"),
        ("Angel", "Old Street"),
        ("Old Street", "Moorgate"),
        ("Moorgate", "Bank"),
        ("Farringdon", "Barbican"),
        ("Barbican", "Moorgate"),
    ]

    for a, b in connections:
        train_map.connect_stations(train_map.get_station(a), train_map.get_station(b))

    expected = (
        "King's Cross St Pancras->Russel Square->Holborn->Chancery Lane->St Paul's"
    )
    result = TrainMap.convert_path_to_string(
        train_map.shortest_path("King's Cross St Pancras", "St Paul's")
    )
    print(f"Expected: {expected}")
    print(f"Got:      {result}")
    return result == expected


if __name__ == "__main__":
    if do_tests_pass():
        print("All tests pass")
    else:
        print("Tests fail")
