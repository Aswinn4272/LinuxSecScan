# checks/password_policy.py

def check_password_policy():

    print("Checking password policy...")
    
    findings = []

    try:

        with open("/etc/login.defs") as f:
            content = f.read()

        if "PASS_MAX_DAYS   99999" in content:

            findings.append({
                "vulnerability": "Password Expiry Disabled",
                "severity": "Medium",
                "location": "/etc/login.defs",
                "mitigation": "Set PASS_MAX_DAYS to 90"
            })

    except Exception:
        pass

    return findings