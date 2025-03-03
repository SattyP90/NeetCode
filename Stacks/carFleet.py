class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #create a list of tuples with the position and time it will take to reach the target
        cars = sorted([(p, (target - p) / s) for p, s in zip(position, speed)])
        fleets = 0
        while len(cars) > 1:
            lead = cars.pop()
            if lead[1] < cars[-1][1]:
                fleets += 1
            else:
                cars[-1] = lead
        return fleets + bool(cars)
    