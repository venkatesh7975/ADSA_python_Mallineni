class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        def units(box):
            return box[1]

        boxTypes.sort(key=units, reverse=True)

        total = 0

        for box in boxTypes:

            boxes = box[0]
            unitsPerBox = box[1]

            if boxes <= truckSize:
                total += boxes * unitsPerBox
                truckSize -= boxes
            else:
                total += truckSize * unitsPerBox
                break

        return total