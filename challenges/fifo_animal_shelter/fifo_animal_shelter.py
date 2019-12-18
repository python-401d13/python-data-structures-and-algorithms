from challenges.stacks_and_queues.stacks_and_queues import Stack, EmptyStackException

class AnimalShelter:
    """Queue of animals in a shelter."""

    def __init__(self):
        """AnimalShelter constructor."""

        self.main_stack = Stack()
        self.helper_stack = Stack()

    def enqueue(self, animal):
        """
        Bring an animal into the shelter.

        Parameters:
        animal (object): The Cat or Dog instance to bring into the shelter.
        """

        while not isinstance(self.main_stack.peek(), EmptyStackException):
            self.helper_stack.push(self.main_stack.pop())

        self.helper_stack.push(animal)

        while not isinstance(self.helper_stack.peek(), EmptyStackException):
            self.main_stack.push(self.helper_stack.pop())

    def dequeue(self, animal):
        """
        Take an animal out of the shelter.

        Parameters:
        animal (class): The Cat or Dog instance which should be taken out of the shelter.

        Returns:
        (Animal): The instance of the Cat or Dog class first in the queue in the shelter.
        """

        if isinstance(self.main_stack.peek(), EmptyStackException):
            return EmptyStackException()

        saved_animal = None

        while not isinstance(self.main_stack.peek(), EmptyStackException):
            if not saved_animal and isinstance(self.main_stack.peek(), animal):
                saved_animal = self.main_stack.pop()
            else:
                self.helper_stack.push(self.main_stack.pop())

        while not isinstance(self.helper_stack.peek(), EmptyStackException):
            self.main_stack.push(self.helper_stack.pop())

        return saved_animal

    def peek(self):
        """See the first animal in the shelter."""

        return self.main_stack.peek()

class Cat:
    """Animal which can be in shelter."""

    pass

class Dog:
    """Animal which can be in shelter."""

    pass

if __name__ == "__main__":
    animal_shelter = AnimalShelter()
    animal_shelter.dequeue(Cat)
