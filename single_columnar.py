import math
msg =input("Enter message : ")
key =input("Enter a key : ")

# Encryption
def encryptMessage(msg):
 cipher = ""

 # track key indices
 key_pos = 0

 msg_len = float(len(msg))
 msg_list = list(msg)
 key_list = sorted(list(key))

 # calculate column of the matrix
 col = len(key)

 # calculate maximum row of the matrix
 row = int(math.ceil(msg_len / col))

 # add the padding character '_' in empty
 # the empty cell of the matix
 fill_null = int((row * col) - msg_len)
 msg_list.extend('_' * fill_null)

 # create Matrix and insert message and
 # padding characters row-wise
 matrix = [msg_list[i: i + col]
	 for i in range(0, len(msg_list), col)]

 # read matrix column-wise using key
 for _ in range(col):
	curr_idx = key.index(key_list[key_pos])
 	cipher += ''.join([row[curr_idx]
		 for row in matrix])
 	key_pos += 1

 return cipher

# Decryption
def decryptMessage(cipher):
 msg = ""

 # track key indices
 key_pos = 0

 # track msg indices
 msg_indx = 0
 msg_len = float(len(cipher))
 msg_list = list(cipher)

 # calculate column of the matrix
 col = len(key)

 # calculate maximum row of the matrix
 row = int(math.ceil(msg_len / col))

 # convert key into list and sort
 # alphabetically so we can access
 # each character by its alphabetical position.
 key_list = sorted(list(key))

 # create an empty matrix to
 # store deciphered message
 dec_cipher = []
 for _ in range(row):
      dec_cipher += [[None] * col]

 # Arrange the matrix column wise according
 # to permutation order by adding into new matrix
 for _ in range(col):
       curr_idx = key.index(key_list[key_pos])

 for j in range(row):
      dec_cipher[j][curr_idx] = msg_list[msg_indx]
      msg_indx += 1
 key_pos += 1

 # convert decrypted msg matrix into a string
 try:
       msg = ''.join(sum(dec_cipher, []))
 except TypeError:
       raise TypeError("This program cannot",
 "handle repeating words.")

 fill_null_count = msg.count('_')

 if fill_null_count > 0:
 return msg[: -fill_null_count]

 return msg

# Driver Code
cipher = encryptMessage(msg)
print("Encrypted Message:",cipher)
cipher = decryptMessage(cipher)
print("Decryped Message:",cipher)