# Property Price Estimator

This is a small beginner project that estimates a house price using simple rules.

It uses a knowledge base and an inference process. The rules are based on house area, bedrooms, location, and condition.

The rates in this project are sample values for practice. They are not real market prices.

## How to run

1. Install Python 3.
2. Open this folder in VS Code.
3. Run `python main.py` in the terminal.
4. Enter the house details when asked.

## Inputs

- Area in marla
- Number of bedrooms
- Location: central, normal, or outer
- Condition: good, average, or poor

## Files

- `main.py`: asks the user for information
- `estimator.py`: applies the rules and calculates the estimate
- `sample_data.csv`: example inputs
- `test_cases.md`: four manual tests
