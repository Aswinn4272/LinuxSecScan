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

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

report = {
    "scan_date": str(datetime.now()),
    "total_findings": len(results),
    "findings": results
}

# Save JSON Report
json_file = f"security_report_{timestamp}.json"

with open(json_file, "w") as f:
    json.dump(report, f, indent=4)

# Generate HTML Report
html_file = f"security_report_{timestamp}.html"

severity_colors = {
    "Critical": "#dc3545",
    "High": "#fd7e14",
    "Medium": "#ffc107",
    "Low": "#28a745"
}

rows = ""

for finding in results:

    color = severity_colors.get(
        finding["severity"],
        "#6c757d"
    )

    rows += f"""
    <tr>
        <td>{finding['vulnerability']}</td>
        <td style="color:{color};font-weight:bold;">
            {finding['severity']}
        </td>
        <td>{finding['location']}</td>
        <td>{finding['mitigation']}</td>
    </tr>
    """

html = f"""
<!DOCTYPE html>
<html>
<head>
<title>LinuxSecScan Report</title>

<style>
body {{
    font-family: Arial, sans-serif;
    margin: 40px;
    background-color: #f4f4f4;
}}

h1 {{
    color: #333;
}}

.summary {{
    background: white;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 5px;
}}

table {{
    width: 100%;
    border-collapse: collapse;
    background: white;
}}

th {{
    background: #343a40;
    color: white;
    padding: 12px;
}}

td {{
    padding: 10px;
    border: 1px solid #ddd;
}}

tr:nth-child(even) {{
    background: #f9f9f9;
}}
</style>

</head>

<body>

<h1>LinuxSecScan Security Report</h1>

<div class="summary">
<p><strong>Scan Date:</strong> {report['scan_date']}</p>
<p><strong>Total Findings:</strong> {report['total_findings']}</p>
</div>

<table>
<tr>
<th>Vulnerability</th>
<th>Severity</th>
<th>Location</th>
<th>Mitigation</th>
</tr>

{rows}

</table>

</body>
</html>
"""

with open(html_file, "w") as f:
    f.write(html)

print(f"[+] JSON Report: {json_file}")
print(f"[+] HTML Report: {html_file}")