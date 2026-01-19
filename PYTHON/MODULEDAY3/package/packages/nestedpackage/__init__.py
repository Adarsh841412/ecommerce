from .abc import abc
from .bcd import bcd 
__all__=["abc","bcd"]

print(__path__)
# 1. What the dot . means

# A single dot . means “look in the current package” (the same directory as the file you’re writing this in).

# Two dots .. mean “look in the parent package”, three dots ... for grandparent, etc.