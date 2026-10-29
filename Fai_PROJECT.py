print("========================================")
print(" AI-BASED WATER QUALITY MONITORING SYSTEM")
print("========================================")

ph = float(input("Enter pH value: "))
turbidity = float(input("Enter Turbidity (NTU): "))
tds = float(input("Enter TDS (mg/L): "))

print("\n----- WATER QUALITY REPORT -----")
print("pH Value:", ph)
print("Turbidity:", turbidity, "NTU")
print("TDS:", tds, "mg/L")

if ph < 6.5 or ph > 8.5:
    print("Alert: pH is outside the example range!")

if turbidity > 5:
    print("Alert: Turbidity is high!")

if tds > 500:
    print("Alert: TDS is high!")

if 6.5 <= ph <= 8.5 and turbidity <= 5 and tds <= 500:
    print("No alert from the given rules.")

print("\nNote: This is an educational prototype.")
print("It cannot confirm whether water is safe to drink.")