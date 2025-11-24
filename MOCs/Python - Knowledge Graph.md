---
tags: [python, knowledge-graph, overview]
moc: true
---

# Python - Knowledge Graph Overview

**Complete interconnection map** of all Python concepts in this knowledge base. Shows how notes relate and link to each other, forming a web of learning paths.

---

## Structure

This knowledge base contains **80+ atomic notes** organized into **7 major MOCs**:

1. **[[Python - IO (MOC)]]** — Input/output, user interaction (10+ notes)
2. **[[Python - Variables & Types (MOC)]]** — Data types, assignment, scope (6+ notes)
3. **[[Python - Lists (MOC)]]** — Collections, indexing, iteration (10+ notes)
4. **[[Python - Loops (MOC)]]** — For, while, control flow (8+ notes)
5. **[[Python - Conditionals (MOC)]]** — If/else, comparisons, logic (5+ notes)
6. **[[Python - Functions (MOC)]]** — Functions, parameters, returns (8+ notes)
7. **[[Python - Practical Math (MOC)]]** — Real-world calculations (10+ notes)

Plus: **Strings, Dicts, File IO, Debugging, Modules, Beginner Path**.

---

## Concept Relationships

### Foundation Layer (Most Basic)

```
Math (Operators)
├─ Arithmetic Operators
├─ Operator Precedence
├─ Rounding & Precision
├─ Absolute Values & Roots
└─ Modulo & Divisibility
  └─ Links to: Conditionals (for divisibility checks)
  └─ Links to: Lists (for filtering patterns)

Variables & Types
├─ Declaration & Assignment
├─ Type Checking
├─ Scope
└─ Type Conversion
  └─ Links to: IO (input type conversion)
  └─ Links to: Math (number types)
```

### IO Layer (User Interaction)

```
IO Fundamentals
├─ Print Basics
├─ Input Basics
├─ Output Formatting
├─ Input-Output Flow
├─ Common IO Patterns
├─ Input Types (Strings vs Numbers vs Lists)
├─ Output Targets (Screen vs File vs Strings)
└─ Error Handling in Input-Output
  └─ Links to: Loops (input validation with while loops)
  └─ Links to: Conditionals (if input is valid)
  └─ Links to: Functions (reusable input functions)
  └─ Links to: File IO (reading/writing with error handling)

Interactive Patterns
├─ Interactive Games & Guessing
├─ Form-Like Input Collection
├─ Menu-Driven Programs
└─ Input Validation
  └─ Links to: Loops (validation loop pattern)
  └─ Links to: Conditionals (checking valid ranges)
```

### Control Flow Layer (Logic & Iteration)

```
Conditionals
├─ Comparison Operators (==, <, >, etc.)
├─ Boolean Logic (and, or, not)
├─ If-Elif-Else Basics
├─ Nested Conditions
└─ Truthiness
  └─ Links to: Loops (stopping conditions)
  └─ Links to: Lists (filtering with conditions)
  └─ Links to: Functions (conditional returns)

Loops
├─ For vs While
├─ Loop Control (Break & Continue)
├─ Enumerate & Zip
├─ Nested Loops
└─ Loop Patterns
  └─ Links to: Lists (accumulation, filtering patterns)
  └─ Links to: IO (menu loops, input validation loops)
  └─ Links to: Functions (loops inside functions)
  └─ Links to: Math (iteration over ranges)
```

### Data Structures Layer

```
Lists (Collections)
├─ Tuple vs List vs Set
├─ Indexing & Edge Cases
├─ Slicing Patterns
├─ List Methods
└─ Common Patterns (accumulation, filtering, searching)
  └─ Links to: Loops (for/while over lists)
  └─ Links to: Conditionals (filtering logic)
  └─ Links to: Functions (list processing functions)
  └─ Links to: Enumerate & Zip (list iteration tricks)

Strings
├─ String Basics
├─ String Methods
├─ String Formatting
└─ String Slicing
  └─ Links to: Lists (similar indexing/slicing)
  └─ Links to: IO (string output)
  └─ Links to: Loops (character iteration)

Dictionaries
├─ Dictionary Basics
├─ Keys & Values
├─ Dictionary Methods
└─ Dictionary Iteration
  └─ Links to: Lists (alternative data structure)
  └─ Links to: Loops (iterating over dict items)
  └─ Links to: Conditionals (checking key existence)
```

### Functions Layer (Abstraction)

