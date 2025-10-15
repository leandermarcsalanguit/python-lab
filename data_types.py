
text = "This is a string."
print(text)
print(type(text), "\n")

x = 13
print(x)
print(type(x), "\n")

y = 13.13
print(y)
print(type(y), "\n")

z = 13 + 13j
print(z)
print(type(z), "\n")

list_ = ["Alpha", "Bravo", "Charlie"]
print(list_)
print(type(list_), "\n")

tuple_ = ("Alpha", "Bravo", "Charlie")
print(tuple_)
print(type(tuple_), "\n")

a = range(13)
print(a)
print(type(a), "\n")

dictionary = {"A" : "Alpha",
              "B" : "Bravo",
              "C" : "Charlie"
              }
print(dictionary)
print(type(dictionary), "\n")

set_ ={"Alpha", "Bravo", "Charlie"}
print(set_)
print(type(set_), "\n")

frozenset_ = frozenset({"Alpha", "Bravo", "Charlie"})
print(frozenset_)
print(type(frozenset_), "\n")

bool_ = True
print(bool_)
print(type(bool_), "\n")

byte_ = b"Byte"
print(byte_)
print(type(byte_), "\n")

byte_array = bytearray(13)
print(byte_array)
print(type(byte_array), "\n")

memory_view = memoryview(bytes(13))
print(memory_view)
print(type(memory_view), "\n")

None_ = None
print(None)
print(type(None), "\n")