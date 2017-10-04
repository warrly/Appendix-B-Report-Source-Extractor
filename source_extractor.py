#!/usr/bin/python3
"""
Call this file as:
    ./source_extracter.py <input file>
"""
import fileinput
import re


website = '(?:http://)(?:www.)\S+\.com(?:/\S+[A-Za-z])'
formal_website = '(?:“.+,” .+, ){}'.format(website)


PATTERNS = [
    # Conversations (Conversation with First (optional-Middle) Last)
    re.compile('Conversation with [A-Z][a-zA-Z]+(?: [A-Z][a-zA-Z]+){1,2}'),
    # Depositions (Deposition of Firstname (optional-Middle) Last, Month Day, Year)
    re.compile('Deposition of [A-Z][a-zA-Z]+(?: [A-Z][a-zA-Z]+){1,2}, [A-Z][a-z]+ \d{1,2}, \d{4}'),
    # Bates sources (EMAILS 12345678 or EMAILS12345678 or EMAILS 1234567 or EMAILS1234567)
    re.compile('[A-Z]+(?:-[A-Z]+)\s?[0-9]{7,8}'),
    # websites
    re.compile('{}|{}'.format(website, formal_website)),
]


def sources_of(footnote: str) -> [str]:
    sources = []
    for pattern in PATTERNS:
        results = pattern.findall(footnote)
        for result in results:
            sources.append('{}.'.format(result))
    return sources


if __name__ == '__main__':
    for i, footnote in enumerate(fileinput.input()):
        sources = sources_of(footnote)
        for source in sources:
            print('{}\t{}'.format(i + 1, source))
