# Booleans datatype
# Comparing Operators [==, >, >=, <, <=, !=]

x = 50
y = 100
print(x < y)
print(50 > 100)
print(x == y)
print(x != y)

# Compare with if
if x < y:
    print("x is less than y")
else:
    print("x is not less than y")

# for sperating code 
print("=" * 60)

# Some of True values
print(bool("I Love Python"))                # String
print(bool(90))                             # Integer
print(bool([1,2,3]))                        # List 
print(bool((1,2,3)))                        # Tuple
print(bool({1,2,3}))                        # Set
print(bool({"char1": "A", "char2": "B"}))   # Dictionary

# for sperating code 
print("=" * 60)

# Some of False values
print(bool(""))         # Empty string
print(bool(0))          # Zero number is false
print(bool(False))      # False value is false
print(bool(None))       # None value is false
print(bool([]))         # List is false 
print(bool(()))         # Tuple is false 
print(bool({}))         # Dictionary/Set is false 
