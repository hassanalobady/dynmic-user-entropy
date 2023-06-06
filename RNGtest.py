import random
import tkinter as tk
from tkinter import messagebox
from Crypto.Util.number import getPrime

class ShamirSecretSharing:
    def __init__(self, num_players, threshold):
        self.num_players = num_players
        self.threshold = threshold
        self.prime = getPrime(256)

    def generate_shares(self, secret):
        coefficients = [random.randint(1, self.prime - 1) for _ in range(self.threshold - 1)]
        shares = []

        for player in range(1, self.num_players + 1):
            share = secret

            for exp in range(1, self.threshold):
                share += coefficients[exp - 1] * pow(player, exp, self.prime)

            shares.append((player, share))

        return shares

class ElGamalHomomorphicEncryption:
    def __init__(self):
        self.prime = getPrime(256)
        self.generator = 2

    def encrypt(self, public_key, plaintext):
        y = random.randint(2, self.prime - 1)
        c1 = pow(self.generator, y, self.prime)
        s = pow(public_key, y, self.prime)
        c2 = (plaintext * s) % self.prime
        return (c1, c2)

    def decrypt(self, private_key, ciphertext):
        c1, c2 = ciphertext
        s = pow(c1, private_key, self.prime)
        s_inv = pow(s, -1, self.prime)
        plaintext = (c2 * s_inv) % self.prime
        return plaintext

class SchnorrSignatures:
    def __init__(self):
        self.prime = getPrime(256)
        self.generator = 2

    def sign(self, private_key, message):
        x = private_key
        k = random.randint(1, self.prime - 2)
        r = pow(self.generator, k, self.prime)
        e = int.from_bytes(self._hash_message(r.to_bytes(32, 'big') + message.encode()), 'big')
        s = (k - x * e) % (self.prime - 1)
        return (r, s)

    def verify(self, public_key, signature, message):
        y = public_key
        r, s = signature
        e = int.from_bytes(self._hash_message(r.to_bytes(32, 'big') + message.encode()), 'big')
        v1 = pow(self.generator, s, self.prime)
        v2 = (pow(y, e, self.prime) * pow(r, self.prime - 1 - s, self.prime)) % self.prime
        return v1 == v2

    def _hash_message(self, message):
        return hashlib.sha256(message).digest()

class MilliMixProtocol:
    @staticmethod
    def mix(shares):
        # Placeholder for actual mixing functionality
        return shares

class SecureRandomNumberGenerator:
    def __init__(self, num_players, threshold, min_value, max_value):
        self.num_players = num_players
        self.threshold = threshold
        self.min_value = min_value
        self.max_value = max_value
        self.sss = ShamirSecretSharing(num_players, threshold)
        self.elgamal = ElGamalHomomorphicEncryption()
        self.schnorr = SchnorrSignatures()

    def generate_random_number(self):
        secret = random.randint(self.min_value, self.max_value)
        shares = self.sss.generate_shares(secret)
        public_key = random.randint(2, self.elgamal.prime - 1)
        encrypted_shares = [self.elgamal.encrypt(public_key, share[1]) for share in shares]
        mixed_shares = MilliMixProtocol.mix(encrypted_shares)
        decrypted_shares = [self.elgamal.decrypt(public_key, mixed_share) for mixed_share in mixed_shares]
        reconstructed_secret = sum(decrypted_shares) % self.elgamal.prime
        random_num = (reconstructed_secret % (self.max_value - self.min_value + 1)) + self.min_value
        return random_num

# User Interface using Tkinter
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("c")
        self.geometry("600x400")

        self.num_players_entry = tk.Entry(self)
        self.num_players_entry.pack(pady=10)
        self.num_players_entry.insert(0, "Number of Players")

        self.threshold_entry = tk.Entry(self)
        self.threshold_entry.pack(pady=10)
        self.threshold_entry.insert(0, "Threshold")

        self.min_value_entry = tk.Entry(self)
        self.min_value_entry.pack(pady=10)
        self.min_value_entry.insert(0, "Minimum Value")

        self.max_value_entry = tk.Entry(self)
        self.max_value_entry.pack(pady=10)
        self.max_value_entry.insert(0, "Maximum Value")

        self.generate_button = tk.Button(self, text="Generate Random Number", command=self.generate_random_number)
        self.generate_button.pack(pady=10)

        self.random_num_label = tk.Label(self, text="Random Number: ")
        self.random_num_label.pack(pady=10)

    def generate_random_number(self):
        try:
            num_players = int(self.num_players_entry.get())
            threshold = int(self.threshold_entry.get())
            min_value = int(self.min_value_entry.get())
            max_value = int(self.max_value_entry.get())

            rng = SecureRandomNumberGenerator(num_players, threshold, min_value, max_value)
            random_num = rng.generate_random_number()
            self.random_num_label.configure(text="Random Number: " + str(random_num))
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    app = Application()
    app.mainloop()

