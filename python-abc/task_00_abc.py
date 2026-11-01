#!/usr/bin/python3
"""This module defines an abstract Animal class and its subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Return the sound the animal makes."""
        pass


class Dog(Animal):
    """Represents a dog."""

    def sound(self):
        """Return the sound a dog makes."""
        return "Bark"


class Cat(Animal):
    """Represents a cat."""

    def sound(self):
        """Return the sound a cat makes."""
        return "Meow"
