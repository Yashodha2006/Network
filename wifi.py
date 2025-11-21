import sys

# Check if user has provided all required command-line arguments
if len(sys.argv) > 4:
    wifi_name = str(sys.argv[1])
    password = str(sys.argv[2])
    speed = float(sys.argv[3])
    data_limit = float(sys.argv[4])

    print("User provided input")
else:
    # Default values
    wifi_name = "BCA"
    password = "1234"
    speed = 30.0
    data_limit = 20.0

# Print configuration summary
print("\nNetwork Configuration:")
print("WiFi Name      :", wifi_name)
print("Password       :", password)
print("Speed (Mbps)   :", speed)
print("Data Limit (GB):", data_limit)

print("\nNetwork is connected successfully!")