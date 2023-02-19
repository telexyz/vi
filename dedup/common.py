#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2022-12-26 15:59:42
# @Author  : Chenghao Mou (mouchenghao@gmail.com)

import logging
from rich.logging import RichHandler
logger = logging.getLogger("text_dedup")
logger.setLevel(logging.INFO)
logger.addHandler(RichHandler(rich_tracebacks=True))
logger.propagate = False


# - - - - - - - - - - - - - - - - - - - - - - - - - - -


class UnionFind:
    """
    A data structure for maintaining disjoint sets. This helps build connected components for given duplicate pairs.
    """

    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            return x

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        self.parent[px] = self.parent[py] = min(px, py)


from itertools import tee
from typing import List
from typing import Text


# - - - - - - - - - - - - - - - - - - - - - - - - - - -


def ngrams(sequence: List[Text], n: int):
    """
    Return the ngrams generated from a sequence of items, as an iterator.

    This is a modified version of nltk.util.ngrams.

    Parameters
    ----------
    sequence : List[Text]
        The sequence of items.
    n : int
        The length of each ngram.

    Returns
    -------
    iterator
        The ngrams.

    Examples
    --------
    >>> list(ngrams(["a", "b", "c", "d"], 2))
    [('a', 'b'), ('b', 'c'), ('c', 'd')]
    >>> list(ngrams(["a", "b"], 3))
    [['a', 'b']]
    """
    if len(sequence) < n:
        return iter([sequence])
    iterables = tee(iter(sequence), n)
    for i, sub_iterable in enumerate(iterables):
        for _ in range(i):
            next(sub_iterable, None)
    return zip(*iterables)


# - - - - - - - - - - - - - - - - - - - - - - - - - - -


import time

class TimerContext:
    def __init__(self, timer: "Timer", name: str):
        self.timer = timer
        self.name = name
        self.start_time = None

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if any([exc_type, exc_val, exc_tb]):
            raise exc_val
        self.timer.elapsed_times[self.name] = time.time() - self.start_time


class Timer:
    """
    A simple timer that tracks the elapsed time of each context.
    """

    def __init__(self):
        self.elapsed_times = {}

    def __call__(self, name: str) -> TimerContext:
        """
        Create a context with the given name.

        Parameters
        ----------
        name: str
            The name of the context.

        Returns
        -------
        TimerContext
            The context.

        Examples
        --------
        >>> t = Timer()
        >>> with t("test"):
        ...     time.sleep(1)
        >>> assert int(t.elapsed_times.get("test", 0)) == 1, "The elapsed time should be 1 second."
        >>> with t("test2"):
        ...     time.sleep(2)
        >>> assert int(t.elapsed_times.get("test2", 0)) == 2, "The elapsed time should be 2 seconds."
        """
        return TimerContext(self, name)
