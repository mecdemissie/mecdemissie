import hashlib
import json
import time

class Block:
    def __init__(self, block_number, data, location, device_name, energy, nonce=0, prev_hash=" ",
                 timestamp=None):
        self.block_number = block_number
        self.data = data
        self.timestamp = timestamp or time.time()
        self.nonce = nonce
        self.prev_hash = prev_hash
        self.device_name = device_name
        self.energy = energy
        self.location = location
        self.hash = self.calculate_hash()

# create a didgital fingerprint for the block(hash) using sha256

    def calculate_hash(self):
        block_str = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_str.encode()).hexdigest()

    def print_hashes(self):
        print("Previous hash: " + self.prev_hash)
        print("Hash: " + self.hash)

class Blockchain:
    chain = []

    def __int__(self):
        self.chain = []
        self.prev_hash = self.get_last_block()

    def genesis_block(self):
        genesis_block = Block(0, ["First Block"], time.time(), "0", "", "", "")
        genesis_block = genesis_block.calculate_hash()
        self.chain.append(genesis_block)
        return genesis_block

    def get_last_block(self):
        return self.chain[-1]

    def add(self, block):
        self.prev_hash = self.get_last_block()
        self.block = block.calculate_hash()
        if self.verify(block) == False:
            return "Invalid Block... sorry we cannot verify this block"
        elif self.verify(block) == True:
            return self.mine(block)

    def mine(self, block):
        difficulty = 3
        block.nonce = 0
        self.hash = block.calculate_hash()
        while not self.hash.startswith(
                '0' * difficulty):
            block.nonce += 1
            # print(self.hash)
            self.hash = block.calculate_hash()
        self.chain.append(self.hash)
        return "---------------------------------------------" + \
               "\nMined Blocked :" + self.hash + \
               "\nNonce: " + str(block.nonce) + \
               "\nBlock Number: " + str(block.block_number) + \
               "\nData: " + str(block.data) + \
               "\nLocation: " + str(block.location) + \
               "\nEnergy Source: " + str(block.device_name) + \
               "\nEnergy Input: " + str(block.energy) + \
               "\nTime: " + str(time.ctime(block.timestamp)) + \
               "\nPrevious Hash: " + str(self.prev_hash) + \
               "\n "

    def length_chain(self):
        return ("The blockchain length is: " + str(len(self.chain)))

    def index_chain(self):
        l = 0
        while len(self.chain) != l:
            for i in self.chain:
                print("\n Block " + str(l) + ":" + i)
                l+= 1
            return ""

    def verify(self, block):
        flag = True
        return flag

blocks = Blockchain()
blocks.genesis_block()

state = input("Enter the state abbreviation in which you live in: ")
if state == 'GA' or state == 'MD' or state == 'VA' or state == 'DC':
  blockenergy = 6000.00
  choice = 'a'
  num = int(1)
  while choice != 'q' and choice != 'Q':
    print("Team Block has", blockenergy, "kilowatts stored in the bank.")
    print("Enter 1 to Buy")
    print("Enter 2 to Sell")
    print("Enter Q to Quit")
    print("\n")
    choice = str(input("Enter choice: "))
    print("\n")
    if choice == 'q' or choice == 'Q':
      print("Thank you for choosing Team Block!")
      print("\n")
      print(blocks.length_chain())
      print(blocks.index_chain())
    elif choice == '1':
      print("You are now buying energy from Team Block.")
      print("\n")
      data = input("Enter name: ")
      location = input("Enter your city: ")
      device_name = input("What is the energy source you will be using?: ")
      energy = float(input("Enter the amount of energy to be bought (kW): "))
      if energy > blockenergy:
        print("Invalid. Energy preffered is greater than Team Block's energy bank.")
      else:
        blockenergy = blockenergy - energy
        num += 1
        print(blocks.add(Block(num, [data], location, device_name, energy, "")))
        num += 1
      print("\n")
    elif choice == '2':
      print("You are now selling energy to Team Block.")
      print("\n")
      data = input("Enter name: ")
      location = input("Enter your city: ")
      device_name = input("What is the energy source you will be using?: ")
      energy = float(input("Enter the amount of energy to be sold (kW): "))
      blockenergy = blockenergy + energy
      print(blocks.add(Block(num, [data], location, device_name, energy, "")))
      num += 1
      print("\n")

else:
  print("You cannot access Team Block's energy bank.")
