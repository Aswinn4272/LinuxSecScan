# checks/file_perm_check.py

import subprocess

def check_permissions():

    findings = []

    try:

        cmd = [
            "find",
            "/",
            "-type",
            "f",
            "-perm",
            "-0002"
        ]

        output = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )

        files = output.stdout.splitlines()

        for file in files[:50]:

            findings.append({
                "vulnerability": "World Writable File",
                "severity": "High",
                "location": file,
                "mitigation": "Remove write permissions for others"
            })

    except Exception:
        pass

    return findings