import re
import random
import datetime

def generate_log_entry(ip_address, url, status_code):
    """Generates a sample log entry."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"{timestamp} - {ip_address} - \"GET {url} HTTP/1.1\" {status_code}\n"

def generate_log_file(filename="access.log", num_entries=100):
    """Generates a sample log file."""
    ip_addresses = ["192.168.1." + str(i) for i in range(1, 25)]
    urls = ["/page1", "/page2", "/page3", "/images/logo.png", "/api/data"]
    status_codes = [200, 404, 500, 301]

    with open(filename, "w") as f:
        for _ in range(num_entries):
            ip = random.choice(ip_addresses)
            url = random.choice(urls)
            status = random.choice(status_codes)
            f.write(generate_log_entry(ip, url, status))


def analyze_log_file(filename="access.log"):
    """Analyzes a log file and extracts information."""

    try:
        with open(filename, "r") as f:
            log_lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: Log file '{filename}' not found.")
        return

    error_count = 0
    unique_ips = set()
    url_counts = {}

    for line in log_lines:
        match = re.search(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \"GET (.+) HTTP/1.1\" (\d+)", line)
        if match:
            timestamp, ip, url, status_code = match.groups()
            unique_ips.add(ip)

            if url in url_counts:
                url_counts[url] += 1
            else:
                url_counts[url] = 1

            if int(status_code) >= 400:
                error_count += 1
        else:
            print(f"Warning: Invalid log format in line: {line.strip()}")

    print(f"Total Errors (4xx and 5xx): {error_count}")
    print(f"Unique IP Addresses: {len(unique_ips)}")
    print("URL Access Counts:")
    for url, count in url_counts.items():
        print(f"  {url}: {count}")

# Generate a sample log file (uncomment to create the file)
generate_log_file()

# Analyze the log file
analyze_log_file()
