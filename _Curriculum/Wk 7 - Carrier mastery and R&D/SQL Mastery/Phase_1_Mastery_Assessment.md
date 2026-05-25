# 🎯 **PHASE 1 MASTERY ASSESSMENT**
*Test What You've Learned Before Moving Forward*

---

## 📊 **WHAT THIS TESTS**

Your Phase 1 knowledge:
- ✅ Lesson 1.1: Data Types (NUMBER, VARCHAR2, DATE)
- ✅ Lesson 1.2: CREATE TABLE & INSERT
- ✅ Lesson 1.3: SELECT (specific columns, all columns)
- ✅ Lesson 1.4: WHERE Clause
- ✅ Lesson 1.5: AND/OR Operators
- 🔄 Lesson 1.6: NULL Handling

**Time Limit:** 30-45 minutes  
**Passing Score:** 80% (16/20 correct)

---

## 🧪 **PART 1: CONCEPTUAL QUESTIONS (5 QUESTIONS)**

### **Question 1: Data Types**
Which data type would you use to store a person's age?

A) VARCHAR2(3)  
B) NUMBER  
C) DATE  
D) CHAR(2)

<details>
<summary>Answer</summary>
**B) NUMBER**

Explanation: Age is a numeric value. VARCHAR2 would work but is inefficient (stores as text). DATE is for dates, not ages.
</details>

---

### **Question 2: NULL Behavior**
What does this query return?

```sql
SELECT * FROM employees WHERE salary = NULL;
```

A) All employees with NULL salary  
B) All employees  
C) No rows  
D) Error

<details>
<summary>Answer</summary>
**C) No rows**

Explanation: `= NULL` is always UNKNOWN (not TRUE). Correct syntax is `WHERE salary IS NULL`.
</details>

---

### **Question 3: Logical Operators**
What's the difference between these two queries?

```sql
-- Query 1
WHERE color = 'Red' OR color = 'Blue' AND weight > 5

-- Query 2
WHERE (color = 'Red' OR color = 'Blue') AND weight > 5
```

A) They're identical  
B) Query 1 returns Red toys OR (Blue toys with weight > 5)  
C) Query 2 returns (Red OR Blue) toys with weight > 5  
D) Both B and C are correct

<details>
<summary>Answer</summary>
**D) Both B and C are correct**

Explanation: AND has higher precedence than OR. Query 1 = `Red OR (Blue AND weight>5)`. Query 2 uses parentheses to force `(Red OR Blue) AND weight>5`.
</details>

---

### **Question 4: SELECT Behavior**
What's the difference between these?

```sql
SELECT * FROM toys;
SELECT toy_name, color FROM toys;
```

A) First is faster  
B) Second is faster  
C) They return the same data  
D) First returns all columns, second returns specific columns

<details>
<summary>Answer</summary>
**D) First returns all columns, second returns specific columns**

Bonus: The second is also typically faster (less data transfer) and is considered better practice.
</details>

---

### **Question 5: WHERE Clause**
Which query finds toys with weight between 2 and 5 (inclusive)?

A) `WHERE weight > 2 AND weight < 5`  
B) `WHERE weight >= 2 AND weight <= 5`  
C) `WHERE weight BETWEEN 2 AND 5`  
D) Both B and C

<details>
<summary>Answer</summary>
**D) Both B and C**

Explanation: BETWEEN is inclusive (includes 2 and 5). Option A excludes 2 and 5.
</details>

---

## 💻 **PART 2: PRACTICAL QUERIES (10 QUESTIONS)**

### **Setup: Create Test Database**

Run this first:

```sql
-- Assassins Guild Database
CREATE TABLE assassins (
    assassin_id NUMBER PRIMARY KEY,
    name VARCHAR2(100) NOT NULL,
    rank VARCHAR2(50),
    kill_count NUMBER,
    entry_date DATE,
    active NUMBER(1)  -- 1 = active, 0 = retired, NULL = unknown
);

INSERT INTO assassins VALUES (1, 'Ezio Auditore', 'Master', 287, DATE '2010-01-15', 1);
INSERT INTO assassins VALUES (2, 'Altair Ibn-La''Ahad', 'Grandmaster', 412, DATE '2007-11-13', 0);
INSERT INTO assassins VALUES (3, 'Connor Kenway', 'Assassin', 156, DATE '2012-10-30', 1);
INSERT INTO assassins VALUES (4, 'Edward Kenway', 'Captain', 203, DATE '2013-10-29', NULL);
INSERT INTO assassins VALUES (5, 'Bayek of Siwa', 'Medjay', 189, DATE '2017-10-27', 1);
INSERT INTO assassins VALUES (6, 'Kassandra', 'Misthios', 301, DATE '2018-10-05', 1);
INSERT INTO assassins VALUES (7, 'Eivor Varinsdottir', 'Drengr', NULL, DATE '2020-11-10', 1);

COMMIT;
```

