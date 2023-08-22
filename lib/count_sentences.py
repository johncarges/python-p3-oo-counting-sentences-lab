#!/usr/bin/env python3

class MyString:
  def __init__(self,value=""):
    self._value = value

  def get_value(self):
    return self._value

  def set_value(self,value):
    if type(value) == str:
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    return True if self._value[-1] == "." else False
  
  def is_question(self):
    return True if self._value[-1] == "?" else False

  def is_exclamation(self):
    return True if self._value[-1] == "!" else False

  def count_sentences(self):
    if self.value == "":
      return 0
    
    newString = ".".join([substring for substring in self.value.split(".") if len(substring) > 0])
    newString = ".".join([substring for substring in newString.split("?") if len(substring) > 0])
    newString = ".".join([substring for substring in newString.split("!") if len(substring) > 0])
    return newString.count(".") + (self.value[-1] in (".","!","?"))

  value = property(get_value,set_value)

  pass
