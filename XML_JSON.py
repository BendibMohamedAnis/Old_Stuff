import json
import sys
import xml.etree.cElementTree 
import argparse

parser = argparse.ArgumentParser(description='=============== [ Convertir XML > JSON ] ===============')
parser.add_argument('infile', nargs='?', type=argparse.FileType('rt'), default=sys.stdin)


def converter(obj):

    inner = dict(obj.attrib)
    children = list(map(converter, list(obj)))
    text = obj.text and obj.text.strip()

    if text:
        inner['@text'] = text
    if children:
        inner['@children'] = children

    return {obj.tag: inner}


def main(args):

    xml_parser = xml.etree.cElementTree.parse(args.infile)
    root = xml_parser.getroot()

    json.dump(converter(root), sys.stdout, indent=2)
    print()


if __name__ == '__main__':
    args = parser.parse_args()
    main(args)