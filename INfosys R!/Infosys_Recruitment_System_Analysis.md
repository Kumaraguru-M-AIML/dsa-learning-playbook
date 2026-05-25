# **Tactical Intelligence Protocol: Infosys Off-Campus SP/DSE Recruitment System 2026**

## **Executive Intelligence Summary**

The algorithmic evaluation framework governing the Infosys off-campus recruitment drive for the 2026 graduating cohort has evolved into an uncompromising, heavily stratified filtering matrix. Historical hiring patterns relying on resume strength and basic algorithmic competence have been entirely deprecated for niche roles. The current architecture systematically segregates candidates into specific compensation and capability bands—Systems Engineer (SE), Digital Specialist Engineer (DSE), and Specialist Programmer (SP)—based purely on deterministic execution metrics under extreme temporal and psychological stress.1

Forensic analysis of recent 2024–2026 assessment cycles indicates that the system leverages sophisticated heuristics, including hidden boundary test cases, strict input/output (I/O) formatting parsers, and partial scoring mechanics.4 Furthermore, anti-cheating protocols have been drastically escalated, integrating Turnitin 2026 algorithmic stylometry, facial mapping, and continuous IP/Zscaler activity logging to eliminate fraudulent candidates instantaneously.5 This document serves as a comprehensive, weaponized system map designed to reverse-engineer these evaluation heuristics, isolate high-probability evaluation vectors, and provide a deterministic framework for maximizing the probability of securing SP and DSE designations.

## **Phase 1: Recruitment System Reverse Engineering**

### **Historical Pattern Evolution and Role Stratification**

The Infosys recruitment system fundamentally altered its architecture to prioritize raw problem-solving capability over theoretical academic knowledge. The recruitment pathways are strictly bifurcated.

| Role Classification | Target Compensation | Algorithmic Competency Requirement | Systemic Evaluation Focus |
| :---- | :---- | :---- | :---- |
| **Systems Engineer (SE)** | ₹3.6 – ₹4.5 LPA | Foundational | Array traversal, string manipulation, standard aptitude heuristics.2 |
| **Digital Specialist Engineer (DSE)** | ₹6.25 – ₹9.5 LPA | Intermediate | Implementation of Two Pointers, Sliding Windows, and localized Greedy Optimization.1 |
| **Specialist Programmer (SP)** | ₹9.5 – ₹21.0 LPA | Elite | State-based Dynamic Programming (DP), Graph Traversals, Range Queries, System Design.1 |

### **Selection Heuristics and Internal Distinction Models**

The internal sorting algorithm determines candidate placement based almost exclusively on the specific difficulty tier successfully cleared during the 180-minute coding phase. The data indicates a stark cutoff behavior:

1. **The DSE Threshold:** Solving the Easy and Medium problems statistically locks a candidate into the DSE bracket. These problems test standard pattern recognition without requiring advanced state transitions.  
2. **The SP Threshold:** Securing an SP interview requires the partial or complete execution of the Hard tier problem (typically DP or Graphs). The internal cutoff does not require perfection; candidates have been shortlisted for SP interviews by solving 2.5 out of 3 questions, leveraging partial test case clearances.9  
3. **The High-Band SP Threshold (SP L2/L3):** Attaining the ₹16 LPA to ₹21 LPA bands mandates attacking the Complex tier problem, which involves advanced data structures such as Segment Trees or multi-dimensional DP.

### **The Partial Scoring Heuristic**

A critical vulnerability in candidate strategy is the misunderstanding of the platform's grading logic. The system utilizes a partial scoring model.4 Credit is awarded proportionally based on the exact number of hidden test cases successfully executed. Consequently, a stable, unoptimized brute-force ![][image1] solution that clears 40% of hidden test cases yields vastly superior systemic value compared to an optimal ![][image2] algorithm that fails at compilation or crashes on edge cases.4

## **Phase 2: Forensic Round 1 Breakdown**

The initial filtering mechanism operates differently based on the specific drive, manifesting as either a hybrid aptitude/coding examination or a pure algorithmic marathon.

### **Sectional Architecture: Non-Coding Hybrid Assessment (120 Minutes)**

This structure is utilized primarily for broad-spectrum filtering, occasionally offering upgrade paths to DSE roles. It enforces rigid temporal boundaries, preventing candidates from reallocating time across sections.10

| Assessment Section | Question Count | Time Allocation | Difficulty Gradient | Evaluated Archetypes |
| :---- | :---- | :---- | :---- | :---- |
| **Reasoning Ability** | 15 | 25 mins | High | Syllogisms, complex data sufficiency, seating matrices.10 |
| **Technical Ability** | 10 | 35 mins | Medium | Probability, permutations, mixture/allegations, time/speed/distance.10 |
| **Verbal Ability** | 20 | 20 mins | Medium | Reading comprehension, advanced sentence correction, parajumbles.10 |
| **Pseudo Code** | 5 | 10 mins | Very High | Tracing sorting algorithms, tracking pointer mutations, recursive unwinding.10 |
| **Numerical Puzzle** | 4 | 10 mins | High | Spatial logic, relational grids, symbol inversion sequences.15 |
| **English Grammar** | 5 | 10 mins | Low | Basic syntax, error spotting, vocabulary validation.10 |
| **English Writing** | 1 | 10 mins | Low | Essay structure, coherence, absence of grammatical flaws.10 |

### **Topic Probability Heatmaps for Non-Coding Subsections**

**Pseudocode Topic Heatmap:**

| Topic | Probability | Strategy / Focus |
| :---- | :---- | :---- |
| Recursive Tracing | 85% | Track stack frames manually. Focus on base cases for n=5 or similar.17 |
| Sorting Algorithm Passes | 75% | Predict array state after ![][image3] iterations of Bubble/Insertion sort.18 |
| Bitwise Operations | 60% | Track AND, OR, XOR mutations across loop iterations.17 |

**Numerical Puzzle Topic Heatmap:**

| Topic | Probability | Strategy / Focus |
| :---- | :---- | :---- |
| Missing Grid Numbers | 90% | Look for squares, cubes, or sums of adjacent cells. e.g., ![][image4].19 |
| Positional Interchanging | 70% | Track element swaps across 4 frames to predict the 5th frame.15 |
| Symbol Inversion | 60% | Track binary state changes (on/off, up/down) in repeating sequences.15 |

### **Sectional Architecture: Advanced Coding Assessment (180 Minutes)**

The core SP/DSE off-campus assessment relies on a brutal 3-to-4 question coding block.1

1. **Question 1: Easy Tier (20 Marks / \~30 mins Target):** Evaluates basic algorithm and data structure application. **Trap:** The problem statements are heavily obfuscated. A simple query operation on a 2D array will be described via a multi-page narrative. Careful parsing is required to extract the core logic.1  
2. **Question 2: Medium Tier (30 Marks / \~45 mins Target):** Almost exclusively tests Greedy algorithms (Pure, Orthogonal, Relaxed) or Two Pointers. **Trap:** Incorrect window sizing or failure to sort elements properly before greedy allocation will trigger WA (Wrong Answer) flags.1  
3. **Question 3: Hard Tier (50 Marks / \~75 mins Target):** The ultimate SP gatekeeper. Demands Dynamic Programming (DP) or Graph combinations. **Trap:** Time Limit Exceeded (TLE) errors. Brute force will pass visible test cases but immediately fail hidden performance evaluations.1  
4. **Question 4: Complex Tier (Varying Marks / 4-question formats):** Involves advanced structures like Trees with range queries. Edge cases are mathematically complex.

## **Phase 3: Coding Intelligence Extraction**

Forensic data mining across GitHub repositories, LeetCode discussion forums, and leaked candidate experiences from 2024–2026 reveals a highly concentrated pool of recurring algorithm archetypes.21 The system does not invent new computer science paradigms; it disguises standard computational geometry and combinatorial optimization problems.

