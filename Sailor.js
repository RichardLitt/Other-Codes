// Prototypes!

// Every JavaScript object has an internal property called [[Prototype]].

// If you look up a property via obj.propName or obj['propName'] and the
// \object does not have such a property - which can be checked via
// obj.hasOwnProperty('propName') - the runtime looks up the property
// in the object referenced by [[Prototype]] instead. If the prototype-object
// also doesn't have such a property, its prototype is checked in turn,
// thus walking the original object's prototype-chain until a match is
// found or its end is reached.

// How many of you are familiar with classes?

// This allows to simulate classes in JavaScript, although JavaScript's
// inheritance system is - as we have seen - prototypical, and not class-based:

// Just think of constructor functions as classes and the properties of
// the prototype (ie of the object referenced by the constructor function's
//   prototype property) as shared members, ie members which are the same
// for each instance. In class-based systems, methods are implemented the
//   same way for each instance, so methods are normally added to the prototype,
// whereas an object's fields are instance-specific and therefore added to
// the object itself during construction.

// Code example 1

// Let's first define the constructor (here, empty).
function Sailor(){}

// Then, let's set a prototypical property
Sailor.prototype.raiseSails = function(){
  return true;
};

// Now, let's make an instance
var sinbad = Sailor();

//==== run =====//

console.log(!sinbad, "Is undefined, not an instance of Sailor." );

//==== run =====//

var sinbad = new Sailor();
console.log( sinbad.raiseSails(), "Method exists and is callable." );

//==== run =====//

// This is an example of Prototypical inheritance. Sailor didn't have
// the method needed; so, Javascript looked for the method in __prototype__.
// The constructur didn't have this method, either, but we had defined a
// protoype method for that object, so it was added to the object and could be
// found and run. Pretty sweet!

//

// Properties added in the constructor (or later) override prototyped properties.

// Let's degine this constructor again, but this time have an internal method
function Sailor(){
  this.raiseSails = function(){
    return true;
  };
}

// This should return false, but it will be overridden by the internal method of the constructor
Sailor.prototype.raiseSails = function(){
  return false;
};

var sinbad = new Sailor();
console.log( sinbad.raiseSails(), "Calling the instance method, not the prototype method." );

//==== run ====//

// Prototyped properties affect all objects of the same constructor,
// simultaneously, even if they already exist.

// Constructor with a method
function Sailor(){
  this.sailed = true;
}

// Two new instances
var sinbad = new Sailor();
var jackSparrow = new Sailor();

// Adding a prototypical method to Sailor
Sailor.prototype.raiseSails = function(){
  return this.sailed;
};

// And here we are, with both working, even after the instances were defined first.
console.log( sinbad.raiseSails(), "Method exists, even out of order." );
console.log( jackSparrow.raiseSails(), "and on all instantiated objects." );

//==== run ====//

// Chainable prototypes! Let's see if we can refer to methods from
// other prototype methods

// Constructor with a method
function Sailor){
  this.sailed = true;
}

// Two new instances
var sinbad = new Sailor();
var jackSparrow = new Sailor();

// Define a new prototype method that returns a method in the constructor
Sailor.prototype.sail = function(){
  this.sailed = false;
  return this;
};

console.log( !sinbad.sail().sailed, "Verify that the sail method exists and returns an instance." ); 
console.log( !jackSparrow.sail().sailed, "and that it works on all Sailor instances." );

//==== run ====//

// Basics of an object -- let's look into this

// Constructor
function Sailor(){} 

// New instance
var sinbad = new Sailor(); 
 
console.log( typeof sinbad == "object", "However the type of the instance is still an object." );   
console.log( sinbad instanceof Sailor, "The object was instantiated properly." ); 
console.log( sinbad.constructor == Sailor, "The sinbad object was created by the Sailor function." );

//==== run ====//

// Let's use this constructor to make other instances

function Sailor(){} 
var sinbad = new Sailor(); 
var jackSparrow = new sinbad.constructor(); 
 
console.log( jackSparrow instanceof Sailor, "Still a sinbad object." );

//==== run ====//

// Prototypical Inheritance!

function Person(){} 
Person.prototype.swim = function(){}; 
 
function Sailor(){} 
 
// Achieve similar, but non-inheritable, results 
Sailor.prototype = Person.prototype; 
Sailor.prototype = { swim: Person.prototype.swim }; 
 
console.log( (new Sailor()) instanceof Person, "Will fail because of a bad prototype chain." ); 
 
// Only this maintains the prototype chain!
Sailor.prototype = new Person(); 
 
var sinbad = new Sailor(); 
console.log( sinbad instanceof Sailor, "sinbad receives functionality from the Sailor prototype" ); 
console.log( sinbad instanceof Person, "... and the Person prototype" ); 
console.log( sinbad instanceof Object, "... and the Object prototype" );

/// And there we have it!

// Let's try a quiz!

function Person(){} 
Person.prototype.getName = function(){ 
  return this.name; 
};


// Implement a function that inherits from Person 
// and sets a name in the constructor 


var me = new Me(); 
assert( me.getName(), "A name was set." );

// And we're done here. Well done class. // 
