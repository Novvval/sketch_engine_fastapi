# SketchEngine API Wrapper

This is a Python wrapper for the SketchEngine API, specifically designed for 
the FastAPI framework. The SketchEngine API provides various linguistic 
functionalities, including retrieving examples of a word in context, 
obtaining grammatical relations of a given word, and getting a list of 
similar words to a queried word.

## Installation

Begin by cloning the repository

    git clone https://github.com/Novvval/sketch_engine_fastapi.git

## Run the app

cd to the project directory use the following command

    docker-compose up -d

The API will run on http://127.0.0.1:8000

# API responses

The API methods are described below.
All methods accept the following query params:
* `lang` - The language used, e.g. `?lang=en`.
Currenly, the following languages can be used:
"en": "English", "de": "German", "it": "Italian", "et": "Estonian", 
"ru": "Russian", "cz": "Czech".
* `query` - the word that will be searched by sketch engine, e.g. `?query=apple`

## Concordance search

Get a list of sentences where the queried word is used.

### Request

`GET /concordance?lang=en&query=foo`

    curl -i -H 'Accept: application/json' http://localhost:8000/concordance?lang=en&query=foo

### Response

```json
{
    "status": 200,
    "query": "foo",
    "method": "concordance",
    "lang": "en",
    "corpus": "skell_3_10",
    "result": [
        {
            "text": "The name of this instruction is \"foo\"."
        },
        {
            "text": "We have 1 billion records in foo."
        },
        {
            "text": "Foo was beyond the point of no return."
        }
    ]
}
```

## Thesaurus

Get a list of word related to the queried word, where `score` is the similarity to the 
original query

### Request

`GET /concordance?lang=en&query=foo`

    curl -i -H 'Accept: application/json' http://localhost:8000/thesaurus?lang=en&query=foo

### Response

```json
{
    "status": 200,
    "query": "foo",
    "method": "thesaurus",
    "lang": "en",
    "corpus": "skell_3_10",
    "result": [
        {
            "word": "Foo",
            "score": 0.115
        },
        {
            "word": "elem",
            "score": 0.1
        },
        {
            "word": "glob",
            "score": 0.094
        }
    ]
}
```

## Wordsketch

Get a list of grammatical relationships of a given word, with a list of examples
of the grammatical relationship used in context

### Request

`GET /concordance?lang=en&query=bar`

    curl -i -H 'Accept: application/json' http://localhost:8000/wordsketch?lang=en&query=bar

### Response

```json
{
    "status": 200,
    "query": "bar",
    "method": "wordsketch",
    "lang": "en",
    "corpus": "skell_3_10",
    "results": [
        {
            "name": "verbs with bar as subject",
            "words": [
                {
                    "word": "code",
                    "lem_pos": "code-v",
                    "context": "bar coding"
                },
                {
                    "word": "close",
                    "lem_pos": "close-v",
                    "context": "bar closed"
                },
                {
                    "word": "overlook",
                    "lem_pos": "overlook-v",
                    "context": "bar overlooking the"
                },
                {
                    "word": "cater",
                    "lem_pos": "cater-v",
                    "context": "bars catering to"
                }
            ]
        }
    ]
}
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for more details.
