"""Build index.html from src/lesson-src.html by inlining the QR code.
Usage: python3 build.py   (qr/qr-lesson.svg must exist: segno, URL below)"""
import re
URL = "https://kaijiewpoo.github.io/radio-lesson/"
svg = re.sub(r'<\?xml[^>]*\?>\s*', '', open('qr/qr-lesson.svg').read())
svg = re.sub(r'width="(\d+)" height="(\d+)"', r'viewBox="0 0 \1 \2"', svg, count=1)
html = open('src/lesson-src.html').read().replace('{{QR}}', svg)
open('index.html', 'w').write(html)
print('built index.html for', URL)
