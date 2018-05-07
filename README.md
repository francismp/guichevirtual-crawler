# guichevirtual-crawler

Python crawler for https://www.guichevirtual.com.br/rodoviarias

## Running
To run execute the following command:
`scrapy runspider crawler.py`

Or to generate a output file:
`scrapy runspider crawler.py -o output.json`

## TODO
- Better naming for BusTerminal fields
- Regex to get the state from name
- Regex to get coordinates from google maps iframe URL