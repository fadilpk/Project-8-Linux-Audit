import re
import matplotlib.pyplot as plt
from collections import Counter

def analyze_ssh_logs(file_path):
    print(f"[*] Starting Intrusion Detection on: {file_path}")
    print("-" * 50)
    
    failed_attempts = []
    pattern = re.compile(r"Failed password for .* from ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)")
    
    try:
        with open(file_path, "r") as file:
            for line in file:
                match = pattern.search(line)
                if match:
                    failed_attempts.append(match.group(1))
                    
        ip_counts = Counter(failed_attempts)
        
        print("[+] SSH Brute-Force Report:")
        for ip, count in ip_counts.items():
            if count >= 3:
                print(f"🚨 ALERT: Brute-Force detected from IP {ip} ({count} failed attempts!)")
            else:
                print(f"⚠️ Warning: Single failed attempt from IP {ip}")
        
        # --- NEW: GENERATE THE GRAPH ---
        if ip_counts:
            print("-" * 50)
            print("[*] Generating visual report...")
            ips = list(ip_counts.keys())
            counts = list(ip_counts.values())
            
            plt.figure(figsize=(8, 5))
            # Color the bars: Red for brute force, Orange for warnings
            colors = ['red' if c >= 3 else 'orange' for c in counts]
            plt.bar(ips, counts, color=colors)
            
            plt.title("Intrusion Detection: SSH Failed Logins")
            plt.xlabel("Attacker IP Address")
            plt.ylabel("Number of Failed Attempts")
            
            # Save the graph as an image for your final report
            plt.savefig("intrusion_graph.png")
            print("[+] Graph saved successfully as 'intrusion_graph.png' 📊")
            
            # Pop open the graph on the screen
            plt.show()

    except FileNotFoundError:
        print("[-] Error: Log file not found.")

if __name__ == "__main__":
    analyze_ssh_logs("sample_auth.log")
    print("-" * 50)
    print("[*] Scan Complete.")
