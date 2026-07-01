import pandas as pd

# 1. Load the Dataset
df = pd.read_csv('2017_Yellow_Taxi_Trip_Data.csv')

# Note: If you want to inspect the dataset, uncomment the lines below:
# print(df.head(10))
# print(df.info())
# print(df.describe())

# 2. Sort the data by total amount and print the bottom 20 values
print("Smallest 20 Total Amounts:")
print(df.nsmallest(20, 'total_amount')[['total_amount']])
print("-" * 55)

# 3. What is the average tip for trips paid for with cash?
print("Transaction Distribution by Payment Type:")
print(df['payment_type'].value_counts())
print("-" * 55)

# Filter for Credit Card and Cash trips (Done only ONCE)
credit_card_trips = df[df['payment_type'] == 1]
cash_trips = df[df['payment_type'] == 2]

# Printing the statistics
print(f"Number of credit card trips: {len(credit_card_trips)}")
print(f"Average tip for credit card trips: ${credit_card_trips['tip_amount'].mean():.2f}")
print(f"Average recorded tip for cash trips: ${cash_trips['tip_amount'].mean():.2f}")
print("-" * 55)

# 4. Average Credit Card Tip by Passenger Count
print("Average Tip Amount by Passenger Count (Credit Card Only):")
avg_tip_by_passenger = credit_card_trips.groupby('passenger_count')['tip_amount'].mean()
print(avg_tip_by_passenger.apply(lambda x: f"${x:.2f}"))
print("-" * 55)

# 5. Fixing the Missing Vendor Analysis
# The original code had missing variables; usually, the column is 'VendorID'
if 'VendorID' in df.columns:
    print("Trip Counts by Vendor:")
    vendor_counts = df['VendorID'].value_counts()
    print(vendor_counts)
    
    print("\nAverage Total Amount by Vendor:")
    avg_total_by_vendor = df.groupby('VendorID')['total_amount'].mean()
    print(avg_total_by_vendor)
