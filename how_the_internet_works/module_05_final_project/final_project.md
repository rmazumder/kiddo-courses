# 🕵️ Module 5: Final Project — Become an Internet Detective!

## 🏆 The Ultimate Internet Investigation Challenge!

---

## 🌟 Your Mission

**Mission: You are now an Internet Detective!** 🕵️‍♂️ Using everything you've learned in this course — PLUS real terminal commands — you're going to investigate exactly how a website works from the moment you type its name to the moment it appears on your screen.

This is a multi-part investigation where you'll use actual tools that network engineers and cybersecurity professionals use every day!

**This project is worth 500 XP — the biggest XP award in the entire course!** ⭐

---

## 🧰 Tools You'll Use

| Tool | What It Does | Command |
|------|-------------|---------|
| 🔍 `nslookup` | Looks up the IP address of a domain (DNS lookup) | `nslookup domain.com` |
| 📡 `ping` | Sends test packets to a server and measures response time | `ping -c 4 domain.com` |
| 🗺️ `traceroute` | Shows every router a packet passes through on its journey | `traceroute domain.com` (Mac/Linux) or `tracert domain.com` (Windows) |
| 📥 `curl` | Fetches raw data from a web server (like a browser, but in text!) | `curl -I domain.com` |
| 🌐 Browser DevTools | Inspect the HTML, CSS, JS, and network requests | `F12` or `Cmd+Option+I` |

### ⚠️ Important Notes Before You Start

- All these commands are **safe and read-only** — they don't change anything!
- You'll need access to a **Terminal** (Mac/Linux) or **Command Prompt** (Windows)
- If a command doesn't work, try running your terminal as an administrator
- Some networks (school, library) may block certain commands — try at home if needed
- **Ask a parent or teacher** if you need help opening the terminal!

### 🖥️ How to Open Terminal / Command Prompt

| Operating System | How to Open |
|-----------------|-------------|
| 🍎 **Mac** | Spotlight search (Cmd+Space) → type "Terminal" → Enter |
| 🪟 **Windows** | Start menu → search "cmd" or "Command Prompt" → Enter |
| 🐧 **Linux** | Ctrl+Alt+T (or search "Terminal" in applications) |

---

## 📋 Choose Your Target Website

Pick **ONE website** to investigate throughout this entire project. Choose from this list (or pick your own!):

| Suggested Websites | Why It's Interesting |
|-------------------|---------------------|
| 🎮 `minecraft.net` | Popular gaming site with global servers |
| 📺 `youtube.com` | One of the largest websites in the world |
| 📚 `wikipedia.org` | The free encyclopedia, hosted by a non-profit |
| 🔍 `google.com` | The most visited website on Earth |
| 🎵 `spotify.com` | Music streaming with servers worldwide |
| 🏫 Your school's website | See how a local website works! |

📝 **My chosen website:** ________________________

---

## 🔍 Part 1: DNS Investigation (+75 XP)

### 🎯 Goal: Discover the IP address behind your website's domain name!

#### Task 1A: Basic DNS Lookup

Open your terminal and run:

```bash
nslookup YOUR_WEBSITE_HERE
```

Example:
```bash
nslookup minecraft.net
```

📝 **Record your results:**

```
┌──────────────────────────────────────────────┐
│           DNS INVESTIGATION REPORT            │
├──────────────────────────────────────────────┤
│                                              │
│  Website investigated: ___________________   │
│                                              │
│  DNS Server used: ________________________   │
│  (This is YOUR DNS resolver's IP)            │
│                                              │
│  IP Address(es) found:                       │
│  1. ______________________________________   │
│  2. ______________________________________   │
│  3. ______________________________________   │
│                                              │
│  Is it IPv4 or IPv6? ____________________    │
│                                              │
└──────────────────────────────────────────────┘
```

#### Task 1B: Multiple DNS Lookups

Run `nslookup` for 3 MORE websites and compare the results:

```bash
nslookup google.com
nslookup youtube.com
nslookup wikipedia.org
```

📝 **Comparison Table:**

| Website | IP Address | Same or Different DNS Server? |
|---------|-----------|------------------------------|
| (Your main site) | _______________ | _______________ |
| google.com | _______________ | _______________ |
| youtube.com | _______________ | _______________ |
| wikipedia.org | _______________ | _______________ |

#### Task 1C: Analysis Questions

Answer these questions based on your DNS investigation:

1. Did your website return ONE IP address or MULTIPLE? Why do you think that is?
   📝 _______________________________________________________________

