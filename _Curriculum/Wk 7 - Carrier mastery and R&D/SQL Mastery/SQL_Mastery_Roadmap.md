# 🗺️ Oracle SQL Mastery Roadmap
*From Zero to Database Architect*

## 🎯 The Ultimate Goal
To achieve **Data Fluency**. You will not just "know code"; you will possess the ability to look at raw, messy data and instantly visualize how to clean, structure, manage, and extract valuable insights from it. You will be able to answer complex business questions ("Who are our top customers?" "Why did sales drop?") in seconds.

---

## 🟢 PHASE 1: THE FOUNDATION (Data Literacy)
*Goal: To store information correctly and ask basic questions.*
*Superpower: You effectively replace Excel for basic tasks.*

### 1.1 The Genesis (DDL - Data Definition Language)
Before data exists, the container must exist.
- [x] **Relational Theory**: Understanding Tables, Rows (Records), and Columns (Fields).
- [x] **Data Types**:
    - [x] `NUMBER`/`INTEGER`: Math-able data.
    - [x] `VARCHAR2`/`TEXT`: Strings and characters.
    - [ ] `DATE`: Handling time (Crucial in Oracle).
- [x] **Constraints**:
    - [x] `PRIMARY KEY`: The unique fingerprint of a row.
    - [ ] `NOT NULL`: Forcing data entry (preventing blanks).
- [x] **Syntax**: Writing `CREATE TABLE` commands.

### 1.2 Data Manipulation (DML - Data Manipulation Language)
Putting data in and taking it out.
- [x] **Insertion**: Using `INSERT INTO` to populate tables.
- [x] **Handling Strings**: The importance of Single Quotes (`' '`).
- [x] **Querying**:
    - [x] `SELECT *`: The wildcard (viewing raw data).
    - [x] `SELECT Column`: The projection (viewing specific data).

### 1.3 The Filter (Conditional Logic)
Finding a needle in a haystack.
- [x] **Equality**: `WHERE name = 'X'`.
- [x] **Comparison**: Greater than (`>`), Less than (`<`).
- [x] **Exclusion**: Not equal to (`<>`, `!=`).
- [x] **Boolean Logic**:
    - [ ] `AND`: Both conditions must be true.
    - [ ] `OR`: At least one condition must be true.
    - [ ] `IN`: Checking against a list (`IN (10, 11, 12)`).

### 1.4 The Void (NULL Handling)
Understanding the concept of "Unknown".
- [x] **The Trap**: Why `NULL != NULL` and why math fails with NULL.
- [x] **The Detection**: Using `IS NULL` and `IS NOT NULL`.
- [x] **The Fix**: Using `NVL()` (Oracle) or `IFNULL()` (SQLite) to sanitize data.

### 1.5 Presentation & Formatting
Making the output readable for humans.
- [ ] **Concatenation**: Merging columns (`||`) to create readable sentences.
- [ ] **Aliases**: Renaming columns (`AS "Total Pay"`) for reports.
- [ ] **Sorting**: Using `ORDER BY` (`ASC`/`DESC`) to rank data.
- [ ] **Limiting**: Fetching top N rows (`FETCH FIRST` / `LIMIT`).

---

## 🟡 PHASE 2: THE ANALYST (Intermediate)
*Goal: Summarize data and do math on groups of rows.*

- [ ] **2.1 String Functions**
    - [ ] `UPPER()`, `LOWER()`, `INITCAP()`
    - [ ] `SUBSTR()` (Cutting text)
    - [ ] `LENGTH()` (Counting characters)
- [ ] **2.2 The Aggregators (Math)**
    - [ ] `COUNT(*)` (How many rows?)
    - [ ] `SUM()` (Total)
    - [ ] `AVG()` (Average)
    - [ ] `MAX()` / `MIN()`
- [ ] **2.3 Grouping (GROUP BY)**
    - [ ] Grouping data (e.g., "Count students per Grade")
    - [ ] The `HAVING` clause (Filtering groups, not rows)

---

## 🟠 PHASE 3: THE RELATIONAL MIND (Advanced)
*Goal: Connecting multiple tables together.*

- [ ] **3.1 The Concept of Keys**
    - [ ] Primary Keys (PK) vs Foreign Keys (FK)
- [ ] **3.2 Inner Joins (INNER JOIN)**
    - [ ] Connecting Table A and Table B
- [ ] **3.3 Outer Joins (LEFT / RIGHT / FULL)**
    - [ ] Finding data even when there is no match
- [ ] **3.4 Self Joins**
    - [ ] Joining a table to itself (e.g. Employee & Manager)

---

## 🔴 PHASE 4: THE ARCHITECT (Expert)
*Goal: Complex logic, subqueries, and database manipulation.*

- [ ] **4.1 Subqueries (Inception)**
    - [ ] A query inside a query
- [ ] **4.2 Set Operators**
    - [ ] `UNION`, `UNION ALL`
    - [ ] `INTERSECT`, `MINUS`
- [ ] **4.3 Case Statements (Logic)**
    - [ ] `CASE WHEN... THEN... ELSE... END`
- [ ] **4.4 DML & DDL (Changing Structure)**
    - [ ] `UPDATE` (Modifying rows)
    - [ ] `DELETE` (Removing rows)
    - [ ] `ALTER TABLE` (Adding columns later)
    - [ ] `DROP TABLE` (Destroying everything)

---
*Check off items as we master them!*
