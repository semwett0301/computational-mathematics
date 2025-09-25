# Theory of Probability

## Overview
This assignment analyzes a small sample (n = 20) and demonstrates basic exploratory statistics and graphical summaries:
- **Sorted sample (variation series)**, **min**, **max**, and **range**
- **Sample mean** and **sample standard deviation**
- **Empirical distribution function (EDF)** values and a step plot
- **Interval (binned) statistical series** using Sturges' rule
- **Histogram (density)** and **frequency polygon**

The dataset is currently hardcoded in `main.py` as a 20-element NumPy array.

## What the script does
The script in `main.py`:
1. Sorts the input data and prints the variation series, min, max, and range
2. Computes and prints the sample mean and sample standard deviation
3. Constructs the empirical distribution function values and displays a step plot
4. Computes the number of bins with Sturges' rule `n = 1 + log2(N)` and builds the interval statistical series
5. Plots a Seaborn histogram with density normalization
6. Plots a frequency polygon (line plot through histogram bin centers)

Console messages are printed in Russian; plots open in separate windows.

## Requirements
- Python 3.9+
- Packages:
  - `numpy`
  - `pandas`
  - `seaborn`
  - `matplotlib`
  - `termcolor`

Install dependencies (prefer a virtual environment):
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install numpy pandas seaborn matplotlib termcolor
```

## How to run
From this directory:
```bash
python3 main.py
```

## Output
- Text output in the terminal with:
  - Sorted data (variation series)
  - Min, max, range
  - Sample mean and standard deviation
  - EDF values table
  - Interval statistical series (bins and frequencies)
- Three plots:
  - EDF step plot
  - Histogram (density)
  - Frequency polygon


