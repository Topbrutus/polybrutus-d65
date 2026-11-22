# Polybrutus D65 — proof-first validation and controlled publication

1. Direct scientific parent D64 frozen v0.1.0 peeled Git commit acc49976f17add61804888d15f3e1898e549ce60, DOI 10.5281/zenodo.24432481, entire original source ZIP SHA256 c43fdc3487fd226eb63d790f3bd4e7e26afb84b58d8b8947b0ad2a265c2dce71, certificate SHA256 ad281b486054b8e756a3d30d8b5a4b0ce313f07310b6cc94940f1dc841100207. Both exact programs validate original ZIP SHA/CRC, original certificate bytes and inherited labels.
2. Exhaust all 70 norm-one points and 2415 labelled exact squared distances; 2346 unchanged old D64 pairs and 69 new squared distances 2R²; Euclidean Gram and centered Gram PSD rank 65.
3. Two independent implementations (SymPy exact Gram vs fractions.Fraction separate pair rules), four adversarial negative controls, exact deterministic certificate. Chosen dimensionless ideal graph eigenvalue 35 mult 59 and 69/2 mult 4.
4. Scientific GitHub initial main CI must pass, then freeze source tag v0.1.0 and require tag CI green; after public Zenodo DOI document on main and require third green CI.
5. Public Zenodo originals: full frozen Git scientific source ZIP, two-page mathematical PDF and exact deterministic certificate JSON; all 3 filenames, sizes and MD5 from public API match SHA256-verified originals. Nine current D65 sixty-five/fifty-ninefold keywords, structured isDerivedFrom direct D64 DOI, separate D64/D7 textual bibliography.
6. Preserve entire historic original source ZIP nesting unchanged, disclose D47/D46 historical parent text SHA mistake, never claim physical spacetime, measured hertz or new universal theorem.

    python -m pip install sympy==1.14.0
    python src/verify_d65.py
    python tests/independent_d65.py
    python src/check_zenodo_metadata.py
