# aixtract

A simple utility to prepare files for AI analysis by copying them with their directory structure encoded in the filename.

## Description

`aixtract` reads a list of file paths from a `.aixtract` file and copies each file to a new directory, encoding the original path hierarchy into the filename using double underscores (`__`). For example, `app/controllers/users_controller.rb` becomes `app__controllers__users_controller.rb`.

This is particularly useful when preparing files to upload to AI assistants that don't support directory structures.

## Installation

```bash
# Download the script
curl -o /usr/local/bin/aixtract https://raw.githubusercontent.com/yourusername/aixtract/main/aixtract.rb

# Make it executable
chmod +x /usr/local/bin/aixtract
```

## Usage

1. Create a `.aixtract` file in your project directory listing the files you want to process:

```plaintext
app/controllers/users_controller.rb
app/models/user.rb
config/routes.rb
# Lines starting with # are ignored
```

2. Run the script:

```bash
aixtract
```

The script will:

1. Create a new directory in your Downloads folder named `project_name_YYYYMMDD_HHMMSS`
2. Copy each listed file to this directory, converting path separators to double underscores
3. Preserve file permissions and metadata
4. Show progress and a summary of processed files

## Example

If your project structure looks like this:

```
myapp/
├── .aixtract
├── app/
│   ├── controllers/
│   │   └── users_controller.rb
│   └── models/
│       └── user.rb
└── config/
    └── routes.rb
```

And your `.aixtract` contains:

```plaintext
app/controllers/users_controller.rb
app/models/user.rb
config/routes.rb
```

Running `aixtract` will create:

```
~/Downloads/myapp_20250108_123456/
├── app__controllers__users_controller.rb
├── app__models__user.rb
└── config__routes.rb
```

## Error Handling

The script will:

- Skip files that don't exist with a warning
- Skip empty lines and comments in `.aixtract`
- Exit with error if `.aixtract` file is not found
- Show clear error messages for any issues during copying

## Requirements

- Ruby 2.0 or later
- Unix-like operating system (tested on macOS and Linux)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -am 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
