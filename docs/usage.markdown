# Usage Guide for Perfume Extraction Optimizer

## Overview
This tool optimizes perfume extraction by predicting the best temperature and solvent mixture for chemical isolates.

## Input Data
Edit `data/sample_data.csv` with your compounds and solvents:
```csv
Compound,SMILES,Temperature_C,Solvent_Mix,Solvent_Polarity,Yield_Percent
Linalool,CC(C)=CCCC(C)(O)C=C,40,Ethanol:Water 70:30,32.7,85
```

- **Compound**: Name of the isolate (e.g., Linalool).
- **SMILES**: Chemical structure in SMILES format.
- **Temperature_C**: Extraction temperature (°C).
- **Solvent_Mix**: Solvent mixture (e.g., Ethanol:Water 70:30).
- **Solvent_Polarity**: Dielectric constant of the mixture.
- **Yield_Percent**: Extraction yield (%).

## Running the Script
1. Update `solvents` and `solvent_polarities` in `perfume_extraction_optimizer.py` with your solvents.
2. Run:
   ```bash
   python perfume_extraction_optimizer.py
   ```
3. Output includes:
   - Optimized protocol (temperature, solvent mix, predicted yield).
   - Heatmap visualization.
   - CSV file (`optimized_extraction_results.csv`).

## Example: Custom Compound
To optimize for citral (SMILES: `CC(C)=CCCC(C)=CC=O`):
1. Update `new_compound_smiles` in the script:
   ```python
   new_compound_smiles = 'CC(C)=CCCC(C)=CC=O'
   ```
2. Run the script to get the protocol.

## Notes
- Use PubChem or ChEMBL for SMILES strings.
- Ensure RDKit is installed via conda for compatibility.
- Adjust temperature range in `temperatures` for heat-sensitive compounds.