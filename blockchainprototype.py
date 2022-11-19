import hashlib  #LIBRARY FOR GENERATING HASH

#FUNCTION TO CREATE HASH FOR THE BLOCK
def hashGenerator(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()

#CREATING THE BLOCK FOR BLOCKCHAIN
class Block:
    def __init__(self, data, block_hash, prev_hash):
        self.data = data
        self.block_hash = block_hash
        self.prev_hash = prev_hash

class BlockChain:

    #CREATING THE GENESIS BLOCK
    def __init__(self):
        prevHash = hashGenerator('0')
        user_data = input("Enter your message: ")
        blockHash = hashGenerator(user_data)

        genesis = Block(user_data,blockHash,prevHash)
        self.chain = [genesis]

blocknum = 0
while True:
    options = input("\nTO ADD MESSAGE (add/a), TO QUIT (quit/q): ").lower()


    if options == "quit" or options == "q":
        print("Quitting....\n")
        break

    #THIS WILL CREATE NEW BLOCK EACH TIME USER PRESS ON ADD 
    elif options == "add" or options == "a":
        bc = BlockChain()
        blocknum += 1
        for block in bc.chain:

            #PRINTING THE BLOCK NUMBER WITH THE BLOCK DETAILS
            print(f"\nBlock Number = {blocknum}\nYour Added Block Looks like this: {block.__dict__}")

    else:
        print("ENTER A VALID OPTION.")
        continue