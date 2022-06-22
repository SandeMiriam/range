 #given a string ("childrenplayinginpayground"),print half of the sentence to uppercase.
sentence=("childrenplayinginpayground")
splitting=len(sentence)//2
sentence1=(sentence[0:splitting]).upper()
sentence2=(sentence[splitting:]).lower()
print(sentence1+sentence2)