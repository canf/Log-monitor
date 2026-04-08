import time

LOG_FILE = "../logs/sample.log"
KEYWORDS = ["error", "failed", "critical", "timeout"]
THRESHOLD = 3

def analyze_logs():
    count = 0

    with open(LOG_FILE, "r") as f:
        for line in f:
            for keyword in KEYWORDS:
                if keyword in line.lower():
                    count += 1

    return count

def follow_log():
    with open(LOG_FILE, "r") as f:
        f.seek(0, 2)  # go to end of file

        while True:
            line = f.readline()
            if not line:
                time.sleep(1)
                continue

            for keyword in KEYWORDS:
                if keyword in line.lower():
                    print(f"[ALERT] {line.strip()}")

def main():
    print("Scanning logs...")
    issues = analyze_logs()

    print(f"Total issues found: {issues}")

    if issues >= THRESHOLD:
        print("ALERT: High number of errors detected!")
    else:
        print("System looks healthy.")
        
    print("Starting real-time monitoring...")
    follow_log()


if __name__ == "__main__":
    main()