import json
from agent import MaintenanceAgent


def main():
    # Create agent
    agent = MaintenanceAgent()
    
    # Reset database for clean start
    agent.reset_database()
    
    # Test complaints
    complaints = [
        "The main motor has stopped and smoke coming from electrical panel!",
        "Temperature sensor showing erratic readings, needs calibration urgently",
        "Squeaking noise from pump bearing, getting worse",
        "Circuit breaker keeps tripping, production line completely halted!",
        "Minor oil leak from hydraulic cylinder seal",
        "Flow meter transmitter not sending signal to control room",
        "Gearbox making loud grinding noise, needs immediate attention",
        "Routine check on pressure gauge, everything normal"
    ]
    
    print("="*50)
    print("🤖 INTELLIGENT MAINTENANCE AGENT")
    print("="*50)
    
    # Process each complaint
    first_result = None
    for complaint in complaints:
        result = agent.process_with_details(complaint)
        if first_result is None:
            first_result = result
    
    # Show JSON output example
    print("\n" + "="*50)
    print("📋 SAMPLE JSON OUTPUT")
    print("="*50)
    print(agent.get_json(first_result))
    
    # Show dashboard
    agent.show_dashboard()
    
    # Show all records
    agent.show_all()


if __name__ == "__main__":
    main()