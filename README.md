# Quranic Audio Downloader

Quranic Audio Downloader is a Python script designed to download audio files from the Quranic Audio website. It provides various functionalities for downloading recitations, taraweeh recitations from Haramain, non-Hafs recitations, and recitations with translation.

## Installation

1. Clone the repository:

   ```bash
   git clone --depth=1 https://github.com/BeedPro/Quran-Audio-Downloader
   ```

2. Create a virtual environment and activate it by:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```


3. Install the required dependencies within a virtual environment:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the Quranic Audio Downloader, run the `program.py` script:

```bash
./run
```

Follow the prompts to select the desired section and proceed with the download.

## Features

- Download recitations from various Qaris.
- Download recitations from Haramain Taraweeh.
- Download non-Hafs recitations.
- Download recitations with translation.

## Dependencies

- [requests](https://pypi.org/project/requests/): For making HTTP requests.
- [tqdm](https://pypi.org/project/tqdm/): For displaying progress bars.
- [typing](https://docs.python.org/3/library/typing.html): For type hints.
- [math](https://docs.python.org/3/library/math.html): For mathematical operations.
- [os](https://docs.python.org/3/library/os.html): For interacting with the operating system.

## Testing
To run the tests, run the following command:
```bash
./run_tests
```
## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
