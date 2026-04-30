class Solution:
    def sortFeatures(self, features: List[str], responses: List[str]) -> List[str]:
        counts = {feature: 0 for feature in features}
        for response in responses:
            words = set(response.split())
            for feature in features:
                if feature in words:
                    counts[feature] += 1
        sorted_features = sorted(features, key=lambda x: (-counts[x], features.index(x)))
        return sorted_features