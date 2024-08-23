# pyTxTchat
### Python Terminal Text Chat 
- using Apache Kafka

### using
```
$ pip install pytxtchat

$ pytxtchat-ping
pong
```

### if you're a developer
```bash
$ git clone ... & cd ...

$ pdm venv create
$ source .venv/bin/activate
$ pdm install

$ pytest --cov
================ test session starts =================
platform linux -- Python 3.11.9, pytest-8.3.2, pluggy-1.5.0
configfile: pyproject.toml
plugins: cov-5.0.0

---------- coverage: platform linux, python 3.11.9-final-0 -----------
Name                      Stmts   Miss  Cover
---------------------------------------------
src/pytchat/__init__.py       0      0   100%
src/pytchat/com.py            2      0   100%
tests/__init__.py             0      0   100%
tests/test_com.py             4      0   100%
---------------------------------------------
TOTAL                         6      0   100%


================= 1 passed in 0.05s ==================

```

### Ref
- https://textual.textualize.io/getting_started