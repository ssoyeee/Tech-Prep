from collections import defaultdict
class Solution:
    def alertNames(self, keyName: list[str], keyTime: list[str]) -> list[str]:
        hashmap = defaultdict(list)
        
        # keyTime 10:00 -> 600
        # keyName[i] : keyTime[i]
        for i, name in enumerate(keyName):
            hour, minute = keyTime[i].split(":")
            total_minutes = int(hour)*60 + int(minute)
            hashmap[name].append(total_minutes)

        alert = []

        for name, times in hashmap.items():
            times.sort()

            for i in range(len(times)-2):
                window = times[i+2]-times[i]
                if window <= 60:
                    alert.append(name)
                    break
        return sorted(alert)