---

### **Query 1: Basic SELECT**
**Task:** Select all assassin names.

```sql
-- Your answer:
```

<details>
<summary>Solution</summary>

```sql
SELECT name FROM assassins;
```
</details>

---

### **Query 2: WHERE with Comparison**
**Task:** Find assassins with kill_count greater than 200.

```sql
-- Your answer:
```

<details>
<summary>Solution</summary>

```sql
SELECT name, kill_count
FROM assassins
WHERE kill_count > 200;
```
</details>

---

### **Query 3: WHERE with Equality**
**Task:** Find the assassin with rank 'Master'.

```sql
-- Your answer:
```

<details>
<summary>Solution</summary>

```sql
SELECT name, rank
FROM assassins
WHERE rank = 'Master';
```
</details>

---

### **Query 4: AND Operator**
**Task:** Find active assassins (active = 1) with kill_count > 200.

```sql
-- Your answer:
```

<details>
<summary>Solution</summary>

```sql
SELECT name, kill_count
FROM assassins
WHERE active = 1
  AND kill_count > 200;
```
</details>

---

### **Query 5: OR Operator**
**Task:** Find assassins who are either 'Master' rank OR have kill_count > 300.

```sql
-- Your answer:
```

<details>
<summary>Solution</summary>

```sql
SELECT name, rank, kill_count
FROM assassins
WHERE rank = 'Master'
   OR kill_count > 300;
```
</details>

---

### **Query 6: IS NULL**
**Task:** Find assassins with unknown kill_count (NULL).

```sql
-- Your answer:
```

<details>
<summary>Solution</summary>

```sql
SELECT name, kill_count
FROM assassins
WHERE kill_count IS NULL;
```
</details>

---

### **Query 7: IS NOT NULL**
**Task:** Find assassins with known active status (NOT NULL).

```sql
-- Your answer:
```

<details>
<summary>Solution</summary>

```sql
SELECT name, active
FROM assassins
WHERE active IS NOT NULL;
```
</details>

---

### **Query 8: Complex AND/OR**
**Task:** Find assassins who are:
- Active (active = 1) AND have kill_count > 150
- OR have rank 'Grandmaster'

```sql
-- Your answer:
```

<details>
<summary>Solution</summary>

```sql
SELECT name, rank, kill_count, active
FROM assassins
WHERE (active = 1 AND kill_count > 150)
   OR rank = 'Grandmaster';
```
</details>

---

### **Query 9: Date Filtering**
**Task:** Find assassins who joined after January 1, 2015.

```sql
-- Your answer:
```

<details>
<summary>Solution</summary>

```sql
SELECT name, entry_date
FROM assassins
WHERE entry_date > DATE '2015-01-01';
```
</details>

---

### **Query 10: Multiple Columns**
**Task:** Select name, rank, and kill_count for all assassins, ordered by name.

```sql
-- Your answer:
```

<details>
<summary>Solution</summary>

```sql
SELECT name, rank, kill_count
FROM assassins
ORDER BY name;
```

**Note:** ORDER BY is technically Lesson 1.7, but if you know it, great! If not, just omit the ORDER BY clause.
</details>

---

## 🔧 **PART 3: DEBUGGING CHALLENGES (5 QUESTIONS)**

### **Challenge 1: Find the Error**
What's wrong with this query?

```sql
SELECT name, kill_count
FROM assassins
WHERE kill_count = NULL;
```

<details>
<summary>Answer</summary>
**Error:** Cannot use `= NULL`. Must use `IS NULL`.

**Corrected:**
```sql
SELECT name, kill_count
FROM assassins
WHERE kill_count IS NULL;
```
</details>

---

### **Challenge 2: Find the Error**
What's wrong with this CREATE TABLE?

```sql
CREATE TABLE missions (
    mission_id NUMBER,
    target VARCHAR2,
    completed DATE
);
```

