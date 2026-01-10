log_data = "ERROR: Disk full. ERROR: Connection lost. Warning: Battery low."

error_count = log_data.count("ERROR")

print(f"The word 'ERROR' appears {error_count} times.")