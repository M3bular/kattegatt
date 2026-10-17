import torch
import pygpubench


def generate_input(**kwargs): ...


def reference_kernel(args): ...


def generate_test_case(*, seed, **kwargs):
    x, y = generate_input(**kwargs, seed=seed)
    expected = torch.empty_like(y)
    reference_kernel((expected, x))
    return (y, x), (expected, 1e-6, 1e-6)


res = pygpubench.do_bench_isolated(
    "submission.kernel", generate_test_case, {"size": 1024}, 100, 5, discard=True
)
print("❌" if res.errors else "✅", pygpubench.basic_stats(res.time_us))
