# acme.sql
これはサンプルのPythonパッケージです。

sdist
```bash
python setup.py sdist
```

```python
dist/
└── acme.sql-0.1.1.tar.gz
```

bdist
```bash
python setup.py bdist
```

```python
dist/
└── acme.sql-0.1.1-py3.11.egg
```

参考：wheel

```bash
python setup.py bdist_wheel
```

```python
dist/
└── acme.sql-0.1.1-py3-none-any.whl
```

インストール
python setup.py install