import csv
from collections import Counter, defaultdict

# Configuration Constants
LOG_FILE = "D:\\CODING\\Python Assignment\\sample.log"  # Path to the log file
OUTPUT_CSV = "D:\\CODING\\Python Assignment\\log_analysis_results.csv"  # Output report path
FAILED_LOGIN_THRESHOLD = 1  # Minimum failed login attempts to flag as suspicious


def parse_log_file(file_path):
    # Initialize counters and tracking dictionaries
    ip_requests = Counter()
    endpoint_requests = Counter()
    failed_logins = defaultdict(int)

    # Read and process log file line by line
    with open(file_path, "r") as file:
        for line in file:
            # Skip malformed log entries
            parts = line.split()
            if len(parts) < 9:
                continue

            # Extract key log entry components
            ip = parts[0]
            request_type = parts[5].strip('"')
            endpoint = parts[6]
            status_code = parts[8]

            # Increment request counters
            ip_requests[ip] += 1
            endpoint_requests[endpoint] += 1

            # Track failed login attempts
            if status_code == "401" or "Invalid credentials" in line:
                failed_logins[ip] += 1

    return ip_requests, endpoint_requests, failed_logins


def write_to_csv(ip_requests, most_accessed, failed_logins, file_path):
    with open(file_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        # Write IP Request Counts section
        writer.writerow(["IP Address", "Request Count"])
        writer.writerows(ip_requests)
        writer.writerow([])  # Blank line separator

        # Write Most Accessed Endpoint section
        writer.writerow(["Most Accessed Endpoint"])
        writer.writerow(["Endpoint", "Access Count"])
        writer.writerow(most_accessed)
        writer.writerow([])  # Blank line separator

        # Write Suspicious Activity section
        writer.writerow(["Suspicious Activity Detected"])
        writer.writerow(["IP Address", "Failed Login Count"])
        writer.writerows(failed_logins)


def main():
    # Parse log file and extract metrics
    ip_requests, endpoint_requests, failed_logins = parse_log_file(LOG_FILE)

    # Sort and analyze results
    sorted_ip_requests = sorted(ip_requests.items(), key=lambda x: x[1], reverse=True)
    most_accessed = max(endpoint_requests.items(), key=lambda x: x[1])

    # Identify suspicious login activities
    suspicious_activity = [
        (ip, count)
        for ip, count in failed_logins.items()
        if count > FAILED_LOGIN_THRESHOLD
    ]
    suspicious_activity.sort(key=lambda x: x[1], reverse=True)

    # Display results in console
    print("IP Address Request Counts:")
    print("\n".join([f"{ip} {count}" for ip, count in sorted_ip_requests]))

    print("\nMost Frequently Accessed Endpoint:")
    print(f"{most_accessed[0]} (Accessed {most_accessed[1]} times)")

    print("\nSuspicious Activity Detected:")
    print("\n".join([f"{ip} {count}" for ip, count in suspicious_activity]))

    # Save detailed results to CSV
    write_to_csv(sorted_ip_requests, most_accessed, suspicious_activity, OUTPUT_CSV)
    print(f"\nDetailed results saved to {OUTPUT_CSV}")


# Ensure script is run directly
if __name__ == "__main__":
    main()
