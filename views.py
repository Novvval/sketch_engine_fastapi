from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from dc.concordance import get_concordance, ConcordanceList
from dc.thesaurus import get_thesaurus_list, ThesaurusList
from dc.wordsketch import get_wordsketch, WordSketch

router = APIRouter()


@router.get("/concordance", response_model=ConcordanceList)
async def concordance(lang, query):
    concordance = jsonable_encoder(get_concordance(lang=lang, query=query))
    return JSONResponse(concordance)


@router.get("/thesaurus", response_model=ThesaurusList)
async def thesaurus(lang, query):
    thesaurus = jsonable_encoder(get_thesaurus_list(lang=lang, query=query))
    return JSONResponse(thesaurus)


@router.get("/wordsketch", response_model=WordSketch)
async def wordsketch(lang, query):
    wordsketch = jsonable_encoder(get_wordsketch(lang=lang, query=query))
    return JSONResponse(wordsketch)
