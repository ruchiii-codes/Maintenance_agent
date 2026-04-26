import json
from classifier import Classifier
from priority import Priority
from database import Database


class MaintenanceAgent:
    def __init__(self, db_path="maintenance.db"):
        self.classifier = Classifier()
        self.priority = Priority()
        self.database = Database(db_path)
    
    def reset_database(self):
        """Clear all records"""
        self.database.reset()
    
    def process(self, complaint):
        category, confidence = self.classifier.classify(complaint)
        priority = self.priority.assign(complaint, category)
        record_id = self.database.save(complaint, category, priority, confidence)
        
        response = {
            "status": "success",
            "complaint_id": record_id,
            "issue_category": category,
            "priority_level": priority,
            "confidence_score": confidence,
            "summary": f"Issue classified as {category} with {priority} priority."
        }
        
        return response
    
    def process_with_details(self, complaint):
        print(f"\n📝 Complaint: {complaint}")
        result = self.process(complaint)
        print(f"   Category: {result['issue_category']}")
        print(f"   Priority: {result['priority_level']}")
        print(f"   Confidence: {result['confidence_score']}")
        print(f"   ID: {result['complaint_id']}")
        return result
    
    def get_json(self, result):
        return json.dumps(result, indent=2)
    
    def show_dashboard(self):
        stats = self.database.get_stats()
        
        print("\n" + "="*50)
        print("📊 MAINTENANCE DASHBOARD")
        print("="*50)
        print(f"Total Complaints: {stats['total']}")
        
        print("\nBy Category:")
        for cat, count in stats['categories'].items():
            bar = "█" * count
            print(f"  {cat:<12} [{count}] {bar}")
        
        print("\nBy Priority:")
        for pri, count in stats['priorities'].items():
            bar = "█" * count
            print(f"  {pri:<8} [{count}] {bar}")
        print("="*50)
    
    def show_all(self):
        records = self.database.get_all()
        print("\n📋 All Complaints:")
        for rec in records:
            print(f"  ID:{rec[0]} | {rec[2]:<12} | {rec[3]:<8} | {rec[1][:50]}...")