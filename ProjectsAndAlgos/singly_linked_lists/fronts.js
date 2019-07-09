//add front
function addFront(pointer,value){
  //create a new node object
  var headNode = new ListNode(value);
  //point the next element to the current head
  headNode.next = this.head;
  //assign this object as the head 
  this.head = headNode;

  return headNode;
}



//remove front


function ListNode(value){
  this.val = value;
  this.next = null;
}