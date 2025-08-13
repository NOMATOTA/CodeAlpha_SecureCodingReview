\# Findings – Secure Coding Review



\## 1) SQL Injection

\- File: vulnerable\_login.py

\- Evidence: string-formatted SQL query with user inputs.

\- Demo: Local injection `admin' OR '1'='1` bypasses auth.

\- Risk: Full account compromise.

\- Fix: Use parameterized queries (example in secure\_login.py).



\## 2) Plaintext Passwords

\- File: users\_vuln.db (created by create\_vuln\_db.py)

\- Evidence: Stored password `password123` as plaintext.

\- Risk: Database theft reveals passwords.

\- Fix: Use bcrypt hashing. See create\_secure\_db.py + secure\_login.py.



\## 3) Static analysis

\- Bandit report saved as bandit\_report.html



\## Recommendations

\- Enforce password complexity, rate limiting, account lockouts.

\- Use prepared statements / parameterized queries everywhere.

\- Use established authentication frameworks for real apps.



