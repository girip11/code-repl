# frozen_string_literal: true

# Operators and Operations

# Expression inside string literals
puts "Computation Result: #{5 + 6}"

# Any expression inside #{} will be evaluated in ruby

# Order of operations
# In the United States we use an acronym called PEMDAS which stands for
# "Parentheses Exponents Multiplication Division Addition Subtraction".
# That's the order Ruby follows as well.
# The mistake people make with PEMDAS is to think this is a strict order,
# as in "Do P, then E, then M, then D, then A, then S."
# The actual order is you do the multiplication and division (M&D) in one step, from left to right,
# then you do the addition and subtraction in one step from left to right.
# So, you could rewrite PEMDAS as PE(M&D)(A&S).
