# 数据类型检查

可以用内置函数 `isinstance()`实现：

```python
if not isinstance(x, (int, float)):
    raise TypeError('bad operand type')
```

> 释义：如果数据 x 不是 `int`, `float`类型时，返回 typeErrot 信息。