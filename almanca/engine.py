"""
Almanca soru motoru — Deutsch_bot'un engine.py'sinden uyarlandı.
JSON formatları:
  - Standart: [{"id", "thema", "frage", "optionen", "antwort", "erklaerung", "kontext"}, ...]
  - DTZ Lesen: [{"id", "thema", "text", "fragen": [{"frage_id", "frage", "optionen", "antwort", "erklaerung"}, ...]}, ...]
"""
import json
import random
from dataclasses import dataclass, field
from pathlib import Path

DATA_DIR = Path(__file__).parent / 'data'

# slug → (dosya adı, thema, türkçe ad)
KONULAR: dict[str, tuple[str, str, str]] = {
    'zu-infinitiv':          ('1-zu_infinitiv.json',              'zu + Infinitiv',               'zu + Mastar'),
    'satzbau':               ('2-satzbau.json',                   'Satzbau',                      'Cümle Yapısı'),
    'wechselpraep':          ('3-wechselprap.json',               'Wechselpräpositionen',         'Değişken Edatlar'),
    'reflexive-verben':      ('4-reflexive_verben.json',          'Reflexive Verben',             'Dönüşlü Fiiller'),
    'relativpronomen':       ('5-relativpronomen.json',           'Relativpronomen',              'İlgi Zamirleri'),
    'verben-praep':          ('6-verben_prap.json',               'Verben mit Präpositionen',     'Edatlı Fiiller'),
    'pronominaladv':         ('7-pronominaladverbien.json',       'Pronominaladverbien',          'Pronominaladverb'),
    'adjektivdekl':          ('8-adjektivdeklination.json',       'Adjektivdeklination',          'Sıfat Çekimi'),
    'n-deklination':         ('9-n_deklination.json',             'N-Deklination',                'N-Çekimi'),
    'modalverben':           ('10-modalverben.json',              'Modalverben',                  'Modal Fiiller'),
    'konnektoren':           ('11-konnektoren_kausativ.json',     'Konnektoren',                  'Bağlaçlar'),
    'dativ-akkusativ':       ('12-Dativ-Akkusativ-Genitiv.json',  'Dativ / Akkusativ / Genitiv',  'Dativ / Akk / Gen'),
    'zweiteilige-konnekt':   ('13-Zweiteilige Konnektoren.json',  'Zweiteilige Konnektoren',      'İkili Bağlaçlar'),
    'dtz-lesen':             ('14_dtz_lesen.json',                'DTZ Lesen',                    'DTZ Okuma'),
}


@dataclass
class Soru:
    uid: str
    thema: str
    frage: str
    optionen: dict          # {"A": ..., "B": ..., "C": ..., "D": ...}
    dogru_harf: str         # "A" / "B" / "C" / "D"
    erklaerung: str
    kontext: str = ''
    lesetext: str = ''      # DTZ Lesen için okuma metni


def _load_all() -> dict[str, list[Soru]]:
    """Tüm JSON'ları yükler, slug → [Soru] dict döner."""
    bank: dict[str, list[Soru]] = {}

    for slug, (fname, thema, _tr) in KONULAR.items():
        path = DATA_DIR / fname
        if not path.exists():
            continue
        raw = json.loads(path.read_text(encoding='utf-8'))

        sorular: list[Soru] = []
        for item in raw:
            # DTZ Lesen — nested format
            if 'fragen' in item:
                lesetext = item.get('text', '')
                for fq in item['fragen']:
                    sorular.append(Soru(
                        uid=str(fq['frage_id']),
                        thema=thema,
                        frage=fq['frage'],
                        optionen=fq['optionen'],
                        dogru_harf=fq['antwort'],
                        erklaerung=fq.get('erklaerung', ''),
                        lesetext=lesetext,
                    ))
            else:
                sorular.append(Soru(
                    uid=str(item['id']),
                    thema=thema,
                    frage=item['frage'],
                    optionen=item['optionen'],
                    dogru_harf=item['antwort'],
                    erklaerung=item.get('erklaerung', ''),
                    kontext=item.get('kontext', ''),
                ))

        bank[slug] = sorular

    return bank


# Modül yüklendiğinde bir kez yükle
_BANK: dict[str, list[Soru]] = _load_all()


def konu_listesi() -> list[dict]:
    """Her konu için {slug, thema, tr, toplam} döner."""
    return [
        {
            'slug': slug,
            'thema': thema,
            'tr': tr,
            'toplam': len(_BANK.get(slug, [])),
        }
        for slug, (_, thema, tr) in KONULAR.items()
        if slug in _BANK
    ]


def rastgele_soru(slug: str, gorulmus: list[str]) -> Soru | None:
    """Görülmemiş sorulardan rastgele bir tane döner."""
    havuz = [s for s in _BANK.get(slug, []) if s.uid not in gorulmus]
    if not havuz:
        return None
    soru = random.choice(havuz)

    # Seçenekleri karıştır
    harfler = list(soru.optionen.keys())
    degerler = list(soru.optionen.values())
    dogru_deger = soru.optionen[soru.dogru_harf]
    random.shuffle(degerler)
    yeni_optionen = {harfler[i]: degerler[i] for i in range(len(harfler))}
    yeni_dogru = next(h for h, v in yeni_optionen.items() if v == dogru_deger)

    return Soru(
        uid=soru.uid,
        thema=soru.thema,
        frage=soru.frage,
        optionen=yeni_optionen,
        dogru_harf=yeni_dogru,
        erklaerung=soru.erklaerung,
        kontext=soru.kontext,
        lesetext=soru.lesetext,
    )


def konu_bilgi(slug: str) -> tuple[str, str] | None:
    """slug → (thema, tr) döner, yoksa None."""
    entry = KONULAR.get(slug)
    if not entry:
        return None
    return entry[1], entry[2]


def soru_sayisi(slug: str) -> int:
    return len(_BANK.get(slug, []))
