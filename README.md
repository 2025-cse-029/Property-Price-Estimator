# Property Price Estimator

This is a small beginner-level project that estimates a house price using simple rules.

It uses a knowledge base of sample values and an inference process. The estimate depends on area, bedrooms, location, and house condition.

The sample rates are only for practice. They are not real property market rates.

## How to run

1. Install Python 3.
2. Open this folder in VS Code.
3. Run `python main.py` in the terminal.
4. Enter the property details.

## Inputs

- Area in marla
- Number of bedrooms
- Location: central, normal, or outer
- Condition: good, average, or poor

## Files

- `main.py`: asks for property information and displays the estimate
- `estimator.py`: applies the rules and calculates the estimate
- `sample_data.csv`: sample properties and practice prices
- `test_cases.md`: four test cases
- `test_project.py`: automated checks

## Algorithm in 3 steps

1. Take the property area, bedrooms, location, and condition.
2. Apply the location and condition rules to the base price and add the bedroom amount.
3. Show the estimated price or an invalid-input message.
