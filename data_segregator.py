text_file = open('data/letters_v1.1.txt').read()
# n = text_file.write(text)
# text_file.close()

letters = text_file.split('\n\n\n')
# print(len(letters))
# print(letters[0])

for i in range(len(letters)):
    filename = 'letters/' + str(i)
    text_file = open(filename,'wt')
    n = text_file.write(letters[i])
    text_file.close()
    print('created letter '+str(i))

