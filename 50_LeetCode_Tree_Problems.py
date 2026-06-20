from typing import Optional, List
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class LeetCodeTreeSolutions:
    
    # 1. 144. Binary Tree Preorder Traversal
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Root, Left, Right"""
        res = []
        def dfs(node):
            if not node: return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res

    # 2. 94. Binary Tree Inorder Traversal
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Left, Root, Right"""
        res = []
        def dfs(node):
            if not node: return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res

    # 3. 145. Binary Tree Postorder Traversal
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Left, Right, Root"""
        res = []
        def dfs(node):
            if not node: return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        dfs(root)
        return res

    # 4. 102. Binary Tree Level Order Traversal
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """Level by level traversal using Queue"""
        if not root: return []
        res, q = [], collections.deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(level)
        return res

    # 5. 104. Maximum Depth of Binary Tree
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # 6. 111. Minimum Depth of Binary Tree
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        if not root.left: return 1 + self.minDepth(root.right)
        if not root.right: return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

    # 7. 100. Same Tree
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q or p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # 8. 101. Symmetric Tree
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if not left and not right: return True
            if not left or not right or left.val != right.val: return False
            return dfs(left.left, right.right) and dfs(left.right, right.left)
        return dfs(root.left, root.right) if root else True

    # 9. 226. Invert Binary Tree
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    # 10. 112. Path Sum
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        if not root.left and not root.right: return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

    # 11. 113. Path Sum II
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, current_path, current_sum):
            if not node: return
            current_path.append(node.val)
            current_sum += node.val
            if not node.left and not node.right and current_sum == targetSum:
                res.append(list(current_path))
            dfs(node.left, current_path, current_sum)
            dfs(node.right, current_path, current_sum)
            current_path.pop()
        dfs(root, [], 0)
        return res

    # 12. 129. Sum Root to Leaf Numbers
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, num):
            if not node: return 0
            num = num * 10 + node.val
            if not node.left and not node.right: return num
            return dfs(node.left, num) + dfs(node.right, num)
        return dfs(root, 0)

    # 13. 257. Binary Tree Paths
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(node, path):
            if not node: return
            path += str(node.val)
            if not node.left and not node.right:
                res.append(path)
            else:
                dfs(node.left, path + "->")
                dfs(node.right, path + "->")
        dfs(root, "")
        return res

    # 14. 110. Balanced Binary Tree
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node: return [True, 0]
            left, right = dfs(node.left), dfs(node.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]

    # 15. 543. Diameter of Binary Tree
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            res = max(res, left + right)
            return 1 + max(left, right)
        dfs(root)
        return res

    # 16. 236. Lowest Common Ancestor of a Binary Tree
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r: return root
        return l if l else r

    # 17. 235. Lowest Common Ancestor of a Binary Search Tree
    def lowestCommonAncestorBST(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > root.val and q.val > root.val: return self.lowestCommonAncestorBST(root.right, p, q)
        if p.val < root.val and q.val < root.val: return self.lowestCommonAncestorBST(root.left, p, q)
        return root

    # 18. 98. Validate Binary Search Tree
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node: return True
            if not (left < node.val < right): return False
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        return valid(root, float('-inf'), float('inf'))

    # 19. 700. Search in a Binary Search Tree
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val: return root
        return self.searchBST(root.left, val) if val < root.val else self.searchBST(root.right, val)

    # 20. 701. Insert into a Binary Search Tree
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)
        if val > root.val: root.right = self.insertIntoBST(root.right, val)
        else: root.left = self.insertIntoBST(root.left, val)
        return root

    # 21. 450. Delete Node in a BST
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return root
        if key > root.val: root.right = self.deleteNode(root.right, key)
        elif key < root.val: root.left = self.deleteNode(root.left, key)
        else:
            if not root.left: return root.right
            elif not root.right: return root.left
            # Find min from right subtree
            cur = root.right
            while cur.left: cur = cur.left
            root.val = cur.val
            root.right = self.deleteNode(root.right, root.val)
        return root

    # 22. 108. Convert Sorted Array to Binary Search Tree
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(l, r):
            if l > r: return None
            m = (l + r) // 2
            root = TreeNode(nums[m])
            root.left = helper(l, m - 1)
            root.right = helper(m + 1, r)
            return root
        return helper(0, len(nums) - 1)

    # 23. 114. Flatten Binary Tree to Linked List
    def flatten(self, root: Optional[TreeNode]) -> None:
        def dfs(root):
            if not root: return None
            leftTail = dfs(root.left)
            rightTail = dfs(root.right)
            if root.left:
                leftTail.right = root.right
                root.right = root.left
                root.left = None
            return rightTail or leftTail or root
        dfs(root)

    # 24. 105. Construct Binary Tree from Preorder and Inorder Traversal
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root

    # 25. 106. Construct Binary Tree from Inorder and Postorder Traversal
    def buildTreeInPost(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder: return None
        root = TreeNode(postorder.pop())
        mid = inorder.index(root.val)
        root.right = self.buildTreeInPost(inorder[mid+1:], postorder)
        root.left = self.buildTreeInPost(inorder[:mid], postorder)
        return root

    # 26. 654. Maximum Binary Tree
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None
        max_val = max(nums)
        max_idx = nums.index(max_val)
        root = TreeNode(max_val)
        root.left = self.constructMaximumBinaryTree(nums[:max_idx])
        root.right = self.constructMaximumBinaryTree(nums[max_idx+1:])
        return root

    # 27. 617. Merge Two Binary Trees
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2: return None
        v1 = root1.val if root1 else 0
        v2 = root2.val if root2 else 0
        root = TreeNode(v1 + v2)
        root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        root.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
        return root

    # 28. 124. Binary Tree Maximum Path Sum
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def dfs(root):
            if not root: return 0
            leftMax = max(dfs(root.left), 0)
            rightMax = max(dfs(root.right), 0)
            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)
        dfs(root)
        return res[0]

    # 29. 199. Binary Tree Right Side View
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])
        while q:
            rightSide = None
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide: res.append(rightSide.val)
        return res

    # 30. 515. Find Largest Value in Each Tree Row
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res, q = [], collections.deque([root])
        while q:
            level_max = float('-inf')
            for _ in range(len(q)):
                node = q.popleft()
                level_max = max(level_max, node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(level_max)
        return res

    # 31. 103. Binary Tree Zigzag Level Order Traversal
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque([root] if root else [])
        leftToRight = True
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(level if leftToRight else level[::-1])
            leftToRight = not leftToRight
        return res

    # 32. 637. Average of Levels in Binary Tree
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res, q = [], collections.deque([root])
        while q:
            level_sum = 0
            count = len(q)
            for _ in range(count):
                node = q.popleft()
                level_sum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(level_sum / count)
        return res

    # 33. 1302. Deepest Leaves Sum
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = collections.deque([root])
        ans = 0
        while q:
            ans = 0
            for _ in range(len(q)):
                node = q.popleft()
                ans += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return ans

    # 34. 872. Leaf-Similar Trees
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves(root):
            res = []
            def dfs(node):
                if not node: return
                if not node.left and not node.right: res.append(node.val)
                dfs(node.left)
                dfs(node.right)
            dfs(root)
            return res
        return get_leaves(root1) == get_leaves(root2)

    # 35. 222. Count Complete Tree Nodes
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    # 36. 404. Sum of Left Leaves
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node, is_left):
            nonlocal res
            if not node: return
            if not node.left and not node.right and is_left:
                res += node.val
            dfs(node.left, True)
            dfs(node.right, False)
        dfs(root, False)
        return res

    # 37. 513. Find Bottom Left Tree Value
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = collections.deque([root])
        ans = root.val
        while q:
            node = q.popleft()
            ans = node.val
            # right first, then left, so the last node popped is the left-most
            if node.right: q.append(node.right)
            if node.left: q.append(node.left)
        return ans

    # 38. 501. Find Mode in Binary Search Tree
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counts = collections.defaultdict(int)
        def dfs(node):
            if not node: return
            counts[node.val] += 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        max_c = max(counts.values())
        return [k for k, v in counts.items() if v == max_c]

    # 39. 530. Minimum Absolute Difference in BST
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev, min_diff = None, float('inf')
        def dfs(node):
            nonlocal prev, min_diff
            if not node: return
            dfs(node.left)
            if prev is not None:
                min_diff = min(min_diff, node.val - prev.val)
            prev = node
            dfs(node.right)
        dfs(root)
        return min_diff

    # 40. 99. Recover Binary Search Tree
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.first = self.middle = self.last = self.prev = None
        def dfs(node):
            if not node: return
            dfs(node.left)
            if self.prev and node.val < self.prev.val:
                if not self.first:
                    self.first = self.prev
                    self.middle = node
                else:
                    self.last = node
            self.prev = node
            dfs(node.right)
        dfs(root)
        if self.first and self.last:
            self.first.val, self.last.val = self.last.val, self.first.val
        elif self.first and self.middle:
            self.first.val, self.middle.val = self.middle.val, self.first.val

    # 41. 173. Binary Search Tree Iterator
    class BSTIterator:
        def __init__(self, root: Optional[TreeNode]):
            self.stack = []
            self.push_left(root)

        def push_left(self, node):
            while node:
                self.stack.append(node)
                node = node.left

        def next(self) -> int:
            node = self.stack.pop()
            self.push_left(node.right)
            return node.val

        def hasNext(self) -> bool:
            return len(self.stack) > 0

    # 42. 230. Kth Smallest Element in a BST
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        ans = -1
        def dfs(node):
            nonlocal n, ans
            if not node or ans != -1: return
            dfs(node.left)
            n += 1
            if n == k:
                ans = node.val
                return
            dfs(node.right)
        dfs(root)
        return ans

    # 43. 653. Two Sum IV - Input is a BST
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        def dfs(node):
            if not node: return False
            if k - node.val in seen: return True
            seen.add(node.val)
            return dfs(node.left) or dfs(node.right)
        return dfs(root)

    # 44. 96. Unique Binary Search Trees
    def numTrees(self, n: int) -> int:
        numTree = [1] * (n + 1)
        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left = root - 1
                right = nodes - root
                total += numTree[left] * numTree[right]
            numTree[nodes] = total
        return numTree[n]

    # 45. 116. Populating Next Right Pointers in Each Node
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        cur, nxt = root, root.left if root else None
        while cur and nxt:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
            cur = cur.next
            if not cur:
                cur = nxt
                nxt = cur.left
        return root

    # 46. 117. Populating Next Right Pointers in Each Node II
    def connectII(self, root: 'Node') -> 'Node':
        dummy = Node(0)
        curr = root
        while curr:
            tail = dummy
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                curr = curr.next
            curr = dummy.next
            dummy.next = None
        return root

    # 47. 863. All Nodes Distance K in Binary Tree
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {}
        def dfs(node, parent):
            if not node: return
            parents[node] = parent
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)
        
        q = collections.deque([(target, 0)])
        visited = {target}
        res = []
        while q:
            node, dist = q.popleft()
            if dist == k:
                res.append(node.val)
            if dist > k: break
            
            for neighbor in [node.left, node.right, parents[node]]:
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor, dist + 1))
        return res

    # 48. 1026. Maximum Difference Between Node and Ancestor
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, cur_max, cur_min):
            if not node: return cur_max - cur_min
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            left = dfs(node.left, cur_max, cur_min)
            right = dfs(node.right, cur_max, cur_min)
            return max(left, right)
        return dfs(root, root.val, root.val)

    # 49. 1339. Maximum Product of Splitted Binary Tree
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        total_sum = 0
        def get_sum(node):
            if not node: return 0
            return node.val + get_sum(node.left) + get_sum(node.right)
        total_sum = get_sum(root)
        
        max_prod = 0
        def dfs(node):
            nonlocal max_prod
            if not node: return 0
            sub_sum = node.val + dfs(node.left) + dfs(node.right)
            max_prod = max(max_prod, sub_sum * (total_sum - sub_sum))
            return sub_sum
        dfs(root)
        return max_prod % MOD

    # 50. 1373. Maximum Sum BST in Binary Tree
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return True, float('inf'), float('-inf'), 0
            
            l_is_bst, l_min, l_max, l_sum = dfs(node.left)
            r_is_bst, r_min, r_max, r_sum = dfs(node.right)
            
            if l_is_bst and r_is_bst and l_max < node.val < r_min:
                cur_sum = node.val + l_sum + r_sum
                ans = max(ans, cur_sum)
                return True, min(l_min, node.val), max(r_max, node.val), cur_sum
            
            return False, 0, 0, 0
        dfs(root)
        return ans
