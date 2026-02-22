# 🔗 Module 2, Lesson 3: Domain Names — Decoding URLs!

## 🗺️ Module 2: Addresses & Names | Lesson 3 of 3

---

## 🌟 Your Mission Today

**Mission: Learn to read and decode any URL like a pro!** You'll understand what every part of a web address means — from `https://` to `.com` to everything after the slash! 🕵️🔗

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- 🎯 Identify every part of a **URL**
- 🎯 Explain what a **domain name** is and how it's structured
- 🎯 List common **TLDs** (Top-Level Domains) and what they mean
- 🎯 Read a complex URL and explain what each piece does

---

## 🪝 Hook — What Does This URL Really Say? 🤔

Look at this URL:

```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

You've probably seen URLs like this a thousand times. But do you know what EACH piece means?

- What's the `https://`?
- What's the `www`?
- What's `.com`?
- What's `/watch`?
- What's `?v=dQw4w9WgXcQ`?

By the end of this lesson, you'll be able to break down ANY URL and know exactly what every part does! (And yes, that particular URL is a Rick Roll. You're welcome. 😏🎵)

---

## 🧠 Learning Point 1: What is a URL?

### 📍 The Big Idea

A **URL** (Uniform Resource Locator) is the complete address of something on the Internet. It tells your browser EXACTLY where to go and what to get.

Think of a URL like a complete set of directions:

```
🏠 Real-World Address:
    "Go to the United States, New York City, 5th Avenue, Building 350, Floor 3, Room 302"

🌐 URL Address:
    "Go to the .com domain, youtube server, the /watch page, video dQw4w9WgXcQ"
```

### 🔬 Anatomy of a URL

Let's break down a URL into its parts:

```
    https://www.youtube.com/watch?v=dQw4w9WgXcQ
    ─┬───   ─┬─ ──┬──── ─┬─ ──┬── ─────┬──────
     │       │    │      │    │        │
     │       │    │      │    │        └── Query String (specific video ID)
     │       │    │      │    └─────────── Path (which page)
     │       │    │      └──────────────── TLD (top-level domain)
     │       │    └─────────────────────── Domain Name (which website)
     │       └──────────────────────────── Subdomain (section of the site)
     └──────────────────────────────────── Protocol (the rules for communication)
```

Let's learn about each part! 👇

---

## 🧠 Learning Point 2: The Parts of a URL (Detailed!)

### 🔒 Part 1: The Protocol (`https://`)

The **protocol** tells your browser HOW to communicate with the server.

| Protocol | What It Means | Analogy |
|----------|-------------|---------|
| `http://` | HyperText Transfer Protocol | Sending a postcard (anyone can read it!) 📬 |
| `https://` | HyperText Transfer Protocol **Secure** | Sending a letter in a sealed, locked box 🔒 |

The `s` in `https` means **secure** — your data is **encrypted** (scrambled) so nobody can spy on it!

> 🔑 **Rule of Thumb:** If a website uses `http://` (no "s"), be VERY careful. Never enter passwords or personal information on an `http` site! Always look for `https` and the 🔒 padlock icon!

### 🏠 Part 2: The Subdomain (`www.`)

The **subdomain** is a section of a bigger website. `www` stands for "World Wide Web" and is the most common subdomain, but there are others:

| Subdomain | Example | What It Is |
|-----------|---------|-----------|
| `www` | `www.google.com` | The main website |
| `mail` | `mail.google.com` | Google's email service (Gmail) |
| `maps` | `maps.google.com` | Google Maps |
| `docs` | `docs.google.com` | Google Docs |
| `drive` | `drive.google.com` | Google Drive |

Think of subdomains like **departments** in a big company building:
- The building is `google.com`
- The mail room is `mail.google.com`
- The map department is `maps.google.com`

### 🏢 Part 3: The Domain Name (`youtube`)

The **domain name** is the main name of the website. This is the name someone chose and registered (paid for).

