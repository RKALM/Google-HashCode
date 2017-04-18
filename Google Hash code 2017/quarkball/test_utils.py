#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
quarkball2017: tests for base classes
"""

# ======================================================================
# :: Imports
from __future__ import (
    division, absolute_import, print_function, unicode_literals)

import os
import datetime
from quarkball.utils import Network, Caching
from quarkball.fill_caching import CachingRandom

DIRPATH = 'data'
IN_DIRPATH = os.path.join(DIRPATH, 'input')
OUT_DIRPATH = os.path.join(DIRPATH, 'output')
SOURCES = (
    'kittens', 'me_at_the_zoo', 'trending_today', 'videos_worth_spreading',)


# ======================================================================
def test_network_input(
        in_dirpath=IN_DIRPATH,
        sources=SOURCES):
    for source in sources:
        in_filepath = os.path.join(in_dirpath, source + '.in')
        network = Network.load(in_filepath)
        print(network)


# ======================================================================
def test_caching_output(
        in_dirpath=OUT_DIRPATH,
        source='example'):
    in_filepath = os.path.join(in_dirpath, source + '.out')
    caching = Caching.load(in_filepath)
    print(caching)
    out_filepath = os.path.join(in_dirpath, 'test_' + source)
    caching.save(out_filepath)


# ======================================================================
def test_score(
        in_dirpath=IN_DIRPATH,
        out_dirpath=OUT_DIRPATH,
        source='example'):
    in_filepath = os.path.join(in_dirpath, source + '.in')
    network = Network.load(in_filepath)
    print(network)
    out_filepath = os.path.join(out_dirpath, source + '.out')
    caching = Caching.load(out_filepath)
    print(caching.score(network))


# ======================================================================
def test_fill(
        in_dirpath=IN_DIRPATH,
        out_dirpath=OUT_DIRPATH,
        source='example'):
    in_filepath = os.path.join(in_dirpath, source + '.in')
    network = Network.load(in_filepath)
    out_filepath = os.path.join(out_dirpath, source + '.out')
    caching = CachingRandom(network.num_caches)
    caching.fill(network)
    print(repr(caching))
    print('Random Caching - Score: {}'.format(caching.score(network)))


def test_method(
        in_dirpath=IN_DIRPATH,
        out_dirpath=OUT_DIRPATH,
        sources=SOURCES,
        caching_method=Caching):
    tot_score = 0
    for source in sources:
        in_filepath = os.path.join(in_dirpath, source + '.in')
        network = Network.load(in_filepath)
        out_filepath = os.path.join(out_dirpath, source + '.out')
        caching = caching_method(network.num_caches)
        caching.fill(network)
        caching.save(out_filepath)
        score = caching.score(network)
        tot_score += score
        print('{} score: {}'.format(source, score))
    print('\nTOTAL SCORE: {}\n'.format(tot_score))


# ======================================================================
def main():
    print(__doc__)
    begin_time = datetime.datetime.now()

    # test_network_input()
    # test_caching_output()
    # test_score()
    # test_fill()
    test_method(caching_method=CachingRandom)

    end_time = datetime.datetime.now()
    print('\nExecTime: {}'.format(end_time - begin_time))


# ======================================================================
if __name__ == '__main__':
    main()
