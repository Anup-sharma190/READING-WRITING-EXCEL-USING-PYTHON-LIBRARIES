"""
📌 Project: OOP Demo – Phone Class in Python
📌 Skills Shown: Object-Oriented Programming (Classes, Objects, Methods, Attributes)
📌 Tools Used: Python 3, PyCharm/VSCode
📌 What We Did:
    - Created a class `Phone` to represent real-world objects in code.
    - Defined methods to set and get (show) phone properties like colour and cost.
    - Demonstrated how to create an object, assign values, and retrieve them.
"""

# ---------------- Step 1: Define a Class ----------------
class Phone:
    # Method to set colour of the phone
    def set_colour(self, colour):
        self.colour = colour   # 'self.colour' becomes an attribute of the object

    # Method to set cost of the phone
    def set_cost(self, cost):
        self.cost = cost       # 'self.cost' is stored in the object

    # Method to show colour of the phone
    def show_colour(self):
        return self.colour     # return the object's attribute

    # Method to show cost of the phone
    def show_cost(self):
        return self.cost       # return the object's attribute


# ---------------- Step 2: Create Objects ----------------
p1 = Phone()                   # Create first Phone object
p1.set_colour("Blue")          # Assign colour
p1.set_cost(10000)             # Assign cost

p2 = Phone()                   # Create second Phone object
p2.set_colour("Black")
p2.set_cost(15000)

# ---------------- Step 3: Print Results ----------------
print("Phone 1 Details:")
print("Colour:", p1.show_colour())
print("Cost:", p1.show_cost())

print("\nPhone 2 Details:")
print("Colour:", p2.show_colour())
print("Cost:", p2.show_cost())
