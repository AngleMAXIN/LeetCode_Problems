def reseverdsLink(head):
    if not head:
        return None 

    curr ,pre = head,None

    while curr:
        curr.next, pre, curr = pre, curr ,curr.next 
    return pre  