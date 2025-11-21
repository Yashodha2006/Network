import sys

# Check if all arguments are provided
if len(sys.argv) != 5:
    print("Usage: python network.py <wifi_name> <password> <speed> <data_limit>")
    sys.exit(1)

# Assign arguments
wifi_name = sys.argv[1]
password = sys.argv[2]
speed = sys.argv[3]
data_limit = sys.argv[4]

# Display summary
print("========= NETWORK CONFIGURATION SUMMARY =========")
print(f"WiFi Name       : {wifi_name}")
print(f"Password        : {password}")
print(f"Speed           : {speed} Mbps")
print(f"Data Limit      : {data_limit} GB")
print("Network connected successfully")
