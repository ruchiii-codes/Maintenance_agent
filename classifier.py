class Classifier:
    def __init__(self):
        self.keywords = {
            "Electrical": [
                "power", "electric", "voltage", "circuit", "breaker",
                "wiring", "motor", "spark", "surge", "shorted", "overload",
                "panel", "smoke", "burning", "cable", "fuse"
            ],
            "Mechanical": [
                "bearing", "gear", "belt", "shaft", "vibration", "noise",
                "leak", "broken", "crack", "wear", "grinding", "squeaking",
                "pump", "valve", "seal", "piston", "loose"
            ],
            "Sensor": [
                "sensor", "reading", "calibration", "probe", "signal",
                "display", "gauge", "measurement", "transmitter", "detector",
                "temperature", "pressure", "flow", "level"
            ]
        }
    
    def classify(self, complaint):
        complaint = complaint.lower()
        scores = {}
        
        for category, keywords in self.keywords.items():
            score = sum(1 for word in keywords if word in complaint)
            scores[category] = score
        
        max_score = max(scores.values())
        
        if max_score == 0:
            return "Unknown", 0.0
        
        best_category = max(scores, key=scores.get)
        total = sum(scores.values())
        confidence = round(scores[best_category] / total, 2)
        
        return best_category, confidence