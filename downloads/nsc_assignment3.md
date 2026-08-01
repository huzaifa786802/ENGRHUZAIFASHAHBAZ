# Network Security & Cryptography Assignment 3 Solutions

## Question 1: Purpose of S-boxes in DES [10 Marks]

The Substitution boxes (S-boxes) in DES serve several critical purposes:

**Primary Functions:**
- **Non-linear transformation**: S-boxes provide the only non-linear component in DES, making the cipher resistant to linear cryptanalysis
- **Confusion**: They obscure the relationship between plaintext, key, and ciphertext by substituting input bits with different output bits
- **Avalanche effect**: Small changes in input produce significant changes in output
- **Security strength**: S-boxes are the main source of DES's cryptographic strength

**Technical Details:**
- DES uses 8 S-boxes (S1 through S8)
- Each S-box takes 6 bits as input and produces 4 bits as output
- The substitution is based on predetermined lookup tables
- S-boxes compress 48 bits to 32 bits during the f-function

**Security Significance:**
The S-boxes were designed with specific criteria to resist known attacks and provide maximum confusion, making DES secure against differential and linear cryptanalysis techniques available at the time of its design.

---

## Question 2: Comparison of Private Key and Public Key Cryptography [10 Marks]

| Aspect | Private Key Cryptography | Public Key Cryptography |
|--------|-------------------------|-------------------------|
| **Key Structure** | Single shared secret key | Key pair (public + private keys) |
| **Key Distribution** | Secure key exchange required before communication | Public key can be distributed openly |
| **Speed** | Very fast encryption/decryption | Slower due to complex mathematical operations |
| **Scalability** | Poor scalability (n(n-1)/2 keys for n users) | Excellent scalability (2 keys per user) |
| **Key Management** | Difficult key management for large networks | Easier key management |
| **Authentication** | Cannot provide non-repudiation | Provides digital signatures and non-repudiation |
| **Computational Complexity** | Low computational overhead | High computational overhead |
| **Key Length** | Shorter keys (128-256 bits typically) | Longer keys (1024-4096 bits typically) |
| **Primary Use** | Bulk data encryption | Key exchange, digital signatures, small data |
| **Examples** | AES, DES, 3DES, Blowfish | RSA, ECC, Diffie-Hellman, DSA |

---

## Question 3: Achieving Confidentiality with Public Key Cryptography [10 Marks]

Confidentiality in public key cryptography is achieved through the following mechanism:

**Basic Principle:**
- Data encrypted with a public key can only be decrypted with the corresponding private key
- The private key is kept secret by the owner, ensuring only they can decrypt messages

**Process for Confidentiality:**
1. **Key Generation**: Receiver generates a public-private key pair
2. **Public Key Distribution**: Receiver shares their public key openly
3. **Encryption**: Sender encrypts the message using receiver's public key
4. **Transmission**: Encrypted message is sent over insecure channel
5. **Decryption**: Only the receiver can decrypt using their private key

**Mathematical Foundation:**
- Based on mathematical trapdoor functions (easy one way, hard reverse)
- RSA uses integer factorization problem
- ECC uses discrete logarithm problem

**Practical Implementation:**
- Often used in hybrid systems (encrypt symmetric key with public key)
- Ensures that even if communication is intercepted, confidentiality is maintained
- No need for prior secure key establishment between parties

**Security Guarantee:**
Confidentiality is mathematically guaranteed as long as the private key remains secret and the underlying mathematical problem remains computationally infeasible.

---

## Question 4: Achieving Authentication with Public Key Cryptography [10 Marks]

Authentication in public key cryptography is achieved through digital signatures:

**Basic Principle:**
- Data signed with a private key can be verified using the corresponding public key
- Only the private key holder can create valid signatures

**Authentication Process:**
1. **Message Preparation**: Sender creates message to be authenticated
2. **Hash Generation**: Message is hashed using cryptographic hash function
3. **Signature Creation**: Hash is encrypted with sender's private key
4. **Transmission**: Message and signature are sent together
5. **Verification**: Receiver decrypts signature with sender's public key
6. **Authentication**: If decrypted hash matches message hash, authentication succeeds

**Types of Authentication Provided:**
- **Entity Authentication**: Proves identity of the sender
- **Message Authentication**: Ensures message came from claimed sender
- **Non-repudiation**: Sender cannot deny sending the message
- **Integrity**: Ensures message hasn't been tampered with

**Technical Implementation:**
- Common algorithms: RSA signatures, DSA, ECDSA
- Often combined with hash functions (SHA-256, SHA-3)
- May use certificates for public key authentication

**Security Features:**
- Prevents impersonation attacks
- Provides proof of origin
- Enables secure communication without prior shared secrets

---

## Question 5: RSA Encryption/Decryption of 'HELLO' [20 Marks]

Given: p = 12347, q = 181, e = 13

**Step 1: Calculate n and φ(n)**
- n = p × q = 12347 × 181 = 2,234,807
- φ(n) = (p-1)(q-1) = 12346 × 180 = 2,222,280

