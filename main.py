import random
lucky_answers = ['It is certain', 'It is decidedly so', 'Without a doubt']
answers = ['Reply hazy, try again', 'Ask again later', 'Better not tell you now', 'Don’t count on it',
'My reply is no', 'My sources say no']

input('Whats your question?')

lucky = True

luck = random.randint(0, 7)
if luck == 1:
    lucky = True
else:
    lucky = False

if lucky:
    print(random.choice(lucky_answers))
else:
    print(random.choice(answers))