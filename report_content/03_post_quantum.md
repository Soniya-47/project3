# Chapter 3: Deep Dive - Post-Quantum Cryptography (2025-2035)

## The Quantum Threat: Harvest Now, Decrypt Later

Quantum computers operate on principles of quantum mechanics (superposition and entanglement), allowing them to solve mathematical problems that are impossible for classical computers. Specifically, Shor's Algorithm can factor large integers exponentially faster than the best known classical algorithms. This capability threatens to break the public-key cryptography (RSA, ECC) that secures the internet, banking systems, and national secrets.

The threat is not theoretical; it is imminent. Nation-states are already executing **"Harvest Now, Decrypt Later" (HNDL)** attacks: intercepting and storing encrypted data today with the intent of decrypting it once a sufficiently powerful quantum computer is available (estimated between 2030-2035).

## Migration Timelines: The Race to 2030

The migration to **Post-Quantum Cryptography (PQC)** is a race against time. The US National Institute of Standards and Technology (NIST) has standardized the first set of PQC algorithms (CRYSTALS-Kyber for key encapsulation, CRYSTALS-Dilithium for digital signatures).

*   **2024-2025:** Initial standardization and pilot programs.
*   **2025-2028:** Hybrid deployments (Classical + PQC) in critical infrastructure and browsers.
*   **2030:** Deprecation of classical algorithms (RSA-2048) by NIST.
*   **2033:** Expected arrival of Cryptographically Relevant Quantum Computers (CRQCs).
*   **2035:** Full global transition to PQC standards.

## QKD vs. PQC Algorithms

Organizations have two primary defense strategies:

1.  **Post-Quantum Cryptography (PQC):** Mathematical algorithms (Lattice-based, Code-based, Multivariate) that are resistant to quantum attacks. This is a software upgrade path and the primary solution for the internet.
2.  **Quantum Key Distribution (QKD):** Using the laws of physics (quantum mechanics) to distribute encryption keys. If an eavesdropper tries to intercept the key, the quantum state collapses, revealing the intrusion. QKD requires specialized hardware and fiber optic networks, making it a niche solution for high-security government and financial links.

## Implementation Challenges

The transition to PQC will be messy and expensive.
*   **Performance Overhead:** PQC keys and signatures are significantly larger than RSA/ECC, causing latency issues for IoT devices and constrained networks.
*   **Legacy Systems:** Billions of embedded devices (smart meters, industrial controllers) cannot support the computational requirements of PQC and must be replaced.
*   **Crypto-Agility:** Organizations must build systems that can swap out cryptographic algorithms on the fly as new vulnerabilities are discovered.

**Future Jobs:** The need for **Quantum Readiness Architects**, **Cryptographic Engineers**, and **QKD Network Specialists** will define the high-end security job market.
