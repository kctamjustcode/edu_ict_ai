import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.chain[-1]['index'] + 1  # seems unnecessary

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


    # Here’s how you can implement it:
    def proof_of_work(self, last_proof):    # includ hash value?
        proof = 0
        while not self.valid_proof(last_proof, proof):
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):     # includ hash value?
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
    
    @staticmethod
    def valid_proof_last_hash(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash

### sample use-case
blkchn = Blockchain()
print('# genesis block: ', blkchn.chain)
print('# genesis block proof: ', blkchn.chain[0]['proof'])
print('# genesis block transaction: ', blkchn.current_transactions)
blkchn.new_transaction('testing','testing', 0)
print('# after transaction: ', blkchn.chain)
print('# blkchn new transaction stored', blkchn.current_transactions)

new_proof = blkchn.proof_of_work(blkchn.chain[-1]['proof'])
print('# generating new proof from last proof: ', new_proof)

blkchn.new_block(new_proof) # DO NOT USE: blkchn.new_block(new_proof, blkchn.chain[-1]['previous_hash'])
print('# new block: ', blkchn.chain[-1])

'''
new_hash = blkchn.hash(blkchn.chain[-1])
print("# generating new_hash using new block: ", new_hash)
blkchn.chain[-1]['previous_hash'] = new_hash
print('# amending hash value of new block: ', blkchn.chain[-1]['previous_hash'])
print(blkchn.chain)
# print(blkchn.chain[1]['proof'])
'''

'''
# print(blkchn.valid_proof(100, 35293))
# print(blkchn.valid_proof_last_hash(100, 35293))

blkchn.new_block(blkchn.proof_of_work(blkchn.chain[-1]['proof'], ))
print('# new block: ', blkchn.chain[-1])
            
blkchn.new_block(blkchn.proof_of_work(blkchn.chain[-1]['proof'], ))
print('# new block: ', blkchn.chain[-1])

# print(blkchn.valid_proof(100, 35293))
# print(blkchn.valid_proof(35293, 35089))
# print(blkchn.valid_proof(35089, 119678))
'''