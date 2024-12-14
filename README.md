# Digital Line Coding Simulator

This repository contains a Python-based simulator for visualizing various digital line coding schemes. It allows users to input a binary string and visualize its encoding using different line coding schemes. The available encoding schemes are:

- NRZ (Non-Return-to-Zero)
- RZ (Return-to-Zero)
- Manchester
- Differential Manchester

## Features

- Step-by-step visualization of digital signals.
- Real-time input and plot generation.
- Clear separation and labeling of each bit in the signal.
- Support for additional encoding schemes and visual enhancements (horizontal lines, text labels, etc.).

## Requirements

- Python 3.x
- `matplotlib` library

To install the required library, run:
pip install matplotlib


## Usage

1. Run the Python script `line_coding_simulator.py`.
2. Enter a binary string (e.g., `101010`).
3. Select one of the available encoding schemes.
4. The corresponding signal will be plotted with bit labels and visual separation.
5. Optionally, try multiple encoding schemes for the same binary string.

## Example

### Input:
Enter the binary string (0s and 1s only): 10101


### Output:
- Step plot with bit labels and clear separation for each encoding scheme.



