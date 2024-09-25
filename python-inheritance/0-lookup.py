#!/usr/bin/python3

"""Defines function that returns a list of attributes."""


def lookup(obj):
    """Return a list of an object available attributes."""
    return (dir(obj))
