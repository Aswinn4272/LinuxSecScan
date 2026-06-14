# scanner.py

import json
from datetime import datetime
from checks.ssh_check import check_ssh
from checks.file_perm_check import check_permissions
from checks.password_policy import check_password_policy
from checks.service_check import check_services

results = []

results.extend(check_ssh())
results.extend(check_permissions())
results.extend(check_password_policy())
results.extend(check_services())

report = {
    "scan_date": str(datetime.now()),
    "findings": results
}

filename = f"security_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

with open(filename, "w") as f:
    json.dump(report, f, indent=4)

print(f"\nReport generated: {filename}")