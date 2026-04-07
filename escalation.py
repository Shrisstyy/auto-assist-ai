from config import ESCALATION_KEYWORDS

def check_escalation(query):
    for word in ESCALATION_KEYWORDS:
        if word.lower() in query.lower():
            return True
    return False

def assign_agent():
    return {
        "status": "Escalated",
        "assigned_to": "Tech Support Agent",
        "message": "Your issue has been assigned to a human agent."
    }