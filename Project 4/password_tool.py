import zxcvbn
import getpass
import itertools

def check_password_strength():
    print("\n=== 🛡️ Password Strength Analyzer ===")
    user_pwd = getpass.getpass("Enter a password to test (input hidden): ")
    if not user_pwd:
        print("[-] No password entered.")
        return

    results = zxcvbn.zxcvbn(user_pwd)
    score = results['score']
    crack_time = results['crack_times_display']['offline_fast_hashing_1e10_per_second']
    feedback = results['feedback']['warning']
    
    print("\n[*] Analyzing Password Entropy...")
    print("-" * 45)
    print(f"Strength Score: {score} / 4")
    print(f"Estimated Time to Crack: {crack_time}")
    
    if score == 0:
        print("Verdict: 🚨 TERRIBLE (Instantly crackable)")
    elif score == 1:
        print("Verdict: ⚠️ WEAK (Easily crackable)")
    elif score == 2:
        print("Verdict: 🟡 FAIR (Might take some time)")
    elif score == 3:
        print("Verdict: 🟢 STRONG (Hard to crack)")
    elif score == 4:
        print("Verdict: 🛡️ VERY STRONG (Practically uncrackable)")
        
    if feedback:
        print(f"Hacker Insight: {feedback}")
    print("-" * 45)

def generate_wordlist():
    print("\n=== 🥷 Custom Wordlist Generator ===")
    print("Enter target details to generate an attack dictionary.")
    
    name = input("Target's First Name: ").strip().lower()
    pet = input("Target's Pet Name: ").strip().lower()
    year = input("Important Year (e.g., 1999): ").strip()
    
    # Filter out empty inputs
    words = [w for w in [name, pet, year] if w] 
    
    if not words:
        print("[-] No data provided.")
        return

    print("\n[*] Generating combinations and leetspeak...")
    wordlist = set()
    
    # 1. Base words and capitalized versions
    for w in words:
        wordlist.add(w)
        wordlist.add(w.capitalize())
    
    # 2. Combine pairs (e.g., name+year, pet+year)
    for pair in itertools.permutations(words, 2):
        combined = "".join(pair)
        wordlist.add(combined)
        wordlist.add(combined.capitalize())

    # 3. Leetspeak variations (e.g., changing 'a' to '@')
    leet_map = {'a': '@', 'e': '3', 'i': '1', 'o': '0', 's': '$'}
    leet_words = set()
    for word in wordlist:
        leet_word = word
        for normal, leet in leet_map.items():
            leet_word = leet_word.replace(normal, leet)
        leet_words.add(leet_word)
    
    # Combine all unique words
    final_wordlist = wordlist.union(leet_words)
    
    # 4. Save to a text file
    filename = "custom_wordlist.txt"
    with open(filename, "w") as f:
        for w in sorted(final_wordlist):
            f.write(w + "\n")
            
    print(f"[+] Success! Generated {len(final_wordlist)} unique passwords.")
    print(f"[+] Wordlist exported to: {filename} 📝")

if __name__ == "__main__":
    while True:
        print("\n=== 💀 Red Team Toolkit ===")
        print("1. Password Strength Analyzer")
        print("2. Custom Wordlist Generator")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ")
        if choice == '1':
            check_password_strength()
        elif choice == '2':
            generate_wordlist()
        elif choice == '3':
            print("[*] Exiting toolkit. Goodbye!")
            break
        else:
            print("[-] Invalid choice.")
