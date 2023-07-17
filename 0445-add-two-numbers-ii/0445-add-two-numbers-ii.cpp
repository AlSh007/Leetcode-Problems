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
    ListNode* reverseList(ListNode* head){
        ListNode* prev = nullptr;
        while(head){
            ListNode* nxt = head->next;
            head->next = prev;
            prev = head;
            head = nxt;
        }
        return prev;
    }
    ListNode* helper(ListNode* l1,ListNode* l2){
        ListNode* dummy = new ListNode(0);
        ListNode* tail = dummy;
        int carry = 0;
        while(l1 != nullptr || l2 != nullptr or carry != 0){
            int digit1 = l1 != nullptr ? l1->val : 0;
            int digit2 = l2 != nullptr ? l2->val : 0;
            int sum = digit1 + digit2 + carry;
            int digit = sum%10;
            carry = sum/10;
            ListNode* newNode = new ListNode(digit);
            tail->next = newNode;
            tail = tail->next;
            
            l1 = (l1 != nullptr) ? l1->next : nullptr;
            l2 = (l2 != nullptr) ? l2->next : nullptr;

        }
        ListNode* result = dummy->next;
        delete dummy;
        return result;
    }
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        l1 = reverseList(l1);
        l2 = reverseList(l2);
        ListNode* ans = helper(l1, l2);
        return reverseList(ans);
    }
};