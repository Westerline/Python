#Stack#
monty_pythons = ['Eric','John','Micheal']
monty_pythons.append('Terry')
python = monty_pythons.pop()
print(monty_pythons)
print(python)

#Queue#
rappers = ['Eminem','Lamar','Jay Z']
rappers.append('Eric B')
rappers.append('Rakim')
print(rappers)
while rappers:
    rapper = rappers.pop(0)
    print rapper, " is now on stage!"