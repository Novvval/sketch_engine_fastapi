from typing import List
from pydantic import BaseModel
from sketch_engine_request import SketchEngineRequest


class ConcordanceItem(BaseModel):
    text: str

    class Config:
        orm_mode = True


class ConcordanceList(BaseModel):
    status: int = 200
    query: str
    method: str
    lang: str
    corpus: str
    result: List[ConcordanceItem]

    class Config:
        orm_mode = True


def get_concordance(lang, query) -> ConcordanceList:
    request = SketchEngineRequest("concordance", lang, query).send()
    corpus = request["CorpName"].split("/")[-1]

    lines = []
    if not request["Lines"]:
        return ConcordanceList(
            status=200,
            query=query, method="concordance",
            lang=lang, corpus=corpus,
            result=[])

    for line in request["Lines"]:
        try:
            left = line["Left"][0]["Str"]
        except IndexError:
            left = ''
        try:
            kwic = line["Kwic"][0]["Str"]
        except IndexError:
            kwic = ''
        try:
            right = line["Right"][0]["Str"]
        except IndexError:
            right = ''
        item = left + kwic + right
        item = ConcordanceItem(text=item)
        lines.append(item)
    return ConcordanceList(
        status=200,
        query=query, method="concordance",
        lang=lang, corpus=corpus,
        result=lines)
