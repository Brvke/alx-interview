#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """ Check if all boxes can be unlocked """
    # Return True if there is only one box
    if len(boxes) == 1:
        return True

    # Initialize an empty set to store the keys
    kset = set()

    # Add keys found in the first box to the kset
    for key in boxes[0]:
        if key < len(boxes):
            kset.add(key)

    # Check if the number of keys in the kset is less than the number of boxes
    while len(kset) < len(boxes):
        # Store the current length of the kset
        prev_length = len(kset)

        # Iterate over a copy of the kset
        for key in kset.copy():
            # Add keys to the kset that correspond to locked boxes
            if key < len(boxes):
                for new_key in boxes[key]:
                    if new_key < len(boxes):
                        kset.add(new_key)

        # If the length of the kset remains the same, exit the loop
        if len(kset) == prev_length:
            break

    # Remove the key 0 from the kset since the first box is always unlocked
    kset.discard(0)

    # Check if all boxes can be unlocked
    if len(kset) == len(boxes) - 1:
        return True

    return False