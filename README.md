# Bulk Heroku APIs Validator

**Bulk Heroku APIs Validator** is a Python script designed to take a list of Bulk API keys and validate them by making requests to their respective services at once. The output includes the validation results for each API key, helping identify valid or invalid keys.

## Features

- Accepts a list of Heroku API keys (provided in a file or via user input).
- Validates each API key by checking its response from the associated service.
- Provides output indicating whether each API key is valid or invalid.
- No Need to check all keys one-by-one.
  
## Prerequisites

To use the API Key Validator, you need the following installed on your system:

- Python 3.7+
- Required libraries (install with `pip`):
  - `sys`
  - `subprocess`

You can install the required dependencies using the following command:
```bash
  pip install -r requirements.txt
```
## Usage

1. **Clone the Repository**:
```bash
  git clone https://github.com/msaadsbr/Bulk-Heroku-APIs-Validator.git
  cd Bulk-Heroku-APIs-Validator
```
2. **Prepare Your API Keys List**:

Prepare your txt file with Heroku API keys per line. These keys can be fetched from any recon process and tools like SecretFinder and Mantra. Examples of required keys format are:
```bash
  Heroku API KEY  ->      C2F41010-65B3-11d1-A29F-00AA00C14882
  C2F41010-65B3-11d1-A29F-00AA00C14882
  HRKU-C2F41010-65B3-11d1-A29F-00AA00C14882
```
3. **Run the Script**:

After preparing your API keys file, you can run the script:
```bash
  python3 checker.py /path/to/your_api_keys.txt
```
4. **Output**:

The script will output the validation results for each API key in the following format:
```
  [-] Your Key Is Invalid! --> If Key Is Invalid!
  [+] Possibly Your Key is Valid!! --> If Key Is Possibly Valid!
```

## Contribution

If you'd like to contribute to this project, feel free to submit a pull request or open an issue. Your suggestions and improvements are welcome!

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
