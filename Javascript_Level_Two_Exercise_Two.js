// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array
function addNew(name){
  roster.push(name)
}

// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//
function remove(name){
  roster.splice(roster.indexOf(name),1)
}

// DISPLAY ROSTER

// Create a function called display that prints out the orster to the console.
function display(){
  console.log(roster);
}

// Start by asking if they want to use the web app
var start = prompt("Would you like to use the web app? Write yes or no only");

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
if (start==='yes'){
  var action = null;
  while (action != 'quit') {
    action = prompt('Define an action: add, remove, display or quit')
    if (action==='add') {
      var add = prompt('What would you like to add?');
      addNew(add)
    }else if (action==='remove') {
      var rev = prompt('What would you like to remove?');
      remove(rev)
    }else if (action==='display') {
      display()
    }else if (action==='quit') {
      alert('Thanks for visiting my web app :)')
    }else {
      alert('Please enter a valid command.')
    }
  }
}else if (start==='no') {
  alert('Thanks for visiting my web app :)')
}else {
  alert('Enter only yes or no')
}
