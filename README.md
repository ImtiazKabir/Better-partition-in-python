# Friendly Implementation of partition in Python 3

Just clone the `partition.py` and import it in your python script with `from partition imoprt partition`
The `partition` is an implementation of mathematical partition of `n` into `r` parts where each part belongs to [`mn`, `mx`].
`mn` and `mx` are optional. The default value of `mn` is `0` and the default value of `mx` is `n`.
The output of this function is a list containing all the possible partitions in provided condition.

## Sample calls
`partition(10, 3)` will output partitions of `10` with `3` numbers each between `0` and `10` (both inclusive).
`partition(10, 3, mn=4)`  will output partitions of `10` with `3` numbers each between `4` and `10` (both inclusive).
`partition(10, 3, mx=7)`  will output partitions of `10` with `3` numbers each between `0` and `7` (both inclusive).
`partition(10, 3, mn=2, mx = 8)`  will output partitions of `10` with `3` numbers each between `2` and `8` (both inclusive).

## Sample outputs
`partition(5, 3)` yields the following output `[[0, 0, 5], [0, 1, 4], [0, 2, 3], [1, 1, 3], [1, 2, 2]]`
