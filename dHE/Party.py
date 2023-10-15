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
        pk_indices = [x for x in range(pk_len)] #new
        subset_size = int(pk_len / 2)

        #self.S = [secrets.choice(range(pk_len)) for _ in range(subset_size)]
        self.S = [x for x in pk_indices if secrets.randbelow(2) == 1] #new

        self.C = sum(self.pk[i] for i in self.S) + m

        return self.C

    
