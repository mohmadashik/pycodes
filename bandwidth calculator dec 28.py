from collections import defaultdict
from datetime import datetime

def process_log_file(log_file_path):
    # Dictionary to store counts for each timestamp
    timestamp_counts = defaultdict(lambda: defaultdict(int))

    with open(log_file_path, 'r') as file:
        for line in file:
            # Check if the line matches the expected log format
            if "rcm: tr packet : time_stamp" in line:
                # Extract timestamp and index from the log line
                timestamp_str, index_str = extract_timestamp_and_index(line)
                
                # Convert timestamp string to datetime object
                timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S,%f')
                
                # Increment count for the specific timestamp and index
                timestamp_counts[timestamp][index_str] += 1

    # Print the results
    for timestamp, index_counts in timestamp_counts.items():
        print(f"At {timestamp.strftime('%H:%M:%S')}:")
        for index, count in index_counts.items():
            print(f"  Index {index}: {count} occurrences")
        print()

def extract_timestamp_and_index(line):
    # Extract timestamp and index using string manipulation
    timestamp_end = line.find(" - radio_communication_manager")
    timestamp_str = line[:timestamp_end].strip()

    index_start = line.find("index : ") + len("index : ")
    index_end = line.find("\n", index_start)
    index = line[index_start:index_end]

    return timestamp_str, index

# Example usage
log_file_path = "radio_communication_manager-2023-12-28-07-30-00.log"
process_log_file(log_file_path)
