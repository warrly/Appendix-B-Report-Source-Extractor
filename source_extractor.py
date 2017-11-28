import argparse
import re
import xml.etree.ElementTree as ET
import zipfile
import os
import sys
import docx2txt
import re

nsmap = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

def qn(tag):
    """
    Stands for 'qualified name', a utility function to turn a namespace
    prefixed tag name into a Clark-notation qualified tag name for lxml. For
    example, ``qn('p:cSld')`` returns ``'{http://schemas.../main}cSld'``.
    Source: https://github.com/python-openxml/python-docx/
    """
    prefix, tagroot = tag.split(':')
    uri = nsmap[prefix]
    return '{{{}}}{}'.format(uri, tagroot)

def xml2text(xml):
    """
    A string representing the textual content of this run, with content
    child elements like ``<w:tab/>`` translated to their Python
    equivalent.
    Adapted from: https://github.com/python-openxml/python-docx/
    """
    text = u''
    root = ET.fromstring(xml)
    for child in root.iter():
        if child.tag == qn('w:t'):
            t_text = child.text
            text += t_text if t_text is not None else ''
        elif child.tag == qn('w:tab'):
            text += '\t'
        #elif child.tag in (qn('w:br'), qn('w:cr'),qn("w:p")):    
        elif child.tag in (qn("w:footnote")):
            text += '\n'
    return text

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

# if __name__ == '__main__':
#     for i, footnote in enumerate(fileinput.input()):
#         sources = sources_of(footnote)
#         for source in sources:
#             print('{}\t{}'.format(i + 1, source))
