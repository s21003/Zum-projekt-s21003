# Projekt końcowy ZUM 2026/2027

To repozytorium rozwijasz przez cały semestr. Górna część tego pliku mówi, jak pracować. Dolna część to dokumentacja Twojego projektu, którą uzupełniasz w kolejnych zadaniach.

## Jak pracować z tym repozytorium

### Co robisz

Przeprowadzasz jeden wiarygodny eksperyment nadzorowanej klasyfikacji jednolabelowej. Każdy przykład ma dokładnie jedną klasę docelową. Pracujesz na tekście, obrazie, audio albo danych multimodalnych. Projekt jest indywidualny.

Projekt ma trzy poziomy:
1. **Poziom A. Punkt odniesienia.** Prosty, sensowny baseline.
2. **Poziom B. Podejście pretrained.** Co najmniej jedno podejście pretrained. Dobrym pierwszym krokiem jest zamrożony encoder i prosty klasyfikator. Fine tuning nie jest obowiązkowy.
3. **Poziom C. Jedno uzasadnione rozszerzenie.** Odpowiada na to samo pytanie projektu i nie zmienia zmiennej docelowej ani problemu klasyfikacyjnego.

Pełne zasady są w pliku [PROJECT_RULES.md](PROJECT_RULES.md). Przeczytaj je przed zgłoszeniem tematu.

### Od czego zacząć

1. Utwórz własne repozytorium z tego szablonu: wybierz „Use this template”, a następnie „Create a new repository”.
2. Nazwij repozytorium `ZUM_2026_ImięNazwisko`.
3. Repozytorium może być publiczne albo prywatne. Jeśli jest prywatne, dodaj konto prowadzącej wskazane na platformie kursu. Jeśli Twoje dane zawierają informacje osobowe albo wrażliwe, przeczytaj najpierw zasadę o prywatności w [zasadach projektu](PROJECT_RULES.md).
4. Przeczytaj [instrukcję zgłoszenia tematu](assignments/00_topic_submission.md) i zgłoś temat.

### Kolejność i terminy

Wszystkie terminy przypadają w niedzielę o godzinie 23:59. Wszystko oddajesz na platformie kursu.

| Etap | Instrukcja | Termin | Punkty | Co oddajesz |
|---|---|---|---|---|
| Zgłoszenie tematu | [00_topic_submission.md](assignments/00_topic_submission.md) | 18 października 2026 | 0, obowiązkowe | wypełniony szablon zgłoszenia |
| Zadanie 1 | [01_data_and_protocol.md](assignments/01_data_and_protocol.md) | 8 listopada 2026 | 15 | link do repozytorium i tag `task-1` |
| Akceptacja artykułu spoza listy | [scientific_paper_review.md](assignments/scientific_paper_review.md) | 22 listopada 2026 | 0, obowiązkowe dla źródeł spoza listy | pełny opis bibliograficzny oraz DOI albo oficjalny link |
| Zadanie 2 | [02_baseline.md](assignments/02_baseline.md) | 29 listopada 2026 | 15 | link i tag `task-2` |
| Artykuł naukowy | [scientific_paper_review.md](assignments/scientific_paper_review.md) | 6 grudnia 2026 | 10, poza projektem | plik PDF albo Markdown |
| Zadanie 3 | [03_pretrained.md](assignments/03_pretrained.md) | 20 grudnia 2026 | 20 | link i tag `task-3` |
| Zadanie 4 | [04_extension.md](assignments/04_extension.md) | 17 stycznia 2027 | 20 | link i tag `task-4` |
| Zadanie 5 | [05_final_evaluation.md](assignments/05_final_evaluation.md) | 31 stycznia 2027 | 30 | link oraz tagi `final-freeze` i `task-5` |

Projekt jest wart 100 punktów. Artykuł jest osobnym zadaniem za 10 punktów.

### Final test w skrócie

1. Final test wydzielasz w Zadaniu 1 i od razu go zamrażasz.
2. Do końca Zadania 4 nie uruchamiasz na nim żadnego modelu. Wszystkie porównania i wybór systemu robisz na validation.
3. W Zadaniu 5 wybierasz dokładnie jeden finalny system, zapisujesz go w `final_system.md` i tworzysz tag `final-freeze`.
4. Nie trenujesz systemu ponownie na `train + validation` ani na żadnym większym zbiorze.
5. Dopiero potem uruchamiasz final test, jeden raz, tylko dla tego systemu. Wynik testu nie może zmienić systemu.

