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
    int pairSum(ListNode* head) {
        ListNode *fast=head,*slow=head;
        int maxVal=0;
        while(fast and fast->next){
            fast=fast->next->next;
            slow=slow->next;
        }
        ListNode *nextNode,*prev=NULL;
        while(slow){
            nextNode = slow->next;
            slow->next = prev;
            prev = slow;
            slow = nextNode;
        }
        while(prev){
            maxVal= max(maxVal, prev->val + head->val);
            prev = prev->next;
            head = head->next;
        }
        return maxVal;
    }
};