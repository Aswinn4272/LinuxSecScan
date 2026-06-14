# LinuxSecScan
LinuxSecScan is a Python-based CLI security auditing tool for Linux systems. It detects vulnerabilities, insecure configurations, weak permissions, and risky services, then generates detailed reports with severity ratings, affected locations, and remediation recommendations to improve system security and compliance.

**LinuxSecScan – Linux Security Auditing and Vulnerability Assessment Tool**
LinuxSecScan is a Python-based command-line security auditing tool designed to identify security vulnerabilities, insecure configurations, and compliance issues on Linux systems. The tool performs automated security assessments by analyzing system configurations, file permissions, authentication settings, running services, and operating system hardening controls.

The primary objective of LinuxSecScan is to help system administrators, security engineers, penetration testers, and auditors quickly identify security weaknesses and generate actionable remediation reports.

**Key Features**
Automated Linux security auditing
Detection of common security misconfigurations
SSH hardening assessment
File and directory permission analysis
User account and password policy validation
Insecure service detection
System hardening verification
Vulnerability severity classification (Critical, High, Medium, Low)
Detailed findings with affected locations
Mitigation and remediation recommendations
JSON, HTML, and PDF report generation
Modular plugin-based architecture for custom security checks
Lightweight and easy-to-deploy CLI interface
Security Checks

**LinuxSecScan can perform assessments including:**
SSH configuration review
Root login detection
Password authentication checks
World-writable file discovery
SUID/SGID file enumeration
Weak password policy identification
Insecure service detection (Telnet, FTP, RSH, etc.)
Firewall configuration validation
User and group auditing
Package and software inventory analysis
Operating system hardening verification
CIS Benchmark compliance checks (future enhancement)
CVE-based vulnerability assessment (future enhancement)
Reporting

**The tool generates comprehensive security reports containing:**
Vulnerability name
Severity rating
Affected file, service, or configuration
Technical description
Recommended mitigation steps
Scan timestamp
Overall security assessment summary
Use Cases
Security Audits
Vulnerability Assessments
System Hardening Reviews
Compliance Verification
Security Baseline Validation
Lab and Research Environments
Continuous Security Monitoring

**Disclaimer**
LinuxSecScan is intended for authorized security testing, auditing, and educational purposes only. Users are responsible for ensuring they have proper authorization before scanning or assessing any system.

