class BTNode {
    constructor(value) {
        this.val = value;
        this.left = null;
        this.right = null;
        }
    }
    class BST {
        constructor() {
            this.root = null;
        }
        add(val) {
            let new_node = new BTNode(val);
            if (this.root == null) {
                this.root = new_node;
                return this;
            }
            else {
                let runner = this.root;
                while (runner) {
                    if (new_node.val > runner.val) {
                        if (runner.right) {
                            runner = runner.right; 
                        }
                        else {
                            runner.right = new_node;
                            return this;
                        }
                    }
                    else {
                        if (runner.left) {
                            runner = runner.left;
                        }
                        else {
                            runner.left = new_node;
                            return this;
                        }
                    }
                }
                if (new_node.val > runner.val) {
                    runner.right = new_node;
                    runner = runner.right;
                }
                else {
                    runner.left = new_node;
                    runner = runner.left;
                }
                return runner;
            }
        }
        contains(val) {
            let runner = this.root; 
            while (runner) {
                if (runner.val == val) {
                    return true; 
                }
                else if (val > runner.val) {
                    runner = runner.right; 
                }
                else if (val < runner.val) {
                    runner = runner.left; 
                }
            }
            return false;
        }
        min() {
            let runner = this.root; 
            while (runner.left != null) {
                runner = runner.left; 
            }
            return runner; 
        }
        max() {
            let runner = this.root;
            while (runner.right != null) {
                runner = runner.right;
            }
            return runner;
        }
    }

const myInstance = new BST();

myInstance.add(21);
myInstance.add(28);
myInstance.add(25);
myInstance.add(32);
myInstance.add(14); 
myInstance.add(18); 
myInstance.add(15); 
myInstance.add(11); 
console.log(myInstance.contains(28));
console.log(myInstance.min());
console.log(myInstance.max());
console.log(myInstance.size());


    