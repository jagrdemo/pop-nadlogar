# Nadlogar

Nadlogar je spletna storitev za generiranje naključnih nalog ter njihovih rešitev. Učitelj izbere seznam tipskih nalog in vzorčno izhodno datoteko ter naloži seznam učencev, storitev pa za vsakega učenca ustvari posamezne datoteke z nalogami ter skupno datoteko z rešitvami. Naloge niso čisto naključne, saj storitev za istega učenca vedno vrne enako nalogo, kar omogoča, da naloge naknadno popravljate, ne da bi se vam pri tem v celoti spremenile.

Nadlogar je projekt, ki nastaja v okviru programerskega kluba [Fakultete za matematiko in fiziko, Univerza v Ljubljani](http://www.fmf.uni-lj.si/). Poleg vseh članov kluba, ki k razvoju prispevajo vse od idej do kode, so k razvoju bistveno pomagali oziroma še pomagajo:

- Gregor Šega, ki je napisal prvo skripto za generiranje nalog v _Mathematici_ in s tem dal idejo za splošen program,
- Matija Pretnar, ki je na osnovi te skripte v _Mathematici_ napisal [splošen program](https://github.com/matijapretnar/generiranje-nalog),
- Urša Pertot, ki je na osnovi tega programa napisala [program v Pythonu](https://github.com/ursa16180/generiranje-nalog/tree/python),
- podjetje [EBA d.o.o., Ljubljana](http://www.ebadms.com), ki je velikodušno prevzelo sponzorstvo programerskega kluba.

## Programska oprema pri pouku

To je kopija (fork) izvirnega repozitorija, ki smo ga uporabili za demonstracijo pri predmetu Programska oprema pri pouku. V nadaljevanju tega razdelka je opisana namestitev projekta na operacijskem sistemu Windows z nekaj dodatnimi opombami.

Najprej ustvarimo virtualno okolje za python knjižnice. Drugi ukaz je morda potreben pri uporabi PowerShell-a. Procesu z njim dodelimo pravico za poganjanje skript (konkretno, skripte `activate`).
```
python -m venv venv
Set-ExecutionPolicy Unrestricted -Scope Process
venv/Scripts/activate
```

Nato namestimo potrebne knjižnice in poženemo migracije, ki so potrebne ob prvem zagonu programa.
```
cd nadlogar
pip install -r requirements\local.txt
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata documents/fixtures/initial.json
```

Ustvarimo še svojega uporabnika in zaženemo program.
```
python manage.py createsuperuser
python manage.py runserver
```

Za ponoven zagon uporabimo naslednje ukaze.
```
Set-ExecutionPolicy Unrestricted -Scope Process
venv/Scripts/activate
cd nadlogar
python manage.py runserver
```

Po dodajanju nove datoteke v `nadlogar/problems/models` osvežimo `__init__.py` in poženemo naslednje ukaze.
```
python manage.py makemigrations
python manage.py migrate
```
Kot primer novega sklopa nalog smo dodali datoteko [`sistemi_enacb.py`](nadlogar/problems/models/sistemi_enacb.py). Omogoča generiranje nalog za reševanje sistemov linearnih enačb z dvemi ali tremi neznankami (tak tip naloge je v nekoliko drugačni obliki sicer že vključen v sklop Linearna funkcija).


## Navodila za namestitev

Na začetku klonirajte repozitorij ter ustvarite virtualno okolje:

    git clone git@github.com:ul-fmf/nadlogar.git
    cd nadlogar
    python3 -m venv venv

Dobiti bi morali sledečo strukturo datotek:

    nadlogar/
        nadlogar/
            config/
            documents/
            ...
            manage.py
        ...
        venv/
            ...

Po prvi namestitvi, pa tudi na vsake toliko časa, greste v mapo `nadlogar/nadlogar/` ter s sledečimi ukazi kodo posodobite, aktivirate virtualno okolje, namestite potrebne pakete in posodobite bazo:

    git pull
    source venv/bin/activate
    pip install -r requirements/local.txt
    python manage.py migrate

Če uporabljate Windowse, je drugi ukaz drugačen

    git pull
    venv\Scripts\activate
    pip install -r requirements\local.txt
    python manage.py migrate

Strežnik nato poženete z

    python manage.py runserver

Teste poženete z

    python manage.py test

Po namestitvi je koristno pognati

    python manage.py loaddata documents/fixtures/initial.json

Tako naložite nekaj koristnih LaTeX predlog.

## Kako poženete Nadlogarja?

Če poženete ukaz

    python manage.py runserver

vam na [lokalnem strežniku](http://127.0.0.1:8000) požene spletno stran. Vendar se morate za njeno uporabo najprej prijaviti.
Zato ustvarite adminskega uporabnika, kar storite z ukazom

    python manage.py createsuperuser

Ko to storite, vam je dostopen tudi [adminski vmesnik](http://127.0.0.1:8000/admin/), kjer med drugim lahko dodajate nova besedila nalog _(vsaj zaenkrat, saj se bo shranjevanje besedil kmalu spremenilo)_.

Za navodila glede dodajanja funkcionalnosti in popravljanja napak glejte
[CONTRIBUTING.md](CONTRIBUTING.md).
