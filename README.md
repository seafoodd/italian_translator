# Italian Translator

**Italian Translator** is a command-line tool for translating Italian sentences and displaying examples using Reverso Context.

## Features

- Translate Italian sentences to English (default) or any specified language.
- Translate from a specified language to Italian using the `--reverse` option.
- Display a specified number of example sentences using the `--examples` option.
- Easy-to-use command-line interface with colored output.

## Installation

You can install the package using `pip`:

```sh
pip install italian-translator
```

## Usage

```sh
italian-translator <sentence>
ita <sentence>
```

## Options

- `--reverse`, `-R`: Translate from a specified language to Italian.
- `--language`, `-L`: Specify the language to translate to (default: English).
- `--examples`, `-E`: Display a specified number of example sentences.
- `--help`, `-h`: Display the help message.

## Examples

Translate an Italian sentence to English:
```sh
italian-translator "Ciao, come stai?"
ita il gatto
```
Translate an English sentence to Italian:
```sh
italian-translator --reverse "Hello, how are you?"
ita -R the cat
```
Translate an Italian sentence to French
```sh
italian-translator --language french "Ciao, come stai?"
ita -L french il gatto
```
Display 5 examples sentences:
```sh
italian-translator --examples 5 "Ciao, come stai"
ita -E 5 il gatto
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
- seafood - [GitHub](https://github.com/seafoodd) | [Telegram](https://t.me/seafudd)

