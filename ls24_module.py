"""An example Python module."""

from typing import List

# Step 0: Implement skeleton function

def total(xs: List[float]) -> float:
    """Total returns the sum of xs"""
    result: float = 0.0
    # for each x float in sx, add it to the result
    for x in xs: 
        result += x
    return result

# Step 1: Think of some use cases
# total([1,2,3]) should return 6.0
# total([110]) should return 110.0
# total([]) should return 0.0