- Google's domain name: `google`
- YouTube's domain name: `youtube`
- Minecraft's domain name: `minecraft`
- Your school might have its own: `myschool`

Domain names must be **unique** — no two websites can have the same domain name with the same TLD!

> 💡 **Fun Fact:** The most expensive domain name ever sold was `cars.com` for **$872 million!** 💰 Others include `insurance.com` ($35.6 million) and `voice.com` ($30 million). Short, common words are worth a fortune!

### 🌍 Part 4: The TLD — Top-Level Domain (`.com`)

The **TLD** (Top-Level Domain) is the ending of a domain name. Here are the most common ones:

| TLD | What It Stands For | Who Uses It | Examples |
|-----|-------------------|-------------|---------|
| `.com` | Commercial | Businesses, general websites | google.com, youtube.com |
| `.org` | Organization | Non-profits, organizations | wikipedia.org, khanacademy.org |
| `.edu` | Education | Schools and universities | mit.edu, harvard.edu |
| `.gov` | Government | Government agencies | nasa.gov, whitehouse.gov |
| `.net` | Network | Internet/tech companies | minecraft.net |
| `.io` | Indian Ocean (but used by tech) | Tech startups and games | itch.io |
| `.gg` | Originally Guernsey island | Gaming communities | discord.gg |

**Country-Code TLDs:** Some countries have their own TLDs!

| TLD | Country | Example |
|-----|---------|---------|
| `.uk` | United Kingdom 🇬🇧 | bbc.co.uk |
| `.jp` | Japan 🇯🇵 | nintendo.co.jp |
| `.de` | Germany 🇩🇪 | bmw.de |
| `.ca` | Canada 🇨🇦 | canada.ca |
| `.au` | Australia 🇦🇺 | abc.net.au |
| `.in` | India 🇮🇳 | google.co.in |

### 📂 Part 5: The Path (`/watch`)

The **path** tells the server which specific page or resource you want. It's like asking for a specific book in a library.

| URL | Path | What It Gets |
|-----|------|-------------|
| `youtube.com/` | `/` | The homepage |
| `youtube.com/watch` | `/watch` | The video player page |
| `youtube.com/trending` | `/trending` | The trending videos page |
| `youtube.com/gaming` | `/gaming` | The gaming section |
| `wikipedia.org/wiki/Cat` | `/wiki/Cat` | The Wikipedia article about cats 🐱 |

### ❓ Part 6: The Query String (`?v=dQw4w9WgXcQ`)

The **query string** sends extra information to the server. It starts with `?` and uses `key=value` pairs.

```
?v=dQw4w9WgXcQ
 │ │
 │ └── The value (the specific video ID)
 └──── The key ("v" means "video")
```

Multiple parameters are separated by `&`:
```
?v=dQw4w9WgXcQ&t=30
 │                │
 │                └── t=30 means "start at 30 seconds"
 └── v=dQw4w9WgXcQ means "this specific video"
```

> 💡 **Key Vocabulary Recap:**
> - **URL** — The full web address of a page
> - **Protocol** — The communication rules (`http` or `https`)
> - **Subdomain** — A section of a website (like `www` or `mail`)
> - **Domain Name** — The main name of the website (like `youtube`)
> - **TLD** — Top-Level Domain, the ending (like `.com`, `.org`, `.edu`)
> - **Path** — Which specific page you want (like `/watch`)
> - **Query String** — Extra info sent to the server (like `?v=abc123`)

---

## 🧠 Learning Point 3: How Domain Names Are Structured

### 📖 Reading a Domain Name — Right to Left!

Fun fact: You should read domain names from **right to left** (just like IP addresses go from general to specific):

```
    www.store.amazon.com
    ───   ────  ─────  ───
     │     │      │     │
     │     │      │     └── TLD (most general)
     │     │      └──────── Domain (the company)
     │     └─────────────── Subdomain (the store section)
     └───────────────────── Subdomain (the web server)
```

