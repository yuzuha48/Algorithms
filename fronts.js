class Node {
    constructor(data){
        this.data=data;
        this.next=null;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
    }

    front() {
        return this.head.data
    }

    addFront(val){
        //Creating a new node object with the value provided
        let new_node= new Node(val);
        //Checking to see if the current list does not have a head node (if the list is empty)
        //If the list is empty, place the new node as the head 
        if(!this.head){
            this.head=new_node;
            return this;
        }
        //If the list is not empty, assign the head to be the next node to the new node (Blue Arrow in picture above)
        new_node.next=this.head;
        //Then finally assign the new_node to be the new head of the list (Red Arrow in picture above)
        this.head=new_node;
        return this;
    }

    removeFront() {
        let head_node = this.head;
        this.head = head_node.next;
        return this;
    }

    addToBack(val) {
        let new_node = new Node(val);
        let runner = this.head;
        while (runner.next != null) {
            runner = runner.next;
        }
        runner.next = new_node;
    }

    contains(val) {
        let runner = this.head;
        while (runner != null) {
            if (runner.data == val) {
                return true;
            }
            else {
                runner = runner.next;
            }
        }
        return false;
    }

    length() {
        let count = 0; 
        let runner = this.head; 
        while (runner != null) {
            count++;
            runner = runner.next;
        }
        return count;
    }

    display() {
        let all_values = "";
        let runner = this.head;
        while (runner != null) {
            if (runner.next != null) {
                all_values += String(runner.data) + ", ";
                runner = runner.next;
            }
            else {
                all_values += String(runner.data);
                runner = runner.next;
            }
        }
        return all_values;
    }
}


const myInstance = new LinkedList();

myInstance.addFront(2);
myInstance.addFront(3);
myInstance.addFront(5);
myInstance.addFront(9);
myInstance.addFront(12);
myInstance.addToBack(4);
myInstance.addToBack(6);
// console.log(myInstance.front());
// myInstance.removeFront();
// console.log(myInstance.contains(13));
// console.log(myInstance.length());
console.log(myInstance.display());
