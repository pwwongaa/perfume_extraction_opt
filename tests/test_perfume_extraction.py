import pytest
from rdkit import Chem
from perfume_extraction_optimizer import compute_descriptors, estimate_polarity

def test_compute_descriptors():
    smiles = 'CC(C)=CCCC(C)(O)C=C'  # Linalool
    descriptors = compute_descriptors(smiles)
    assert descriptors is not None
    assert 'MolecularWeight' in descriptors
    assert abs(descriptors['MolecularWeight'] - 154.249) < 0.01
    assert 'LogP' in descriptors

def test_compute_descriptors_invalid_smiles():
    smiles = 'InvalidSMILES'
    descriptors = compute_descriptors(smiles)
    assert descriptors is None

def test_estimate_polarity():
    solvent_ratios = {'Ethanol': 0.7, 'Water': 0.3, 'Hexane': 0.0}
    polarity = estimate_polarity(solvent_ratios)
    expected_polarity = (0.7 * 24.3) + (0.3 * 80.1)
    assert abs(polarity - expected_polarity) < 0.01

if __name__ == '__main__':
    pytest.main()