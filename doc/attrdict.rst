
Attrdict
--------
A dictionary that allows to get and set items, attribute style.

Example:
^^^^^^^^

>>> my_attrdict = AttrDict.from_container({"swallows": {"laden": 1, "unladen": 9000}})
>>> my_attrdict.swallows.unladen
9000
>>> my_attrdict.swallows.unladen += 111
>>> my_attrdict.swallows.unladen
9111
