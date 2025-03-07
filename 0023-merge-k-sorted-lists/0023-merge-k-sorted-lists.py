class Solution:
    def mergeKLists(self, list_nodes: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        pq= []
        
        for ind,val in enumerate(list_nodes):
            if val:
                heapq.heappush(pq, (val.val,ind,val)) 
        
        dummy = ListNode()
        curr = dummy
        while(pq):
            val,ind,node = heapq.heappop(pq)
            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(pq, (node.next.val,ind,node.next))
            
        return dummy.next
    