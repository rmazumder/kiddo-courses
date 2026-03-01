# Lesson 2: How Bitcoin Works

**Module:** 1 -- What Is Bitcoin?
**Difficulty:** Star-1 Beginner
**Session Time:** 40--50 minutes
**Age:** 10--14 years
**XP Available:** 160 XP

---

## Your Mission Today

Welcome back, Explorer! Last time you learned what money and Bitcoin are. Today you are going DEEPER -- you are going to discover the secret technology behind Bitcoin called the **blockchain**. Think of it like X-ray goggles for Bitcoin! By the end of this lesson, you will understand how Bitcoin keeps track of every transaction without needing a bank. Let's go!

---

## Learning Objectives

By the end of this lesson, you will be able to:
- Explain what a blockchain is using a simple analogy
- Understand how Bitcoin transactions work
- Know what "mining" means (and why it is NOT digging in the ground)
- Build a mini paper blockchain

---

## What You Need

| Item | Qty |
|------|-----|
| Index cards or small pieces of paper | 10--15 |
| Pencil | 1 |
| Tape or glue stick | 1 |
| Dice (any kind) | 1 pair |
| Timer or phone with stopwatch | 1 |

---

## How to Teach This Lesson

### Step 1: Hook -- The Trust Problem (5 min)

Say:
> "Imagine you lend your friend $10. A week later, you ask for it back. Your friend says: 'I already paid you back!' But you know they did not. Who is right? How do you PROVE it?"

Let them think about this. Then ask:
> "What if there was a notebook that EVERYONE in your school could see, and every time anyone gave or received money, it was written down in that notebook? Could your friend lie then?"

(No! Because everyone can see the record.)

> "THAT is basically what the blockchain is -- a notebook that the whole world can see, and nobody can erase or change what is written in it!"

**Award: +15 XP for understanding the trust problem!**

---

### Step 2: The Blockchain Explained (10 min)

**Analogy: A Chain of Notebooks**

> "Imagine a special notebook. Every page records a bunch of transactions -- like 'Alice sent 2 BTC to Bob' and 'Carlos sent 0.5 BTC to Diana.' When a page gets full, it is sealed shut, stamped with a special code, and CHAINED to the previous page. Nobody can rip out a page or change what is written without breaking the whole chain."

```
The Blockchain:

  +-----------+     +-----------+     +-----------+     +-----------+
  | Block #1  |---->| Block #2  |---->| Block #3  |---->| Block #4  |
  |           |     |           |     |           |     |           |
  | Alice->Bob|     | Bob->Carol|     | Carol->Dan|     | Dan->Eve  |
  | 2 BTC     |     | 1 BTC     |     | 0.5 BTC   |     | 3 BTC     |
  |           |     |           |     |           |     |           |
  | Stamp:    |     | Stamp:    |     | Stamp:    |     | Stamp:    |
  | #a1b2c3   |     | #d4e5f6   |     | #g7h8i9   |     | #j0k1l2   |
  +-----------+     +-----------+     +-----------+     +-----------+
       ^                 |                 |                 |
       |    includes     |    includes     |    includes     |
       +--- prev stamp --+--- prev stamp --+--- prev stamp --+
```

**Key vocabulary:**

| Word | Kid-Friendly Definition |
|------|------------------------|
| **Block** | A page in the notebook -- it holds a bunch of transactions |
| **Blockchain** | All the pages chained together in order -- the complete history |
| **Transaction** | A record that says "Person A sent X Bitcoin to Person B" |
| **Hash** | The special stamp/code on each block (like a fingerprint -- unique to that block) |

> "Each block contains the stamp of the PREVIOUS block. So if someone tried to change Block #2, the stamp would not match, and everyone would know something is wrong. It is like a chain -- break one link and the whole thing falls apart!"

**Award: +20 XP for understanding the blockchain concept!**

---

### Step 3: What Is Mining? (8 min)

Say:
> "You might have heard the word 'mining' used with Bitcoin. But nobody is digging underground! Bitcoin mining is actually a COMPETITION."

**The Mining Game analogy:**

> "Imagine thousands of people around the world are all trying to solve a super hard math puzzle at the same time. The first person to solve the puzzle gets to add the next page (block) to the notebook, AND they get rewarded with brand new Bitcoin! That is mining."

```
Mining in a Nutshell:

  Step 1: Collect transactions
  +---------------------------------+
  | "Alice -> Bob: 1 BTC"           |
  | "Carol -> Dan: 0.3 BTC"         |
  | "Eve -> Frank: 2 BTC"           |
  +---------------------------------+

  Step 2: Race to solve the puzzle
  +--------+  +--------+  +--------+
  | Miner  |  | Miner  |  | Miner  |
  |   A    |  |   B    |  |   C    |
  | trying |  | trying |  | GOT IT!|  <-- Winner!
  +--------+  +--------+  +--------+

  Step 3: Winner adds the block + earns Bitcoin reward
  +-----------+
  | New Block |  + Reward: 3.125 BTC (as of 2024)
  +-----------+
```

