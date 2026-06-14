# checks/ssh_check.py

def check_ssh():

    findings = []

    try:
        with open("/etc/ssh/sshd_config") as f:
            config = f.read()

        if "PermitRootLogin yes" in config:
            findings.append({
                "vulnerability": "Root Login Enabled",
                "severity": "High",
                "location": "/etc/ssh/sshd_config",
                "mitigation": "Set PermitRootLogin no"
            })

        if "PasswordAuthentication yes" in config:
            findings.append({
                "vulnerability": "Password Authentication Enabled",
                "severity": "Medium",
                "location": "/etc/ssh/sshd_config",
                "mitigation": "Use key-based authentication"
            })

    except Exception as e:
        print(e)

    return findings