'use strict';
class Node {
  constructor(value){
    this.value = value;
    this.next = null;
  }
}

class List {
  constructor(){
    this.head = null;
  }
  
  //add front
  add(value){
    const node = new Node(value);
    
    node.next = this.head;
    this.head = node;
    return this;
  }
  
  //remove front
  remove(){
    const current = this.head;
    if(current){
      console.log('node object');
      this.head = current.next;
    }
    else {
      console.log('not a node object');
    }
    //use a ternary operator for the return statement
    return current ? current.value:null;
  }

  //front
  front(){
    const current = this.head;
    return current ? current.value: null;
  }

  //contains
  contains(testValue){
    let current = this.head;
    
    while(current){
      if (current.value === testValue){
        return true;
      }
      current = current.next;
    }
    return false;
  }

  //display
  display(){
    console.log('beginning to print list');
    
    let current = this.head;
    
    while(current){
      console.log(current.value);
      current = current.next;
    }
    console.log('finished printing list');
  }
  
  //a function that has a common format used to traverse SLs
  traverse(callback){
    let current = this.head;

    while(current){
      callback();
      current = current.next;
    }
  }
  
  //length
  length_w_traverse(){
    let count = 0;
    this.traverse(()=> count++);

    return count;
  }

  max_w_traverse(){
    let max = this.head ? this.head.value:null;
    let node = this.head;
    this.traverse(function(node){
      if(node.value > max){
        max = node.value;
      }
    });
    return max;
  }
  min_w_traverse(){
    let min = this.head ? this.max_w_traverse.value:null;

    this.traverse(function(node){
      if(node.value < min){
        min = node.value;
      }
    })
    return min;
  }

  average_w_traverse(){
    const length = this.length();
    let sum = 0;

    //uses an anonymous function to simplify the code. 
    //don't need parenthesis if it just accepts 1 parameter
    this.traverse((node) => sum += node.value);
    // this.traverse(function(node){
    //   sum += node.value;
    // })
    return sum/length;
  }

    
}

const array = [1,2,3,4,5,6,7];

//const node1 = new Node(1);
//const node2 = new Node(2);
//const node3 = new Node(3);
//node2.next = node3;
//node1.next = node2;

const list = new List();

//test out the add method
list.add(5);
list.add(9);

console.log(list.front());

//use a loop to create nodes from an array
for (let index = 0; index < array.length; index++){
  const value = array[index];
  console.log('adding value '+value);
  list.add(value);
}
console.log(list);
list.display();
console.log('contains 7? ' + list.contains(7));
console.log(list.remove());
list.display();
console.log('contains 7? '  + list.contains(7));


console.log('the max with travers is '+list.max_w_traverse());
console.log('the min with travers is '+list.min_w_traverse());
console.log('the average with travers is '+list.average_w_traverse());
console.log('the length with travers is '+list.length_w_traverse());