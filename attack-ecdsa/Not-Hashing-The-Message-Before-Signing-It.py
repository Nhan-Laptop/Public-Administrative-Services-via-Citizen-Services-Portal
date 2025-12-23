from ecdsa import SigningKey, NIST256p

sign_key = SigningKey.generate(NIST256p)
verifying_key = sign_key.verifying_key

class MyHash:
    def __init__(self, data):
        self.data = data

    def digest(self):
        return self.data

message = r"""
Please transfer 1 million from my account.
Beneficiary: Hoang
Purpose: Living expenses
"""
signature = sign_key.sign(message.encode(), hashfunc=MyHash)
assert verifying_key.verify(signature, message.encode(), hashfunc=MyHash)

new_message = r"""
Please transfer 1 million from my account.
Beneficiary: Hoang
Purpose: Living expenses
Additional transfer: 10 million to Trang
"""
assert verifying_key.verify(signature, new_message.encode(), hashfunc=MyHash)
print("success!")