Szczegóły są w [zasadach projektu](PROJECT_RULES.md), w części „Zasady final test”.

### Tagi Git

Każde oddanie wskazuje commit oznaczony tagiem. Oceniamy stan repozytorium z tego commita.

```bash
git add .
git commit -m "Zadanie 1: protokół i podział danych"
git tag -a task-1 -m "Zadanie 1"
git push origin main
git push origin task-1
```

Polecenie `git ls-remote --tags origin` pokazuje, czy tag jest już na GitHub. Tag możesz też utworzyć na stronie GitHub w zakładce Releases. Nie przesuwaj i nie usuwaj tagów po oddaniu.

### Gdzie co zapisujesz

| Miejsce | Co tam trafia |
|---|---|
| `README.md`, część dolna | dokumentacja projektu |
| `notebooks/` | notebooki kolejnych etapów |
| `src/` | kod wspólny dla notebooków (opcjonalnie) |
| `splits/` | identyfikatory przykładów train, validation i final test ([opis formatu](splits/README.md)) |
| `results/` | metryki i predykcje na validation, dziennik eksperymentów, wynik final test (dopiero po `final-freeze`); [opis układu](results/README.md) |
| `final_system.md` | zapis finalnego systemu (Zadanie 5); [szablon](templates/final_system_template.md) |
| `data/sample/` | mała próbka danych, jeśli licencja i zasady prywatności na to pozwalają |
| `templates/` | szablony do skopiowania |

### Czego nie wrzucasz

* pełnych zbiorów danych;
* dużych wag modeli i checkpointów (przechowujesz je poza repozytorium i opisujesz, gdzie są);
* danych, próbek ani identyfikatorów umożliwiających identyfikację osób;
* haseł, tokenów i kluczy API;
* plików tymczasowych środowiska.

Plik `.gitignore` blokuje typowe przypadki, ale to Ty odpowiadasz za zawartość repozytorium.

### Jak oceniamy

Liczy się poprawność metodologiczna, uzasadnienie decyzji i jakość analizy. Wysokość wyniku nie jest sama w sobie kryterium. Projekt z niższym F1, wykonany poprawnie i dobrze przeanalizowany, może dostać więcej punktów niż projekt z bardzo wysokim wynikiem uzyskanym przy wycieku danych. Kryteria każdego zadania są w jego instrukcji, a rubryka ogólna w [zasadach projektu](PROJECT_RULES.md).

---

# Dokumentacja projektu

Uzupełniaj sekcje w zadaniach podanych w nawiasach. Zastępuj teksty w nawiasach kwadratowych.

## Informacje ogólne

* Tytuł: Porównanie prostych cech barwnych i modelu pretrained w rozpoznawaniu chorób liści fasoli
* Autor: Dominik Kamiński
* Modalność: obraz (RGB, 500x500 px)
* Problem klasyfikacji: Nadzorowana klasyfikacja jednolabelowa do 3 klas (angular_leaf_spot, bean_rust, healthy)

## Problem i pytanie eksperymentalne (Zadanie 1)

Celem projektu jest nadzorowana, jednolabelowa klasyfikacja zdjęć liści fasoli do 3 klas: `angular_leaf_spot`, `bean_rust` oraz `healthy`.

- **Pytanie eksperymentalne:** Czy cechy z zamrożonego modelu `MobileNetV3 Small` (ImageNet-1K) z regresją logistyczną pozwalają uzyskać wyższy wynik `macro-F1` niż punkt odniesienia (baseline) oparty na histogramach barw HSV i regresji logistycznej?
- **Pytanie badawcze (Poziom C):** Czy augmentacja zbioru treningowego pojedynczym odbiciem poziomym (horizontal flip) poprawia wynik `macro-F1` modelu `MobileNetV3 Small` na nienaruszonym zbiorze walidacyjnym?

## Dane i licencja (Zadanie 1)

