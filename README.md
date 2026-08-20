# ♾️ Eternyx

### The Infinite Wordlist Generator

> **Generate. Combine. Expand.**

**Eternyx** is a lightweight and customizable Wordlist Generator designed to create large sets of combinations from **words, numbers, dates, and symbols** provided by the user.

## ✨ Features

* ♾️ **Combination Generation**

  * Generate a large number of combinations from your custom inputs.

* 🔤 **Smart Case Expansion**

  * Automatically generate multiple case variations:

    ```text
    adam
    Adam
    ADAM
    aDaM
    ```

* 🔢 **Numbers & Dates**

  * Add custom numbers and dates to the generation pool.

* 🔣 **Custom Symbols**

  * Include symbols such as:

    ```text
    @  #  !  $  %
    ```

* 🎚️ **Custom Generation Depth**

  * Control the maximum combination depth.

* 📄 **Automatic Output**

  * Results are automatically saved to:

    ```text
    output.txt
    ```

* ⚡ **Memory-Efficient Writing**

  * Generated results are written directly to the output file instead of keeping the entire list in memory.

* 📊 **Live Progress**

  * Displays generation progress while Eternyx is running.

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/0xQuantum9/Eternyx
cd eternyx
```

Run the generator:

```bash
python Eternyx.py
```

Eternyx uses only Python's standard library, so no external dependencies are required.

---

## 🖥️ Usage

Start Eternyx:

```bash
python Eternyx.py
```

The program will interactively ask you for different types of input.

### 1. Enter Words

```text
[+] Enter words
    1> adam
    2> eternyx
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

### 3. Enter Dates

```text
[+] Enter dates
    1> 1995
    2> 2026
    3>
```

### 4. Enter Symbols

```text
[+] Enter symbols
    1> @
    2> #
    3> !
    4>
```

### 5. Set Maximum Depth

```text
Enter max depth [Default: 3]:
```

If you simply press **Enter**, Eternyx uses a default depth of `3`.


Words are first expanded into multiple case variations.

Eternyx then builds a generation pool from:

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

Eternyx can be useful for legitimate purposes such as:

* 🧪 Custom dictionary testing
* 🔬 Research and experimentation
* 🧰 Test-data generation
* 🧩 Combinatorial testing
* 📚 Custom word collection generation
* 🤖 Automation workflows

> **Use Eternyx only with systems, accounts, and data that you own or have explicit permission to test.**


**Generate • Combine • Expand**

</div>
