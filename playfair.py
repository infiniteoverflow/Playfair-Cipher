import numpy as np

alphabets = 'abcdefghijklmnopqrstuvwxyz'

def create_matrix(key):
    '''
     Method to convert given key into the matrix
     required to perform the playfair cipher algorithm
    '''

    arr = np.full((5,5),' ')
    key_letters = []
    for ch in key:
        if ch not in key_letters:
            key_letters.append(ch)

    ele_count = 0
    alpha_count = 0

    new_alphabet_list = []
    for ch in alphabets:
        if ch not in key_letters:
            new_alphabet_list.append(ch)
    

    for i in range(5):
        for j in range(5):
            if ele_count < len(key_letters):
                arr[i][j] = key_letters[ele_count]
                ele_count+=1
            else:
                if new_alphabet_list[alpha_count] != 'j':
                    arr[i][j] = new_alphabet_list[alpha_count]
                else:
                    alpha_count+=1
                    arr[i][j] = new_alphabet_list[alpha_count]
                alpha_count+=1
    
    return arr


def generate_pairs(message):
    '''
        Method used to generate word pairs used 
        in the cipher algorithm
    '''
    no_of_pairs = int(len(message)/2)

    pairs = []

    message_list = [ch for ch in message]
    message_list.append('0')

    for i in range(0,len(message),2):
        if (message_list[i] != message_list[i+1]) and (message_list[i+1] != '0'):
            pairs.append(message_list[i]+message_list[i+1])
        elif message_list[i+1] == '0':
            pairs.append(message_list[i]+'x')
        elif message_list[i] == message_list[i+1]:
            pairs.append(message_list[i]+'x')
            pairs.append(message_list[i+1]+'x')
    
    return pairs


def generate_playfair_cipher(matrix,message_pairs):
    '''
        Method to implement the playfair algorithm
    '''

    cipher_pair = []

    hash_map = {}

    for i in range(5):
        for j in range(5):
            hash_map[matrix[i][j]] = '{} {}'.format(i,j)
    
    hash_map['j'] = hash_map['i']

    for pair in message_pairs:
        p1,p2 = pair[0],pair[1]

        r1,c1 = hash_map[p1].split(' ')
        r2,c2 = hash_map[p2].split(' ')

        r1,c1,r2,c2 = int(r1),int(c1),int(r2),int(c2)
    
        if(r1 == r2):
            if c1+1 > 4:
                c1 = -1
            if c2+1 > 4:
                c2 = -1
            
            cipher_pair.append(matrix[r1][(c1+1)]+matrix[r2][(c2+1)])

        elif(c1 == c2):
            if r1+1 > 4:
                r1 = -1
            if r2+1 > 4:
                r2 = -1
            
            cipher_pair.append(matrix[(r1+1)][c1]+matrix[(r2+1)][c2])

        else:
            cipher_pair.append(matrix[r1][c2]+matrix[r2][c1])

    return cipher_pair

def preprocess_input(name):
    lst = [ch.lower() for ch in name]

    lst.remove(' ')

    return ''.join(lst[-6:])

name = input("Enter ur name:")

if len(name)<6:
    print("Please enter the name with more than 6 characters")
    name = input('Name:')

key = preprocess_input(name)

print(key)

message = input("Message:")

matrix = create_matrix(key)
message_pairs = generate_pairs(message)

cipher = generate_playfair_cipher(matrix,message_pairs)

print(cipher)