2. Did `google.com` and `youtube.com` have similar IP addresses? Why might that be? (Hint: Who owns YouTube?)
   📝 _______________________________________________________________

3. What was the DNS server IP that appeared? Do you know whose DNS server this is?
   📝 _______________________________________________________________

---

## 📡 Part 2: Ping Test — Measuring Speed! (+75 XP)

### 🎯 Goal: Measure how fast your computer can communicate with the server!

#### Task 2A: Ping Your Website

```bash
# Mac/Linux:
ping -c 10 YOUR_WEBSITE_HERE

# Windows:
ping -n 10 YOUR_WEBSITE_HERE
```

This sends 10 test packets and measures the round-trip time!

📝 **Record your results:**

```
┌──────────────────────────────────────────────┐
│           PING TEST REPORT                    │
├──────────────────────────────────────────────┤
│                                              │
│  Website: ________________________________   │
│  IP Address: _____________________________   │
│                                              │
│  Packets sent: 10                            │
│  Packets received: _______                   │
│  Packets lost: _______                       │
│  Packet loss: _______  %                     │
│                                              │
│  Minimum time: _______ ms                    │
│  Maximum time: _______ ms                    │
│  Average time: _______ ms                    │
│                                              │
└──────────────────────────────────────────────┘
```

#### Task 2B: Ping Speed Comparison

Ping websites that you think are NEAR and FAR from your location:

```bash
# Something nearby (your country):
ping -c 5 google.com

# Something far away:
ping -c 5 bbc.co.uk

# Something very far away:
ping -c 5 japan.go.jp
```

📝 **Speed Comparison:**

| Website | Location (Guess) | Average Ping (ms) | Fast or Slow? |
|---------|-----------------|-------------------|---------------|
| Your main site | _______________ | _______ ms | _______________ |
| google.com | _______________ | _______ ms | _______________ |
| bbc.co.uk | UK 🇬🇧 | _______ ms | _______________ |
| japan.go.jp | Japan 🇯🇵 | _______ ms | _______________ |

#### Task 2C: Analysis Questions

1. Which website had the LOWEST (fastest) ping? Why?
   📝 _______________________________________________________________

2. Which had the HIGHEST (slowest) ping? Why?
   📝 _______________________________________________________________

3. Was there any packet loss? What might cause that?
   📝 _______________________________________________________________

4. If you're a gamer: what ping time would you consider "laggy" for online gaming?
   📝 _______________________________________________________________

---

## 🗺️ Part 3: Traceroute — Map the Journey! (+100 XP)

### 🎯 Goal: See every router your data passes through on its way to the server!

#### Task 3A: Trace the Route

```bash
# Mac/Linux:
traceroute YOUR_WEBSITE_HERE

# Windows:
tracert YOUR_WEBSITE_HERE
```

> ⚠️ This might take 30-60 seconds to complete! Some steps might show `* * *` — that means the router didn't respond (it's hiding!).

📝 **Record your traceroute:**

```
┌──────────────────────────────────────────────────┐
│           TRACEROUTE MAP                          │
├──────────────────────────────────────────────────┤
│                                                  │
│  Destination: ________________________________   │
│  Total hops: ___________                         │
│                                                  │
│  Hop 1: _______________________________________  │
│  Hop 2: _______________________________________  │
│  Hop 3: _______________________________________  │
│  Hop 4: _______________________________________  │
│  Hop 5: _______________________________________  │
│  ...                                             │
│  Final: _______________________________________  │
│                                                  │
│  Total time: _________ ms                        │
│                                                  │
└──────────────────────────────────────────────────┘
```

#### Task 3B: Draw Your Route Map!

On a piece of paper (or digitally), draw a map showing the journey of your packet:

1. 🖥️ Start at YOUR computer
2. 📡 Draw your home router (Hop 1)
3. 🏢 Draw your ISP (Hops 2-4, probably)
4. 🌐 Draw the Internet backbone routers (middle hops)
5. 🖥️ End at the destination server (final hop)

Label each hop with its name (if shown) and the time it took!

#### Task 3C: Analysis Questions

1. How many hops (routers) did your data pass through?
   📝 _______________________________________________________________

