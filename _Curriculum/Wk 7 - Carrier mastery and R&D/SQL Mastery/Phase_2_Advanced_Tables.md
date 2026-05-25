# 🏛️ **PHASE 2: ADVANCED TABLES — THE ARCHITECT'S VAULT**
*From Basic Builder to Database Architect*

---

## 📚 **SOURCE MATERIALS**
This tutorial synthesizes knowledge from:
1. **Oracle FreeSQL Tutorial:** "Creating Tables: Databases for Developers"  
   URL: `https://freesql.com/library/tutorials/creating-tables-databases-for-developers-SQru0F`
2. **Oracle Dev Gym Course:** "Databases for Developers" (Episode 1: Table Types)  
   Source: `E:\Wk 7 - Carrier mastery and R&D\Sql courses from oracle\Databases for Developers- dev gym\YT notes from playlist.md`

Both are official Oracle educational resources, integrated into Sol's learning architecture.

---

## 📍 **Your Current Position**
- ✅ **Phase 1 Complete:** You know `CREATE TABLE`, `INSERT`, `SELECT`, `WHERE`, and `NULL`.
- 🎯 **Phase 2 Objective:** Master **Industrial-Grade Table Architecture** used by Oracle developers worldwide.

---

## 🧠 **The Mental Model: Tables Are Not Just Tables**

In Phase 1, you learned that a table is like a **filing cabinet**.

In Phase 2, you'll learn that Oracle gives you **7 different types of filing cabinets**, each optimized for different scenarios:

| Cabinet Type | When to Use | Real-World Example |
| :--- | :--- | :--- |
| **Heap Table** (Default) | General purpose, no special order | Employee records |
| **Index-Organized Table (IOT)** | Data must be sorted by ID | Product catalog (sorted by Product_ID) |
| **External Table** | Reading CSV/TXT files without importing | Analyzing server logs |
| **Global Temporary Table (GTT)** | Session-specific staging data | Shopping cart during checkout |
| **Private Temporary Table (PTT)** | Ultra-private session data (18c+) | Calculation scratch space |
| **Partitioned Table** | Massive datasets (millions of rows) | 10 years of sales data (partitioned by month) |
| **Clustered Table** | Multiple tables sharing physical space | Orders + Order_Items stored together |

---

## 📚 **MODULE 1: THE FOUNDATION — HEAP TABLES**

### **What You Already Know:**
```sql
CREATE TABLE Assassin_Guild (
    Agent_Name VARCHAR2(100),
    Kill_Count NUMBER,
    Entry_Date DATE
);
```

This is a **Heap Table** (the default). The database stores rows **wherever there is space** — no guaranteed order.

### **When to Use:**
- 99% of the time. This is your default choice.
- When you don't need rows in a specific physical order.

### **Explicit Syntax (Optional):**
```sql
CREATE TABLE Toys_Heap (
    Toy_Name VARCHAR2(100)
) ORGANIZATION HEAP;
```

---

## 📚 **MODULE 2: INDEX-ORGANIZED TABLES (IOT)**

### **The Problem:**
Imagine you have a **Product Catalog** with 1 million products. Users always search by `Product_ID`. 

With a heap table, the database has to **scan randomly** to find Product_ID = 12345.

### **The Solution: IOT**
An **Index-Organized Table** physically stores rows **sorted by the Primary Key**. This makes lookups by PK **lightning fast**.

### **The Syntax:**
```sql
CREATE TABLE Products_IOT (
    Product_ID   INTEGER PRIMARY KEY,
    Product_Name VARCHAR2(100),
    Price        NUMBER
) ORGANIZATION INDEX;
```

### **The Rules:**
1. ✅ **MUST have a Primary Key** (this is what it sorts by).
2. ✅ Rows are stored **in PK order** on disk.
3. ⚠️ **Trade-off:** Inserts can be slower (because it has to maintain order).

### **When to Use:**
- Lookup tables (Country Codes, Product IDs).
- Tables where you **always** query by the Primary Key.

