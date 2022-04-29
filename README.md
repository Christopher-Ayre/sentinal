# Sentinal

Sentinal is a python program using sentiment analysis and social media scraping to trade crypto. 

## Configuration

Add any 'CoinName,CoinCode' combinations you would like the software to look for to the Whitelist in resources/Whitelist

## Installation

Run the install script, it will create a virtualenv and install all the needed modules.

```bash
./install.sh
```

## Usage

```bash
# Arguments are someones twitter handle and the amount of tweets to look through.
./run.sh elonmusk 1000
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[GNU AGPLv3](https://choosealicense.com/licenses/agpl-3.0/)