#!/usr/bin/env python3
"""Ricalcola le mediane dell'Osservatorio prezzi gestionale su misura 2026.

Uso: python3 mediane.py [osservatorio-prezzi-gestionale-2026.csv]
Entrano nel calcolo solo le righe con entra_nelle_mediane = si.
I campi vuoti (valore non dichiarato) vengono ignorati.
"""
import csv
import statistics
import sys

path = sys.argv[1] if len(sys.argv) > 1 else "osservatorio-prezzi-gestionale-2026.csv"
with open(path, encoding="utf-8", newline="") as f:
    righe = list(csv.DictReader(f))

def mediane(sel, titolo):
    print(f"\n{titolo} ({len(sel)} fonti)")
    for fascia in ("piccolo", "medio", "grande"):
        for lato in ("min", "max"):
            v = [float(r[f"{fascia}_{lato}_eur"]) for r in sel if r[f"{fascia}_{lato}_eur"]]
            if v:
                print(f"  {fascia:8s} mediana dei {lato}: {statistics.median(v):>9,.0f} EUR  (su {len(v)} fonti)")

nelle = [r for r in righe if r["entra_nelle_mediane"] == "si"]
mediane(nelle, "Tutte le fonti incluse nelle mediane")
mediane([r for r in nelle if r["software_house_per_pmi"] == "si"], "Solo software house per PMI (classificazione S-Data)")