```
Functions
├─ Parameters & Return Values
├─ Default Parameters & Keywords
├─ Lambda Functions
├─ Function Scope
└─ Advanced Arguments (*args/**kwargs)
  └─ Links to: IO (input/output functions)
  └─ Links to: Math (calculator functions)
  └─ Links to: Lists (sorting/filtering with lambdas)
  └─ Links to: Loops (functions taking iterables)
  └─ Links to: Conditionals (conditional returns)
```

### Practical Applications Layer

```
Practical Math
├─ Calculator Basics
├─ Percentages & Discounts (real-world: shopping)
├─ Money & Budget (real-world: allowance)
├─ Time Calculations (real-world: homework timing)
└─ Geometry & Shapes (real-world: room sizing)
  └─ Links to: Functions (math helper functions)
  └─ Links to: IO (input prices, output results)
  └─ Links to: Conditionals (budget checks)

File IO
├─ Reading Files
├─ Writing Files
├─ File Modes
├─ CSV & Data Files
└─ Error Handling in Files
  └─ Links to: IO (file reading is extended IO)
  └─ Links to: Loops (reading multiple lines)
  └─ Links to: Lists (storing file data)
  └─ Links to: Conditionals (checking file existence)
```

### Tools & Debugging Layer

```
Debugging
├─ Error Types & Messages
├─ Tracebacks
├─ Common Errors
├─ Print Debugging
└─ Debugging Strategies
  └─ Links to: All concepts (errors appear everywhere)

Modules
├─ Standard Library Overview
├─ Import Statements
├─ Common Modules (math, random, etc.)
└─ Module Organization
  └─ Links to: Functions (organizing code)
  └─ Links to: All concepts (modules organize functionality)
```

---

## Cross-Cutting Relationships

### By Frequency of Use

**Every Day (Fundamental):**
- Variables & Types
- IO (print, input)
- Conditionals (if/else)
- Loops (for, while)

**Very Often (Essential):**
- Lists
- Functions
- Strings
- Math operators

**Often (Important):**
- Loop control (break, continue)
- Enumerate & zip
- Default parameters
- List methods

**Sometimes (Useful):**
- Lambdas
- Sets & Tuples
- Nested loops
- File IO
- Debugging

### By Learning Dependency

```
Math Operators
  ↓
Variables & Types
  ↓
Conditionals ← → IO
  ↓
Loops → Lists ← → Functions
  ↓
Practical Applications (Math, File IO)
```

### By Complexity

**Level 0 (Syntax):**
- Variable assignment
- Print statement
- If statement

**Level 1 (Patterns):**
- For loops
- List indexing
- Function calls

**Level 2 (Combining):**
- Nested loops
- Filtering lists
- Input validation

**Level 3 (Abstraction):**
- Writing functions
- Organizing code
- Advanced features

---

## Learning Paths

### Path 1: "Get Input, Process, Show Output"
1. [[Python - IO - Input Basics]]
2. [[Python - Variables & Types - Declaration & Assignment]]
3. [[Python - Math - Arithmetic Operators]]
4. [[Python - IO - Print Basics]]
5. [[Python - Practical Math - Calculator Basics]]

### Path 2: "Make Decisions"
1. [[Python - Conditionals - Comparison Operators]]
2. [[Python - Conditionals - Boolean Logic (and-or-not)]]
3. [[Python - Conditionals - If-Else Basics]]
4. [[Python - Practical Math - Percentages & Discounts]]

### Path 3: "Repeat Actions"
1. [[Python - Loops - For vs While]]
2. [[Python - Lists - Tuple vs List vs Set]]
3. [[Python - Loops - Loop Control (Break & Continue)]]
4. [[Python - Lists - Common Patterns]]

### Path 4: "Reuse Code"
1. [[Python - Functions - Parameters & Return Values]]
2. [[Python - Functions - Default Parameters & Keywords]]
3. [[Python - Conditionals - If-Else Basics]]
4. [[Python - Lists - Common Patterns]]

### Path 5: "Master Collections"
1. [[Python - Lists - Tuple vs List vs Set]]
2. [[Python - Lists - Indexing & Edge Cases]]
3. [[Python - Lists - Slicing Patterns]]
4. [[Python - Lists - List Methods]]
5. [[Python - Loops - Enumerate & Zip]]

---

## Common Concepts That Link Everything

