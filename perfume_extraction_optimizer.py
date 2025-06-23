import pandas as pd
import numpy as np
from rdkit import Chem
from rdkit.Chem import Descriptors, AllChem
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import seaborn as sns

# Placeholder dataset (replace with user-provided isolates and solvents)
data = {
    'Compound': ['Linalool', 'Limonene', 'Geraniol'],
    'SMILES': [
        'CC(C)=CCCC(C)(O)C=C',           # Linalool
        'CC1=CC[C@@H](CC1)C(=C)C',       # Limonene
        'CC(C)=CCCC(C)=CCO',             # Geraniol
    ],
    'Temperature_C': [40, 50, 60, 40, 50, 60, 40, 50, 60],  # Example conditions
    'Solvent_Mix': ['Ethanol:Water 70:30', 'Hexane 100', 'Ethanol 100'] * 3,
    'Solvent_Polarity': [32.7, 24.3, 24.3] * 3,  # Dielectric constants
    'Yield_Percent': [85, 80, 88, 90, 85, 82, 78, 75, 80]  # Hypothetical yields
}
df = pd.DataFrame(data)

# Function to compute molecular descriptors
def compute_descriptors(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    return {
        'MolecularWeight': Descriptors.MolWt(mol),
        'LogP': Descriptors.MolLogP(mol),
        'Polarizability': AllChem.CalcLabuteASA(mol),
        'NumHDonors': Descriptors.NumHDonors(mol),
        'NumHAcceptors': Descriptors.NumHAcceptors(mol)
    }

# Process dataset
df['Descriptors'] = df['SMILES'].apply(compute_descriptors)
df = df.dropna(subset=['Descriptors'])
descriptor_df = pd.DataFrame(df['Descriptors'].tolist())
df = pd.concat([df, descriptor_df], axis=1)

# Prepare data for ML
X = df[['MolecularWeight', 'LogP', 'Polarizability', 'NumHDonors', 'NumHAcceptors', 'Temperature_C', 'Solvent_Polarity']]
y = df['Yield_Percent']
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Function to estimate solvent mixture polarity
def estimate_polarity(solvent_ratios):
    # Dielectric constants for common solvents
    solvent_polarities = {'Ethanol': 24.3, 'Water': 80.1, 'Hexane': 1.9}
    total_polarity = sum(ratio * solvent_polarities[solvent] for solvent, ratio in solvent_ratios.items())
    return total_polarity

# Optimize for a new compound (replace with user input)
new_compound_smiles = 'CC(C)=CCCC(C)(O)C=C'  # Example: Linalool
new_descriptors = compute_descriptors(new_compound_smiles)
if not new_descriptors:
    print("Invalid SMILES provided")
    exit()

# Test solvent mixtures and temperatures
solvents = ['Ethanol', 'Water', 'Hexane']  # Replace with user-provided solvents
temperatures = np.arange(30, 71, 10)  # 30–70°C to avoid degradation
ethanol_ratios = np.linspace(0, 1, 5)  # 0–100% ethanol
results = []

for temp in temperatures:
    for eth_ratio in ethanol_ratios:
        water_ratio = 1 - eth_ratio
        solvent_ratios = {'Ethanol': eth_ratio, 'Water': water_ratio, 'Hexane': 0}
        polarity = estimate_polarity(solvent_ratios)
        input_data = {**new_descriptors, 'Temperature_C': temp, 'Solvent_Polarity': polarity}
        input_df = pd.DataFrame([input_data])
        predicted_yield = model.predict(input_df)[0]
        results.append({
            'Temperature_C': temp,
            'Ethanol_Percent': eth_ratio * 100,
            'Water_Percent': water_ratio * 100,
            'Solvent_Polarity': polarity,
            'Predicted_Yield': predicted_yield
        })

results_df = pd.DataFrame(results)
optimal_conditions = results_df.loc[results_df['Predicted_Yield'].idxmax()]

# Output optimized protocol
print("\nOptimized Extraction Protocol")
print("-----------------------------")
print(f"Compound: Linalool (SMILES: {new_compound_smiles})")
print(f"Optimal Temperature: {optimal_conditions['Temperature_C']}°C")
print(f"Optimal Solvent Mix: Ethanol {optimal_conditions['Ethanol_Percent']:.1f}%, Water {optimal_conditions['Water_Percent']:.1f}%")
print(f"Predicted Yield: {optimal_conditions['Predicted_Yield']:.1f}%")
print("\nSteps:")
print("1. Prepare raw material (e.g., dried lavender flowers) and grind to increase surface area.")
print("2. Mix with solvent (ethanol:water as above) at a 1:5 material:solvent ratio.")
print(f"3. Heat to {optimal_conditions['Temperature_C']}°C in a reflux setup for 2–4 hours.")
print("4. Filter the extract and evaporate solvent under reduced pressure.")
print("5. Store extract in a dark, airtight container at <10°C to preserve volatiles.")

# Visualize results
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.heatmap(
    results_df.pivot(index='Temperature_C', columns='Ethanol_Percent', values='Predicted_Yield'),
    annot=True, fmt='.1f', cmap='viridis'
)
plt.title('Predicted Extraction Yield (%) vs. Temperature and Ethanol %')
plt.xlabel('Ethanol %')
plt.ylabel('Temperature (°C)')
plt.show()

# Save results
results_df.to_csv('optimized_extraction_results.csv', index=False)
print("\nResults saved to 'optimized_extraction_results.csv'")