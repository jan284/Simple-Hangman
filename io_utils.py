"""
File: io_utils.py

This module contains the function get_filehandle to
call in main program to open the dictionary
"""


def get_filehandle(filename, mode='r'):
    """
    Takes a filename and a mode of opening and tries
    to open the given file. Raises OSError if the file
    name is not valid, and ValueError if the mode is not valid.

    :param filename: name of file to be opened
    :type filename: str
    :param mode: mode to open the file in
    :type mode: str
    :return handle: file object if opened successfully
    :raises OSError: if file cannot be opened successfully
    :raises ValueError: if appropriate mode is not given
    """

    try:
        handle = open(filename, mode)
    # Raise OSError if file cannot be opened
    except IOError:
        raise OSError(f'File {filename} does not exist')
    # Raise value error if mode is not valid
    else:
        if mode not in ['r', 'w']:
            raise ValueError('Mode must be be either r or w')
        return handle
