# checks/service_check.py

import subprocess

def check_services():

    findings = []

    services = [
        "telnet",
        "rsh",
        "rlogin",
        "vsftpd"
    ]

    for service in services:

        result = subprocess.run(
            ["systemctl", "is-active", service],
            capture_output=True,
            text=True
        )

        if "active" in result.stdout:

            findings.append({
                "vulnerability": f"Insecure Service Running ({service})",
                "severity": "High",
                "location": service,
                "mitigation": "Disable and remove service"
            })

    return findings