from typing import List
from pydantic import BaseModel
from sketch_engine_request import SketchEngineRequest


class ThesaurusItem(BaseModel):
    word: str
    score: float

    class Config:
        orm_mode = True


class ThesaurusList(BaseModel):
    status: int = 200
    query: str
    method: str
    lang: str
    corpus: str
    result: List[ThesaurusItem]

    class Config:
        orm_mode = True


def get_thesaurus_list(lang, query) -> ThesaurusList:
    request = SketchEngineRequest("thesaurus", lang, query).send()
    corpus = request["CorpName"].split("/")[-1]

    words = []
    if not request["Words"]:
        return ThesaurusList(status=200, query=query, method="thesaurus", lang=lang, corpus=corpus, result=[])
    for word in request["Words"]:
        word = ThesaurusItem(word=word["Word"], score=word["Score"])
        words.append(word)
    return ThesaurusList(status=200, query=query, method="thesaurus", lang=lang, corpus=corpus, result=words)