### **Verification:**
```sql
SELECT table_name, iot_type
FROM user_tables
WHERE table_name = 'PRODUCTS_IOT';
```
**Output:**
```
TABLE_NAME    IOT_TYPE
PRODUCTS_IOT  IOT
```

---

## 📚 **MODULE 3: EXTERNAL TABLES — THE FILE READER**

### **The Scenario:**
You have a **CSV file** sitting on your server:
```
/data/server_logs.csv
```

You want to **query it with SQL** without importing it into the database.

### **The Magic: External Tables**
```sql
-- Step 1: Create a directory object pointing to the file location
CREATE OR REPLACE DIRECTORY data_dir AS '/data';

-- Step 2: Create the external table
CREATE TABLE Server_Logs_Ext (
    Log_Line VARCHAR2(4000)
) ORGANIZATION EXTERNAL (
    TYPE ORACLE_LOADER
    DEFAULT DIRECTORY data_dir
    LOCATION ('server_logs.csv')
);
```

### **Now Query It Like a Normal Table:**
```sql
SELECT * FROM Server_Logs_Ext WHERE Log_Line LIKE '%ERROR%';
```

### **Key Points:**
- ✅ The file **must be on the database server** (not your local machine).
- ✅ You can't `INSERT` into external tables (read-only).
- ✅ Perfect for **ETL** (Extract, Transform, Load) workflows.

### **When to Use:**
- Analyzing log files.
- Reading CSV exports from other systems.
- One-time data migrations.

---

## 📚 **MODULE 4: TEMPORARY TABLES — THE SESSION VAULT**

### **The Problem:**
You're building a **shopping cart**. Each user's cart should be **private** and **disappear** when they log out.

### **The Solution: Global Temporary Tables (GTT)**
```sql
CREATE GLOBAL TEMPORARY TABLE Shopping_Cart (
    User_ID   NUMBER,
    Item_Name VARCHAR2(100),
    Quantity  NUMBER
) ON COMMIT DELETE ROWS;  -- Rows vanish after COMMIT
```

**Alternative:**
```sql
ON COMMIT PRESERVE ROWS;  -- Rows stay until session ends
```

### **The Behavior:**
- ✅ The **table definition** is permanent (all users can see it).
- ✅ The **rows** are session-private (only you can see your rows).
- ✅ Rows auto-delete after `COMMIT` or session end.

