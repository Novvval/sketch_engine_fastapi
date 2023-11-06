from fastapi.testclient import TestClient
from dc.concordance import ConcordanceList, ConcordanceItem
from dc.thesaurus import ThesaurusList, ThesaurusItem
from dc.wordsketch import WordSketch, Gramrel
from main import app

client = TestClient(app)


def test_concordance():
    response = client.get("/concordance?lang=en&query=foo")
    assert response.status_code == 200
    result = ConcordanceList(**response.json())
    assert isinstance(result, ConcordanceList)
    assert result.lang == "en"
    assert result.query == "foo"
    assert result.method == "concordance"
    assert isinstance(result.result[0], ConcordanceItem)


def test_thesaurus():
    response = client.get("/thesaurus?lang=en&query=foo")
    assert response.status_code == 200
    result = ThesaurusList(**response.json())
    assert isinstance(result, ThesaurusList)
    assert result.lang == "en"
    assert result.query == "foo"
    assert result.method == "thesaurus"
    assert isinstance(result.result[0], ThesaurusItem)


def test_wordsketch():
    response = client.get("/wordsketch?lang=en&query=foo")
    assert response.status_code == 200
    result = WordSketch(**response.json())
    assert isinstance(result, WordSketch)
    assert result.lang == "en"
    assert result.query == "foo"
    assert result.method == "wordsketch"
    assert isinstance(result.results[0], Gramrel)


def test_wrong_language():
    response = client.get("/concordance?lang=xyz&query=foo")
    assert response.status_code == 400
    assert response.json()["detail"] == "Language does not exist"


def test_wrong_query():
    response = client.get("/concordance?lang=en&query=")
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid query"
