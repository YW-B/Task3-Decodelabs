def ask_question(question):
    answer = input(question + " (yes/no): ").strip().lower()
    return answer == "yes"


print("=== Phishing Triage Toolkit ===")

suspicious_domain = ask_question("Is the sender domain suspicious or misspelled")
reply_mismatch = ask_question("Is the reply-to address different from the sender")
urgent_language = ask_question("Does the email use urgent or manipulative language")
suspicious_link = ask_question("Does the email contain a suspicious link or odd subdomain")
sensitive_request = ask_question("Does the email ask for passwords, money, or sensitive information")

score = 0

if suspicious_domain:
    score += 1
if reply_mismatch:
    score += 1
if urgent_language:
    score += 1
if suspicious_link:
    score += 1
if sensitive_request:
    score += 1

if score <= 1:
    classification = "Safe"
    action = "Close"
elif score <= 3:
    classification = "Suspicious"
    action = "Warn User"
else:
    classification = "Malicious"
    action = "Block & Escalate"

print("\n--- Triage Result ---")
print("Risk Score:", score)
print("Classification:", classification)
print("Recommended Action:", action)