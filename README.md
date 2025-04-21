# Non-Overlapping Activities

This repository contains a Python implementation of an algorithm that selects activities with no overlapping schedules, based on sorting by finishing time. It is ideal for solving task selection problems within specific time intervals.

## Description

The algorithm takes a list of activities, each with a name, start time, and end time. Its goal is to return a set of activities that can be completed without schedule conflicts.

### Features

- Sorts activities by their finishing time.
- Allows updating the schedules of existing activities.
- Enables adding new activities with validations to avoid conflicts.
- Returns the selected activities that do not overlap.

## Usage

### Requirements

- Python 3.x

### Execution

1. Clone this repository.
2. Run the Python script in your terminal with:

    ```bash
    python n-overlap-schedule.py
    ```
4. Enter the initial activities or modify the existing ones.
5. Add new activities if desired.
6. The program will display the selected activities that can be performed without conflicts.

### Example

Given the initial list of activities:
```python
actividades = [
    {"nombre": "A1", "inicio": 1, "fin": 4},
    {"nombre": "A2", "inicio": 3, "fin": 5},
    {"nombre": "A3", "inicio": 0, "fin": 6},
    {"nombre": "A5", "inicio": 5, "fin": 7},
    {"nombre": "A6", "inicio": 5, "fin": 9}
]

```
### Example
### The results will be something like this:

```
--- Actividades que puedes hacer sin chocar ---
A1, A5

```


### Code Details

#### Function elegir_actividades
This function selects activities using the sorting criterion of finishing time. It receives a list of activities and returns a list with the names of the selected activities.

### User Interaction

The program allows modifying schedules and adding new activities via user input. It also validates that added activities have valid schedules (start time before end time) and that names do not repeat.
