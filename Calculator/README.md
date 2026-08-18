# Calculator

A collection of mathematical tools, algorithm visualisers, and number-theory experiments.

## Prerequisites

```bash
pip install -e ".[gui]"   # for GUI-based scripts (matplotlib, sympy, tkinter)
```

Tkinter ships with the standard library on most platforms. On Linux you may need:

```bash
sudo apt-get install python3-tk
```

## Scripts

| Script | Description | Run |
|--------|-------------|-----|
| `sudoku.py` | Backtracking Sudoku solver with a `SudokuSolver` class | `python sudoku.py` |
| `Mortgage.py` | Fixed-rate mortgage calculator with amortisation breakdown | `python Mortgage.py` |
| `conject.py` | Collatz Conjecture visualiser (Tkinter GUI) | `python conject.py` |
| `Quadratic_Equation.py` | Quadratic equation solver with graph | `python Quadratic_Equation.py` |
| `mega_calculator.py` | Multi-operation scientific calculator | `python mega_calculator.py` |
| `stock.py` | Stock price analyser using yfinance | `python stock.py` |
| `number_base.py` | Convert numbers between bases 2–36 | `python number_base.py` |
| `int_diff.py` | Symbolic integration & differentiation (sympy) | `python int_diff.py` |
| `bmi.py` | Body Mass Index calculator | `python bmi.py` |
| `roman_number.py` | Roman ↔ decimal converter | `python roman_number.py` |
| `time_calculator.py` | Time arithmetic (add/subtract durations) | `python time_calculator.py` |
| `special_relativity_calculator.py` | Lorentz factor and relativistic effects | `python special_relativity_calculator.py` |
| `sequence.py` | Fibonacci sequence generator | `python sequence.py` |
| `graph.py` | Function graphing calculator | `python graph.py` |
| `time.py` | 12-hour ↔ 24-hour time converter | `python time.py` |
| `grade.py` | Grade percentage calculator | `python grade.py` |

## Running Tests

```bash
pytest ../tests/test_calculators/ -v
```
