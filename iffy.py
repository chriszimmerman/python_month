print('How old are you?')
age = int(input())

if age < 40:
    print("You're not THAT old.")
else:
    print("Wow! You be old!")

print('Are you |dead| or |alive|?')
status = input()

if status == 'dead':
    print('Dead |inside| or dead |physically|?')
    dead = input()

    if dead == 'inside':
        print('Maybe you should do some soul searching.')
    elif dead == 'physically':
        print('Wow! A corpse that can type!')
    else:
        print('I do not understand that')
elif status == 'alive':
    print('Hooray! You are not dead yet!')
else:
    print('No comprendo')

