You are given a 2D array of cells representing a spreadsheet. Each cell in the spreadsheet is contained in a `Cell` class which can either be a **CONSTANT** or **FORMULA** type.

- A **CONSTANT** type is an individual integer in the cell (i.e., `5`, `7`, `1`, etc.).
- A **FORMULA** type is represented in a `Formula` class which contains an array of constants (strictly integers) and an array of cell positions (represented as strings).

---

A cell position is always in the format of `<character><integer>` where:
- The character is 1 uppercase character (from `'A'` to `'Z'`).
- The integer is a single-digit number (from `0` to `9`).

### Examples of cell positions:
1. `"A1"` → position `[0][0]` in the spreadsheet  
2. `"B6"` → position `[5][1]` in the spreadsheet  
3. `"C2"` → position `[1][2]` in the spreadsheet  

---

### Examples of formulas:
1. `constants = [3]`, `cells = [A1, B2]` → `A1 + B2 + 3`
2. `constants = []`, `cells = [C2, C6]` → `C2 + C6`
3. `constants = [2, 5]`, `cells = [A2]` → `A2 + 2 + 5`

---

### Evaluation:
The evaluation of a formula would be the sum of all constants and cells together. Return the spreadsheet with all formulas evaluated.

---

### Notes:
- A cell position always corresponds to a valid position in the spreadsheet.
- A formula will never have a cell position that corresponds to itself.
- A spreadsheet will always have solvable formulas.