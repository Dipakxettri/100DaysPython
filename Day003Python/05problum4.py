letter = """ Dear <|Name|>,
          you are selected
          <|Date|>

"""
print(letter.replace("<|Name|>","Deepak").replace("<|Date|>","2024 2 2"))