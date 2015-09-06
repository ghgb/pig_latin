#!-*- coding: utf8 -*-
print 'Bem-vindo ao Tradutor de Pig Latin!'

# Define 'pyg'
pyg = 'ay'
# Mostra um prompt para o usuário digitar uma palavra:
original = raw_input('Enter a word:')
# Verifica se a palavra digitada é constituída somente por letras
# e se a palavra tem pelo menos uma letra:

if len(original) > 0 and original.isalpha():
    print original 
    word = original.lower()
# Move a primeira letra da palavra digitada para o final, 
# e adiciona 'ay':
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
# Exibe a nova palavra:  
    print new_word
# Exibe 'empty' caso a palavra digitada não tenha pelo menos uma letra,
# ou se a palavra digitada não for composta apenas por letras:
else:
    print 'empty'
