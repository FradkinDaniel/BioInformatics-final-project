# Cell Differentiation Transcription Factor Analysis

**Bio‑Informatics High‑School Project – 2 Unit Submission (June 2015)**
Authors: *Daniel צאלון (Daniel Tsalon) & Guy Tal*
Supervisor: Dr Zohar Yitzhaki

---

## Project Summary

This repository contains a **small Python toolkit** that scans gene‑sequence FASTA files and identifies genes that are potential binding targets of **five pluripotency / cell‑cycle transcription factors**:

| Factor | Regex motif used (`re` syntax)               |
| ------ | -------------------------------------------- |
| OCT4   | `ATTTGCAT`                                   |
| SOX2   | `ATTTGCAT`                                   |
| KLF4   | `CACCC`                                      |
| MYC    | `CAC[GA]TC`                                  |
| E2F1   | `TTTC[CG]CGC`                                |
| NANOG  | `TTTC[CG]CGC` / `[CG][GA][CG]C[GC]ATTAN[GC]` |

The pipeline:

1. **`findCommonGenes.py`**

   * Reads a FASTA‑style file named `data` (example provided).
   * Extracts each gene record, searches for the above motifs, and records every gene that matches at least one motif.
   * Produces **`gene.txt`** – a tab‑separated list of `<motif>\t<gene‑name>` pairs.

2. **`rewrite.py`**

   * Counts how many motifs point to the *same* gene.
   * Writes genes that appear **more than once** to **`finaly.txt`** – the “consensus” set for downstream functional‑enrichment analysis (e.g., DAVID).

> The original investigation used DAVID to confirm that these candidate genes are indeed enriched for cell‑cycle and differentiation processes.

---

## Repository Layout

```
├── data                          # Example FASTA input (hg19_refGene excerpt)
├── findCommonGenes.py            # Motif‑scan script
├── rewrite.py                    # Post‑processing script
└── README.md                     # (You are here)
```

---

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/<your-user>/<repo>.git
cd <repo>

# 2. (Optional) create a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Run the motif scan
python findCommonGenes.py          # creates gene.txt

# 4. Filter genes that hit ≥2 motifs
python rewrite.py                  # creates finaly.txt
```

### Input Format

`data` should be a plain‑text FASTA file in which each gene starts with a header line beginning with `>` followed by sequence lines.

### Output Files

| File         | Description                                      |
| ------------ | ------------------------------------------------ |
| `gene.txt`   | All genes that match *any* motif (one per line). |
| `finaly.txt` | Genes matched by **two or more** motifs.         |

---

## Requirements

* Python 3.8+
* Standard library only (`re`, `sys`, …) – no external packages required.

---

## Extending the Project

* **Add more motifs** – extend the `trascription` list in `findCommonGenes.py`.
* **Adjust thresholds** – change the `>1` condition in `rewrite.py`.
* **Visualise results** – feed `finaly.txt` into DAVID, Enrichr, or GOATOOLS.

Feel free to open an issue or PR with improvements!

---

## License

MIT License (see `LICENSE`).

---

## Acknowledgements

Inspired by the 2015 high‑school bioinformatics curriculum and the UCSC `hg19_refGene` database.
