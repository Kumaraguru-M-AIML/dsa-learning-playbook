# 📚 Sol's SQL Textbook: The Architecture of Data
*A Masterclass in Relational Intelligence*

---

## 🏛️ Chapter 1: The Mental Model
### 1.1 The Digital Filing Cabinet
Imagine you own a store. You have a physical filing cabinet.
*   **The Cabinet** = The Database.
*   **The Drawers** = The Tables (e.g., "Customers", "Products", "Orders").
*   **The Folders** = The Rows (Each individual customer).
*   **The Form Fields** = The Columns (Name, Age, Phone).

### 1.2 The "Strict Parent" Rule
Unlike Excel, where you can put a word in a "Total Price" box, SQL is a "Strict Parent."
*   If a column is marked as **NUMBER**, it will *refuse* to save text.
*   This is called **Data Integrity**. It’s why banks don't lose your money.

---

## 🛠️ Chapter 2: The Foundation (DDL)
### 2.1 Building the Container (`CREATE TABLE`)
To store data, you must first describe the container.

**The Syntax:**
```sql
CREATE TABLE Students (
    ID NUMBER PRIMARY KEY,
    NAME VARCHAR2(50),
    MARK NUMBER
);
```

**Vocabulary Bridge:**
*   `NUMBER`: Math-able data (Prices, Ages, Grades).
*   `VARCHAR2(50)`: A text string with up to 50 characters.
*   `PRIMARY KEY`: The unique ID (The fingerprint). No two rows can have the same PK.

---

## 🏗️ Chapter 3: Putting Data In (DML)
### 3.1 The `INSERT` Command
```sql
INSERT INTO Students (ID, NAME, MARK)
VALUES (1, 'Vahn', 95);
```
*Note: Strings must use Single Quotes (' ')!*

### 3.2 The Single Quote Rule (Core Concept)
**The Golden Law:**
- **Text (VARCHAR2):** MUST be wrapped in `'single quotes'`.
- **Dates (DATE):** MUST be wrapped in `'single quotes'`.
- **Numbers (NUMBER):** NO quotes. They are raw.

**Why?**
Without quotes, SQL interprets text as a **column name** and dates as **arithmetic**.

| Value | Without Quotes | With Quotes |
| :--- | :--- | :--- |
| `Vahn` | ❌ Error: Column "Vahn" not found | ✅ Text value |
| `2026-02-08` | ❌ Math: 2026 - 2 - 8 = 2016 | ✅ Date value |
| `999` | ✅ Number value | ⚠️ Treated as text |

---
*This textbook will evolve as we conquer new chapters.*
