from collections import deque
from typing import Optional


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []
        if root is None:
            return str(result)

        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                result.append(node.val if node else "null")
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
        return str(result).replace("'", "").replace(', ', ',')

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "[]":
            return None
        elements = data[1:-1].split(',')

        root = TreeNode(int(elements[0]), None, None)
        node_queue = deque([root])
        val_queue = deque(elements[1:])
        while val_queue:
            val1 = val_queue.popleft()
            val2 = val_queue.popleft() if val_queue else "null"
            node = node_queue.popleft()

            if val1 != "null":
                node.left = TreeNode(int(val1), None, None)
                node_queue.append(node.left)
            if val2 != "null":
                node.right = TreeNode(int(val2), None, None)
                node_queue.append(node.right)
        return root
