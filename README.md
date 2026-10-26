# NumPy Analyzer

## Description
A Python-based console application that integrates NumPy functionalities with Object-Oriented Programming (OOP) principles. It provides a menu-driven interface to perform common data operations, statistical analyses, and mathematical computations on NumPy arrays.

## Features
- **Array Management**: Create 1D, 2D, or 3D arrays; indexing; slicing; combining (concatenate/vstack); splitting.
- **Mathematical Operations**: Element-wise addition, subtraction, multiplication, division; dot product; matrix multiplication.
- **Search, Sort, Filter**: Search values, sort ascending/descending, filter by conditions.
- **Aggregates**: Sum, mean, median, standard deviation, variance.
- **Statistics**: Min, max, percentiles, correlation coefficients.
- **OOP Principles**: Constructor, encapsulation, private methods, `@classmethod`, `@staticmethod`.
- **Menu-Driven Interface**: Easy navigation with nested sub-menus.

## Project Structure
NumPy-Analyzer/
│
├── numpy_analyzer.py
├── README.md
└── requirements.txt

## Assumptions
- The program is a console-based application.
- Users have Python 3.x and NumPy installed.
- Arrays are created by user-provided elements (space-separated).
- Mathematical operations between two arrays require matching shapes.
- Sorting is applied row-wise for multi-dimensional arrays.
- Correlation requires two 1D arrays of equal length.
- Percentiles use NumPy's default linear interpolation method.

## Requirements
- Python 3.x
- NumPy (`pip install numpy`)

## How to Run
1. Ensure Python 3.x is installed.
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python numpy_analyzer.py`

## OOP Concepts Demonstrated
| Concept | Implementation |
|---------|----------------|
| Class | `DataAnalytics` |
| Constructor | `__init__(self, array=None)` |
| Encapsulation | Private methods prefixed with `_` |
| Class method | `get_instance_count()` |
| Static method | `array_info(array)` |

## NumPy Operations Demonstrated
- Array creation: `np.array()`, `reshape()`
- Indexing & slicing: `arr[idx]`, `arr[start:end]`
- Combining: `np.concatenate()`, `np.vstack()`
- Splitting: `np.split()`
- Math: `+`, `-`, `*`, `/`, `np.dot()`, `np.matmul()`
- Search: `np.where()`
- Sort: `np.sort()`
- Filter: Boolean masking
- Aggregates: `np.sum()`, `np.mean()`, `np.median()`, `np.std()`, `np.var()`
- Statistics: `np.min()`, `np.max()`, `np.percentile()`, `np.corrcoef()`

## Author
[Chirag.]
