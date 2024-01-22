import subprocess
from subprocess import TimeoutExpired

# Creates a new text file in write mode to store the results in 
result_file = open("IP Address Ping Results.txt" , "w")

def ping_host(host):
    try:
        # Use subprocess to open a command prompt and execute the ping command
        result = subprocess.run(['ping', '-n', '4', host], capture_output=True, text=True, check=True, timeout=10)
        # Print the result
        print(result.stdout)
        # Print each result to the external text document
        result_file.write(result.stdout) 
    except subprocess.CalledProcessError as e:
        # If the ping command fails, print the error message
        print(f"Error: {e.stderr}")
    except TimeoutExpired:
        # Handle the case where the ping command times out
        print(f"Timeout: The ping command took too long.")

# Open the file in read mode
with open("ping.txt", "r") as file:
    # Iterate through each line in the file
    for line in file:
        # Remove newline character from the end of the line
        host = line.strip()

        # Call the ping_host function for each host
        ping_host(host)
# Always close your files when you are finished 
result_file.close()
