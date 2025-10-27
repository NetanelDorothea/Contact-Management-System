class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self, name, number):
        self.name = name
        self.number = number
    
    def __str__(self):
        return f"{self.name}: {self.number}"

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
   
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
  
    def hash_function(self, key):
        """Convert a string key (i.e. the contact’s name) into an array index using ord() or another method."""
        total = 0
        for char in key:
            # print(char, ord(char)) # Print out the character and Unicode value
            total += ord(char)
        # print(f"TOTAL: {total}") # Print out the total
        return total % self.size # Return the index
    
    def insert(self, key, value):
        """Create a Contact object and add it to the hash table a new Node. Be sure to handle collisions by adding to the linked list. If the key (name) already exists, update the contact's number."""
        index = self.hash_function(key)
        current = self.data[index] # Get the linked list value(s) for index

        contact = Contact(key, value) # Create the Contact object here
            
        # If there are no values currently at that position
        if current is None:
            self.data[index] = Node(key, contact)
            return

        while current: # Iterate until you reach a value of None
            if current.key == key: # Check if it is a duplicate
                current.value = contact
                return

            if current.next is None: 
                break  # Stop at last node
        
            current = current.next
        current.next = Node(key, contact) # Add to the end of the list

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next
        
        return None
    
    def print_table(self):
        for i in range(self.size):
            current = self.data[i]
            if current is None:
                print(f"Index {i}: Empty")
            else:
                value = ""
                while current:
                    value += f" - {current.value}"
                    current = current.next
                print(f"Index {i}:{value}")
        

# Test your hash table implementation here.  

table = HashTable(10)
table.print_table()

table.insert("John", "909-876-1234")
table.insert("Rebecca", "111-555-0002")

table.print_table()

contact = table.search("John") 
print("\nSearch result:", contact)

# Create HashTable instance
table = HashTable(10)
table.print_table()

# Add initial contacts
table.insert("John", "909-876-1234")
table.insert("Rebecca", "111-555-0002")
table.print_table()

# Edge Case #1 - Hash Collisions
table.insert("Amy", "111-222-3333")
table.insert("May", "222-333-1111")  # May collide with Amy
table.print_table()

# Edge Case #2 - Duplicate Keys (update existing contact)
table.insert("Rebecca", "999-444-9999")
table.print_table()

# Edge Case #3 - Search for non-existent contact
print(table.search("Chris"))  # Should print: None

"""
Design memo

Why is a hash table the right structure for fast lookups?

Hash tables are a great solution for this scenario because they allow for fast lookups. 
Instead of checking every value one by one, a hash table uses a special function to calculate exactly where the data should be stored or found. 
This lets the program jump straight to the correct location.
keys are associated with values which can be converted to an index.
With the hash function we can have an O(1) time complexity regardless of the size of the hash table.

How did you handle collisions?

The collisions are handled by associating the linked list with that index. 
The values with the same index will be stored in the linked list.
This way we only have to loop through the linked list onece we hit that index.

When might an engineer choose a hash table over a list or tree?

An engineer might vhoose a hash table over a list or tree when fast look ups are the priority and memory, and order does not matter. 
With a list you have to go through every element until the right element is reached.
A tree uses binary search which is also a little bit slower.  

"""