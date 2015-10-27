#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
    	prev=head
    	nextP=head
    	while n-1>0:
    		nextP=nextP.next
    		n=n-1
    	if nextP.next==None:
    		return head.next
    	else:
    		nextP=nextP.next
    		while nextP.next!=None:
    			nextP=nextP.next
    			prev=prev.next
    		prev.next=prev.next.next
    		return head
