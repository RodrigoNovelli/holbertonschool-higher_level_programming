# **Python - Everything is object**

- **Object**: A value stored in memory, like a list or number.
- **Class vs. Object**: A class is a blueprint; an object (or instance) is created from it.
- **Mutable vs. Immutable**: Mutable objects (e.g. lists) can change; immutable ones (e.g. strings) cannot.
- **Reference**: A variable that points to an object in memory.
- **Assignment**: Binding a variable to an object.
- **Alias**: Two variables that refer to the same object.
- **Identical Variables**: Use `is` to check identity.
- **Same Object**: If `a is b`, they point to the same object.
- **Variable ID**: Use `id(variable)` to see its identity (memory address in CPython).
- **Mutable Types**: Lists, dictionaries, sets.
- **Immutable Types**: Integers, floats, strings, tuples.
- **Function Argument Passing**: Python passes references; mutable objects can be changed inside functions.

## Is `a` a tuple?

- **Question:** `a = ()`
- **Answer:** Yes, `a` is a tuple (empty tuple).

## Is `a` a tuple?

- **Question:** `a = (1, 2)`
- **Answer:** Yes, `a` is a tuple containing `(1, 2)`.

## Is `a` a tuple?

- **Question:** `a = (1)`
- **Answer:** No, `a` is not a tuple. It's an integer in parentheses. A single-element tuple should be written as `a = (1,)`.

## Do `a` and `b` point to the same object?

- **Question:** `a = 89`, `b = 100`
- **Answer:** No, they are different objects.

## Do `a` and `b` point to the same object?

- **Question:** `a = 89`, `b = 89`
- **Answer:** Yes, they point to the same object because small integers are cached.

## Do `a` and `b` point to the same object?

- **Question:** `a = 89`, `b = a`
- **Answer:** Yes, `a` and `b` point to the same object.

## Do `a` and `b` point to the same object?

- **Question:** `a = 89`, `b = a + 1`
- **Answer:** No, `a` and `b` are different objects after the operation.

## What do these 3 lines print?

- **Code:**
    
    ```python
    s1 = "Best School"
    s2 = "Best School"
    print(s1 == s2)
    
      Answer: True, since the string values are the same.
    
    ```
    

What do these 3 lines print?

```
Code:

s1 = "Best"
s2 = s1
print(s1 is s2)

Answer: True, because s1 and s2 point to the same object in memory.

```

What do these 3 lines print?

```
Code:

s1 = "Best School"
s2 = "Best School"
print(s1 is s2)

Answer: True, since Python may use string interning for identical literals.

```

What do these 3 lines print?

```
Code:

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2)

Answer: True, because the lists contain the same elements.

```

What do these 3 lines print?

```
Code:

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 is l2)

Answer: False, since l1 and l2 are two distinct objects.

```

What do these 3 lines print?

```
Code:

l1 = [1, 2, 3]
l2 = l1
print(l1 is l2)

Answer: True, since both l1 and l2 point to the same list object.

```

What do these 3 lines print?

```
Code:

l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)

Answer: [1, 2, 3, 4], since l2 is the same list as l1.

```

What do these 3 lines print?

```
Code:

l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)

Answer: [1, 2, 3], because l1 now points to a new list, but l2 still refers to the old one.

```

What does this script print?

```
Code:

def increment(n):
    n += 1

a = 1
increment(a)
print(a)

Answer: 1, since integers are immutable and a is not modified by the function.

```

What does this script print?

```
Code:

def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)

Answer: [1, 2, 3, 4], since lists are mutable and append modifies the list in place.

```

What does this script print?

```
Code:

def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)

Answer: [1, 2, 3], since the assignment inside the function does not affect l1.

```

What does this script print?

```
Code:

l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)

Answer: [1, 2, 3], because the + operator creates a new list, so l2 is unaffected.

```

What does this script print?

```
Code:

l1 = [1, 2, 3]
l2 = l1
l1 += [4]
print(l2)

Answer: [1, 2, 3, 4], since the += operator modifies the list in place.

```