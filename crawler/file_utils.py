# coding: utf-8

import os
import json

from os.path import join


def read_file(filepath):
    with open(join(filepath)) as fp:
        query = json.load(fp)
    return query


def list_files(path, filter_by_extensions=None):
    filter_by_extensions = filter_by_extensions or []
    files = os.listdir(path)
    for filename in filter(lambda file_: file_.split('.')[-1] in filter_by_extensions, files):
        yield read_file(join(path, filename))


