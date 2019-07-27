class BSTNode {
  constructor(val) {
    this.value = val;
    this.left = null;
    this.right = null;
  }
}

class BST {
  constructor() {
    this.root = null;
  }

  min() {
    if (this.root === null) {
      return false;
    }

    let runner = this.root;
    while (runner.left != null) {
      runner = runner.left;
    }
    return runner.value;
  }

  max() {
    if (this.root === null) {
      return false;
    }

    let runner = this.root;
    while (runner.right != null) {
      runner = runner.right;
    }
    return runner.value;
  }

  contains(value, node = this.root) {
    if (node === null) {
      return null;
    }
    //does the node we're looking at possess the value we seek
    if (node.value === value) {
      return true;
    }
    if (node.value < value) {
      //look left
    } else {
      //look right
    }
  }

  breadth_first() {
    //print the node values in a breadth first order. 
    //breadth uses queues FIFO. 
    //start at the root
    //make a queue as an array
    if (this.root == null) {
      return false;
    }
    var queue = [];
    //start with the root
    queue.push(this.root); //adds the node object

    //add the left and right child after checking the root
    while (queue.length > 0) {
      //add some code that checks if the left or right are null before trying to access them.
      queue.push(queue[0].left);
      queue.push(queue[0].right);
      console.log(queue[0].value);
      queue.shift();
    }
  }

  add(value) {
    var node = new BSTNode(value);
    if (!this.root) {
      return this.root = node;
    }
    var current = this.root;
    while (current) {
      if (value < current.value) {
        if (current.left) {
          current = current.left;
        } else {
          return current.left = node;
        }
      } else {
        // val >= current.value
        if (current.right) {
          current = current.right;
        } else {
          return current.right = node;
        }
      }
    }
  }
}

let tree = new BST();


tree.add(5);
tree.add(1);
tree.add(10);
tree.add(3);
tree.add(15);
tree.add(-1);
tree.add(8);
//search methods can use queues and stacks. 
//stacks is good for a depth search
//queues is good for a breadth search
console.log(tree);
tree.breadth_first();