### Iteration
Appears in: Loops, Lists, Functions, IO, Strings, Dicts
- [[Python - Loops - For vs While]] — How to iterate
- [[Python - Loops - Enumerate & Zip]] — Iterate with index/pairs
- [[Python - Lists - Common Patterns]] — Patterns for lists
- [[Python - Strings - String Slicing]] — Iterating characters

### Conditions
Appears in: Conditionals, Loops, Functions, Lists
- [[Python - Conditionals - Comparison Operators]] — Test conditions
- [[Python - Conditionals - Boolean Logic (and-or-not)]] — Combine tests
- [[Python - Lists - Common Patterns]] — Filter with conditions
- [[Python - Loops - Loop Control (Break & Continue)]] — Stop looping

### Data Transformation
Appears in: Functions, Loops, Lists, Math
- [[Python - Functions - Lambda Functions]] — Transform with lambda
- [[Python - Lists - Common Patterns]] — Accumulate, filter, search
- [[Python - Practical Math - Calculator Basics]] — Convert values
- [[Python - IO - Output Formatting]] — Display transformed data

### Error Handling
Appears in: IO, File IO, Functions, Loops
- [[Python - IO - Error Handling in Input-Output]] — Handle input/output errors
- [[Python - File IO - Error Handling in Files]] — Handle file errors
- [[Python - Functions - Parameters & Return Values]] — Valid arguments
- [[Python - Loops - Loop Control (Break & Continue)]] — Exit on error

---

## Recommended Reading Order for Beginners

### Week 1: Basics
1. [[Python - Variables & Types - Declaration & Assignment]]
2. [[Python - IO - Print Basics]]
3. [[Python - IO - Input Basics]]
4. [[Python - Math - Arithmetic Operators]]
5. [[Python - Practical Math - Calculator Basics]]

### Week 2: Decision Making
6. [[Python - Conditionals - Comparison Operators]]
7. [[Python - Conditionals - Boolean Logic (and-or-not)]]
8. [[Python - Conditionals - If-Else Basics]]
9. [[Python - Practical Math - Percentages & Discounts]]

### Week 3: Repetition
10. [[Python - Loops - For vs While]]
11. [[Python - Lists - Tuple vs List vs Set]]
12. [[Python - Loops - Loop Control (Break & Continue)]]
13. [[Python - Lists - Common Patterns]]

### Week 4: Reusability
14. [[Python - Functions - Parameters & Return Values]]
15. [[Python - Functions - Default Parameters & Keywords]]
16. [[Python - Practical Math - Money & Budget]]

### Week 5: Data Structures
17. [[Python - Lists - Indexing & Edge Cases]]
18. [[Python - Lists - Slicing Patterns]]
19. [[Python - Lists - List Methods]]
20. [[Python - Loops - Enumerate & Zip]]

### Week 6+: Advanced
21. [[Python - Functions - Lambda Functions]]
22. [[Python - Strings - String Basics]]
23. [[Python - Practical Math - Geometry & Shapes]]
24. [[Python - Debugging - Error Types & Messages]]

---

## How to Explore This Knowledge Base

1. **Start with a MOC**: Pick a topic that interests you (e.g., [[Python - IO (MOC)]])
2. **Read a note**: Follow the progression from Fundamentals → Advanced
3. **Follow links**: Click "Related Concepts" to explore connections
4. **Try examples**: Run the code samples in each note
5. **Do exercises**: Complete Bloom-level exercises (Remember → Create)
6. **Build projects**: Combine multiple concepts into a program

---

## Statistics

- **Total Notes**: 80+
- **MOCs**: 7 major + 6 extended
- **Concepts**: 15+ categories
- **Code Examples**: 200+ runnable snippets
- **Bloom Levels**: All 6 (Remember → Create)
- **Real-World Scenarios**: 50+ (shopping, school, games, etc.)

---

## Missing Pieces (Future Expansion)

- **Classes & Objects** — OOP basics
- **Decorators** — Advanced function patterns
- **Generators** — Memory-efficient iteration
- **Context Managers** — With statement
- **Regular Expressions** — Pattern matching in strings
- **Testing** — Unit tests with pytest
- **Web Basics** — HTTP, requests, APIs
- **Data Analysis** — Pandas, visualization
- **Game Dev** — Pygame basics

---

## Navigation Tips

