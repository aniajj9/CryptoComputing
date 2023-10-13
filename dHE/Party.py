import secrets

class Party():
    def __init__(self, bloodtype):
        self.bloodtype = bloodtype

        self.alice_encrypted_blood_type = []
        self.encrypted_result = None

        self.C = 0
        self.S = []
        self.pk = []

    def encrypt(self, m):
        pk_len = len(self.pk)
        subset_size = int(pk_len / 2)

        self.S = [secrets.choice(range(pk_len)) for _ in range(subset_size)]
        self.C = sum(self.pk[i] for i in self.S) + m

        return self.C

    
