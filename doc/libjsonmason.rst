
libjsonmason: Deconstruct and reconstruct container types.
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
