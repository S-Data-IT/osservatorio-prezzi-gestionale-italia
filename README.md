# Osservatorio prezzi: gestionale su misura in Italia (2026)

Dataset aperto con le fasce di prezzo che **12 software house e professionisti italiani pubblicano sui loro siti** per un software gestionale su misura (piccolo progetto o primo modulo, gestionale con più moduli, gestionale completo/ERP). Rilevazione del **22 ottobre 2026**, prezzi **IVA esclusa** salvo dove indicato.

- Pagina con tabelle, fonti e metodo: <https://www.s-data.it/osservatorio-prezzi-gestionale-su-misura-2026.html>
- Dati: [`osservatorio-prezzi-gestionale-2026.csv`](osservatorio-prezzi-gestionale-2026.csv) (13 righe: 12 fonti, con due pagine per LEMIO)
- Ricalcolo delle mediane: [`mediane.py`](mediane.py) (solo libreria standard di Python 3)
- Licenza: [CC BY 4.0](LICENSE)

## Risultato in breve

Mediane dei prezzi dichiarati dalle 9 fonti che pubblicano cifre per almeno due fasce (IVA esclusa):

| Fascia | Mediana dei minimi | Mediana dei massimi |
|---|---|---|
| Piccolo progetto o primo modulo | 5.000 € | 13.500 € |
| Gestionale con più moduli collegati | 15.000 € | 22.000 € |
| Gestionale completo / ERP | 37.500 € | 40.000 € (molte fonti scrivono «oltre») |

Sono **prezzi pubblicati, non preventivi chiusi**, raccolti su un campione piccolo: leggi i limiti qui sotto prima di citarli.

## Cosa contiene il CSV

| Colonna | Significato |
|---|---|
| `id` | numero della fonte (`1b` = seconda pagina della stessa azienda) |
| `fonte`, `url` | nome e pagina pubblica letta |
| `data_rilevazione` | giorno di lettura |
| `piccolo_*`, `medio_*`, `grande_*` (`_min_eur`, `_max_eur`) | minimo e massimo dichiarati in euro; vuoto = non dichiarato. Per «oltre X» è riportato solo X come minimo |
| `manutenzione_annua` | come scritta dalla fonte |
| `tempi_dichiarati` | tempi dichiarati dalla fonte, per fascia |
| `software_house_per_pmi` | classificazione nostra (`si`/`no`), per come l'azienda si presenta sul proprio sito |
| `entra_nelle_mediane` | `si`/`no` |
| `note` | scelte di lettura e casi particolari |

Codifica UTF-8, separatore virgola, campi di testo tra virgolette.

## Metodologia (onesta)

1. Il 22 ottobre 2026 abbiamo cercato sul web pagine italiane che pubblicano i prezzi di un gestionale su misura. **Non è un campione casuale**: sono le pagine che la ricerca ha mostrato.
2. Per ogni pagina abbiamo trascritto a mano le cifre dichiarate per un progetto piccolo, medio e grande.
3. **9 fonti su 12 entrano nelle mediane**: quelle che pubblicano cifre per almeno due fasce. Le altre tre (Mariano Matera, B.NET, Studio JEM) pubblicano una sola fascia o nessun listino.
4. Una sola pagina per azienda: per LEMIO conta il listino, non l'articolo del blog (le due pagine riportano fasce diverse, entrambe sono nel CSV).
5. Per ogni fascia si calcola la mediana dei minimi e la mediana dei massimi. Dove la fonte scrive «oltre X» si usa X come minimo e non c'è un massimo: per questo le mediane dei massimi, soprattutto per i progetti grandi, si basano su meno fonti (8 e 6 per la fascia grande).
6. Si calcola anche la mediana solo sulle 5 software house che si rivolgono alle PMI (LEMIO, NovaMarte, Ctrl Studio, Garda Informatica, CityGraph). La classificazione è nostra. `mediane.py` stampa entrambe.
7. Le fasce di prezzo di S-Data **non sono nei dati e non entrano in nessun calcolo**.

## Limiti

- Prezzi pubblicati, non prezzi chiusi: un preventivo reale può essere più alto o più basso.
- Campione piccolo (9 fonti nelle mediane), trovato con una ricerca, non rappresentativo di tutto il mercato italiano.
- Le pagine sono scritte da chi vende il servizio: possono essere ottimistiche o rivolte a clienti di dimensione diversa (le agenzie orientate ai clienti più grandi pubblicano cifre molto più alte).
- «Piccolo», «medio», «grande» non significano la stessa cosa per tutte le fonti; alcune cifre sono per modulo, reparto o verticale.
- Le pagine citate possono essere cambiate dopo il 22 ottobre 2026.
- **Conflitto di interessi dichiarato:** S-Data sviluppa software gestionale su misura ed è quindi un operatore di questo mercato. Per questo le sue fasce restano fuori dal dataset.

Se sei una delle aziende citate e una cifra non è corretta, scrivi a info@s-data.it: verifichiamo e correggiamo.

## Licenza e come citare

Il dataset (raccolta, selezione e calcoli) è rilasciato con licenza [Creative Commons Attribuzione 4.0 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.it): puoi riusarlo, copiarlo e rielaborarlo, anche per scopi commerciali, citando la fonte. Le cifre di partenza sono fatti pubblicati dalle aziende citate.

Formula consigliata:

> S-Data, «Osservatorio prezzi gestionale su misura 2026», rilevazione del 22 ottobre 2026. https://www.s-data.it/osservatorio-prezzi-gestionale-su-misura-2026.html. Licenza CC BY 4.0.

Se rielabori i dati, indica che li hai modificati.

## Autore

[S-Data](https://www.s-data.it) di Braga Simone, software house dal 2007: software gestionale su misura, web app e integrazioni per PMI.
