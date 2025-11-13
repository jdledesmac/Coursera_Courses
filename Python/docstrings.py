"""Statistics utility: mean, median, mode

This module provides a single function `mean_median_mode` which accepts a
sequence of numbers and returns the mean, median and mode.

Behavior/contract
- Input: iterable of numbers (ints or floats)
- Output: tuple (mean: float, median: float, mode: list)
- Error modes: raises ValueError on empty input
- Mode is returned as a list. If there's a single most common value the list
  will contain one element; if multiple values tie for max frequency all are
  returned (sorted ascending).

Edge cases handled: empty input, even-length median, multimodal data.
"""

from collections import Counter
from typing import Iterable, List, Tuple


def mean_median_mode(numbers: Iterable[float]) -> Tuple[float, float, List[float]]:
	"""Return (mean, median, mode_list) for the given numbers.

	Args:
		numbers: iterable of numeric values (int or float).

	Returns:
		A tuple containing:
		  - mean (float)
		  - median (float)
		  - mode (list of numbers): list of the most frequent value(s), sorted

	Raises:
		ValueError: if `numbers` is empty.
	"""

	# Convert to list so we can iterate multiple times and sort
	data = list(numbers)
	if not data:
		raise ValueError("mean_median_mode() requires a non-empty sequence")

	n = len(data)

	# Mean
	mean = float(sum(data)) / n

	# Median
	sorted_data = sorted(data)
	mid = n // 2
	if n % 2 == 1:
		median = float(sorted_data[mid])
	else:
		median = (float(sorted_data[mid - 1]) + float(sorted_data[mid])) / 2.0

	# Mode: return list of most common value(s)
	counts = Counter(sorted_data)
	if not counts:
		mode_list = []
	else:
		max_count = max(counts.values())
		# collect all values that have frequency == max_count
		mode_list = sorted([val for val, cnt in counts.items() if cnt == max_count])

	return mean, median, mode_list


if __name__ == "__main__":
	# Simple self-tests / examples
	examples = [
		([1, 2, 2, 3], (2.0, 2.0, [2])),
		([1, 2, 3, 4], (2.5, 2.5, [1, 2, 3, 4]) if False else (2.5, 2.5, [1, 2, 3, 4])),
	]

	# The second example above is intentionally not expecting a single mode.
	# For [1,2,3,4] all values occur once so they tie; our function returns all of them.

	# Run assertions
	m, med, mode = mean_median_mode([1, 2, 2, 3])
	assert abs(m - 2.0) < 1e-9
	assert abs(med - 2.0) < 1e-9
	assert mode == [2]

	m, med, mode = mean_median_mode([1, 2, 3, 4])
	assert abs(m - 2.5) < 1e-9
	assert abs(med - 2.5) < 1e-9
	# multimodal: all values appear once -> all returned
	assert mode == [1, 2, 3, 4]

	# additional checks
	m, med, mode = mean_median_mode([5])
	assert m == 5.0 and med == 5.0 and mode == [5]

	print("All self-tests passed. Examples:\n")
	print("[1,2,2,3] ->", mean_median_mode([1, 2, 2, 3]))
	print("[1,2,3,4] ->", mean_median_mode([1, 2, 3, 4]))
