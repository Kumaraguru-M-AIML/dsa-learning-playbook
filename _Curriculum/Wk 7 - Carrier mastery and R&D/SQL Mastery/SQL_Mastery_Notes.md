# Oracle SQL Mastery Notes
*Reference guide generated during your Anti-Gravity learning sessions.*

---

## Lesson 1: Genesis (Creating Data)
Before you can query data, you must build the structure.

### 1. Creating a Table ("The Excel Sheet")
We use `CREATE TABLE` to define the columns and their data types.

**Scenario:** We want to build this empty sheet:

| StudentID | Name    | GradeLevel | FavoriteSubject |
| :-------- | :------ | :--------- | :-------------- |
| (Empty)   | (Empty) | (Empty)    | (Empty)         |

**Code:**
```sql
CREATE TABLE Students (
    StudentID INTEGER PRIMARY KEY,
    Name TEXT,
    GradeLevel INTEGER,
    FavoriteSubject TEXT
);
```

### 2. Inserting Data ("The Rows")
We use `INSERT INTO` to add data.

**Code:**
```sql
INSERT INTO Students VALUES (101, 'Rahul', 10, 'Math');
INSERT INTO Students VALUES (102, 'Priya', 11, 'Biology');
INSERT INTO Students VALUES (103, 'Amit', 10, 'History');
INSERT INTO Students VALUES (104, 'Zack', 12, NULL); -- New: Student with no favorite subject
```

**Resulting Table in Database:**

| StudentID | Name  | GradeLevel | FavoriteSubject |
| :-------- | :---- | :--------- | :-------------- |
| 101       | Rahul | 10         | Math            |
| 102       | Priya | 11         | Biology         |
| 103       | Amit  | 10         | History         |
| 104       | Zack  | 12         | **NULL**        |

---

## Lesson 2: The Art of Asking (SELECT)
Retrieving data from the database.

### 1. The "Lazy" Select (Everything)
The asterisk `*` means "Show me all columns".

**Query:**
```sql
SELECT * FROM Students;
```

**Result:**
*(Shows all 4 rows)*

### 2. The Specific Select
Only ask for what you need.

**Query:**
```sql
SELECT Name, FavoriteSubject FROM Students;
```

**Result:**

| Name  | FavoriteSubject |
| :---- | :-------------- |
| Rahul | Math            |
| Priya | Biology         |
| Amit  | History         |
| Zack  | **NULL**        |

---

## Lesson 3: The Filter (WHERE)
Filtering rows to find specific data.

### Syntax
`SELECT * FROM Table WHERE Column = Value`

**Query (Find Priya):**
```sql
SELECT * FROM Students WHERE Name = 'Priya';
```

**Result:**

| StudentID | Name  | GradeLevel | FavoriteSubject |
| :-------- | :---- | :--------- | :-------------- |
| 102       | Priya | 11         | Biology         |

**Query (Find NOT Grade 11):**
```sql
SELECT * FROM Students WHERE GradeLevel <> 11;
```

**Result:**

| StudentID | Name  | GradeLevel | FavoriteSubject |
| :-------- | :---- | :--------- | :-------------- |
| 101       | Rahul | 10         | Math            |
| 103       | Amit  | 10         | History         |
| 104       | Zack  | 12         | NULL            |

---

## Lesson 4: Dealing with NULL (The Void)
**The Golden Rule:** Never use `=` for NULL. Always use `IS` or `IS NOT`.

### 1. Finding the Nulls
**Query:**
```sql
SELECT * FROM Students WHERE FavoriteSubject IS NULL;
```

**Result:**

| StudentID | Name | GradeLevel | FavoriteSubject |
| :-------- | :--- | :--------- | :-------------- |
| 104       | Zack | 12         | **NULL**        |

### 2. Finding the Non-Nulls
**Query:**
```sql
SELECT * FROM Students WHERE FavoriteSubject IS NOT NULL;
```

**Result:**
*(Shows Rahul, Priya, and Amit. Zack is hidden.)*

### 3. Math with NULLs (NVL/IFNULL)
*From our earlier experiment.*

**The Solution Query:**
```sql
-- SQLite Syntax (Oracle uses NVL)
SELECT Name, Salary + IFNULL(Commission, 0) as TotalPay FROM Employees;
```

---

## Lesson 5: Concatenation (Joining Text)
Putting two strings together using `||`.

**Query:**
```sql
SELECT FirstName || ' ' || LastName as FullName FROM Employees;
```

**Result:**

| FullName    |
| :---------- |
| John Smith  |
| Jane Doe    |
| Bob Builder |

---
*Last Updated: Just now*