<details>
<summary>Answer</summary>
**Error:** VARCHAR2 requires a size (e.g., VARCHAR2(100)).

**Corrected:**
```sql
CREATE TABLE missions (
    mission_id NUMBER,
    target VARCHAR2(100),
    completed DATE
);
```
</details>

---

### **Challenge 3: Find the Error**
What's wrong with this INSERT?

```sql
INSERT INTO assassins
VALUES ('Desmond Miles', 'Novice', 5);
```

<details>
<summary>Answer</summary>
**Error:** Missing columns (assassin_id, entry_date, active) and wrong order.

**Corrected:**
```sql
INSERT INTO assassins (name, rank, kill_count)
VALUES ('Desmond Miles', 'Novice', 5);
```

Or provide all columns in correct order.
</details>

---

### **Challenge 4: Logic Error**
This query should find active assassins with kill_count > 200, but returns wrong results. Why?

```sql
SELECT name
FROM assassins
WHERE active = 1 OR kill_count > 200;
```

<details>
<summary>Answer</summary>
**Logic Error:** OR should be AND. Current query returns assassins who are active OR have high kill count (not both).

**Corrected:**
```sql
SELECT name
FROM assassins
WHERE active = 1 AND kill_count > 200;
```
</details>

---

### **Challenge 5: NULL Trap**
Why does this query return 0 rows even though Eivor has NULL kill_count?

```sql
SELECT name
FROM assassins
WHERE kill_count < 300;
```

<details>
<summary>Answer</summary>
**NULL Trap:** `NULL < 300` evaluates to UNKNOWN (not TRUE), so Eivor is excluded.

**To include NULL:**
```sql
SELECT name
FROM assassins
WHERE kill_count < 300 OR kill_count IS NULL;
```
</details>

---

## 📊 **SCORING GUIDE**

### **Part 1: Conceptual (5 points)**
- 1 point per correct answer
- Passing: 4/5

### **Part 2: Practical (10 points)**
- 1 point per correct query
- Passing: 8/10

### **Part 3: Debugging (5 points)**
- 1 point per correct fix
- Passing: 4/5

### **Total: 20 points**
- **16-20:** ✅ **MASTERY** — Ready for Critical Path
- **12-15:** ⚠️ **REVIEW** — Revisit weak areas, then retest
- **0-11:** ❌ **STUDY** — Review Phase 1 lessons before advancing

---

## 🎯 **AFTER THE TEST**

### **If You Pass (16+):**
1. ✅ Update `My_Progress_Log.md`
2. ✅ Mark Phase 1 as COMPLETE
3. 🎯 **Start Critical Path** (Module 1: JOINS)

### **If You Need Review (12-15):**
1. Identify weak areas (NULL? AND/OR? WHERE?)
2. Review specific lessons
3. Retake test in 1-2 days

### **If You Need Study (0-11):**
1. Review all Phase 1 lessons
2. Practice more queries
3. Retake test in 3-5 days

---

## 📝 **SELF-ASSESSMENT TEMPLATE**

Copy this to `My_Progress_Log.md`:

```markdown
## Phase 1 Mastery Assessment — 2026-02-13

**Part 1 (Conceptual):** __/5
**Part 2 (Practical):** __/10
**Part 3 (Debugging):** __/5
**TOTAL:** __/20

**Result:** [MASTERY / REVIEW / STUDY]

**Strengths:**
- 

**Weaknesses:**
- 

**Action Plan:**
- 

**Ready for Critical Path?** [YES / NO]
```

---

## 🔥 **BONUS CHALLENGE (OPTIONAL)**

If you scored 18+, try this advanced query:

**Task:** Find assassins who:
- Are active (active = 1)
- Have kill_count between 150 and 300 (inclusive)
- Joined after 2010
- Have a known kill_count (NOT NULL)

```sql
-- Your answer:
```

<details>
<summary>Solution</summary>

```sql
SELECT name, rank, kill_count, entry_date
FROM assassins
WHERE active = 1
  AND kill_count BETWEEN 150 AND 300
  AND entry_date > DATE '2010-01-01'
  AND kill_count IS NOT NULL;
```
</details>

---

**Ready to begin the assessment, Sol?** 🎯

*Phase 1 Mastery Assessment | Active Recall Protocol*  
*"Test Before You Progress"*
