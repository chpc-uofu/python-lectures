<img src="images/py.svg"
     alt="Lettermark to symbolize Python"
     role="img"
     width="100" />

# Hands-on Introduction to Python from the University of Utah Center for High Performance Computing

This repository contains the Jupyter Notebooks and related files for the University of Utah Center for High Performance Computing's Python course. This is an introduction to the Python language for beginners, written by Brett Milash, Wim Cardoen, and Robben Migacz. We give a tour of the Python language's features and syntax, and of the structure of Python scripts and snippets. This isn't an introduction to computer science or software development, for which you may need to refer to other materials; however, we've designed the course to be approachable for students, researchers, and professionals who are new to software development.

## Contents

[notebooks/lectures](notebooks/lectures) contains lecture notes, exercises, and collapsed supplemental material and solutions.

### Notebook guide

- `00_introduction` introduces the course
- `01_types_literals_variables` through `04_lists` cover values, variables, operators, strings, and lists
- `05_functions` through `10_modules` cover functions, lambda expressions, flow control, file input and output, looping, and modules
- `11_sets` through `14_exceptions` cover sets, tuples, dictionaries, and exception handling
- `15_classes` and `16_inheritance` introduce object-oriented programming
- `17_conclusion` collects next steps, programming advice, and further resources

Throughout, we have added exercises alongside their related lessons. We include solutions and supplementary materials within the relevant notebooks.

### NumPy and SciPy content

As of Summer 2024, the [NumPy and SciPy content has been separated into its own repository](https://github.com/chpc-uofu/intro-numpy).

### JupyterLite build

As of Fall 2026, we recommend hosting the lecture materials as a static site instead of relying on a third-party service or having attendees set up Python. Build a static site with

```console
make build
```

This creates `_output/` with static web content.
