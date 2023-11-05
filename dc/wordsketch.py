from typing import List
from pydantic import BaseModel
from sketch_engine_request import SketchEngineRequest


class Word(BaseModel):
    word: str
    lem_pos: str
    context: str


class Gramrel(BaseModel):
    name: str
    words: List[Word]

    class Config:
        orm_mode = True


class WordSketch(BaseModel):
    status: int = 200
    query: str
    method: str
    lang: str
    corpus: str
    results: List[Gramrel]

    class Config:
        orm_mode = True


def get_wordsketch(lang, query):
    request = SketchEngineRequest("wordsketch", lang, query).send()
    corpus = request["CorpName"].split("/")[-1]

    results = []
    if not request["GramRels"]:
        return WordSketch(
            status=200,
            query=query,
            method="wordsketch",
            lang=lang,
            corpus=corpus,
            results=[])

    for wordsketch in request["GramRels"]:
        words = []
        for word in wordsketch["Words"]:
            word = Word(word=word["Word"], lem_pos=word["Lempos"], context=word["Cm"])
            words.append(word)
        gramrel = Gramrel(name=wordsketch["Name"].replace("%w", query), words=words)
        results.append(gramrel)

    return WordSketch(
        status=200,
        query=query,
        method="wordsketch",
        lang=lang,
        corpus=corpus,
        results=results)
