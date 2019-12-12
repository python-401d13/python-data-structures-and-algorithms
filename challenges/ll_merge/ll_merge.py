
def merge_lists(ll_one, ll_two):
    """
    Merge two linked lists by zipping their nodes.

    Parameters:
    ll_one (LinkedList): First linked list instance.
    ll_two (LinkedList): Second linked list instance.

    Retruns:
    LinkedList: First linked list merged with second.
    """

    if ll_one.head == None:
        return ll_two

    if ll_two.head == None:
        return ll_one

    current_one = ll_one.head
    current_two = ll_two.head
    step_count = 0
    while not current_one.next == None and not current_two.next == None:
        step_count += 1
        current_one = current_one.next
        current_two = current_two.next

    if current_two.next == None:
        current_two.next = current_one.next

    current_one.next = current_two

    while step_count > 0:
        current_one = ll_one.head
        current_two = ll_two.head
        for _ in range(step_count - 1):
            current_one = current_one.next
            current_two = current_two.next

        current_two.next = current_one.next
        current_one.next = current_two
        step_count -= 1

    return ll_one
