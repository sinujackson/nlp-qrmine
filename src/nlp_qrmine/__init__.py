# -*- coding: utf-8 -*-
from pkg_resources import get_distribution, DistributionNotFound

from .readfiles import ReadData
from .content import Content

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = 'nlp-qrmine'
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = 'unknown'