It's like a street address read backwards:
```
    Room 5, Building A, 100 Main St, New York
    ─────   ──────────  ──────────  ────────
    Most                            Most
    specific                        general
```

### 🌳 Domain Name Hierarchy

```
                    . (ROOT)
                   / | \
                 /   |   \
              .com  .org  .net
              / \     |
         amazon google wikipedia
          / \     \
      www store  mail
```

---

## 🎮 Activity 1: URL Decoder Challenge! (+25 XP)

### 📋 Instructions

Break down each URL into its parts! Fill in the table:

**URL 1:** `https://www.minecraft.net/en-us/store`

| Part | Your Answer |
|------|-------------|
| Protocol | _______________ |
| Subdomain | _______________ |
| Domain Name | _______________ |
| TLD | _______________ |
| Path | _______________ |

**URL 2:** `https://mail.google.com/mail/inbox`

| Part | Your Answer |
|------|-------------|
| Protocol | _______________ |
| Subdomain | _______________ |
| Domain Name | _______________ |
| TLD | _______________ |
| Path | _______________ |

**URL 3:** `https://en.wikipedia.org/wiki/Internet`

| Part | Your Answer |
|------|-------------|
| Protocol | _______________ |
| Subdomain | _______________ |
| Domain Name | _______________ |
| TLD | _______________ |
| Path | _______________ |

**URL 4:** `https://www.youtube.com/results?search_query=cute+cats`

| Part | Your Answer |
|------|-------------|
| Protocol | _______________ |
| Subdomain | _______________ |
| Domain Name | _______________ |
| TLD | _______________ |
| Path | _______________ |
| Query String | _______________ |

<details>
<summary>🔑 Click for answers!</summary>

**URL 1:** `https://www.minecraft.net/en-us/store`
- Protocol: `https`
- Subdomain: `www`
- Domain: `minecraft`
- TLD: `.net`
- Path: `/en-us/store`

**URL 2:** `https://mail.google.com/mail/inbox`
- Protocol: `https`
- Subdomain: `mail`
- Domain: `google`
- TLD: `.com`
- Path: `/mail/inbox`

**URL 3:** `https://en.wikipedia.org/wiki/Internet`
- Protocol: `https`
- Subdomain: `en` (English language version)
- Domain: `wikipedia`
- TLD: `.org`
- Path: `/wiki/Internet`

**URL 4:** `https://www.youtube.com/results?search_query=cute+cats`
- Protocol: `https`
- Subdomain: `www`
- Domain: `youtube`
- TLD: `.com`
- Path: `/results`
- Query String: `?search_query=cute+cats`

</details>

---

## 🎮 Activity 2: Design Your Own Domain! (+25 XP)

### 📋 Instructions

Imagine you're starting your own website! Design 3 domain names for these scenarios:

**Scenario 1:** You're creating a website where kids can share their drawings and art.
- Your domain name: ___________________
- TLD you'd choose: ___________________
- Full URL: `https://www.____________.____`
- Why did you choose this name? ___________________

**Scenario 2:** You're building an educational website about space and planets.
- Your domain name: ___________________
- TLD you'd choose: ___________________
- Full URL: `https://www.____________.____`
- Why? ___________________

**Scenario 3:** You're starting a non-profit organization to help rescue animals.
- Your domain name: ___________________
- TLD you'd choose: ___________________
- Full URL: `https://www.____________.____`
- Why? (Hint: What TLD is best for non-profits?) ___________________

**Bonus (+15 XP):** Design a complete URL with a path AND query string! For example, if your art website has a gallery page showing cat drawings:

```
https://www.____________.____/gallery?category=____________&sort=____________
```

---

## 🎮 Activity 3: TLD Matching Game! (+25 XP)

### 📋 Instructions

Match each website to the **most appropriate TLD**! Draw a line (or write the letter):

