class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "{}-->{}".format(self.val, self.next)

def main():
    l1 = ListNode(0)
    l1.next = ListNode(1)
    l2 = ListNode(6)
    l1.next = l2
    # l1.next.next = ListNode(2)
    print(l1)

if __name__ == '__main__':
    main()