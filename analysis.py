import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# 1. Main Dataset Load
# -------------------------------

file_path = "Data/data.csv"      # <-- Quotes જરૂરી છે

df = pd.read_csv(file_path)

print(df.columns.tolist())
print("CSV Successfully Loaded ✅")
print(df.head())

# -------------------------------
# 2. Loss Analysis
# -------------------------------

df['LossAmount'] = df['LossAmount'].fillna(0)

loss_by_servicer = (
    df.groupby('ServicerName')['LossAmount']
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(12,6))

bars = plt.bar(
    loss_by_servicer.index,
    loss_by_servicer.values,
    color="red"
)

plt.title("Average Loss Amount by Servicer", fontsize=16, fontweight='bold')
plt.xlabel("Servicer")
plt.ylabel("Average Loss Amount (₹)")
plt.xticks(rotation=45, ha='right')

# Value Labels
for bar in bars:
    y = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width()/2,
        y,
        f"{y:,.0f}",
        ha='center',
        va='bottom'
    )

plt.tight_layout()
plt.show()

# -------------------------------
# 3. Star Schema Creation
# -------------------------------

fact_table = df[['LoanID', 'LossAmount', 'RecoveryAmount', 'NetLoss']]

servicer_dim = (
    df[['ServicerID', 'ServicerName']]
    .drop_duplicates()
)

print("\nFact Table:")
print(fact_table.head())

print("\nDimension Table (Servicer):")
print(servicer_dim.head())

print("\nTop 5 Servicers by Loss:")

print(
    df.groupby("ServicerName")["LossAmount"]
      .mean()
      .sort_values(ascending=False)
      .head()
)

# -------------------------------
# 4. Risk Scoring Model
# -------------------------------

# DPD_Days column છે કે નહીં તે ચેક કરો
if 'Times30DPD_Last12M' in df.columns:

    df['DPD_Days'] = df['Times30DPD_Last12M'].fillna(0)

    def calculate_risk(row):

        if row['Times30DPD_Last12M'] > 30:
            return 'High Risk'

        elif row['Times30DPD_Last12M'] > 0:
            return 'Medium Risk'

        else:
            return 'Low Risk'

    df['Risk_Category'] = df.apply(
        calculate_risk,
        axis=1
    )

    risk_analysis = (
        df.groupby(
            ['ServicerName', 'Risk_Category']
        )
        .size()
        .unstack(fill_value=0)
    )

    print("\n--- Risk Analysis Report ---")
    print(risk_analysis)

else:
    print("\n⚠️ Times30DPD_Last12M column not found in dataset")
    # આ રિપોર્ટને Excel ફાઈલમાં સેવ કરો
risk_analysis.to_excel("Risk_Analysis_Report.xlsx")
print("\n✅ રિપોર્ટ 'Risk_Analysis_Report.xlsx' નામથી સેવ થઈ ગયો છે!")
# -------------------------------
# 5. Recovery Amount Analysis
# -------------------------------

recovery_by_servicer = (
    df.groupby('ServicerName')['RecoveryAmount']
    .mean()
    .sort_values(ascending=False)
)

print("\n--- Recovery Analysis Report ---")
print(recovery_by_servicer)

plt.figure(figsize=(10,6))

recovery_by_servicer.plot(
    kind='bar',
    color='green'
)

plt.title("Average Recovery Amount by Servicer")
plt.xlabel("Servicer Name")
plt.ylabel("Average Recovery Amount")
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()
# -------------------------------
# 6. Net Loss Analysis
# -------------------------------

netloss_by_servicer = (
    df.groupby('ServicerName')['NetLoss']
    .mean()
    .sort_values(ascending=False)
)

print("\n--- Net Loss Analysis Report ---")
print(netloss_by_servicer)

plt.figure(figsize=(10,6))

netloss_by_servicer.plot(
    kind='bar',
    color='orange'
)

plt.title("Average Net Loss by Servicer")
plt.xlabel("Servicer Name")
plt.ylabel("Average Net Loss")

plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()