from uuid import uuid4

from blockchain import Blockchain
from verification import Verification

class Node:
    def __init__(self):
        # self.id = str(uuid4())
        self.id = 'Antonio' # waiting for the wallet
        self.blockchain = Blockchain(self.id)


    def get_transaction_value(self):
        """ Returns the input of the user (a new transaction amount) as a float """
        recipient = input('Enter the recipient of the transaction:')
        amount = float(input('Your transaction amount please: '))
        return recipient, amount  # tuple


    def get_user_choice(self):
        user_input = input('Your choice: ')
        return user_input


    def print_blockchain_elements(self):
        for block in self.blockchain.chain:
            print('Outputting Block')
            print(block)
        else:
            print('-' * 20)


    def listen_for_input(self):
        waiting_for_input = True

        while waiting_for_input:
            print('Please choose: ')
            print('1: Add a new transaction value')
            print('2: Mine a new block')
            print('3: Output the blockchain blocks')
            print('4: Check transaction validity')
            print('h: Manipulate the chain')
            print('q: Quit')
            user_choice = self.get_user_choice()
            if user_choice == '1':
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data  # tuple unpack
                # Add transaction amount to the blockchain
                if self.blockchain.add_transaction(recipient, self.id, amount=amount):
                    print('Added transaction!')
                else:
                    print('Transaction failed!')
                print(self.blockchain.open_transactions)
            elif user_choice == '2':
                self.blockchain.mine_block()
            elif user_choice == '3':
                self.print_blockchain_elements()
            elif user_choice == '4':
                verifier = Verification()
                if verifier.verify_transactions(self.blockchain.open_transactions, self.blockchain.get_balance):
                    print('All transactions are valid')
                else:
                    print('There are invalid transactions')
            elif user_choice == 'q':
                waiting_for_input = False
            else:
                print('Invalid input. Please pick a valid value from the list')
            verifier = Verification()
            if not verifier.verify_chain(self.blockchain.chain):
                self.print_blockchain_elements()
                print('Invalid blockchain!')
                break
            print('Balance of {}: {:6.2f}'.format(self.id, self.blockchain.get_balance()))
        else:
            print('User Left!')


        print('Done!')


node = Node()
node.listen_for_input()