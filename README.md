## Secure Random Number Generator

This project implements a dynmic user entropy for Secure Random Number Generation in Distributed Adversarial Card Games. you can find the whitepaper in their website. 
The cryptography primitives used in this RNG are combination of SSS [1],  ElGamal Homomorphic Encryption [2] , Schnorr Singatures [3] and Millimix [4].



### High-level overview 

![image](https://github.com/hassanalobady/dynmic-user-entropy/assets/19050553/04664c44-2526-4b62-9aab-bae9c8c66001)



![image](https://github.com/hassanalobady/dynmic-user-entropy/assets/19050553/b3b9384a-3e1f-4662-bd51-f565c2203396)

### Secure Random Number Generation:
      1) Use the input data from the user interface to configure the secure random number generation process.
      2) Implement the SSS algorithm to split the secret (random number) into shares among the players.
      3) Distribute the shares securely to each player in the game.
      4)  Use ElGamal homomorphic encryption to encrypt the shares received from SSS.
      4) Share the encrypted shares among the players.
      5) Implement the Millimix protocol to securely mix the encrypted shares among the players.
      6) Decrypt the mixed shares using the players' ElGamal private keys.
      7) Combine the decrypted shares using the SSS algorithm to obtain the random number for the game.

 ### Schnorr Signatures:
        1) Generate Schnorr key pairs for each player in the game.
        2) Use Schnorr signatures to verify the authenticity of players' moves or actions during the game.
        3) Integrate Schnorr signatures as part of the game's integrity checks.

    
### Game Logic and Interaction:

        1) Integrate the secure random number generation into the game logic.
        2) Use the random number for fair card dealing, determining turn order, or resolving game outcomes.
        3) Implement rules and mechanisms to prevent cheating or unfair practices during gameplay.
        4) Validate moves and actions using Schnorr signatures to ensure integrity.
        5) Update the user interface to reflect the game state, player actions, and random number generation.

#### Run this project

python3 RNGtest.py

# Example usage
num_players = 5
threshold = 3
min_value = 1
max_value = 100


### References 
[1]. Pedersen, T. P. (2001, May). Non-interactive and information-theoretic secure verifiable secret sharing. In Advances in Cryptology—CRYPTO’91: Proceedings (pp. 129-140). Berlin, Heidelberg: Springer Berlin Heidelberg.
[2]. ElGamal, T. (1985). A public key cryptosystem and a signature scheme based on discrete logarithms. IEEE transactions on information theory, 31(4), 469-472.

[3]. Schnorr, C. P. (1990). Efficient identification and signatures for smart cards. In Advances in Cryptology—CRYPTO’89 Proceedings 9 (pp. 239-252). Springer New York.

[4]. Jakobsson, M., & Juels, A. (1999). Millimix: Mixing in small batches. DIMACS Technical 

