from random import randint

def generator(g, x, p):
    return pow(g, x) % p

def prime_finder(a):
  a_p = []
  for i in range(a-10,a+10):
    if(is_prime(i)):
      a_p.append(i)
  return a_p

def encrypt(cipher, key):
    semi_cipher = []
    for char in cipher:
      l = (char / key/311)
      if(not l.is_integer()):
        return 0
      semi_cipher.append(int(l))
    return semi_cipher

def dynamic_xor_encrypt(semi_cipher, text_key):
    plain_text = ""
    key_length = len(text_key)
    for i in range(len(semi_cipher)):
        key_char = text_key[i % key_length]
        encrypted_char = chr(semi_cipher[i] ^ ord(key_char))
        plain_text += encrypted_char
    return plain_text[::-1]

def main(a,b,cipher,textkey):
  p = prime_finder(a)
  g = prime_finder(b)
  secret_key = []
  semi_cipher = []
  for i in p:
    for j in g:
      u = generator(j, a, i)
      v = generator(j, b, i)
      key = generator(v, a, i)
      b_key = generator(u, b, i)
      if key == b_key:
        secret_key.append(key)

  for i in secret_key:
    l = encrypt(cipher, i)
    if(l):
      semi_cipher.append(l)
  for i in semi_cipher:
    text = dynamic_xor_encrypt(i, textkey)
    print(text[::-1])

a = 90
b = 26
cipher = [61578, 109472, 437888, 6842, 0, 20526, 129998, 526834, 478940, 287364, 0, 567886, 143682, 34210, 465256, 0, 150524, 588412, 6842, 424204, 164208, 184734, 41052, 41052, 116314, 41052, 177892, 348942, 218944, 335258, 177892, 47894, 82104, 116314]
textkey = "trudeau"
main(a,b,cipher,textkey)
