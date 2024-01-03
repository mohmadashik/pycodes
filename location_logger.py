import subprocess
import time

log_filename = "rostopic_echo_log.txt"
duration_minutes = 30
end_time = time.time() + duration_minutes * 60

with open(log_filename, "w") as log_file:
    while time.time() < end_time:
        try:
            # Run the rostopic echo command and capture stdout
            result = subprocess.run(
                ["rostopic", "echo", "stdout"], capture_output=True, text=True
            )
            output = result.stdout

            # Write the output to the log file
            log_file.write(output)

            # Print the output (optional)
            print(output)

            # Sleep for a short interval before the next iteration
            time.sleep(1)
        except KeyboardInterrupt:
            # Allow the user to interrupt the script with Ctrl+C
            break

print(f"Logging complete. Output saved to {log_filename}")
