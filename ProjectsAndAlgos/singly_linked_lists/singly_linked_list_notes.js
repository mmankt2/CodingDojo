function ListNode(value){
  this.val = value;
  this.next = null;
}

class Node {
  consttructor(value){
    this.value = value;
    this.next = null;
  }
}

class List {
  constructor(){
    this.head = null;
  }
  
  display(){
    console.log('beginning to print list');
    
    let current = this.head;
    
    while(current){
      console.log(current.value);
      current = current.next;
    }
    console.log('finished printing list');
  }
  
  add(value){
    const node = new Node(value);
    
    node.next = this.head;
    this.head = node;
    //if (this.head !== null){
    //  this.head.next = node;
    //}
    //else {
    //  this.head = node;
    //}
    return this;
  }
  
  remove(){
    const current = this.head;
    if(current){
      console.log('node object');
      this.head = current.next;
    }
    else {
      console.log('not a node object');
    }
    
    return current ? current.value:null;
  }
  
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

console.log(node1);
console.log(list);

//programattically create nodes from an array
for (let index = 0; index < array.length; index++){
  const value = array[index];
  console.log('adding value '+value);
  list.add(value);
}

list.display();
console.log('contains 7? ' + list.contains(7));
console.log(list.remove());
list.display();
console.log('contains 7? '  + list.contains(7));