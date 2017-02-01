# Return the first item of an iterable, or a default value if the iterable is
# exhausted.
def first(iterable, default=None):
    if iterable:
        for i in iterable:
            return i
    return default
