# coding: utf-8
import os
_UNSET_VAR = 'environment variable %s is not set'


def env_string(name):
    '''Asserts an environment variable is set and is a string.

        >>> env_string('PATH')
    '''
    val = os.getenv(name)
    assert val is not None, _UNSET_VAR % name


__all__ = [
    'env_string',
    'env_int'
]

