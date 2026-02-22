# Quran Chapter XML Parser

This project parses a Quran chapters XML file and extracts structured information such as chapter names, Sajdah details, and revelation order using Python.

## 📂 Project Structure

* `quranChapter.xml` — XML file containing Quran chapter metadata
* `quran_xml.py` — Python script to parse and analyze the XML file
* Output files (optional):

  * `sajdah_chapterlist.txt`
  * `chapterByOrder.txt`

---

## 📖 XML Structure

Each `<sura>` element contains attributes like:

* `index` — Chapter number
* `ayas` — Number of verses
* `name` — Arabic name
* `tname` — Transliteration
* `ename` — English name
* `type` — Meccan or Medinan
* `order` — Revelation order
* `rukus` — Number of rukus
* `sajda_index` — Sajdah reference
* `sajda_aya` — Sajdah verse number
* `sajda_type` — Type of Sajdah

Example:

```xml
<sura index="1" ayas="7" start="0" name="الفاتحة" tname="Al-Faatiha" ename="The Opening" type="Meccan" order="5" rukus="1" sajda_index="NA" sajda_aya="NA" sajda_type="NA" />
```

---

## ⚙️ Features

The script demonstrates how to:

* Extract chapter names
* Identify chapters containing Sajdah verses
* Export Sajdah chapter details to a file
* Sort chapters by revelation order
* Compare chapter index with revelation sequence

---

## ▶️ How to Run

Make sure you have Python 3 installed.

```bash
python quran_xml.py
```

---

## 🛠 Requirements

* Python 3.x
* Built-in library: `xml.etree.ElementTree`

---

## 📌 Purpose

This project is a simple XML parsing example using structured Quran metadata for learning, analysis, and data extraction tasks.

---

