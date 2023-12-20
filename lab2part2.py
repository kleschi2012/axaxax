from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import wikipedia

app = FastAPI(
    title = "Лабораторная 2"
)


class Search(BaseModel): #шаблон для функции
    search:list[str]

class Suggest(BaseModel):
    word: str


class Page(BaseModel):
    title: str
    content: str

class Title(BaseModel):
    title: str

@app.post("/search/{src}", response_model=Search)  #path # функция возвращает то что ты написал, поиск по википедии погода + слово которое написал
def src(src: str):                                                          #ветка закрыта / нет
    return Search(search=wikipedia.search(src))


@app.post("/ispravlyator-inator", response_model=Suggest)  #query #функция возвращает то что ты написал, исправляет слова, ветка открыта(/ есть)
def ispravlyator(word: str):
    return Suggest(word=wikipedia.suggest(word))


@app.post("/page/result", response_model=Page)  #body          #дефолтный путь (неважно открытый или закрытый)
def return_page(peremennaya: Title):
    try:
        pg = wikipedia.page(peremennaya.title)
    except wikipedia.WikipediaException:
        raise HTTPException(status_code=404, detail = "No results")
        return Page(title=pg.title,content=pg.content)