| Website | | Best TLD |
|---------|---|---------|
| 1. A school's homework portal | | A. `.com` |
| 2. A new video game store | | B. `.org` |
| 3. A charity helping homeless pets | | C. `.edu` |
| 4. NASA's website | | D. `.gov` |
| 5. A coding tutorial site for kids | | E. `.net` |
| 6. A British news website | | F. `.co.uk` |
| 7. A Japanese gaming company | | G. `.co.jp` |
| 8. An Internet service provider | | H. `.io` |
| 9. A tech startup's app | | I. `.gg` |
| 10. A gaming community Discord link | | J. `.gov` |

<details>
<summary>🔑 Answers</summary>

1. → **C** `.edu` (educational institution)
2. → **A** `.com` (commercial business)
3. → **B** `.org` (non-profit organization)
4. → **D** `.gov` (government agency)
5. → **A** `.com` or **H** `.io` (both are common for tech/coding sites)
6. → **F** `.co.uk` (British website)
7. → **G** `.co.jp` (Japanese company)
8. → **E** `.net` (network/Internet company)
9. → **H** `.io` (tech startup)
10. → **I** `.gg` (gaming community)

</details>

---

## ⚡ Quick Quiz — Earn Bonus XP! (+10 XP each)

**Question 1:** In the URL `https://www.example.com/about`, what is `about`?
- A) The domain name
- B) The TLD
- C) The path
- D) The protocol

<details>
<summary>Answer</summary>

**C) The path!** The path tells the server which specific page you want.
</details>

---

**Question 2:** What does TLD stand for?
- A) Top-Level Domain
- B) The Last Domain
- C) Total Link Destination
- D) Temporary Loading Data

<details>
<summary>Answer</summary>

**A) Top-Level Domain!** TLDs are the endings like `.com`, `.org`, `.edu`, `.net`, etc.
</details>

---

**Question 3:** In `https://mail.google.com`, what is `mail`?
- A) The TLD
- B) The domain name
- C) The subdomain
- D) The query string

<details>
<summary>Answer</summary>

**C) The subdomain!** `mail` is a subdomain of `google.com`. It's like a department within Google.
</details>

---

## 🏅 Lesson Complete!

### 🎉 You're a URL Master! You now know:

- ✅ Every part of a URL: protocol, subdomain, domain, TLD, path, query string
- ✅ Common TLDs and what they mean (`.com`, `.org`, `.edu`, `.gov`, etc.)
- ✅ How domain names are structured (read them right to left!)
- ✅ How to design your own domain name!

### ⭐ XP Earned This Lesson

| Activity | XP |
|----------|----|
| 📖 Reading the lesson | +25 XP |
| 🎮 Activity 1: URL Decoder | +25 XP |
| 🎮 Activity 2: Design Your Domain | +25 XP |
| 🎮 Activity 3: TLD Matching | +25 XP |
| ⚡ Quiz (3 questions) | +30 XP |
| 💡 Bonus challenge | +15 XP |
| **Total possible** | **145 XP** |

---

## 🏅 MODULE 2 COMPLETE! Badge Earned: 📬 Address Ace!

**Congratulations!** You've completed Module 2: "Addresses & Names" 🎉🎊

You now understand the Internet's entire addressing system:
- IP addresses (the house numbers)
- DNS (the phone book)
- Domain names and URLs (the friendly addresses)

**Don't forget to take the Module 2 Quiz!**

👉 [Module 2 Quiz](quiz_02.md)

---

## 🔍 Coming Up Next...

**Module 3: How Websites Work!** 🖥️

Now that you know how addresses work, it's time to learn what happens when you actually VISIT a website! You'll discover the **client-server model**, **HTTP/HTTPS**, and how your browser turns code into the beautiful pages you see! 🌐✨

👉 [Module 3, Lesson 1: Clients & Servers](../module_03_how_websites_work/lesson_01_clients_and_servers.md)
