def lab_rot_cipher():
  import string
  letters = string.ascii_lowercase
  upper = string.ascii_uppercase
  other = string.digits + string.punctuation
  passphrase = input('enter the phrase to be encrypted: \n')
  passphraselist = list(passphrase)
  encryptedlist = []
  rot = 13
  rotplus = 0
  response = input(
      'would you like to specify the number of rotations (y/n): \n')
  if response == 'y':
    rotplus = input('enter the number: \n')
    rotplus = int(rotplus)
    rot += rotplus
    if rot // 26 == 1:
      rot -= rotplus
      print('disregarded input as the encrypted phrase would identical to the original phrase')
  for char in passphraselist:
    if char in letters:
      index = letters.find(char)
      index += rot
      if index > 25:
        index -= 26
      echar = upper[index]
    elif char in upper:
      index = upper.find(char)
      index += rot
      if index > 25:
        index -= 26
      echar = letters[index]
    elif char in other:
      index = other.find(char)
      index += 21 + rotplus
      if index > 41:
        index -= 42
      echar = other[index]
    else:
      echar = char
    encryptedlist.append(echar)
  passphrase = ''
  encryptedphrase = ''
  for char in passphraselist:
    passphrase += char
  for char in encryptedlist:
    encryptedphrase += char
  result = f'encrypted "({passphrase})" using rot {rot}+{rotplus}\n resulting in "({encryptedphrase})"'
  print(result)
  return result
