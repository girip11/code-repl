# Object Oriented Design

**NOTE**: These notes will be useful if you have read he book atleast once.

Object - collection of data and its associated behaviors.

## Object oriented analysis
* analysing the problem and get the **set of requirements**. Identify objects and their interaction.

## Object oriented design
* Based on the requirements, arrive at the **implementation specification**. Define objects, their behaviour etc.

## Object oriented programming
* implement the design(implementation specification)

## Objectes and classes
* class - blueprint for creating object. class of objects.

## Attributes
Attribute/member/property - characteristic of object.
Class hold the attribute, while objects of that class usually have different values for that attribute. Ex: name(attribute) of student(object).

## Behaviors
Behavior - action on an object. referred to as **methods**

## Public interface
collection of attributes and methods that other objects can use for interacting with an object
* information hiding
* encapsulation 
* abstraction - expose level of detail that is most appropriate. Ex: car interface to a driver and a mechanic

Objects names are nouns, while method names are verbs, attribute can be either adjective or noun.


## Composition and aggregation

Composition - collection of objects together to create another object.
Composition is aggregation and not vice versa. Aggregation is general form of composition.

* Composition - when the outer object(composite) object controls the inner objects creation and destruction. Solid diamond in UML.
* Aggregation - inner objects created and exist independently of the outer(composite) object.Hollow diamond in UML

## Inheritance
A class inherits attributes and methods from its parent class. Ex: king, queen, pawn, rook, bishop, knight can all inherit from ChessPiece.
* overriding methods
* abstract methods

## Polymorphism
treat class differently depending on subclass implementation.
* duck typing - walks like a duck, swims like a duck then its a duck.

## Multiple inheritance
inheriting from multiple parent classes.
Usage discouraged. move towards composite design.

---

## References:
* [Python3 Object oriented programming by Dusty Phillips](https://www.amazon.in/dp/B005O9OFWQ/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1)