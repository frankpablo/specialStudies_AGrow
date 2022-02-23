# Open a file for reading and appending
with open('example.txt', 'r+') as f:
  # Read in two integers
  lines = f.readlines()


print ("lines:\n",lines)
print()

print ("BEFORE:")
for idx in range(len(lines)):
  lines[idx] = lines[idx].replace("\n", "")
  print(lines[idx])
  
print()

# move line 2 to 0, 1, and 2
new_lines = []
new_lines.append(lines[2]+"\n")
new_lines.append(lines[3]+"\n")
new_lines.append(lines[4]+"\n")
new_lines.append(lines[0]+"\n")
new_lines.append(lines[1]+"\n")

print ("new lines:\n",new_lines)
print()


# and write everything back
with open('example.txt', 'w+') as f:
  f.writelines( new_lines )

# Open a file for reading and appending
with open('example.txt', 'r+') as f:
  # Read in two integers
  lines = f.readlines()

print ("AFTER:")
for li in lines:
  li = li.replace("\n", "")
  print(li)
  
print()

# No need to call f.close() - f closed automatically 
print('Closed example.txt')