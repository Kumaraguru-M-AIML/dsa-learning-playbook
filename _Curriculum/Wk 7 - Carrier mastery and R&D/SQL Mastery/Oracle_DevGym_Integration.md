# 🎓 **ORACLE DEV GYM → SOL'S MASTERY INTEGRATION**
*Complete Curriculum Synthesis from Oracle's "Databases for Developers"*

---

## 📊 **CURRICULUM ARCHITECTURE**

This document integrates the **Oracle Dev Gym** playlist into your existing SQL Mastery framework. The Oracle course has **14 Episodes** covering everything from table types to advanced analytics.

---

## 🗺️ **COMPLETE EPISODE MAP**

| Episode | Topic | Your Current Status | Integration Point |
| :--- | :--- | :--- | :--- |
| **1** | Table Types (Heap, IOT, External, Temp, Partitioned, Clusters) | ✅ Covered in Phase 2 | Advanced Tables |
| **2** | Columns & Data Types | ✅ Covered in Phase 1 | Foundations |
| **3** | Data Modeling (Relational vs Document) | 🆕 NEW | Phase 3 (Design) |
| **4** | SELECT & WHERE | ✅ Mastered (1.3-1.5) | Foundations |
| **5** | JOINS (INNER, LEFT, RIGHT, FULL) | 🆕 NEW | Phase 3 (Relationships) |
| **6** | Aggregation (GROUP BY, HAVING, ROLLUP) | 🆕 NEW | Phase 3 (Analytics) |
| **7** | INSERT & Transactions (COMMIT/ROLLBACK) | ✅ Covered (1.2) | Foundations |
| **8** | UPDATE & Concurrency (Deadlocks, Optimistic Locking) | 🆕 NEW | Phase 4 (Advanced DML) |
| **9** | DELETE vs TRUNCATE & Soft Deletes | 🆕 NEW | Phase 4 (Data Management) |
| **10** | NULL (Three-Valued Logic, NVL, COALESCE) | ✅ Current Lesson (1.6) | Foundations |
| **11** | Subqueries & WITH (CTEs) | 🆕 NEW | Phase 5 (Advanced Queries) |
| **12** | ORDER BY & Top-N (FETCH FIRST, ROWNUM) | 🆕 NEW | Phase 5 (Result Control) |
| **13** | Analytic Functions (Window Functions, PARTITION BY) | 🆕 NEW | Phase 6 (Analytics Pro) |
| **14** | PIVOT/UNPIVOT | 🆕 NEW | Phase 6 (Data Transformation) |

---

## 🎯 **YOUR LEARNING PATH (OPTIMIZED)**

### **✅ PHASE 1: FOUNDATIONS (COMPLETE)**
- Data Types ✅
- CREATE TABLE ✅
- INSERT ✅
- SELECT ✅
- WHERE ✅
- NULL (Current: 1.6) 🔄

### **🆕 PHASE 2: ADVANCED TABLES (DEPLOYED)**
- Heap Tables
- Index-Organized Tables (IOT)
- External Tables
- Temporary Tables (GTT/PTT)
- Partitioned Tables
- Table Clusters

**Status:** Tutorial created (`Phase_2_Advanced_Tables.md`)

### **🆕 PHASE 3: RELATIONSHIPS & ANALYTICS**

#### **Module 3.1: Data Modeling**
- Relational vs Document modeling
- Normalization principles
- Entity-Relationship design
- When to separate vs combine tables

#### **Module 3.2: JOINS**
- Cross Join (Cartesian Product)
- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- FULL OUTER JOIN
- **Critical Trap:** WHERE vs ON in outer joins

#### **Module 3.3: Aggregation**
- COUNT, SUM, MIN, MAX, AVG
- GROUP BY rules
- HAVING vs WHERE
- ROLLUP (subtotals)
- COUNT(*) vs COUNT(column)

---

