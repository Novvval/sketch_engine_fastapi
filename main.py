from fastapi import FastAPI
from starlette.responses import RedirectResponse
import views

app = FastAPI(title="Sketch Engine FastAPI wrapper",
              version="1.0.0",
              description="This is a Python wrapper for the SketchEngine API, specifically designed for the FastAPI "
                          "framework. The SketchEngine API provides various linguistic functionalities, "
                          "including retrieving examples of a word in context, obtaining grammatical relations of a "
                          "given word, and getting a list of similar words to a queried word.")
app.include_router(views.router)


@app.get("/")
async def index():
    return RedirectResponse("/docs")


if "__name__" == "__main__":
    app = app
