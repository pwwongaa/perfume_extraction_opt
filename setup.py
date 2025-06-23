from setuptools import setup, find_packages

setup(
    name='perfume_extraction_optimizer',
    version='0.1.0',
    description='A tool to optimize perfume extraction protocols using cheminformatics',
    author='[Your Name]',
    author_email='[your-email@example.com]',
    url='https://github.com/your-username/perfume-extraction-optimizer',
    packages=find_packages(),
    install_requires=[
        'rdkit==2023.9.6',
        'pandas==2.2.2',
        'scikit-learn==1.5.0',
        'matplotlib==3.9.0',
        'seaborn==0.13.2',
        'numpy==2.0.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)