### **🆕 PHASE 4: DATA MODIFICATION MASTERY**

#### **Module 4.1: UPDATE & Concurrency**
- UPDATE syntax
- Concurrency control
- Locking mechanisms
- Deadlock prevention
- Optimistic locking (version columns)
- FOR UPDATE clause

#### **Module 4.2: DELETE Strategies**
- DELETE vs TRUNCATE
- Soft deletes (logical deletion)
- Audit trails
- Views for soft-deleted data
- VPD (Virtual Private Database)

---

### **🆕 PHASE 5: ADVANCED QUERY MECHANICS**

#### **Module 5.1: Subqueries**
- Inline views (subquery in FROM)
- WITH clause (CTEs)
- Subqueries in WHERE (IN, EXISTS)
- Correlated subqueries
- Scalar subqueries
- **Critical Trap:** NOT IN with NULL

#### **Module 5.2: Result Control**
- ORDER BY (ASC/DESC)
- NULL ordering (NULLS FIRST/LAST)
- Custom sort (CASE in ORDER BY)
- Top-N queries (FETCH FIRST)
- ROWNUM (pre-12c)
- Deterministic sorting

---

### **🆕 PHASE 6: ANALYTICS & TRANSFORMATION**

#### **Module 6.1: Analytic (Window) Functions**
- PARTITION BY (grouping without collapse)
- Running totals
- RANGE vs ROWS
- LAG/LEAD (access previous/next rows)
- RANK, DENSE_RANK, ROW_NUMBER
- Moving averages

#### **Module 6.2: Data Transformation**
- PIVOT (rows → columns)
- UNPIVOT (columns → rows)
- Dynamic pivoting
- Crosstab reports

---

## 🔥 **KEY CONCEPTS FROM ORACLE DEV GYM**

### **1. The Three-Valued Logic Trap (Episode 10)**
```sql
-- WRONG
WHERE stuffing = NULL;  -- Always UNKNOWN

-- CORRECT
WHERE stuffing IS NULL;
```

**Critical Rule:** NULL comparisons return UNKNOWN, not FALSE.

---

### **2. The Outer Join WHERE Trap (Episode 5)**
```sql
-- WRONG (turns LEFT JOIN into INNER JOIN)
LEFT JOIN bricks b ON t.color = b.color
WHERE b.shape = 'cube';

-- CORRECT
LEFT JOIN bricks b
  ON t.color = b.color
 AND b.shape = 'cube';
```

**Rule:** Filtering on the outer table must go in the ON clause, not WHERE.

---

### **3. The NOT IN NULL Trap (Episode 11)**
```sql
-- DANGEROUS
WHERE color NOT IN (SELECT color FROM table);
-- If subquery returns even ONE NULL → entire result is empty

-- SAFE
WHERE NOT EXISTS (
    SELECT 1 FROM table WHERE table.color = outer.color
);
```

---

### **4. The ROWNUM Top-N Trap (Episode 12)**
```sql
-- WRONG (picks 3 random rows, then sorts)
SELECT * FROM bricks
WHERE ROWNUM <= 3
ORDER BY weight DESC;

-- CORRECT (sorts first, then limits)
SELECT * FROM (
    SELECT * FROM bricks ORDER BY weight DESC
)
WHERE ROWNUM <= 3;

-- BEST (12c+)
SELECT * FROM bricks
ORDER BY weight DESC
FETCH FIRST 3 ROWS ONLY;
```

---

### **5. Optimistic Locking Pattern (Episode 8)**
```sql
UPDATE accounts
SET balance = balance - 100,
    version = version + 1
WHERE account_id = 1
  AND version = 3;  -- Fails if someone else updated

-- Check rows affected
-- If 0 → concurrent modification detected
```

---

## 📚 **STRATEGIC LEARNING SEQUENCE**

