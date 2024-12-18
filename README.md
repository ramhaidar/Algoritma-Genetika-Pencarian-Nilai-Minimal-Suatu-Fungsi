# Genetic Algorithm for Function Minimization 🧬

A Python implementation of Genetic Algorithm to find the minimum value of a complex mathematical function.

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Mathematical Function](#mathematical-function)
4. [Installation](#installation)
5. [Implementation Details](#implementation-details)
6. [Usage](#usage)
7. [License](#license)

---

## Overview

This project implements a Genetic Algorithm (GA) to find the x and y values that minimize the given mathematical function. It was developed as part of the Introduction to Artificial Intelligence course at Telkom University.

## Features

-   🧬 Genetic Algorithm implementation
-   📊 Population-based optimization
-   🔄 Generational replacement model
-   📈 Fitness evaluation
-   🎯 Elitism selection
-   ⚡ Efficient binary encoding/decoding

## Mathematical Function

The algorithm minimizes the following function:

![Function](/Function.png)

where x and y are bounded within the interval [-5, 5].

## Installation

1. Ensure you have Python 3.6 or higher installed
2. Clone the repository:

```bash
git clone https://github.com/filzarahma/Algoritma-Genetika-Pencarian-Nilai-Minimal-Suatu-Fungsi.git
```

3. No additional dependencies required (uses only standard Python libraries)

## Implementation Details

The genetic algorithm implementation includes:

-   Binary chromosome representation
-   Population size: 10 chromosomes
-   Number of generations: 10
-   Crossover probability: 0.8
-   Mutation probability: 0.01
-   Roulette wheel selection
-   Single-point crossover
-   Binary mutation
-   Elitism selection

## Usage

Run the program using:

```bash
python code.py
```

The program will display:

-   Population details for each generation
-   Best chromosome in each generation
-   Final optimal solution with:
    -   Best chromosome representation
    -   Corresponding x and y values
    -   Minimum function value achieved

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors

-   Filza Rahma Muflihah
-   Ummu Husnul Khatimah

---

_This project was developed for the Introduction to Artificial Intelligence course at Telkom University._
