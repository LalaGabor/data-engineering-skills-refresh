yield pauses a function and produces one value at a time.
Generators are lazy: they don't build the whole result in memory.
next() retrieves one value, but normally generators are consumed with for.

Generator expressions use () instead of []:

(x * 2 for x in numbers)
They work naturally with consumers like sum(), max(), etc.

Generator pipelines chain processing stages:

raw → clean → filter → transform → output
Each stage can yield records onward without creating intermediate lists.
This is useful for large files, APIs, and memory-efficient data pipelines.
Key distinction: iter()/next() explain the mechanism; generators and lazy pipelines are the practically useful DE concept.