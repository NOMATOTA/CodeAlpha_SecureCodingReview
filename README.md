# Secure Coding Review – Python Login Script

## Overview
This repo demonstrates a vulnerable login implementation (SQL injection + plaintext passwords) and a fixed implementation (parameterized queries + bcrypt password hashing). It was created for the CodeAlpha Cyber Security Internship secure coding review task.

## How to run
1. Create virtualenv and install dependencies:

```
python -m venv venv
venv\Scripts\activate # Windows
pip install -r requirements.txt
```


2. Create demo databases:

```
python create_vuln_db.py
python create_secure_db.py
```

3. Run the vulnerable example:

```
python vulnerable_login.py
```

4. Run the secure example:

```
python secure_login.py
```

## Issues found
- SQL Injection (vulnerable_login.py)
- Plaintext password storage (users_vuln.db)

## Fixes implemented
- Use parameterized queries
- Store hashed passwords with bcrypt

## Tools used
- Manual inspection
- Bandit static analysis (report: bandit_report.html)

