# 定义节点
class TreeNode(object):
    def __init__(self,x,leftNode=None,rightNode=None):
        self.val = x
        self.left = leftNode
        self.right = rightNode
    def __str__(self):
        return str(self.val)

class Solution(object):
    def inver_tree(self,node):
        """
        :param node:TreeNode 
        :return: TreeNode
        """
        if node:           # 如果存在节点
            node.left,node.right = node.right,node.left # 父节点的左右子节点进行交换
            if node.left:  # 如果存在子左节点
                node.left = self.inver_tree(node.left)  # 把左节点传入递归函数inver_tree继续进行左子节点的孩子的左右交换
            if node.right:  # 如果存在子左节点
                node.right = self.inver_tree(node.right)  # 把右节点传入递归函数inver_tree继续进行右子节点的孩子的左右交换
        return node
def print_tree(node=None,is_child=False,deep=3):
    if not node and is_child: # 如果节点不为空且is_child等于True
        return
    if not is_child:           # 如果is_child为False
        print(node)
    if not node.left and not node.right:
        return
    print('%s>'%node,node.left,node.right)
    print_tree(node.left,is_child=True)
    print_tree(node.right,is_child=True)
if __name__ == '__main__':
    root = TreeNode(
        4,
        TreeNode(2,TreeNode(1),TreeNode(3)),
        TreeNode(7,TreeNode(6),TreeNode(9)),
    )
    print_tree(root)
    print('--------反转后--------')
    solution = Solution()
    inver_node = solution.inver_tree(root)
    print_tree(inver_node)
    
# 4
# 4> 2 7
# 2> 1 3
# 7> 6 9
# --------反转后--------
# 4
# 4> 7 2
# 7> 9 6
# 2> 3 1