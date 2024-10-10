#!/usr/bin/python3
'''function to check if boxes can be unlocked'''


def canUnlockAll(boxes):
    '''checking boxes and keys'''
    unlocked = {0}
    queue = [0]
    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key not in unlocked and key < len(boxes):
                unlocked.add(key)
                queue.append(key)
    return len(unlocked) == len(boxes)
