class Solution:
	def recoverTree(self, root: Optional[TreeNode]) -> None:
		

		array = []

		def InOrder(node):

			if node != None:

				InOrder(node.left)
				array.append(node)
				InOrder(node.right)

		InOrder(root)

		length = len(array)

		first_node = array[0]

		second_node = array[-1]

		for i in range(1,length):
			if array[i].val < array[i-1].val:
				first_node = array[i-1]
				break

		for i in range(length-2,-1,-1):
			if array[i].val > array[i+1].val:
				second_node = array[i+1]
				break

		first_node.val , second_node.val = second_node.val , first_node.val