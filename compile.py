#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from jinja2 import Template
import json
import argparse


def fill_template(filename, variables):
    s = '\n'
    to_name = variables['to_prename'] + ' ' + variables['to_surname']
    from_name = variables['from_prename'] + ' ' + variables['from_surname']
    s += ' TO:\t{}\n'.format(to_name)
    s += ' FROM:\t{}\n\n'.format(from_name)
    with open(filename, 'r') as f:
        template = Template(f.read())
        for line in template.render(variables).splitlines():
            s += '  ' + line + '\n'
    return s


def main():
    config = {}
    with open('conf.json', 'r') as f:
        config = json.load(f)
    parser = argparse.ArgumentParser(description='theinternetl0vesyou')
    parser.add_argument('template',
                        type=str,
                        help='path to template file')
    args = parser.parse_args()
    print(fill_template(args.template, config))

if __name__ == '__main__':
    main()
