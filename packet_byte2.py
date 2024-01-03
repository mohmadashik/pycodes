import os
from collections import defaultdict
from datetime import datetime, timedelta

def process_log_files_in_directory(directory):
    # Dictionary to store counts for each timestamp
    packet_rate_result_log_path= 'packet_rate_result_log.log'
    timestamp_counts = defaultdict(lambda: defaultdict(int))
    result_file = open(packet_rate_result_log_path,'w')
    # Get the current time
    current_time = datetime.now()

    # Calculate the time 30 minutes ago
    thirty_minutes_ago = current_time - timedelta(minutes=30)

    # Iterate through files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".log"):
            file_path = os.path.join(directory, filename)
            # Check if the file was created in the last 30 minutes
            if os.path.getmtime(file_path) >= thirty_minutes_ago.timestamp():
                with open(file_path, 'r') as file:
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
        time_msg = f"At {timestamp.strftime('%H:%M:%S')}:"
        print(time_msg)
        time_msg+='\n'
        result_file.write(time_msg)
        for index, count in index_counts.items():
            index_msg = f"  Index {index}: {count} occurrences"
            print(index_msg)
            index_msg+='\n'
            result_file.write(index_msg)
        print()
    result_file.close()

def extract_timestamp_and_index(line):
    # Extract timestamp and index using string manipulation
    timestamp_end = line.find(" - radio_communication_manager")
    timestamp_str = line[:timestamp_end].strip()

    index_start = line.find("index : ") + len("index : ")
    index_end = line.find("\n", index_start)
    index = line[index_start:index_end]

    return timestamp_str, index

# Use the current directory
current_directory = os.getcwd()
process_log_files_in_directory(current_directory)
