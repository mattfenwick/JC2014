import nmrpystar.examples


url = "http://rest.bmrb.wisc.edu/bmrb/NMR-STAR3/19182"


out = nmrpystar.examples.parseUrl(url)
val = out.value


d = val[1] # the data block
sav = d.saves['assigned_chem_shift_list_1'] # chemical shifts


shifts = []
residues = {}
for r in sav.loops[1].rows:
    resid, shift = int(r[4]), float(r[10])
    aatype, atom = r[6], r[7]
    shifts.append((resid, aatype, atom, shift))
    if not residues.has_key(resid):
        residues[resid] = {'aatype': aatype}
    residues[resid][atom] = shift


# ideas:
#  1. find the overall amount of CA overlap
#  2. find residues with similar CA/C shifts

# 2
def get_overlap(tol_c=0.1, tol_ca=0.1):
  for (i1,r1) in residues.items():
    for (i2,r2) in residues.items():
      if i1 >= i2:
        continue
      if 'C' in r1 and 'C' in r2 and (abs(r1['C'] - r2['C']) < tol_c):
        if 'CA' in r1 and 'CA' in r2 and (abs(r1['CA'] - r2['CA']) < tol_ca):
          print i1, r1
          print i2, r2
          print
# better idea: build them into groups by shifts, that
#  way, more than 2 can be in the same group



gb1_seq = 'MQYKLILNGK' + 'TLKGETTTEA' + 'VDAATAEKVF' + 'KQYANDNGVD' + 'GEWTYDDATK' + 'TFTVTE'
gb1_sequence = dict(enumerate(gb1_seq, start=1))

# first six are from the pET15b vector -- so C161 is the first real residue
apr_seq = 'GSHMLECSVPLKKGKDAPIKKESLGHWSQGLKISMQDPKMQVYKDEQVVVIKDKYPKARYHWLVLPWTSISSLKAVAREHLELLKHMHTVGEKVIVDFAGSSKLRFRLGYHAIPSMSHVHLHVISQDFDSPCLKNKKHWNSFNTEYFLESQAVIEMVQEAGRVTVRDGMPELLKLPLRCHECQQLLPSIPQLKEHLRKHWTQ'
apr_sequence = dict(enumerate(apr_seq, start=155))

