class TimeMap:

    def __init__(self):
        self.keys={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.keys:
            self.keys[key]=[[timestamp,value]]
        else:
            self.keys[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:

        if key in self.keys:
            array=self.keys[key]

            low=0
            high=len(array)-1

            if timestamp >= array[-1][0]:
                return array[-1][1]

            while low <= high:

                mid = (low + high)//2

                if array[mid][0]==timestamp:
                    return array[mid][1]
                
                elif mid + 1 < len(array) and array[mid+1][0] > timestamp and array[mid][0] <= timestamp:
                    return array[mid][1]
                
                elif array[mid][0] > timestamp:
                    high = mid -1
                else:
                    low = mid +1
        return ""

               









        
