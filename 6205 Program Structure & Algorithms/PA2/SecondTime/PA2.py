import argparse
import time

# def all_construct(target, wordbank, memo=None):
#     if memo is None:
#         memo = {}

#     if target == "":
#         return [[]]  # Base case: one valid way to construct nothing

#     result = []

#     for word in wordbank:
#         if target.startswith(word):
#             suffix = target[len(word):]  # Remove prefix
#             suffix_ways = all_construct(suffix, wordbank, memo)  # Recurse on suffix
#             target_ways = [[word] + way for way in suffix_ways]  # Prepend current word
#             result.extend(target_ways)  # Add all combinations to result

#     memo[target] = result  # Save in memo before returning
#     return result


# def main():
#     """
#     Entry point for the program. Parses command-line arguments and prints results.
#     """
#     parser = argparse.ArgumentParser(description="Find all ways to construct a target from a wordbank.")
#     parser.add_argument('-target', type=str, required=True, help="The target string to construct.")
#     parser.add_argument('-wordbank', nargs='*', default=[], help="The list of words in the wordbank (optional).")
#     args = parser.parse_args()

#     target = args.target
#     wordbank = args.wordbank

#     start_time = time.time()
#     ways = all_construct(target, wordbank)
#     end_time = time.time()

#     print(f"\nNumber of ways: {len(ways)}")
#     print("[")
#     for way in ways:
#         print(f"  {way}")
#     print("]")
#     print(f"Runtime: {end_time - start_time:.6f} seconds\n")


# if __name__ == '__main__':
#     main()
import argparse
import time

"""
Dynamic Programming Solution for "All Construct" Problem

Subproblem Definition:
- Let `all_construct(target, wordbank)` represent all the ways to construct the `target` string
  using the words in the `wordbank`.

Decisions:
- For each word in the `wordbank`, check if it is a prefix of the `target`.
- If yes, recursively solve the subproblem for the remaining suffix of the `target`.

Recursion:
- Base Case: If `target` is an empty string, return `[[]]` (one way to construct nothing).
- Recursive Case: For each word that is a prefix of `target`, find all ways to construct the
  suffix and prepend the current word to each way.

Memoization:
- Use a dictionary `memo` to store results of previously solved subproblems to avoid redundant computation.
"""

def all_construct(target, wordbank, memo=None):
    if memo is None:
        memo = {}

    if target in memo:
        print(f"Retrieving from memo: {target} -> {memo[target]}")
        return memo[target]

    if target == "":
        print(f"Base case reached for target: {target}")
        return [[]]  # Base case: one valid way to construct nothing

    print(f"Solving for target: {target}")
    result = []

    for word in wordbank:
        if target.startswith(word):
            suffix = target[len(word):]  # Remove prefix
            suffix_ways = all_construct(suffix, wordbank, memo)  # Recurse on suffix
            target_ways = [[word] + way for way in suffix_ways]  # Prepend current word
            result.extend(target_ways)  # Add all combinations to result

    memo[target] = result  # Save in memo before returning
    print(f"Memoizing: {target} -> {result}")
    return result


def main():
    """
    Entry point for the program. Parses command-line arguments and prints results.
    """
    parser = argparse.ArgumentParser(description="Find all ways to construct a target from a wordbank.")
    parser.add_argument('--target', type=str, required=True, help="The target string to construct.")
    parser.add_argument('--wordbank', nargs='*', default=[], help="The list of words in the wordbank (optional).")
    args = parser.parse_args()

    target = args.target
    wordbank = args.wordbank

    # Error handling for invalid inputs
    if not target and not wordbank:
        print("\nNumber of ways: 1")
        print("[[]]")
        print("Runtime: 0.000000 seconds\n")
        return

    if not wordbank:
        print("\nNumber of ways: 0")
        print("[]")
        print("Runtime: 0.000000 seconds\n")
        return

    start_time = time.time()
    ways = all_construct(target, wordbank)
    end_time = time.time()

    # Output results
    print(f"\nNumber of ways: {len(ways)}")
    print("[")
    for way in ways:
        print(f"  {way}")
    print("]")
    print(f"Runtime: {end_time - start_time:.6f} seconds\n")


if __name__ == '__main__':
    main()