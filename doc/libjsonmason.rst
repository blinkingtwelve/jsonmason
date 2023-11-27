
What
----

A utility for transforming an object into an editable stream, and reconstructing an object from that stream.
To be precise:

* Transform an an object of acyclic nested collections into an iterable of assignment operations (deconstruction)
* Create an object of acyclic nested collections from an iterable of assignment operations (reconstruction)

Why
---
Deconstructing only to reconstruct does not seem very useful in itself. The power is in operating on the intermediary format — the iterable of nodes
lends itself well to pattern matching, transformations, and other forms of computation.

How
---
In the shell
^^^^^^^^^^^^
If you've installed this package (eg ``pip install jsonmason``), then you should have two executables on your ``$PATH``. Both accept JSON on standard input, and print the deconstruction of that JSON on standard output.

* ``jsonmason-nodedump`` makes it easy to ``grep`` for patterns - this is a bit like `gron <https://github.com/tomnomnom/gron>`_, but is intended to make it easy to find patterns for creating transformations in your Python code.
* ``jsonmason-jsdump`` is even more like `gron <https://github.com/tomnomnom/gron>`_, as it prints JS-style assignments that can be pasted straight into a JS console.


In Python code
^^^^^^^^^^^^^^
Any nested container type inheriting from ``Sequence`` or ``Mapping`` is supported for deconstruction.
However, any such sequence or mapping will be squashed to a list or a dict, respectively; those are the only ones supported
in JSON.
Thus deserialized JSON in particular will survive a roundtrip through deconstruction and reconstruction; the resulting structure
will be a semantically identical copy of the original.

The following deconstruction example shows the intermediary format:

>>> my_deserialized_json = [34, {"hello": [["a", "b"], ["c", "d"]], "world": 42}]
>>> node_generator = deconstruct(my_deserialized_json)
>>> next(node_generator)
Node(path=(), value=typing.List, is_leaf=False)
>>> next(node_generator)
Node(path=(typing.List, 0), value=34, is_leaf=True)
>>> next(node_generator)
Node(path=(typing.List, 1), value=typing.Dict, is_leaf=False)
>>> next(node_generator)
Node(path=(typing.List, 1, typing.Dict, 'hello'), value=typing.List, is_leaf=False)

and so on.
A full roundtrip of deserialized JSON results in a semantically identical structure, as promised:

>>> reconstruct(deconstruct(my_deserialized_json))
[34, {'hello': [['a', 'b'], ['c', 'd']], 'world': 42}]

Adding an inline transformation makes things more interesting:

>>> reconstruct(map(lambda node: node.clone(value = node.value * 2) if node.is_leaf else node, deconstruct(my_deserialized_json)))
[68, {'hello': [['aa', 'bb'], ['cc', 'dd']], 'world': 84}]
