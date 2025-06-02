# diff_maker

A Python package for annotating string differences with HTML-like tags.

## Installation

```bash
pip install diff_maker
```

## Usage

```python
from diff_maker import diff_maker

# Examples
print(diff_maker("думают что", "думают, что"))
# Output: "думают<ins>,</ins> что"

print(diff_maker("зойти", "зайти"))
# Output: "<rep>зойти</rep>"

print(diff_maker("вообще забудут", "забудут вообще"))
# Output: "<rep>вообще забудут</rep>"

print(diff_maker("телефон, и даже", "телефон и даже"))
# Output: "телефон<del>,</del> и даже"
```

## Tags

The function uses the following HTML-like tags to mark differences:

- `<ins>...</ins>` - Text that needs to be inserted
- `<del>...</del>` - Text that needs to be removed
- `<rep>...</rep>` - Text that needs to be replaced (i.e., deleted and substituted)

## Algorithm

The algorithm uses Python's built-in `difflib` module to identify differences between strings and applies the appropriate annotation tags. It follows these rules:

1. If there are complex changes (replacements or both insertions and deletions), the entire original string is marked as needing replacement with `<rep>` tags.
2. For simpler changes (only insertions or only deletions), specific parts are annotated with `<ins>` or `<del>` tags.

## License

MIT
