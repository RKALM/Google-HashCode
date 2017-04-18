#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import numpy as np

from quarkball.utils import Network, Caching


# random.seed(0)


# ======================================================================
class CachingRandom(Caching):
    def __init__(self, *args, **kwargs):
        Caching.__init__(self, *args, **kwargs)

    # ----------------------------------------------------------
    def fill(self, network):
        min_video_size = np.min(network.videos)
        new_videos = list(range(network.num_videos))
        for i, cache in enumerate(self.caches):
            avail_cache = network.cache_size
            random.shuffle(new_videos)
            for new_video in new_videos:
                video_size = network.videos[new_video]
                if video_size <= avail_cache and new_video not in cache:
                    cache.add(new_video)
                    avail_cache -= video_size
                if min_video_size > avail_cache:
                    break


# ======================================================================
class CachingRandomSeed(Caching):
    def __init__(self, *args, **kwargs):
        Caching.__init__(self, *args, **kwargs)

    # ----------------------------------------------------------
    def fill(self, network):
        min_video_size = np.min(network.videos)
        new_videos = list(range(network.num_videos))
        random.shuffle(new_videos)
        for i, cache in enumerate(self.caches):
            avail_cache = network.cache_size
            for new_video in new_videos:
                video_size = network.videos[new_video]
                if video_size <= avail_cache and new_video not in cache:
                    cache.add(new_video)
                    avail_cache -= video_size
                if min_video_size > avail_cache:
                    break


# ======================================================================
class CachingOptimByRequests(Caching):
    def __init__(self, *args, **kwargs):
        Caching.__init__(self, *args, **kwargs)

    # ----------------------------------------------------------
    def fill(self, network, p=(0)):
        # sort requests by number of requests divided by video size
        sorted_requests = sorted(
            network.requests,
            key=lambda x: x[2] / network.videos[x[1]])[::-1]
        # key=lambda x: x[2])[::-1]
        # min_video_size = np.min(network.videos)
        free_caches = np.ones(network.num_caches) * network.cache_size
        cached_requests = []
        for request in sorted_requests:
            if request not in cached_requests:
                new_video, endpoint, num = request
                # sorted_caches = np.argsort(
                #     network.cache_latencies[endpoint, :])
                sorted_caches = np.argsort(
                    network.cache_latencies[endpoint, :] / (free_caches + 1))
                sorted_caches = sorted_caches[
                    network.cache_latencies[endpoint, :] > 0]
                for i in list(sorted_caches):
                    video_size = network.videos[new_video]
                    if (video_size <= free_caches[i] and
                                new_video not in self.caches[i]):
                        self.caches[i].add(new_video)
                        free_caches[i] -= video_size
                        cached_requests.append(request)


# ======================================================================
class CachingOptimByCaches(Caching):
    def __init__(self, *args, **kwargs):
        Caching.__init__(self, *args, **kwargs)

    # ----------------------------------------------------------
    def fill(self, network, p=(0)):
        # sort requests by number of requests divided by video size
        sorted_requests = sorted(
            network.requests,
            key=lambda x: x[2] / network.videos[x[1]])[::-1]
        # key=lambda x: x[2])[::-1]
        min_video_size = np.min(network.videos)
        free_caches = np.ones(network.num_caches) * network.cache_size
        cached_requests = []
        for i, cache in enumerate(self.caches):
            for request in sorted_requests:
                if request not in cached_requests:
                    new_video, endpoint, num = request
                    video_size = network.videos[new_video]
                    if (video_size <= free_caches[i] and
                                new_video not in cache):
                        cache.add(new_video)
                        free_caches[i] -= video_size
                        cached_requests.append(request)
                if free_caches[i] < min_video_size:
                    break


# ======================================================================
class CachingBruteForce(Caching):
    def __init__(self, *args, **kwargs):
        Caching.__init__(self, *args, **kwargs)

    # ----------------------------------------------------------
    def fill(self, network, id=None):
        pass
