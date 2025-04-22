import math
def jump_search(sorted_keys, target_range):
    """
    Performs Jump Search on a sorted list of keys to find values within a target range.
    Returns a list of matching keys.
    :target_range: Tuple of (min, max) values to search within.
    """
    n = len(sorted_keys)
    step = int(math.sqrt(n))
    result = []

    prev = 0
    while prev < n and sorted_keys[min(n - 1, prev + step - 1)] < target_range[0]:
        prev += step

    for i in range(prev, min(prev + step, n)):
        if target_range[0] <= sorted_keys[i] <= target_range[1]:
            result.append(sorted_keys[i])
    return result

def exponential_search(sorted_keys, target_range):
    """
    Performs Exponential Search to find a value range within a sorted list.
    Returns a list of matching keys.
    :target_range: Tuple of (min, max) values to search within.
    """
    n = len(sorted_keys)
    if n == 0:
        return []

    bound = 1
    while bound < n and sorted_keys[bound] < target_range[0]:
        bound *= 2

    left = bound // 2
    right = min(bound, n - 1)
    result = []

    for i in range(left, right + 1):
        if target_range[0] <= sorted_keys[i] <= target_range[1]:
            result.append(sorted_keys[i])
    return result


def search_nutrient(self, nutrient_index, value_range, algorithm):
    """
    Searches for food IDs whose nutrient value at a given index falls within a range.
    :nutrient_index: Index of the nutrient in the interface.
    :value_range: A tuple of (min, max) values to search within.
    :algorithm: "Jump" or "Exponential"
    :return: A set of matching food IDs.
    """
    sorted_dict = self.interface[nutrient_index]
    sorted_keys = list(sorted_dict.keys())

    if algorithm == "Jump":
        matching_keys = jump_search(sorted_keys, value_range)
    elif algorithm == "Exponential":
        matching_keys = exponential_search(sorted_keys, value_range)
    else:
        raise ValueError("Unsupported search algorithm.")
    matched_ids = set()
    for key in matching_keys:
        matched_ids.update(sorted_dict[key])
    return matched_ids