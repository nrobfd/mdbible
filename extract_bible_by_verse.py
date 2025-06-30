import json
import re
import os

# Load the JSON data
with open("json/ESV.json") as file:
    data = json.load(file)
    books = data["books"]

# Create output directory
os.makedirs("by_verse", exist_ok=True)

book_index = 1
for book_title in books:
    book_dir = f"{book_index:02d}_{book_title.replace(' ', '_')}"
    os.makedirs(f"by_verse/{book_dir}", exist_ok=True)

    book = books[book_title]
    chapters = [chapter for chapter in book]

    chap_index = 1
    for chapter in chapters:
        verses_raw = chapter
        verse_num = 1

        for verse_obj in verses_raw:
            chunks = [i for i in verse_obj]
            verse = " ".join([chunk[0] for chunk in chunks if not isinstance(chunk[0], list)])
            verse = re.sub(r'\s([?.,;!"](?:\s|$))', r'\1', verse)

            file_name = f"{book_title.replace(' ', '_')}_{chap_index}_{verse_num}.md"
            file_path = os.path.join("by_verse", book_dir, file_name)

            with open(file_path, "w", encoding="utf-8") as verse_file:
                verse_file.write(f"# {book_title} {chap_index}:{verse_num}\n\n{verse}\n")

            verse_num += 1

        chap_index += 1
    book_index += 1
