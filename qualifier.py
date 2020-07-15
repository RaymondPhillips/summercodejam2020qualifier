"""
Use this file to write your solution for the Summer Code Jam 2020 Qualifier.

Important notes for submission:

- Do not change the names of the two classes included below. The test suite we
  will use to test your submission relies on existence these two classes.

- You can leave the `ArticleField` class as-is if you do not wish to tackle the
  advanced requirements.

- Do not include "debug"-code in your submission. This means that you should
  remove all debug prints and other debug statements before you submit your
  solution.
"""
from collections import Counter
import datetime
import typing


class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    def __init__(self, field_type: typing.Type[typing.Any]):
        pass


class Article:
    """The `Article` class you need to write for the qualifier."""
    title = ''
    author = ''
    publication_date = ''
    content = ''

    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
      self.title = title
      self.author = author
      self.publication_date = publication_date
      self.content = content

    def __repr__(self):
      return '<Article title="{title}" author=\'{author}\' publication_date=\'{date}\'>'.format(title = self.title, author = self.author, date = self.publication_date.isoformat())
    
    def __len__(self):
      return len(self.content)

    def short_introduction(self, n_characters: int):
      newStr = self.content[:n_characters]
      period = newStr.rfind('.',0)
      space = newStr.rfind(' ',0)
      if period > space:
        return newStr[:period+1]
      else:
        return newStr[:space]
      return newStr

    def most_common_words(self, n_words: int):
      str = self.content.lower()
      wordList2 =[]
      wordList1 = str.split()
      for word in wordList1:
          cleanWord = ""
          for char in word:
              if char in '!\',.?":;0123456789@#$%^&*()\{\}[]\\></|_-+=`~':
                  char = ""
              cleanWord += char
          wordList2.append(cleanWord)

      str_list = wordList2
      most_occur = Counter(str_list).most_common(n_words)
      common = {}
      first = []
      second = []

      for a_tuple in most_occur:
        first.append(a_tuple[0])
      for b_tuple in most_occur:
        second.append(b_tuple[1])
      for key in first: 
        for value in second: 
          common[key] = value 
          second.remove(value) 
          break  
      return common
      
