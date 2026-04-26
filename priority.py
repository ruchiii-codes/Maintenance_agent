class Priority:
    def __init__(self):
        self.high_words = [
            "urgent", "critical", "emergency", "immediate", "danger",
            "hazard", "stopped", "halted", "shutdown", "failure",
            "safety", "fire", "smoke", "explosion", "catastrophic",
            "complete", "serious", "severe"
        ]
        
        self.medium_words = [
            "issue", "problem", "error", "fault", "warning",
            "abnormal", "unusual", "irregular", "intermittent",
            "soon", "degrading", "declining", "attention"
        ]
    
    def assign(self, complaint, category):
        complaint = complaint.lower()
        
        high_count = sum(1 for word in self.high_words if word in complaint)
        medium_count = sum(1 for word in self.medium_words if word in complaint)
        
        # Electrical issues are priority
        if category == "Electrical":
            high_count += 1
        
        if high_count >= 2:
            return "High"
        elif high_count >= 1 or medium_count >= 2:
            return "Medium"
        elif medium_count >= 1:
            return "Medium"
        else:
            return "Low"