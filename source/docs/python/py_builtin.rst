=======================
Python Built-in Modules
=======================


re
==

Regular Expression processing module.

- compile(pattern, flags=0) -- Escape all non-alphanumeric characters in pattern.
- findall(pattern, string, flags=0) -- Return a list of all non-overlapping matches in the string.
    - Empty matches are included in the result.
- finditer(pattern, string, flags=0) -- Return an iterator over all non-overlapping matches in the string. 
- match(pattern, string, flags=0) -- Try to apply the pattern at the start of the string, returning a match object, or None if no match was found.
- purge() -- Clear the regular expression cache
- search(pattern, string, flags=0) -- Scan through string looking for a match to the pattern, returni
- split(pattern, string, maxsplit=0, flags=0) -- Split the source string by the occurrences of the pattern, returning a list containing the resulting substrings.
- sub(pattern, repl, string, count=0, flags=0) -- Return the string obtained by replacing the leftmost non-overlapping occurrences of the pattern in string by the replacement repl.
- subn(pattern, repl, string, count=0, flags=0) -- Return a 2-tuple containing (new_string, number).
    - number is the number of substitutions that were made.
- template(pattern, flags=0) -- Compile a template pattern, returning a pattern object

.. code-block:: python

    p = re.compile('regex')
    if p.match("str"):
        do_some_thing()
    if re.search("regex", "str"):
        do_some_thing()





SocketServer
============


.. code-block:: guess

    +------------+
    | BaseServer |
    +------------+
          |
          v
    +-----------+        +------------------+
    | TCPServer |------->| UnixStreamServer |
    +-----------+        +------------------+
          |
          v
    +-----------+        +--------------------+
    | UDPServer |------->| UnixDatagramServer |
    +-----------+        +--------------------+
