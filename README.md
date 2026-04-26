# Intelligent Maintenance Agent

Takes a maintenance complaint in plain English, figures out what kind of problem it is, how urgent, and saves it to a database.

## Quick Start
```bash
python main.py
```
No installation needed. Uses only Python standard library.

## What It Does

You type: `"Motor stopped and smoke from electrical panel"`

It returns:
- **Category**: Electrical
- **Priority**: High
- **Confidence**: 1.0

And stores everything in SQLite.

## Files

| File | Purpose |
|------|---------|
| `agent.py` | Connects everything together |
| `classifier.py` | Keyword matching to find problem type |
| `priority.py` | Checks urgency words for priority |
| `database.py` | Saves and retrieves from SQLite |
| `main.py` | Run this to test it |

## How It Works

**Step 1 — Classify:** Each category has a list of keywords. Electrical = motor, circuit, breaker, smoke. Mechanical = bearing, noise, leak, grinding. Sensor = reading, signal, gauge, calibration. Highest match wins. No match = Unknown.

**Step 2 — Prioritize:** Checks for urgent words. "Emergency", "stopped", "fire" = High. "Issue", "warning", "error" = Medium. Everything else = Low. Electrical issues get automatic boost.

**Step 3 — Store:** Saves to `maintenance.db` with timestamp.

**Step 4 — Return:** Clean JSON response.

## Sample Inputs and Outputs

| Input | Category | Priority |
|-------|----------|----------|
| Motor stopped and smoke from panel | Electrical | High |
| Temperature sensor erratic readings | Sensor | Medium |
| Squeaking noise from pump bearing | Mechanical | Low |
| Circuit breaker tripping, line halted | Electrical | High |
| Oil leak from hydraulic seal | Mechanical | Low |
| Flow meter not sending signal | Sensor | Low |
| Gearbox grinding, needs attention now | Mechanical | Medium |
| Routine check on pressure gauge | Sensor | Low |

**JSON output:**

```json
{
  "complaint_id": 1,
  "issue_category": "Electrical",
  "priority_level": "High",
  "confidence_score": 1.0
}
