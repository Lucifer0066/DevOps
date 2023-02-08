string = "this is python language"
even_string = []
odd_string = []
for i in range(len(string)):
        if i % 2 == 0:
            even_string.append(string[i])
        else:
            odd_string.append(string[i])

print(f'odd chars are {odd_string}')
print(f'even chars are {even_string}')            
