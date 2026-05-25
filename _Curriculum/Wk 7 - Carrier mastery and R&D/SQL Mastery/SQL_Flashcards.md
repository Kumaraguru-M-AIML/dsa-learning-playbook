# 🗂️ SQL Flashcards (Spaced Repetition)
*Format: Question vs Answer (Cloze Deletion style)*

## 🟢 Phase 1: The Foundation

### Lesson 1: Genesis (CREATE)
**Q:** What SQL command creates a new table structure?
**A:** `CREATE TABLE`

**Q:** Which data type should be used for whole numbers (like age)?
**A:** `INTEGER` (or `NUMBER`)

**Q:** Which data type is used for text in databases?
**A:** `TEXT` (SQLite) or `VARCHAR2` (Oracle)

**Q:** What constraint ensures a row is unique (like a fingerprint)?
**A:** `PRIMARY KEY`

### Lesson 2: Data Entry (INSERT)
**Q:** Text strings in SQL must be wrapped in ______ quotes.
**A:** `'Single'`

**Q:** True or False: Numbers need quotes (e.g., '10').
**A:** False. (Numbers are naked).

### Lesson 3: The Filter (WHERE)
**Q:** What symbol means "Not Equal To" in SQL?
**A:** `<>` (or `!=`)

**Q:** To find rows where text matches exactly 'Rahul', which operator do we use?
**A:** `=`

### Lesson 4: The Void (NULL)
**Q:** Does `NULL` equal `0`?
**A:** No. `NULL` means **Unknown**.

**Q:** What is the result of `5000 + NULL`?
**A:** `NULL`

**Q:** What is the "Golden Rule" for finding NULLs in a WHERE clause?
**A:** Always use `IS NULL` (Never use `= NULL`).

**Q:** Which function converts a NULL value to a number (like 0) in SQLite?
**A:** `IFNULL(Column, 0)`  *(Oracle: `NVL`)*

---
*Status: Ready for review via Anki or Self-Quiz.*
