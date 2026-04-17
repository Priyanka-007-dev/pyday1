# Given logs
logs = [
    "ERROR DISK FULL",
    "INFO STARTED",
    "ERROR FILE MISSING",
    "WARNING MEMORY LOW"
]

# Initialize counters
error_count = 0
info_count = 0
warning_count = 0

# Process logs (case insensitive)
for log in logs:
    log = log.lower()   # ignore case
    
    if "error" in log:
        error_count += 1
    elif "info" in log:
        info_count += 1
    elif "warning" in log:
        warning_count += 1

# Print counts
print("ERROR count:", error_count)
print("INFO count:", info_count)
print("WARNING count:", warning_count)

# Bonus: Find most frequent log type
counts = {
    "ERROR": error_count,
    "INFO": info_count,
    "WARNING": warning_count
}

most_frequent = max(counts, key=counts.get)
print("Most frequent log type:", most_frequent)=
