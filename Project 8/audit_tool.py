import os
import subprocess
import sys

# --- Configuration ---
# This is where we save the report
REPORT_FILE = "audit_report.txt"

def print_message(message, status="INFO"):
    """Prints a formatted message to the console and saves it to the report."""
    if status == "PASS":
        color = "\033[92m[PASS]\033[0m" # Green
    elif status == "FAIL":
        color = "\033[91m[FAIL]\033[0m" # Red
    elif status == "WARN":
        color = "\033[93m[WARN]\033[0m" # Yellow
    else:
        color = "\033[94m[INFO]\033[0m" # Blue

    full_message = f"{color} {message}"
    print(full_message)

    # Append to report file (stripping colors for text file)
    with open(REPORT_FILE, "a") as f:
        clean_message = f"[{status}] {message}\n"
        f.write(clean_message)

def audit_firewall():
    """Checks if the UFW firewall is active."""
    print_message("Checking Firewall Status...", "INFO")
    try:
        # Run the command 'ufw status'
        result = subprocess.run(["sudo", "ufw", "status"], capture_output=True, text=True)
        if "Status: active" in result.stdout:
            print_message("Firewall is ACTIVE.", "PASS")
        else:
            print_message("Firewall is INACTIVE. Recommendation: Enable ufw.", "FAIL")
    except Exception as e:
        print_message(f"Error checking firewall: {e}", "WARN")

def audit_ssh():
    """Checks if SSH Root Login is disabled."""
    print_message("Checking SSH Configuration...", "INFO")
    try:
        # We need to read the config file
        with open("/etc/ssh/sshd_config", "r") as f:
            content = f.read()
            
        # Check for 'PermitRootLogin no'
        if "PermitRootLogin no" in content:
            print_message("SSH Root Login is DISABLED.", "PASS")
        else:
            print_message("SSH Root Login is ENABLED (or not set). Recommendation: Disable it.", "FAIL")
    except FileNotFoundError:
        print_message("SSH config file not found. Is SSH installed?", "WARN")
        
def audit_ip_forwarding():
    """Checks if IP Forwarding is disabled."""
    print_message("Checking IP Forwarding...", "INFO")
    try:
        # Read the value from the system file
        with open("/proc/sys/net/ipv4/ip_forward", "r") as f:
            value = f.read().strip()
            
        if value == "0":
            print_message("IP Forwarding is DISABLED.", "PASS")
        else:
            print_message("IP Forwarding is ENABLED. Recommendation: Set net.ipv4.ip_forward = 0", "FAIL")
    except Exception as e:
        print_message(f"Error checking IP forwarding: {e}", "WARN")

# --- Main Execution ---
if __name__ == "__main__":
    # Clear the report file if it exists
    if os.path.exists(REPORT_FILE):
        os.remove(REPORT_FILE)
    
    print("\nStarting Linux Hardening Audit...\n" + "="*40)
    
    # Run Checks
    audit_firewall()
    audit_ssh()
    audit_ip_forwarding()
    
    print("\n" + "="*40 + "\nAudit Complete! Report saved to audit_report.txt")