### **Immediate Next Steps:**
1. ✅ **Complete Lesson 1.6 (NULL)** — You're 85% done with Phase 1
2. 🎯 **Deploy Phase 3.2 (JOINS)** — This is the gateway to real SQL power
3. 🎯 **Deploy Phase 3.3 (Aggregation)** — GROUP BY is essential for analytics

### **Week 2:**
4. 🎯 **Phase 5.1 (Subqueries & CTEs)** — Professional query structure
5. 🎯 **Phase 5.2 (ORDER BY & Top-N)** — Result control

### **Week 3:**
6. 🎯 **Phase 6.1 (Window Functions)** — Advanced analytics without GROUP BY collapse
7. 🎯 **Phase 4 (UPDATE/DELETE Mastery)** — Production-grade data modification

---

## 🧠 **MENTAL MODELS FROM ORACLE**

### **Table Type = Physical Storage Strategy**
- Heap → General purpose, unordered
- IOT → Sorted by primary key
- External → Read files as tables
- Temporary → Session-private data
- Partitioned → Segmented for scale
- Clustered → Multiple tables, shared storage

### **Query Processing Order**
```
1. FROM       (identify tables)
2. WHERE      (filter rows)
3. GROUP BY   (create groups)
4. HAVING     (filter groups)
5. SELECT     (choose columns)
6. ORDER BY   (sort results)
7. FETCH      (limit results)
```

### **JOIN Mental Model**
- INNER → Intersection (only matches)
- LEFT → All from left + matches from right
- RIGHT → All from right + matches from left
- FULL → Union (all from both)

### **NULL Philosophy**
- NULL ≠ 0
- NULL ≠ ''
- NULL ≠ FALSE
- NULL = "unknown" or "not applicable"

---

## 🎯 **PRACTICE DRILLS (FROM ORACLE)**

### **Drill 1: Data Modeling**
**Scenario:** Library database
- Should books and authors be in one table or separate?
- **Answer:** Separate (one author can write many books; avoid duplication)

### **Drill 2: Aggregation**
**Table:**
| order_id | customer | amount |
| :--- | :--- | :--- |
| 1 | A | 100 |
| 2 | A | 50 |
| 3 | B | 200 |

**Query 1:** Total per customer
```sql
SELECT customer, SUM(amount)
FROM orders
GROUP BY customer;
```

**Query 2:** Customers with total > 120
```sql
SELECT customer, SUM(amount)
FROM orders
GROUP BY customer
HAVING SUM(amount) > 120;
```

### **Drill 3: Optimistic Locking**
**Table:**
| account_id | balance | version |
| :--- | :--- | :--- |
| 1 | 500 | 2 |

**Task:** Deduct 100 with version check
```sql
UPDATE accounts
SET balance = balance - 100,
    version = version + 1
WHERE account_id = 1
  AND version = 2;
```

### **Drill 4: NULL Behavior**
**Table:**
| id | marks |
| :--- | :--- |
| 1 | 80 |
| 2 | NULL |
| 3 | 50 |

**Question 1:** `SELECT COUNT(marks) FROM table;`
**Answer:** 2 (NULL ignored)

**Question 2:** `SELECT COUNT(*) FROM table;`
**Answer:** 3 (counts all rows)

---

## 🔧 **NEXT TUTORIAL DEPLOYMENT**

Would you like me to create:

1. **Phase 3.2: JOINS Mastery** (INNER, LEFT, RIGHT, FULL + traps)
2. **Phase 3.3: Aggregation Mastery** (GROUP BY, HAVING, ROLLUP)
3. **Phase 5.1: Subqueries & CTEs** (WITH clause, EXISTS, IN)
4. **Phase 6.1: Window Functions** (PARTITION BY, LAG/LEAD, RANK)

**Or continue with Lesson 1.6 (NULL) to complete Phase 1 first?**

---

*Vahn's Cortex — Oracle Dev Gym Integration v1.0*
*Source: Oracle Dev Gym "Databases for Developers" (14 Episodes)*
