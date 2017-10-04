#!/usr/bin/python3
"""
Call this file as:
    ./source_extracter.py <input file>
"""
import re


website = '(?:http://)(?:www.)\S+\.com(?:/\S+[A-Za-z])'
formal_website = '(?:“.+,” .+, ){}'.format(website)


PATTERNS = [
    # Conversations (Conversation with First (optional-Middle) Last)
    re.compile('Conversation with [A-Z][a-zA-Z]+(?: [A-Z][a-zA-Z]+){1,2}'),
    # Depositions (Deposition of Firstname (optional-Middle) Last, Month Day, Year)
    re.compile('Deposition of [A-Z][a-zA-Z]+(?: [A-Z][a-zA-Z]+){1,2}, [A-Z][a-z]+ \d{1,2}, \d{4}'),
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
    bates_prefixes = []
    prefix = None
    while True:
        prefix = input(
            'Provide a Bates prefix to match (e.g. BSC-EDWARD or EMAILS).\n'
            'Press "enter" on a blank line to stop inputting prefixes.\n'
        ).strip()
        if not prefix:
            break
        bates_prefixes.append(prefix)

    if bates_prefixes:
        print('Proceeding with the following prefixes:')
        print('  ' + ', '.join(bates_prefixes))
        print('')
        for prefix in bates_prefixes:
            PATTERNS.append(re.compile(prefix + '\s?[0-9]{7,8}'))

    with open('input.txt') as f:
        for i, line in enumerate(f.readlines()):
            sources = sources_of(line)
            for source in sources:
                print('{}\t{}'.format(i + 1, source))
