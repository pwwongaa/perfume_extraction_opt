# Perfume Extraction Optimizer (Demo)

A Python tool to optimize perfume extraction protocols by predicting the best temperature and solvent mixture for chemical isolates using cheminformatics and machine learning.

## Features
- Computes molecular descriptors using RDKit.
- Predicts extraction yield with a Random Forest model.
- Optimizes temperature and solvent mixtures (e.g., ethanol:water ratios).
- Visualizes results with heatmaps.

## Requirements
- Python 3.7+
- RDKit, Pandas, Scikit-learn, Matplotlib, Seaborn

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/perfume-extraction-optimizer.git
   cd perfume-extraction-optimizer
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *Note*: RDKit is best installed via conda:
   ```bash
   conda install -c rdkit rdkit
   ```

## Usage
Run the script with default settings:
```bash
python perfume_extraction_optimizer.py
```

To use custom chemical isolates and solvents:
1. Edit `data/sample_data.csv` with your SMILES strings and solvents.
2. Update `solvents` in the script.
3. Run the script to generate an optimized protocol.

See [docs/usage.md](docs/usage.md) for detailed examples.

## Example Output
```
Optimized Extraction Protocol
-----------------------------
Compound: Linalool (SMILES: CC(C)=CCCC(C)(O)C=C)
Optimal Temperature: 50°C
Optimal Solvent Mix: Ethanol 75.0%, Water 25.0%
Predicted Yield: 89.2%
```

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License
XXX License. See [LICENSE](LICENSE) for details.

## Contact
For issues or questions, open an issue or email [your-email@example.com].
