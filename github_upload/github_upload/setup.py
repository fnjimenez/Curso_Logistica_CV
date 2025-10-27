"""
Setup configuration for Amazon Logistics Optimization package
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

# Read requirements
requirements_file = Path(__file__).parent / "requirements.txt"
if requirements_file.exists():
    requirements = [
        line.strip()
        for line in requirements_file.read_text().splitlines()
        if line.strip() and not line.startswith("#")
    ]
else:
    requirements = [
        "pulp>=2.7.0",
        "networkx>=3.0",
        "matplotlib>=3.5.0",
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "Pillow>=9.0.0",
        "qrcode>=7.3.1",
        "reportlab>=3.6.0",
    ]

setup(
    name="amazon-logistics-optimization",
    version="4.0.0",
    author="Francisco Jiménez",
    author_email="tu-email@ejemplo.com",
    description="Sistema de optimización logística para Amazon México",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fnjimenez/Curso_Logistica_CV",
    project_urls={
        "Bug Reports": "https://github.com/fnjimenez/Curso_Logistica_CV/issues",
        "Source": "https://github.com/fnjimenez/Curso_Logistica_CV",
        "Documentation": "https://github.com/fnjimenez/Curso_Logistica_CV/tree/main/docs",
    },
    packages=find_packages(exclude=["tests", "docs", "examples"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Visualization",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.950",
        ],
        "docs": [
            "sphinx>=4.5.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
        "jupyter": [
            "jupyter>=1.0.0",
            "ipywidgets>=7.6.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "amazon-logistics=src.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="logistics optimization linear-programming supply-chain amazon",
)
