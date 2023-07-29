from collections import deque
from typing import Optional

NULL = "#"


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []

        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                result.append(str(node.val) if node else NULL)
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
        return ' '.join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == NULL:
            return None
        elements = data.split()

        root = TreeNode(int(elements[0]), None, None)
        node_queue = deque([root])
        val_queue = deque(elements[1:])
        while val_queue:
            val1 = val_queue.popleft()
            val2 = val_queue.popleft() if val_queue else NULL
            node = node_queue.popleft()

            if val1 != NULL:
                node.left = TreeNode(int(val1), None, None)
                node_queue.append(node.left)
            if val2 != NULL:
                node.right = TreeNode(int(val2), None, None)
                node_queue.append(node.right)
        return root
