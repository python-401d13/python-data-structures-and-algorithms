import pytest
from fifo_animal_shelter import AnimalShelter, Cat, Dog
from challenges.stacks_and_queues.stacks_and_queues import Stack, EmptyStackException


def test_shelter_enqueue_when_empty(animal_shelter):
    """The animal shelter should add an animal to the queue when the queue is empty."""

    assert isinstance(animal_shelter.peek(), EmptyStackException)
    cat = Cat()
    animal_shelter.enqueue(cat)
    assert isinstance(animal_shelter.peek(), Cat)


def test_shelter_enqueue_when_not_empty(animal_shelter):
    """The animal shelter should add an animal to the queue when the queue is empty."""

    animals = [Cat(), Cat(), Dog()]
    for animal in animals:
        animal_shelter.enqueue(animal)

    assert isinstance(animal_shelter.peek(), Cat)


def test_shelter_dequeue_when_empty(animal_shelter):
    """The animal shelter can't remove an animal from the queue when the queue is empty."""

    assert isinstance(animal_shelter.dequeue(Cat), EmptyStackException)


def test_shelter_dequeue_when_not_empty_and_at_top(animal_shelter):
    """The animal shelter removes an animal from the queue when the queue isn't empty and the animal is at the front of the animal shelter."""

    animals = [Cat(), Cat(), Dog()]
    for animal in animals:
        animal_shelter.enqueue(animal)

    assert isinstance(animal_shelter.dequeue(Cat), Cat)


def test_shelter_dequeue_when_not_empty_and_not_at_top(animal_shelter):
    """The animal shelter removes an animal from the queue when the queue isn't empty and the animal isn't at the front of the animal shelter."""

    animals = [Cat(), Cat(), Dog()]
    for animal in animals:
        animal_shelter.enqueue(animal)

    assert isinstance(animal_shelter.dequeue(Dog), Dog)


# fixtures


@pytest.fixture
def animal_shelter():
    """AnimalShelter instance."""

    return AnimalShelter()
