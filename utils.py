import ast
import re
import time
import tracemalloc
from functools import wraps

BASE_DIR = "/home/addua/practice-session/"
INPUT_FILE = BASE_DIR + "input.txt"
OUTPUT_FILE = BASE_DIR + "output.txt"

def parse_input_file(filename=INPUT_FILE):
    params = {}

    with open(filename, "r") as f:
        text = f.read()

    # match: nums = [1,2,3], target = 9, s = "abc"
    pattern = r'(\w+)\s*=\s*(\[[^\]]*\]|\{[^\}]*\}|".*?"|\'.*?\'|[^,\n]+)'

    matches = re.findall(pattern, text)

    for key, value in matches:
        value = value.strip()

        try:
            params[key] = ast.literal_eval(value)
        except Exception:
            params[key] = value

    return params


def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print("\n")
        print(f"[Profiler] {func.__name__} | Time: {end_time - start_time:.6f}s | Peak Memory: {peak / 1024:.2f} KB")
        print("\n")
        return result
    return wrapper

def write_output(result):
    with open(OUTPUT_FILE, "w") as f:
        f.write(str(result))