**Ask:**
> "Why does this matter? Because it means no single person or company controls Bitcoin. Thousands of miners around the world all work together to keep the system running and honest. If one miner tried to cheat, all the others would catch it!"

**Award: +20 XP for understanding mining!**

---

### Step 4: Activity -- Build a Paper Blockchain (12 min)

Say:
> "Now YOU are going to build your own blockchain -- using paper! You are going to be a miner."

**Materials:** 5 index cards, a pencil, tape, and a pair of dice.

**Instructions:**

1. **Write "BLOCK #1 -- GENESIS BLOCK" on the first card.** This is the very first block, just like Bitcoin's first block.
   - Write a transaction: "You found 10 BTC (mining reward)"
   - Roll the dice. Write the number as your "hash" (stamp). Example: rolled 7 = Hash: #007

2. **Create Block #2:**
   - Write "Block #2" at the top
   - Write "Previous Hash: #007" (copy from Block #1)
   - Write a transaction: "You sent 3 BTC to Mom"
   - Roll the dice again for a new hash. Example: rolled 11 = Hash: #011

3. **Create Block #3:**
   - Write "Block #3" at the top
   - Write "Previous Hash: #011" (copy from Block #2)
   - Write a transaction: "Mom sent 1 BTC to Dad"
   - Roll the dice. Example: rolled 4 = Hash: #004

4. **Tape the cards together in a chain** (each card connected to the next).

5. **The tamper test:** Now try to "cheat" -- change the transaction on Block #2. What happens?
   - The hash on Block #2 would change
   - Block #3's "Previous Hash" would no longer match
   - THE CHAIN IS BROKEN! Everyone can see the tampering.

> "This is why the blockchain is so secure. If you change ANYTHING, every block after it breaks. With Bitcoin, thousands of computers are checking this all the time!"

**Award: +35 XP for building your own blockchain!**

---

### Step 5: Bitcoin Wallets and Addresses (5 min)

Say:
> "If Bitcoin is digital, where do you keep it? You keep it in a **wallet** -- but not the kind in your pocket!"

**The email analogy:**

> "A Bitcoin wallet is like an email account. You have an email address that people can send messages to, right? A Bitcoin wallet has an ADDRESS that people can send Bitcoin to. It looks something like this:"

```
A Bitcoin address looks like this:
1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa

(That is actually Satoshi Nakamoto's address -- the very first one ever!)
```

> "You also have a **private key** -- think of it like your email password. You NEVER share your private key with anyone, just like you never share your password!"

| Concept | Analogy | Share It? |
|---------|---------|-----------|
| **Wallet address** | Email address | Yes -- give it to people who want to send you Bitcoin |
| **Private key** | Email password | NEVER -- whoever has this can take your Bitcoin |

**Award: +15 XP for understanding wallets!**

---

### Step 6: Quick Quiz (5 min)

**Question 1:** "What is a blockchain?"
(A chain of blocks, where each block records transactions and is linked to the one before it -- like a notebook everyone can see that nobody can change)
**+10 XP for a correct answer!**

**Question 2:** "What do Bitcoin miners actually do?"
(They compete to solve math puzzles. The winner adds the next block to the blockchain and earns new Bitcoin as a reward)
**+10 XP for a correct answer!**

**Question 3:** "Why is the blockchain so hard to cheat?"
(Because each block contains the stamp/hash of the previous block. If you change one block, all the blocks after it break, and everyone can see it)
**+10 XP for a correct answer!**

**Bonus question:**
> "What is the difference between a wallet address and a private key?"
(A wallet address is like an email address -- you share it so people can send you Bitcoin. A private key is like your password -- you NEVER share it)
**+25 XP bonus!**

---

## Lesson 2 Complete!

```
  =============================================

     BLOCKCHAIN BUILDER BADGE UNLOCKED!

     Skills unlocked:
     [check] Know what a blockchain is
     [check] Understand how Bitcoin transactions work
     [check] Know what mining means
     [check] Built your own paper blockchain!

  =============================================
```

**XP Breakdown:**
| Activity | XP |
|----------|-----|
| Trust problem discussion | 15 |
| Blockchain concept | 20 |
| Understanding mining | 20 |
| Paper blockchain activity | 35 |
| Wallets and addresses | 15 |
| Quiz (3 questions) | 30 |
| Bonus question | 25 |
| **TOTAL POSSIBLE** | **160** |

---

## Coming Up Next...

In **Lesson 3**, you will learn what **trading** actually means! You will discover what BTC/USD means, how buyers and sellers set prices, and you will run your very own trading simulation using cards. Get your trading hat ready!

---

## Navigation

| | |
|:---|---:|
| [Lesson 1: What Is Money and Bitcoin?](lesson_01_what_is_money_and_bitcoin.md) | [Lesson 3: What Is Trading?](lesson_03_what_is_trading.md) |
