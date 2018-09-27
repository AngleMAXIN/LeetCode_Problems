

/* struct ListNode {
      int val;
      struct ListNode *next;
  };

思路:

    1-->3-->4-->6-->9
    假如要删除 `4` 结点

    1. 首先将该结点的值改为其下一个结点的值,即

        1-->3-->6-->6-->9
    2. 然后将该结点的next指向的原来下一个结点的下一个结点

        1-->3-->6   6   9
                I ______I
*/ 
void deleteNode(struct ListNode* node) {
    if (node == NULL)
        return;
    node->val = node->next->val;
    node->next = node->next->next;
}


