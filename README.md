# Easy Wordcloud Generator

Dieses Projekt extrahiert Text aus einer PDF-Datei, entfernt Stoppwörter und generiert eine Wortwolke.

## Voraussetzungen
- Python 3.x

## Installation
1. Klone das Repository:
```sh
git clone https://github.com/felixBtzr/easy-wordclouds
cd easy-wordclouds
```

2. Erstelle eine virtuelle Umgebung (optional, aber empfohlen)
python -m venv venv

Linux: ```source venv/bin/activate```
Windows: ```venv\Scripts\Activate```

3. Notwendige Bibliotheken installieren
```sh
pip install -r requirements.txt
```

## Nutzung
1. Ersetzt ``pdf_path`` in deinem Skript durch den Pfad zu deiner PDF-Datei
2. Skript ausführen: ``python3 -m main.py``