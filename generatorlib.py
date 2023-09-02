import hashlib


class GeneratorLib:

    def __init__(self, username: str, pwd_length: int = 32, algo_index: int = 1):
        """
            Instantiates the input parameters required for password generation
        """
        self.username = username
        self.pwd_length_int = int(pwd_length) if (isinstance(pwd_length, int)) else 32
        self.algo_list = {1: "sha256", 2: "sha384", 3: "sha512"}
        self.algo_index = algo_index
        self.algo = self.algo_list[int(self.algo_index)] \
            if (isinstance(self.algo_index, int) and (self.algo_index in range(1, 4))) \
            else self.algo_list[1]
        self.iter = 100000

    def compute_hash(self, iterr=0):
        """
        Recursively computes hash for the given number of iterations

        :iterr: Number of iterations
        """
        self.iter = iterr if (iterr != 0) else self.iter
        hash_val = self.username
        for i in range(0, self.iter):
            hash_val = getattr(hashlib, self.algo)(hash_val.encode('ascii')).hexdigest()
        return hash_val

    def getpassword(self):
        self.pwd_length_int = (int(self.pwd_length_int) - 4) if isinstance(self.pwd_length_int, int) else 28
        pwd_init = self.compute_hash()
        password = (pwd_init[:int(self.pwd_length_int / 2)].lower() +
                    pwd_init[int(self.pwd_length_int / 2):self.pwd_length_int].upper() + "!@#$")
        return password
