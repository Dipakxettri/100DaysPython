
# Python Tuples and Methods

## Basics of Tuples:
- A tuple is an ordered collection of items, similar to a list, but **immutable** (cannot be changed after creation).
- Tuples are indexed, with indexing starting from 0.
- Tuples are defined using parentheses `()`.

## Tuple Operations:
- **Accessing Elements**:
  - `tuple[index]` â€“ Access an element by index.
  - Negative indexing: `tuple[-1]` â€“ Last element, `tuple[-2]` â€“ Second last, etc.

- **Slicing**:
  - `tuple[start:end]` â€“ Slicing from `start` to `end-1`.
  - `tuple[start:end:step]` â€“ Slicing with a step.

- **Modifying Tuples**:
  - Tuples are immutable, so their elements cannot be modified once created.
  - To "modify" a tuple, you need to create a new tuple by concatenating or slicing old tuples.

- **Tuple Operations**:
  - `tuple.index(value)` â€“ Return the index of the first occurrence of a value.
  - `tuple.count(value)` â€“ Return the number of occurrences of a value.
  - `tuple + tuple2` â€“ Concatenates two tuples (returns a new tuple).
  - `tuple * n` â€“ Repeats the tuple `n` times.

## Tuple Functions:
- `len(tuple)` â€“ Returns the number of elements in the tuple.
- `min(tuple)` â€“ Returns the smallest item in the tuple.
- `max(tuple)` â€“ Returns the largest item in the tuple.
- `sum(tuple)` â€“ Returns the sum of all elements in the tuple.
- `sorted(tuple)` â€“ Returns a sorted version of the tuple (returns a list).
- `any(tuple)` â€“ Returns `True` if any element is truthy.
- `all(tuple)` â€“ Returns `True` if all elements are truthy.
- `reversed(tuple)` â€“ Returns an iterator that accesses the tuple in reverse order (returns a tuple).

## Other Tuple Operations:
- `tuple in iterable` â€“ Check if an element is in the tuple.
- `tuple not in iterable` â€“ Check if an element is not in the tuple.