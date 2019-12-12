import linked_list

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