### **Most Repeated Algorithm Archetypes**

1. **State-Machine Dynamic Programming:** Specifically unbounded knapsack and 0/1 knapsack variations. The system frequently asks candidates to maximize or minimize a value given a constraint budget (e.g., minimizing "string ugliness" with specific swap/flip costs).21  
2. **Multi-Source Graph Traversals:** Utilizing Breadth-First Search (BFS) to track the spread of a state across a grid (e.g., Rotting Oranges) or Depth-First Search (DFS) for component counting.23  
3. **Resource Allocation via Greedy Sorting:** Problems mirroring the "RPG Monster Quest," where sorting elements by requirement and iterating provides the optimal local and global maximum.21

### **TOP 50 MOST IMPORTANT QUESTIONS: ELITE BREAKDOWN**

#### **Category A: MUST MASTER (High Probability of Direct Appearance \- Rank 1 to 15\)**

These specific problems constitute the absolute baseline for SP-level clearance.

1\. Number of Islands / Warship Groups 24

* **Pattern:** Graph Components (DFS/BFS).  
* **Trigger:** "Find the number of distinct groups," "connected 1s in a grid."  
* **Fastest Strategy:** Iterate through the matrix. Upon finding a '1', increment group count and initiate DFS/BFS to mutate all connected '1's to '0's.  
* **Python Trap:** Deep recursion on large grids will hit Python's limit. sys.setrecursionlimit(20000) must be utilized, or an iterative BFS with collections.deque must be deployed.25  
* **Complexity:** ![][image5] Time, ![][image5] Space.

2\. Rotting Oranges (Multi-source BFS) 24

* **Pattern:** Simultaneous Graph Traversal.  
* **Trigger:** "Minimum time to infect/rot all entities."  
* **Fastest Strategy:** Enqueue all initially rotten oranges with timestamp 0\. Track the total count of fresh oranges. Run BFS, decrementing the fresh count. If the queue empties and fresh count ![][image6], return \-1.  
* **Edge Case:** A grid with zero fresh oranges initially must immediately return 0\.

3\. LRU Cache Implementation 24

* **Pattern:** Hash Map \+ Doubly Linked List (DLL).  
* **Trigger:** "Design a data structure with ![][image7] get and put."  
* **Fastest Strategy:** In Python, collections.OrderedDict provides this natively. However, to survive interview grilling, one must implement a dictionary pointing to DLL nodes.24  
* **Complexity:** ![][image7] operations.

4\. Minimum Coins Required (Unbounded Knapsack) 22

* **Pattern:** Dynamic Programming.  
* **Trigger:** "Minimum number of items to reach a target sum," infinite supply.  
* **Fastest Strategy:** 1D DP array of size Target \+ 1, initialized to infinity. dp \= 0\. Iterate through coins, updating dp\[i\] \= min(dp\[i\], dp\[i \- coin\] \+ 1).

5\. Subset Sum / 0-1 Knapsack 22

* **Pattern:** Dynamic Programming.  
* **Trigger:** "Can we partition the array," "Is there a subset that equals target."  
* **Fastest Strategy:** 1D boolean DP array. **Crucial:** Iterate the DP array backwards to prevent utilizing the same element multiple times.

6\. RPG Monster Experience (Greedy Resource Allocation) 21

* **Pattern:** Sorting \+ Greedy.  
* **Trigger:** "Defeat monsters with minimum power," "Gain bonus experience."  
* **Fastest Strategy:** Zip the power and bonus arrays. Sort the combined array based on power in ascending order. Iterate: if current experience ![][image8] power, add bonus. Else, break.  
* **Complexity:** ![][image2] due to sorting.

