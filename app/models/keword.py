from odmantic import AIOEngine, Model
import datetime


class KeywordModel(Model):
    keyword_ko: str
    keyword_en: str
    count: int
    update_at: datetime.datetime

    class Config:
        collection = "Keywords"