### **Private Temporary Tables (Oracle 18c+):**
```sql
CREATE PRIVATE TEMPORARY TABLE ora$ptt_Calculations (
    Result NUMBER
);
```
- ✅ Even the **table definition** is private (other sessions can't see it).
- ✅ Must start with `ora$ptt_`.

### **When to Use:**
- Staging complex calculations.
- Session-specific working data.
- Shopping carts, wizards, multi-step forms.

---

## 📚 **MODULE 5: PARTITIONED TABLES — THE SEGMENTED VAULT**

### **The Problem:**
You have **10 years of sales data** (100 million rows). Queries are **painfully slow**.

### **The Solution: Partitioning**
Split the table into **monthly segments**. When you query for "January 2025", Oracle only scans **that partition** (not all 100 million rows).

### **The Syntax (Range Partitioning):**
```sql
CREATE TABLE Sales_History (
    Sale_Date DATE,
    Amount    NUMBER
) PARTITION BY RANGE (Sale_Date) (
    PARTITION p_2024_jan VALUES LESS THAN (TO_DATE('2024-02-01', 'YYYY-MM-DD')),
    PARTITION p_2024_feb VALUES LESS THAN (TO_DATE('2024-03-01', 'YYYY-MM-DD')),
    PARTITION p_2024_mar VALUES LESS THAN (TO_DATE('2024-04-01', 'YYYY-MM-DD'))
);
```

### **Other Partition Types:**

#### **List Partitioning** (by specific values):
```sql
CREATE TABLE Toys_List (
    Toy_Name VARCHAR2(100)
) PARTITION BY LIST (Toy_Name) (
    PARTITION p0 VALUES ('Sir Stripypants'),
    PARTITION p1 VALUES ('Miss Snuggles')
);
```

#### **Hash Partitioning** (automatic distribution):
```sql
CREATE TABLE Toys_Hash (
    Toy_ID INTEGER
) PARTITION BY HASH (Toy_ID) PARTITIONS 8;
```

### **The Power:**
- ✅ **Partition Pruning:** Queries only scan relevant partitions (100x faster).
- ✅ **Easy Archival:** Drop old partitions instead of deleting millions of rows.
- ⚠️ **License Required:** Partitioning is a separately licensed Oracle feature.

### **When to Use:**
- Tables with **millions/billions** of rows.
- Time-series data (sales, logs, sensor data).
- When you query by date ranges frequently.

---

## 📚 **MODULE 6: TABLE CLUSTERS — THE SHARED VAULT**

### **The Scenario:**
You frequently join `Toys` and `Toy_Owners` by `Toy_Name`. 

### **The Optimization:**
Store rows from **both tables** in the **same physical location** if they share the same `Toy_Name`.

### **The Syntax:**
```sql
-- Step 1: Create the cluster
CREATE CLUSTER Toy_Cluster (
    Toy_Name VARCHAR2(100)
);

-- Step 2: Add tables to the cluster
CREATE TABLE Toys_Clustered (
    Toy_Name VARCHAR2(100),
    Weight   NUMBER
) CLUSTER Toy_Cluster (Toy_Name);

CREATE TABLE Toy_Owners_Clustered (
    Owner    VARCHAR2(100),
    Toy_Name VARCHAR2(100)
) CLUSTER Toy_Cluster (Toy_Name);
```

### **The Benefit:**
- ✅ Rows with the same `Toy_Name` are stored **together** on disk.
- ✅ Joins are **faster** (less disk I/O).

### **When to Use:**
- Advanced optimization (rare).
- Tables that are **always joined** together.

---

## 📚 **MODULE 7: DROPPING TABLES — THE DESTROYER**

### **The Syntax:**
```sql
DROP TABLE Assassin_Guild;
```

### **⚠️ WARNING:**
- This is **permanent**. No undo.
- All data is **lost**.
- Use with extreme caution in production.

---

## 🎯 **PRACTICE LAB: BUILD THE VAULT**

### **Challenge 1: Create an IOT**
```sql
CREATE TABLE Agents_IOT (
    Agent_ID   INTEGER PRIMARY KEY,
    Agent_Name VARCHAR2(100)
) ORGANIZATION INDEX;
```

### **Challenge 2: Create a Hash-Partitioned Table**
```sql
CREATE TABLE Mission_Logs (
    Mission_ID INTEGER,
    Log_Entry  VARCHAR2(1000)
) PARTITION BY HASH (Mission_ID) PARTITIONS 4;
```

### **Challenge 3: Create a Global Temporary Table**
```sql
CREATE GLOBAL TEMPORARY TABLE Session_Data (
    Data_Key   VARCHAR2(50),
    Data_Value VARCHAR2(500)
) ON COMMIT PRESERVE ROWS;
```

---

## 📊 **VERIFICATION QUERIES**

### **Check Table Type:**
```sql
SELECT table_name, iot_type, external, partitioned, temporary, cluster_name
FROM user_tables
WHERE table_name IN ('AGENTS_IOT', 'MISSION_LOGS', 'SESSION_DATA');
```

### **View Partition Details:**
```sql
SELECT table_name, partition_name
FROM user_tab_partitions
WHERE table_name = 'MISSION_LOGS';
```

---

## 🏆 **MASTERY CHECKPOINT**

You have mastered Phase 2 when you can:
- ✅ Explain the difference between Heap, IOT, and External tables.
- ✅ Create a partitioned table and explain partition pruning.
- ✅ Use temporary tables for session-specific data.
- ✅ Query `user_tables` to inspect table properties.

---

**Next Phase:** Phase 3 — **Advanced Constraints & Relationships** (Foreign Keys, Check Constraints, Triggers)

*Vahn's Cortex � Sol's SQL Mastery Engine v2.0*`n*Sources: Oracle FreeSQL Tutorial + Oracle Dev Gym Course*
