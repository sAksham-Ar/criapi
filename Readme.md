# criapi

An API to get cricket scores,scorecards and commentary in python.

## Installation

Install it as below:

```bash
pip3 install criapi
```

## Usage

### Initialization 

```python
from criapi import Cricbuzz
c=Cricbuzz()
```

### live scores

```python
print(c.livescore())
```

### scorecard

```python
print(c.scorecard(id))
```

### commentary

```python
print(c.commentary(id))
```




