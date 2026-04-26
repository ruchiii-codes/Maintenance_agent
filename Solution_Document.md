# Solution Document

## Assumptions

- Complaints are in English, short, and about one issue at a time
- Keywords are enough to figure out the problem type
- Electrical problems are riskier than mechanical ones
- Production stoppage = urgent, routine checks = not
- Single user, local machine, SQLite is fine for now

## Trade-offs

**Keywords vs ML:** Keywords work instantly with no training data. Downside — won't understand synonyms like "broken" vs "damaged". Would switch to ML with enough data.

**SQLite vs PostgreSQL:** SQLite needs zero setup. Downside — can't handle multiple users writing at once. Would upgrade for production.

**Hardcoded lists vs config file:** Kept keywords in code to keep things simple. A JSON config would let non-devs update it without touching code.

## What I'd Improve

**Soon:**
- Add input validation
- Move keywords to a config file
- Flag low confidence results for human review

**Later:**
- Build a REST API
- Switch to PostgreSQL
- Email alerts for high priority
- Train on real complaint data

**Eventually:**
- Multi-language support
- Predictive maintenance
- Mobile app for technicians