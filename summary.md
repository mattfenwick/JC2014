# Resonance assignment for a particularly challenging protein based on systematic unlabeling of amino acids to complement incomplete NMR data sets

## Abstract

 - 1st step to NMR structures: resonance assignment
 - standard approaches may fail if low concentration or poor stability
 - new strategy for assignment: specific unlabeling of amino acid types
 - applied strategy to aprataxin
 - aprataxin is difficult to study because it quickly precipitates
 - standard experiments fail on aprataxin
 - approach also validated on GB1
 - studied amino acid scrambling in E. coli as well

## Introduction

 - NMR prerequisites: labeling, high concentration and stability
 - if limited concentration/stability, some experiments start to fail, while the more sensitive ones may continue to work
 - however, these experiments may not give enough information to get unambiguous assignments
 - there are various ways to disambiguate assignments based on specific amino acid types
 - whereas specific labeling is extremely expensive, specific unlabeling is cheap
 - unlabeling is complicated by aa scrambling
 - scrambling is hard to avoid
 - new strategy was validated in GB1
 - then applied to aprataxin
 - aprataxin is linked to ataxia, DNA repair, and colorectal cancer
 - aprataxin is very hard to study using NMR
 - managed to get some chemical shifts assigned

## Materials and methods

### Expression and purification of GB1

 - E. coli BL21(DE3)
 - M9 media, 1 g/l ammonium chloride (15N), 2 g/l glucose (13C)
 - expressed (15N, 13C) GB1 -- T2Q mutant
 - selectively unlabeled: 1 g/l of amino acid (Cys: 0.1 g/l) added 15 min before induction
 - induced with 0.3 mM IPTG for 3 hours, 30 degrees C
 - disrupted harvested cells at 80 degrees C, 15 min, phosphate-buffered saline
 - centrifuged
 - size exclusion chromatography on supernatant
 - combined GB1 fractions
 - added D2O
 - concentrated
 - got ~30 mg of protein from 250 ml M9

### Expression and purification of aprataxin

 - pET-15b expression plasmid:  residues 161-356 of human aprataxin
 - enzymatically active histidine triad domain and zinc finger motif
 - E. coli BL21(DE3)
 - His-tag
 - M9 media, 1 g/l (15N)H4Cl, 1.5 g/l (13C)glucose, 10 micromolar ZnSO4
 - selectively unlabeled: 1 g/l of amino acid (Cys: 0.1 g/l) added 15 min before induction
 - induced with 0.3 mM IPTG for 3 hours, 30 degrees C
 - disrupted harvested cells with French Press, ultrasonification
 - centrifuged
 - affinity chromatography of supernatant
 - thrombin cleavage and dialysis
 - anion exchange chromatography
 - concentrated and moved into NMR buffer
 - 5 mg protein from 200 ml M9

### NMR experiments

 - Bruker 750 Avance III
 - 25 C -- GB1
 - 29 C -- aprataxin
 - GB1 -- 2.3 mM -- HNCO, HN(CA)CO
 - aprataxin: 0.5 mM
   - 16 hours, HNCO
   - 66 hours, HN(CA)CO
   - 44 hours, HNCA
   - 44 hours, HN(CO)CA
   - 89 hours, HNCACB
 - concentration dropped from 0.5 mM to 0.1 mM after "several hours", and to 0.05 mM after "one day"
 - data was inadequate for unambiguous assignments
 - collected unlabeling experiments
   - NHSQC
   - HN(CO)
   - GB1: 2 hours
   - aprataxin: 6 hours
 
### Data analysis

 - used CCPN
 - TopSpin provided peak intensities
 - processing: ?????????????

