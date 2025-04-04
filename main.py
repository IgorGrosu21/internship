from typing import List, Set
import time

INPUT_FILE = 'sample.txt'

class AnagramList:
  '''
  We store all the words that share the same letters and the set of those letters which is the same for the whole list
  We use encapsulation to combine data - words and letters, in one class
  '''
  
  _words: List[str]
  _letters: Set[str]
  
  def __init__(self, word: str):
    '''
    create the list with the first word and create a set of letters out of it
    '''
    self._words = [word]
    self._letters = set(word)
    
  def is_anagram(self, new_word: str):
    '''
    if new_word letters count is the same of this anagram letters count and the letters also are the same, return True
    '''
    new_letters = set(new_word)
    if len(new_letters) == len(self._letters):
      if new_letters == self._letters:
        return True
    return False
  
  def add_word(self, new_word: str):
    self._words.append(new_word)
    
  def __str__(self):
    return ' '.join(self._words)
          
def main():
  #store the list of anagram groups
  anagram_groups: List[AnagramList] = []
  with open(INPUT_FILE, 'r') as f:
    for line in f.readlines():
      word: str = line.strip()
      #check all anagrams if any shares the same letters, otherwise, create new Anagram List
      for anagram_list in anagram_groups:
        if anagram_list.is_anagram(word):
          anagram_list.add_word(word)
          break
      else:
        anagram_groups.append(AnagramList(word))
  for anagram_list in anagram_groups:
    print(anagram_list)
  
if __name__ == '__main__':
  #time function execution
  start_time = time.time()
  main()
  end_time = time.time()
  print(f'Program executed in {round(end_time - start_time, 5)} seconds')