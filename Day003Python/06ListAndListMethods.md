# Python Lists and Methods

## Basics of Lists:
- A list is an ordered collection of items, which can be of different types.
- Lists are mutable, meaning their elements can be changed.
- Lists are indexed, with indexing starting from 0.
- Lists are defined using square brackets `[]`.

## List Operations:
- **Accessing Elements**: 
  - `list[index]` – Access an element by index.
  - Negative indexing: `list[-1]` – Last element, `list[-2]` – Second last, etc.

- **Slicing**:
  - `list[start:end]` – Slicing from `start` to `end-1`.
  - `list[start:end:step]` – Slicing with a step.

- **Modifying Lists**:
  - `list[index] = value` – Change an element at a specific index.
  - `list.append(value)` – Add an item to the end.
  - `list.insert(index, value)` – Insert an item at a specific index.
  - `list.extend(iterable)` – Add multiple items at the end.
  - `list.remove(value)` – Remove the first occurrence of a value.
  - `list.pop(index)` – Remove and return the item at the given index (default is last).
  - `list.clear()` – Remove all elements.

- **List Operations**:
  - `list.index(value)` – Return the index of the first occurrence of a value.
  - `list.count(value)` – Return the number of occurrences of a value.
  - `list.sort()` – Sort the list in ascending order (modifies the list).
  - `list.reverse()` – Reverse the order of elements in the list (modifies the list).
  - `list.copy()` – Return a shallow copy of the list.
  - `list.join()` – Join list elements into a single string (for strings in list).

- **List Comprehensions**:
  - `[expression for item in iterable]` – Basic list comprehension.
  - `[expression for item in iterable if condition]` – With a condition.

## List Functions:
- `len(list)` – Returns the number of elements in the list.
- `min(list)` – Returns the smallest item in the list.
- `max(list)` – Returns the largest item in the list.
- `sum(list)` – Returns the sum of all elements in the list.
- `sorted(list)` – Returns a sorted version of the list (doesn't modify the list).
- `any(list)` – Returns `True` if any element is truthy.
- `all(list)` – Returns `True` if all elements are truthy.
- `reversed(list)` – Returns an iterator that accesses the list in reverse order.

## Other List Operations:
- `list * n` – Repeats the list `n` times.
- `list + list2` – Concatenates two lists.
- `list in iterable` – Check if an element is in the list.
- `list not in iterable` – Check if an element is not in the list.