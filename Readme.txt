HR POLICY CHATBOT (OFFLINE FLASK PROJECT)
=========================================

PROJECT OVERVIEW
----------------
The HR Policy Chatbot is an offline intelligent assistant built using Flask (Python) for the backend and HTML, CSS, and JavaScript for the frontend.
It helps employees ask questions related to HR policies such as working hours, leave rules, and HR contact details.
The chatbot can also draft professional HR emails (for leave, work-from-home, or salary inquiries).
This chatbot works fully offline without using any external APIs. All responses come from a local HR policy file (hr_policy.txt).

FEATURES
--------
1. Works completely offline (no API keys required)
2. Keyword-based HR policy detection
3. Auto email drafting for leave, WFH, and salary inquiries
4. User-friendly chat interface
5. Lightweight and fast setup

PROJECT STRUCTURE
-----------------
hrchatbot/
│
├── backend/
│   ├── app.py              - Flask backend server
│   ├── utils.py            - Logic for HR policy and email generation
│   ├── hr_policy.txt       - HR policies text file
│
├── frontend/
│   ├── index.html          - Chat interface
│   ├── style.css           - Chat styling
│   ├── app.js              - Frontend logic (connects to Flask)
│
├── .venv/                  - Virtual environment (auto-created)
│
└── README.txt              - Documentation (this file)

REQUIREMENTS
------------
- Python 3.8 or higher
- Flask (latest)
- Flask-CORS (latest)
- Any text editor (VS Code recommended)
- Web browser (Google Chrome recommended)

INSTALLATION STEPS
------------------
1. Create the project folder:
   cd Documents
   mkdir hrchatbot
   cd hrchatbot

2. Create a virtual environment:
   python -m venv .venv

3. Activate the virtual environment:
   For Windows PowerShell:
   .\.venv\Scripts\activate

4. Install required packages:
   pip install flask flask-cors

5. Run the Flask backend:
   cd backend
   python app.py
   (You should see the message: Running on http://127.0.0.1:5000/)

6. Run the frontend (HTML):
   Open a new terminal, navigate to the frontend folder:
   cd frontend
   python -m http.server 5501

7. Open your browser and go to:
   http://127.0.0.1:5501

HOW TO USE
----------
1. Open the chatbot page in your browser.
2. Type questions such as:
   - What are the working hours?
   - How many annual leaves do I have?
   - Draft an email for 3 days of leave.
   - How can I contact HR?
3. The chatbot will reply with:
   - Relevant policy details, or
   - A drafted HR email, or
   - Both, depending on the question.

HR_POLICY.TXT FORMAT
--------------------
Your hr_policy.txt should be formatted into clear sections separated by blank lines:

1. Working Hours
- Standard working hours are 9:00 AM to 6:00 PM, Monday to Friday.
- Employees must be punctual and inform their manager in case of delay.

2. Leave Policy
- Annual leave: 20 days per year.
- Sick leave: 10 days with medical certificate.
- Emergency leave must be reported to your manager immediately.

3. HR Contact
- Email: hr@company.com
- Phone: +91 9876543210
- Office: 3rd Floor, Corporate Block

4. Salary and Benefits
- Salary credited on the last working day of the month.
- Bonus and reimbursements are managed through the HR portal.

EXAMPLE QUESTIONS
-----------------
1. What are the working hours?
2. How many annual leaves do I have?
3. How can I contact HR?
4. Draft an email to request 3 days of leave.
5. Write a WFH email.
6. Tell me about the leave policy and draft an email for it.

SAMPLE EMAIL OUTPUT
-------------------
Subject: Leave Request (3 Days)

Dear HR Team,
I would like to request 3 days of leave from 10th to 12th October due to personal reasons.
Kindly approve my leave.

Best regards,
[Your Name]
[Your Department]

CUSTOMIZATION IDEAS
-------------------
- Replace the hr_policy.txt with your real company policies.
- Add more categories (attendance, code of conduct, etc.).
- Connect to a real HR database in the future.
- Add voice input or advanced NLP if desired.

TROUBLESHOOTING
---------------
Issue: Error connecting to server.
Fix: Ensure BACKEND_URL in app.js points to http://127.0.0.1:5000/chat

Issue: HR policy repeating.
Fix: Add blank lines between sections in hr_policy.txt

Issue: Flask not running.
Fix: Ensure the virtual environment is activated and you are inside the backend folder.

PROJECT OUTCOME
---------------
A fully offline HR chatbot that:
- Answers HR-related queries from a local file.
- Drafts professional HR emails instantly.
- Runs locally on any system without internet access.