**Step 2: Calculate private key d**
- d = e⁻¹ mod φ(n)
- Using Extended Euclidean Algorithm: d = 171,329
- Verification: (13 × 171,329) mod 2,222,280 = 1 ✓

**Step 3: Convert 'HELLO' to numeric values**
- H = 72, E = 69, L = 76, L = 76, O = 79

**Step 4: Encryption (C = M^e mod n)**
- H: 72¹³ mod 2,234,807 = 1,317,460
- E: 69¹³ mod 2,234,807 = 1,261,239  
- L: 76¹³ mod 2,234,807 = 1,914,022
- L: 76¹³ mod 2,234,807 = 1,914,022
- O: 79¹³ mod 2,234,807 = 2,065,927

**Encrypted HELLO**: [1317460, 1261239, 1914022, 1914022, 2065927]

**Step 5: Decryption (M = C^d mod n)**
- 1,317,460¹⁷¹'³²⁹ mod 2,234,807 = 72 = H
- 1,261,239¹⁷¹'³²⁹ mod 2,234,807 = 69 = E
- 1,914,022¹⁷¹'³²⁹ mod 2,234,807 = 76 = L
- 1,914,022¹⁷¹'³²⁹ mod 2,234,807 = 76 = L
- 2,065,927¹⁷¹'³²⁹ mod 2,234,807 = 79 = O

**Decrypted result**: HELLO ✓

---

## Question 6: Attacks on Digital Signatures [10 Marks]

**1. Key-Only Attacks:**
- Attacker has access to public key only
- Attempts to forge signatures without additional information

**2. Known Message Attacks:**
- Attacker has valid message-signature pairs
- Tries to forge signatures for new messages

**3. Chosen Message Attacks:**
- Attacker can obtain signatures for chosen messages
- Uses these to forge signatures for other messages

**4. Hash Function Attacks:**
- Collision attacks on underlying hash function
- Birthday attacks to find hash collisions

**5. Implementation Attacks:**
- Side-channel attacks (timing, power analysis)
- Fault injection attacks during signature generation

**6. Man-in-the-Middle Attacks:**
- Interception and modification of signatures
- Public key substitution attacks

**7. Replay Attacks:**
- Reusing valid signatures in different contexts
- Timestamp manipulation

**8. Social Engineering Attacks:**
- Tricking users into signing malicious documents
- Phishing for private keys

---

## Question 7: Merits and Drawbacks of Digital Signatures [10 Marks]

**Merits:**

**Security Benefits:**
- **Non-repudiation**: Signer cannot deny having signed the document
- **Authentication**: Verifies the identity of the signer
- **Integrity**: Ensures document hasn't been tampered with
- **Unforgeable**: Computationally infeasible to forge valid signatures

**Practical Advantages:**
- **Legal validity**: Legally recognized in many jurisdictions
- **Cost-effective**: Reduces paper, printing, and storage costs
- **Speed**: Instant signing and verification
- **Global reach**: Can sign documents remotely
- **Audit trail**: Maintains record of signing process

**Drawbacks:**

**Technical Limitations:**
- **Key management complexity**: Requires secure key storage and management
- **Certificate dependency**: Relies on PKI infrastructure
- **Computational overhead**: Resource-intensive operations
- **Revocation issues**: Difficulty in handling compromised keys

**Practical Challenges:**
- **Technology dependence**: Requires compatible software/hardware
- **User education**: Need for technical understanding
- **Backup concerns**: Risk of losing private keys
- **Interoperability**: Compatibility issues between different systems
- **Long-term validity**: Questions about signature validity over time

---

## Question 8: Criteria of Cryptographic Hash Functions [10 Marks]

**Essential Criteria:**

**1. Deterministic:**
- Same input always produces same hash output
- Ensures consistency and reproducibility

**2. Fixed Output Length:**
- Hash produces fixed-size output regardless of input size
- Enables uniform storage and comparison

**3. Efficient Computation:**
- Fast to compute hash for any input
- Enables practical implementation

**4. Pre-image Resistance (One-way property):**
- Computationally infeasible to find input from hash output
- Given h, finding x where h = hash(x) should be impossible

**5. Second Pre-image Resistance:**
- Given input x₁, infeasible to find different x₂ where hash(x₁) = hash(x₂)
- Prevents targeted collision attacks

**6. Collision Resistance:**
- Infeasible to find any two different inputs with same hash
- Strongest security requirement

**Additional Desirable Properties:**

**7. Avalanche Effect:**
- Small input change causes significant output change
- Enhances security and unpredictability

**8. Uniform Distribution:**
- Hash values should be uniformly distributed
- Prevents clustering and improves security

**9. Pseudorandomness:**
- Output should appear random to statistical tests
- Enhances cryptographic strength

**Security Implications:**
These criteria ensure hash functions are suitable for digital signatures, password storage, integrity verification, and other cryptographic applications. Violation of any criterion can lead to serious security vulnerabilities.