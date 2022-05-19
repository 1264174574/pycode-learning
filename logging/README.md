# logging模块

> This module defines functions and classes which implement a flexible event logging system for applications and libraries.

- 使用 Python Logging 模块的主要好处是所有 Python 模块都可以参与日志记录
- Logging 模块提供了大量具有灵活性的功能

**日志级别等级排序**：critical > error > warning > info > debug

**级别越高打印的日志越少，反之亦然，即**

- debug : 打印全部的日志( notset 等同于 debug )
- info : 打印 info, warning, error, critical 级别的日志
- warning : 打印 warning, error, critical 级别的日志
- error : 打印 error, critical 级别的日志
- critical : 打印 critical 级别

默认的级别是WARNING,也就意味着只有级别大于等于的才会被看到，跟踪日志的方式可以是写入到文件中，也可以直接输出到控制台。

