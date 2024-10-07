class AverageMeter:
    r"""
    Computes and stores the average and current value.

    Attributes:
        val: Result of current batch.
        avg: Result of all data.
        sum: Sum of values.
        count: Number of values.

    Examples:
        >>> meter = AverageMeter()
        >>> meter.update(0.7)
        >>> meter.val
        0.7
        >>> meter.avg
        0.7
        >>> meter.update(0.9)
        >>> meter.val
        0.9
        >>> meter.avg
        0.8
        >>> meter.sum
        1.6
        >>> meter.count
        2
        >>> meter.reset()
        >>> meter.val
        0.0
        >>> meter.avg
        nan
    """

    v: float = 0
    n: float = 0
    sum: float = 0
    count: float = 0

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.v = 0
        self.n = 0
        self.sum = 0
        self.count = 0

    def update(self, value, n: float = 1) -> None:
        self.v = value
        self.n = n
        self.sum += value
        self.count += n

    def value(self):
        return self.v / self.n if self.n != 0 else float("nan")

    def average(self):
        return self.sum / self.count if self.count != 0 else float("nan")

    @property
    def val(self):
        return self.value()

    @property
    def avg(self):
        return self.average()

    def __format__(self, format_spec) -> str:
        return f"{self.val.__format__(format_spec)} ({self.avg.__format__(format_spec)})"
