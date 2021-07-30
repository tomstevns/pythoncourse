""" 
I Python kan du lægge alt i en liste, og de behøver ikke at have nogen relation til hinanden.

Navngivning af lister er i flertal.

Square bracket [ ] indiker en liste, og elementerne er adskilt med komma.
 """

numbers = [1, 2, 3, 4, 5]
print(numbers)

words = ['cat', 'bat', 'rat']
print(words)

mixed_elements = ['Hello', 3.231, True, None, 42]
print(mixed_elements)

empty_list = [ ]
print(empty_list)

# Accessing Elements
animals = ['cat', 'bat', 'rat', 'elephant']
print(animals[3]) # elephant

print(animals[0] + 'woman and ' + animals[1] + 'man') # catwoman and batman

# Negativ indexes - How to get the last element of a list?
print(animals[-1]) # elephant

print(animals[-3]) # bat

# Getting Sublists with Slices
# Slice på lists skrives [1:4]. Start på index 1 og gå til index 4(index 4 er ikke includeret). Returner et nyt array.
print(animals[1:3]) # ['bat', 'rat']

print(animals[0:-1]) # ['cat', 'bat', 'rat'] PRinter ikke det sidste element.

print(animals[-2:-1]) # ['rat'] Fjerner de 2 første og det sidste element.

print(animals[:3]) # ['cat', 'bat', 'rat'] Svarer til at der står [0:3]

print(animals[::2]) # ['cat', 'rat']

# Getting a List's Length with len()
fst_sentence = ['Call', 'me', 'Ishmael']
print(len(fst_sentence)) # 3

# Changing Values in a List with Indexes
fst_sentence[1] = 'him'
print(fst_sentence) # ['Call', 'him', 'Ishmael']

fst_sentence[-1] = 1000
print(fst_sentence) # ['Call', 'him', 1000]

# List Concatenation and List Replication
number = [1, 2, 3, 4]
concat = fst_sentence + numbers
print(concat) # ['Call', 'him', 1000, 1, 2, 3, 4, 5]

kopier_indhold = fst_sentence * 3
print(kopier_indhold) # ['Call', 'him', 1000, 'Call', 'him', 1000, 'Call', 'him', 1000]

# Slet elementer fra en liste med del. Alle elementerne rykker en plads op efter en sletning.
fst_sentence_del = ['Call', 'me', 'Ishmael']
del fst_sentence_del[1]
print(fst_sentence_del) # ['Call', 'Ishmael']

# Kopier en liste
fst_sentence = ['Call', 'me', 'Ishmael']

new_sentence = fst_sentence[:]
new_sentence[1] = 'him'

print(fst_sentence) # ['Call', 'me', 'Ishmael']
print(new_sentence) # ['Call', 'him', 'Ishmael']

# Sorter en liste af elementer med sorted()
sorted_sentence = sorted(fst_sentence)
print(sorted_sentence) # ['Call', 'Ishmael', 'me']
print(fst_sentence) # ['Call', 'me', 'Ishmael']

unordered_numbers = [50, 1, -20, 34 , 2, -400]
sorted_numbers = sorted(unordered_numbers)
print(sorted_numbers) # [-400, -20, 1, 2, 34, 50]
