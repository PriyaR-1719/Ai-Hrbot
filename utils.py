import os

# Load HR policy chunks from file
def load_policy(path="hr_policy.txt"):
    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, path)

    with open(full_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Split by double newlines to get sections
    chunks = [p.strip() for p in text.split("\n\n") if p.strip()]
    return chunks

policy_chunks = load_policy()

# HR categories keywords
hr_keywords = {
    "working hours": ["working hours", "office hours", "time", "schedule"],
    "leave": ["leave", "annual leave", "sick leave", "vacation", "holiday", "emergency leave"],
    "contact": ["contact", "hr", "manager", "email", "phone"],
    "salary": ["salary", "pay", "bonus", "benefits", "reimbursement"]
}

# Map each policy chunk to its category based on headings
policy_mapping = {
    "working hours": "",
    "leave": "",
    "contact": "",
    "salary": ""
}

for chunk in policy_chunks:
    lower_chunk = chunk.lower()
    if "working hours" in lower_chunk:
        policy_mapping["working hours"] = chunk
    elif "leave policy" in lower_chunk:
        policy_mapping["leave"] = chunk
    elif "hr contact" in lower_chunk:
        policy_mapping["contact"] = chunk
    elif "salary and benefits" in lower_chunk:
        policy_mapping["salary"] = chunk

# Email templates
email_templates = {
    "leave_request": (
        "Subject: Leave Request\n\n"
        "Dear [Manager Name],\n\n"
        "I would like to request leave from [start date] to [end date]. "
        "Please let me know if this is approved.\n\n"
        "Thank you.\nBest regards,\n[Your Name]"
    ),
    "wfh_request": (
        "Subject: Work From Home Request\n\n"
        "Dear [Manager Name],\n\n"
        "I would like to request to work from home on [date(s)]. "
        "Please let me know if this is approved.\n\n"
        "Thank you.\nBest regards,\n[Your Name]"
    ),
    "salary_query": (
        "Subject: Salary/Benefits Inquiry\n\n"
        "Dear HR Team,\n\n"
        "I would like to inquire about [salary/bonus/benefits/reimbursement]. "
        "Please provide the details at your earliest convenience.\n\n"
        "Thank you.\nBest regards,\n[Your Name]"
    )
}

# Keywords to detect which email to draft
email_keywords = {
    "leave_request": ["leave", "day off", "vacation", "annual leave", "sick leave"],
    "wfh_request": ["work from home", "wfh", "remote work", "home office"],
    "salary_query": ["salary", "pay", "bonus", "benefits", "reimbursement"]
}

def generate_response(prompt):
    prompt_lower = prompt.lower()

    # 1. Detect email type automatically
    for email_type, keywords in email_keywords.items():
        if any(k in prompt_lower for k in keywords):
            if "draft" in prompt_lower or "email" in prompt_lower or "write" in prompt_lower:
                return email_templates[email_type]

    # 2. Check HR policy by category keywords
    for category, keywords in hr_keywords.items():
        if any(k in prompt_lower for k in keywords):
            if policy_mapping[category]:
                return policy_mapping[category]

    # 3. Default response if no match
    return "Sorry, I don't have information on that. Please ask HR directly."
