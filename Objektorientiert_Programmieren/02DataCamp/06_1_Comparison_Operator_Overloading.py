class Customer():
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


customer1 = Customer(1, "Ben", 23)
customer2 = Customer(1, "Ben", 23)

print(customer1 == customer2) # False
print(customer1) # unterschiedlicher Speicher
print(customer2)

# Bei Vergleichsoperatoren wird geschaut, ob der Speicher identisch ist.
# Da beide unterschiedliche Speicher haben, ist es False.

import numpy as np

array1 = np.array([[1,2,3]])
array2 = np.array([[1,2,3]])

print(array1 == array2) # Wuas? wieso bei numpy den gleichen Speicher?