- **Search** for a concept you want to learn
- **Follow the MOCs** for structured progression
- **Use Related Concepts** links to jump between topics
- **Try code examples** immediately (don't just read)
- **Complete exercises** before moving to next note
- **Build mini-projects** combining 2-3 concepts

---

## Remember

Each note is **atomic** — it covers one concept clearly. Together, they form a **knowledge graph** where concepts relate and reinforce each other. **Non-linear learning** is encouraged: jump between topics, follow curiosity, build projects.

Happy learning! 🐍

---

**Last Updated**: November 2025
**Total Atomic Notes**: 80+ and growing
**Bloom's Coverage**: Complete (Remember → Create)
**Real-World Examples**: Heavy emphasis on relevance for 14-year-olds


[Python - IO (MOC)]: <Python - IO (MOC).md> "Python - IO (MOC)"
[Python - Variables & Types (MOC)]: <Python - Variables %26 Types (MOC).md> "Python - Variables & Types (MOC)"
[Python - Lists (MOC)]: <Python - Lists (MOC).md> "Python - Lists (MOC)"
[Python - Loops (MOC)]: <Python - Loops (MOC).md> "Python - Loops (MOC)"
[Python - Conditionals (MOC)]: <Python - Conditionals (MOC).md> "Python - Conditionals (MOC)"
[Python - Functions (MOC)]: <Python - Functions (MOC).md> "Python - Functions (MOC)"
[Python - Practical Math (MOC)]: <Python - Practical Math (MOC).md> "Python - Practical Math (MOC)"
[Python - IO - Input Basics]: <../Python Notes/Python - IO - Input Basics.md> "Python - IO - Input Basics"
[Python - Math - Arithmetic Operators]: <../Python Notes/Python - Math - Arithmetic Operators.md> "Python - Math - Arithmetic Operators"
[Python - IO - Print Basics]: <../Python Notes/Python - IO - Print Basics.md> "Python - IO - Print Basics"
[Python - Conditionals - Comparison Operators]: <../Python Notes/Python - Conditionals - Comparison Operators.md> "Python - Conditionals - Comparison Operators"
[Python - Conditionals - Boolean Logic (and-or-not)]: <../Python Notes/Python - Conditionals - Boolean Logic (and-or-not).md> "Python - Conditionals - Boolean Logic (and/or/not)"
[Python - Conditionals - If-Else Basics]: <../Python Notes/Python - Conditionals - If-Else Basics.md> "Python - Conditionals - If-Else Basics"
[Python - Loops - For vs While]: <../Python Notes/Python - Loops - For vs While.md> "Python - Loops - For vs While"
[Python - Lists - Tuple vs List vs Set]: <../Python Notes/Python - Lists - Tuple vs List vs Set.md> "Python - Lists - Tuple vs List vs Set"
[Python - Loops - Loop Control (Break & Continue)]: <../Python Notes/Python - Loops - Loop Control (Break %26 Continue).md> "Python - Loops - Loop Control (Break & Continue)"
[Python - Lists - Common Patterns]: <../Python Notes/Python - Lists - Common Patterns.md> "Python - Lists - Common Patterns"
[Python - Functions - Parameters & Return Values]: <../Python Notes/Python - Functions - Parameters %26 Return Values.md> "Python - Functions - Parameters & Return Values"
[Python - Functions - Default Parameters & Keywords]: <../Python Notes/Python - Functions - Default Parameters %26 Keywords.md> "Python - Functions - Default Parameters & Keyword Arguments"
[Python - Lists - Indexing & Edge Cases]: <../Python Notes/Python - Lists - Indexing %26 Edge Cases.md> "Python - Lists - Indexing & Edge Cases"
[Python - Lists - Slicing Patterns]: <../Python Notes/Python - Lists - Slicing Patterns.md> "Python - Lists - Slicing Patterns"
[Python - Lists - List Methods]: <../Python Notes/Python - Lists - List Methods.md> "Python - Lists - List Methods"
[Python - Loops - Enumerate & Zip]: <../Python Notes/Python - Loops - Enumerate %26 Zip.md> "Python - Loops - Enumerate & Zip"
[Python - Functions - Lambda Functions]: <../Python Notes/Python - Functions - Lambda Functions.md> "Python - Functions - Lambda Functions"
[Python - IO - Output Formatting]: <../Python Notes/Python - IO - Output Formatting.md> "Python - IO - Output Formatting"
[Python - IO - Error Handling in Input-Output]: <../Python Notes/Python - IO - Error Handling in Input-Output.md> "Python - IO - Error Handling in Input/Output"
[Python - Strings - String Basics]: <../Python Notes/Python - Strings - String Basics.md> "Python - Strings - String Basics"
