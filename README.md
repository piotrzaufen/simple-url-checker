# 🔗 Simple URL Checker

A lightweight Python script to check the availability (HTTP status) of URLs from a text file. Useful for monitoring uptime, testing APIs, or verifying scraped links.

## 📂 Features

- Accepts a list of URLs from a file
- Uses `requests` for fast HTTP checks
- Prints response status code per URL
- Saves logs to `results.txt`
- Written in under 50 lines of Python 🐍

## 🚀 Requirements

- Python 3.6+
- `requests` module (`pip install requests`)

## 🛠️ Usage

1. Clone the repository or download the script:
```bash
git clone https://github.com/yourusername/simple-url-checker
cd simple-url-checker
```

2. Prepare a file named `urls.txt` with one URL per line.

3. Run the checker:
```bash
python url_checker.py
```

4. Results will appear on the screen and be saved to `results.txt`.

## 📥 Example

**urls.txt:**
```
https://google.com
https://nonexistent.website.abc
https://github.com
```

**Output:**
```
[200] https://google.com
[404] https://nonexistent.website.abc
[200] https://github.com
```

## 📄 License

MIT – use, modify, share freely ✌️
