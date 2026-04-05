# 🏏 Data Engineering Fundamentals: Python & CSVs

Welcome to Day 3 of the Data Engineering track! Today's focus is on efficiently reading and processing structured data using Python's built-in `csv` module.

## 1. The Iterator (`csv.reader`)
Think of an iterator like a **conveyor belt** in a factory.
- **Exhaustible:** Once a piece of data (a row) passes you on the belt, it's gone. If you want to see it again, you have to "restart the belt" by re-opening the file or resetting the pointer.
- **The Header Trick:** CSV files usually have a header row (e.g., `Name, Team, Runs`). If you try to perform math on the word "Runs", your code will crash.
  - **Solution:** Use `next(reader)` before starting your loop. This "consumes" the first row, leaving only the actual data for your loop.

## 2. DictReader vs. Reader
Choosing the right tool depends on how you want to access your data.

### `csv.reader` (The List Approach)
- **Format:** Returns each row as a **List** `[]`.
- **Access:** You access columns by their index: `row[0]`, `row[1]`.
- **Risk:** If someone adds a new column to the start of your CSV, `row[0]` might suddenly point to the wrong data!

### `csv.DictReader` (The Dictionary Approach)
- **Format:** Returns each row as a **Dictionary** `{}`.
- **Access:** You access columns by their name: `row["Name"]`.
- **Safety:** This is much safer. Even if the column order changes, `row["Name"]` will always find the right data.

## 3. List Comprehensions
List comprehensions are a concise way to create new lists from existing ones.
**Anatomy:** `[output for item in list if condition]`

### The Data Engineering Catch: Types
When Python reads a CSV, **everything is a string** (`"100"`, not `100`).
- **The Fix:** Always wrap numeric columns in `int()` or `float()` when filtering or performing math.
```python
# Example: Get names of players with more than 50 runs
high_scorers = [row["Name"] for row in reader if int(row["Runs"]) > 50]
```

## 4. Common Beginner Errors 🚩

### `TypeError`
*   **The Cause:** Trying to compare a string to an integer (e.g., `"100" > 50`).
*   **The Fix:** Use `int(row["column_name"])`.

### `IndentationError`
*   **The Cause:** Mixing tabs and spaces or inconsistent spacing.
*   **The Fix:** Always use 4 spaces for indentation in Python.

### `FileNotFoundError`
*   **The Cause:** The script can't find your CSV because it's looking in the wrong folder.
*   **The Fix:** Use the `pathlib` pattern:
  ```python
  from pathlib import Path
  file_path = Path(__file__).parent / "data.csv"
  ```
