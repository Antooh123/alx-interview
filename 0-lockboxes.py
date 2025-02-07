#!/usr/bin/python3
from collections import deque

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of lists): A list of lists where each inner list contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)  # Total number of boxes
    if n == 0:
        return False  # No boxes to open

    visited = set()  # Set to track visited boxes
    queue = deque()  # Queue for BFS traversal

    # Start with the first box (already unlocked)
    queue.append(0)
    visited.add(0)

    # Perform BFS
    while queue:
        current_box = queue.popleft()
        for key in boxes[current_box]:
            if key < n and key not in visited:
                visited.add(key)
                queue.append(key)

    # Check if all boxes are visited
    return len(visited) == n
