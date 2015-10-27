# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
    	startingFrom = None
        if l1.val<l2.val:
        	startingFrom=l1
        	(aHead,bHead,aFollowing,bFollowing)=(l1,l2,l1.next,l2)
        else:
        	startingFrom=l2
        	bFollowing=l2.next
        	(aHead,bHead,aFollowing,bFollowing)=(l2,l1,l2.next,l1)
        while (aFollowing.next!=None and bFollowing.next!=None):
        	if aFollowing.val>=bFollowing.val:
        		aHead.next=bFollowing
        		bFollowing=bFollowing.next
        	else:
        		aHead.next=aFollowing
        		aFollowing=aFollowing.next
        if aFollowing.next==None:
        	aHead.next=bFollowing
        return startingFrom