2. Can you identify which hop was your home router? (Hint: it's usually the first one, often `192.168.x.x` or `10.x.x.x`)
   📝 _______________________________________________________________

3. Can you identify your ISP in the traceroute? (Look for familiar company names)
   📝 _______________________________________________________________

4. Did any hops show `* * *`? What does that mean?
   📝 _______________________________________________________________

---

## 📥 Part 4: HTTP Headers — Talk to the Server! (+100 XP)

### 🎯 Goal: See the raw HTTP response headers from the server!

#### Task 4A: Fetch HTTP Headers

The `curl` command with `-I` flag fetches ONLY the headers (not the whole page):

```bash
curl -I https://YOUR_WEBSITE_HERE
```

Example:
```bash
curl -I https://www.google.com
```

📝 **Record the key headers:**

```
┌──────────────────────────────────────────────┐
│           HTTP RESPONSE HEADERS               │
├──────────────────────────────────────────────┤
│                                              │
│  Website: ________________________________   │
│                                              │
│  Status Code: ____________                   │
│  (What does this status code mean?)          │
│  ________________________________________    │
│                                              │
│  Server: _________________________________   │
│  (What web server software is it running?)   │
│                                              │
│  Content-Type: ___________________________   │
│  (What type of content is being sent?)       │
│                                              │
│  Date: ___________________________________   │
│  (When did the server respond?)              │
│                                              │
│  Any other interesting headers?              │
│  ________________________________________    │
│  ________________________________________    │
│                                              │
└──────────────────────────────────────────────┘
```

#### Task 4B: Compare HTTP vs HTTPS

```bash
curl -I http://YOUR_WEBSITE_HERE
curl -I https://YOUR_WEBSITE_HERE
```

📝 **Comparison:**

| Feature | HTTP (no S) | HTTPS (with S) |
|---------|-------------|----------------|
| Status code | _______________ | _______________ |
| Did it redirect? | _______________ | _______________ |
| Server header | _______________ | _______________ |

Did the HTTP version redirect to HTTPS? (Hint: Look for a `301` or `302` status code and a `Location` header!)

#### Task 4C: Fetch Actual HTML

Want to see what a server ACTUALLY sends to your browser? Try:

```bash
curl https://www.example.com | head -50
```

This fetches the first 50 lines of HTML! You should see raw HTML code — `<html>`, `<head>`, `<body>`, etc.!

📝 What HTML tags did you see? List at least 5:

1. `<_________>`
2. `<_________>`
3. `<_________>`
4. `<_________>`
5. `<_________>`

---

## 🌐 Part 5: Browser DevTools Investigation (+100 XP)

### 🎯 Goal: Use Browser Developer Tools to see what happens behind the scenes!

#### Task 5A: Network Tab Analysis

1. Open your website in Chrome/Firefox/Edge
2. Open DevTools (`F12` or `Cmd+Option+I`)
3. Click the **Network** tab
4. **Refresh the page** (Ctrl+R or Cmd+R)
5. Watch all the requests appear!

📝 **Network Analysis Report:**

```
┌──────────────────────────────────────────────┐
│           NETWORK ANALYSIS REPORT             │
├──────────────────────────────────────────────┤
│                                              │
│  Website: ________________________________   │
│                                              │
│  Total number of requests: _______________   │
│                                              │
│  Total data transferred: _______ KB/MB       │
│                                              │
│  Page load time: ________________ seconds    │
│                                              │
│  Largest file: ___________________________   │
│  Size: ___________ KB                        │
│  Type: ___________                           │
│                                              │
│  Types of files loaded:                      │
│  □ HTML files: ______ (how many?)            │
│  □ CSS files: ______                         │
│  □ JavaScript files: ______                  │
│  □ Image files: ______                       │
│  □ Font files: ______                        │
│  □ Other: ______                             │
│                                              │
└──────────────────────────────────────────────┘
```

#### Task 5B: HTTP Status Codes in the Wild

Look at the **Status** column in the Network tab. Find examples of:

| Status Code | File/Request That Returned It | What It Means |
|------------|------------------------------|---------------|
| 200 | __________________________ | OK — Loaded successfully |
| 301 or 302 | __________________________ | Redirect |
| 304 | __________________________ | Not Modified (cached) |
| Other? | __________________________ | __________________________ |

#### Task 5C: Elements Tab Exploration

1. Switch to the **Elements** tab
2. Use the element selector tool (🔍 icon)
3. Click on different parts of the page

📝 Find and record the HTML for:

- The main heading: `<_________ > _________________ </_________>`
- A link: `<a href="_______________">_______________</a>`
- An image: `<img src="_______________">`

---

## 📊 Part 6: The Complete Investigation Report (+50 XP)

### 🎯 Goal: Put it all together into one comprehensive report!

Write up your complete findings. This is your final deliverable!

### 📝 Investigation Report Template

```
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║        🕵️ INTERNET DETECTIVE INVESTIGATION REPORT 🕵️     ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  Detective Name: ___________________________________     ║
║  Date: _____________________________________________     ║
║  Website Investigated: _____________________________     ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  1. DNS FINDINGS                                         ║
║  ────────────────                                        ║
║  The domain _________ resolves to IP address _________.  ║
║  This means the website's server is located at           ║
║  this numerical address on the Internet.                 ║
║                                                          ║
║  2. PING RESULTS                                         ║
║  ───────────────                                         ║
║  The average response time was _______ ms.               ║
║  This means data takes _______ milliseconds to travel    ║
║  from my computer to the server and back.                ║
║  This is [fast/medium/slow] because ________________.    ║
║                                                          ║
║  3. TRACEROUTE JOURNEY                                   ║
║  ────────────────────                                    ║
║  My data passed through _______ routers (hops).          ║
║  The journey went through:                               ║
║  My computer → _______ → _______ → _______ → Server     ║
║                                                          ║
║  4. HTTP HEADERS                                         ║
║  ───────────────                                         ║
║  The server returned status code _______ which means     ║
║  ___________________________________________________.    ║
║  The server is running _________ software.               ║
║  The website uses [HTTP/HTTPS] encryption.               ║
║                                                          ║
║  5. BROWSER ANALYSIS                                     ║
║  ───────────────────                                     ║
║  Loading the page required _______ HTTP requests.        ║
║  The total data transferred was _______ MB.              ║
║  The page took _______ seconds to load.                  ║
║  It loaded __ HTML, __ CSS, __ JS, and __ image files.   ║
║                                                          ║
║  6. CONCLUSION                                           ║
║  ─────────────                                           ║
║  When I type _________ in my browser, here's what        ║
║  happens in order:                                       ║
║                                                          ║
║  Step 1: DNS looks up ________ → finds IP __________     ║
║  Step 2: My computer pings the server (_______ ms)       ║
║  Step 3: Data travels through ______ routers             ║
║  Step 4: Server responds with status ______ and          ║
║          sends back ______ files                         ║
║  Step 5: My browser renders the page in ______ seconds!  ║
║                                                          ║
║  The coolest thing I learned: ________________________   ║
║  __________________________________________________      ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
```

---

## 🏅 PROJECT COMPLETE!

### 🎉 You've completed the ULTIMATE Internet Detective Project! 🕵️

### ⭐ XP Breakdown

| Part | XP |
|------|----|
| 🔍 Part 1: DNS Investigation | +75 XP |
| 📡 Part 2: Ping Test | +75 XP |
| 🗺️ Part 3: Traceroute | +100 XP |
| 📥 Part 4: HTTP Headers | +100 XP |
| 🌐 Part 5: Browser DevTools | +100 XP |
| 📊 Part 6: Complete Report | +50 XP |
| **Total** | **+500 XP** ⭐ |

---

## 🏅 Badge Earned: 🕵️ Internet Detective!

**Congratulations, Internet Detective!** You have demonstrated mastery of:

- ✅ DNS lookups with `nslookup`
- ✅ Network testing with `ping`
- ✅ Route mapping with `traceroute`
- ✅ HTTP investigation with `curl`
- ✅ Browser Developer Tools
- ✅ Understanding the COMPLETE journey of data on the Internet

---

## 🏆 Final Badge Check: Internet Master!

**Have you completed ALL modules and earned 1800+ XP?**

If so, head to the achievements page to claim your ultimate badge!

👉 [Achievements & Badge Tracker](../achievements.md)

---

## 🎓 What's Next?

You've finished the course — but your learning journey doesn't have to end! Here are some ideas for what to explore next:

| Interest | What to Learn | Resource |
|----------|-------------|---------|
| 🎨 **Build websites** | Learn HTML, CSS, JavaScript | freeCodeCamp.org, Khan Academy |
| 🐍 **Programming** | Learn Python | Scratch → Python pathway |
| 🛡️ **Cybersecurity** | Ethical hacking basics | PicoCTF.org (capture the flag games!) |
| 🌐 **Networking** | Go deeper into protocols | Cisco Networking Academy |
| 🎮 **Game Development** | Build your own games | Unity, Godot, or Roblox Studio |
| 🤖 **AI & Machine Learning** | Understand how AI works | Google's Machine Learning Crash Course |

**Remember: Every expert was once a beginner. You've already proven you can learn hard things. Keep going!** 🚀

---

> 🎉 **Thank you for completing "How the Internet Works"!** You now understand more about the Internet than most adults on the planet. Use this knowledge wisely, stay safe online, and never stop being curious! 🌟
