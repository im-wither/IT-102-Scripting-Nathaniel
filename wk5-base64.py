import base64

def encode(i):
    i_utf = i.encode('utf-8')
    i_b64 = base64.b64encode(i_utf)
    print("Base64 Encoded Text: ", i_b64)
    i_decoded = base64.b64decode(i_b64)
    #print("b64 decoded is", i_decoded)
    i_decoded_plain = i_decoded.decode('utf-8')
    print('Base 64 Decoded Text', i_decoded_plain)
    
    if i == i_decoded_plain:
        print("Decoded output matches inital prompt!")
    else:
        print('There is a mismatch...')




prompt = input("Enter your plaintext message: ")
encode(prompt)
