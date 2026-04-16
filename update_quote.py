import requests

url = "https://quotes-github-readme.vercel.app/api?type=horizontal"
response = requests.get(url).json()

quote = response.get("quote", "Stay consistent.")
author = response.get("author", "Unknown")

new_quote = f"## ✨ Quote for Developers\n\n> {quote}  \n> — {author}\n"

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

start = content.find("## ✨ Quote for Developers")
end = content.find("---", start)

updated = content[:start] + new_quote + "\n\n---" + content[end+3:]

with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated)
