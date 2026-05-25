[## Course: **Databases for Developers** – Oracle Dev Gym](https://devgym.oracle.com/pls/apex/f?p=10001:329:130305281103475:::329:P329_CLASS_ID,AI_LAST_PAGE:5482,29&cs=1VUm0eRHMmgk6eNK7t2mZJufGCLtXjnDrg6W00LIkYpXepVDI4g1KFCmOZxMYPanFHzTUWWgH1GunWPDYhgA7_Q)
[playlist ](https://www.youtube.com/watch?v=79iFaaHRBCo&list=PL78V83xV2fYnhHiT9R7HFGGWoL1oo6zJb&index=2)

Platform: Oracle Dev Gym  
Focus: Practical Oracle Database design and SQL fundamentals.

---

# 1️⃣ Oracle Table Types — Structural Choices

## 1. Heap-Organized Tables (Default)

![Image](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/media/iam-heap.gif?view=sql-server-ver17)

![Image](https://media.licdn.com/dms/image/v2/D4D12AQGN4CJumV8c6w/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1676872850946?e=2147483647&t=ZRbEu5bKlvGgERk43ZI7XDY_uaRG0rrkQSapfGG-hSM&v=beta)

![Image](https://miro.medium.com/0%2A5yLa0MSjBOcvizm5.png)

![Image](https://kodekloud.com/kk-media/image/upload/v1752873043/notes-assets/images/DP-900-Microsoft-Azure-Data-Fundamentals-Table-Storage/data-storage-partition-row-key-diagram.jpg)

**Mechanism**

- Rows stored wherever free space exists.
    
- No inherent order.
    

**Strengths**

- Fast inserts.
    
- Simple structure.
    
- Suitable for general workloads.
    

**Weakness**

- Retrieval by key requires index lookup.
    

**Use When**

- High insert volume.
    
- No strict physical ordering needed.
    

---

## 2. Index-Organized Tables (IOT)

![Image](https://docs.oracle.com/cd/A91202_01/901_doc/appdev.901/a88876/adg81081.gif)

![Image](https://builtin.com/sites/www.builtin.com/files/styles/ckeditor_optimize/public/inline-images/1_b-tree-indexing.jpg)

![Image](https://cdn.sanity.io/images/oaglaatp/production/6366923af7606472b084668ba805df3b1300a990-6511x2392.jpg)

![Image](https://studyglance.in/dbms/images/Clustered-Index.jpg)

**Mechanism**

- Data stored inside a B-tree structure.
    
- Rows physically ordered by primary key.
    

**Strengths**

- Faster primary key lookups.
    
- Reduced storage redundancy.
    

**Weakness**

- Slower inserts (must maintain order).
    
- Less flexible for non-PK access.
    

**Use When**

- Primary-key-driven access dominates.
    
- Read-heavy systems.
    

---

## 3. External Tables

![Image](https://oracle-base.com/articles/misc/images/partitioning/xmltag-external-tables.png)

![Image](https://objectstorage.us-phoenix-1.oraclecloud.com/p/BqK85Rn1zA5MP0vYiqbAdPgs7Z6OmMxw8SD3WCFVm5kY8uReidZ1KPIKkgJ1hCkG/n/axciphqpnohg/b/forums-legacy/o/uploads/KB962557ELEL/image.png)

![Image](https://dangvinhcuong.files.wordpress.com/2019/06/2019-06-04_161121.png)

![Image](https://www.zuar.com/blog/content/images/2022/11/Data-Staging.png)

**Mechanism**

- Access data stored outside database (e.g., CSV files).
    
- Read-only.
    

**Use Case**

- ETL staging.
    
- Data ingestion pipelines.
    
- Log file querying.
    

---

## 4. Temporary Tables

![Image](https://docs.oracle.com/en/industries/health-sciences/argus-insight/8.4/aiexg/img/image058.png)

![Image](https://www.educative.io/v2api/editorpage/5043968730202112/image/6411380434796544)

![Image](https://media.licdn.com/dms/image/sync/v2/D4E27AQEGUoCNLB5ECg/articleshare-shrink_800/B4EZuXgqlbIUAI-/0/1767773481902?e=2147483647&t=O_VI9fbO1eTzV2Hl2MuSOg9sOBfV7InQ_nyArR48HEQ&v=beta)

![Image](https://media.licdn.com/dms/image/v2/D5612AQHHwMiMqYLqEQ/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1726934937277?e=2147483647&t=iN23GW6_gHKGxaow5-qhvxBdTvZ79m1VvDTFdNA-z4U&v=beta)

**Mechanism**

- Data private per session.
    
- Automatically cleared.
    

**Use Case**

- Intermediate calculations.
    
- Batch processing.
    
- Complex report building.
    

---

## 5. Partitioned Tables

![Image](https://miro.medium.com/0%2A_meq1rhtWrEewocP.png)

![Image](https://miro.medium.com/v2/resize%3Afit%3A1200/0%2ALZxR0NpCwoA9dm4W.gif)

![Image](https://substackcdn.com/image/fetch/%24s_%210d7d%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6a6cc6c8-d39c-49d3-ab1a-b4520f23901a_1200x628.png)

![Image](https://www.researchgate.net/publication/327383033/figure/fig1/AS%3A962181659127822%401606413392172/Hash-based-partitioning-method.png)

**Mechanism**

- Splits large table into smaller physical segments.
    
- Based on partition key (range, hash, list).
    

**Strengths**

- Faster queries on large datasets.
    
- Easier maintenance.
    
- Better scalability.
    

**Use When**

- Millions/billions of rows.
    
- Time-based data (e.g., logs).
    

---

## 6. Table Clusters

![Image](https://docs.oracle.com/en/database/oracle/oracle-database/21/cncpt/img/cncpt284.gif)

![Image](https://docs.oracle.com/html/E25494_01/img/admin021.gif)

![Image](https://media.licdn.com/dms/image/v2/D5612AQHdX7h2MdFKxQ/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1694154143284?e=2147483647&t=iR06P5RsRec6HKDIdyNcpxsYhShP3V3gQJtZqSIqk-g&v=beta)

![Image](https://www.mysql.com/why-mysql/white-papers/mysql-cluster-7.2-ga/MySQL_Cluster_Clustering.png)

**Mechanism**

- Physically stores related tables together.
    

**Benefit**

- Faster joins.
    
- Reduced disk I/O.
    

---

# 2️⃣ Columns — Structural Precision

Every table must have columns.

Each column = one attribute of the entity.

---

# 3️⃣ Data Types — Critical Design Decision

## Numeric Types

- Store numbers.
    
- Use for price, quantity, weight.
    
- Must choose precision carefully.
    

**Failure Mode**

- Overflow.
    
- Rounding errors.
    
- Performance degradation.
    

---

## Date vs Timestamp

|Type|Precision|Time Zone Support|
|---|---|---|
|DATE|Seconds|❌|
|TIMESTAMP|Nanoseconds|❌|
|TIMESTAMP WITH TIME ZONE|Nanoseconds|✅|

**Rule**  
Never store dates as strings or numbers.

---

## String Types

|Type|Usage|
|---|---|
|VARCHAR2|General text|
|CLOB|Large text blocks|
|BLOB|Binary data|

**Common Error**  
Using VARCHAR2 for massive text → performance cost.

---

# 4️⃣ Structural Design Logic

Before creating a table:

1. What entity am I modeling?
    
2. What are its attributes?
    
3. What is the access pattern?
    
4. Expected scale?
    
5. Insert vs read ratio?
    
6. Time-based queries required?
    

---

# 5️⃣ Strategic Insight (For You)

Given your objective of mastering systems:

Database design =  
**Information architecture + performance forecasting + future constraint modeling.**

Poor table decisions compound negatively over years.

Strong schema design:

- Reduces technical debt.
    
- Enables scale.
    
- Minimizes refactor cost.
    

---

# 6️⃣ Compression Summary (Mental Model)

Table Type = Physical Storage Strategy  
Column Type = Data Representation Strategy  
Partitioning = Scalability Strategy  
Clustering = Join Optimization Strategy

---

If required, I can now:

- Convert this into a structured 3-level mastery roadmap.
    
- Provide SQL examples for each table type.
    
- Create schema design drills.
    
- Or deconstruct how Oracle internally manages blocks and segments.
    

Choose direction.

----
Good. Now we move from **structure** to **thinking**.

You’re confused because two big ideas are mixed:

1. **How to design tables (modeling)**
    
2. **How to retrieve data (SELECT)**
    

We separate them.

---

# EPISODE 3 — How Do You Decide What Goes in Which Table?

This is called **data modeling**.

There are two main philosophies:

---

# 1️⃣ Relational Modeling (Separate Ingredients)

![Image](https://miro.medium.com/v2/resize%3Afit%3A1400/1%2Akv-24zUQuUmC4vxIMlzILw.jpeg)

![Image](https://dotnettrickscloud.blob.core.windows.net/img/sqlserver/1nf.png)

![Image](https://creately.com/static/assets/guides/foreign-key-in-er-diagram/simple-customer-and-orders-er-diagram-e0ARXrf434i.svg)

![Image](https://creately.com/static/assets/guides/foreign-key-in-er-diagram/foreign-key-in-er-diagram-hero.webp)

### Rule:

Store each fact once.

Example: Film database

Instead of this (bad):

|film|actor_name|
|---|---|
|Batman|Christian Bale|
|Prestige|Christian Bale|

You do this (correct):

### Film Table

|film_id|title|
|---|---|

### Actor Table

|actor_id|name|
|---|---|

### Film_Actor Table

| film_id | actor_id |

Now:

- Actor name stored once.
    
- No duplication.
    
- No inconsistency.
    

This is called **normalization**.

---

# 2️⃣ Document Modeling (Pancake Kit)

![Image](https://www.researchgate.net/publication/332945890/figure/fig6/AS%3A763123027955714%401558954116631/JSON-documents-in-the-database-example.png)

![Image](https://rubygarage.s3.amazonaws.com/uploads/article_image/file/1428/storing_derivable_data_1x.png)

![Image](https://cdn.thenewstack.io/media/2023/06/8b510bed-image1.png)

![Image](https://cdn.thenewstack.io/media/2023/06/4614a080-image2.png)

Instead of separating ingredients:

You store everything in one row:

```
{
  film: "Batman",
  actors: ["Christian Bale", "Michael Caine"],
  genre: "Action"
}
```

### Advantage

- Easy to read everything at once.
    
- Fewer joins.
    

### Problem

- Duplication.
    
- Hard to update consistently.
    
- Explosion of variants.
    

---

# Core Tradeoff

|Relational|Document|
|---|---|
|Clean|Convenient|
|Consistent|Flexible|
|No duplication|Easy retrieval|
|Harder joins|Easier single fetch|

Oracle Database is primarily **relational**.

---

# Teddy vs Bricks Question

You decide based on:

### Are they structurally the same?

If both toys only need:

- name
    
- type
    

Then:

```
toys table
```

If bricks need:

- color
    
- dimension
    

And teddy needs:

- stuffing_amount
    
- fabric_type
    

Then separate:

```
bricks table
teddies table
```

---

# The Rule You Must Burn Into Memory

> A table represents ONE type of thing.

Each row = ONE instance of that thing.

If structure differs → separate tables.

---

# EPISODE 4 — SELECT (Getting Data Out)

Now retrieval.

---

# Basic Select

```sql
SELECT * FROM toys;
```

Means:  
Return all rows and all columns.

---

# Select Specific Columns

```sql
SELECT toy_name, color FROM toys;
```

Better:

- Faster
    
- Cleaner
    
- Less data transfer
    

---

# Filtering Rows (WHERE)

```sql
SELECT * FROM toys
WHERE color = 'Red';
```

Only red toys.

---

# Multiple Conditions

```sql
WHERE color = 'Red'
AND weight > 2;
```

AND = both must be true  
OR = either can be true

---

# IN (Cleaner OR)

Instead of:

```sql
color = 'Red' OR color = 'Blue'
```

Use:

```sql
color IN ('Red', 'Blue')
```

---

# Range Queries

```sql
WHERE weight BETWEEN 1 AND 5;
```

Includes 1 and 5.

Or:

```sql
WHERE weight > 2;
```

---

# LIKE (Pattern Matching)

![Image](https://www.w3resource.com/w3r_images/sql-like-operator.gif)

![Image](https://www.w3resource.com/w3r_images/sql-exercise-special-operator-result-11.gif)

![Image](https://cdn.sanity.io/images/oaglaatp/production/41e0bebd0140943dc1a62d9557e7ec3cd924781c-4423x2060.png)

![Image](https://cdn.sanity.io/images/oaglaatp/production/b4642210631c4ea70b8007f859e94f9efa81d269-4147x3600.png)

Wildcards:

|Symbol|Meaning|
|---|---|
|%|any number of characters|
|_|exactly one character|

Example:

```sql
WHERE toy_name LIKE 'B%';
```

Starts with B.

```sql
WHERE toy_name LIKE '_ear';
```

Matches:  
Bear  
Pear  
Tear

---

# NULL (Very Important)

Null = unknown.

This is NOT equal to anything.

Wrong:

```sql
WHERE weight = NULL;
```

Correct:

```sql
WHERE weight IS NULL;
```

Opposite:

```sql
WHERE weight IS NOT NULL;
```

---

# Mental Model Upgrade

SELECT has 3 decisions:

1. Which columns?
    
2. From which table?
    
3. Which rows?
    

Form:

```sql
SELECT columns
FROM table
WHERE condition;
```

That’s the core engine.

---

# Your Weakness Right Now

You are trying to understand:

- modeling
    
- normalization
    
- query filtering
    
- wildcards
    
- null logic
    

All at once.

We slow it down.

---

# Drill (Answer Directly)

Design a simple system:

We are building a **Library Database**.

Should we:

A) Store books and authors in one table?  
B) Separate them?

Explain why.

Answer in 3–5 lines.

----

Good. Now we enter the **core power** of SQL:

- Episode 5 → **JOINS**
    
- Episode 6 → **AGGREGATION**
    

These two separate beginners from real database users.

---

# EPISODE 5 — JOINS (Connecting Tables)

A relational database is powerful because **data is split across tables**.

Join = combine related rows from different tables.

---

# Step 1 — The Danger: Cross Join (Cartesian Product)

If you do this:

```sql
SELECT *
FROM teddies, bricks;
```

You get:

Every teddy × every brick.

If:

- 3 teddies
    
- 4 bricks
    

Result = 12 rows.

Almost never correct.

---

# Proper Join (Match by Column)

Example tables:

### Teddies

|id|color|
|---|---|
|1|Red|
|2|Green|

### Bricks

|id|color|
|---|---|
|10|Green|
|11|Green|
|12|Red|

We want matching colors.

---

# ANSI Inner Join (Recommended Style)

```sql
SELECT *
FROM teddies t
JOIN bricks b
  ON t.color = b.color;
```

This returns only matching colors.

---

# INNER JOIN

![Image](https://images.openai.com/static-rsc-3/Wy0ZAelFVfxChDFYPLk4ndM3E80ynaw49ujvR11fmRgv00I8q3TxWwO5l8ZMEzH_G_naFJAGtYrt0x4EwlV0h7lxcgeEjAV_CHQGnC_ZhHk?purpose=fullsize&v=1)

![Image](https://images.openai.com/static-rsc-3/QteZbv8Lg-IqbOjFNI5rYNfO29mcIwyX66RtQBJpBM9ie-PTuqCWi-Cu_Q6KYv2cjMAAt5ISDTbvEC_RiCorIVl0s0AHbnMdcEoM-sqbkIU?purpose=fullsize&v=1)

![Image](https://miro.medium.com/1%2Ao4PpF9GtvfyJoIUsYYZFFg.gif)

![Image](https://images.ctfassets.net/xwxknivhjv1b/2iUBO7kXh87vuQbImvP4QK/0f0e4a9ff75c95184f5bc215f33b874b/table_1.png?fl=png8&fm=png&h=750&q=80&w=1000)

Returns rows where match exists in both tables.

If no match → row disappears.

---

# OUTER JOINS

Sometimes you want unmatched rows too.

---

## LEFT JOIN

```sql
SELECT *
FROM teddies t
LEFT JOIN bricks b
  ON t.color = b.color;
```

Returns:

- All teddies
    
- Matching bricks if exist
    
- If no match → brick columns = NULL
    

---

## RIGHT JOIN

Opposite:  
Keeps all rows from right table.

---

## FULL OUTER JOIN

```sql
SELECT *
FROM teddies t
FULL OUTER JOIN bricks b
  ON t.color = b.color;
```

Keeps:

- All teddies
    
- All bricks
    
- Matches where possible
    

---

# Critical Outer Join Trap

If you do:

```sql
LEFT JOIN bricks b ON t.color = b.color
WHERE b.shape = 'cube';
```

You just turned it into an INNER JOIN.

Because:

- WHERE removes NULL rows.
    

Correct way:

```sql
LEFT JOIN bricks b
  ON t.color = b.color
 AND b.shape = 'cube';
```

Filtering outer table must go inside JOIN clause.

Memorize this.

---

# JOIN Summary Table

|Join Type|Keeps Unmatched Rows From|
|---|---|
|INNER|none|
|LEFT|left table|
|RIGHT|right table|
|FULL|both|

---

# EPISODE 6 — AGGREGATION (Summarizing Data)

Now we move from rows → statistics.

---

# Aggregate Functions

|Function|Meaning|
|---|---|
|COUNT|number of rows|
|SUM|total|
|MIN|smallest|
|MAX|largest|
|AVG|average|

---

# COUNT Variations

```sql
COUNT(*)        -- all rows
COUNT(color)    -- non-null values only
COUNT(DISTINCT color) -- unique values only
```

If column has NULL → COUNT(column) ignores them.

---

# GROUP BY (Split Data Into Buckets)

Example:

Bricks table:

|color|weight|
|---|---|
|Red|2|
|Red|3|
|Blue|4|

Count per color:

```sql
SELECT color, COUNT(*)
FROM bricks
GROUP BY color;
```

Result:

|color|count|
|---|---|
|Red|2|
|Blue|1|

---

# GROUP BY Rule (Very Important)

If column appears in SELECT and is not aggregated →  
It must appear in GROUP BY.

Valid:

```sql
SELECT color, COUNT(*)
FROM bricks
GROUP BY color;
```

Invalid:

```sql
SELECT color, weight, COUNT(*)
FROM bricks
GROUP BY color;
```

Because weight not grouped or aggregated.

---

# HAVING (Filter After Grouping)

Wrong:

```sql
WHERE COUNT(*) > 10
```

Doesn't work.

Correct:

```sql
SELECT color, COUNT(*)
FROM bricks
GROUP BY color
HAVING COUNT(*) >= 10;
```

Order of execution:

1. FROM
    
2. WHERE
    
3. GROUP BY
    
4. HAVING
    
5. SELECT
    

WHERE filters rows.  
HAVING filters groups.

---

# ROLLUP

Adds subtotal and grand total.

```sql
GROUP BY ROLLUP(color)
```

You get:

- Count per color
    
- Total count
    

---

# Mental Model Upgrade

SELECT has two modes:

### Row Mode

Return rows as they exist.

### Summary Mode

Collapse rows into statistics.

GROUP BY switches mode.

---

# Now I Test You

Given table:

|order_id|customer|amount|
|---|---|---|
|1|A|100|
|2|A|50|
|3|B|200|

Question 1:  
Write query to get total amount per customer.

Question 2:  
Write query to return only customers whose total > 120.

Answer in SQL.  
No explanation.

Now we enter **data modification + transactions**.  
This is where databases become serious systems.

We split this cleanly:

- Episode 7 → **INSERT + COMMIT + ROLLBACK**
    
- Episode 8 → **UPDATE + Transactions + Concurrency**
    

---

# EPISODE 7 — INSERT (Adding Data)

## 1️⃣ Single Row Insert

Basic form:

```sql
INSERT INTO toys
VALUES (1, 'Teddy', 'Blue');
```

⚠️ Problem:  
You must provide values:

- For every column
    
- In exact column order
    

If order wrong → silent corruption or error.

---

## Safer Version (Recommended)

```sql
INSERT INTO toys (toy_id, toy_name, color)
VALUES (1, 'Teddy', 'Blue');
```

Always specify columns.  
Prevents structural mistakes.

---

## 2️⃣ Multi-Row Insert (Insert from Query)

Used to copy data:

```sql
INSERT INTO toys_archive
SELECT *
FROM toys;
```

This inserts many rows at once.

Much faster than inserting row-by-row.

---

## 3️⃣ Insert Into Multiple Tables

### Unconditional

```sql
INSERT ALL
  INTO red_toys VALUES (...)
  INTO toy_backup VALUES (...)
SELECT *
FROM toys;
```

Every row goes into every listed table.

---

### Conditional

```sql
INSERT ALL
  WHEN color = 'Red' THEN
    INTO red_toys VALUES (...)
  WHEN color = 'Blue' THEN
    INTO blue_toys VALUES (...)
SELECT *
FROM toys;
```

Row goes into tables where condition is true.

---

### INSERT FIRST

Stops after first match.

```sql
INSERT FIRST
  WHEN color = 'Red' THEN
    INTO red_toys VALUES (...)
  WHEN color = 'Blue' THEN
    INTO blue_toys VALUES (...)
SELECT *
FROM toys;
```

Row inserted only once.

---

# COMMIT & ROLLBACK

This is critical.

## What Happens After INSERT?

Until you run:

```sql
COMMIT;
```

Only you see the changes.

Other users cannot.

---

## If You Make a Mistake

```sql
ROLLBACK;
```

Undo everything since last commit.

---

# Transaction

A **transaction** = smallest unit of work that must fully succeed or fully fail.

Example:

Transfer ₹100.

```sql
UPDATE wallet SET balance = balance - 100 WHERE user = 'A';
UPDATE wallet SET balance = balance + 100 WHERE user = 'B';
COMMIT;
```

If disaster happens before commit → rollback ensures no inconsistency.

Never commit halfway.

---

# EPISODE 8 — UPDATE (Changing Data)

## Basic Update

```sql
UPDATE toys
SET color = 'Blue'
WHERE color = 'Pink';
```

Without WHERE:

```sql
UPDATE toys SET color = 'Blue';
```

This updates EVERY row.

Catastrophic in production.

---

# Concurrency (Multi-User Reality)

Databases are shared systems.

When you update rows:

- Oracle locks them.
    
- Others must wait.
    
- Lock released after COMMIT or ROLLBACK.
    

---

# Problem 1 — Deadlock

## What Is It?

User A locks row 1  
User B locks row 2

Then:

User A tries row 2  
User B tries row 1

Both wait forever.

Oracle detects and kills one transaction.

---

## Prevent Deadlocks

1. Update tables in same order everywhere.
    
2. Keep transactions short.
    
3. Use:
    

```sql
SELECT * 
FROM toys
WHERE toy_id = 1
FOR UPDATE;
```

This locks rows early.

---

# Problem 2 — Lost Update

Two users read same row.

User A updates and commits.

User B updates using old copy → overwrites A.

Silent data loss.

---

# Solution: Optimistic Locking

Add column:

```sql
version_number NUMBER
```

Update like:

```sql
UPDATE toys
SET color = 'Blue',
    version_number = version_number + 1
WHERE toy_id = 1
AND version_number = 3;
```

If no row updated → someone changed it.

Application must detect this.

---

# Mental Model Upgrade

Database modification = controlled state machine.

Rules:

1. Never update without WHERE.
    
2. Keep transactions minimal.
    
3. Commit at logical completion.
    
4. Avoid long locks.
    
5. Guard against concurrent overwrites.
    

---

# Execution Order in Modification

- UPDATE locks rows.
    
- Other users wait.
    
- COMMIT releases locks.
    
- ROLLBACK reverts changes.
    

---

# Strategic View

SELECT = read power  
JOIN = relational power  
GROUP BY = analytical power  
INSERT/UPDATE = state mutation power  
TRANSACTION = integrity control

Integrity > speed.

---

# Now Your Drill

Table:

|account_id|balance|version|
|---|---|---|
|1|500|2|

Write SQL to:

- Deduct 100
    
- Use optimistic locking
    
- Ensure no lost update
    

Only SQL.

Now we cover:

- **Episode 9 → DELETE / TRUNCATE / Soft Deletes**
    
- **Episode 10 → NULL (the dangerous third logic state)**
    

These are conceptual traps. Pay attention.

---

# EPISODE 9 — DELETE vs TRUNCATE

## 1️⃣ DELETE (Row-by-row removal)

```sql
DELETE FROM toys
WHERE color = 'Pink';
```

Removes only matching rows.

If you forget `WHERE`:

```sql
DELETE FROM toys;
```

Deletes everything.

But:

- It is transactional.
    
- You can `ROLLBACK` before commit.
    

---

## 2️⃣ TRUNCATE (Fast wipe)

```sql
TRUNCATE TABLE toys;
```

Characteristics:

|Property|DELETE|TRUNCATE|
|---|---|---|
|Can filter rows|✅|❌|
|Can rollback|✅ (before commit)|❌|
|Speed|Slower|Very fast|
|Logs row-by-row|Yes|No|

Truncate:

- Instantly marks table empty.
    
- Auto-commits.
    
- Cannot undo.
    

Use only when certain.

---

# Soft Delete (Logical Deletion)

Instead of removing row:

Add column:

```sql
is_deleted NUMBER(1)
```

Then:

```sql
UPDATE toys
SET is_deleted = 1
WHERE toy_id = 10;
```

Row still exists.

---

## Why Use Soft Delete?

- Audit trail
    
- Recover mistakes
    
- Prevent fraud
    

---

## Problem

You must add this everywhere:

```sql
WHERE is_deleted = 0
```

Easy to forget.

---

## Cleaner Solution → View

```sql
CREATE VIEW active_toys AS
SELECT *
FROM toys
WHERE is_deleted = 0;
```

Application queries the view instead of table.

---

## Advanced Oracle Features Mentioned

- **Virtual Private Database (VPD)** → auto-adds filters based on user
    
- **In-Database Archiving** → hidden column controlling visibility
    

But conceptually:  
Soft delete increases complexity.

Ask:  
Do you need deletion prevention?  
Or just auditing?

Often audit is enough.

---

# EPISODE 10 — NULL (The Third Logic State)

This is where SQL gets dangerous.

---

# What Is NULL?

NULL ≠ 0  
NULL ≠ ''  
NULL ≠ false

NULL = unknown / not applicable.

---

# Three-Valued Logic

Normal logic:

TRUE  
FALSE

With NULL:

TRUE  
FALSE  
UNKNOWN

SQL WHERE only returns rows where condition = TRUE.

FALSE or UNKNOWN → row removed.

---

# Example

|toy|stuffing|
|---|---|
|Teddy|50|
|Brick|NULL|

Query:

```sql
WHERE stuffing > 10
```

For Brick:

NULL > 10 → UNKNOWN

Row not returned.

---

# Comparison Rules

These are always UNKNOWN:

```sql
stuffing = NULL
stuffing <> NULL
stuffing > NULL
```

Correct check:

```sql
stuffing IS NULL
stuffing IS NOT NULL
```

---

# Problem with Comparisons

```sql
WHERE stuffing > brick.stuffing
```

If brick.stuffing is NULL → comparison fails.

Even if logically obvious.

---

# Solution 1 — NVL (Oracle)

```sql
NVL(stuffing, 0)
```

If stuffing is NULL → treat as 0.

Example:

```sql
WHERE NVL(stuffing, 0) > 10
```

---

# Solution 2 — COALESCE (ANSI Standard)

```sql
COALESCE(stuffing, 0)
```

Difference:

- NVL → 2 arguments
    
- COALESCE → multiple arguments
    

Example:

```sql
COALESCE(stuffing, alternative_value, 0)
```

Returns first non-null.

---

# Magic Values (Dangerous Alternative)

Instead of NULL, use:

-1  
999999  
'UNKNOWN'

Example:

Brick stuffing = -1.

Problem:  
Aggregates break.

Example:

```sql
SUM(stuffing)
```

Subtracts 1 for each brick.

Silent corruption.

---

# Rule

Magic values introduce hidden bugs.

NULL introduces logical complexity.

Choose carefully.

---

# Best Practice

1. Use `NOT NULL` constraint when value must exist.
    

```sql
stuffing NUMBER NOT NULL
```

2. Only allow NULL when:
    
    - Data truly missing
        
    - Or attribute not applicable
        
3. Always test with rows containing NULL.
    

---

# Mental Model Upgrade

NULL forces you to ask:

Is this:

- Unknown?
    
- Not applicable?
    
- Or actual zero?
    

Design error here compounds everywhere.

---

# Order of Execution Reminder

WHERE filters only TRUE rows.

NULL comparisons return UNKNOWN.

Therefore:  
Most bugs come from forgetting NULL behavior.

---

# Precision Question For You

Table:

|id|marks|
|---|---|
|1|80|
|2|NULL|
|3|50|

Question:

What does this return?

```sql
SELECT COUNT(marks) FROM table;
```

And what does this return?

```sql
SELECT COUNT(*) FROM table;
```

Answer both.

Now we enter:

- **Episode 11 → Subqueries & WITH (CTE)**
    
- **Episode 12 → ORDER BY & Top-N queries**
    

These are about **query structure and result control**.

---

# EPISODE 11 — SUBQUERIES

## Core Idea

> A SELECT returns a table.  
> So you can use a SELECT inside another SELECT.

---

# 1️⃣ Inline View (Subquery in FROM)

Instead of:

```sql
SELECT *
FROM bricks;
```

You can do:

```sql
SELECT *
FROM (
    SELECT color, COUNT(*) cnt
    FROM bricks
    GROUP BY color
);
```

That inner SELECT behaves like a temporary table.

This is called an **inline view**.

---

## Why Use It?

Break complex logic into stages.

Example pattern:

1. Aggregate
    
2. Join
    
3. Filter
    
4. Aggregate again
    

Trying in one flat query → chaos.

Using inline views → layered logic.

---

# 2️⃣ WITH Clause (Common Table Expression – CTE)

Cleaner version of inline views.

Instead of nesting:

```sql
WITH brick_counts AS (
    SELECT color, COUNT(*) cnt
    FROM bricks
    GROUP BY color
)
SELECT *
FROM brick_counts;
```

Advantages:

- Named subqueries
    
- Easier to debug
    
- Readable
    
- Modular
    

You can stack multiple:

```sql
WITH
brick_counts AS (...),
model_requirements AS (...),
valid_models AS (...)
SELECT *
FROM valid_models;
```

Professional SQL almost always uses WITH for complex queries.

---

# 3️⃣ Subqueries in WHERE

## IN

```sql
SELECT *
FROM bricks
WHERE color IN (
    SELECT color
    FROM allowed_colors
);
```

If subquery returns list → IN checks membership.

---

## EXISTS

```sql
SELECT *
FROM bricks b
WHERE EXISTS (
    SELECT 1
    FROM allowed_colors c
    WHERE c.color = b.color
);
```

Difference:

|IN|EXISTS|
|---|---|
|Compares values|Checks row existence|
|Simpler syntax|More flexible|
|Breaks with NULL in NOT IN|Safer with NULL|

---

## Critical NULL Trap

```sql
WHERE color NOT IN (SELECT color FROM table);
```

If subquery returns even ONE NULL → entire condition becomes UNKNOWN.

Returns nothing.

Safer:

```sql
WHERE NOT EXISTS (...)
```

Memorize this.

---

# 4️⃣ Correlated Subquery

Subquery references outer query table.

```sql
SELECT *
FROM bricks b
WHERE EXISTS (
    SELECT 1
    FROM models m
    WHERE m.color = b.color
);
```

Inner query depends on outer row.

Runs per-row logically (optimizer may optimize).

---

# 5️⃣ Scalar Subquery

Returns exactly:

- 1 row
    
- 1 column
    

Example:

```sql
SELECT
    color,
    (SELECT COUNT(*) FROM bricks) total_bricks
FROM bricks;
```

Behaves like a column.

Useful in SELECT, INSERT, UPDATE.

---

# 6️⃣ Subqueries in DML

Valid in:

- INSERT values
    
- UPDATE set
    
- DELETE where
    

Example:

```sql
UPDATE toys
SET color = (
    SELECT new_color
    FROM color_map
    WHERE color_map.old_color = toys.color
);
```

---

# Professional Rule

If query feels unreadable:  
Use WITH.

Indent properly.  
Alias tables.  
Qualify columns.

---

---

# EPISODE 12 — ORDER BY & Top-N

---

# 1️⃣ ORDER BY (Mandatory for Predictable Output)

Without ORDER BY:

Database returns rows in physical storage order.

This is coincidence.

Never rely on it.

---

## Basic Sort

```sql
SELECT *
FROM toys
ORDER BY weight;
```

Default: ASC (ascending)

Descending:

```sql
ORDER BY weight DESC;
```

---

# NULL Ordering

Default:

NULLS LAST (in ascending)

Override:

```sql
ORDER BY weight NULLS FIRST;
```

---

# Custom Sort

Example:

Green → first  
Red → second  
Blue → third

```sql
ORDER BY
    CASE color
        WHEN 'Green' THEN 1
        WHEN 'Red' THEN 2
        WHEN 'Blue' THEN 3
    END;
```

Better:

Alias it:

```sql
SELECT
    color,
    CASE ... END sort_order
FROM bricks
ORDER BY sort_order;
```

---

# Positional Notation (Avoid)

```sql
ORDER BY 2;
```

Sort by second column in SELECT.

Dangerous if column order changes.

Avoid in production.

---

# Top-N Queries

Goal:  
Get first N rows after sorting.

---

## Wrong Way (Classic Mistake)

```sql
SELECT *
FROM bricks
WHERE ROWNUM <= 3
ORDER BY weight DESC;
```

This:

1. Picks any 3 rows
    
2. Then sorts them
    

Wrong logic order.

---

## Correct (Pre-12c)

```sql
SELECT *
FROM (
    SELECT *
    FROM bricks
    ORDER BY weight DESC
)
WHERE ROWNUM <= 3;
```

Now:

1. Sort
    
2. Then limit
    

Correct.

---

## Better (12c+)

```sql
SELECT *
FROM bricks
ORDER BY weight DESC
FETCH FIRST 3 ROWS ONLY;
```

Cleaner.  
ANSI standard.

---

# Non-Deterministic Trap

If sorting column has duplicates:

Example:

weight:  
100  
90  
90  
80

Fetch first 2 rows → which 90?

Not deterministic.

Fix:

```sql
ORDER BY weight DESC, toy_id;
```

Make sort unique.

---

# Dense Rank vs Row Number

If you want:  
Top 3 unique weights including ties:

Use:

```sql
DENSE_RANK() OVER (ORDER BY weight DESC)
```

Instead of ROW_NUMBER.

---

# Mental Model

ORDER BY = presentation logic  
FETCH FIRST = limit after sorting

Processing order simplified:

1. FROM
    
2. WHERE
    
3. GROUP BY
    
4. HAVING
    
5. SELECT
    
6. ORDER BY
    
7. FETCH
    

---

# Precision Test

Table:

|id|score|
|---|---|
|1|100|
|2|95|
|3|95|
|4|90|

Query:

```sql
SELECT *
FROM table
ORDER BY score DESC
FETCH FIRST 2 ROWS ONLY;
```

Is result deterministic?

Explain why in 2 lines.


Now we’re in **advanced query mechanics**:

- Episode 13 → **Analytic (Window) Functions**
    
- Episode 14 → **PIVOT / UNPIVOT**
    

These are about transforming and analyzing data **without destroying row detail**.

---

# EPISODE 13 — ANALYTIC (WINDOW) FUNCTIONS

## Core Problem

`GROUP BY` collapses rows.

If you do:

```sql
SELECT color, COUNT(*)
FROM bricks
GROUP BY color;
```

You lose individual brick rows.

Sometimes you want:

- Each row
    
- Plus aggregated info
    

This is where analytic functions win.

---

# 1️⃣ Basic Analytic Count

```sql
SELECT
    color,
    COUNT(*) OVER (PARTITION BY color) AS color_count
FROM bricks;
```

Now:

- Every row stays
    
- Each row shows how many bricks share its color
    

No grouping collapse.

---

## Mental Model

`PARTITION BY` = logical grouping  
But rows are NOT removed.

Think:  
“GROUP BY without compression.”

---

# 2️⃣ Running Totals

Example:

```sql
SELECT
    weight,
    SUM(weight) OVER (ORDER BY weight) AS running_total
FROM toys;
```

This calculates cumulative sum.

---

## Default Window Behavior

By default:

```
RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
```

Meaning:  
All rows with value ≤ current value included.

If duplicate weights exist → identical running totals.

---

# 3️⃣ RANGE vs ROWS

### RANGE

Based on value.  
Duplicates grouped together.

### ROWS

Based on physical row position.

Example fix:

```sql
SUM(weight)
OVER (
    ORDER BY weight
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
)
```

Now total increases per row.

⚠ If order not unique → non-deterministic.

Fix by adding unique tie-breaker:

```sql
ORDER BY weight, toy_id
```

---

# 4️⃣ Rolling Windows

Example:  
Current row + previous row only:

```sql
SUM(weight)
OVER (
    ORDER BY weight
    ROWS BETWEEN 1 PRECEDING AND CURRENT ROW
)
```

---

Example:  
Current + 1 before + 1 after:

```sql
AVG(weight)
OVER (
    ORDER BY weight
    ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
)
```

---

Example:  
Exclude current row:

```sql
ROWS BETWEEN 3 PRECEDING AND 1 PRECEDING
```

---

# 5️⃣ Partition + Running Total

Separate running totals per color:

```sql
SUM(weight)
OVER (
    PARTITION BY color
    ORDER BY weight
)
```

Each color gets its own window.

---

# 6️⃣ Other Analytic Functions

Common:

- `ROW_NUMBER()` → unique ranking
    
- `RANK()` → gaps allowed
    
- `DENSE_RANK()` → no gaps
    
- `LAG()` → look backward
    
- `LEAD()` → look forward
    
- `FIRST_VALUE()`
    
- `LAST_VALUE()`
    

Example:

```sql
SELECT
    weight,
    LAG(weight) OVER (ORDER BY weight) AS previous_weight
FROM toys;
```

---

# Important Restriction

You **cannot** use analytic functions in WHERE.

Wrong:

```sql
WHERE ROW_NUMBER() OVER (...) <= 3
```

Correct:

```sql
SELECT *
FROM (
    SELECT t.*, ROW_NUMBER() OVER (ORDER BY weight DESC) rn
    FROM toys t
)
WHERE rn <= 3;
```

Analytic functions are evaluated after WHERE.

---

# EPISODE 14 — PIVOT / UNPIVOT

Now we transform structure.

---

# PIVOT (Rows → Columns)

Example original table:

|date|food|calories|
|---|---|---|

Goal:  
One row per week.  
Columns = Monday, Tuesday, etc.

---

## Manual Way (Messy)

Using SUM + CASE:

```sql
SUM(CASE WHEN day = 'MON' THEN calories END)
```

Repeated 7 times.

---

## Proper Pivot

```sql
SELECT *
FROM (
    SELECT
        TRUNC(date, 'IW') week_start,
        TO_CHAR(date, 'DY') day,
        calories
    FROM meals
)
PIVOT (
    SUM(calories)
    FOR day IN ('MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN')
);
```

---

## Key Rules

1. Pivot requires aggregation.
    
2. Pivot column must be real column (not function).
    
3. Columns not included become implicit GROUP BY.
    

If extra column present → extra rows appear.

---

# Dynamic Pivot Problem

You must explicitly list pivot values:

```sql
FOR food IN ('Cake', 'Fruit', 'Pizza')
```

Cannot auto-detect unless using XML pivot (complex).

If column list changes frequently → reconsider design.

---

# Filter Placement

Since pivot sits after FROM:

```sql
FROM ...
PIVOT (...)
WHERE ...
```

But better:  
Filter in subquery before pivot.

Principle:  
Filter early = faster query.

---

# UNPIVOT (Columns → Rows)

Reverse operation.

Example:

| week | MON | TUE | WED |

Convert to:

| week | day | calories |

```sql
SELECT *
FROM table
UNPIVOT (
    calories FOR day IN (MON, TUE, WED)
);
```

---

## Limitation

If pivoted data was aggregated →  
You cannot recover original detail.

Aggregation loses information permanently.

---

# Strategic Understanding

|Tool|Purpose|
|---|---|
|GROUP BY|compress rows|
|Analytic|aggregate without compression|
|PIVOT|rotate rows to columns|
|UNPIVOT|rotate columns to rows|

---

# Conceptual Hierarchy

Basic SQL → filtering rows  
Joins → combining tables  
Aggregation → summarizing  
Analytic → advanced contextual metrics  
Pivot → structural transformation

---

# Final Precision Drill

Given:

|id|color|weight|
|---|---|---|
|1|Red|10|
|2|Red|20|
|3|Blue|5|

Question:

What does this produce?

```sql
SELECT
    id,
    SUM(weight) OVER (PARTITION BY color ORDER BY weight) AS rt
FROM table;
```

Explain:

- Red rows
    
- Blue row
    

Be precise.

----

Now we cover:

- **Episode 15 → Set Operators (UNION, INTERSECT, MINUS)**
    
- **Episode 16 → Hierarchical Queries (Trees)**
    

These are structural comparison and recursive traversal tools.

---

# EPISODE 15 — SET OPERATORS

Set operators combine full result sets.

They require:

- Same number of columns
    
- Same data types
    
- Same column order
    

---

# 1️⃣ UNION

```sql
SELECT toy_id, color FROM teddies
UNION
SELECT toy_id, color FROM bricks;
```

Returns unique rows from both queries.

Important:  
`UNION` = `UNION DISTINCT`.

Duplicates removed automatically.

---

## UNION ALL (Preferred)

```sql
SELECT ...
UNION ALL
SELECT ...
```

Keeps duplicates.

Faster.  
No distinct sort step.

Rule:  
Use `UNION ALL` unless you explicitly need duplicate removal.

---

# 2️⃣ INTERSECT

```sql
SELECT ...
FROM table1
INTERSECT
SELECT ...
FROM table2;
```

Returns rows existing in both tables.

Equivalent to:  
`EXISTS` + `DISTINCT`.

Rare in production but clean for comparison logic.

---

# 3️⃣ MINUS (Oracle)

```sql
SELECT ...
FROM table1
MINUS
SELECT ...
FROM table2;
```

Returns rows in table1 not in table2.

Important:

- Removes duplicates.
    
- Treats NULLs as equal.
    
- Simpler than NOT EXISTS for full-row comparison.
    

---

# Operator Precedence Trap

All set operators have equal priority.

This:

```sql
A MINUS B
UNION
C MINUS D
```

Is evaluated left-to-right.

Use parentheses to control order:

```sql
(A MINUS B)
UNION
(C MINUS D)
```

Always bracket complex set operations.

---

# Comparing Two Tables Efficiently

Classic method:

```sql
(A MINUS B)
UNION
(B MINUS A)
```

Finds differences.

But reads both tables twice.

---

## Efficient Comparison Pattern

```sql
SELECT *
FROM (
    SELECT col1, col2, 1 AS t1, 0 AS t2 FROM table1
    UNION ALL
    SELECT col1, col2, 0 AS t1, 1 AS t2 FROM table2
)
GROUP BY col1, col2
HAVING SUM(t1) != SUM(t2);
```

This:

- Reads each table once
    
- Detects mismatches
    
- Handles duplicates correctly
    

Advanced but scalable.

---

# Summary Table

|Operator|Keeps Duplicates|Typical Use|
|---|---|---|
|UNION|No|Merge unique rows|
|UNION ALL|Yes|Merge raw data|
|INTERSECT|No|Common rows|
|MINUS|No|Differences|

---

---

# EPISODE 16 — HIERARCHIES (TREES)

When rows reference other rows in same table.

Example structure:

|id|name|parent_id|
|---|---|---|

---

# 1️⃣ CONNECT BY (Oracle proprietary)

Example:

```sql
SELECT
    LEVEL,
    name
FROM family
START WITH parent_id IS NULL
CONNECT BY PRIOR id = parent_id;
```

Key parts:

- `START WITH` → defines root
    
- `CONNECT BY` → defines relationship
    
- `PRIOR` → links parent to child
    
- `LEVEL` → depth counter
    

---

# LEVEL

Root = 1  
Children = 2  
Grandchildren = 3

Use for indentation:

```sql
LPAD(name, LEVEL * 3) AS tree_view
```

---

# ORDER SIBLINGS BY

```sql
ORDER SIBLINGS BY birth_date;
```

Sorts children under same parent.

Normal ORDER BY breaks hierarchy.

---

# 2️⃣ Recursive WITH (ANSI Standard)

More flexible.

Structure:

```sql
WITH family_tree (id, name, parent_id, lvl) AS (

    -- Base case (root)
    SELECT id, name, parent_id, 1
    FROM family
    WHERE parent_id IS NULL

    UNION ALL

    -- Recursive step
    SELECT f.id, f.name, f.parent_id, ft.lvl + 1
    FROM family f
    JOIN family_tree ft
      ON f.parent_id = ft.id
)
SELECT *
FROM family_tree;
```

Two parts:

1. Anchor query
    
2. Recursive query
    

---

# Depth-First vs Breadth-First

Recursive WITH allows:

- Depth-first search
    
- Breadth-first search
    

Depth-first:  
Go down one branch fully.

Breadth-first:  
Visit level by level.

---

# Loop Detection

If row references itself indirectly:

Infinite loop risk.

---

## CONNECT BY Fix

```sql
CONNECT BY NOCYCLE PRIOR id = parent_id
```

---

## Recursive WITH Cycle Detection

```sql
CYCLE id
SET is_cycle TO 'Y'
DEFAULT 'N'
```

Detects repeated path values.

---

# Important Reality

True trees:  
Each node has one parent.

Family trees:  
Two parents → actually a Directed Acyclic Graph (DAG).

SQL hierarchical tools assume single-parent tree.

Model carefully.

---

# Mental Models

Set operators → horizontal comparison  
Hierarchical queries → vertical traversal

Together:  
You can compare structures and explore recursive relationships.

---

# Precision Drill

Given:

|id|parent_id|
|---|---|
|1|NULL|
|2|1|
|3|2|
|4|3|

What is LEVEL for each row using CONNECT BY?

List id and level.

Be exact.

----

Now we cover:

- **Episode 17 → MERGE (Upsert)**
    
- **Episode 18 → Isolation Levels & Read Phenomena**
    

These are about correctness under change.

---

# EPISODE 17 — MERGE (UPSERT)

Problem:

You want to:

- INSERT if row doesn’t exist
    
- UPDATE if row already exists
    

Doing this manually:

Option 1:

```sql
INSERT ...
IF error THEN UPDATE ...
```

Option 2:

```sql
UPDATE ...
IF sql%rowcount = 0 THEN INSERT ...
```

Both require guessing which happens more often.

Wrong guess → wasted work.

---

## Solution: MERGE

Single atomic statement.

```sql
MERGE INTO target t
USING source s
ON (t.card_value = s.card_value
    AND t.suit = s.suit)

WHEN MATCHED THEN
  UPDATE SET t.style = s.style

WHEN NOT MATCHED THEN
  INSERT (card_value, suit, style)
  VALUES (s.card_value, s.suit, s.style);
```

---

## How It Works

- `USING` → source rows
    
- `ON` → join condition (must match at most one target row)
    
- `WHEN MATCHED` → update
    
- `WHEN NOT MATCHED` → insert
    

You don’t choose update-first or insert-first.  
Optimizer handles it.

---

## Important Rule

The `ON` condition must be unique.

If one source row matches multiple target rows → error.

Therefore:  
Merge join condition must use primary key or unique key.

---

## Update-Only Merge (Performance Use Case)

Correlated update:

```sql
UPDATE target t
SET value = (
    SELECT s.value
    FROM source s
    WHERE s.id = t.id
);
```

This may re-execute subquery per row.

Merge version scans each table once:

```sql
MERGE INTO target t
USING source s
ON (t.id = s.id)
WHEN MATCHED THEN
  UPDATE SET t.value = s.value;
```

Often faster at scale.

---

## Conditional Merge

You can add filters:

```sql
WHEN MATCHED THEN
  UPDATE SET ...
  WHERE t.card_value != 'JOKER'
```

You can also:

```sql
WHEN MATCHED THEN
  DELETE WHERE ...
```

But delete only affects matched rows.

It will NOT delete rows in target that don’t appear in source.

Important limitation.

---

## When NOT to Use MERGE

If:

- 99% guaranteed insert-only
    
- Or 99% update-only
    

Separate statements may be faster.

Always benchmark on real data.

---

# EPISODE 18 — ISOLATION LEVELS & READ PHENOMENA

This is about **what happens when users act concurrently.**

Three classic problems:

---

# 1️⃣ Dirty Read

Reading uncommitted data.

Session A:

```sql
UPDATE bricks SET color = 'Red';
-- not committed
```

Session B:  
Reads table and sees Red.

Then Session A rolls back.

Session B saw data that never existed permanently.

Oracle: **Does NOT allow dirty reads.**

---

# 2️⃣ Non-Repeatable Read (Fuzzy Read)

Session A:

```sql
SELECT COUNT(*) FROM bricks;
-- returns 3 blue
```

Session B:  
Changes a blue to red and commits.

Session A:  
Runs same query again → now 2 blue.

Same query, same transaction, different result.

---

# 3️⃣ Phantom Read

Session A:  
Counts red bricks → 4.

Session B:  
Inserts new red brick and commits.

Session A:  
Counts again → 5.

New row appeared.

---

# Why This Matters

Within one transaction you expect logical consistency.

If data changes mid-logic:  
Derived calculations become invalid.

Example:

- Compute invoice total
    
- Then compute tax
    
- If items changed in between → mismatch
    

---

# SQL Standard Isolation Levels

|Level|Dirty Reads|Fuzzy Reads|Phantom Reads|
|---|---|---|---|
|Read Uncommitted|Allowed|Allowed|Allowed|
|Read Committed|❌|Allowed|Allowed|
|Repeatable Read|❌|❌|Allowed|
|Serializable|❌|❌|❌|

---

# Oracle Reality

Oracle supports:

- READ COMMITTED (default)
    
- SERIALIZABLE
    
- READ ONLY
    

No dirty reads ever.

---

# Oracle’s Advantage — MVCC

Multiversion Concurrency Control.

In READ COMMITTED:

Each statement sees a consistent snapshot  
as of the time it started.

So:

Within one SELECT:  
No fuzzy reads.  
No phantoms.

But:

Between two SELECTs in same transaction:  
You may see changes.

---

# Serializable Mode

```sql
ALTER SESSION SET ISOLATION_LEVEL = SERIALIZABLE;
```

Now:  
All queries in transaction see same snapshot.

Prevents fuzzy & phantom across statements.

But:

If you try to modify row changed by someone else since transaction began → error.

Higher safety.  
Lower concurrency.

---

# Read Only Mode

```sql
SET TRANSACTION READ ONLY;
```

- Snapshot frozen
    
- Cannot modify data
    
- Useful for reporting
    

---

# Blocking Behavior (Oracle)

Readers do not block writers.  
Writers do not block readers.  
(Writers block writers on same rows.)

This is a major design difference from some databases.

---

# Strategic Implication

Most applications use READ COMMITTED safely.

Use SERIALIZABLE only when:

- Same table read multiple times
    
- Logical consistency across reads required
    

Higher isolation = lower throughput.

Always choose isolation level based on business logic.

---

# Mental Model

Statement-level consistency → guaranteed (Oracle)

Transaction-level consistency → optional (Serializable)

---

# Final Precision Drill

Under Oracle READ COMMITTED:

Transaction T1:

```sql
SELECT COUNT(*) FROM bricks;
-- returns 10
```

Before T1 commits, T2 inserts 2 bricks and commits.

T1 runs:

```sql
SELECT COUNT(*) FROM bricks;
```

What count can T1 see?

Explain in one sentence.

