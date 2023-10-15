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
        self.S = set()
        
        while len(self.S) < subset_size:
            self.S.add(secrets.choice(range(pk_len)))
        self.S = list(self.S)

        self.C = sum(self.pk[i] for i in self.S) + m

        return self.C

    
