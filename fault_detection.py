import pandas as pd

# Read CSV
df = pd.read_csv("sensor_data.csv")

# Fault Detection Function
def detect_fault(row):

    faults = []

    if row["RPM"] > 2800:
        faults.append("P0016 - RPM Spike Detected")

    if row["Temperature"] > 110:
        faults.append("P0217 - Engine Overheat")

    if row["Speed"] > 100:
        faults.append("P0219 - Vehicle Overspeed")

    if len(faults) == 0:
        return "PASS"

    return " | ".join(faults)

# Apply fault detection
df["Diagnostic_Result"] = df.apply(detect_fault, axis=1)

# Save diagnostic output
df.to_csv("diagnostic_results.csv", index=False)

print("Diagnostic analysis complete.")
print(df.head(20))

# Summary
total_records = len(df)

fault_records = len(
    df[df["Diagnostic_Result"] != "PASS"]
)

print("\n===== SUMMARY =====")
print("Total Records :", total_records)
print("Fault Records :", fault_records)
print("Pass Records  :", total_records - fault_records)