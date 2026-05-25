# 🐛 SQL Error Log (White-Box Audit)
*Rule: Labeling the error fixes the error.*

| Date | The Query | The Error Message | Failure Mode | The Fix |
| :--- | :--- | :--- | :--- | :--- |
| **Example** | `SELECT * FROM Students WHERE Name = Rahul` | `no such column: Rahul` | **Syntax Failure** (Forgot Quotes) | `WHERE Name = 'Rahul'` |
| **Example** | `SELECT Salary + Commission` | `Result: NULL` | **Logic Failure** (Forgot NULL handling) | `Salary + IFNULL(Comm, 0)` |
| | | | | |
| | | | | |
