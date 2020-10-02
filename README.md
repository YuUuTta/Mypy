# Mypy

## Overview(概要)
自身の利用頻度が高い関数に関して集めたものです。


## Usage(使用方法)

### import

モジュールとして用いる場合は`sys`でモジュールサーチパスを追加してからimportしてください。
myh5モジュールを使用したい場合、
```python
import sys
sys.path.append("Mypy/myh5/main_h5/")
import main_h5
```
generalモジュールを使用したい場合、
```python
import sys
sys.path.append("Mypy/general/main_general")
import main_general

```


