# aixtract

A simple utility to prepare files for AI analysis by copying them with their directory structure encoded in the filename.

## Description

`aixtract` reads a list of file paths from a `.aixtract` file and copies each file to a new directory, encoding the original path hierarchy into the filename using double underscores (`__`).  
For example, `src/models/user.py` becomes `src__models__user.py`.

This is particularly useful when preparing files to upload to AI assistants that don't support directory structures.

## Installation

```sh
pip install aixtract
```

## Usage

1. Create a `.aixtract` file in your project directory listing the files you want to process:

```plaintext
src/models/user.py
tests/test_user.py
config/settings.json
# Lines starting with # are ignored
```

2. Run the command:

```sh
aixtract
```

The utility will:

1. Create a new directory in your Downloads folder named `project_name_YYYYMMDD_HHMMSS`
2. Copy each listed file to this directory, converting path separators to double underscores
3. Preserve file permissions and metadata
4. Open the target directory automatically (on supported platforms)

## Example

If your project structure looks like this:

```txt
myproject/
├── .aixtract
├── src/
│   └── models/
│       └── user.py
├── tests/
│   └── test_user.py
└── config/
    └── settings.json
```

And your `.aixtract` contains:

```txt
src/models/user.py
tests/test_user.py
config/settings.json
```

Running `aixtract` will create:

```txt
/tmp/myproject_20250101_123456/
├── src__models__user.py
├── tests__test_user.py
└── config__settings.json
```

## Error Handling

The utility will:

- Skip files that don't exist with a warning
- Skip empty lines and comments in `.aixtract`
- Exit with error if `.aixtract` file is not found
- Show clear error messages for any issues during copying

## Requirements

- Python 3.8 or later
- Works on macOS, Linux, and Windows (directory opening feature supported on macOS and Linux)
