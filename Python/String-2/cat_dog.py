def cat_dog(str):
  dog_count = 0
  cat_count = 0
  for i in range(len(str) -2):
    if(str[i:i+3] == 'dog'):
      dog_count += 1
    elif(str[i:i+3] == 'cat'):
      cat_count += 1
  return True if dog_count == cat_count else False