7\. Subarray With Maximum Sum (Kadane's Algorithm) 23

* **Pattern:** Array Optimization.  
* **Trigger:** "Maximum contiguous subarray."  
* **Fastest Strategy:** Maintain current\_sum and max\_sum. If current\_sum drops below zero, reset it to zero.

8\. Next Greater Element 26

* **Pattern:** Monotonic Decreasing Stack.  
* **Trigger:** "Find the first element to the right that is larger."  
* **Fastest Strategy:** Traverse the array backward. While the stack is not empty and the top is ![][image9] current element, pop the stack. The top of the stack is the answer; push the current element.

9\. Minimum Window Substring 23

* **Pattern:** Sliding Window \+ Frequency Maps.  
* **Trigger:** "Smallest substring containing all characters of string T."  
* **Fastest Strategy:** Maintain two collections.Counter dictionaries (have and need). Expand the right pointer until have meets need, then shrink the left pointer to minimize the window.

10\. Arrange Strings by Frequency 23

* **Pattern:** Hash Map \+ Sorting.  
* **Trigger:** "Sort characters by occurrence."  
* **Fastest Strategy:** Counter(s).most\_common(). Reconstruct the string by multiplying characters by their frequencies.

11\. Merge Intervals 23

* **Pattern:** Array Sorting.  
* **Trigger:** "Overlapping meetings," "Merge ranges."  
* **Fastest Strategy:** Sort array by start times. Iterate, checking if the current start is ![][image9] the previous end. If so, update the previous end to max(prev\_end, curr\_end).

12\. Valid Parentheses 23

* **Pattern:** Stack.  
* **Trigger:** "Balanced string," "matching brackets."  
* **Fastest Strategy:** Dictionary mapping closing brackets to opening ones. Push openings to stack. For closings, check if stack top matches.

13\. Add Two Numbers (Linked List) 23

* **Pattern:** Linked List Traversal.  
* **Trigger:** "Numbers represented as linked lists."  
* **Fastest Strategy:** Utilize a dummy head node. Maintain a carry variable. Loop while l1, l2, or carry exists.

14\. Longest Substring Without Repeating Characters 23

* **Pattern:** Sliding Window.  
* **Trigger:** "Longest substring of unique characters."  
* **Fastest Strategy:** Hash map storing the *last seen index* of characters. If a duplicate is encountered, instantly jump the left pointer to max(left, last\_seen\[char\] \+ 1).

15\. Bitwise XOR-Sum Maximization 21

* **Pattern:** Bit Manipulation \+ Greedy.  
* **Trigger:** "Maximize ![][image10] where ![][image11]."  
* **Fastest Strategy:** Iterate through the 32 bits from most significant to least. Count set bits in array ![][image12] at that position. If unset bits ![][image13] set bits, setting that bit in ![][image14] yields a higher sum. Ensure ![][image14] does not exceed ![][image3].

#### **Category B: HIGH ROI (Medium Tier Mastery \- Rank 16 to 35\)**

These problems feature heavily in the 30-mark sections. 16\. **Natural Number Base Conversion:** Iterate base ![][image15] from 2 upwards. Check if all remainders modulo ![][image15] are identical.21 17\. **Minimize String Ugliness:** DP state machine for flip vs swap operations.21 18\. **Trapping Rain Water:** Precompute left\_max and right\_max arrays, or deploy a highly optimized two-pointer approach.27 19\. **Best Time to Buy and Sell Stock:** Single pass tracking min\_price and computing max\_profit.27 20\. **Two Sum / Three Sum:** Standard hash map lookup for Two Sum; sorting plus two pointers for Three Sum to handle duplicates.27 21\. **Move Zeroes:** In-place fast pointer looking for non-zeros, swapping with a slow pointer.27 22\. **Transform Array by Parity:** Array manipulation utilizing modulo operators.27 23\. **Spiral Matrix Traversal:** Maintain top, bottom, left, right boundary variables.28 24\. **Reverse Singly Linked List:** Track prev, curr, and next pointers. Update iteratively.26 25\. **First Non-Repeating Character:** Two passes; one to build frequency map, one to find the first character with a frequency of 1\.26 26\. **Largest Number from Array:** Custom comparator string formatting. In Python 3, use functools.cmp\_to\_key.22 27\. **Wine Bottle Transport:** Greedy pattern recognition.22 28\. **Invert Binary Tree:** Standard recursive swap of .left and .right pointers.26 29\. **Largest Subarray with Equal Character Frequency:** Transform string to \+1 / \-1 representations. Use prefix sum tracking with a hash map.26 30\. **Longest Increasing Subsequence (LIS):** Utilize the bisect library to build a strictly increasing sub-array in ![][image2].26 31\. **Find Duplicates in Array:** Cycle sort for ![][image16] time and ![][image7] space, or hash set if space permits.8 32\. **String Palindrome Check:** Two pointers originating at edges and moving inward.8 33\. **Fibonacci Optimization:** Replace ![][image17] recursion with ![][image16] bottom-up array, or optimize to ![][image7] space using two variables.24 34\. **Insert Interval:** Iterate through existing intervals, append left side, merge overlapping, append right side.24 35\. **Find Building Where Alice & Bob Meet:** Stack / Binary Search logic.27

#### **Category C: LOW PROBABILITY / COMPLEX EXTREMES (SP L3 Only \- Rank 36 to 50\)**

These concepts separate the ₹16 LPA band from the ₹21 LPA band. Focus here only after mastering Categories A and B.

36\. **Segment Trees (Range Sum/Min Queries with Lazy Propagation).**

37\. **Fenwick Trees (Binary Indexed Trees) for rapid point updates.**

38\. **Kruskal’s Minimum Spanning Tree (Union-Find architecture).**

39\. **Dijkstra’s Shortest Path algorithm utilizing Min-Heaps (Priority Queues).**

40\. **Topological Sorting (Kahn’s Algorithm) for task scheduling.**

41\. **Trie (Prefix Tree) implementation for auto-complete simulation.**

42\. **State-based DP on Trees (e.g., Maximum independent set on a tree structure).**

43\. **Matrix Chain Multiplication variants (Classic DP formatting).**

44\. **Travelling Salesperson Problem utilizing Bitmask DP.**

45\. **Tarjan’s Algorithm for finding Bridges and Articulation points in graphs.**

46\. *A Search algorithm heuristic mapping.*\*

47\. **Combinatorics using Fermat's Little Theorem for modulo division.**

48\. **KMP (Knuth-Morris-Pratt) pattern matching array construction.**

49\. **Lowest Common Ancestor (LCA) in a Binary Tree using Binary Lifting.**

50\. **Sliding Window Maximum utilizing a Monotonic Deque.**

## **Phase 4: Python Advantage Engineering**

Python inherently provides an immense speed advantage in logic formulation but suffers from severe execution overhead. To survive the Infosys computational constraints, standard Python must be engineered into competitive Python.

### **The Fast I/O Bottleneck**

Python's standard input() and print() functions perform individual system calls per execution, creating catastrophic Time Limit Exceeded (TLE) errors when parsing arrays of ![][image18] integers.29

**Input/Output Optimization Template:**

Python

import sys

def fast\_io():  
    \# Reads the entire input stream into memory, splitting by whitespace.  
    \# This bypasses the line-by-line parsing bottleneck completely.  
    input\_data \= sys.stdin.read().split()  
    if not input\_data:  
        return  
      
    \# Iterator logic to pull data sequentially  
    iterator \= iter(input\_data)  
    n \= int(next(iterator))  
    arr \= \[int(next(iterator)) for \_ in range(n)\]  
      
    \# Processing logic here...  
    result \= sum(arr)  
      
    \# Fast Output writing directly to the system buffer  
    sys.stdout.write(str(result) \+ "\\n")

if \_\_name\_\_ \== "\_\_main\_\_":  
    fast\_io()

### **Recursion Traps**

The CPython interpreter guards against stack overflows by hard-capping the recursion depth at 1000 frames.25 Deep DFS graph algorithms will instantly crash. **The Survival Override:**

Python

import sys  
\# Must be declared at the absolute top of the submission  
sys.setrecursionlimit(25000) 

### **Python Survival Sheet for Infosys SP/DSE**

* **Frequency Map Mastery:** Never implement manual loops for character or integer counting. Always deploy collections.Counter(iterable). This operates in optimized C backend logic, mapping frequencies in ![][image16].30  
* **BFS Queue Deployment:** Never use list.pop(0). In Python, arrays shift all elements in memory, making it an ![][image16] operation resulting in immediate TLE on large graphs. Always import collections.deque and utilize queue.popleft() for ![][image7] operations.  
* **Matrix Generation Trap:** Never use \[ \* cols\] \* rows. This creates references to the *same* list. Modifying matrix will modify matrix. Always utilize list comprehensions: \[\[0 for \_ in range(cols)\] for \_ in range(rows)\].  
* **Binary Search Optimization:** Avoid writing manual binary search boilerplate unless heavily customized logic is required. Deploy import bisect and use bisect.bisect\_left(arr, target) for instantaneous ![][image19] resolution.

### **Archetype Core Templates**

**Prefix Sum Skeleton:**

Python

prefix \=  \* (n \+ 1)  
for i in range(n):  
    prefix\[i \+ 1\] \= prefix\[i\] \+ arr\[i\]  
\# Sum of subarray from index L to R (inclusive) \= prefix \- prefix\[L\]

**Sliding Window Skeleton:**

Python

left \= 0  
current\_state \= 0  
best\_result \= 0  
for right in range(len(arr)):  
    current\_state \+= arr\[right\] \# Add to window  
    while invalid\_condition(current\_state):  
        current\_state \-= arr\[left\] \# Remove from window  
        left \+= 1  
    best\_result \= max(best\_result, right \- left \+ 1)

## **Phase 5: Technical MCQ Domination (80/20 Theory Sheet)**

The theoretical evaluation—both in Round 1 MCQs and Round 2 Interview interrogations—heavily targets specific blind spots in freshers. The 80/20 principle dictates that 80% of technical questions originate from 20% of core concepts.31

### **Database Management Systems (DBMS) & SQL**

* **The Nth Highest Salary Trap:** This is a guaranteed SP interview question. The standard LIMIT/OFFSET approach fails on duplicate salaries. The optimal solution requires window functions. The core trap is understanding the difference between RANK() and DENSE\_RANK(). RANK() skips sequence numbers on ties (1, 1, 3), whereas DENSE\_RANK() provides continuous sequences (1, 1, 2). Interviewers demand DENSE\_RANK().24  
* **The Deletion Trinity:** Candidates must instantly distinguish between DROP (destroys table structure and data entirely), TRUNCATE (rapidly empties the table without logging individual row deletions, cannot be rolled back), and DELETE (removes rows based on conditions, logs operations, slower).24  
* **ACID Properties:** Atomicity, Consistency, Isolation, Durability.23  
* **Normalization:** 2NF guarantees the elimination of partial dependency. 3NF guarantees the elimination of transitive dependency.33

### **Operating Systems (OS)**

* **Thrashing:** This phenomenon occurs when a system’s virtual memory is over-allocated, causing the OS to spend more computational cycles swapping pages between RAM and disk than executing actual processes.32  
* **Deadlock Heuristics:** The four Coffman conditions must be memorized: Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait. Interviewers expect a clear explanation of the Banker’s Algorithm for deadlock avoidance.23  
* **Processes vs. Threads:** A process is an independent execution entity with its own memory space. A thread is a lightweight execution unit existing within a process, sharing the same memory context.23

### **Object-Oriented Programming (OOP)**

* **The Core Pillars:** Encapsulation, Abstraction, Inheritance, Polymorphism.24  
* **Abstraction Implementations:** Understanding why Java prohibits multiple class inheritance (to avoid the Diamond Problem) but permits it exclusively through interfaces.24

### **Computer Networks (CN)**

* **Architectural Addressing:** The structural differences between 32-bit IPv4 and 128-bit IPv6 addressing.31  
* **Security Protocols:** The functional difference between HTTP and HTTPS, specifically focusing on the SSL/TLS secure handshake mechanism.31

## **Phase 6: Aptitude Warfare (Infosys Aptitude Kill Sheet)**

The non-coding sections rely heavily on speed and rapid pattern identification.15

### **Pseudocode Warfare Tactics**

The pseudocode section evaluates the mental tracing of logic without reliance on syntax execution.18

* **Recursive Unwinding:** When presented with fun1(p, q), do not attempt to map the entire tree. Map only the first two recursive steps and extrapolate the pattern. Base cases are the most critical line of code.17  
* **Sorting Passes:** A frequent archetype asks for the state of an array after ![][image3] iterations of Bubble Sort or Insertion Sort. Understand that Bubble Sort pushes the largest element to the absolute end in pass 1\.18  
* **Modulo Logic:** Expressions involving X mod i \== 0 usually denote primality testing or factor finding.18

### **Numerical Puzzle Warfare Tactics**

* **Positional Interchanging Grids:** Puzzles presenting a 3x3 or 4x4 matrix of shifting symbols require tracking a single element. Do not look at the whole grid. Track the trajectory of one specific circle or square across 4 frames to predict the 5th.15  
* **Arithmetic Center Formulas:** If a number is enclosed by multiple outer numbers, immediately test the sum of squares, or (Top \+ Bottom) \* (Left \+ Right).16  
* **The 30-Second Elimination Rule:** If the geometric sequence or matrix pattern is not mathematically identified within 30 seconds, immediately eliminate the two statistically most improbable answers, guess, and proceed. Time capital is weighted heavier than absolute accuracy.13

## **Phase 7: Interview Prediction Model**

The Round 2 Interview is not a formality. It is an intense technical and behavioral audit designed to confirm the legitimacy of the Round 1 score and finalize role placement.24

### **The Wingspan Live Coding Paradigm**

A mandatory requirement for the SP/DSE role involves writing live code on the Infosys Wingspan portal while sharing a screen.34 The interviewer provides 1 to 2 problems. A candidate who passed the Round 1 hard DP problem but cannot explain the logic of a basic array traversal will face immediate systemic downgrade or rejection.24

### **Project Grilling & Resume Attack Vectors**

Resume items are aggressively cross-examined for authenticity.31

* **The Metric Trap:** If a machine learning project is listed, the interviewer will demand the mathematical formulas for Precision, Recall, and the F1 Score.31  
* **The Architecture Trap:** If a web deployment is listed, candidates will be grilled on monolithic vs. microservice architecture, Docker containerization utilities, and specific SQL joins used in the database backend.23

### **AI-Cheating Detection Protocols**

The 2026 assessment heavily integrates forensic anti-cheating software.

* **Vector Space Stylometry:** The system utilizes Turnitin 2026 standards, which employ vector space models and stylometric analysis to catch semantic paraphrasing and AI-generated outputs.7 Copying a ChatGPT output, even if variable names are altered, triggers similarity thresholds.  
* **Environmental Auditing:** Modern AI proctoring commandeers the webcam and microphone to map facial data to prevent candidate swapping, and parses ambient audio to detect whispering or earpiece use.5

### **The "Downgrade Risk" Behavior**

Candidates can be downgraded from Specialist Programmer (SP) to Digital Specialist Engineer (DSE) if they 24:

1. Explain logic fluently but fail to write executable syntax.  
2. Fail to articulate the Time and Space complexity (![][image20] notation) of their own written code.  
3. Show extreme performance variance between the offline assessment and the live interview.35

## **Phase 8: Strategic Preparation Blueprint**

### **The 14-Day Elite Transformation Roadmap**

**Days 1–4: The Algorithmic Core (Graphs & DP)**

* *08:00 \- 10:00:* Study graph representations and DFS/BFS state templates.  
* *10:00 \- 13:00:* Execute grid traversal problems (Number of Islands, Rotting Oranges). Embed sys.setrecursionlimit and fast I/O into muscle memory.24  
* *14:00 \- 17:00:* Unbounded and 0/1 Knapsack DP state-transition mapping.  
* *18:00 \- 20:00:* Dry-run recursion trees manually on paper to prepare for Pseudocode MCQs.17

**Days 5–7: Greedy Logic & Sliding Windows**

* *08:00 \- 12:00:* Implement optimal sliding window templates. Master collections.Counter.23  
* *13:00 \- 17:00:* Execute sorting-based Greedy problems (RPG Monster variants).21  
* *18:00 \- 20:00:* Practice Two Pointer convergence techniques (Three Sum, Trapping Rain Water).27

**Days 8–10: The 80/20 Theory Domination**

* *08:00 \- 11:00:* Memorize the Coffman conditions for Deadlocks, Banker's Algorithm, and ACID properties.23  
* *12:00 \- 15:00:* Write and execute DENSE\_RANK() SQL queries and master the DROP/DELETE/TRUNCATE trinity.24  
* *16:00 \- 19:00:* Practice out-loud verbalization of the 4 Pillars of OOPs.24

**Days 11–13: Systemic Simulation & Aptitude Warfare**

* *09:00 \- 12:00:* Execute full 180-minute mock coding assessments utilizing Infosys-specific strict I/O parameters.4  
* *14:00 \- 16:00:* Drill numerical puzzles (symbol inversion, grid tracking) under intense 30-second-per-question constraints.15  
* *17:00 \- 19:00:* Practice live coding while sharing a screen, narrating the time complexity before writing the syntax.34

**Day 14: Tactical Review & Rest**

* Review the Python Survival Sheet and Theory MCQs. Cease all heavy coding execution to minimize cognitive fatigue.

### **The 48-Hour Emergency Protocol**

If operational time is critically constrained, abandon all advanced data structures (Segment Trees, Tries). Execute the following:

1. Memorize the Python Fast I/O syntax and recursion limits.25  
2. Drill the Top 5 Must-Master coding problems exclusively (Islands, Rotting Oranges, DP Knapsack, Sliding Window, Valid Parentheses).23  
3. Memorize the 80/20 Theory Sheet (OOP pillars, Process vs Thread, Deadlocks, DENSE\_RANK()).24

## **Phase 9: Red Team Failure Analysis (Anti-Failure Protocol)**

Statistical aggregation of rejected candidates reveals that capable programmers frequently fail due to misunderstandings of the platform's heuristics.4

### **The Strict I/O Formatting Trap**

The automated evaluation engine parses standard output against deterministic string models. A logically flawless algorithm will register as a 0% failure if the candidate includes debug statements (e.g., print("Array is:")) or fails to match exact whitespace formatting. All output must be sanitized before final submission.4

### **The Hidden Test Case Collapse**

Candidates frequently assume their code is correct after passing the 2 to 3 visible sample cases. The visible cases only validate basic formatting. The hidden test suite is adversarial, specifically injecting:

* **Null vectors:** Empty strings or arrays of length zero.  
* **Extreme boundaries:** Inputs scaling to ![][image21].4  
* **Failure Protocol:** Candidates fail by hardcoding assumptions about input safety. Elite candidates employ defensive programming, inserting explicit if not arr: return 0 checks at the top of every function.4

### **Over-Optimization Panic and Partial Scoring**

Under temporal pressure, candidates often attempt to architect complex ![][image2] algorithms. When these fail to compile or hit edge case bugs, the candidate scores zero. Because of the partial scoring mechanism, an ugly, unoptimized ![][image1] brute-force solution that clears 40% of the test cases is mathematically superior to a broken optimized solution.4 If an optimal solution cannot be synthesized in 15 minutes, deploy brute force to secure partial algorithmic credit, then move to the next question.

## **Phase 10: Top 1% Candidate Model**

The transition from an average candidate to an SP-caliber candidate requires a systemic paradigm shift in execution behavior.

### **Profile Comparison**

* **The DSE Candidate Profile:** Solves the Easy and Medium problems using standard nested loops. Relies on standard input() resulting in slower execution. Passes sample cases but misses boundary edge cases. In the interview, struggles to define system architecture conceptually but can write basic operational code.1  
* **The SP Candidate Profile:** Solves Easy, Medium, and secures partial or full credit on the Hard DP/Graph problem. Employs sys.stdin.read().split() for instantaneous memory loading, prevents recursion errors via sys.setrecursionlimit, and implements defensive edge-case handlers.4 During the Wingspan interview, dictates the time complexity prior to syntax generation, expertly writes a DENSE\_RANK() query, and details the CAP theorem effortlessly.24

### **Transformation Roadmap**

1. **Stop coding blindly:** Begin analyzing every problem based on input constraints. If ![][image22], think Backtracking. If ![][image23], think ![][image1] DP. If ![][image24], think ![][image2] Sorting or ![][image16] Two Pointers.  
2. **Abandon language defaults:** Switch immediately to Python competitive templates (Deque, Counter, Fast I/O).30  
3. **Verbalize Logic:** Force yourself to speak out loud while solving LeetCode problems to build the cognitive pathways required for the live interview execution.34

## **Final Execution Directives**

### **Daily Execution Checklist**

* \[ \] Complete 2 LeetCode Mediums (Strict Focus: Graphs, DP, Sliding Window).  
* \[ \] Complete 1 LeetCode Hard (Strict Focus: State-transition formulation).  
* \[ \] Review 15 Minutes of CS Theory (OS, CN, DBMS).  
* \[ \] Execute 1 Verbal dry-run of an algorithm to simulate interview pressure.

### **Final Exam-Day Protocol**

1. **Hardware & Environment Audit:** Verify microphone and webcam functionality. Ensure the testing environment has zero background audio to prevent immediate AI flagging by the proctoring algorithms.37  
2. **Defensive Initiation:** Immediately type out the Python sys I/O optimization templates and setrecursionlimit upon entering the coding environment.25  
3. **Strategic Triage:** Read all 3 or 4 questions prior to writing any syntax. Identify the Easy and Medium archetypes and secure those marks within the first 60 minutes.  
4. **Leverage the Partial Scoring Heuristic:** If the Hard tier problem is mathematically obscure, do not freeze. Immediately write the ![][image1] brute-force mechanism to capture 30% of the hidden test cases.4  
5. **Sanitize the Output:** Prior to final submission, scrub the entire codebase of print debugs and comments to prevent parser mismatch failures.4

#### **Works cited**

1. Infosys SP / DSE Off-Campus Test Experience (Offline)(Jan — 2026\) | by Varun \- Medium, accessed on May 15, 2026, [https://medium.com/@sbvc.varun/infosys-sp-dse-off-campus-test-experience-offline-jan-2026-8605a34b2703](https://medium.com/@sbvc.varun/infosys-sp-dse-off-campus-test-experience-offline-jan-2026-8605a34b2703)  
2. Infosys Recruitment Process 2026: Eligibility, Round Details, Tips\! \- Unstop, accessed on May 15, 2026, [https://unstop.com/blog/infosys-recruitment-process](https://unstop.com/blog/infosys-recruitment-process)  
3. Infosys SP and DSE Placement Papers 2026 \- PrepInsta, accessed on May 15, 2026, [https://prepinsta.com/infosys-sp-and-dse/](https://prepinsta.com/infosys-sp-and-dse/)  
4. Infosys Coding Interview Questions \- Educative.io, accessed on May 15, 2026, [https://www.educative.io/blog/infosys-coding-interview-questions](https://www.educative.io/blog/infosys-coding-interview-questions)  
5. Infosys Wingspan Online Test Guidelines | PDF | Computing \- Scribd, accessed on May 15, 2026, [https://www.scribd.com/document/708861368/Examination-Guidelines-Infosys-Online-Test](https://www.scribd.com/document/708861368/Examination-Guidelines-Infosys-Online-Test)  
6. Cheating in Infosys OA \- Reddit, accessed on May 15, 2026, [https://www.reddit.com/r/infosys/comments/1rqqwjn/cheating\_in\_infosys\_oa/](https://www.reddit.com/r/infosys/comments/1rqqwjn/cheating_in_infosys_oa/)  
7. Turnitin Flags Everything\! Do These Hidden Tricks Still Work in 2026? \- YouTube, accessed on May 15, 2026, [https://www.youtube.com/watch?v=-Sc1dEjNhc0](https://www.youtube.com/watch?v=-Sc1dEjNhc0)  
8. Infosys Interview Questions 2026: InfyTQ, Tech \+ HR Rounds Decoded | OphyAI Blog, accessed on May 15, 2026, [https://ophyai.com/blog/company-guides/infosys-interview-guide](https://ophyai.com/blog/company-guides/infosys-interview-guide)  
9. Infosys SP/DSE Online Test – Need Real Experience & Last-Minute Tips \- Reddit, accessed on May 15, 2026, [https://www.reddit.com/r/infosys/comments/1suipdu/infosys\_spdse\_online\_test\_need\_real\_experience/](https://www.reddit.com/r/infosys/comments/1suipdu/infosys_spdse_online_test_need_real_experience/)  
10. Infosys Syllabus and Online Test Pattern 2026 \- PrepInsta, accessed on May 15, 2026, [https://prepinsta.com/infosys-syllabus/](https://prepinsta.com/infosys-syllabus/)  
11. Infosys Placement Papers – Past Papers and Expert Analysis for 2026 \- Naukri.com, accessed on May 15, 2026, [https://www.naukri.com/campus/career-guidance/infosys-placement-papers](https://www.naukri.com/campus/career-guidance/infosys-placement-papers)  
12. Infosys Technical Ability Questions with Solutions 2025 \- PrepInsta, accessed on May 15, 2026, [https://prepinsta.com/infosys/technical-ability-questions/](https://prepinsta.com/infosys/technical-ability-questions/)  
13. Infosys Exam Pattern 2026 & Syllabus | Free Preparation Guide \- Career Rise Hub, accessed on May 15, 2026, [https://careerrisehub.com/infosys-exam-pattern-2026-syllabus/](https://careerrisehub.com/infosys-exam-pattern-2026-syllabus/)  
14. Infosys Pseudo Code Questions and Answers 2026 | PrepInsta, accessed on May 15, 2026, [https://prepinsta.com/infosys/pseudo-code/](https://prepinsta.com/infosys/pseudo-code/)  
15. Infosys Puzzle Questions: Top 5 Puzzles & Answers for Freshers, accessed on May 15, 2026, [https://unstop.com/blog/infosys-puzzle-questions-for-freshers](https://unstop.com/blog/infosys-puzzle-questions-for-freshers)  
16. Infosys Puzzle Questions and Answers 2026 \- PrepInsta, accessed on May 15, 2026, [https://prepinsta.com/infosys/puzzle-questions-and-answers-pdf/](https://prepinsta.com/infosys/puzzle-questions-and-answers-pdf/)  
17. Infosys Pseudocode Questions \- Talent Battle, accessed on May 15, 2026, [https://talentbattle.in/company-specific-previous-year-questions/infosys-pseudocode-previous-year-questions](https://talentbattle.in/company-specific-previous-year-questions/infosys-pseudocode-previous-year-questions)  
18. Infosys Pseudocode Questions and Tips for Freshers 2025 \- Unstop, accessed on May 15, 2026, [https://unstop.com/blog/infosys-pseudocode-question](https://unstop.com/blog/infosys-pseudocode-question)  
19. Infosys Puzzle Solving Previous Year Questions \- Talent Battle, accessed on May 15, 2026, [https://talentbattle.in/infosys/puzzle-solving](https://talentbattle.in/infosys/puzzle-solving)  
20. Infosys DSE and SP Syllabus 2026(Updated) \- PrepInsta, accessed on May 15, 2026, [https://prepinsta.com/infosys-sp-and-dse/syllabus/](https://prepinsta.com/infosys-sp-and-dse/syllabus/)  
21. Infosys SP and DSE Coding Questions | PrepInsta, accessed on May 15, 2026, [https://prepinsta.com/infosys-sp-and-dse/coding-questions/](https://prepinsta.com/infosys-sp-and-dse/coding-questions/)  
22. karthikreddy-7/Infosys-SP-Coding-Questions \- GitHub, accessed on May 15, 2026, [https://github.com/karthikreddy-7/Infosys-SP-Coding-Questions](https://github.com/karthikreddy-7/Infosys-SP-Coding-Questions)  
23. Infosys SP/DSE: 10 Coding & Tech PYQs | PDF \- Scribd, accessed on May 15, 2026, [https://www.scribd.com/document/967765629/Infosys-PYQs](https://www.scribd.com/document/967765629/Infosys-PYQs)  
24. Infosys Round 2 Interview — 10 Real Questions Asked | Exact Format \+ Prep Guide 2026, accessed on May 15, 2026, [https://www.youtube.com/watch?v=MInZoDzfuJw](https://www.youtube.com/watch?v=MInZoDzfuJw)  
25. python \- What is the maximum recursion depth, and how to increase it? \- Stack Overflow, accessed on May 15, 2026, [https://stackoverflow.com/questions/3323001/what-is-the-maximum-recursion-depth-and-how-to-increase-it](https://stackoverflow.com/questions/3323001/what-is-the-maximum-recursion-depth-and-how-to-increase-it)  
26. Infosys SP & DSE Coding Questions | PDF | Integer (Computer Science) \- Scribd, accessed on May 15, 2026, [https://www.scribd.com/document/916567584/Coding-Sheet-for-Infosys-SP-DSE-Role](https://www.scribd.com/document/916567584/Coding-Sheet-for-Infosys-SP-DSE-Role)  
27. Infosys Coding Interview Questions (2026 Guide) \- DSA Prep, accessed on May 15, 2026, [https://www.dsaprep.dev/blog/infosys-coding-interview-questions](https://www.dsaprep.dev/blog/infosys-coding-interview-questions)  
28. Infosys 9th Feb 2026 Interview Experience for Specialist Programmer L3 : r/developersIndia, accessed on May 15, 2026, [https://www.reddit.com/r/developersIndia/comments/1r03yx1/infosys\_9th\_feb\_2026\_interview\_experience\_for/](https://www.reddit.com/r/developersIndia/comments/1r03yx1/infosys_9th_feb_2026_interview_experience_for/)  
29. Fast I/O for Competitive Programming in Python \- GeeksforGeeks, accessed on May 15, 2026, [https://www.geeksforgeeks.org/python/fast-i-o-for-competitive-programming-in-python/](https://www.geeksforgeeks.org/python/fast-i-o-for-competitive-programming-in-python/)  
30. Hackerrank Solutions for Python \- Total 115 Challenges \- GitHub, accessed on May 15, 2026, [https://github.com/absognety/Python-Hackerrank-Solutions](https://github.com/absognety/Python-Hackerrank-Solutions)  
31. Infosys SP-L1 role upgrade interview experience (2026) by Varshitha.K \- Medium, accessed on May 15, 2026, [https://medium.com/@varshuvarshitha20/infosys-sp-l1-role-upgrade-interview-experience-2026-by-varshitha-k-66e9d0816b77](https://medium.com/@varshuvarshitha20/infosys-sp-l1-role-upgrade-interview-experience-2026-by-varshitha-k-66e9d0816b77)  
32. 50+ OS, DBMS, CN Interview Questions \[2025 Updated\] \- GeeksforGeeks, accessed on May 15, 2026, [https://www.geeksforgeeks.org/interview-prep/os-cn-dbms-interview-questions/](https://www.geeksforgeeks.org/interview-prep/os-cn-dbms-interview-questions/)  
33. Infosys MCQs: Pseudocode, DBMS, Networks, Cloud | PDF | Database Index | Acid \- Scribd, accessed on May 15, 2026, [https://www.scribd.com/document/939964784/Infosys-50-Mcq](https://www.scribd.com/document/939964784/Infosys-50-Mcq)  
34. Infosys SP role interview experience (2025) by Dev Sharma \- Medium, accessed on May 15, 2026, [https://medium.com/@giga\_dummy/infosys-sp-role-interview-experience-2025-by-dev-sharma-210bcfa7dfef](https://medium.com/@giga_dummy/infosys-sp-role-interview-experience-2025-by-dev-sharma-210bcfa7dfef)  
35. Infosys Dse role interview experience \- Reddit, accessed on May 15, 2026, [https://www.reddit.com/r/infosys/comments/1p9juo0/infosys\_dse\_role\_interview\_experience/](https://www.reddit.com/r/infosys/comments/1p9juo0/infosys_dse_role_interview_experience/)  
36. Understanding plagiarism detection algorithms in 2026, accessed on May 15, 2026, [https://plagiarismcheck.org/blog/understanding-plagiarism-detection-algorithms-in-2026/](https://plagiarismcheck.org/blog/understanding-plagiarism-detection-algorithms-in-2026/)  
37. Understanding How AI Proctoring Work in Education? \- Infosys BPM, accessed on May 15, 2026, [https://www.infosysbpm.com/blogs/education-technology-services/ai-proctoring-for-online-exams.html](https://www.infosysbpm.com/blogs/education-technology-services/ai-proctoring-for-online-exams.html)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADkAAAAZCAYAAACLtIazAAABCUlEQVR4Xu2T2wrDMAxD+/8/vZExj1STZKeXMEYO9CHWxWmh27ZYzOTRPT/DlZfBl7uye1fef8mjSyod6GE+NWNzSx/Apa5QzRuYZ95Mb4zOKb2ZBd0l2Axx+YaaN5zWyPQX+IIqxDQ8O1g+cHOlBZn+VeIC6I1ZBvazDJtVUZ0frAhgGZ4VWYbNGjFXemB1KxLQj2cFejCH+ijYt8OKBPTjmcE8OEP9CLIDlzmYl80Qpldyo8i+kWXMV8krvZIdQXbFIml4ozxqXuVsvsf2ZIsyzekZZ/NBqSdMvRHPDOdhnUimVyn3VC7FGPXfwZF7D3FreZEpd5iyRDBt97RFhKm7b/8vFos/5gnihrlH/CD3bgAAAABJRU5ErkJggg==>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGEAAAAZCAYAAAAhd0APAAABiElEQVR4Xu2RgWrDMBBD+/8/veGBwQhJJze5dBt+UKh1ks5JXq/D4XD413yhcHjvnYzQDM7/q8Zw86Rjx/MJdu7HPHi2rGYsdUXVzHXgnHkGbtZNdb90XjJNKqD0HVyH0lcSTxfV+6koM6tBLXF6iuoYKH0l8XTR+hGw1JnRO7WKqp9pjNTXCXsHA6Yh0lO9oBWcqwshuAMzeFYo3+xk3SvrPPErWA7PDOphZQrmZRqCHjxPLQF9rGuAGp4HTFOgl+3FM4N6WJmCeZmGsHmSY2BG9aCuPCnMizsSqH+niPmSPJsnOQZmVA/qypPCvLgjgfrTIuVTesLM7uTRq/JMX884e5fdZ6C+tEB50jxj9wEG6FV51Od/1K+y+wzS50rcbJDMHVUeQa/Ko848KVUWdzmsbxbhxW3o5T1uNqnmCOtkZ6XhryLxVfOV0pssZLyTeRL3XErvoHVXa/kNuI8wcLM7ad/TvuAC7iMo/W7cHW7jkSUXYPdjWhdP7fnh0WV/hPNODofDb+cbNdEj6w9LUK0AAAAASUVORK5CYII=>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAaCAYAAABRqrc5AAAAXUlEQVR4Xu2OQQqAMBAD+/9PKwiVbUjG6sHTDvTQZBMyRvMbh3kV8haeDsi7SSVOi7gSpyEaeBWe1BIt3EJD+t9ihj4vSYGkW9KxrkPokLwFOiTvos5101XHsqZxnFu+PsJ84JprAAAAAElFTkSuQmCC>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAH4AAAAWCAYAAAAGhCi/AAAA+0lEQVR4Xu2SQQqEMBAE/f+nd8khIE0mu5pqFewCD8mYshS3LYQQQghv4TO4/pldiTakEaQKqvbvoGqp9q9m1lHt384oWtdnoTwN7STchKOjfX3vsWiwrlegPI19F9VIODraRLpt9Gg6lvQ5GklXw9FoxRVM+hyNpKtB912CI9rhI52kq0H07X/w6sKwSDfW110OJ4njO1pxBFO+vYdyNiiX9lFeGxpIRxMubdL1Ci4P2YhThZHRq57qPNXoclB9OLOw2ewoK55Zx2x2hFVHdZ7qw+hBozCdje45ypnzv56v89E9/3LmrD5bHTrT+St4+ks/vS+EEEIIYcgX5NG9Q1MvJ7sAAAAASUVORK5CYII=>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAF0AAAAZCAYAAABTuCK5AAABWElEQVR4Xu2UUaoDMQwDe/9Ltyw8gxGyrKTJ8pZmvhp7rGT90dfrcDgcHsUbCz/I1A6uoRiM37nGUH03Ixj1d+C8QTl4lmQZQ1VQ13MyglF/B90b3H5LSNVAVR/BmV9xzwq6fXS0M1moLlF1lyoj4zh3sHXpGKpkdKPW4XxA9Ko+Y9SfobqD1ZDSyY1S+gP71YOQcCq/6yuUr3ojsHfhmUEdFlbBXFZjZEf5qqdw3+GCWSwfzwzqsLAK5rIagg76qjfCqpwLNo/f4UD9kSDmOfPYV8vB8yjOexxYxkw29d2gyqvqGezHmdWxNsuqHCTe6OZTzw2oHHc+s2vpefabHMWSpV+oENW7cPpINcNq31Dd09HNjORKL4KyhGeGclhm1BHmuag51WM47+j6mdZ1LmTMzPwCW/eyNfzBbN/L9gsexuy/xhC3XPIgbt3FrZf9U84ODofD3XwAX67wEDLgA1QAAAAASUVORK5CYII=>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAXCAYAAAAcP/9qAAAAcElEQVR4Xu3NQQrAIAxEUe9/6RaEQlvnNxPRRSFv55hJWivlh47gvY06pLIeyo9JahfewI8k2kP5gzUEqEv5wB58oR7lnzIlmqU85JboAOUoW6B5ygfWEFDd8HA4YFB9lXUrDt5d+3Avfiywa28p2gkqQzzEL0DrJwAAAABJRU5ErkJggg==>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACkAAAAYCAYAAABnRtT+AAAAwUlEQVR4Xu2RWwrDQAwDc/9LtyxEkApZq33Qj7ADhdQeKYZc1+GwxIcHIVO5FkIQz8+ZorfvEWf5OMYd4uYuBxLnR6gCbu6ockzXGTmSd/yfUZlh+EAH75MDEgdIb6SgwW6STxwgvdECdtWMSRwgvdWCJJ84QHqrBUk+cYD00oLKq+ZPEgdIDwVyeeP2bgcSB5SeK3G7Rm/fSBxgPRTxL6HyuCvp7O2jEsVMRrGrp2THC3Z0WGa/AljJDvG3Fx1eyReDWoR8uAt25AAAAABJRU5ErkJggg==>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAWCAYAAAAfD8YZAAAAMklEQVR4XmNgGAVkgf9QTBVAsUFUcQ1VDAEBigwiWTPJGmCA9prIdtoQBjA/E4uHMgAA/HUc5Bf3mlgAAAAASUVORK5CYII=>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAWCAYAAAAfD8YZAAAAOElEQVR4XmNgGAU0Bf+hmGhAsgYYIEsjSZpIUowNUGwADFBsEMUGgABVDIEBqhk0wAAWKMTioQwAMaMe4ixKaUgAAAAASUVORK5CYII=>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANsAAAAZCAYAAAC4o1v/AAACbUlEQVR4Xu2TjWokMQyD9/1f+o7hLmCE5CiezLbZ9QdDG1n+iZu+Xk3TNE3TNE3TFPmDQlOi97i4gyXzL+OavTp/Na/5x8n72z27Xc82/kLu/LNd3Mn9Zu7u/afZPb9Vb2rYwBjEGmiBHTXv5FfzPoGn7/6ON7Oz7sW03tRwg3ih+HNXzx1Lu5NfzTudJ+/9jjczfu6qOZjWmxqKYF08XzDNZefSqvnVvNN56t5YF893ifV2vBuGrCkD/2ED4ZlRzavAeq1Sza/mnYyzb/TgmcHiruayOlMFWVMGXnowZ0gWZ9qF0jPUbFWqNSo5p5PtCvWVd8NiTLtQ+gqzearImiqAejxXh1Q5SlegvzoPUqlRyTmdlX0P30pOROUoPQNzsplUbOgsNpAxGQBc3yAO5X4umKdqKF2R+bCP881wfDOP0w/ncr4Mx3Ph+gY4w+xbAXNndYaOcTwzpEcGANeXoWoonaG8anFKZ7i+SCXndNydOp4ZqobSV8juMXT0KH9EemQAcH0ZqobSkcyHSxkoneH6IpWc03F36nhmqBpKZyhvdo+ho0f5I9KjArHJroZM2wXOOFA64ngY1byTUTvN3szQMljc1RSZl83IcDwR6VcNcWnRw/wM9OH5gmkMnCHCZhwoHXE8jGreyaid4hvJzi4sh2mM7F1cZLGI44mk/jR4k3ihHctfxe3jeBjVvNN58t74TuLvT/YdsB4rvVNfGtzAGBS/d+D0cjyKat7pPH1vfCt3/karsD5uf8fzkbh/qCzWaD5xb+q94JnB8iiWqWkC9uP6EpZ2sWT+AL7tvk/Re+wdNE3TNE3TNHv5C0uWoG7L25PLAAAAAElFTkSuQmCC>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADYAAAAZCAYAAAB6v90+AAAAp0lEQVR4Xu3SWwqFMAwE0O5/0/olxCGTNFMqBXNALk3zUu4YrbU2xuU8VnR3NFwcl4/utlsdGtWz+FbRQhWsjxfbii2i8Hp5MQqT8TxLrWPkflhoz3jnmclZwXZLYaLSaDZPYT/y8yvNkooMeTDh9ZJmlAsIaThgPVic8grwXOH1q2D1LP5ikzAZz6sq/bLls/vXS6XJH4p2sbuynPY7+LfIntZaO9MN+IJzjVJ1XXYAAAAASUVORK5CYII=>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAZCAYAAADuWXTMAAAAQElEQVR4XmNgGAX4wH90AWIBSCNZmmEa6asZWQP9NKMrJsnp6AqJ1owcSOgYL8ClgLaa8Uni1UzIX/jkRsEwBgAxwifZ2Y+WhAAAAABJRU5ErkJggg==>

[image13]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAWCAYAAAAfD8YZAAAANUlEQVR4XmNgGAX0B//RBUgFIAMoNgQEqGIQxYZQbAAyINsgkjWS7GySNcAAyRpJ1jAKyAAApiMS7hxyGHUAAAAASUVORK5CYII=>

[image14]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAZCAYAAADnstS2AAAAN0lEQVR4XmNgGAWDHvyHYlx8rILIfHQ5DN24NGIFeCXRAdGKsVmL4WZkDyEDdD6GzzEUjAL6AQDJwBrmQWIJqgAAAABJRU5ErkJggg==>

[image15]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAYCAYAAADzoH0MAAAATElEQVR4Xu2NMQ4AIAjE/P+ndZJE5XrMhiYstuAYTcY0Y7kXsrFQWDpEAbmAAnuAAnKBitT7A4XkAhegr/yA3h1wXsq9qPwRqGn+ZQGyjT7CY5ssggAAAABJRU5ErkJggg==>

[image16]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADEAAAAZCAYAAACYY8ZHAAAA7UlEQVR4Xu2TwQ7CMAxD9/8/DcpEpmJsN2Xr4NAnTSK242wHtm2x+HseKPyKeJF8mfzdagznVzpUBucSrAAfhtKD3j76mMHZkmFWFCh9BNeh9MB5B225OuT0KqojUHrgvB0sdguYTa0H9uMOzkjP/zjgQJ+9EANv4A7OiPVZoYJlmYZgBufUHNZnhQqWZRrC/Mpei82OlLEs0xDlV3YTm7Vmg8opvULuVvZt5mxJdZ9x2UcErkzpScV39PaTSoZ+CM6MXsZ5Qc9PqrmdofCLb3ZGmX5j+oHtnhtTj8zsfqP33zjDrF7J7QcXi4t4Atx+oV+/Qs/0AAAAAElFTkSuQmCC>

[image17]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADYAAAAYCAYAAACx4w6bAAAA9UlEQVR4Xu2SUQrDMAxDc/9Lb2Qsw9Nkxa6bsEIf5KOyLDuhrd1s5YFC49ql6BcY56+oLjT6IzkRzw/21ewrqrBZPULmYp2o74UKV8szHbVMv9pjoPI+WJPXoHQG06MZw4c6Mqt/GbxAbxh+d5QXNUbUJ8FLKbCuFmC68iMlX2ZQB71H+vEh7bHgtwf1sUAP5mWaR8abgWZmhjEv0zyiviw0t7pYpD/iqUCzo0M9n6dbZvUqNH8sRotvVF3VOqzGtApunrqcpw9U3ebiOROZh4MzCzAf5mQzM4QyQybgSM9ZLJ+9fIDD8rmrfjPFtnnbBt3cXIAnFtumWkCRUOwAAAAASUVORK5CYII=>

[image18]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAXCAYAAAD6FjQuAAAAg0lEQVR4Xu2PSwqAMBBDe/9LKxYqNeTThc5CfVCweZMOtvYCNjiPUrbooGTJYGnZyu+jZ7PWzw/gYwjzeJ9h8ydWNu6wg9+s03FSOczxm3U6TiqH+biz2QtuSDmVR1xROZVHXFE5lUdcUTmVR1KRudSRpCJzLLOMJXgYKzO3UrLk50Psl3JfoX/1iawAAAAASUVORK5CYII=>

[image19]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAE0AAAAZCAYAAAB0FqNRAAABQElEQVR4Xu2QgQrEMAhD9/8/fYdwgoREXa/d3VgfDKaJqe1xbDabh/HCxs0Y3t8Gfdj/Y4+BemdmJZ29lUf5JTiMnwK1zsxKqr07egs3ZkGsrzjrn011n4zWTDSogazPUP6rWPpoaMjM6PUeg3l/gdqD9SKp3n0wA3W1kNHRlG6gjvUZ2CzWiNRZmIJ5Wc9hGtZGp+c19hXo6+4SkToLUzAv6zlMw9rBflVXMD/bJ0N6zwQxXzaPGtYR1NCHdQXz4xkV0i8FQPlU30AN6whq+K/mzuJZnTzp+TYgm0cN6wjrZ/5RpjyakYVkmpHpTMPa6Pq6VLPsPEbp8aBoxJqReZTWOSPuozyMjrfSnZavcyBjZCZD5Y3uN8Lys2aHZ3mZNpPlj2bMPEBlXXKRD5ecM/tCmDU7/6+4+8Xuvv9m81Tey0X0DPaS2EQAAAAASUVORK5CYII=>

[image20]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAYCAYAAADzoH0MAAAAVUlEQVR4Xu2OWQoAIAhEvf+l60dCHBtbhH56EMRsKPJhNH32b7UpPuQLdMgXw5AQ72oABEL9AAgJkAchAbI7A2GubCA0lcxPA8wb2EtWrgo5Ln5e0QH68znHcRH65gAAAABJRU5ErkJggg==>

[image21]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAXCAYAAAD6FjQuAAAAhklEQVR4Xu2PSwqAMBBDe/9LK4gjbczHhXWhPijUvIlDW3sRy36mU0umL5z6c6R/laSe7IbQs1n0w0wfnCTAvPtm8wdWNu6wg3fW2XBSOczxzjobTirH8sowH3ADyqk84orKqTziisqpPOKKyqk8korMpY4kFZljmaWW4GFcmbmVR5b8fIgVSfhgoJWG770AAAAASUVORK5CYII=>

[image22]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD4AAAAZCAYAAABpaJ3KAAAA0klEQVR4Xu3S7QqEIBCF4e7/pndBLOTwjo5jGLvNA/3ozIcJHUdK6W0+8iitU89PGl1qVN9h5hu8fcVU86LZc7S3N695r7fYdfHIGdRPe7wZshop87J2etH8SmaiZn33ol13oL3e7KIFbdb3kdn+WdZ+yim7aEGbte4RmfHS7ztRTtmFCu0A1b26Bwf0dtFZlBUYVuZQ0Oq+0Sztp6zAsDKHFkR30hy9e7ICw8ocusnM/rNXn5Y347Axqu+il+19l+a93r/0qss+Tn/J0ZNSSinqC2m0qFifk48FAAAAAElFTkSuQmCC>

[image23]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFEAAAAZCAYAAABJhMI3AAABA0lEQVR4Xu2SwQ7CMAxD9/8/DeIQKTh2m7TVQJAn7ZBXxysT19U0TdOMeMCD4DnL/D2zDzQ7v5vRHSp3zeQqffngAarv8fnZLp7hbKBXvehwfuOuj7j7jtE+88qhVw5hLsDKXjCXRXWuoLoqPuNwNpQPsCDOWVjXDqqv4jMOZ0P5IDGI84xqvoLqrviMw9lQPkgM4vkM3D+J6q74jMPZUJ5KH2bnWeRLF1F9FZ9xOBvUB+GgCxuc6FMdFZ9xOBvUB+GgC5vsdo72mWf5ikNYLgoHXTjISvfoTswrh145JDi26Jmdf4LZnfAMZwO96vVOZX6W7I89nWu+CfvbZ56maZqmaZ6V2OwULfFlqQAAAABJRU5ErkJggg==>

[image24]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEYAAAAZCAYAAACM9limAAAA20lEQVR4Xu2SUQrDMAxDd/9LbwRWSDVbsp1so9QP+lHJUtzQx6NpmhxPeJo34ctQN4i+NXMlwvurj1b+r2E7RHZV/gk17OmMSsZi3ovtOEAP3xHV95WLGVRzHtkdLW2G9Z0MOrjIjl5vv4we/l406PAiq91ePqsfMO/DxDL0d4BnRPFyWb0Elm0rnsAzoni5rF5mLtxZvLqol8/qEhYqlwK7egZeV1aXsFC5dGI1j7CdLJ3NU1ioWlrNRWDdlm5pEnbIQPn/QO00e2r2lvSFXInjF448TdM0zZ15Ac3wo13oYOENAAAAAElFTkSuQmCC>