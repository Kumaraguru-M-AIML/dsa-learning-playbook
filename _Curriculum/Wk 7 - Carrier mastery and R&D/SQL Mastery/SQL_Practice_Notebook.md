# 🧪 SQL Practice Notebook
*Live Lab Interface - DB Browser (SQLite)*

---

## ⚙️ Setup Status
- **Tool:** DB Browser for SQLite ✅
- **Database Created:** ✅ Active
- **Tables Active:** `Assassin_Guild` (3 rows)

---

## 📋 Drill Submission Format
For each drill, paste:
1. **The Query** (Code Block)
2. **The Output** (Table or Screenshot description)
3. **Status:** ✅ Success / ❌ Error

---

## 🏗️ DRILL 0: Environment Setup
**Objective:** Create the `Assassin_Guild` table and populate it with sample data.

### Step 1: Create the Table
```sql
CREATE TABLE Assassin_Guild (
    Agent_Name VARCHAR(50),
    Kill_Count INTEGER,
    Entry_Date TEXT
);
```

### Step 2: Insert Sample Data
```sql
INSERT INTO Assassin_Guild (Agent_Name, Kill_Count, Entry_Date) VALUES ('Ayanokoji', 0, '2026-02-08');
INSERT INTO Assassin_Guild (Agent_Name, Kill_Count, Entry_Date) VALUES ('Vahn', 999, '2026-02-08');
INSERT INTO Assassin_Guild (Agent_Name, Kill_Count, Entry_Date) VALUES ('Sol', 50, '2026-01-15');
```

### Step 3: Verify Data
```sql
SELECT * FROM Assassin_Guild;
```

**Expected Output:**
| Agent_Name | Kill_Count | Entry_Date |
| :--- | :--- | :--- |
| Ayanokoji | 0 | 2026-02-08 |
| Vahn | 999 | 2026-02-08 |
| Sol | 50 | 2026-01-15 |

### Your Submission:
> 
![[Pasted image 20260209000749.png]]
**Status:** ✅ Success - Environment Ready!

---

## 🎯 DRILL 1: The WHERE Filter
**Objective:** Practice conditional filtering.

### Task 1.1: Find agents with 0 kills
```sql
SELECT * FROM Assassin_Guild;SELECT * FROM Assassin_Guild WHERE Kill_Count=0;
```
**Your Output:**
> *Paste result here*![[Pasted image 20260209001034.png]]

### Task 1.2: Find the agent named 'Vahn'
```sql
SELECT * FROM Assassin_Guild where Agent_Name='vahn';
```
**Your Output:**
> *Paste result here*![[Pasted image 20260209001134.png]]

### Task 1.3: Find agents with Kill_Count > 10
```sql
SELECT * FROM Assassin_Guild where Kill_Count > 10;
```
**Your Output:**
> *Paste result here*![[Pasted image 20260209001217.png]]

**Status:** ✅ Success - WHERE Clause Mastered!

---
*This notebook is your live lab. Vahn is watching.*
-- Find agents with MORE than 10 kills AND joined in 2026:
SELECT * FROM Assassin_Guild 
WHERE Kill_Count > 10 AND Entry_Date = '2026-02-08';
![[Pasted image 20260209001514.png]]
-- Find agents named 'Sol' OR 'Vahn':
SELECT * FROM Assassin_Guild 
WHERE Agent_Name = 'Sol' OR Agent_Name = 'Vahn';
![[Pasted image 20260209001540.png]]
### 🛠️ **DRILL 2: Boolean Logic (Add to your Notebook)**

**Task 2.1:** Find agents who have **more than 0 kills AND joined on '2026-02-08'**. **Task 2.2:** Find agents named **'Ayanokoji' OR 'Sol'**. **Task 2.3:** Find agents whose `Kill_Count` is **less than 100 AND greater than 0**.

**Execute in DB Browser, paste results, and signal when done.**
![[Pasted image 20260209001859.png]]

-------
----


# Phase_1_Mastery_Assessment


## 🧪 **PART 1: CONCEPTUAL QUESTIONS (5 QUESTIONS)**
1. B ) NUMBER 
2. A) All employees with NULL salary  
3. D) Both B and C are correct
4. D) First returns all columns, second returns specific columns
5. B) `WHERE weight >= 2 AND weight <= 5`  

## 💻 **PART 2: PRACTICAL QUERIES (10 QUESTIONS)**
### **Query 1: Basic SELECT**
![[Pasted image 20260214085029.png]]

### **Query 2: WHERE with Comparison**
![[Pasted image 20260214085212.png]]

q3 

![[Pasted image 20260214085337.png]]

Q4 
![[Pasted image 20260214085447.png]]

Q5
![[Pasted image 20260214085601.png]]

Q6
![[Pasted image 20260214085658.png]]
Q7
![[Pasted image 20260214085747.png]]
Q8
![[Pasted image 20260214085949.png]]

Q9
