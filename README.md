# pyTxTchat
### Python Terminal Text Chat 
- using Apache Kafka

### using
- ping
```
$ pip install pytxtchat

$ txtping
pong
```

- chat
```bash
$ txtchat
```

![chathome](https://github.com/user-attachments/assets/067127c4-4e61-4755-9b3c-763b0d7a6e2d)

![chatui](https://github.com/user-attachments/assets/acccd899-e264-479c-9450-4030bd5ec0a6)

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
- [recursive-include tcss](https://docs.python.org/ko/3.8/distutils/sourcedist.html)