**Źródło:** Zbiór *Beans* (`AI-Lab-Makerere/beans`) autorstwa Makerere University i NARL (Uganda).
- **Licencja:** MIT.
- **Pobieranie:** Skrypt `audit_and_freeze.py` przez bibliotekę `datasets`.
- **Liczba próbek:** 1295 zdjęć RGB 500x500 px (432 `angular_leaf_spot`, 436 `bean_rust`, 427 `healthy`).
- **Etykietowanie:** Diagnozy polowe agronomów z NaCRRI.
- **Wyniki audytu:** 0 braków danych, 0 dokładnych duplikatów MD5, 0 par o odległości pHash <= 2 między podziałami (brak wycieku).
- **Ograniczenia i prywatność:** Brak identyfikatorów roślin (`plant_id`). Dane publiczne, brak danych wrażliwych.

## Protokół (Zadanie 1)

* Jednostka generalizacji: - Jednostka generalizacji: Pojedyncze zdjęcie liścia w warunkach polowych (brak identyfikatorów krzaków plant_id w metadanych wymusza generalizację na poziomie obrazu).
* Podział: Oficjalny podział benchmarkowy autorów zbioru (zgodny z TFDS i Hugging Face). Zapewnia pełną porównywalność z literaturą oraz zachowuje naturalny balans klas w każdym segmencie.
* Metryka główna i pomocnicze: Główna: `macro-F1` (traktuje każdą klasę z jednakową wagą i penalizuje pomijanie trudniejszych stadiów chorób). Pomocnicze: `accuracy` oraz F1 per klasa (pozwalają ocenić ogólny odsetek poprawnych diagnoz i specyfikę błędów dla danej choroby).
* Seed: 42
* Final test: zamrożony w commicie z tagiem `task-1`, identyfikatory w `splits/final_test_ids.txt`. Całkowita izolacja zbioru testowego zapobiega wyciekowi danych (data leakage) i optymalizacji hiperparametrów pod zbiór końcowy.

| Zbiór | Liczba przykładów | Liczba niezależnych jednostek |
|---|---|---|
| train | 1034 | 1034 |
| validation | 133 | 133 |
| final test | 128 | 128 |

## Wyniki (Zadania 2 do 5)

Wyniki na validation:

| Podejście | Zadanie | Metryka główna | Metryki pomocnicze | Czas i sprzęt | Uwagi |
|---|---|---|---|---|---|
| Trivial baseline | 2 | | | | |
| Baseline | 2 | | | | |
| Podejście pretrained | 3 | | | | |
| Rozszerzenie | 4 | | | | |

Wynik na final test, wyłącznie dla finalnego systemu i dopiero po utworzeniu tagu `final-freeze`:

| System | Metryka główna | Metryki pomocnicze |
|---|---|---|
| [nazwa z `final_system.md`] | | |

## Finalny system (Zadanie 5)

Pełny zapis jest w `final_system.md`. [Krótkie uzasadnienie wyboru na podstawie validation.]

## Reprodukcja

- **Środowisko:** Python 3.12, wirtualne środowisko `venv`.
- **Paczki (Zadanie 1):** `datasets`, `pillow`, `imagehash`, `pandas`, `numpy`.
- **Generowanie podziałów i audyt:** Uruchomienie skryptu `python audit_and_freeze.py`, który pobiera dane i generuje pliki w katalogu `splits/`.
- **Sprzęt:** Desktop PC, CPU AMD Ryzen 7 5700X, 32 GB RAM, system Windows 11.
- **Czas audytu:** ok. 2 minuty (pobranie zbioru, hashowanie MD5 i weryfikacja pHash).

## Ograniczenia

1. **Brak metadanych o roślinach (`plant_id`):** Ryzyko obecności liści z tego samego krzaka po obu stronach podziału. Wnioskowanie dotyczy generalizacji na poziomie obrazu, a nie w pełni niezależnych biologicznie upraw.
2. **Rozmiar zbioru testowego:** 128 próbek oznacza zmianę wyniku o ok. 0.78 p.p. przy pojedynczym błędzie.
3. **Specyfika upraw:** Zdjęcia zebrano w Ugandzie, co może ograniczać transferowalność modelu na inne odmiany fasoli i warunki klimatyczne.

## Dziennik zmian

| Data | Zadanie | Co zmieniono i dlaczego |
|---|---|---|
| 2026-11-08 | Zadanie 1 | Inicjalizacja dokumentacji, audyt danych i zamrożenie podziałów w `splits/`. |

## Licencja projektu

Projekt na licencji MIT. Zbiór danych na licencji MIT (AIR Lab Makerere University).