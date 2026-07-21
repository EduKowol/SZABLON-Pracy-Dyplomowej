"""Moving-average filter used in Appendix G."""

from collections.abc import Sequence


def moving_average(samples: Sequence[float], window: int) -> list[float]:
    """Return a causal moving average with a shortened initial window."""
    if window <= 0:
        raise ValueError("window must be positive")

    result: list[float] = []
    running_sum = 0.0

    for index, sample in enumerate(samples):
        running_sum += sample
        if index >= window:
            running_sum -= samples[index - window]

        current_window = min(index + 1, window)
        result.append(running_sum / current_window)

    return result


if __name__ == "__main__":
    data = [1.0, 1.4, 2.1, 2.8, 3.0]
    print(moving_average(data, window=3))
