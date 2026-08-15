None selected 

Skip to content
Using Gmail with screen readers
bear 
Conversations
Py instagram project code and README
Inbox

Bear Cahill <bear@bearmo.com>
Attachments
Jan 26, 2026, 7:30 PM
to me



Thanks,
Bear
 3 Attachments
  •  Scanned by Gmail

Mitch Cahill <recedingimp@gmail.com>
Attachments
Jan 28, 2026, 2:02 AM
to Bear

here are some things I made after doing the MIT probability math course. Chat said to code one thing related to each lecture after the lecture prob set. Onya!

On Mon, Jan 26, 2026 at 7:30 PM Bear Cahill <bear@bearmo.com> wrote:


Thanks,
Bear
 2 Attachments
  •  Scanned by Gmail
# Instagram Follow-Back Checker

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![CS50P](https://img.shields.io/badge/Harvard-CS50P-crimson)
![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Windows%20%7C%20Linux-lightgrey)

A Python script that identifies Instagram accounts you follow **that do not follow you back**.  
It outputs both a **summary and a detailed CSV file** of the results.

Created as a final project for **Harvard CS50P**.

---

## Features

- Compares followers vs. following using Instagram-exported data
- Generates a CSV report of non-followers
- Displays total counts for followers, following, and non-followers
- Uses **only your own exported data** (no API access)

---

## How It Works

The script compares two JSON files exported from Instagram:
- Your **followers** list
- Your **following** list

Any account present in *following* but missing from *followers* is flagged.

---

## Quick Start

1. Export your Instagram data (Followers + Following only)
2. Place the JSON files next to `IG_Project.py`
3. Run:
   ```bash
   python IG_Project.py followers_1.json following.json
   ```
   > On macOS and some Linux systems, you may need:
   ```bash
   python3 IG_Project.py followers_1.json following.json
   ```

---

## Output

After running the script, a file named:

```text
not_following_back.csv
```

is created in the same directory.

### What the CSV Contains

The CSV includes:

- Total number of accounts you **follow**
- Total number of **followers**
- Total number of accounts that **do not follow you back**
- A list of usernames that do not follow you back

This makes the results easy to:
- Open in Excel, Google Sheets, or Numbers
- Sort or filter usernames
- Save or share as a report

---

## Example Output (Console)

```text
you follow           151
followers            21
dont follow you back 136
usernames:  
<username1>
<username2>
...
```

---

## Detailed Instructions

1. **Log in to Instagram on a desktop browser.**

2. **Request your Instagram data export**  
   Navigate to:  
   **More (☰ bottom-right) → Settings → Accounts Center → Your information and permissions → Export your information → Create export → Export to device**  
   (Select your Instagram account if prompted.)

3. **Customize the export**
   - Choose **Customize information**
   - Deselect everything except **Followers** and **Following**
   - Set your desired **date range**
   - Select **JSON** as the format  

   Instagram will email you a ZIP file.

4. **Prepare the files**
   - Download and unzip the export
   - Locate the JSON files (typically `followers_1.json` and `following.json`)
   - Place them in the same directory as `IG_Project.py`

5. **Run the script**
   ```bash
   python IG_Project.py followers_1.json following.json
   ```
   or, if required:
   ```bash
   python3 IG_Project.py followers_1.json following.json
   ```

---

## Requirements & Setup

> Placed near the bottom to keep the main flow readable.

- **Python 3.8 or newer**  
  https://www.python.org/downloads/

- **Command-line access**
  - macOS / Linux: Terminal
  - Windows: Command Prompt or PowerShell

- **Instagram account with data export enabled**  
  https://www.instagram.com/accounts/privacy_and_security/

No external Python libraries are required.

---

## Project Structure

```text
.
├── IG_Project.py
├── followers_1.json
├── following.json
└── not_following_back.csv
```

---

## Disclaimer

This project:
- Does **not** use the Instagram API
- Does **not** scrape data
- Uses **only data you personally export from Instagram**

Use responsibly.

---

## License

This project is provided for educational purposes as part of CS50P.

---

Enjoy responsibly 😄  
Vanity is optional.
README.md
Displaying README.md.
