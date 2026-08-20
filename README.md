# ♾️ WordMatrix

### The Infinite Wordlist Generator

> **Generate. Combine. Expand.**

**WordMatrix** is a lightweight and customizable Wordlist Generator designed to create large sets of combinations from **words, numbers, dates, and symbols** provided by the user.

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/0xQuantum9/WordMatrix
cd WordMatrix
```

Run the generator:

```bash
python WordMatrix.py
```

WordMatrix uses only Python's standard library, so no external dependencies are required.

---

## 🖥️ Usage

Start WordMatrix:

```bash
python WordMatrix.py
```

The program will interactively ask you for different types of input.

### 1. Enter Words

```text
[+] Enter words
    1> adam
    2> WordMatrix
    3>
```

Press **Enter on an empty line** when you are finished.

### 2. Enter Numbers

```text
[+] Enter numbers
    1> 2
    2> 20
    3>
```

### 3. Enter Symbols

```text
[+] Enter symbols
    1> @
    2> #
    3> !
    4>
```

### 4. Set Maximum Depth

```text
Enter max depth [Default: 3]:
```

If you simply press **Enter**, WordMatrix uses a default depth of `3`.


Words are first expanded into multiple case variations.

WordMatrix then builds a generation pool from:

* Expanded words
* Numbers
* Dates
* Symbols
* Individual digits extracted from numeric inputs

The combination engine generates results according to the selected maximum depth.

---

## 🎚️ Generation Depth

The depth controls the maximum number of pool elements used in each generated combination.

For example:

```text
Depth 1
Depth 2
Depth 3
Depth 4
```

Increasing the depth can increase the number of generated combinations **extremely quickly**.

> ⚠️ Higher depths can produce very large output files and may require significant processing time and disk space.


## 🎯 Use Cases

WordMatrix can be useful for legitimate purposes such as:

* 🧪 Custom dictionary testing
* 🔬 Research and experimentation
* 🧰 Test-data generation
* 🧩 Combinatorial testing
* 📚 Custom word collection generation
* 🤖 Automation workflows

> **Use WordMatrix only with systems, accounts, and data that you own or have explicit permission to test.**


**Generate • Combine • Expand**

</div>
