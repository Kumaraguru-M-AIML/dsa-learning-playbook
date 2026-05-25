# 📓 Sol's SQL Notebook: Laboratory & Scratchpad
*Active Learning & Session Notes*

---

## 🧪 Session 1: The Genesis
**Objective:** Create a table, insert a row, and read it back.

### 🏗️ Laborary Task: The "Starfleet" Table
We are building a table for a space crew.

#### Step 1: CREATE
```sql
CREATE TABLE Crew (
    Rank_ID NUMBER,
    Name VARCHAR2(100),
    Specialty VARCHAR2(50)
);
```

#### Step 2: INSERT
```sql
INSERT INTO Crew (Rank_ID, Name, Specialty)
VALUES (101, 'Sol', 'System Architect');
```

#### Step 3: SELECT (The Wildcard)
```sql
SELECT * FROM Crew;
```

---

## 🚩 My Failure Modes (Bugs encountered)
*   *Pending...* (We will record errors here to build metacognition).

---
## 💡 Lightning Round Memory Bank
1. What does `*` mean in `SELECT *`?
2. Why did the query fail when I forgot the single quote?
3. What is the difference between `NUMBER` and `VARCHAR2`?
