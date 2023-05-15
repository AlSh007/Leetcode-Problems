/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        ListNode *first=head;
        ListNode *slow=head;
        ListNode *kth=nullptr;
        while(--k){
            first=first->next;
        }
        kth=first;
        first=first->next;
        while(first){
            slow=slow->next;
            first=first->next;
        }
        swap(slow->val,kth->val);
        return head;
    }
};