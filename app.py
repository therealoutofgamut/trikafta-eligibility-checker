
import streamlit as st
from difflib import get_close_matches

alias_lookup = {
  "c.1521_1523del|1653delCTT": [
    "c.1521_1523del|1653delCTT",
    "p.Phe508del",
    "c.1521_1523del",
    "F508del"
  ],
  "p.Phe508del": [
    "c.1521_1523del|1653delCTT",
    "p.Phe508del",
    "c.1521_1523del",
    "F508del"
  ],
  "c.1521_1523del": [
    "c.1521_1523del|1653delCTT",
    "p.Phe508del",
    "c.1521_1523del",
    "F508del"
  ],
  "F508del": [
    "c.1521_1523del|1653delCTT",
    "p.Phe508del",
    "c.1521_1523del",
    "F508del"
  ],
  "G542X": [
    "G542X",
    "p.Gly542X",
    "c.1624G>T",
    "1756G>T"
  ],
  "p.Gly542X": [
    "G542X",
    "p.Gly542X",
    "c.1624G>T",
    "1756G>T"
  ],
  "c.1624G>T": [
    "G542X",
    "p.Gly542X",
    "c.1624G>T",
    "1756G>T"
  ],
  "1756G>T": [
    "G542X",
    "p.Gly542X",
    "c.1624G>T",
    "1756G>T"
  ],
  "1784G>A": [
    "1784G>A",
    "c.1652G>A",
    "p.Gly551Asp",
    "G551D"
  ],
  "c.1652G>A": [
    "1784G>A",
    "c.1652G>A",
    "p.Gly551Asp",
    "G551D"
  ],
  "p.Gly551Asp": [
    "1784G>A",
    "c.1652G>A",
    "p.Gly551Asp",
    "G551D"
  ],
  "G551D": [
    "1784G>A",
    "c.1652G>A",
    "p.Gly551Asp",
    "G551D"
  ],
  "c.3909C>G": [
    "c.3909C>G",
    "N1303K",
    "p.Asn1303Lys",
    "4041C>G"
  ],
  "N1303K": [
    "c.3909C>G",
    "N1303K",
    "p.Asn1303Lys",
    "4041C>G"
  ],
  "p.Asn1303Lys": [
    "c.3909C>G",
    "N1303K",
    "p.Asn1303Lys",
    "4041C>G"
  ],
  "4041C>G": [
    "c.3909C>G",
    "N1303K",
    "p.Asn1303Lys",
    "4041C>G"
  ],
  "p.Trp1282X": [
    "p.Trp1282X",
    "W1282X",
    "c.3845G>A|c.3846G>A",
    "3978G>A"
  ],
  "W1282X": [
    "p.Trp1282X",
    "W1282X",
    "c.3845G>A|c.3846G>A",
    "3978G>A"
  ],
  "c.3845G>A|c.3846G>A": [
    "p.Trp1282X",
    "W1282X",
    "c.3845G>A|c.3846G>A",
    "3978G>A"
  ],
  "3978G>A": [
    "p.Trp1282X",
    "W1282X",
    "c.3845G>A|c.3846G>A",
    "3978G>A"
  ],
  "p.Arg117His": [
    "p.Arg117His",
    "R117H",
    "482G>A",
    "c.350G>A"
  ],
  "R117H": [
    "p.Arg117His",
    "R117H",
    "482G>A",
    "c.350G>A"
  ],
  "482G>A": [
    "p.Arg117His",
    "R117H",
    "482G>A",
    "c.350G>A"
  ],
  "c.350G>A": [
    "p.Arg117His",
    "R117H",
    "482G>A",
    "c.350G>A"
  ],
  "c.3717+12191C>T|3850-2477C->T|3849+12191C->T": [
    "c.3717+12191C>T|3850-2477C->T|3849+12191C->T",
    "p.?",
    "c.3718-2477C>T",
    "3849+10kbC->T"
  ],
  "p.?": [
    "c.273+7982del18652",
    "p.?",
    "405+7982del18652"
  ],
  "c.3718-2477C>T": [
    "c.3717+12191C>T|3850-2477C->T|3849+12191C->T",
    "p.?",
    "c.3718-2477C>T",
    "3849+10kbC->T"
  ],
  "3849+10kbC->T": [
    "c.3717+12191C>T|3850-2477C->T|3849+12191C->T",
    "p.?",
    "c.3718-2477C>T",
    "3849+10kbC->T"
  ],
  "621+1G->T": [
    "p.?",
    "621+1G->T",
    "c.489+1G>T"
  ],
  "c.489+1G>T": [
    "p.?",
    "621+1G->T",
    "c.489+1G>T"
  ],
  "c.1657C>T": [
    "c.1657C>T",
    "R553X",
    "p.Arg553X",
    "1789C>T"
  ],
  "R553X": [
    "c.1657C>T",
    "R553X",
    "p.Arg553X",
    "1789C>T"
  ],
  "p.Arg553X": [
    "c.1657C>T",
    "R553X",
    "p.Arg553X",
    "1789C>T"
  ],
  "1789C>T": [
    "c.1657C>T",
    "R553X",
    "p.Arg553X",
    "1789C>T"
  ],
  "c.2657+5G>A": [
    "c.2657+5G>A",
    "p.?",
    "2789+5G->A"
  ],
  "2789+5G->A": [
    "c.2657+5G>A",
    "p.?",
    "2789+5G->A"
  ],
  "1717-1G->A": [
    "1717-1G->A",
    "p.?",
    "c.1585-1G>A"
  ],
  "c.1585-1G>A": [
    "1717-1G->A",
    "p.?",
    "c.1585-1G>A"
  ],
  "deletion of exons 2 and 3 (legacy and current numbering)": [
    "deletion of exons 2 and 3 (legacy and current numbering)",
    "CFTRdele2,3",
    "c.(53+1_54-1)_(273+1_274-1)del",
    "p.?"
  ],
  "CFTRdele2,3": [
    "deletion of exons 2 and 3 (legacy and current numbering)",
    "CFTRdele2,3",
    "c.(53+1_54-1)_(273+1_274-1)del",
    "p.?"
  ],
  "c.(53+1_54-1)_(273+1_274-1)del": [
    "deletion of exons 2 and 3 (legacy and current numbering)",
    "CFTRdele2,3",
    "c.(53+1_54-1)_(273+1_274-1)del",
    "p.?"
  ],
  "3586G>C": [
    "3586G>C",
    "p.Asp1152His",
    "c.3454G>C",
    "D1152H"
  ],
  "p.Asp1152His": [
    "3586G>C",
    "p.Asp1152His",
    "c.3454G>C",
    "D1152H"
  ],
  "c.3454G>C": [
    "3586G>C",
    "p.Asp1152His",
    "c.3454G>C",
    "D1152H"
  ],
  "D1152H": [
    "3586G>C",
    "p.Asp1152His",
    "c.3454G>C",
    "D1152H"
  ],
  "386G>A": [
    "386G>A",
    "p.Gly85Glu",
    "G85E",
    "c.254G>A"
  ],
  "p.Gly85Glu": [
    "386G>A",
    "p.Gly85Glu",
    "G85E",
    "c.254G>A"
  ],
  "G85E": [
    "386G>A",
    "p.Gly85Glu",
    "G85E",
    "c.254G>A"
  ],
  "c.254G>A": [
    "386G>A",
    "p.Gly85Glu",
    "G85E",
    "c.254G>A"
  ],
  "p.Arg1162X": [
    "p.Arg1162X",
    "3616C>T",
    "R1162X",
    "c.3484C>T"
  ],
  "3616C>T": [
    "p.Arg1162X",
    "3616C>T",
    "R1162X",
    "c.3484C>T"
  ],
  "R1162X": [
    "p.Arg1162X",
    "3616C>T",
    "R1162X",
    "c.3484C>T"
  ],
  "c.3484C>T": [
    "p.Arg1162X",
    "3616C>T",
    "R1162X",
    "c.3484C>T"
  ],
  "p.Arg334Trp": [
    "p.Arg334Trp",
    "c.1000C>T",
    "R334W",
    "1132C>T"
  ],
  "c.1000C>T": [
    "p.Arg334Trp",
    "c.1000C>T",
    "R334W",
    "1132C>T"
  ],
  "R334W": [
    "p.Arg334Trp",
    "c.1000C>T",
    "R334W",
    "1132C>T"
  ],
  "1132C>T": [
    "p.Arg334Trp",
    "c.1000C>T",
    "R334W",
    "1132C>T"
  ],
  "3272-26A->G": [
    "p.?",
    "3272-26A->G",
    "c.3140-26A>G"
  ],
  "c.3140-26A>G": [
    "p.?",
    "3272-26A->G",
    "c.3140-26A>G"
  ],
  "3120+1G->A": [
    "3120+1G->A",
    "c.2988+1G>A",
    "p.?"
  ],
  "c.2988+1G>A": [
    "3120+1G->A",
    "c.2988+1G>A",
    "p.?"
  ],
  "p.Lys684SerfsX38": [
    "p.Lys684SerfsX38",
    "2183delAA->G",
    "2183AA->G",
    "c.2051_2052delinsG"
  ],
  "2183delAA->G": [
    "p.Lys684SerfsX38",
    "2183delAA->G",
    "2183AA->G",
    "c.2051_2052delinsG"
  ],
  "2183AA->G": [
    "p.Lys684SerfsX38",
    "2183delAA->G",
    "2183AA->G",
    "c.2051_2052delinsG"
  ],
  "c.2051_2052delinsG": [
    "p.Lys684SerfsX38",
    "2183delAA->G",
    "2183AA->G",
    "c.2051_2052delinsG"
  ],
  "c.1519_1521del|c.1516_1518delATC|I506del|p.Ile506del|1651delATC": [
    "c.1519_1521del|c.1516_1518delATC|I506del|p.Ile506del|1651delATC",
    "c.1519_1521del",
    "p.Ile507del",
    "I507del"
  ],
  "c.1519_1521del": [
    "c.1519_1521del|c.1516_1518delATC|I506del|p.Ile506del|1651delATC",
    "c.1519_1521del",
    "p.Ile507del",
    "I507del"
  ],
  "p.Ile507del": [
    "c.1519_1521del|c.1516_1518delATC|I506del|p.Ile506del|1651delATC",
    "c.1519_1521del",
    "p.Ile507del",
    "I507del"
  ],
  "I507del": [
    "c.1519_1521del|c.1516_1518delATC|I506del|p.Ile506del|1651delATC",
    "c.1519_1521del",
    "p.Ile507del",
    "I507del"
  ],
  "c.1040G>C": [
    "c.1040G>C",
    "1172G>C",
    "p.Arg347Pro",
    "R347P"
  ],
  "1172G>C": [
    "c.1040G>C",
    "1172G>C",
    "p.Arg347Pro",
    "R347P"
  ],
  "p.Arg347Pro": [
    "c.1040G>C",
    "1172G>C",
    "p.Arg347Pro",
    "R347P"
  ],
  "R347P": [
    "c.1040G>C",
    "1172G>C",
    "p.Arg347Pro",
    "R347P"
  ],
  "2184insA": [
    "2184insA",
    "c.2052dup",
    "c.2052_2053insA|2185insA",
    "p.Gln685ThrfsX4"
  ],
  "c.2052dup": [
    "2184insA",
    "c.2052dup",
    "c.2052_2053insA|2185insA",
    "p.Gln685ThrfsX4"
  ],
  "c.2052_2053insA|2185insA": [
    "2184insA",
    "c.2052dup",
    "c.2052_2053insA|2185insA",
    "p.Gln685ThrfsX4"
  ],
  "p.Gln685ThrfsX4": [
    "2176insC",
    "c.2045dup",
    "p.Gln685ThrfsX4"
  ],
  "p.Lys1177SerfsX15": [
    "c.3530del",
    "p.Lys1177SerfsX15",
    "3662delA"
  ],
  "3659delC": [
    "p.Lys1177SerfsX15",
    "3659delC",
    "c.3528del"
  ],
  "c.3528del": [
    "p.Lys1177SerfsX15",
    "3659delC",
    "c.3528del"
  ],
  "c.617T>G": [
    "c.617T>G",
    "749T>G",
    "p.Leu206Trp",
    "L206W"
  ],
  "749T>G": [
    "c.617T>G",
    "749T>G",
    "p.Leu206Trp",
    "L206W"
  ],
  "p.Leu206Trp": [
    "c.617T>G",
    "749T>G",
    "p.Leu206Trp",
    "L206W"
  ],
  "L206W": [
    "c.617T>G",
    "749T>G",
    "p.Leu206Trp",
    "L206W"
  ],
  "5T": [
    "5T",
    "p.?",
    "c.1210-12T[5]"
  ],
  "c.1210-12T[5]": [
    "5T",
    "p.?",
    "c.1210-12T[5]"
  ],
  "1496C>A": [
    "1496C>A",
    "p.Ala455Glu",
    "A455E",
    "c.1364C>A"
  ],
  "p.Ala455Glu": [
    "1496C>A",
    "p.Ala455Glu",
    "A455E",
    "c.1364C>A"
  ],
  "A455E": [
    "1496C>A",
    "p.Ala455Glu",
    "A455E",
    "c.1364C>A"
  ],
  "c.1364C>A": [
    "1496C>A",
    "p.Ala455Glu",
    "A455E",
    "c.1364C>A"
  ],
  "5T;TG12": [
    "5T;TG12",
    "p.?",
    "c.1210-11T>G",
    "c.1210-33_1210-6GT[12]T[4]"
  ],
  "c.1210-11T>G": [
    "5T;TG12",
    "p.?",
    "c.1210-11T>G",
    "c.1210-33_1210-6GT[12]T[4]"
  ],
  "c.1210-33_1210-6GT[12]T[4]": [
    "5T;TG12",
    "p.?",
    "c.1210-11T>G",
    "c.1210-33_1210-6GT[12]T[4]"
  ],
  "c.1766+1G>A": [
    "p.?",
    "c.1766+1G>A",
    "1898+1G->A"
  ],
  "1898+1G->A": [
    "p.?",
    "c.1766+1G>A",
    "1898+1G->A"
  ],
  "3328C>T": [
    "3328C>T",
    "c.3196C>T",
    "R1066C",
    "p.Arg1066Cys"
  ],
  "c.3196C>T": [
    "3328C>T",
    "c.3196C>T",
    "R1066C",
    "p.Arg1066Cys"
  ],
  "R1066C": [
    "3328C>T",
    "c.3196C>T",
    "R1066C",
    "p.Arg1066Cys"
  ],
  "p.Arg1066Cys": [
    "3328C>T",
    "c.3196C>T",
    "R1066C",
    "p.Arg1066Cys"
  ],
  "p.Tyr515X": [
    "p.Tyr515X",
    "1677delTA",
    "c.1545_1546del"
  ],
  "1677delTA": [
    "p.Tyr515X",
    "1677delTA",
    "c.1545_1546del"
  ],
  "c.1545_1546del": [
    "p.Tyr515X",
    "1677delTA",
    "c.1545_1546del"
  ],
  "[482G>A with 1342-12T[7]]|R117H with 7T": [
    "[482G>A with 1342-12T[7]]|R117H with 7T",
    "c.[350G>A;1210-12T[7]]",
    "R117H;7T"
  ],
  "c.[350G>A;1210-12T[7]]": [
    "[482G>A with 1342-12T[7]]|R117H with 7T",
    "c.[350G>A;1210-12T[7]]",
    "R117H;7T"
  ],
  "R117H;7T": [
    "[482G>A with 1342-12T[7]]|R117H with 7T",
    "c.[350G>A;1210-12T[7]]",
    "R117H;7T"
  ],
  "394delTT": [
    "394delTT",
    "p.Leu88IlefsX22",
    "c.262_263del"
  ],
  "p.Leu88IlefsX22": [
    "394delTT",
    "p.Leu88IlefsX22",
    "c.262_263del"
  ],
  "c.262_263del": [
    "394delTT",
    "p.Leu88IlefsX22",
    "c.262_263del"
  ],
  "711+1G->T": [
    "p.?",
    "711+1G->T",
    "c.579+1G>T"
  ],
  "c.579+1G>T": [
    "p.?",
    "711+1G->T",
    "c.579+1G>T"
  ],
  "R560T": [
    "R560T",
    "1811G>C",
    "p.Arg560Thr",
    "c.1679G>C"
  ],
  "1811G>C": [
    "R560T",
    "1811G>C",
    "p.Arg560Thr",
    "c.1679G>C"
  ],
  "p.Arg560Thr": [
    "R560T",
    "1811G>C",
    "p.Arg560Thr",
    "c.1679G>C"
  ],
  "c.1679G>C": [
    "R560T",
    "1811G>C",
    "p.Arg560Thr",
    "c.1679G>C"
  ],
  "c.1477C>T": [
    "c.1477C>T",
    "p.Gln493X",
    "Q493X",
    "1609C>T"
  ],
  "p.Gln493X": [
    "c.1477C>T",
    "p.Gln493X",
    "Q493X",
    "1609C>T"
  ],
  "Q493X": [
    "c.1477C>T",
    "p.Gln493X",
    "Q493X",
    "1609C>T"
  ],
  "1609C>T": [
    "c.1477C>T",
    "p.Gln493X",
    "Q493X",
    "1609C>T"
  ],
  "p.Lys684AsnfsX38": [
    "p.Lys684AsnfsX38",
    "2184delA",
    "c.2052del"
  ],
  "2184delA": [
    "p.Lys684AsnfsX38",
    "2184delA",
    "c.2052del"
  ],
  "c.2052del": [
    "p.Lys684AsnfsX38",
    "2184delA",
    "c.2052del"
  ],
  "M470V": [
    "M470V",
    "p.Met470Val",
    "1540A>G",
    "c.1408A>G"
  ],
  "p.Met470Val": [
    "M470V",
    "p.Met470Val",
    "1540A>G",
    "c.1408A>G"
  ],
  "1540A>G": [
    "M470V",
    "p.Met470Val",
    "1540A>G",
    "c.1408A>G"
  ],
  "c.1408A>G": [
    "M470V",
    "p.Met470Val",
    "1540A>G",
    "c.1408A>G"
  ],
  "c.178G>T": [
    "c.178G>T",
    "p.Glu60X",
    "310G>T",
    "E60X"
  ],
  "p.Glu60X": [
    "c.178G>T",
    "p.Glu60X",
    "310G>T",
    "E60X"
  ],
  "310G>T": [
    "c.178G>T",
    "p.Glu60X",
    "310G>T",
    "E60X"
  ],
  "E60X": [
    "c.178G>T",
    "p.Glu60X",
    "310G>T",
    "E60X"
  ],
  "c.200C>T": [
    "c.200C>T",
    "p.Pro67Leu",
    "332C>T",
    "P67L"
  ],
  "p.Pro67Leu": [
    "c.200C>T",
    "p.Pro67Leu",
    "332C>T",
    "P67L"
  ],
  "332C>T": [
    "c.200C>T",
    "p.Pro67Leu",
    "332C>T",
    "P67L"
  ],
  "P67L": [
    "c.200C>T",
    "p.Pro67Leu",
    "332C>T",
    "P67L"
  ],
  "c.1022_1023insTC": [
    "c.1022_1023insTC",
    "c.1021_1022dup",
    "p.Phe342HisfsX28",
    "1154insTC"
  ],
  "c.1021_1022dup": [
    "c.1022_1023insTC",
    "c.1021_1022dup",
    "p.Phe342HisfsX28",
    "1154insTC"
  ],
  "p.Phe342HisfsX28": [
    "c.1022_1023insTC",
    "c.1021_1022dup",
    "p.Phe342HisfsX28",
    "1154insTC"
  ],
  "1154insTC": [
    "c.1022_1023insTC",
    "c.1021_1022dup",
    "p.Phe342HisfsX28",
    "1154insTC"
  ],
  "p.Arg117Cys": [
    "p.Arg117Cys",
    "481C>T",
    "R117C",
    "c.349C>T"
  ],
  "481C>T": [
    "p.Arg117Cys",
    "481C>T",
    "R117C",
    "c.349C>T"
  ],
  "R117C": [
    "p.Arg117Cys",
    "481C>T",
    "R117C",
    "c.349C>T"
  ],
  "c.349C>T": [
    "p.Arg117Cys",
    "481C>T",
    "R117C",
    "c.349C>T"
  ],
  "p.Arg347His": [
    "p.Arg347His",
    "1172G>A",
    "R347H",
    "c.1040G>A"
  ],
  "1172G>A": [
    "p.Arg347His",
    "1172G>A",
    "R347H",
    "c.1040G>A"
  ],
  "R347H": [
    "p.Arg347His",
    "1172G>A",
    "R347H",
    "c.1040G>A"
  ],
  "c.1040G>A": [
    "p.Arg347His",
    "1172G>A",
    "R347H",
    "c.1040G>A"
  ],
  "Y1092X(C->A)|Y1092X(C->G)|3408C>A|3408C>G": [
    "Y1092X(C->A)|Y1092X(C->G)|3408C>A|3408C>G",
    "Y1092X",
    "p.Tyr1092X",
    "c.3276C>A|c.3276C>G"
  ],
  "Y1092X": [
    "Y1092X(C->A)|Y1092X(C->G)|3408C>A|3408C>G",
    "Y1092X",
    "p.Tyr1092X",
    "c.3276C>A|c.3276C>G"
  ],
  "p.Tyr1092X": [
    "Y1092X(C->A)|Y1092X(C->G)|3408C>A|3408C>G",
    "Y1092X",
    "p.Tyr1092X",
    "c.3276C>A|c.3276C>G"
  ],
  "c.3276C>A|c.3276C>G": [
    "Y1092X(C->A)|Y1092X(C->G)|3408C>A|3408C>G",
    "Y1092X",
    "p.Tyr1092X",
    "c.3276C>A|c.3276C>G"
  ],
  "p.Arg1158X": [
    "p.Arg1158X",
    "c.3472C>T",
    "3604C>T",
    "R1158X"
  ],
  "c.3472C>T": [
    "p.Arg1158X",
    "c.3472C>T",
    "3604C>T",
    "R1158X"
  ],
  "3604C>T": [
    "p.Arg1158X",
    "c.3472C>T",
    "3604C>T",
    "R1158X"
  ],
  "R1158X": [
    "p.Arg1158X",
    "c.3472C>T",
    "3604C>T",
    "R1158X"
  ],
  "3434T>A": [
    "3434T>A",
    "p.Met1101Lys",
    "c.3302T>A",
    "M1101K"
  ],
  "p.Met1101Lys": [
    "3434T>A",
    "p.Met1101Lys",
    "c.3302T>A",
    "M1101K"
  ],
  "c.3302T>A": [
    "3434T>A",
    "p.Met1101Lys",
    "c.3302T>A",
    "M1101K"
  ],
  "M1101K": [
    "3434T>A",
    "p.Met1101Lys",
    "c.3302T>A",
    "M1101K"
  ],
  "E92K": [
    "E92K",
    "c.274G>A",
    "406G>A",
    "p.Glu92Lys"
  ],
  "c.274G>A": [
    "E92K",
    "c.274G>A",
    "406G>A",
    "p.Glu92Lys"
  ],
  "406G>A": [
    "E92K",
    "c.274G>A",
    "406G>A",
    "p.Glu92Lys"
  ],
  "p.Glu92Lys": [
    "E92K",
    "c.274G>A",
    "406G>A",
    "p.Glu92Lys"
  ],
  "p.Leu1258PhefsX7": [
    "p.Leu1258PhefsX7",
    "c.3767dup",
    "3898insC"
  ],
  "c.3773_3774insT": [
    "p.Leu1258PhefsX7",
    "c.3773_3774insT",
    "c.3773dup",
    "3905insT"
  ],
  "c.3773dup": [
    "p.Leu1258PhefsX7",
    "c.3773_3774insT",
    "c.3773dup",
    "3905insT"
  ],
  "3905insT": [
    "p.Leu1258PhefsX7",
    "c.3773_3774insT",
    "c.3773dup",
    "3905insT"
  ],
  "2144delT": [
    "2144delT",
    "p.Leu671X",
    "c.2012del",
    "2143delT"
  ],
  "p.Leu671X": [
    "2144delT",
    "p.Leu671X",
    "c.2012del",
    "2143delT"
  ],
  "c.2012del": [
    "2144delT",
    "p.Leu671X",
    "c.2012del",
    "2143delT"
  ],
  "2143delT": [
    "2144delT",
    "p.Leu671X",
    "c.2012del",
    "2143delT"
  ],
  "S549N": [
    "S549N",
    "p.Ser549Asn",
    "c.1646G>A",
    "1778G>A"
  ],
  "p.Ser549Asn": [
    "S549N",
    "p.Ser549Asn",
    "c.1646G>A",
    "1778G>A"
  ],
  "c.1646G>A": [
    "S549N",
    "p.Ser549Asn",
    "c.1646G>A",
    "1778G>A"
  ],
  "1778G>A": [
    "S549N",
    "p.Ser549Asn",
    "c.1646G>A",
    "1778G>A"
  ],
  "[482G>A with 1342-12T[5]]|R117H with 5T": [
    "[482G>A with 1342-12T[5]]|R117H with 5T",
    "R117H;5T",
    "c.[350G>A;1210-11T>G]"
  ],
  "R117H;5T": [
    "[482G>A with 1342-12T[5]]|R117H with 5T",
    "R117H;5T",
    "c.[350G>A;1210-11T>G]"
  ],
  "c.[350G>A;1210-11T>G]": [
    "[482G>A with 1342-12T[5]]|R117H with 5T",
    "R117H;5T",
    "c.[350G>A;1210-11T>G]"
  ],
  "p.Ser945Leu": [
    "p.Ser945Leu",
    "S945L",
    "c.2834C>T",
    "2966C>T"
  ],
  "S945L": [
    "p.Ser945Leu",
    "S945L",
    "c.2834C>T",
    "2966C>T"
  ],
  "c.2834C>T": [
    "p.Ser945Leu",
    "S945L",
    "c.2834C>T",
    "2966C>T"
  ],
  "2966C>T": [
    "p.Ser945Leu",
    "S945L",
    "c.2834C>T",
    "2966C>T"
  ],
  "c.948del": [
    "c.948del",
    "1080delT",
    "1078delT",
    "p.Phe316LeufsX12"
  ],
  "1080delT": [
    "c.948del",
    "1080delT",
    "1078delT",
    "p.Phe316LeufsX12"
  ],
  "1078delT": [
    "c.948del",
    "1080delT",
    "1078delT",
    "p.Phe316LeufsX12"
  ],
  "p.Phe316LeufsX12": [
    "c.948del",
    "1080delT",
    "1078delT",
    "p.Phe316LeufsX12"
  ],
  "S549R": [
    "S549R",
    "p.Ser549Arg",
    "S549R(A->C)|S549R(T->G)|1777A>C|1779T>G|1779T>A",
    "c.1645A>C|c.1647T>A|c.1647T>G"
  ],
  "p.Ser549Arg": [
    "S549R",
    "p.Ser549Arg",
    "S549R(A->C)|S549R(T->G)|1777A>C|1779T>G|1779T>A",
    "c.1645A>C|c.1647T>A|c.1647T>G"
  ],
  "S549R(A->C)|S549R(T->G)|1777A>C|1779T>G|1779T>A": [
    "S549R",
    "p.Ser549Arg",
    "S549R(A->C)|S549R(T->G)|1777A>C|1779T>G|1779T>A",
    "c.1645A>C|c.1647T>A|c.1647T>G"
  ],
  "c.1645A>C|c.1647T>A|c.1647T>G": [
    "S549R",
    "p.Ser549Arg",
    "S549R(A->C)|S549R(T->G)|1777A>C|1779T>G|1779T>A",
    "c.1645A>C|c.1647T>A|c.1647T>G"
  ],
  "c.2657+2_2657+3insA": [
    "c.2657+2_2657+3insA",
    "2789+2insA",
    "p.?"
  ],
  "2789+2insA": [
    "c.2657+2_2657+3insA",
    "2789+2insA",
    "p.?"
  ],
  "E585X": [
    "E585X",
    "p.Glu585X",
    "c.1753G>T",
    "1885G>T"
  ],
  "p.Glu585X": [
    "E585X",
    "p.Glu585X",
    "c.1753G>T",
    "1885G>T"
  ],
  "c.1753G>T": [
    "E585X",
    "p.Glu585X",
    "c.1753G>T",
    "1885G>T"
  ],
  "1885G>T": [
    "E585X",
    "p.Glu585X",
    "c.1753G>T",
    "1885G>T"
  ],
  "p.Leu1077Pro": [
    "p.Leu1077Pro",
    "3362T>C",
    "L1077P",
    "c.3230T>C"
  ],
  "3362T>C": [
    "p.Leu1077Pro",
    "3362T>C",
    "L1077P",
    "c.3230T>C"
  ],
  "L1077P": [
    "p.Leu1077Pro",
    "3362T>C",
    "L1077P",
    "c.3230T>C"
  ],
  "c.3230T>C": [
    "p.Leu1077Pro",
    "3362T>C",
    "L1077P",
    "c.3230T>C"
  ],
  "1690G>T": [
    "1690G>T",
    "p.Val520Phe",
    "c.1558G>T",
    "V520F"
  ],
  "p.Val520Phe": [
    "1690G>T",
    "p.Val520Phe",
    "c.1558G>T",
    "V520F"
  ],
  "c.1558G>T": [
    "1690G>T",
    "p.Val520Phe",
    "c.1558G>T",
    "V520F"
  ],
  "V520F": [
    "1690G>T",
    "p.Val520Phe",
    "c.1558G>T",
    "V520F"
  ],
  "c.2991G>C": [
    "c.2991G>C",
    "p.Leu997Phe",
    "3123G>C",
    "L997F"
  ],
  "p.Leu997Phe": [
    "c.2991G>C",
    "p.Leu997Phe",
    "3123G>C",
    "L997F"
  ],
  "3123G>C": [
    "c.2991G>C",
    "p.Leu997Phe",
    "3123G>C",
    "L997F"
  ],
  "L997F": [
    "c.2991G>C",
    "p.Leu997Phe",
    "3123G>C",
    "L997F"
  ],
  "3329G>A": [
    "3329G>A",
    "R1066H",
    "p.Arg1066His",
    "c.3197G>A"
  ],
  "R1066H": [
    "3329G>A",
    "R1066H",
    "p.Arg1066His",
    "c.3197G>A"
  ],
  "p.Arg1066His": [
    "3329G>A",
    "R1066H",
    "p.Arg1066His",
    "c.3197G>A"
  ],
  "c.3197G>A": [
    "3329G>A",
    "R1066H",
    "p.Arg1066His",
    "c.3197G>A"
  ],
  "R352Q": [
    "R352Q",
    "1187G>A",
    "p.Arg352Gln",
    "c.1055G>A"
  ],
  "1187G>A": [
    "R352Q",
    "1187G>A",
    "p.Arg352Gln",
    "c.1055G>A"
  ],
  "p.Arg352Gln": [
    "R352Q",
    "1187G>A",
    "p.Arg352Gln",
    "c.1055G>A"
  ],
  "c.1055G>A": [
    "R352Q",
    "1187G>A",
    "p.Arg352Gln",
    "c.1055G>A"
  ],
  "c.3731G>A": [
    "c.3731G>A",
    "p.Gly1244Glu",
    "G1244E",
    "3863G>A"
  ],
  "p.Gly1244Glu": [
    "c.3731G>A",
    "p.Gly1244Glu",
    "G1244E",
    "3863G>A"
  ],
  "G1244E": [
    "c.3731G>A",
    "p.Gly1244Glu",
    "G1244E",
    "3863G>A"
  ],
  "3863G>A": [
    "c.3731G>A",
    "p.Gly1244Glu",
    "G1244E",
    "3863G>A"
  ],
  "D110H": [
    "D110H",
    "p.Asp110His",
    "c.328G>C",
    "460G>C"
  ],
  "p.Asp110His": [
    "D110H",
    "p.Asp110His",
    "c.328G>C",
    "460G>C"
  ],
  "c.328G>C": [
    "D110H",
    "p.Asp110His",
    "c.328G>C",
    "460G>C"
  ],
  "460G>C": [
    "D110H",
    "p.Asp110His",
    "c.328G>C",
    "460G>C"
  ],
  "c.1680-886A>G": [
    "c.1680-886A>G",
    "p.?",
    "c.1679+1634A>G|1812-886A>G|1811+1.6kbA->G",
    "1811+1634A->G"
  ],
  "c.1679+1634A>G|1812-886A>G|1811+1.6kbA->G": [
    "c.1680-886A>G",
    "p.?",
    "c.1679+1634A>G|1812-886A>G|1811+1.6kbA->G",
    "1811+1634A->G"
  ],
  "1811+1634A->G": [
    "c.1680-886A>G",
    "p.?",
    "c.1679+1634A>G|1812-886A>G|1811+1.6kbA->G",
    "1811+1634A->G"
  ],
  "CFTRdele2": [
    "CFTRdele2",
    "p.?",
    "c.(53+1_54-1)_(164+1_165-1)del",
    "deletion of exon 2 (legacy and current numbering)"
  ],
  "c.(53+1_54-1)_(164+1_165-1)del": [
    "CFTRdele2",
    "p.?",
    "c.(53+1_54-1)_(164+1_165-1)del",
    "deletion of exon 2 (legacy and current numbering)"
  ],
  "deletion of exon 2 (legacy and current numbering)": [
    "CFTRdele2",
    "p.?",
    "c.(53+1_54-1)_(164+1_165-1)del",
    "deletion of exon 2 (legacy and current numbering)"
  ],
  "664G>A": [
    "664G>A",
    "p.Gly178Arg",
    "G178R",
    "c.532G>A"
  ],
  "p.Gly178Arg": [
    "664G>A",
    "p.Gly178Arg",
    "G178R",
    "c.532G>A"
  ],
  "G178R": [
    "664G>A",
    "p.Gly178Arg",
    "G178R",
    "c.532G>A"
  ],
  "c.532G>A": [
    "664G>A",
    "p.Gly178Arg",
    "G178R",
    "c.532G>A"
  ],
  "c.3744del": [
    "c.3744del",
    "3876delA",
    "p.Lys1250ArgfsX9"
  ],
  "3876delA": [
    "c.3744del",
    "3876delA",
    "p.Lys1250ArgfsX9"
  ],
  "p.Lys1250ArgfsX9": [
    "c.3747del",
    "3878delG",
    "p.Lys1250ArgfsX9"
  ],
  "2622+1G->A": [
    "2622+1G->A",
    "c.2490+1G>A",
    "p.?"
  ],
  "c.2490+1G>A": [
    "2622+1G->A",
    "c.2490+1G>A",
    "p.?"
  ],
  "711+3A->G": [
    "711+3A->G",
    "p.?",
    "c.579+3A>G"
  ],
  "c.579+3A>G": [
    "711+3A->G",
    "p.?",
    "c.579+3A>G"
  ],
  "I148T": [
    "I148T",
    "575T>C",
    "p.Ile148Thr",
    "c.443T>C"
  ],
  "575T>C": [
    "I148T",
    "575T>C",
    "p.Ile148Thr",
    "c.443T>C"
  ],
  "p.Ile148Thr": [
    "I148T",
    "575T>C",
    "p.Ile148Thr",
    "c.443T>C"
  ],
  "c.443T>C": [
    "I148T",
    "575T>C",
    "p.Ile148Thr",
    "c.443T>C"
  ],
  "3884G>A": [
    "3884G>A",
    "S1251N",
    "p.Ser1251Asn",
    "c.3752G>A"
  ],
  "S1251N": [
    "3884G>A",
    "S1251N",
    "p.Ser1251Asn",
    "c.3752G>A"
  ],
  "p.Ser1251Asn": [
    "3884G>A",
    "S1251N",
    "p.Ser1251Asn",
    "c.3752G>A"
  ],
  "c.3752G>A": [
    "3884G>A",
    "S1251N",
    "p.Ser1251Asn",
    "c.3752G>A"
  ],
  "4016insT": [
    "4016insT",
    "c.3884_3885insT|4021dupT",
    "p.Ser1297PhefsX5",
    "c.3889dup"
  ],
  "c.3884_3885insT|4021dupT": [
    "4016insT",
    "c.3884_3885insT|4021dupT",
    "p.Ser1297PhefsX5",
    "c.3889dup"
  ],
  "p.Ser1297PhefsX5": [
    "4016insT",
    "c.3884_3885insT|4021dupT",
    "p.Ser1297PhefsX5",
    "c.3889dup"
  ],
  "c.3889dup": [
    "4016insT",
    "c.3884_3885insT|4021dupT",
    "p.Ser1297PhefsX5",
    "c.3889dup"
  ],
  "A559T": [
    "A559T",
    "1807G>A",
    "c.1675G>A",
    "p.Ala559Thr"
  ],
  "1807G>A": [
    "A559T",
    "1807G>A",
    "c.1675G>A",
    "p.Ala559Thr"
  ],
  "c.1675G>A": [
    "A559T",
    "1807G>A",
    "c.1675G>A",
    "p.Ala559Thr"
  ],
  "p.Ala559Thr": [
    "A559T",
    "1807G>A",
    "c.1675G>A",
    "p.Ala559Thr"
  ],
  "c.1393-1G>A": [
    "p.?",
    "c.1393-1G>A",
    "1525-1G->A"
  ],
  "1525-1G->A": [
    "p.?",
    "c.1393-1G>A",
    "1525-1G->A"
  ],
  "p.Arg75X": [
    "p.Arg75X",
    "R75X",
    "355C>T",
    "c.223C>T"
  ],
  "R75X": [
    "p.Arg75X",
    "R75X",
    "355C>T",
    "c.223C>T"
  ],
  "355C>T": [
    "p.Arg75X",
    "R75X",
    "355C>T",
    "c.223C>T"
  ],
  "c.223C>T": [
    "p.Arg75X",
    "R75X",
    "355C>T",
    "c.223C>T"
  ],
  "790C>T": [
    "790C>T",
    "Q220X",
    "c.658C>T",
    "p.Gln220X"
  ],
  "Q220X": [
    "790C>T",
    "Q220X",
    "c.658C>T",
    "p.Gln220X"
  ],
  "c.658C>T": [
    "790C>T",
    "Q220X",
    "c.658C>T",
    "p.Gln220X"
  ],
  "p.Gln220X": [
    "790C>T",
    "Q220X",
    "c.658C>T",
    "p.Gln220X"
  ],
  "Q996Q|p.Gln996Gln": [
    "Q996Q|p.Gln996Gln",
    "p.Gln996=",
    "c.2988G>A",
    "3120G->A"
  ],
  "p.Gln996=": [
    "Q996Q|p.Gln996Gln",
    "p.Gln996=",
    "c.2988G>A",
    "3120G->A"
  ],
  "c.2988G>A": [
    "Q996Q|p.Gln996Gln",
    "p.Gln996=",
    "c.2988G>A",
    "3120G->A"
  ],
  "3120G->A": [
    "Q996Q|p.Gln996Gln",
    "p.Gln996=",
    "c.2988G>A",
    "3120G->A"
  ],
  "p.Glu1418ArgfsX14": [
    "p.Glu1418ArgfsX14",
    "c.4251del",
    "4382delA"
  ],
  "c.4251del": [
    "p.Glu1418ArgfsX14",
    "c.4251del",
    "4382delA"
  ],
  "4382delA": [
    "p.Glu1418ArgfsX14",
    "c.4251del",
    "4382delA"
  ],
  "3837T>G": [
    "3837T>G",
    "p.Ser1235Arg",
    "c.3705T>G",
    "S1235R"
  ],
  "p.Ser1235Arg": [
    "3837T>G",
    "p.Ser1235Arg",
    "c.3705T>G",
    "S1235R"
  ],
  "c.3705T>G": [
    "3837T>G",
    "p.Ser1235Arg",
    "c.3705T>G",
    "S1235R"
  ],
  "S1235R": [
    "3837T>G",
    "p.Ser1235Arg",
    "c.3705T>G",
    "S1235R"
  ],
  "c.613C>T": [
    "c.613C>T",
    "P205S",
    "745C>T",
    "p.Pro205Ser"
  ],
  "P205S": [
    "c.613C>T",
    "P205S",
    "745C>T",
    "p.Pro205Ser"
  ],
  "745C>T": [
    "c.613C>T",
    "P205S",
    "745C>T",
    "p.Pro205Ser"
  ],
  "p.Pro205Ser": [
    "c.613C>T",
    "P205S",
    "745C>T",
    "p.Pro205Ser"
  ],
  "p.Arg709X": [
    "p.Arg709X",
    "R709X",
    "c.2125C>T",
    "2257C>T"
  ],
  "R709X": [
    "p.Arg709X",
    "R709X",
    "c.2125C>T",
    "2257C>T"
  ],
  "c.2125C>T": [
    "p.Arg709X",
    "R709X",
    "c.2125C>T",
    "2257C>T"
  ],
  "2257C>T": [
    "p.Arg709X",
    "R709X",
    "c.2125C>T",
    "2257C>T"
  ],
  "p.Pro5Leu": [
    "p.Pro5Leu",
    "c.14C>T",
    "P5L",
    "146C>T"
  ],
  "c.14C>T": [
    "p.Pro5Leu",
    "c.14C>T",
    "P5L",
    "146C>T"
  ],
  "P5L": [
    "p.Pro5Leu",
    "c.14C>T",
    "P5L",
    "146C>T"
  ],
  "146C>T": [
    "p.Pro5Leu",
    "c.14C>T",
    "P5L",
    "146C>T"
  ],
  "3199del6": [
    "3199del6",
    "c.3067_3072del",
    "p.Ile1023_Val1024del",
    "3199delATAGTG"
  ],
  "c.3067_3072del": [
    "3199del6",
    "c.3067_3072del",
    "p.Ile1023_Val1024del",
    "3199delATAGTG"
  ],
  "p.Ile1023_Val1024del": [
    "3199del6",
    "c.3067_3072del",
    "p.Ile1023_Val1024del",
    "3199delATAGTG"
  ],
  "3199delATAGTG": [
    "3199del6",
    "c.3067_3072del",
    "p.Ile1023_Val1024del",
    "3199delATAGTG"
  ],
  "c.1397C>A|c.1397C>G": [
    "c.1397C>A|c.1397C>G",
    "p.Ser466X",
    "S466X(TGA)|S466X(TAA)|1529C>A|1529C>G",
    "S466X"
  ],
  "p.Ser466X": [
    "c.1397C>A|c.1397C>G",
    "p.Ser466X",
    "S466X(TGA)|S466X(TAA)|1529C>A|1529C>G",
    "S466X"
  ],
  "S466X(TGA)|S466X(TAA)|1529C>A|1529C>G": [
    "c.1397C>A|c.1397C>G",
    "p.Ser466X",
    "S466X(TGA)|S466X(TAA)|1529C>A|1529C>G",
    "S466X"
  ],
  "S466X": [
    "c.1397C>A|c.1397C>G",
    "p.Ser466X",
    "S466X(TGA)|S466X(TAA)|1529C>A|1529C>G",
    "S466X"
  ],
  "c.579+5G>A": [
    "p.?",
    "c.579+5G>A",
    "711+5G->A"
  ],
  "711+5G->A": [
    "p.?",
    "c.579+5G>A",
    "711+5G->A"
  ],
  "c.1210-7_1210-6del": [
    "c.1210-7_1210-6del",
    "c.1210-33_1210-6GT[11]T[4]",
    "p.?",
    "5T;TG11"
  ],
  "c.1210-33_1210-6GT[11]T[4]": [
    "c.1210-7_1210-6del",
    "c.1210-33_1210-6GT[11]T[4]",
    "p.?",
    "5T;TG11"
  ],
  "5T;TG11": [
    "c.1210-7_1210-6del",
    "c.1210-33_1210-6GT[11]T[4]",
    "p.?",
    "5T;TG11"
  ],
  "5T;TG13": [
    "5T;TG13",
    "p.?",
    "c.1210-33_1210-6GT[13]T[4]",
    "c.1210-11delinsGTG"
  ],
  "c.1210-33_1210-6GT[13]T[4]": [
    "5T;TG13",
    "p.?",
    "c.1210-33_1210-6GT[13]T[4]",
    "c.1210-11delinsGTG"
  ],
  "c.1210-11delinsGTG": [
    "5T;TG13",
    "p.?",
    "c.1210-33_1210-6GT[13]T[4]",
    "c.1210-11delinsGTG"
  ],
  "c.695T>A": [
    "c.695T>A",
    "V232D",
    "p.Val232Asp",
    "827T>A"
  ],
  "V232D": [
    "c.695T>A",
    "V232D",
    "p.Val232Asp",
    "827T>A"
  ],
  "p.Val232Asp": [
    "c.695T>A",
    "V232D",
    "p.Val232Asp",
    "827T>A"
  ],
  "827T>A": [
    "c.695T>A",
    "V232D",
    "p.Val232Asp",
    "827T>A"
  ],
  "p.Leu138dup": [
    "p.Leu138dup",
    "546insCTA|545dupTAC",
    "c.413_415dup",
    "L138ins"
  ],
  "546insCTA|545dupTAC": [
    "p.Leu138dup",
    "546insCTA|545dupTAC",
    "c.413_415dup",
    "L138ins"
  ],
  "c.413_415dup": [
    "p.Leu138dup",
    "546insCTA|545dupTAC",
    "c.413_415dup",
    "L138ins"
  ],
  "L138ins": [
    "p.Leu138dup",
    "546insCTA|545dupTAC",
    "c.413_415dup",
    "L138ins"
  ],
  "c.1007T>A": [
    "c.1007T>A",
    "p.Ile336Lys",
    "I336K",
    "1139T>A"
  ],
  "p.Ile336Lys": [
    "c.1007T>A",
    "p.Ile336Lys",
    "I336K",
    "1139T>A"
  ],
  "I336K": [
    "c.1007T>A",
    "p.Ile336Lys",
    "I336K",
    "1139T>A"
  ],
  "1139T>A": [
    "c.1007T>A",
    "p.Ile336Lys",
    "I336K",
    "1139T>A"
  ],
  "R75Q": [
    "R75Q",
    "356G>A",
    "p.Arg75Gln",
    "c.224G>A"
  ],
  "356G>A": [
    "R75Q",
    "356G>A",
    "p.Arg75Gln",
    "c.224G>A"
  ],
  "p.Arg75Gln": [
    "R75Q",
    "356G>A",
    "p.Arg75Gln",
    "c.224G>A"
  ],
  "c.224G>A": [
    "R75Q",
    "356G>A",
    "p.Arg75Gln",
    "c.224G>A"
  ],
  "c.2491G>T": [
    "c.2491G>T",
    "2623G>T",
    "E831X",
    "p.Glu831X"
  ],
  "2623G>T": [
    "c.2491G>T",
    "2623G>T",
    "E831X",
    "p.Glu831X"
  ],
  "E831X": [
    "c.2491G>T",
    "2623G>T",
    "E831X",
    "p.Glu831X"
  ],
  "p.Glu831X": [
    "c.2491G>T",
    "2623G>T",
    "E831X",
    "p.Glu831X"
  ],
  "c.(2988+1_2989-1)_(3468+1_3469-1)del": [
    "c.(2988+1_2989-1)_(3468+1_3469-1)del",
    "p.?",
    "3120+1kbdel8.6kb|deletion of exons 17a, 17b, and 18 (legacy numbering)|deletion of exons 19, 20, and 21 (current numbering)",
    "CFTRdele17a-18"
  ],
  "3120+1kbdel8.6kb|deletion of exons 17a, 17b, and 18 (legacy numbering)|deletion of exons 19, 20, and 21 (current numbering)": [
    "c.(2988+1_2989-1)_(3468+1_3469-1)del",
    "p.?",
    "3120+1kbdel8.6kb|deletion of exons 17a, 17b, and 18 (legacy numbering)|deletion of exons 19, 20, and 21 (current numbering)",
    "CFTRdele17a-18"
  ],
  "CFTRdele17a-18": [
    "c.(2988+1_2989-1)_(3468+1_3469-1)del",
    "p.?",
    "3120+1kbdel8.6kb|deletion of exons 17a, 17b, and 18 (legacy numbering)|deletion of exons 19, 20, and 21 (current numbering)",
    "CFTRdele17a-18"
  ],
  "I1027T": [
    "I1027T",
    "3212T>C",
    "c.3080T>C",
    "p.Ile1027Thr"
  ],
  "3212T>C": [
    "I1027T",
    "3212T>C",
    "c.3080T>C",
    "p.Ile1027Thr"
  ],
  "c.3080T>C": [
    "I1027T",
    "3212T>C",
    "c.3080T>C",
    "p.Ile1027Thr"
  ],
  "p.Ile1027Thr": [
    "I1027T",
    "3212T>C",
    "c.3080T>C",
    "p.Ile1027Thr"
  ],
  "c.11C>A": [
    "c.11C>A",
    "143C>A",
    "p.Ser4X",
    "S4X"
  ],
  "143C>A": [
    "c.11C>A",
    "143C>A",
    "p.Ser4X",
    "S4X"
  ],
  "p.Ser4X": [
    "c.11C>A",
    "143C>A",
    "p.Ser4X",
    "S4X"
  ],
  "S4X": [
    "c.11C>A",
    "143C>A",
    "p.Ser4X",
    "S4X"
  ],
  "3398G>A": [
    "3398G>A",
    "c.3266G>A",
    "W1089X",
    "p.Trp1089X"
  ],
  "c.3266G>A": [
    "3398G>A",
    "c.3266G>A",
    "W1089X",
    "p.Trp1089X"
  ],
  "W1089X": [
    "3398G>A",
    "c.3266G>A",
    "W1089X",
    "p.Trp1089X"
  ],
  "p.Trp1089X": [
    "3398G>A",
    "c.3266G>A",
    "W1089X",
    "p.Trp1089X"
  ],
  "F508del in cis with I1027T|[1653delCTT with 3212T>C]": [
    "F508del in cis with I1027T|[1653delCTT with 3212T>C]",
    "c.[1521_1523del;3080T>C]",
    "p.[Phe508del;Ile1027Thr]",
    "F508del;I1027T"
  ],
  "c.[1521_1523del;3080T>C]": [
    "F508del in cis with I1027T|[1653delCTT with 3212T>C]",
    "c.[1521_1523del;3080T>C]",
    "p.[Phe508del;Ile1027Thr]",
    "F508del;I1027T"
  ],
  "p.[Phe508del;Ile1027Thr]": [
    "F508del in cis with I1027T|[1653delCTT with 3212T>C]",
    "c.[1521_1523del;3080T>C]",
    "p.[Phe508del;Ile1027Thr]",
    "F508del;I1027T"
  ],
  "F508del;I1027T": [
    "F508del in cis with I1027T|[1653delCTT with 3212T>C]",
    "c.[1521_1523del;3080T>C]",
    "p.[Phe508del;Ile1027Thr]",
    "F508del;I1027T"
  ],
  "c.(3963+1_3964-1)_(4242+1_4243-1)del": [
    "c.(3963+1_3964-1)_(4242+1_4243-1)del",
    "p.?",
    "deletion of exons 22 and 23 (legacy numbering)|deletion of exons 25 and 26 (current numbering)",
    "CFTRdele22,23"
  ],
  "deletion of exons 22 and 23 (legacy numbering)|deletion of exons 25 and 26 (current numbering)": [
    "c.(3963+1_3964-1)_(4242+1_4243-1)del",
    "p.?",
    "deletion of exons 22 and 23 (legacy numbering)|deletion of exons 25 and 26 (current numbering)",
    "CFTRdele22,23"
  ],
  "CFTRdele22,23": [
    "c.(3963+1_3964-1)_(4242+1_4243-1)del",
    "p.?",
    "deletion of exons 22 and 23 (legacy numbering)|deletion of exons 25 and 26 (current numbering)",
    "CFTRdele22,23"
  ],
  "c.1013C>T": [
    "c.1013C>T",
    "T338I",
    "p.Thr338Ile",
    "1145C>T"
  ],
  "T338I": [
    "c.1013C>T",
    "T338I",
    "p.Thr338Ile",
    "1145C>T"
  ],
  "p.Thr338Ile": [
    "c.1013C>T",
    "T338I",
    "p.Thr338Ile",
    "1145C>T"
  ],
  "1145C>T": [
    "c.1013C>T",
    "T338I",
    "p.Thr338Ile",
    "1145C>T"
  ],
  "c.580-1G>T": [
    "p.?",
    "c.580-1G>T",
    "712-1G->T"
  ],
  "712-1G->T": [
    "p.?",
    "c.580-1G>T",
    "712-1G->T"
  ],
  "3286T>G": [
    "3286T>G",
    "p.Phe1052Val",
    "F1052V",
    "c.3154T>G"
  ],
  "p.Phe1052Val": [
    "3286T>G",
    "p.Phe1052Val",
    "F1052V",
    "c.3154T>G"
  ],
  "F1052V": [
    "3286T>G",
    "p.Phe1052Val",
    "F1052V",
    "c.3154T>G"
  ],
  "c.3154T>G": [
    "3286T>G",
    "p.Phe1052Val",
    "F1052V",
    "c.3154T>G"
  ],
  "c.1736A>G": [
    "c.1736A>G",
    "1868A>G",
    "p.Asp579Gly",
    "D579G"
  ],
  "1868A>G": [
    "c.1736A>G",
    "1868A>G",
    "p.Asp579Gly",
    "D579G"
  ],
  "p.Asp579Gly": [
    "c.1736A>G",
    "1868A>G",
    "p.Asp579Gly",
    "D579G"
  ],
  "D579G": [
    "c.1736A>G",
    "1868A>G",
    "p.Asp579Gly",
    "D579G"
  ],
  "p.Lys710X": [
    "p.Lys710X",
    "2260A>T",
    "c.2128A>T",
    "K710X"
  ],
  "2260A>T": [
    "p.Lys710X",
    "2260A>T",
    "c.2128A>T",
    "K710X"
  ],
  "c.2128A>T": [
    "p.Lys710X",
    "2260A>T",
    "c.2128A>T",
    "K710X"
  ],
  "K710X": [
    "p.Lys710X",
    "2260A>T",
    "c.2128A>T",
    "K710X"
  ],
  "2307insA": [
    "2307insA",
    "c.2175dup",
    "p.Glu726ArgfsX4",
    "c.2175_2176insA"
  ],
  "c.2175dup": [
    "2307insA",
    "c.2175dup",
    "p.Glu726ArgfsX4",
    "c.2175_2176insA"
  ],
  "p.Glu726ArgfsX4": [
    "2307insA",
    "c.2175dup",
    "p.Glu726ArgfsX4",
    "c.2175_2176insA"
  ],
  "c.2175_2176insA": [
    "2307insA",
    "c.2175dup",
    "p.Glu726ArgfsX4",
    "c.2175_2176insA"
  ],
  "p.Ser489X": [
    "p.Ser489X",
    "c.1466C>A|c.1466C>G",
    "S489X",
    "1598C>A"
  ],
  "c.1466C>A|c.1466C>G": [
    "p.Ser489X",
    "c.1466C>A|c.1466C>G",
    "S489X",
    "1598C>A"
  ],
  "S489X": [
    "p.Ser489X",
    "c.1466C>A|c.1466C>G",
    "S489X",
    "1598C>A"
  ],
  "1598C>A": [
    "p.Ser489X",
    "c.1466C>A|c.1466C>G",
    "S489X",
    "1598C>A"
  ],
  "1461ins4": [
    "1461ins4",
    "c.1326_1329dupAGAT|c.1329_1330insAGAT",
    "c.1327_1330dup",
    "p.Ile444ArgfsX3"
  ],
  "c.1326_1329dupAGAT|c.1329_1330insAGAT": [
    "1461ins4",
    "c.1326_1329dupAGAT|c.1329_1330insAGAT",
    "c.1327_1330dup",
    "p.Ile444ArgfsX3"
  ],
  "c.1327_1330dup": [
    "1461ins4",
    "c.1326_1329dupAGAT|c.1329_1330insAGAT",
    "c.1327_1330dup",
    "p.Ile444ArgfsX3"
  ],
  "p.Ile444ArgfsX3": [
    "1461ins4",
    "c.1326_1329dupAGAT|c.1329_1330insAGAT",
    "c.1327_1330dup",
    "p.Ile444ArgfsX3"
  ],
  "1812-1G->A": [
    "1812-1G->A",
    "c.1680-1G>A",
    "p.?"
  ],
  "c.1680-1G>A": [
    "1812-1G->A",
    "c.1680-1G>A",
    "p.?"
  ],
  "p.Tyr122X": [
    "p.Tyr122X",
    "c.366T>A",
    "498T>A",
    "Y122X"
  ],
  "c.366T>A": [
    "p.Tyr122X",
    "c.366T>A",
    "498T>A",
    "Y122X"
  ],
  "498T>A": [
    "p.Tyr122X",
    "c.366T>A",
    "498T>A",
    "Y122X"
  ],
  "Y122X": [
    "p.Tyr122X",
    "c.366T>A",
    "498T>A",
    "Y122X"
  ],
  "c.1682C>A": [
    "c.1682C>A",
    "p.Ala561Glu",
    "A561E",
    "1814C>A"
  ],
  "p.Ala561Glu": [
    "c.1682C>A",
    "p.Ala561Glu",
    "A561E",
    "1814C>A"
  ],
  "A561E": [
    "c.1682C>A",
    "p.Ala561Glu",
    "A561E",
    "1814C>A"
  ],
  "1814C>A": [
    "c.1682C>A",
    "p.Ala561Glu",
    "A561E",
    "1814C>A"
  ],
  "p.Leu732X": [
    "p.Leu732X",
    "c.2195T>G",
    "L732X",
    "2327T>G"
  ],
  "c.2195T>G": [
    "p.Leu732X",
    "c.2195T>G",
    "L732X",
    "2327T>G"
  ],
  "L732X": [
    "p.Leu732X",
    "c.2195T>G",
    "L732X",
    "2327T>G"
  ],
  "2327T>G": [
    "p.Leu732X",
    "c.2195T>G",
    "L732X",
    "2327T>G"
  ],
  "c.3700A>G": [
    "c.3700A>G",
    "I1234V",
    "p.Ile1234Val",
    "3832A>G"
  ],
  "I1234V": [
    "c.3700A>G",
    "I1234V",
    "p.Ile1234Val",
    "3832A>G"
  ],
  "p.Ile1234Val": [
    "c.3700A>G",
    "I1234V",
    "p.Ile1234Val",
    "3832A>G"
  ],
  "3832A>G": [
    "c.3700A>G",
    "I1234V",
    "p.Ile1234Val",
    "3832A>G"
  ],
  "c.2353C>T": [
    "c.2353C>T",
    "2485C>T",
    "p.Arg785X",
    "R785X"
  ],
  "2485C>T": [
    "c.2353C>T",
    "2485C>T",
    "p.Arg785X",
    "R785X"
  ],
  "p.Arg785X": [
    "c.2353C>T",
    "2485C>T",
    "p.Arg785X",
    "R785X"
  ],
  "R785X": [
    "c.2353C>T",
    "2485C>T",
    "p.Arg785X",
    "R785X"
  ],
  "p.Leu467Pro": [
    "p.Leu467Pro",
    "L467P",
    "1532T>C",
    "c.1400T>C"
  ],
  "L467P": [
    "p.Leu467Pro",
    "L467P",
    "1532T>C",
    "c.1400T>C"
  ],
  "1532T>C": [
    "p.Leu467Pro",
    "L467P",
    "1532T>C",
    "c.1400T>C"
  ],
  "c.1400T>C": [
    "p.Leu467Pro",
    "L467P",
    "1532T>C",
    "c.1400T>C"
  ],
  "p.Gln890X": [
    "p.Gln890X",
    "c.2668C>T",
    "2800C>T",
    "Q890X"
  ],
  "c.2668C>T": [
    "p.Gln890X",
    "c.2668C>T",
    "2800C>T",
    "Q890X"
  ],
  "2800C>T": [
    "p.Gln890X",
    "c.2668C>T",
    "2800C>T",
    "Q890X"
  ],
  "Q890X": [
    "p.Gln890X",
    "c.2668C>T",
    "2800C>T",
    "Q890X"
  ],
  "247C>T": [
    "247C>T",
    "Q39X",
    "c.115C>T",
    "p.Gln39X"
  ],
  "Q39X": [
    "247C>T",
    "Q39X",
    "c.115C>T",
    "p.Gln39X"
  ],
  "c.115C>T": [
    "247C>T",
    "Q39X",
    "c.115C>T",
    "p.Gln39X"
  ],
  "p.Gln39X": [
    "247C>T",
    "Q39X",
    "c.115C>T",
    "p.Gln39X"
  ],
  "c.1116+1G>A": [
    "c.1116+1G>A",
    "p.?",
    "1248+1G->A"
  ],
  "1248+1G->A": [
    "c.1116+1G>A",
    "p.?",
    "1248+1G->A"
  ],
  "E92X": [
    "E92X",
    "c.274G>T",
    "p.Glu92X",
    "406G>T"
  ],
  "c.274G>T": [
    "E92X",
    "c.274G>T",
    "p.Glu92X",
    "406G>T"
  ],
  "p.Glu92X": [
    "E92X",
    "c.274G>T",
    "p.Glu92X",
    "406G>T"
  ],
  "406G>T": [
    "E92X",
    "c.274G>T",
    "p.Glu92X",
    "406G>T"
  ],
  "W846X": [
    "W846X",
    "c.2537G>A|c.2538G>A",
    "2669G>A|2670G>A",
    "p.Trp846X"
  ],
  "c.2537G>A|c.2538G>A": [
    "W846X",
    "c.2537G>A|c.2538G>A",
    "2669G>A|2670G>A",
    "p.Trp846X"
  ],
  "2669G>A|2670G>A": [
    "W846X",
    "c.2537G>A|c.2538G>A",
    "2669G>A|2670G>A",
    "p.Trp846X"
  ],
  "p.Trp846X": [
    "c.2538delG",
    "c.2538del",
    "p.Trp846X"
  ],
  "c.2215del": [
    "c.2215del",
    "p.Val739TyrfsX16",
    "2347delG"
  ],
  "p.Val739TyrfsX16": [
    "c.2215del",
    "p.Val739TyrfsX16",
    "2347delG"
  ],
  "2347delG": [
    "c.2215del",
    "p.Val739TyrfsX16",
    "2347delG"
  ],
  "p.Gly576Ala": [
    "p.Gly576Ala",
    "G576A",
    "c.1727G>C",
    "1859G>C"
  ],
  "G576A": [
    "p.Gly576Ala",
    "G576A",
    "c.1727G>C",
    "1859G>C"
  ],
  "c.1727G>C": [
    "p.Gly576Ala",
    "G576A",
    "c.1727G>C",
    "1859G>C"
  ],
  "1859G>C": [
    "p.Gly576Ala",
    "G576A",
    "c.1727G>C",
    "1859G>C"
  ],
  "1898+3A->G": [
    "1898+3A->G",
    "p.?",
    "c.1766+3A>G"
  ],
  "c.1766+3A>G": [
    "1898+3A->G",
    "p.?",
    "c.1766+3A>G"
  ],
  "c.(3963+1_3964-1)_(*1_?)del": [
    "c.(3963+1_3964-1)_(*1_?)del",
    "p.?",
    "deletion of exons 22, 23, and 24 (legacy numbering)|deletion of exons 25, 26, and 27 (current numbering)",
    "CFTRdele22-24"
  ],
  "deletion of exons 22, 23, and 24 (legacy numbering)|deletion of exons 25, 26, and 27 (current numbering)": [
    "c.(3963+1_3964-1)_(*1_?)del",
    "p.?",
    "deletion of exons 22, 23, and 24 (legacy numbering)|deletion of exons 25, 26, and 27 (current numbering)",
    "CFTRdele22-24"
  ],
  "CFTRdele22-24": [
    "c.(3963+1_3964-1)_(*1_?)del",
    "p.?",
    "deletion of exons 22, 23, and 24 (legacy numbering)|deletion of exons 25, 26, and 27 (current numbering)",
    "CFTRdele22-24"
  ],
  "406-1G->A": [
    "406-1G->A",
    "c.274-1G>A",
    "p.?"
  ],
  "c.274-1G>A": [
    "406-1G->A",
    "c.274-1G>A",
    "p.?"
  ],
  "c.1705T>G": [
    "c.1705T>G",
    "Y569D",
    "p.Tyr569Asp",
    "1837T>G"
  ],
  "Y569D": [
    "c.1705T>G",
    "Y569D",
    "p.Tyr569Asp",
    "1837T>G"
  ],
  "p.Tyr569Asp": [
    "c.1705T>G",
    "Y569D",
    "p.Tyr569Asp",
    "1837T>G"
  ],
  "1837T>G": [
    "c.1705T>G",
    "Y569D",
    "p.Tyr569Asp",
    "1837T>G"
  ],
  "3340C>T": [
    "3340C>T",
    "R1070W",
    "c.3208C>T",
    "p.Arg1070Trp"
  ],
  "R1070W": [
    "3340C>T",
    "R1070W",
    "c.3208C>T",
    "p.Arg1070Trp"
  ],
  "c.3208C>T": [
    "3340C>T",
    "R1070W",
    "c.3208C>T",
    "p.Arg1070Trp"
  ],
  "p.Arg1070Trp": [
    "3340C>T",
    "R1070W",
    "c.3208C>T",
    "p.Arg1070Trp"
  ],
  "c.2290C>T": [
    "c.2290C>T",
    "2422C>T",
    "R764X",
    "p.Arg764X"
  ],
  "2422C>T": [
    "c.2290C>T",
    "2422C>T",
    "R764X",
    "p.Arg764X"
  ],
  "R764X": [
    "c.2290C>T",
    "2422C>T",
    "R764X",
    "p.Arg764X"
  ],
  "p.Arg764X": [
    "c.2290C>T",
    "2422C>T",
    "R764X",
    "p.Arg764X"
  ],
  "E822X": [
    "E822X",
    "2596G>T",
    "p.Glu822X",
    "c.2464G>T"
  ],
  "2596G>T": [
    "E822X",
    "2596G>T",
    "p.Glu822X",
    "c.2464G>T"
  ],
  "p.Glu822X": [
    "E822X",
    "2596G>T",
    "p.Glu822X",
    "c.2464G>T"
  ],
  "c.2464G>T": [
    "E822X",
    "2596G>T",
    "p.Glu822X",
    "c.2464G>T"
  ],
  "3281T>C": [
    "3281T>C",
    "p.Leu1065Pro",
    "L1065P",
    "c.3194T>C"
  ],
  "p.Leu1065Pro": [
    "3281T>C",
    "p.Leu1065Pro",
    "L1065P",
    "c.3194T>C"
  ],
  "L1065P": [
    "3281T>C",
    "p.Leu1065Pro",
    "L1065P",
    "c.3194T>C"
  ],
  "c.3194T>C": [
    "3281T>C",
    "p.Leu1065Pro",
    "L1065P",
    "c.3194T>C"
  ],
  "c.1654C>T": [
    "c.1654C>T",
    "Q552X",
    "1786C>T",
    "p.Gln552X"
  ],
  "Q552X": [
    "c.1654C>T",
    "Q552X",
    "1786C>T",
    "p.Gln552X"
  ],
  "1786C>T": [
    "c.1654C>T",
    "Q552X",
    "1786C>T",
    "p.Gln552X"
  ],
  "p.Gln552X": [
    "c.1654C>T",
    "Q552X",
    "1786C>T",
    "p.Gln552X"
  ],
  "c.3209G>A": [
    "c.3209G>A",
    "p.Arg1070Gln",
    "3341G>A",
    "R1070Q"
  ],
  "p.Arg1070Gln": [
    "c.3209G>A",
    "p.Arg1070Gln",
    "3341G>A",
    "R1070Q"
  ],
  "3341G>A": [
    "c.3209G>A",
    "p.Arg1070Gln",
    "3341G>A",
    "R1070Q"
  ],
  "R1070Q": [
    "c.3209G>A",
    "p.Arg1070Gln",
    "3341G>A",
    "R1070Q"
  ],
  "1716G/A": [
    "1716G/A",
    "c.1584G>A",
    "E528E",
    "p.Glu528="
  ],
  "c.1584G>A": [
    "1716G/A",
    "c.1584G>A",
    "E528E",
    "p.Glu528="
  ],
  "E528E": [
    "1716G/A",
    "c.1584G>A",
    "E528E",
    "p.Glu528="
  ],
  "p.Glu528=": [
    "1716G/A",
    "c.1584G>A",
    "E528E",
    "p.Glu528="
  ],
  "R851X": [
    "R851X",
    "2683C>T",
    "p.Arg851X",
    "c.2551C>T"
  ],
  "2683C>T": [
    "R851X",
    "2683C>T",
    "p.Arg851X",
    "c.2551C>T"
  ],
  "p.Arg851X": [
    "R851X",
    "2683C>T",
    "p.Arg851X",
    "c.2551C>T"
  ],
  "c.2551C>T": [
    "R851X",
    "2683C>T",
    "p.Arg851X",
    "c.2551C>T"
  ],
  "S492F": [
    "S492F",
    "1607C>T",
    "p.Ser492Phe",
    "c.1475C>T"
  ],
  "1607C>T": [
    "S492F",
    "1607C>T",
    "p.Ser492Phe",
    "c.1475C>T"
  ],
  "p.Ser492Phe": [
    "S492F",
    "1607C>T",
    "p.Ser492Phe",
    "c.1475C>T"
  ],
  "c.1475C>T": [
    "S492F",
    "1607C>T",
    "p.Ser492Phe",
    "c.1475C>T"
  ],
  "2134C>T": [
    "2134C>T",
    "R668C",
    "c.2002C>T",
    "p.Arg668Cys"
  ],
  "R668C": [
    "2134C>T",
    "R668C",
    "c.2002C>T",
    "p.Arg668Cys"
  ],
  "c.2002C>T": [
    "2134C>T",
    "R668C",
    "c.2002C>T",
    "p.Arg668Cys"
  ],
  "p.Arg668Cys": [
    "2134C>T",
    "R668C",
    "c.2002C>T",
    "p.Arg668Cys"
  ],
  "V456A": [
    "V456A",
    "p.Val456Ala",
    "1499T>C",
    "c.1367T>C"
  ],
  "p.Val456Ala": [
    "V456A",
    "p.Val456Ala",
    "1499T>C",
    "c.1367T>C"
  ],
  "1499T>C": [
    "V456A",
    "p.Val456Ala",
    "1499T>C",
    "c.1367T>C"
  ],
  "c.1367T>C": [
    "V456A",
    "p.Val456Ala",
    "1499T>C",
    "c.1367T>C"
  ],
  "S466X in cis with R1070Q|[1529C>G with 3341G>A]": [
    "S466X in cis with R1070Q|[1529C>G with 3341G>A]",
    "c.[1397C>A;3209G>A]|c.[1397C>G;3209G>A]",
    "S466X;R1070Q"
  ],
  "c.[1397C>A;3209G>A]|c.[1397C>G;3209G>A]": [
    "S466X in cis with R1070Q|[1529C>G with 3341G>A]",
    "c.[1397C>A;3209G>A]|c.[1397C>G;3209G>A]",
    "S466X;R1070Q"
  ],
  "S466X;R1070Q": [
    "S466X in cis with R1070Q|[1529C>G with 3341G>A]",
    "c.[1397C>A;3209G>A]|c.[1397C>G;3209G>A]",
    "S466X;R1070Q"
  ],
  "S1196X": [
    "S1196X",
    "p.Ser1196X",
    "3719C>G",
    "c.3587C>A|c.3587C>G"
  ],
  "p.Ser1196X": [
    "S1196X",
    "p.Ser1196X",
    "3719C>G",
    "c.3587C>A|c.3587C>G"
  ],
  "3719C>G": [
    "S1196X",
    "p.Ser1196X",
    "3719C>G",
    "c.3587C>A|c.3587C>G"
  ],
  "c.3587C>A|c.3587C>G": [
    "S1196X",
    "p.Ser1196X",
    "3719C>G",
    "c.3587C>A|c.3587C>G"
  ],
  "1811+1643G->T": [
    "1811+1643G->T",
    "c.1679+1643G>T",
    "c.1680-877G>T",
    "p.?"
  ],
  "c.1679+1643G>T": [
    "1811+1643G->T",
    "c.1679+1643G>T",
    "c.1680-877G>T",
    "p.?"
  ],
  "c.1680-877G>T": [
    "1811+1643G->T",
    "c.1679+1643G>T",
    "c.1680-877G>T",
    "p.?"
  ],
  "T854T": [
    "T854T",
    "p.Thr854=",
    "c.2562T>A|c.2562T>C|c.2562T>G",
    "2694T/G|2694T/C|2694T>C|2694T>G|2694T>A"
  ],
  "p.Thr854=": [
    "T854T",
    "p.Thr854=",
    "c.2562T>A|c.2562T>C|c.2562T>G",
    "2694T/G|2694T/C|2694T>C|2694T>G|2694T>A"
  ],
  "c.2562T>A|c.2562T>C|c.2562T>G": [
    "T854T",
    "p.Thr854=",
    "c.2562T>A|c.2562T>C|c.2562T>G",
    "2694T/G|2694T/C|2694T>C|2694T>G|2694T>A"
  ],
  "2694T/G|2694T/C|2694T>C|2694T>G|2694T>A": [
    "T854T",
    "p.Thr854=",
    "c.2562T>A|c.2562T>C|c.2562T>G",
    "2694T/G|2694T/C|2694T>C|2694T>G|2694T>A"
  ],
  "c.273+1G>A": [
    "c.273+1G>A",
    "p.?",
    "405+1G->A"
  ],
  "405+1G->A": [
    "c.273+1G>A",
    "p.?",
    "405+1G->A"
  ],
  "2711delT": [
    "2711delT",
    "p.Phe861LeufsX3",
    "c.2583del"
  ],
  "p.Phe861LeufsX3": [
    "2711delT",
    "p.Phe861LeufsX3",
    "c.2583del"
  ],
  "c.2583del": [
    "2711delT",
    "p.Phe861LeufsX3",
    "c.2583del"
  ],
  "c.325_327delinsG": [
    "c.325_327delinsG",
    "457TAT->G",
    "p.Tyr109GlyfsX4"
  ],
  "457TAT->G": [
    "c.325_327delinsG",
    "457TAT->G",
    "p.Tyr109GlyfsX4"
  ],
  "p.Tyr109GlyfsX4": [
    "c.325_327delinsG",
    "457TAT->G",
    "p.Tyr109GlyfsX4"
  ],
  "wild-type/reference": [
    "wild-type/reference",
    "p.?",
    "7T"
  ],
  "7T": [
    "wild-type/reference",
    "p.?",
    "7T"
  ],
  "c.3873+2T>C": [
    "p.?",
    "c.3873+2T>C",
    "4005+2T->C"
  ],
  "4005+2T->C": [
    "p.?",
    "c.3873+2T>C",
    "4005+2T->C"
  ],
  "p.Ala959HisfsX9": [
    "p.Ala959HisfsX9",
    "c.2875del",
    "3007delG"
  ],
  "c.2875del": [
    "p.Ala959HisfsX9",
    "c.2875del",
    "3007delG"
  ],
  "3007delG": [
    "p.Ala959HisfsX9",
    "c.2875del",
    "3007delG"
  ],
  "4178G>A": [
    "4178G>A",
    "c.4046G>A",
    "G1349D",
    "p.Gly1349Asp"
  ],
  "c.4046G>A": [
    "4178G>A",
    "c.4046G>A",
    "G1349D",
    "p.Gly1349Asp"
  ],
  "G1349D": [
    "4178G>A",
    "c.4046G>A",
    "G1349D",
    "p.Gly1349Asp"
  ],
  "p.Gly1349Asp": [
    "4178G>A",
    "c.4046G>A",
    "G1349D",
    "p.Gly1349Asp"
  ],
  "p.Leu558Ser": [
    "p.Leu558Ser",
    "1805T>C",
    "c.1673T>C",
    "L558S"
  ],
  "1805T>C": [
    "p.Leu558Ser",
    "1805T>C",
    "c.1673T>C",
    "L558S"
  ],
  "c.1673T>C": [
    "p.Leu558Ser",
    "1805T>C",
    "c.1673T>C",
    "L558S"
  ],
  "L558S": [
    "p.Leu558Ser",
    "1805T>C",
    "c.1673T>C",
    "L558S"
  ],
  "p.Ser1455X": [
    "p.Ser1455X",
    "c.4364C>G",
    "4496C>G",
    "S1455X"
  ],
  "c.4364C>G": [
    "p.Ser1455X",
    "c.4364C>G",
    "4496C>G",
    "S1455X"
  ],
  "4496C>G": [
    "p.Ser1455X",
    "c.4364C>G",
    "4496C>G",
    "S1455X"
  ],
  "S1455X": [
    "p.Ser1455X",
    "c.4364C>G",
    "4496C>G",
    "S1455X"
  ],
  "p.Ile148LeufsX5": [
    "p.Ile148LeufsX5",
    "c.442del",
    "574delA"
  ],
  "c.442del": [
    "p.Ile148LeufsX5",
    "c.442del",
    "574delA"
  ],
  "574delA": [
    "p.Ile148LeufsX5",
    "c.442del",
    "574delA"
  ],
  "c.1130dup": [
    "c.1130dup",
    "1259insA",
    "p.Gln378AlafsX4",
    "1262insA|c.1127_1128insA"
  ],
  "1259insA": [
    "c.1130dup",
    "1259insA",
    "p.Gln378AlafsX4",
    "1262insA|c.1127_1128insA"
  ],
  "p.Gln378AlafsX4": [
    "c.1130dup",
    "1259insA",
    "p.Gln378AlafsX4",
    "1262insA|c.1127_1128insA"
  ],
  "1262insA|c.1127_1128insA": [
    "c.1130dup",
    "1259insA",
    "p.Gln378AlafsX4",
    "1262insA|c.1127_1128insA"
  ],
  "c.1826A>G": [
    "c.1826A>G",
    "H609R",
    "1958A>G",
    "p.His609Arg"
  ],
  "H609R": [
    "c.1826A>G",
    "H609R",
    "1958A>G",
    "p.His609Arg"
  ],
  "1958A>G": [
    "c.1826A>G",
    "H609R",
    "1958A>G",
    "p.His609Arg"
  ],
  "p.His609Arg": [
    "c.1826A>G",
    "H609R",
    "1958A>G",
    "p.His609Arg"
  ],
  "L927P": [
    "L927P",
    "c.2780T>C",
    "2912T>C",
    "p.Leu927Pro"
  ],
  "c.2780T>C": [
    "L927P",
    "c.2780T>C",
    "2912T>C",
    "p.Leu927Pro"
  ],
  "2912T>C": [
    "L927P",
    "c.2780T>C",
    "2912T>C",
    "p.Leu927Pro"
  ],
  "p.Leu927Pro": [
    "L927P",
    "c.2780T>C",
    "2912T>C",
    "p.Leu927Pro"
  ],
  "c.4004T>C": [
    "c.4004T>C",
    "L1335P",
    "p.Leu1335Pro",
    "4136T>C"
  ],
  "L1335P": [
    "c.4004T>C",
    "L1335P",
    "p.Leu1335Pro",
    "4136T>C"
  ],
  "p.Leu1335Pro": [
    "c.4004T>C",
    "L1335P",
    "p.Leu1335Pro",
    "4136T>C"
  ],
  "4136T>C": [
    "c.4004T>C",
    "L1335P",
    "p.Leu1335Pro",
    "4136T>C"
  ],
  "p.Ser341Pro": [
    "p.Ser341Pro",
    "1153T>C",
    "S341P",
    "c.1021T>C"
  ],
  "1153T>C": [
    "p.Ser341Pro",
    "1153T>C",
    "S341P",
    "c.1021T>C"
  ],
  "S341P": [
    "p.Ser341Pro",
    "1153T>C",
    "S341P",
    "c.1021T>C"
  ],
  "c.1021T>C": [
    "p.Ser341Pro",
    "1153T>C",
    "S341P",
    "c.1021T>C"
  ],
  "c.3937C>T": [
    "c.3937C>T",
    "4069C>T",
    "Q1313X",
    "p.Gln1313X"
  ],
  "4069C>T": [
    "c.3937C>T",
    "4069C>T",
    "Q1313X",
    "p.Gln1313X"
  ],
  "Q1313X": [
    "c.3937C>T",
    "4069C>T",
    "Q1313X",
    "p.Gln1313X"
  ],
  "p.Gln1313X": [
    "c.3937C>T",
    "4069C>T",
    "Q1313X",
    "p.Gln1313X"
  ],
  "1609delCA": [
    "1609delCA",
    "p.Gln493ValfsX10",
    "c.1477_1478del"
  ],
  "p.Gln493ValfsX10": [
    "1609delCA",
    "p.Gln493ValfsX10",
    "c.1477_1478del"
  ],
  "c.1477_1478del": [
    "1609delCA",
    "p.Gln493ValfsX10",
    "c.1477_1478del"
  ],
  "c.3181G>A|c.3181G>C": [
    "c.3181G>A|c.3181G>C",
    "G1061R",
    "3313G>C",
    "p.Gly1061Arg"
  ],
  "G1061R": [
    "c.3181G>A|c.3181G>C",
    "G1061R",
    "3313G>C",
    "p.Gly1061Arg"
  ],
  "3313G>C": [
    "c.3181G>A|c.3181G>C",
    "G1061R",
    "3313G>C",
    "p.Gly1061Arg"
  ],
  "p.Gly1061Arg": [
    "c.3181G>A|c.3181G>C",
    "G1061R",
    "3313G>C",
    "p.Gly1061Arg"
  ],
  "c.3873G>C": [
    "c.3873G>C",
    "p.Gln1291His",
    "4005G>C",
    "Q1291H"
  ],
  "p.Gln1291His": [
    "c.3873G>C",
    "p.Gln1291His",
    "4005G>C",
    "Q1291H"
  ],
  "4005G>C": [
    "c.3873G>C",
    "p.Gln1291His",
    "4005G>C",
    "Q1291H"
  ],
  "Q1291H": [
    "c.3873G>C",
    "p.Gln1291His",
    "4005G>C",
    "Q1291H"
  ],
  "p.Arg658LysfsX4": [
    "p.Arg658LysfsX4",
    "2105-2117del13insAGAAA",
    "c.1973_1985delGAAATTCAATCCTinsAGAAA",
    "c.1973_1985delinsAGAAA"
  ],
  "2105-2117del13insAGAAA": [
    "p.Arg658LysfsX4",
    "2105-2117del13insAGAAA",
    "c.1973_1985delGAAATTCAATCCTinsAGAAA",
    "c.1973_1985delinsAGAAA"
  ],
  "c.1973_1985delGAAATTCAATCCTinsAGAAA": [
    "p.Arg658LysfsX4",
    "2105-2117del13insAGAAA",
    "c.1973_1985delGAAATTCAATCCTinsAGAAA",
    "c.1973_1985delinsAGAAA"
  ],
  "c.1973_1985delinsAGAAA": [
    "p.Arg658LysfsX4",
    "2105-2117del13insAGAAA",
    "c.1973_1985delGAAATTCAATCCTinsAGAAA",
    "c.1973_1985delinsAGAAA"
  ],
  "c.(743+1_744-1)_(1584+1_1585-1)dup": [
    "c.(743+1_744-1)_(1584+1_1585-1)dup",
    "duplication of exons 6b, 7, 8, 9, and 10 (legacy numbering)|duplication of exons 7, 8, 9, 10, and 11 (current numbering)",
    "p.?",
    "CFTRdup6b-10"
  ],
  "duplication of exons 6b, 7, 8, 9, and 10 (legacy numbering)|duplication of exons 7, 8, 9, 10, and 11 (current numbering)": [
    "c.(743+1_744-1)_(1584+1_1585-1)dup",
    "duplication of exons 6b, 7, 8, 9, and 10 (legacy numbering)|duplication of exons 7, 8, 9, 10, and 11 (current numbering)",
    "p.?",
    "CFTRdup6b-10"
  ],
  "CFTRdup6b-10": [
    "c.(743+1_744-1)_(1584+1_1585-1)dup",
    "duplication of exons 6b, 7, 8, 9, and 10 (legacy numbering)|duplication of exons 7, 8, 9, 10, and 11 (current numbering)",
    "p.?",
    "CFTRdup6b-10"
  ],
  "p.Met1Val|133A>G": [
    "p.Met1Val|133A>G",
    "c.1A>G",
    "p.?",
    "M1V"
  ],
  "c.1A>G": [
    "p.Met1Val|133A>G",
    "c.1A>G",
    "p.?",
    "M1V"
  ],
  "M1V": [
    "p.Met1Val|133A>G",
    "c.1A>G",
    "p.?",
    "M1V"
  ],
  "4209TGTT->AA": [
    "4209TGTT->AA",
    "c.4077_4080delinsAA",
    "p.Val1360ThrfsX3"
  ],
  "c.4077_4080delinsAA": [
    "4209TGTT->AA",
    "c.4077_4080delinsAA",
    "p.Val1360ThrfsX3"
  ],
  "p.Val1360ThrfsX3": [
    "4209TGTT->AA",
    "c.4077_4080delinsAA",
    "p.Val1360ThrfsX3"
  ],
  "D1270N": [
    "D1270N",
    "3940G>A",
    "c.3808G>A",
    "p.Asp1270Asn"
  ],
  "3940G>A": [
    "D1270N",
    "3940G>A",
    "c.3808G>A",
    "p.Asp1270Asn"
  ],
  "c.3808G>A": [
    "D1270N",
    "3940G>A",
    "c.3808G>A",
    "p.Asp1270Asn"
  ],
  "p.Asp1270Asn": [
    "D1270N",
    "3940G>A",
    "c.3808G>A",
    "p.Asp1270Asn"
  ],
  "L218X": [
    "L218X",
    "c.653T>A",
    "785T>A",
    "p.Leu218X"
  ],
  "c.653T>A": [
    "L218X",
    "c.653T>A",
    "785T>A",
    "p.Leu218X"
  ],
  "785T>A": [
    "L218X",
    "c.653T>A",
    "785T>A",
    "p.Leu218X"
  ],
  "p.Leu218X": [
    "L218X",
    "c.653T>A",
    "785T>A",
    "p.Leu218X"
  ],
  "CFTRdele17a,17b": [
    "CFTRdele17a,17b",
    "c.(2988+1_2989-1)_(3367+1_3368-1)del",
    "p.?",
    "deletion of exons 17a and 17b (legacy numbering)|deletion of exons 19 and 20 (current numbering)|3121-977_3499+248del2515"
  ],
  "c.(2988+1_2989-1)_(3367+1_3368-1)del": [
    "CFTRdele17a,17b",
    "c.(2988+1_2989-1)_(3367+1_3368-1)del",
    "p.?",
    "deletion of exons 17a and 17b (legacy numbering)|deletion of exons 19 and 20 (current numbering)|3121-977_3499+248del2515"
  ],
  "deletion of exons 17a and 17b (legacy numbering)|deletion of exons 19 and 20 (current numbering)|3121-977_3499+248del2515": [
    "CFTRdele17a,17b",
    "c.(2988+1_2989-1)_(3367+1_3368-1)del",
    "p.?",
    "deletion of exons 17a and 17b (legacy numbering)|deletion of exons 19 and 20 (current numbering)|3121-977_3499+248del2515"
  ],
  "1717-8G->A": [
    "p.?",
    "1717-8G->A",
    "c.1585-8G>A"
  ],
  "c.1585-8G>A": [
    "p.?",
    "1717-8G->A",
    "c.1585-8G>A"
  ],
  "p.Ser641ArgfsX5": [
    "p.Ser641ArgfsX5",
    "c.1923_1931delCTCAAAACTinsA",
    "2055del9->A",
    "c.1923_1931delinsA"
  ],
  "c.1923_1931delCTCAAAACTinsA": [
    "p.Ser641ArgfsX5",
    "c.1923_1931delCTCAAAACTinsA",
    "2055del9->A",
    "c.1923_1931delinsA"
  ],
  "2055del9->A": [
    "p.Ser641ArgfsX5",
    "c.1923_1931delCTCAAAACTinsA",
    "2055del9->A",
    "c.1923_1931delinsA"
  ],
  "c.1923_1931delinsA": [
    "p.Ser641ArgfsX5",
    "c.1923_1931delCTCAAAACTinsA",
    "2055del9->A",
    "c.1923_1931delinsA"
  ],
  "c.1820_1903del": [
    "c.1820_1903del",
    "1949del84",
    "p.Met607_Gln634del"
  ],
  "1949del84": [
    "c.1820_1903del",
    "1949del84",
    "p.Met607_Gln634del"
  ],
  "p.Met607_Gln634del": [
    "c.1820_1903del",
    "1949del84",
    "p.Met607_Gln634del"
  ],
  "p.Asp614Gly": [
    "p.Asp614Gly",
    "1973A>G",
    "c.1841A>G",
    "D614G"
  ],
  "1973A>G": [
    "p.Asp614Gly",
    "1973A>G",
    "c.1841A>G",
    "D614G"
  ],
  "c.1841A>G": [
    "p.Asp614Gly",
    "1973A>G",
    "c.1841A>G",
    "D614G"
  ],
  "D614G": [
    "p.Asp614Gly",
    "1973A>G",
    "c.1841A>G",
    "D614G"
  ],
  "c.3611G>A|c.3612G>A": [
    "c.3611G>A|c.3612G>A",
    "p.Trp1204X",
    "W1204X",
    "3743G>A|3644G>A"
  ],
  "p.Trp1204X": [
    "c.3611G>A|c.3612G>A",
    "p.Trp1204X",
    "W1204X",
    "3743G>A|3644G>A"
  ],
  "W1204X": [
    "c.3611G>A|c.3612G>A",
    "p.Trp1204X",
    "W1204X",
    "3743G>A|3644G>A"
  ],
  "3743G>A|3644G>A": [
    "c.3611G>A|c.3612G>A",
    "p.Trp1204X",
    "W1204X",
    "3743G>A|3644G>A"
  ],
  "p.Tyr563Asn": [
    "p.Tyr563Asn",
    "c.1687T>A",
    "1819T>A",
    "Y563N"
  ],
  "c.1687T>A": [
    "p.Tyr563Asn",
    "c.1687T>A",
    "1819T>A",
    "Y563N"
  ],
  "1819T>A": [
    "p.Tyr563Asn",
    "c.1687T>A",
    "1819T>A",
    "Y563N"
  ],
  "Y563N": [
    "p.Tyr563Asn",
    "c.1687T>A",
    "1819T>A",
    "Y563N"
  ],
  "p.Gly1069Arg": [
    "p.Gly1069Arg",
    "3337G>A",
    "c.3205G>A",
    "G1069R"
  ],
  "3337G>A": [
    "p.Gly1069Arg",
    "3337G>A",
    "c.3205G>A",
    "G1069R"
  ],
  "c.3205G>A": [
    "p.Gly1069Arg",
    "3337G>A",
    "c.3205G>A",
    "G1069R"
  ],
  "G1069R": [
    "p.Gly1069Arg",
    "3337G>A",
    "c.3205G>A",
    "G1069R"
  ],
  "L967S": [
    "L967S",
    "3032T>C",
    "p.Leu967Ser",
    "c.2900T>C"
  ],
  "3032T>C": [
    "L967S",
    "3032T>C",
    "p.Leu967Ser",
    "c.2900T>C"
  ],
  "p.Leu967Ser": [
    "L967S",
    "3032T>C",
    "p.Leu967Ser",
    "c.2900T>C"
  ],
  "c.2900T>C": [
    "L967S",
    "3032T>C",
    "p.Leu967Ser",
    "c.2900T>C"
  ],
  "p.Ala1006Glu": [
    "p.Ala1006Glu",
    "A1006E",
    "c.3017C>A",
    "3149C>A"
  ],
  "A1006E": [
    "p.Ala1006Glu",
    "A1006E",
    "c.3017C>A",
    "3149C>A"
  ],
  "c.3017C>A": [
    "p.Ala1006Glu",
    "A1006E",
    "c.3017C>A",
    "3149C>A"
  ],
  "3149C>A": [
    "p.Ala1006Glu",
    "A1006E",
    "c.3017C>A",
    "3149C>A"
  ],
  "c.3737C>T": [
    "c.3737C>T",
    "T1246I",
    "3869C>T",
    "p.Thr1246Ile"
  ],
  "T1246I": [
    "c.3737C>T",
    "T1246I",
    "3869C>T",
    "p.Thr1246Ile"
  ],
  "3869C>T": [
    "c.3737C>T",
    "T1246I",
    "3869C>T",
    "p.Thr1246Ile"
  ],
  "p.Thr1246Ile": [
    "c.3737C>T",
    "T1246I",
    "3869C>T",
    "p.Thr1246Ile"
  ],
  "c.595C>T": [
    "c.595C>T",
    "H199Y",
    "p.His199Tyr",
    "727C>T"
  ],
  "H199Y": [
    "c.595C>T",
    "H199Y",
    "p.His199Tyr",
    "727C>T"
  ],
  "p.His199Tyr": [
    "c.595C>T",
    "H199Y",
    "p.His199Tyr",
    "727C>T"
  ],
  "727C>T": [
    "c.595C>T",
    "H199Y",
    "p.His199Tyr",
    "727C>T"
  ],
  "p.Phe312del": [
    "p.Phe312del",
    "c.935_937del",
    "F312del",
    "1067delTCT|[delta]F311"
  ],
  "c.935_937del": [
    "p.Phe312del",
    "c.935_937del",
    "F312del",
    "1067delTCT|[delta]F311"
  ],
  "F312del": [
    "p.Phe312del",
    "c.935_937del",
    "F312del",
    "1067delTCT|[delta]F311"
  ],
  "1067delTCT|[delta]F311": [
    "p.Phe312del",
    "c.935_937del",
    "F312del",
    "1067delTCT|[delta]F311"
  ],
  "G551S": [
    "G551S",
    "p.Gly551Ser",
    "1783G>A",
    "c.1651G>A"
  ],
  "p.Gly551Ser": [
    "G551S",
    "p.Gly551Ser",
    "1783G>A",
    "c.1651G>A"
  ],
  "1783G>A": [
    "G551S",
    "p.Gly551Ser",
    "1783G>A",
    "c.1651G>A"
  ],
  "c.1651G>A": [
    "G551S",
    "p.Gly551Ser",
    "1783G>A",
    "c.1651G>A"
  ],
  "c.292C>T": [
    "c.292C>T",
    "424C>T",
    "Q98X",
    "p.Gln98X"
  ],
  "424C>T": [
    "c.292C>T",
    "424C>T",
    "Q98X",
    "p.Gln98X"
  ],
  "Q98X": [
    "c.292C>T",
    "424C>T",
    "Q98X",
    "p.Gln98X"
  ],
  "p.Gln98X": [
    "c.292C>T",
    "424C>T",
    "Q98X",
    "p.Gln98X"
  ],
  "Y1032C": [
    "Y1032C",
    "c.3095A>G",
    "3227A>G",
    "p.Tyr1032Cys"
  ],
  "c.3095A>G": [
    "Y1032C",
    "c.3095A>G",
    "3227A>G",
    "p.Tyr1032Cys"
  ],
  "3227A>G": [
    "Y1032C",
    "c.3095A>G",
    "3227A>G",
    "p.Tyr1032Cys"
  ],
  "p.Tyr1032Cys": [
    "Y1032C",
    "c.3095A>G",
    "3227A>G",
    "p.Tyr1032Cys"
  ],
  "3442G>T": [
    "3442G>T",
    "c.3310G>T",
    "p.Glu1104X",
    "E1104X"
  ],
  "c.3310G>T": [
    "3442G>T",
    "c.3310G>T",
    "p.Glu1104X",
    "E1104X"
  ],
  "p.Glu1104X": [
    "3442G>T",
    "c.3310G>T",
    "p.Glu1104X",
    "E1104X"
  ],
  "E1104X": [
    "3442G>T",
    "c.3310G>T",
    "p.Glu1104X",
    "E1104X"
  ],
  "3896C>A": [
    "3896C>A",
    "c.3764C>A",
    "p.Ser1255X",
    "S1255X"
  ],
  "c.3764C>A": [
    "3896C>A",
    "c.3764C>A",
    "p.Ser1255X",
    "S1255X"
  ],
  "p.Ser1255X": [
    "3896C>A",
    "c.3764C>A",
    "p.Ser1255X",
    "S1255X"
  ],
  "S1255X": [
    "3896C>A",
    "c.3764C>A",
    "p.Ser1255X",
    "S1255X"
  ],
  "3600G->A": [
    "3600G->A",
    "c.3468G>A",
    "p.Leu1156Leu|L1156L",
    "p.Leu1156="
  ],
  "c.3468G>A": [
    "3600G->A",
    "c.3468G>A",
    "p.Leu1156Leu|L1156L",
    "p.Leu1156="
  ],
  "p.Leu1156Leu|L1156L": [
    "3600G->A",
    "c.3468G>A",
    "p.Leu1156Leu|L1156L",
    "p.Leu1156="
  ],
  "p.Leu1156=": [
    "3600G->A",
    "c.3468G>A",
    "p.Leu1156Leu|L1156L",
    "p.Leu1156="
  ],
  "c.2989-1G>A": [
    "c.2989-1G>A",
    "p.?",
    "3121-1G->A"
  ],
  "3121-1G->A": [
    "c.2989-1G>A",
    "p.?",
    "3121-1G->A"
  ],
  "p.Ile177MetfsX12": [
    "p.Ile177MetfsX12",
    "c.531del",
    "663delT"
  ],
  "c.531del": [
    "p.Ile177MetfsX12",
    "c.531del",
    "663delT"
  ],
  "663delT": [
    "p.Ile177MetfsX12",
    "c.531del",
    "663delT"
  ],
  "p.Ser1231ProfsX4": [
    "p.Ser1231ProfsX4",
    "c.3691del",
    "3821delT"
  ],
  "c.3691del": [
    "p.Ser1231ProfsX4",
    "c.3691del",
    "3821delT"
  ],
  "3821delT": [
    "p.Ser1231ProfsX4",
    "c.3691del",
    "3821delT"
  ],
  "p.Asn268IlefsX17": [
    "p.Asn268IlefsX17",
    "935delA",
    "c.803del"
  ],
  "935delA": [
    "p.Asn268IlefsX17",
    "935delA",
    "c.803del"
  ],
  "c.803del": [
    "p.Asn268IlefsX17",
    "935delA",
    "c.803del"
  ],
  "c.293A>G": [
    "c.293A>G",
    "p.Gln98Arg",
    "Q98R",
    "425A>G"
  ],
  "p.Gln98Arg": [
    "c.293A>G",
    "p.Gln98Arg",
    "Q98R",
    "425A>G"
  ],
  "Q98R": [
    "c.293A>G",
    "p.Gln98Arg",
    "Q98R",
    "425A>G"
  ],
  "425A>G": [
    "c.293A>G",
    "p.Gln98Arg",
    "Q98R",
    "425A>G"
  ],
  "I336fs": [
    "I336fs",
    "c.1006_1007insG",
    "p.Ile336SerfsX28",
    "1138insG"
  ],
  "c.1006_1007insG": [
    "I336fs",
    "c.1006_1007insG",
    "p.Ile336SerfsX28",
    "1138insG"
  ],
  "p.Ile336SerfsX28": [
    "I336fs",
    "c.1006_1007insG",
    "p.Ile336SerfsX28",
    "1138insG"
  ],
  "1138insG": [
    "I336fs",
    "c.1006_1007insG",
    "p.Ile336SerfsX28",
    "1138insG"
  ],
  "1471delA": [
    "1471delA",
    "p.Lys447ArgfsX2",
    "c.1340del"
  ],
  "p.Lys447ArgfsX2": [
    "1471delA",
    "p.Lys447ArgfsX2",
    "c.1340del"
  ],
  "c.1340del": [
    "1471delA",
    "p.Lys447ArgfsX2",
    "c.1340del"
  ],
  "c.220C>T": [
    "c.220C>T",
    "p.Arg74Trp",
    "R74W",
    "352C>T"
  ],
  "p.Arg74Trp": [
    "c.220C>T",
    "p.Arg74Trp",
    "R74W",
    "352C>T"
  ],
  "R74W": [
    "c.220C>T",
    "p.Arg74Trp",
    "R74W",
    "352C>T"
  ],
  "352C>T": [
    "c.220C>T",
    "p.Arg74Trp",
    "R74W",
    "352C>T"
  ],
  "c.377G>A": [
    "c.377G>A",
    "509G>A",
    "G126D",
    "p.Gly126Asp"
  ],
  "509G>A": [
    "c.377G>A",
    "509G>A",
    "G126D",
    "p.Gly126Asp"
  ],
  "G126D": [
    "c.377G>A",
    "509G>A",
    "G126D",
    "p.Gly126Asp"
  ],
  "p.Gly126Asp": [
    "c.377G>A",
    "509G>A",
    "G126D",
    "p.Gly126Asp"
  ],
  "p.Asn386IlefsX3": [
    "p.Asn386IlefsX3",
    "c.1155_1156dup",
    "1288insTA",
    "c.1152_1153dupAT"
  ],
  "c.1155_1156dup": [
    "p.Asn386IlefsX3",
    "c.1155_1156dup",
    "1288insTA",
    "c.1152_1153dupAT"
  ],
  "1288insTA": [
    "p.Asn386IlefsX3",
    "c.1155_1156dup",
    "1288insTA",
    "c.1152_1153dupAT"
  ],
  "c.1152_1153dupAT": [
    "p.Asn386IlefsX3",
    "c.1155_1156dup",
    "1288insTA",
    "c.1152_1153dupAT"
  ],
  "p.Gly473GlufsX54": [
    "p.Gly473GlufsX54",
    "1550delG",
    "c.1418del",
    "1548delG"
  ],
  "1550delG": [
    "p.Gly473GlufsX54",
    "1550delG",
    "c.1418del",
    "1548delG"
  ],
  "c.1418del": [
    "p.Gly473GlufsX54",
    "1550delG",
    "c.1418del",
    "1548delG"
  ],
  "1548delG": [
    "p.Gly473GlufsX54",
    "1550delG",
    "c.1418del",
    "1548delG"
  ],
  "p.Leu227Arg": [
    "p.Leu227Arg",
    "c.680T>G",
    "812T>G",
    "L227R"
  ],
  "c.680T>G": [
    "p.Leu227Arg",
    "c.680T>G",
    "812T>G",
    "L227R"
  ],
  "812T>G": [
    "p.Leu227Arg",
    "c.680T>G",
    "812T>G",
    "L227R"
  ],
  "L227R": [
    "p.Leu227Arg",
    "c.680T>G",
    "812T>G",
    "L227R"
  ],
  "c.3883del": [
    "c.3883del",
    "4015delA",
    "p.Ile1295PhefsX33"
  ],
  "4015delA": [
    "c.3883del",
    "4015delA",
    "p.Ile1295PhefsX33"
  ],
  "p.Ile1295PhefsX33": [
    "c.3883del",
    "4015delA",
    "p.Ile1295PhefsX33"
  ],
  "c.91C>T": [
    "c.91C>T",
    "R31C",
    "p.Arg31Cys",
    "223C>T"
  ],
  "R31C": [
    "c.91C>T",
    "R31C",
    "p.Arg31Cys",
    "223C>T"
  ],
  "p.Arg31Cys": [
    "c.91C>T",
    "R31C",
    "p.Arg31Cys",
    "223C>T"
  ],
  "223C>T": [
    "c.91C>T",
    "R31C",
    "p.Arg31Cys",
    "223C>T"
  ],
  "R792X": [
    "R792X",
    "c.2374C>T",
    "p.Arg792X",
    "2506C>T"
  ],
  "c.2374C>T": [
    "R792X",
    "c.2374C>T",
    "p.Arg792X",
    "2506C>T"
  ],
  "p.Arg792X": [
    "R792X",
    "c.2374C>T",
    "p.Arg792X",
    "2506C>T"
  ],
  "2506C>T": [
    "R792X",
    "c.2374C>T",
    "p.Arg792X",
    "2506C>T"
  ],
  "3893T>G": [
    "3893T>G",
    "c.3761T>A|c.3761T>G",
    "L1254X",
    "p.Leu1254X"
  ],
  "c.3761T>A|c.3761T>G": [
    "3893T>G",
    "c.3761T>A|c.3761T>G",
    "L1254X",
    "p.Leu1254X"
  ],
  "L1254X": [
    "3893T>G",
    "c.3761T>A|c.3761T>G",
    "L1254X",
    "p.Leu1254X"
  ],
  "p.Leu1254X": [
    "3893T>G",
    "c.3761T>A|c.3761T>G",
    "L1254X",
    "p.Leu1254X"
  ],
  "3791delC": [
    "3791delC",
    "c.3659del",
    "p.Thr1220LysfsX8"
  ],
  "c.3659del": [
    "3791delC",
    "c.3659del",
    "p.Thr1220LysfsX8"
  ],
  "p.Thr1220LysfsX8": [
    "3791delC",
    "c.3659del",
    "p.Thr1220LysfsX8"
  ],
  "2585delT": [
    "2585delT",
    "c.2453del",
    "p.Leu818TrpfsX3"
  ],
  "c.2453del": [
    "2585delT",
    "c.2453del",
    "p.Leu818TrpfsX3"
  ],
  "p.Leu818TrpfsX3": [
    "2585delT",
    "c.2453del",
    "p.Leu818TrpfsX3"
  ],
  "2392G>A": [
    "2392G>A",
    "c.2260G>A",
    "V754M",
    "p.Val754Met"
  ],
  "c.2260G>A": [
    "2392G>A",
    "c.2260G>A",
    "V754M",
    "p.Val754Met"
  ],
  "V754M": [
    "2392G>A",
    "c.2260G>A",
    "V754M",
    "p.Val754Met"
  ],
  "p.Val754Met": [
    "2392G>A",
    "c.2260G>A",
    "V754M",
    "p.Val754Met"
  ],
  "4558C>T": [
    "4558C>T",
    "Q1476X",
    "p.Gln1476X",
    "c.4426C>T"
  ],
  "Q1476X": [
    "4558C>T",
    "Q1476X",
    "p.Gln1476X",
    "c.4426C>T"
  ],
  "p.Gln1476X": [
    "4558C>T",
    "Q1476X",
    "p.Gln1476X",
    "c.4426C>T"
  ],
  "c.4426C>T": [
    "4558C>T",
    "Q1476X",
    "p.Gln1476X",
    "c.4426C>T"
  ],
  "3600+2insT": [
    "3600+2insT",
    "c.3468+2dup",
    "c.3468+2_3468+3insT",
    "p.?"
  ],
  "c.3468+2dup": [
    "3600+2insT",
    "c.3468+2dup",
    "c.3468+2_3468+3insT",
    "p.?"
  ],
  "c.3468+2_3468+3insT": [
    "3600+2insT",
    "c.3468+2dup",
    "c.3468+2_3468+3insT",
    "p.?"
  ],
  "1811+1G->C": [
    "1811+1G->C",
    "c.1679+1G>C",
    "p.?"
  ],
  "c.1679+1G>C": [
    "1811+1G->C",
    "c.1679+1G>C",
    "p.?"
  ],
  "4374+1G->T": [
    "p.?",
    "4374+1G->T",
    "c.4242+1G>T"
  ],
  "c.4242+1G>T": [
    "p.?",
    "4374+1G->T",
    "c.4242+1G>T"
  ],
  "2869insG": [
    "2869insG",
    "c.2737_2738insG",
    "p.Tyr913X"
  ],
  "c.2737_2738insG": [
    "2869insG",
    "c.2737_2738insG",
    "p.Tyr913X"
  ],
  "p.Tyr913X": [
    "p.Tyr913X",
    "2871T>A",
    "c.2739T>A",
    "Y913X"
  ],
  "P574H": [
    "P574H",
    "c.1721C>A",
    "p.Pro574His",
    "1853C>A"
  ],
  "c.1721C>A": [
    "P574H",
    "c.1721C>A",
    "p.Pro574His",
    "1853C>A"
  ],
  "p.Pro574His": [
    "P574H",
    "c.1721C>A",
    "p.Pro574His",
    "1853C>A"
  ],
  "1853C>A": [
    "P574H",
    "c.1721C>A",
    "p.Pro574His",
    "1853C>A"
  ],
  "2118del4": [
    "2118del4",
    "p.Thr663ArgfsX8",
    "c.1986_1989del",
    "2116delCTAA"
  ],
  "p.Thr663ArgfsX8": [
    "2118del4",
    "p.Thr663ArgfsX8",
    "c.1986_1989del",
    "2116delCTAA"
  ],
  "c.1986_1989del": [
    "2118del4",
    "p.Thr663ArgfsX8",
    "c.1986_1989del",
    "2116delCTAA"
  ],
  "2116delCTAA": [
    "2118del4",
    "p.Thr663ArgfsX8",
    "c.1986_1989del",
    "2116delCTAA"
  ],
  "S1159F": [
    "S1159F",
    "p.Ser1159Phe",
    "c.3476C>T",
    "3608C>T"
  ],
  "p.Ser1159Phe": [
    "S1159F",
    "p.Ser1159Phe",
    "c.3476C>T",
    "3608C>T"
  ],
  "c.3476C>T": [
    "S1159F",
    "p.Ser1159Phe",
    "c.3476C>T",
    "3608C>T"
  ],
  "3608C>T": [
    "S1159F",
    "p.Ser1159Phe",
    "c.3476C>T",
    "3608C>T"
  ],
  "709G>T": [
    "709G>T",
    "E193X",
    "c.577G>T",
    "p.Glu193X"
  ],
  "E193X": [
    "709G>T",
    "E193X",
    "c.577G>T",
    "p.Glu193X"
  ],
  "c.577G>T": [
    "709G>T",
    "E193X",
    "c.577G>T",
    "p.Glu193X"
  ],
  "p.Glu193X": [
    "709G>T",
    "E193X",
    "c.577G>T",
    "p.Glu193X"
  ],
  "c.1075_1079delCAAACinsAAAAA|p.Gln359_Thr360delinsLysLys|[1207C>A or1211C>A]": [
    "c.1075_1079delCAAACinsAAAAA|p.Gln359_Thr360delinsLysLys|[1207C>A or1211C>A]",
    "c.[1075C>A;1079C>A]",
    "p.Gln359_Thr360delinsLysLys",
    "Q359K/T360K"
  ],
  "c.[1075C>A;1079C>A]": [
    "c.1075_1079delCAAACinsAAAAA|p.Gln359_Thr360delinsLysLys|[1207C>A or1211C>A]",
    "c.[1075C>A;1079C>A]",
    "p.Gln359_Thr360delinsLysLys",
    "Q359K/T360K"
  ],
  "p.Gln359_Thr360delinsLysLys": [
    "c.1075_1079delCAAACinsAAAAA|p.Gln359_Thr360delinsLysLys|[1207C>A or1211C>A]",
    "c.[1075C>A;1079C>A]",
    "p.Gln359_Thr360delinsLysLys",
    "Q359K/T360K"
  ],
  "Q359K/T360K": [
    "c.1075_1079delCAAACinsAAAAA|p.Gln359_Thr360delinsLysLys|[1207C>A or1211C>A]",
    "c.[1075C>A;1079C>A]",
    "p.Gln359_Thr360delinsLysLys",
    "Q359K/T360K"
  ],
  "c.1001G>T": [
    "c.1001G>T",
    "R334L",
    "p.Arg334Leu",
    "1133G>T"
  ],
  "R334L": [
    "c.1001G>T",
    "R334L",
    "p.Arg334Leu",
    "1133G>T"
  ],
  "p.Arg334Leu": [
    "c.1001G>T",
    "R334L",
    "p.Arg334Leu",
    "1133G>T"
  ],
  "1133G>T": [
    "c.1001G>T",
    "R334L",
    "p.Arg334Leu",
    "1133G>T"
  ],
  "p.Cys1400X": [
    "4332T>A",
    "c.4200T>A",
    "p.Cys1400X",
    "C1400X"
  ],
  "c.4197_4198del": [
    "p.Cys1400X",
    "c.4197_4198del",
    "4326delTC",
    "4329delCT|c.4196_4197delTC"
  ],
  "4326delTC": [
    "p.Cys1400X",
    "c.4197_4198del",
    "4326delTC",
    "4329delCT|c.4196_4197delTC"
  ],
  "4329delCT|c.4196_4197delTC": [
    "p.Cys1400X",
    "c.4197_4198del",
    "4326delTC",
    "4329delCT|c.4196_4197delTC"
  ],
  "deletion of exons 4 through 10 (legacy numbering)|deletion of exons 4 through 11 (current numbering)": [
    "deletion of exons 4 through 10 (legacy numbering)|deletion of exons 4 through 11 (current numbering)",
    "p.?",
    "c.(273+1_274-1)_(1584+1_1585-1)del",
    "CFTRdele4-10"
  ],
  "c.(273+1_274-1)_(1584+1_1585-1)del": [
    "deletion of exons 4 through 10 (legacy numbering)|deletion of exons 4 through 11 (current numbering)",
    "p.?",
    "c.(273+1_274-1)_(1584+1_1585-1)del",
    "CFTRdele4-10"
  ],
  "CFTRdele4-10": [
    "deletion of exons 4 through 10 (legacy numbering)|deletion of exons 4 through 11 (current numbering)",
    "p.?",
    "c.(273+1_274-1)_(1584+1_1585-1)del",
    "CFTRdele4-10"
  ],
  "c.3873+1G>A": [
    "c.3873+1G>A",
    "4005+1G->A",
    "p.?"
  ],
  "4005+1G->A": [
    "c.3873+1G>A",
    "4005+1G->A",
    "p.?"
  ],
  "4035delA": [
    "4035delA",
    "4040delA",
    "p.Asn1303ThrfsX25",
    "c.3908del"
  ],
  "4040delA": [
    "4035delA",
    "4040delA",
    "p.Asn1303ThrfsX25",
    "c.3908del"
  ],
  "p.Asn1303ThrfsX25": [
    "4035delA",
    "4040delA",
    "p.Asn1303ThrfsX25",
    "c.3908del"
  ],
  "c.3908del": [
    "4035delA",
    "4040delA",
    "p.Asn1303ThrfsX25",
    "c.3908del"
  ],
  "c.1209+1G>A": [
    "p.?",
    "c.1209+1G>A",
    "1341+1G->A"
  ],
  "1341+1G->A": [
    "p.?",
    "c.1209+1G>A",
    "1341+1G->A"
  ],
  "1161delC": [
    "1161delC",
    "p.Cys343X",
    "c.1029del"
  ],
  "p.Cys343X": [
    "1161delC",
    "p.Cys343X",
    "c.1029del"
  ],
  "c.1029del": [
    "1161delC",
    "p.Cys343X",
    "c.1029del"
  ],
  "p.Asn415X": [
    "p.Asn415X",
    "1367del5",
    "c.1243_1247del"
  ],
  "1367del5": [
    "p.Asn415X",
    "1367del5",
    "c.1243_1247del"
  ],
  "c.1243_1247del": [
    "p.Asn415X",
    "1367del5",
    "c.1243_1247del"
  ],
  "c.2735C>A": [
    "c.2735C>A",
    "p.Ser912X",
    "2867C>A",
    "S912X"
  ],
  "p.Ser912X": [
    "c.2735C>A",
    "p.Ser912X",
    "2867C>A",
    "S912X"
  ],
  "2867C>A": [
    "c.2735C>A",
    "p.Ser912X",
    "2867C>A",
    "S912X"
  ],
  "S912X": [
    "c.2735C>A",
    "p.Ser912X",
    "2867C>A",
    "S912X"
  ],
  "3041G>A": [
    "3041G>A",
    "p.Gly970Asp",
    "G970D",
    "c.2909G>A"
  ],
  "p.Gly970Asp": [
    "3041G>A",
    "p.Gly970Asp",
    "G970D",
    "c.2909G>A"
  ],
  "G970D": [
    "3041G>A",
    "p.Gly970Asp",
    "G970D",
    "c.2909G>A"
  ],
  "c.2909G>A": [
    "3041G>A",
    "p.Gly970Asp",
    "G970D",
    "c.2909G>A"
  ],
  "4061G>A": [
    "4061G>A",
    "p.Trp1310X",
    "c.3929G>A|c.3930G>A",
    "W1310X"
  ],
  "p.Trp1310X": [
    "4061G>A",
    "p.Trp1310X",
    "c.3929G>A|c.3930G>A",
    "W1310X"
  ],
  "c.3929G>A|c.3930G>A": [
    "4061G>A",
    "p.Trp1310X",
    "c.3929G>A|c.3930G>A",
    "W1310X"
  ],
  "W1310X": [
    "4061G>A",
    "p.Trp1310X",
    "c.3929G>A|c.3930G>A",
    "W1310X"
  ],
  "c.494T>C": [
    "c.494T>C",
    "p.Leu165Ser",
    "L165S",
    "626T>C"
  ],
  "p.Leu165Ser": [
    "c.494T>C",
    "p.Leu165Ser",
    "L165S",
    "626T>C"
  ],
  "L165S": [
    "c.494T>C",
    "p.Leu165Ser",
    "L165S",
    "626T>C"
  ],
  "626T>C": [
    "c.494T>C",
    "p.Leu165Ser",
    "L165S",
    "626T>C"
  ],
  "c.828C>A": [
    "c.828C>A",
    "C276X",
    "960C>A",
    "p.Cys276X"
  ],
  "C276X": [
    "c.828C>A",
    "C276X",
    "960C>A",
    "p.Cys276X"
  ],
  "960C>A": [
    "c.828C>A",
    "C276X",
    "960C>A",
    "p.Cys276X"
  ],
  "p.Cys276X": [
    "c.828C>A",
    "C276X",
    "960C>A",
    "p.Cys276X"
  ],
  "c.(2619+1_2620-1)_(3367+1_3368-1)del": [
    "c.(2619+1_2620-1)_(3367+1_3368-1)del",
    "deletion of exons 14b, 15, 16, 17a, and 17b (legacy numbering)|deletion of exons 16, 17, 18, 19, and 20 (current numbering)",
    "p.?",
    "CFTRdele14b-17b"
  ],
  "deletion of exons 14b, 15, 16, 17a, and 17b (legacy numbering)|deletion of exons 16, 17, 18, 19, and 20 (current numbering)": [
    "c.(2619+1_2620-1)_(3367+1_3368-1)del",
    "deletion of exons 14b, 15, 16, 17a, and 17b (legacy numbering)|deletion of exons 16, 17, 18, 19, and 20 (current numbering)",
    "p.?",
    "CFTRdele14b-17b"
  ],
  "CFTRdele14b-17b": [
    "c.(2619+1_2620-1)_(3367+1_3368-1)del",
    "deletion of exons 14b, 15, 16, 17a, and 17b (legacy numbering)|deletion of exons 16, 17, 18, 19, and 20 (current numbering)",
    "p.?",
    "CFTRdele14b-17b"
  ],
  "3849G->A": [
    "3849G->A",
    "c.3717G>A",
    "p.Arg1239=",
    "R1239R"
  ],
  "c.3717G>A": [
    "3849G->A",
    "c.3717G>A",
    "p.Arg1239=",
    "R1239R"
  ],
  "p.Arg1239=": [
    "3849G->A",
    "c.3717G>A",
    "p.Arg1239=",
    "R1239R"
  ],
  "R1239R": [
    "3849G->A",
    "c.3717G>A",
    "p.Arg1239=",
    "R1239R"
  ],
  "301T>G": [
    "301T>G",
    "p.Trp57Gly",
    "c.169T>G",
    "W57G"
  ],
  "p.Trp57Gly": [
    "301T>G",
    "p.Trp57Gly",
    "c.169T>G",
    "W57G"
  ],
  "c.169T>G": [
    "301T>G",
    "p.Trp57Gly",
    "c.169T>G",
    "W57G"
  ],
  "W57G": [
    "301T>G",
    "p.Trp57Gly",
    "c.169T>G",
    "W57G"
  ],
  "993delCTTAA|c.859_863delAACTT": [
    "993delCTTAA|c.859_863delAACTT",
    "991del5",
    "c.861_865del",
    "p.Asn287LysfsX19"
  ],
  "991del5": [
    "993delCTTAA|c.859_863delAACTT",
    "991del5",
    "c.861_865del",
    "p.Asn287LysfsX19"
  ],
  "c.861_865del": [
    "993delCTTAA|c.859_863delAACTT",
    "991del5",
    "c.861_865del",
    "p.Asn287LysfsX19"
  ],
  "p.Asn287LysfsX19": [
    "993delCTTAA|c.859_863delAACTT",
    "991del5",
    "c.861_865del",
    "p.Asn287LysfsX19"
  ],
  "182delT": [
    "182delT",
    "c.50del",
    "p.Phe17SerfsX8"
  ],
  "c.50del": [
    "182delT",
    "c.50del",
    "p.Phe17SerfsX8"
  ],
  "p.Phe17SerfsX8": [
    "182delT",
    "c.50del",
    "p.Phe17SerfsX8"
  ],
  "3130delA": [
    "3130delA",
    "p.Ile1000LeufsX2",
    "c.2998del"
  ],
  "p.Ile1000LeufsX2": [
    "3130delA",
    "p.Ile1000LeufsX2",
    "c.2998del"
  ],
  "c.2998del": [
    "3130delA",
    "p.Ile1000LeufsX2",
    "c.2998del"
  ],
  "1120G>T": [
    "1120G>T",
    "c.988G>T",
    "G330X",
    "p.Gly330X"
  ],
  "c.988G>T": [
    "1120G>T",
    "c.988G>T",
    "G330X",
    "p.Gly330X"
  ],
  "G330X": [
    "1120G>T",
    "c.988G>T",
    "G330X",
    "p.Gly330X"
  ],
  "p.Gly330X": [
    "1120G>T",
    "c.988G>T",
    "G330X",
    "p.Gly330X"
  ],
  "p.Val562Ile": [
    "p.Val562Ile",
    "1816G>A",
    "c.1684G>A",
    "V562I"
  ],
  "1816G>A": [
    "p.Val562Ile",
    "1816G>A",
    "c.1684G>A",
    "V562I"
  ],
  "c.1684G>A": [
    "p.Val562Ile",
    "1816G>A",
    "c.1684G>A",
    "V562I"
  ],
  "V562I": [
    "p.Val562Ile",
    "1816G>A",
    "c.1684G>A",
    "V562I"
  ],
  "S977F": [
    "S977F",
    "3062C>T",
    "c.2930C>T",
    "p.Ser977Phe"
  ],
  "3062C>T": [
    "S977F",
    "3062C>T",
    "c.2930C>T",
    "p.Ser977Phe"
  ],
  "c.2930C>T": [
    "S977F",
    "3062C>T",
    "c.2930C>T",
    "p.Ser977Phe"
  ],
  "p.Ser977Phe": [
    "S977F",
    "3062C>T",
    "c.2930C>T",
    "p.Ser977Phe"
  ],
  "p.His1054Asp": [
    "p.His1054Asp",
    "3292C>G",
    "H1054D",
    "c.3160C>G"
  ],
  "3292C>G": [
    "p.His1054Asp",
    "3292C>G",
    "H1054D",
    "c.3160C>G"
  ],
  "H1054D": [
    "p.His1054Asp",
    "3292C>G",
    "H1054D",
    "c.3160C>G"
  ],
  "c.3160C>G": [
    "p.His1054Asp",
    "3292C>G",
    "H1054D",
    "c.3160C>G"
  ],
  "4243G>T": [
    "4243G>T",
    "c.4111G>T",
    "p.Glu1371X",
    "E1371X"
  ],
  "c.4111G>T": [
    "4243G>T",
    "c.4111G>T",
    "p.Glu1371X",
    "E1371X"
  ],
  "p.Glu1371X": [
    "4243G>T",
    "c.4111G>T",
    "p.Glu1371X",
    "E1371X"
  ],
  "E1371X": [
    "4243G>T",
    "c.4111G>T",
    "p.Glu1371X",
    "E1371X"
  ],
  "852del22": [
    "852del22",
    "p.?",
    "c.720_741delAGGGAGAATGATGATGAAGTAC",
    "c.723_743+1del"
  ],
  "c.720_741delAGGGAGAATGATGATGAAGTAC": [
    "852del22",
    "p.?",
    "c.720_741delAGGGAGAATGATGATGAAGTAC",
    "c.723_743+1del"
  ],
  "c.723_743+1del": [
    "852del22",
    "p.?",
    "c.720_741delAGGGAGAATGATGATGAAGTAC",
    "c.723_743+1del"
  ],
  "p.Gln637HisfsX26": [
    "p.Gln637HisfsX26",
    "2043delG",
    "c.1911del"
  ],
  "2043delG": [
    "p.Gln637HisfsX26",
    "2043delG",
    "c.1911del"
  ],
  "c.1911del": [
    "p.Gln637HisfsX26",
    "2043delG",
    "c.1911del"
  ],
  "c.1202G>A|c.1203G>A": [
    "c.1202G>A|c.1203G>A",
    "W401X(TAG)|W401X(TGA)|1334G>A|1335G>A",
    "p.Trp401X",
    "W401X"
  ],
  "W401X(TAG)|W401X(TGA)|1334G>A|1335G>A": [
    "c.1202G>A|c.1203G>A",
    "W401X(TAG)|W401X(TGA)|1334G>A|1335G>A",
    "p.Trp401X",
    "W401X"
  ],
  "p.Trp401X": [
    "c.1202G>A|c.1203G>A",
    "W401X(TAG)|W401X(TGA)|1334G>A|1335G>A",
    "p.Trp401X",
    "W401X"
  ],
  "W401X": [
    "c.1202G>A|c.1203G>A",
    "W401X(TAG)|W401X(TGA)|1334G>A|1335G>A",
    "p.Trp401X",
    "W401X"
  ],
  "1898+1G->C": [
    "1898+1G->C",
    "p.?",
    "c.1766+1G>C"
  ],
  "c.1766+1G>C": [
    "1898+1G->C",
    "p.?",
    "c.1766+1G>C"
  ],
  "S434X": [
    "S434X",
    "p.Ser434X",
    "1433C>G|1433C>A",
    "c.1301C>A|c.1301C>G"
  ],
  "p.Ser434X": [
    "S434X",
    "p.Ser434X",
    "1433C>G|1433C>A",
    "c.1301C>A|c.1301C>G"
  ],
  "1433C>G|1433C>A": [
    "S434X",
    "p.Ser434X",
    "1433C>G|1433C>A",
    "c.1301C>A|c.1301C>G"
  ],
  "c.1301C>A|c.1301C>G": [
    "S434X",
    "p.Ser434X",
    "1433C>G|1433C>A",
    "c.1301C>A|c.1301C>G"
  ],
  "2871T>A": [
    "p.Tyr913X",
    "2871T>A",
    "c.2739T>A",
    "Y913X"
  ],
  "c.2739T>A": [
    "p.Tyr913X",
    "2871T>A",
    "c.2739T>A",
    "Y913X"
  ],
  "Y913X": [
    "p.Tyr913X",
    "2871T>A",
    "c.2739T>A",
    "Y913X"
  ],
  "307insA|c.174_175insA": [
    "307insA|c.174_175insA",
    "c.175dup",
    "306insA",
    "p.Arg59LysfsX10"
  ],
  "c.175dup": [
    "307insA|c.174_175insA",
    "c.175dup",
    "306insA",
    "p.Arg59LysfsX10"
  ],
  "306insA": [
    "307insA|c.174_175insA",
    "c.175dup",
    "306insA",
    "p.Arg59LysfsX10"
  ],
  "p.Arg59LysfsX10": [
    "307insA|c.174_175insA",
    "c.175dup",
    "306insA",
    "p.Arg59LysfsX10"
  ],
  "c.330C>A": [
    "c.330C>A",
    "462C>A",
    "p.Asp110Glu",
    "D110E"
  ],
  "462C>A": [
    "c.330C>A",
    "462C>A",
    "p.Asp110Glu",
    "D110E"
  ],
  "p.Asp110Glu": [
    "c.330C>A",
    "462C>A",
    "p.Asp110Glu",
    "D110E"
  ],
  "D110E": [
    "c.330C>A",
    "462C>A",
    "p.Asp110Glu",
    "D110E"
  ],
  "3500-2A->G": [
    "3500-2A->G",
    "p.?",
    "c.3368-2A>G"
  ],
  "c.3368-2A>G": [
    "3500-2A->G",
    "p.?",
    "c.3368-2A>G"
  ],
  "c.3816_3817del": [
    "c.3816_3817del",
    "p.Ser1273LeufsX28",
    "3944delGT"
  ],
  "p.Ser1273LeufsX28": [
    "c.3816_3817del",
    "p.Ser1273LeufsX28",
    "3944delGT"
  ],
  "3944delGT": [
    "c.3816_3817del",
    "p.Ser1273LeufsX28",
    "3944delGT"
  ],
  "c.1505T>C": [
    "c.1505T>C",
    "I502T",
    "p.Ile502Thr",
    "1637T>C"
  ],
  "I502T": [
    "c.1505T>C",
    "I502T",
    "p.Ile502Thr",
    "1637T>C"
  ],
  "p.Ile502Thr": [
    "c.1505T>C",
    "I502T",
    "p.Ile502Thr",
    "1637T>C"
  ],
  "1637T>C": [
    "c.1505T>C",
    "I502T",
    "p.Ile502Thr",
    "1637T>C"
  ],
  "p.Gly673X": [
    "p.Gly673X",
    "2149G>T",
    "c.2017G>T",
    "G673X"
  ],
  "2149G>T": [
    "p.Gly673X",
    "2149G>T",
    "c.2017G>T",
    "G673X"
  ],
  "c.2017G>T": [
    "p.Gly673X",
    "2149G>T",
    "c.2017G>T",
    "G673X"
  ],
  "G673X": [
    "p.Gly673X",
    "2149G>T",
    "c.2017G>T",
    "G673X"
  ],
  "A613T": [
    "A613T",
    "c.1837G>A",
    "p.Ala613Thr",
    "1969G>A"
  ],
  "c.1837G>A": [
    "A613T",
    "c.1837G>A",
    "p.Ala613Thr",
    "1969G>A"
  ],
  "p.Ala613Thr": [
    "A613T",
    "c.1837G>A",
    "p.Ala613Thr",
    "1969G>A"
  ],
  "1969G>A": [
    "A613T",
    "c.1837G>A",
    "p.Ala613Thr",
    "1969G>A"
  ],
  "3239C>A": [
    "3239C>A",
    "c.3107C>A",
    "T1036N",
    "p.Thr1036Asn"
  ],
  "c.3107C>A": [
    "3239C>A",
    "c.3107C>A",
    "T1036N",
    "p.Thr1036Asn"
  ],
  "T1036N": [
    "3239C>A",
    "c.3107C>A",
    "T1036N",
    "p.Thr1036Asn"
  ],
  "p.Thr1036Asn": [
    "3239C>A",
    "c.3107C>A",
    "T1036N",
    "p.Thr1036Asn"
  ],
  "CFTRdele19-21": [
    "p.?",
    "CFTRdele19-21",
    "deletion of exons 19, 20, and 21 (legacy numbering)|deletion of exons 22, 23, and 24 (current numbering)",
    "c.(3468+1_3469-1)_(3963+1_3964-1)del"
  ],
  "deletion of exons 19, 20, and 21 (legacy numbering)|deletion of exons 22, 23, and 24 (current numbering)": [
    "p.?",
    "CFTRdele19-21",
    "deletion of exons 19, 20, and 21 (legacy numbering)|deletion of exons 22, 23, and 24 (current numbering)",
    "c.(3468+1_3469-1)_(3963+1_3964-1)del"
  ],
  "c.(3468+1_3469-1)_(3963+1_3964-1)del": [
    "p.?",
    "CFTRdele19-21",
    "deletion of exons 19, 20, and 21 (legacy numbering)|deletion of exons 22, 23, and 24 (current numbering)",
    "c.(3468+1_3469-1)_(3963+1_3964-1)del"
  ],
  "c.1393-2A>G": [
    "c.1393-2A>G",
    "p.?",
    "1525-2A->G"
  ],
  "1525-2A->G": [
    "c.1393-2A>G",
    "p.?",
    "1525-2A->G"
  ],
  "875+1G->A": [
    "875+1G->A",
    "p.?",
    "c.743+1G>A"
  ],
  "c.743+1G>A": [
    "875+1G->A",
    "p.?",
    "c.743+1G>A"
  ],
  "c.(273+1_274-1)_(1679+1_1680-1)del": [
    "c.(273+1_274-1)_(1679+1_1680-1)del",
    "p.?",
    "deletion of exons 4 through 11 (legacy numbering)|deletion of exons 4 through 12 (current numbering)",
    "CFTRdele4-11"
  ],
  "deletion of exons 4 through 11 (legacy numbering)|deletion of exons 4 through 12 (current numbering)": [
    "c.(273+1_274-1)_(1679+1_1680-1)del",
    "p.?",
    "deletion of exons 4 through 11 (legacy numbering)|deletion of exons 4 through 12 (current numbering)",
    "CFTRdele4-11"
  ],
  "CFTRdele4-11": [
    "c.(273+1_274-1)_(1679+1_1680-1)del",
    "p.?",
    "deletion of exons 4 through 11 (legacy numbering)|deletion of exons 4 through 12 (current numbering)",
    "CFTRdele4-11"
  ],
  "p.Trp361GlyfsX8": [
    "p.Trp361GlyfsX8",
    "1212delA",
    "c.1080del"
  ],
  "1213delT": [
    "p.Trp361GlyfsX8",
    "1213delT",
    "c.1081del"
  ],
  "c.1081del": [
    "p.Trp361GlyfsX8",
    "1213delT",
    "c.1081del"
  ],
  "c.2T>C": [
    "c.2T>C",
    "M1T",
    "p.?"
  ],
  "M1T": [
    "c.2T>C",
    "M1T",
    "p.?"
  ],
  "c.489+3A>G": [
    "c.489+3A>G",
    "621+3A->G",
    "p.?"
  ],
  "621+3A->G": [
    "c.489+3A>G",
    "621+3A->G",
    "p.?"
  ],
  "c.1853T>C": [
    "c.1853T>C",
    "I618T",
    "p.Ile618Thr",
    "1985T>C"
  ],
  "I618T": [
    "c.1853T>C",
    "I618T",
    "p.Ile618Thr",
    "1985T>C"
  ],
  "p.Ile618Thr": [
    "c.1853T>C",
    "I618T",
    "p.Ile618Thr",
    "1985T>C"
  ],
  "1985T>C": [
    "c.1853T>C",
    "I618T",
    "p.Ile618Thr",
    "1985T>C"
  ],
  "p.Ile807Met": [
    "p.Ile807Met",
    "2553A>G",
    "I807M",
    "c.2421A>G"
  ],
  "2553A>G": [
    "p.Ile807Met",
    "2553A>G",
    "I807M",
    "c.2421A>G"
  ],
  "I807M": [
    "p.Ile807Met",
    "2553A>G",
    "I807M",
    "c.2421A>G"
  ],
  "c.2421A>G": [
    "p.Ile807Met",
    "2553A>G",
    "I807M",
    "c.2421A>G"
  ],
  "c.2547C>A": [
    "c.2547C>A",
    "p.Tyr849X",
    "Y849X",
    "2679C>A"
  ],
  "p.Tyr849X": [
    "c.2547C>A",
    "p.Tyr849X",
    "Y849X",
    "2679C>A"
  ],
  "Y849X": [
    "c.2547C>A",
    "p.Tyr849X",
    "Y849X",
    "2679C>A"
  ],
  "2679C>A": [
    "c.2547C>A",
    "p.Tyr849X",
    "Y849X",
    "2679C>A"
  ],
  "3354T>A|3352T>C|3354T>G": [
    "3354T>A|3352T>C|3354T>G",
    "p.Phe1074Leu",
    "c.3220T>C|c.3222T>G|c.3222T>A",
    "F1074L"
  ],
  "p.Phe1074Leu": [
    "3354T>A|3352T>C|3354T>G",
    "p.Phe1074Leu",
    "c.3220T>C|c.3222T>G|c.3222T>A",
    "F1074L"
  ],
  "c.3220T>C|c.3222T>G|c.3222T>A": [
    "3354T>A|3352T>C|3354T>G",
    "p.Phe1074Leu",
    "c.3220T>C|c.3222T>G|c.3222T>A",
    "F1074L"
  ],
  "F1074L": [
    "3354T>A|3352T>C|3354T>G",
    "p.Phe1074Leu",
    "c.3220T>C|c.3222T>G|c.3222T>A",
    "F1074L"
  ],
  "p.Tyr275X": [
    "p.Tyr275X",
    "957C>G",
    "Y275X",
    "c.825C>G"
  ],
  "957C>G": [
    "p.Tyr275X",
    "957C>G",
    "Y275X",
    "c.825C>G"
  ],
  "Y275X": [
    "p.Tyr275X",
    "957C>G",
    "Y275X",
    "c.825C>G"
  ],
  "c.825C>G": [
    "p.Tyr275X",
    "957C>G",
    "Y275X",
    "c.825C>G"
  ],
  "c.3532_3535dup": [
    "c.3532_3535dup",
    "p.Thr1179IlefsX17",
    "c.3535_3536insTCAA",
    "3667ins4"
  ],
  "p.Thr1179IlefsX17": [
    "c.3532_3535dup",
    "p.Thr1179IlefsX17",
    "c.3535_3536insTCAA",
    "3667ins4"
  ],
  "c.3535_3536insTCAA": [
    "c.3532_3535dup",
    "p.Thr1179IlefsX17",
    "c.3535_3536insTCAA",
    "3667ins4"
  ],
  "3667ins4": [
    "c.3532_3535dup",
    "p.Thr1179IlefsX17",
    "c.3535_3536insTCAA",
    "3667ins4"
  ],
  "p.Ile105SerfsX2": [
    "p.Ile105SerfsX2",
    "444delA",
    "c.313del"
  ],
  "444delA": [
    "p.Ile105SerfsX2",
    "444delA",
    "c.313del"
  ],
  "c.313del": [
    "p.Ile105SerfsX2",
    "444delA",
    "c.313del"
  ],
  "c.2051_2052del": [
    "c.2051_2052del",
    "p.Lys684ThrfsX4",
    "2183delAA"
  ],
  "p.Lys684ThrfsX4": [
    "c.2051_2052del",
    "p.Lys684ThrfsX4",
    "2183delAA"
  ],
  "2183delAA": [
    "c.2051_2052del",
    "p.Lys684ThrfsX4",
    "2183delAA"
  ],
  "c.1135G>T": [
    "c.1135G>T",
    "E379X",
    "p.Glu379X",
    "1267G>T"
  ],
  "E379X": [
    "c.1135G>T",
    "E379X",
    "p.Glu379X",
    "1267G>T"
  ],
  "p.Glu379X": [
    "c.1135G>T",
    "E379X",
    "p.Glu379X",
    "1267G>T"
  ],
  "1267G>T": [
    "c.1135G>T",
    "E379X",
    "p.Glu379X",
    "1267G>T"
  ],
  "1704C>A": [
    "1704C>A",
    "C524X",
    "c.1572C>A",
    "p.Cys524X"
  ],
  "C524X": [
    "1704C>A",
    "C524X",
    "c.1572C>A",
    "p.Cys524X"
  ],
  "c.1572C>A": [
    "1704C>A",
    "C524X",
    "c.1572C>A",
    "p.Cys524X"
  ],
  "p.Cys524X": [
    "1704C>A",
    "C524X",
    "c.1572C>A",
    "p.Cys524X"
  ],
  "1811G>A": [
    "1811G>A",
    "R560K",
    "c.1679G>A",
    "p.Arg560Lys"
  ],
  "R560K": [
    "1811G>A",
    "R560K",
    "c.1679G>A",
    "p.Arg560Lys"
  ],
  "c.1679G>A": [
    "1811G>A",
    "R560K",
    "c.1679G>A",
    "p.Arg560Lys"
  ],
  "p.Arg560Lys": [
    "1811G>A",
    "R560K",
    "c.1679G>A",
    "p.Arg560Lys"
  ],
  "3607T>C": [
    "3607T>C",
    "c.3475T>C",
    "S1159P",
    "p.Ser1159Pro"
  ],
  "c.3475T>C": [
    "3607T>C",
    "c.3475T>C",
    "S1159P",
    "p.Ser1159Pro"
  ],
  "S1159P": [
    "3607T>C",
    "c.3475T>C",
    "S1159P",
    "p.Ser1159Pro"
  ],
  "p.Ser1159Pro": [
    "3607T>C",
    "c.3475T>C",
    "S1159P",
    "p.Ser1159Pro"
  ],
  "p.Arg1162Leu": [
    "p.Arg1162Leu",
    "c.3485G>T",
    "3671G/T|3617G>T",
    "R1162L"
  ],
  "c.3485G>T": [
    "p.Arg1162Leu",
    "c.3485G>T",
    "3671G/T|3617G>T",
    "R1162L"
  ],
  "3671G/T|3617G>T": [
    "p.Arg1162Leu",
    "c.3485G>T",
    "3671G/T|3617G>T",
    "R1162L"
  ],
  "R1162L": [
    "p.Arg1162Leu",
    "c.3485G>T",
    "3671G/T|3617G>T",
    "R1162L"
  ],
  "3938T>A": [
    "3938T>A",
    "p.Ile1269Asn",
    "I1269N",
    "c.3806T>A"
  ],
  "p.Ile1269Asn": [
    "3938T>A",
    "p.Ile1269Asn",
    "I1269N",
    "c.3806T>A"
  ],
  "I1269N": [
    "3938T>A",
    "p.Ile1269Asn",
    "I1269N",
    "c.3806T>A"
  ],
  "c.3806T>A": [
    "3938T>A",
    "p.Ile1269Asn",
    "I1269N",
    "c.3806T>A"
  ],
  "p.Arg170His": [
    "p.Arg170His",
    "R170H",
    "c.509G>A",
    "641G>A"
  ],
  "R170H": [
    "p.Arg170His",
    "R170H",
    "c.509G>A",
    "641G>A"
  ],
  "c.509G>A": [
    "p.Arg170His",
    "R170H",
    "c.509G>A",
    "641G>A"
  ],
  "641G>A": [
    "p.Arg170His",
    "R170H",
    "c.509G>A",
    "641G>A"
  ],
  "c.53+1G>T": [
    "c.53+1G>T",
    "185+1G->T",
    "p.?"
  ],
  "185+1G->T": [
    "c.53+1G>T",
    "185+1G->T",
    "p.?"
  ],
  "c.3874-1G>A": [
    "c.3874-1G>A",
    "p.?",
    "4006-1G->A"
  ],
  "4006-1G->A": [
    "c.3874-1G>A",
    "p.?",
    "4006-1G->A"
  ],
  "c.3747del": [
    "c.3747del",
    "3878delG",
    "p.Lys1250ArgfsX9"
  ],
  "3878delG": [
    "c.3747del",
    "3878delG",
    "p.Lys1250ArgfsX9"
  ],
  "3849+4A->G": [
    "3849+4A->G",
    "p.?",
    "c.3717+4A>G"
  ],
  "c.3717+4A>G": [
    "3849+4A->G",
    "p.?",
    "c.3717+4A>G"
  ],
  "p.Gln525X": [
    "p.Gln525X",
    "1705C>T",
    "Q525X",
    "c.1573C>T"
  ],
  "1705C>T": [
    "p.Gln525X",
    "1705C>T",
    "Q525X",
    "c.1573C>T"
  ],
  "Q525X": [
    "p.Gln525X",
    "1705C>T",
    "Q525X",
    "c.1573C>T"
  ],
  "c.1573C>T": [
    "p.Gln525X",
    "1705C>T",
    "Q525X",
    "c.1573C>T"
  ],
  "4004A>G": [
    "4004A>G",
    "c.3872A>G",
    "Q1291R",
    "p.Gln1291Arg"
  ],
  "c.3872A>G": [
    "4004A>G",
    "c.3872A>G",
    "Q1291R",
    "p.Gln1291Arg"
  ],
  "Q1291R": [
    "4004A>G",
    "c.3872A>G",
    "Q1291R",
    "p.Gln1291Arg"
  ],
  "p.Gln1291Arg": [
    "4004A>G",
    "c.3872A>G",
    "Q1291R",
    "p.Gln1291Arg"
  ],
  "deletion of exons 2, 3, and 4 (legacy and current numbering)|IVSI-5842_IVS4+401del|c.54-5842_489+401del": [
    "deletion of exons 2, 3, and 4 (legacy and current numbering)|IVSI-5842_IVS4+401del|c.54-5842_489+401del",
    "c.(53+1_54-1)_(489+1_490-1)del",
    "CFTRdele2-4",
    "p.?"
  ],
  "c.(53+1_54-1)_(489+1_490-1)del": [
    "deletion of exons 2, 3, and 4 (legacy and current numbering)|IVSI-5842_IVS4+401del|c.54-5842_489+401del",
    "c.(53+1_54-1)_(489+1_490-1)del",
    "CFTRdele2-4",
    "p.?"
  ],
  "CFTRdele2-4": [
    "deletion of exons 2, 3, and 4 (legacy and current numbering)|IVSI-5842_IVS4+401del|c.54-5842_489+401del",
    "c.(53+1_54-1)_(489+1_490-1)del",
    "CFTRdele2-4",
    "p.?"
  ],
  "p.Val1001AspfsX45": [
    "p.Val1001AspfsX45",
    "3132delTG",
    "c.3002_3003del"
  ],
  "3132delTG": [
    "p.Val1001AspfsX45",
    "3132delTG",
    "c.3002_3003del"
  ],
  "c.3002_3003del": [
    "p.Val1001AspfsX45",
    "3132delTG",
    "c.3002_3003del"
  ],
  "1372C>T": [
    "1372C>T",
    "c.1240C>T",
    "p.Gln414X",
    "Q414X"
  ],
  "c.1240C>T": [
    "1372C>T",
    "c.1240C>T",
    "p.Gln414X",
    "Q414X"
  ],
  "p.Gln414X": [
    "1372C>T",
    "c.1240C>T",
    "p.Gln414X",
    "Q414X"
  ],
  "Q414X": [
    "1372C>T",
    "c.1240C>T",
    "p.Gln414X",
    "Q414X"
  ],
  "2014G>C|2014G>A": [
    "2014G>C|2014G>A",
    "G628R",
    "p.Gly628Arg",
    "c.1882G>A|c.1882G>C"
  ],
  "G628R": [
    "2014G>C|2014G>A",
    "G628R",
    "p.Gly628Arg",
    "c.1882G>A|c.1882G>C"
  ],
  "p.Gly628Arg": [
    "2014G>C|2014G>A",
    "G628R",
    "p.Gly628Arg",
    "c.1882G>A|c.1882G>C"
  ],
  "c.1882G>A|c.1882G>C": [
    "2014G>C|2014G>A",
    "G628R",
    "p.Gly628Arg",
    "c.1882G>A|c.1882G>C"
  ],
  "p.Gly970Arg": [
    "p.Gly970Arg",
    "G970R",
    "c.2908G>C",
    "3040G>C"
  ],
  "G970R": [
    "p.Gly970Arg",
    "G970R",
    "c.2908G>C",
    "3040G>C"
  ],
  "c.2908G>C": [
    "p.Gly970Arg",
    "G970R",
    "c.2908G>C",
    "3040G>C"
  ],
  "3040G>C": [
    "p.Gly970Arg",
    "G970R",
    "c.2908G>C",
    "3040G>C"
  ],
  "4010del4": [
    "4010del4",
    "c.3883_3886del",
    "p.Ile1295PhefsX32",
    "4015del4|c.3882_3885delTATT"
  ],
  "c.3883_3886del": [
    "4010del4",
    "c.3883_3886del",
    "p.Ile1295PhefsX32",
    "4015del4|c.3882_3885delTATT"
  ],
  "p.Ile1295PhefsX32": [
    "4010del4",
    "c.3883_3886del",
    "p.Ile1295PhefsX32",
    "4015del4|c.3882_3885delTATT"
  ],
  "4015del4|c.3882_3885delTATT": [
    "4010del4",
    "c.3883_3886del",
    "p.Ile1295PhefsX32",
    "4015del4|c.3882_3885delTATT"
  ],
  "p.Gln1411X": [
    "p.Gln1411X",
    "c.4231C>T",
    "Q1411X",
    "4363C>T"
  ],
  "c.4231C>T": [
    "p.Gln1411X",
    "c.4231C>T",
    "Q1411X",
    "4363C>T"
  ],
  "Q1411X": [
    "p.Gln1411X",
    "c.4231C>T",
    "Q1411X",
    "4363C>T"
  ],
  "4363C>T": [
    "p.Gln1411X",
    "c.4231C>T",
    "Q1411X",
    "4363C>T"
  ],
  "3121-2A->G": [
    "3121-2A->G",
    "p.?",
    "c.2989-2A>G"
  ],
  "c.2989-2A>G": [
    "3121-2A->G",
    "p.?",
    "c.2989-2A>G"
  ],
  "p.Ser1255Pro": [
    "p.Ser1255Pro",
    "3895T>C",
    "S1255P",
    "c.3763T>C"
  ],
  "3895T>C": [
    "p.Ser1255Pro",
    "3895T>C",
    "S1255P",
    "c.3763T>C"
  ],
  "S1255P": [
    "p.Ser1255Pro",
    "3895T>C",
    "S1255P",
    "c.3763T>C"
  ],
  "c.3763T>C": [
    "p.Ser1255Pro",
    "3895T>C",
    "S1255P",
    "c.3763T>C"
  ],
  "R117L": [
    "R117L",
    "482G>T",
    "c.350G>T",
    "p.Arg117Leu"
  ],
  "482G>T": [
    "R117L",
    "482G>T",
    "c.350G>T",
    "p.Arg117Leu"
  ],
  "c.350G>T": [
    "R117L",
    "482G>T",
    "c.350G>T",
    "p.Arg117Leu"
  ],
  "p.Arg117Leu": [
    "R117L",
    "482G>T",
    "c.350G>T",
    "p.Arg117Leu"
  ],
  "365-366insT": [
    "365-366insT",
    "p.Trp79LeufsX32",
    "c.233_234insT|359insT|360-365insT",
    "c.233dup"
  ],
  "p.Trp79LeufsX32": [
    "c.234dup",
    "p.Trp79LeufsX32",
    "366insC"
  ],
  "c.233_234insT|359insT|360-365insT": [
    "365-366insT",
    "p.Trp79LeufsX32",
    "c.233_234insT|359insT|360-365insT",
    "c.233dup"
  ],
  "c.233dup": [
    "365-366insT",
    "p.Trp79LeufsX32",
    "c.233_234insT|359insT|360-365insT",
    "c.233dup"
  ],
  "c.2810dup": [
    "c.2810dup",
    "c.2810_2811insT",
    "2942insT",
    "p.Val938GlyfsX37"
  ],
  "c.2810_2811insT": [
    "c.2810dup",
    "c.2810_2811insT",
    "2942insT",
    "p.Val938GlyfsX37"
  ],
  "2942insT": [
    "c.2810dup",
    "c.2810_2811insT",
    "2942insT",
    "p.Val938GlyfsX37"
  ],
  "p.Val938GlyfsX37": [
    "c.2810dup",
    "c.2810_2811insT",
    "2942insT",
    "p.Val938GlyfsX37"
  ],
  "c.(2908+1_2909-1)_(3367+1_3368-1)del": [
    "c.(2908+1_2909-1)_(3367+1_3368-1)del",
    "deletion of exons 16, 17a, and 17b (legacy numbering)|deletion of exons 18, 19, and 20 (current numbering)",
    "p.?",
    "CFTRdele16-17b"
  ],
  "deletion of exons 16, 17a, and 17b (legacy numbering)|deletion of exons 18, 19, and 20 (current numbering)": [
    "c.(2908+1_2909-1)_(3367+1_3368-1)del",
    "deletion of exons 16, 17a, and 17b (legacy numbering)|deletion of exons 18, 19, and 20 (current numbering)",
    "p.?",
    "CFTRdele16-17b"
  ],
  "CFTRdele16-17b": [
    "c.(2908+1_2909-1)_(3367+1_3368-1)del",
    "deletion of exons 16, 17a, and 17b (legacy numbering)|deletion of exons 18, 19, and 20 (current numbering)",
    "p.?",
    "CFTRdele16-17b"
  ],
  "c.1210-2A>C": [
    "p.?",
    "c.1210-2A>C",
    "1342-2A->C"
  ],
  "1342-2A->C": [
    "p.?",
    "c.1210-2A>C",
    "1342-2A->C"
  ],
  "c.1365_1366del": [
    "c.1365_1366del",
    "1497delGG",
    "p.Val456CysfsX25"
  ],
  "1497delGG": [
    "c.1365_1366del",
    "1497delGG",
    "p.Val456CysfsX25"
  ],
  "p.Val456CysfsX25": [
    "c.1365_1366del",
    "1497delGG",
    "p.Val456CysfsX25"
  ],
  "p.Asp58GlufsX32": [
    "p.Asp58GlufsX32",
    "c.174_177del",
    "306delTAGA"
  ],
  "c.174_177del": [
    "p.Asp58GlufsX32",
    "c.174_177del",
    "306delTAGA"
  ],
  "306delTAGA": [
    "p.Asp58GlufsX32",
    "c.174_177del",
    "306delTAGA"
  ],
  "1898+5G->T": [
    "1898+5G->T",
    "p.?",
    "c.1766+5G>T"
  ],
  "c.1766+5G>T": [
    "1898+5G->T",
    "p.?",
    "c.1766+5G>T"
  ],
  "c.2249C>T": [
    "c.2249C>T",
    "2381C>T",
    "P750L",
    "p.Pro750Leu"
  ],
  "2381C>T": [
    "c.2249C>T",
    "2381C>T",
    "P750L",
    "p.Pro750Leu"
  ],
  "P750L": [
    "c.2249C>T",
    "2381C>T",
    "P750L",
    "p.Pro750Leu"
  ],
  "p.Pro750Leu": [
    "c.2249C>T",
    "2381C>T",
    "P750L",
    "p.Pro750Leu"
  ],
  "W1098R": [
    "W1098R",
    "p.Trp1098Arg",
    "3424T>C",
    "c.3292T>C"
  ],
  "p.Trp1098Arg": [
    "W1098R",
    "p.Trp1098Arg",
    "3424T>C",
    "c.3292T>C"
  ],
  "3424T>C": [
    "W1098R",
    "p.Trp1098Arg",
    "3424T>C",
    "c.3292T>C"
  ],
  "c.3292T>C": [
    "W1098R",
    "p.Trp1098Arg",
    "3424T>C",
    "c.3292T>C"
  ],
  "3850-1G->A": [
    "3850-1G->A",
    "c.3718-1G>A",
    "p.?"
  ],
  "c.3718-1G>A": [
    "3850-1G->A",
    "c.3718-1G>A",
    "p.?"
  ],
  "c.1584+1G>A": [
    "c.1584+1G>A",
    "p.?",
    "1716+1G->A"
  ],
  "1716+1G->A": [
    "c.1584+1G>A",
    "p.?",
    "1716+1G->A"
  ],
  "2721del11": [
    "2721del11",
    "p.Ile864SerfsX28",
    "c.2589_2599del"
  ],
  "p.Ile864SerfsX28": [
    "2721del11",
    "p.Ile864SerfsX28",
    "c.2589_2599del"
  ],
  "c.2589_2599del": [
    "2721del11",
    "p.Ile864SerfsX28",
    "c.2589_2599del"
  ],
  "c.3718-3T>G": [
    "c.3718-3T>G",
    "p.?",
    "3850-3T->G"
  ],
  "3850-3T->G": [
    "c.3718-3T>G",
    "p.?",
    "3850-3T->G"
  ],
  "124del23bp": [
    "p.?",
    "124del23bp",
    "c.-9_14del"
  ],
  "c.-9_14del": [
    "p.?",
    "124del23bp",
    "c.-9_14del"
  ],
  "F311L": [
    "F311L",
    "p.Phe311Leu",
    "1065C>G",
    "c.933C>A|c.933C>G"
  ],
  "p.Phe311Leu": [
    "F311L",
    "p.Phe311Leu",
    "1065C>G",
    "c.933C>A|c.933C>G"
  ],
  "1065C>G": [
    "F311L",
    "p.Phe311Leu",
    "1065C>G",
    "c.933C>A|c.933C>G"
  ],
  "c.933C>A|c.933C>G": [
    "F311L",
    "p.Phe311Leu",
    "1065C>G",
    "c.933C>A|c.933C>G"
  ],
  "1133G>A": [
    "1133G>A",
    "p.Arg334Gln",
    "R334Q",
    "c.1001G>A"
  ],
  "p.Arg334Gln": [
    "1133G>A",
    "p.Arg334Gln",
    "R334Q",
    "c.1001G>A"
  ],
  "R334Q": [
    "1133G>A",
    "p.Arg334Gln",
    "R334Q",
    "c.1001G>A"
  ],
  "c.1001G>A": [
    "1133G>A",
    "p.Arg334Gln",
    "R334Q",
    "c.1001G>A"
  ],
  "D836Y": [
    "D836Y",
    "p.Asp836Tyr",
    "c.2506G>T",
    "2638G>T"
  ],
  "p.Asp836Tyr": [
    "D836Y",
    "p.Asp836Tyr",
    "c.2506G>T",
    "2638G>T"
  ],
  "c.2506G>T": [
    "D836Y",
    "p.Asp836Tyr",
    "c.2506G>T",
    "2638G>T"
  ],
  "2638G>T": [
    "D836Y",
    "p.Asp836Tyr",
    "c.2506G>T",
    "2638G>T"
  ],
  "c.137C>A": [
    "c.137C>A",
    "A46D",
    "269C>A",
    "p.Ala46Asp"
  ],
  "A46D": [
    "c.137C>A",
    "A46D",
    "269C>A",
    "p.Ala46Asp"
  ],
  "269C>A": [
    "c.137C>A",
    "A46D",
    "269C>A",
    "p.Ala46Asp"
  ],
  "p.Ala46Asp": [
    "c.137C>A",
    "A46D",
    "269C>A",
    "p.Ala46Asp"
  ],
  "3173A>G": [
    "3173A>G",
    "p.Tyr1014Cys",
    "c.3041A>G",
    "Y1014C"
  ],
  "p.Tyr1014Cys": [
    "3173A>G",
    "p.Tyr1014Cys",
    "c.3041A>G",
    "Y1014C"
  ],
  "c.3041A>G": [
    "3173A>G",
    "p.Tyr1014Cys",
    "c.3041A>G",
    "Y1014C"
  ],
  "Y1014C": [
    "3173A>G",
    "p.Tyr1014Cys",
    "c.3041A>G",
    "Y1014C"
  ],
  "S1118F": [
    "S1118F",
    "3485C>T",
    "c.3353C>T",
    "p.Ser1118Phe"
  ],
  "3485C>T": [
    "S1118F",
    "3485C>T",
    "c.3353C>T",
    "p.Ser1118Phe"
  ],
  "c.3353C>T": [
    "S1118F",
    "3485C>T",
    "c.3353C>T",
    "p.Ser1118Phe"
  ],
  "p.Ser1118Phe": [
    "S1118F",
    "3485C>T",
    "c.3353C>T",
    "p.Ser1118Phe"
  ],
  "4256A>C": [
    "4256A>C",
    "c.4124A>C",
    "p.His1375Pro",
    "H1375P"
  ],
  "c.4124A>C": [
    "4256A>C",
    "c.4124A>C",
    "p.His1375Pro",
    "H1375P"
  ],
  "p.His1375Pro": [
    "4256A>C",
    "c.4124A>C",
    "p.His1375Pro",
    "H1375P"
  ],
  "H1375P": [
    "4256A>C",
    "c.4124A>C",
    "p.His1375Pro",
    "H1375P"
  ],
  "c.2859_2890del": [
    "c.2859_2890del",
    "p.Leu953PhefsX11",
    "c.2859_2890del32",
    "2991del32"
  ],
  "p.Leu953PhefsX11": [
    "c.2859_2890del",
    "p.Leu953PhefsX11",
    "c.2859_2890del32",
    "2991del32"
  ],
  "c.2859_2890del32": [
    "c.2859_2890del",
    "p.Leu953PhefsX11",
    "c.2859_2890del32",
    "2991del32"
  ],
  "2991del32": [
    "c.2859_2890del",
    "p.Leu953PhefsX11",
    "c.2859_2890del32",
    "2991del32"
  ],
  "W57X": [
    "W57X",
    "W57X(TAG)|W57X(TGA)|302G>A|303G>A",
    "p.Trp57X",
    "c.170G>A|c.171G>A"
  ],
  "W57X(TAG)|W57X(TGA)|302G>A|303G>A": [
    "W57X",
    "W57X(TAG)|W57X(TGA)|302G>A|303G>A",
    "p.Trp57X",
    "c.170G>A|c.171G>A"
  ],
  "p.Trp57X": [
    "W57X",
    "W57X(TAG)|W57X(TGA)|302G>A|303G>A",
    "p.Trp57X",
    "c.170G>A|c.171G>A"
  ],
  "c.170G>A|c.171G>A": [
    "W57X",
    "W57X(TAG)|W57X(TGA)|302G>A|303G>A",
    "p.Trp57X",
    "c.170G>A|c.171G>A"
  ],
  "c.2658-1G>C": [
    "p.?",
    "c.2658-1G>C",
    "2790-1G->C"
  ],
  "2790-1G->C": [
    "p.?",
    "c.2658-1G>C",
    "2790-1G->C"
  ],
  "296+1G->T": [
    "296+1G->T",
    "c.164+1G>T",
    "p.?"
  ],
  "c.164+1G>T": [
    "296+1G->T",
    "c.164+1G>T",
    "p.?"
  ],
  "c.3717+40A>G": [
    "c.3717+40A>G",
    "p.?",
    "3849+40A->G"
  ],
  "3849+40A->G": [
    "c.3717+40A>G",
    "p.?",
    "3849+40A->G"
  ],
  "405+3A->C": [
    "405+3A->C",
    "p.?",
    "c.273+3A>C"
  ],
  "c.273+3A>C": [
    "405+3A->C",
    "p.?",
    "c.273+3A>C"
  ],
  "c.3717+5G>A": [
    "c.3717+5G>A",
    "3849+5G->A",
    "p.?"
  ],
  "3849+5G->A": [
    "c.3717+5G>A",
    "3849+5G->A",
    "p.?"
  ],
  "p.Phe508Cys": [
    "p.Phe508Cys",
    "1655T>G",
    "c.1523T>G",
    "F508C"
  ],
  "1655T>G": [
    "p.Phe508Cys",
    "1655T>G",
    "c.1523T>G",
    "F508C"
  ],
  "c.1523T>G": [
    "p.Phe508Cys",
    "1655T>G",
    "c.1523T>G",
    "F508C"
  ],
  "F508C": [
    "p.Phe508Cys",
    "1655T>G",
    "c.1523T>G",
    "F508C"
  ],
  "G622D": [
    "G622D",
    "p.Gly622Asp",
    "1997G>A",
    "c.1865G>A"
  ],
  "p.Gly622Asp": [
    "G622D",
    "p.Gly622Asp",
    "1997G>A",
    "c.1865G>A"
  ],
  "1997G>A": [
    "G622D",
    "p.Gly622Asp",
    "1997G>A",
    "c.1865G>A"
  ],
  "c.1865G>A": [
    "G622D",
    "p.Gly622Asp",
    "1997G>A",
    "c.1865G>A"
  ],
  "Q1035X": [
    "Q1035X",
    "3235C>T",
    "c.3103C>T",
    "p.Gln1035X"
  ],
  "3235C>T": [
    "Q1035X",
    "3235C>T",
    "c.3103C>T",
    "p.Gln1035X"
  ],
  "c.3103C>T": [
    "Q1035X",
    "3235C>T",
    "c.3103C>T",
    "p.Gln1035X"
  ],
  "p.Gln1035X": [
    "Q1035X",
    "3235C>T",
    "c.3103C>T",
    "p.Gln1035X"
  ],
  "CFTRdele19": [
    "CFTRdele19",
    "c.(3468+1_3469-1)_(3717+1_3718-1)del",
    "p.?",
    "deletion of exon 19 (legacy numbering)|deletion of exon 22 (current numbering)"
  ],
  "c.(3468+1_3469-1)_(3717+1_3718-1)del": [
    "CFTRdele19",
    "c.(3468+1_3469-1)_(3717+1_3718-1)del",
    "p.?",
    "deletion of exon 19 (legacy numbering)|deletion of exon 22 (current numbering)"
  ],
  "deletion of exon 19 (legacy numbering)|deletion of exon 22 (current numbering)": [
    "CFTRdele19",
    "c.(3468+1_3469-1)_(3717+1_3718-1)del",
    "p.?",
    "deletion of exon 19 (legacy numbering)|deletion of exon 22 (current numbering)"
  ],
  "c.4242+1G>A": [
    "c.4242+1G>A",
    "p.?",
    "4374+1G->A"
  ],
  "4374+1G->A": [
    "c.4242+1G>A",
    "p.?",
    "4374+1G->A"
  ],
  "c.1117-1G>A": [
    "c.1117-1G>A",
    "p.?",
    "1249-1G->A"
  ],
  "1249-1G->A": [
    "c.1117-1G>A",
    "p.?",
    "1249-1G->A"
  ],
  "V470M": [
    "V470M",
    "1540G>A",
    "c.1408G>A",
    "p.Val470Met"
  ],
  "1540G>A": [
    "V470M",
    "1540G>A",
    "c.1408G>A",
    "p.Val470Met"
  ],
  "c.1408G>A": [
    "V470M",
    "1540G>A",
    "c.1408G>A",
    "p.Val470Met"
  ],
  "p.Val470Met": [
    "V470M",
    "1540G>A",
    "c.1408G>A",
    "p.Val470Met"
  ],
  "c.79G>T": [
    "c.79G>T",
    "211G>T",
    "p.Gly27X",
    "G27X"
  ],
  "211G>T": [
    "c.79G>T",
    "211G>T",
    "p.Gly27X",
    "G27X"
  ],
  "p.Gly27X": [
    "c.79G>T",
    "211G>T",
    "p.Gly27X",
    "G27X"
  ],
  "G27X": [
    "c.79G>T",
    "211G>T",
    "p.Gly27X",
    "G27X"
  ],
  "p.Met1101Arg": [
    "p.Met1101Arg",
    "M1101R",
    "c.3302T>G",
    "3434T>G"
  ],
  "M1101R": [
    "p.Met1101Arg",
    "M1101R",
    "c.3302T>G",
    "3434T>G"
  ],
  "c.3302T>G": [
    "p.Met1101Arg",
    "M1101R",
    "c.3302T>G",
    "3434T>G"
  ],
  "3434T>G": [
    "p.Met1101Arg",
    "M1101R",
    "c.3302T>G",
    "3434T>G"
  ],
  "R1102X": [
    "R1102X",
    "3436A>T",
    "c.3304A>T",
    "p.Arg1102X"
  ],
  "3436A>T": [
    "R1102X",
    "3436A>T",
    "c.3304A>T",
    "p.Arg1102X"
  ],
  "c.3304A>T": [
    "R1102X",
    "3436A>T",
    "c.3304A>T",
    "p.Arg1102X"
  ],
  "p.Arg1102X": [
    "R1102X",
    "3436A>T",
    "c.3304A>T",
    "p.Arg1102X"
  ],
  "c.601G>A": [
    "c.601G>A",
    "p.Val201Met",
    "733G>A",
    "V201M"
  ],
  "p.Val201Met": [
    "c.601G>A",
    "p.Val201Met",
    "733G>A",
    "V201M"
  ],
  "733G>A": [
    "c.601G>A",
    "p.Val201Met",
    "733G>A",
    "V201M"
  ],
  "V201M": [
    "c.601G>A",
    "p.Val201Met",
    "733G>A",
    "V201M"
  ],
  "4428insGA": [
    "4428insGA",
    "c.4300_4301dup",
    "p.Ser1435GlyfsX14",
    "c.4296_4297insGA"
  ],
  "c.4300_4301dup": [
    "4428insGA",
    "c.4300_4301dup",
    "p.Ser1435GlyfsX14",
    "c.4296_4297insGA"
  ],
  "p.Ser1435GlyfsX14": [
    "4428insGA",
    "c.4300_4301dup",
    "p.Ser1435GlyfsX14",
    "c.4296_4297insGA"
  ],
  "c.4296_4297insGA": [
    "4428insGA",
    "c.4300_4301dup",
    "p.Ser1435GlyfsX14",
    "c.4296_4297insGA"
  ],
  "c.(?_1)_(53+1_54-1)del": [
    "c.(?_1)_(53+1_54-1)del",
    "CFTRdele1",
    "p.?",
    "deletion of exon 1 (legacy and current numbering)|CFTRdelePr-1|deletion of part of the promoter and exon 1 (legacy and current numbering)"
  ],
  "CFTRdele1": [
    "c.(?_1)_(53+1_54-1)del",
    "CFTRdele1",
    "p.?",
    "deletion of exon 1 (legacy and current numbering)|CFTRdelePr-1|deletion of part of the promoter and exon 1 (legacy and current numbering)"
  ],
  "deletion of exon 1 (legacy and current numbering)|CFTRdelePr-1|deletion of part of the promoter and exon 1 (legacy and current numbering)": [
    "c.(?_1)_(53+1_54-1)del",
    "CFTRdele1",
    "p.?",
    "deletion of exon 1 (legacy and current numbering)|CFTRdelePr-1|deletion of part of the promoter and exon 1 (legacy and current numbering)"
  ],
  "deletion of exons 19 and 20 (legacy numbering)|deletion of exons 22 and 23 (current numbering)": [
    "p.?",
    "deletion of exons 19 and 20 (legacy numbering)|deletion of exons 22 and 23 (current numbering)",
    "CFTRdele19,20",
    "c.(3468+1_3469-1)_(3873+1_3874-1)del"
  ],
  "CFTRdele19,20": [
    "p.?",
    "deletion of exons 19 and 20 (legacy numbering)|deletion of exons 22 and 23 (current numbering)",
    "CFTRdele19,20",
    "c.(3468+1_3469-1)_(3873+1_3874-1)del"
  ],
  "c.(3468+1_3469-1)_(3873+1_3874-1)del": [
    "p.?",
    "deletion of exons 19 and 20 (legacy numbering)|deletion of exons 22 and 23 (current numbering)",
    "CFTRdele19,20",
    "c.(3468+1_3469-1)_(3873+1_3874-1)del"
  ],
  "c.743+1G>C": [
    "c.743+1G>C",
    "p.?",
    "875+1G->C"
  ],
  "875+1G->C": [
    "c.743+1G>C",
    "p.?",
    "875+1G->C"
  ],
  "c.1585-2A>G": [
    "c.1585-2A>G",
    "p.?",
    "1717-2A->G"
  ],
  "1717-2A->G": [
    "c.1585-2A>G",
    "p.?",
    "1717-2A->G"
  ],
  "1898+1G->T": [
    "1898+1G->T",
    "p.?",
    "c.1766+1G>T"
  ],
  "c.1766+1G>T": [
    "1898+1G->T",
    "p.?",
    "c.1766+1G>T"
  ],
  "c.429del": [
    "c.429del",
    "557delT",
    "p.Phe143LeufsX10"
  ],
  "557delT": [
    "c.429del",
    "557delT",
    "p.Phe143LeufsX10"
  ],
  "p.Phe143LeufsX10": [
    "c.429del",
    "557delT",
    "p.Phe143LeufsX10"
  ],
  "2176insC": [
    "2176insC",
    "c.2045dup",
    "p.Gln685ThrfsX4"
  ],
  "c.2045dup": [
    "2176insC",
    "c.2045dup",
    "p.Gln685ThrfsX4"
  ],
  "2957delT": [
    "2957delT",
    "c.2825del",
    "p.Ile942ThrfsX26"
  ],
  "c.2825del": [
    "2957delT",
    "c.2825del",
    "p.Ile942ThrfsX26"
  ],
  "p.Ile942ThrfsX26": [
    "2957delT",
    "c.2825del",
    "p.Ile942ThrfsX26"
  ],
  "c.-8G>C": [
    "p.?",
    "c.-8G>C",
    "125G/C"
  ],
  "125G/C": [
    "p.?",
    "c.-8G>C",
    "125G/C"
  ],
  "p.Asp443Tyr": [
    "p.Asp443Tyr",
    "1459G>T",
    "c.1327G>T",
    "D443Y"
  ],
  "1459G>T": [
    "p.Asp443Tyr",
    "1459G>T",
    "c.1327G>T",
    "D443Y"
  ],
  "c.1327G>T": [
    "p.Asp443Tyr",
    "1459G>T",
    "c.1327G>T",
    "D443Y"
  ],
  "D443Y": [
    "p.Asp443Tyr",
    "1459G>T",
    "c.1327G>T",
    "D443Y"
  ],
  "c.1487G>A": [
    "c.1487G>A",
    "1619G>A",
    "p.Trp496X",
    "W496X"
  ],
  "1619G>A": [
    "c.1487G>A",
    "1619G>A",
    "p.Trp496X",
    "W496X"
  ],
  "p.Trp496X": [
    "c.1487G>A",
    "1619G>A",
    "p.Trp496X",
    "W496X"
  ],
  "W496X": [
    "c.1487G>A",
    "1619G>A",
    "p.Trp496X",
    "W496X"
  ],
  "c.1680A>C|c.1680A>T": [
    "c.1680A>C|c.1680A>T",
    "1812A>C",
    "p.Arg560Ser",
    "R560S"
  ],
  "1812A>C": [
    "c.1680A>C|c.1680A>T",
    "1812A>C",
    "p.Arg560Ser",
    "R560S"
  ],
  "p.Arg560Ser": [
    "c.1680A>C|c.1680A>T",
    "1812A>C",
    "p.Arg560Ser",
    "R560S"
  ],
  "R560S": [
    "c.1680A>C|c.1680A>T",
    "1812A>C",
    "p.Arg560Ser",
    "R560S"
  ],
  "c.2855T>C": [
    "c.2855T>C",
    "M952T",
    "p.Met952Thr",
    "2987T>C"
  ],
  "M952T": [
    "c.2855T>C",
    "M952T",
    "p.Met952Thr",
    "2987T>C"
  ],
  "p.Met952Thr": [
    "c.2855T>C",
    "M952T",
    "p.Met952Thr",
    "2987T>C"
  ],
  "2987T>C": [
    "c.2855T>C",
    "M952T",
    "p.Met952Thr",
    "2987T>C"
  ],
  "3141del9": [
    "3141del9",
    "c.3011_3019del",
    "3143del9",
    "p.Ala1004_Ala1006del"
  ],
  "c.3011_3019del": [
    "3141del9",
    "c.3011_3019del",
    "3143del9",
    "p.Ala1004_Ala1006del"
  ],
  "3143del9": [
    "3141del9",
    "c.3011_3019del",
    "3143del9",
    "p.Ala1004_Ala1006del"
  ],
  "p.Ala1004_Ala1006del": [
    "3141del9",
    "c.3011_3019del",
    "3143del9",
    "p.Ala1004_Ala1006del"
  ],
  "p.Thr1053Ile": [
    "p.Thr1053Ile",
    "c.3158C>T",
    "3290C>T",
    "T1053I"
  ],
  "c.3158C>T": [
    "p.Thr1053Ile",
    "c.3158C>T",
    "3290C>T",
    "T1053I"
  ],
  "3290C>T": [
    "p.Thr1053Ile",
    "c.3158C>T",
    "3290C>T",
    "T1053I"
  ],
  "T1053I": [
    "p.Thr1053Ile",
    "c.3158C>T",
    "3290C>T",
    "T1053I"
  ],
  "c.3407_3422del": [
    "c.3407_3422del",
    "p.Ala1136ValfsX7",
    "3407_3422del16",
    "3539del16"
  ],
  "p.Ala1136ValfsX7": [
    "c.3407_3422del",
    "p.Ala1136ValfsX7",
    "3407_3422del16",
    "3539del16"
  ],
  "3407_3422del16": [
    "3407_3422del16"
  ],
  "3539del16": [
    "c.3407_3422del",
    "p.Ala1136ValfsX7",
    "3407_3422del16",
    "3539del16"
  ],
  "W1098X": [
    "W1098X",
    "3425G>A|3426G>A",
    "p.Trp1098X",
    "c.3293G>A|c.3294G>A"
  ],
  "3425G>A|3426G>A": [
    "W1098X",
    "3425G>A|3426G>A",
    "p.Trp1098X",
    "c.3293G>A|c.3294G>A"
  ],
  "p.Trp1098X": [
    "W1098X",
    "3425G>A|3426G>A",
    "p.Trp1098X",
    "c.3293G>A|c.3294G>A"
  ],
  "c.3293G>A|c.3294G>A": [
    "W1098X",
    "3425G>A|3426G>A",
    "p.Trp1098X",
    "c.3293G>A|c.3294G>A"
  ],
  "F1099L": [
    "F1099L",
    "c.3297C>A",
    "p.Phe1099Leu",
    "3429C>A"
  ],
  "c.3297C>A": [
    "F1099L",
    "c.3297C>A",
    "p.Phe1099Leu",
    "3429C>A"
  ],
  "p.Phe1099Leu": [
    "F1099L",
    "c.3297C>A",
    "p.Phe1099Leu",
    "3429C>A"
  ],
  "3429C>A": [
    "F1099L",
    "c.3297C>A",
    "p.Phe1099Leu",
    "3429C>A"
  ],
  "p.Gln1382X": [
    "p.Gln1382X",
    "Q1382X",
    "4276C>T",
    "c.4144C>T"
  ],
  "Q1382X": [
    "p.Gln1382X",
    "Q1382X",
    "4276C>T",
    "c.4144C>T"
  ],
  "4276C>T": [
    "p.Gln1382X",
    "Q1382X",
    "4276C>T",
    "c.4144C>T"
  ],
  "c.4144C>T": [
    "p.Gln1382X",
    "Q1382X",
    "4276C>T",
    "c.4144C>T"
  ],
  "Q1412X": [
    "Q1412X",
    "c.4234C>T",
    "p.Gln1412X",
    "4366C>T"
  ],
  "c.4234C>T": [
    "Q1412X",
    "c.4234C>T",
    "p.Gln1412X",
    "4366C>T"
  ],
  "p.Gln1412X": [
    "Q1412X",
    "c.4234C>T",
    "p.Gln1412X",
    "4366C>T"
  ],
  "4366C>T": [
    "Q1412X",
    "c.4234C>T",
    "p.Gln1412X",
    "4366C>T"
  ],
  "977insA": [
    "977insA",
    "p.Met284AsnfsX3",
    "982dupA",
    "c.850dup"
  ],
  "p.Met284AsnfsX3": [
    "977insA",
    "p.Met284AsnfsX3",
    "982dupA",
    "c.850dup"
  ],
  "982dupA": [
    "977insA",
    "p.Met284AsnfsX3",
    "982dupA",
    "c.850dup"
  ],
  "c.850dup": [
    "977insA",
    "p.Met284AsnfsX3",
    "982dupA",
    "c.850dup"
  ],
  "L88X(T->G)|L88X(T->A)|395T>A|395T>G": [
    "L88X(T->G)|L88X(T->A)|395T>A|395T>G",
    "c.263T>A|c.263T>G",
    "L88X",
    "p.Leu88X"
  ],
  "c.263T>A|c.263T>G": [
    "L88X(T->G)|L88X(T->A)|395T>A|395T>G",
    "c.263T>A|c.263T>G",
    "L88X",
    "p.Leu88X"
  ],
  "L88X": [
    "L88X(T->G)|L88X(T->A)|395T>A|395T>G",
    "c.263T>A|c.263T>G",
    "L88X",
    "p.Leu88X"
  ],
  "p.Leu88X": [
    "L88X(T->G)|L88X(T->A)|395T>A|395T>G",
    "c.263T>A|c.263T>G",
    "L88X",
    "p.Leu88X"
  ],
  "c.1766+2T>C": [
    "c.1766+2T>C",
    "p.?",
    "1898+2T->C"
  ],
  "1898+2T->C": [
    "c.1766+2T>C",
    "p.?",
    "1898+2T->C"
  ],
  "c.168del": [
    "c.168del",
    "p.Glu56AspfsX35",
    "300delA"
  ],
  "p.Glu56AspfsX35": [
    "c.168del",
    "p.Glu56AspfsX35",
    "300delA"
  ],
  "300delA": [
    "c.168del",
    "p.Glu56AspfsX35",
    "300delA"
  ],
  "p.Leu137SerfsX16": [
    "p.Leu137SerfsX16",
    "c.409del",
    "541delC"
  ],
  "c.409del": [
    "p.Leu137SerfsX16",
    "c.409del",
    "541delC"
  ],
  "541delC": [
    "p.Leu137SerfsX16",
    "c.409del",
    "541delC"
  ],
  "622-1G->A": [
    "p.?",
    "622-1G->A",
    "c.490-1G>A"
  ],
  "c.490-1G>A": [
    "p.?",
    "622-1G->A",
    "c.490-1G>A"
  ],
  "1186C>T": [
    "1186C>T",
    "p.Arg352Trp",
    "R352W",
    "c.1054C>T"
  ],
  "p.Arg352Trp": [
    "1186C>T",
    "p.Arg352Trp",
    "R352W",
    "c.1054C>T"
  ],
  "R352W": [
    "1186C>T",
    "p.Arg352Trp",
    "R352W",
    "c.1054C>T"
  ],
  "c.1054C>T": [
    "1186C>T",
    "p.Arg352Trp",
    "R352W",
    "c.1054C>T"
  ],
  "c.1648G>T": [
    "c.1648G>T",
    "p.Gly550X",
    "G550X",
    "1780G>T"
  ],
  "p.Gly550X": [
    "c.1648G>T",
    "p.Gly550X",
    "G550X",
    "1780G>T"
  ],
  "G550X": [
    "c.1648G>T",
    "p.Gly550X",
    "G550X",
    "1780G>T"
  ],
  "1780G>T": [
    "c.1648G>T",
    "p.Gly550X",
    "G550X",
    "1780G>T"
  ],
  "E56K": [
    "E56K",
    "p.Glu56Lys",
    "c.166G>A",
    "298G>A"
  ],
  "p.Glu56Lys": [
    "E56K",
    "p.Glu56Lys",
    "c.166G>A",
    "298G>A"
  ],
  "c.166G>A": [
    "E56K",
    "p.Glu56Lys",
    "c.166G>A",
    "298G>A"
  ],
  "298G>A": [
    "E56K",
    "p.Glu56Lys",
    "c.166G>A",
    "298G>A"
  ],
  "478G>A": [
    "478G>A",
    "c.346G>A",
    "p.Glu116Lys",
    "E116K"
  ],
  "c.346G>A": [
    "478G>A",
    "c.346G>A",
    "p.Glu116Lys",
    "E116K"
  ],
  "p.Glu116Lys": [
    "478G>A",
    "c.346G>A",
    "p.Glu116Lys",
    "E116K"
  ],
  "E116K": [
    "478G>A",
    "c.346G>A",
    "p.Glu116Lys",
    "E116K"
  ],
  "R117G": [
    "R117G",
    "481C>G",
    "p.Arg117Gly",
    "c.349C>G"
  ],
  "481C>G": [
    "R117G",
    "481C>G",
    "p.Arg117Gly",
    "c.349C>G"
  ],
  "p.Arg117Gly": [
    "R117G",
    "481C>G",
    "p.Arg117Gly",
    "c.349C>G"
  ],
  "c.349C>G": [
    "R117G",
    "481C>G",
    "p.Arg117Gly",
    "c.349C>G"
  ],
  "548A>G": [
    "548A>G",
    "p.His139Arg",
    "c.416A>G",
    "H139R"
  ],
  "p.His139Arg": [
    "548A>G",
    "p.His139Arg",
    "c.416A>G",
    "H139R"
  ],
  "c.416A>G": [
    "548A>G",
    "p.His139Arg",
    "c.416A>G",
    "H139R"
  ],
  "H139R": [
    "548A>G",
    "p.His139Arg",
    "c.416A>G",
    "H139R"
  ],
  "E193K": [
    "E193K",
    "709G>A",
    "c.577G>A",
    "p.Glu193Lys"
  ],
  "709G>A": [
    "E193K",
    "709G>A",
    "c.577G>A",
    "p.Glu193Lys"
  ],
  "c.577G>A": [
    "E193K",
    "709G>A",
    "c.577G>A",
    "p.Glu193Lys"
  ],
  "p.Glu193Lys": [
    "E193K",
    "709G>A",
    "c.577G>A",
    "p.Glu193Lys"
  ],
  "c.581G>T": [
    "c.581G>T",
    "G194V",
    "p.Gly194Val",
    "713G>T"
  ],
  "G194V": [
    "c.581G>T",
    "G194V",
    "p.Gly194Val",
    "713G>T"
  ],
  "p.Gly194Val": [
    "c.581G>T",
    "G194V",
    "p.Gly194Val",
    "713G>T"
  ],
  "713G>T": [
    "c.581G>T",
    "G194V",
    "p.Gly194Val",
    "713G>T"
  ],
  "c.2462_2463delGT": [
    "c.2462_2463delGT",
    "p.Ser821ArgfsX4",
    "2594delGT",
    "c.2463_2464del"
  ],
  "p.Ser821ArgfsX4": [
    "c.2462_2463delGT",
    "p.Ser821ArgfsX4",
    "2594delGT",
    "c.2463_2464del"
  ],
  "2594delGT": [
    "c.2462_2463delGT",
    "p.Ser821ArgfsX4",
    "2594delGT",
    "c.2463_2464del"
  ],
  "c.2463_2464del": [
    "c.2462_2463delGT",
    "p.Ser821ArgfsX4",
    "2594delGT",
    "c.2463_2464del"
  ],
  "c.2763_2764dup": [
    "c.2763_2764dup",
    "2896insAG",
    "p.Val922GlufsX2",
    "c.2764_2765insAGA"
  ],
  "2896insAG": [
    "c.2763_2764dup",
    "2896insAG",
    "p.Val922GlufsX2",
    "c.2764_2765insAGA"
  ],
  "p.Val922GlufsX2": [
    "c.2763_2764dup",
    "2896insAG",
    "p.Val922GlufsX2",
    "c.2764_2765insAGA"
  ],
  "c.2764_2765insAGA": [
    "c.2763_2764dup",
    "2896insAG",
    "p.Val922GlufsX2",
    "c.2764_2765insAGA"
  ],
  "c.3890_3891insT": [
    "c.3890_3891insT",
    "c.3891dup",
    "p.Gly1298TrpfsX4",
    "4022insT"
  ],
  "c.3891dup": [
    "c.3890_3891insT",
    "c.3891dup",
    "p.Gly1298TrpfsX4",
    "4022insT"
  ],
  "p.Gly1298TrpfsX4": [
    "c.3890_3891insT",
    "c.3891dup",
    "p.Gly1298TrpfsX4",
    "4022insT"
  ],
  "4022insT": [
    "c.3890_3891insT",
    "c.3891dup",
    "p.Gly1298TrpfsX4",
    "4022insT"
  ],
  "175insT": [
    "175insT",
    "c.50dup",
    "p.Ser18GlnfsX27"
  ],
  "c.50dup": [
    "175insT",
    "c.50dup",
    "p.Ser18GlnfsX27"
  ],
  "p.Ser18GlnfsX27": [
    "175insT",
    "c.50dup",
    "p.Ser18GlnfsX27"
  ],
  "663insT": [
    "663insT",
    "c.531dup",
    "p.Gly178TrpfsX5"
  ],
  "c.531dup": [
    "663insT",
    "c.531dup",
    "p.Gly178TrpfsX5"
  ],
  "p.Gly178TrpfsX5": [
    "663insT",
    "c.531dup",
    "p.Gly178TrpfsX5"
  ],
  "c.2620-26A>G": [
    "p.?",
    "c.2620-26A>G",
    "2752-26A->G"
  ],
  "2752-26A->G": [
    "p.?",
    "c.2620-26A>G",
    "2752-26A->G"
  ],
  "1189C>T": [
    "1189C>T",
    "c.1057C>T",
    "Q353X",
    "p.Gln353X"
  ],
  "c.1057C>T": [
    "1189C>T",
    "c.1057C>T",
    "Q353X",
    "p.Gln353X"
  ],
  "Q353X": [
    "1189C>T",
    "c.1057C>T",
    "Q353X",
    "p.Gln353X"
  ],
  "p.Gln353X": [
    "1189C>T",
    "c.1057C>T",
    "Q353X",
    "p.Gln353X"
  ],
  "p.Gly404AspfsX38": [
    "p.Gly404AspfsX38",
    "1343delG",
    "c.1211del",
    "1342delG|c.1210delG"
  ],
  "1343delG": [
    "p.Gly404AspfsX38",
    "1343delG",
    "c.1211del",
    "1342delG|c.1210delG"
  ],
  "c.1211del": [
    "p.Gly404AspfsX38",
    "1343delG",
    "c.1211del",
    "1342delG|c.1210delG"
  ],
  "1342delG|c.1210delG": [
    "p.Gly404AspfsX38",
    "1343delG",
    "c.1211del",
    "1342delG|c.1210delG"
  ],
  "D513G": [
    "D513G",
    "p.Asp513Gly",
    "c.1538A>G",
    "1670A>G"
  ],
  "p.Asp513Gly": [
    "D513G",
    "p.Asp513Gly",
    "c.1538A>G",
    "1670A>G"
  ],
  "c.1538A>G": [
    "D513G",
    "p.Asp513Gly",
    "c.1538A>G",
    "1670A>G"
  ],
  "1670A>G": [
    "D513G",
    "p.Asp513Gly",
    "c.1538A>G",
    "1670A>G"
  ],
  "170C>T": [
    "170C>T",
    "S13F",
    "p.Ser13Phe",
    "c.38C>T"
  ],
  "S13F": [
    "170C>T",
    "S13F",
    "p.Ser13Phe",
    "c.38C>T"
  ],
  "p.Ser13Phe": [
    "170C>T",
    "S13F",
    "p.Ser13Phe",
    "c.38C>T"
  ],
  "c.38C>T": [
    "170C>T",
    "S13F",
    "p.Ser13Phe",
    "c.38C>T"
  ],
  "2733insA|c.2600_2601insA": [
    "2733insA|c.2600_2601insA",
    "c.2601dup",
    "2732insA",
    "p.Val868SerfsX28"
  ],
  "c.2601dup": [
    "2733insA|c.2600_2601insA",
    "c.2601dup",
    "2732insA",
    "p.Val868SerfsX28"
  ],
  "2732insA": [
    "2733insA|c.2600_2601insA",
    "c.2601dup",
    "2732insA",
    "p.Val868SerfsX28"
  ],
  "p.Val868SerfsX28": [
    "2733insA|c.2600_2601insA",
    "c.2601dup",
    "2732insA",
    "p.Val868SerfsX28"
  ],
  "c.3745G>A|c.3745G>C": [
    "c.3745G>A|c.3745G>C",
    "G1249R",
    "p.Gly1249Arg",
    "3877G>A"
  ],
  "G1249R": [
    "c.3745G>A|c.3745G>C",
    "G1249R",
    "p.Gly1249Arg",
    "3877G>A"
  ],
  "p.Gly1249Arg": [
    "c.3745G>A|c.3745G>C",
    "G1249R",
    "p.Gly1249Arg",
    "3877G>A"
  ],
  "3877G>A": [
    "c.3745G>A|c.3745G>C",
    "G1249R",
    "p.Gly1249Arg",
    "3877G>A"
  ],
  "Q1330X": [
    "Q1330X",
    "4120C>T",
    "p.Gln1330X",
    "c.3988C>T"
  ],
  "4120C>T": [
    "Q1330X",
    "4120C>T",
    "p.Gln1330X",
    "c.3988C>T"
  ],
  "p.Gln1330X": [
    "Q1330X",
    "4120C>T",
    "p.Gln1330X",
    "c.3988C>T"
  ],
  "c.3988C>T": [
    "Q1330X",
    "4120C>T",
    "p.Gln1330X",
    "c.3988C>T"
  ],
  "I1366N": [
    "I1366N",
    "4229T>A",
    "c.4097T>A",
    "p.Ile1366Asn"
  ],
  "4229T>A": [
    "I1366N",
    "4229T>A",
    "c.4097T>A",
    "p.Ile1366Asn"
  ],
  "c.4097T>A": [
    "I1366N",
    "4229T>A",
    "c.4097T>A",
    "p.Ile1366Asn"
  ],
  "p.Ile1366Asn": [
    "I1366N",
    "4229T>A",
    "c.4097T>A",
    "p.Ile1366Asn"
  ],
  "c.571T>G": [
    "c.571T>G",
    "F191V",
    "p.Phe191Val",
    "703T>G"
  ],
  "F191V": [
    "c.571T>G",
    "F191V",
    "p.Phe191Val",
    "703T>G"
  ],
  "p.Phe191Val": [
    "c.571T>G",
    "F191V",
    "p.Phe191Val",
    "703T>G"
  ],
  "703T>G": [
    "c.571T>G",
    "F191V",
    "p.Phe191Val",
    "703T>G"
  ],
  "D192G": [
    "D192G",
    "p.Asp192Gly",
    "707A>G",
    "c.575A>G"
  ],
  "p.Asp192Gly": [
    "D192G",
    "p.Asp192Gly",
    "707A>G",
    "c.575A>G"
  ],
  "707A>G": [
    "D192G",
    "p.Asp192Gly",
    "707A>G",
    "c.575A>G"
  ],
  "c.575A>G": [
    "D192G",
    "p.Asp192Gly",
    "707A>G",
    "c.575A>G"
  ],
  "p.Gln685ProfsX4": [
    "p.Gln685ProfsX4",
    "c.2053_2054insC",
    "2185insC",
    "c.2053dup"
  ],
  "c.2053_2054insC": [
    "p.Gln685ProfsX4",
    "c.2053_2054insC",
    "2185insC",
    "c.2053dup"
  ],
  "2185insC": [
    "p.Gln685ProfsX4",
    "c.2053_2054insC",
    "2185insC",
    "c.2053dup"
  ],
  "c.2053dup": [
    "p.Gln685ProfsX4",
    "c.2053_2054insC",
    "2185insC",
    "c.2053dup"
  ],
  "c.3039_3040insC": [
    "c.3039_3040insC",
    "c.3039dup",
    "3171insC",
    "p.Tyr1014LeufsX33"
  ],
  "c.3039dup": [
    "c.3039_3040insC",
    "c.3039dup",
    "3171insC",
    "p.Tyr1014LeufsX33"
  ],
  "3171insC": [
    "c.3039_3040insC",
    "c.3039dup",
    "3171insC",
    "p.Tyr1014LeufsX33"
  ],
  "p.Tyr1014LeufsX33": [
    "c.3039_3040insC",
    "c.3039dup",
    "3171insC",
    "p.Tyr1014LeufsX33"
  ],
  "CFTRdele11": [
    "CFTRdele11",
    "deletion of exon 11 (legacy numbering)|deletion of exon 12 (current numbering)",
    "p.?",
    "c.(1584+1_1585-1)_(1679+1_1680-1)del"
  ],
  "deletion of exon 11 (legacy numbering)|deletion of exon 12 (current numbering)": [
    "CFTRdele11",
    "deletion of exon 11 (legacy numbering)|deletion of exon 12 (current numbering)",
    "p.?",
    "c.(1584+1_1585-1)_(1679+1_1680-1)del"
  ],
  "c.(1584+1_1585-1)_(1679+1_1680-1)del": [
    "CFTRdele11",
    "deletion of exon 11 (legacy numbering)|deletion of exon 12 (current numbering)",
    "p.?",
    "c.(1584+1_1585-1)_(1679+1_1680-1)del"
  ],
  "deletion of exon 9 (legacy numbering)|deletion of exon 10 (current numbering)": [
    "deletion of exon 9 (legacy numbering)|deletion of exon 10 (current numbering)",
    "p.?",
    "CFTRdele9",
    "c.(1209+1_1210-1)_(1392+1_1393-1)del"
  ],
  "CFTRdele9": [
    "deletion of exon 9 (legacy numbering)|deletion of exon 10 (current numbering)",
    "p.?",
    "CFTRdele9",
    "c.(1209+1_1210-1)_(1392+1_1393-1)del"
  ],
  "c.(1209+1_1210-1)_(1392+1_1393-1)del": [
    "deletion of exon 9 (legacy numbering)|deletion of exon 10 (current numbering)",
    "p.?",
    "CFTRdele9",
    "c.(1209+1_1210-1)_(1392+1_1393-1)del"
  ],
  "c.(273+1_274-1)_(1116+1_1117-1)del": [
    "c.(273+1_274-1)_(1116+1_1117-1)del",
    "p.?",
    "CFTRdele4-7",
    "deletion of exons 4, 5, 6a, 6b, and 7 (legacy numbering)|deletion of exons 4, 5, 6, 7, and 8 (current numbering)"
  ],
  "CFTRdele4-7": [
    "c.(273+1_274-1)_(1116+1_1117-1)del",
    "p.?",
    "CFTRdele4-7",
    "deletion of exons 4, 5, 6a, 6b, and 7 (legacy numbering)|deletion of exons 4, 5, 6, 7, and 8 (current numbering)"
  ],
  "deletion of exons 4, 5, 6a, 6b, and 7 (legacy numbering)|deletion of exons 4, 5, 6, 7, and 8 (current numbering)": [
    "c.(273+1_274-1)_(1116+1_1117-1)del",
    "p.?",
    "CFTRdele4-7",
    "deletion of exons 4, 5, 6a, 6b, and 7 (legacy numbering)|deletion of exons 4, 5, 6, 7, and 8 (current numbering)"
  ],
  "c.(3963+1_3964-1)_(4136+1_4137-1)dup": [
    "p.?",
    "c.(3963+1_3964-1)_(4136+1_4137-1)dup",
    "duplication of exon 22 (legacy numbering)|duplication of exon 25 (current numbering)",
    "CFTRdup22"
  ],
  "duplication of exon 22 (legacy numbering)|duplication of exon 25 (current numbering)": [
    "p.?",
    "c.(3963+1_3964-1)_(4136+1_4137-1)dup",
    "duplication of exon 22 (legacy numbering)|duplication of exon 25 (current numbering)",
    "CFTRdup22"
  ],
  "CFTRdup22": [
    "p.?",
    "c.(3963+1_3964-1)_(4136+1_4137-1)dup",
    "duplication of exon 22 (legacy numbering)|duplication of exon 25 (current numbering)",
    "CFTRdup22"
  ],
  "c.1679+1G>A": [
    "c.1679+1G>A",
    "p.?",
    "1811+1G->A"
  ],
  "1811+1G->A": [
    "c.1679+1G>A",
    "p.?",
    "1811+1G->A"
  ],
  "c.165-1G>A": [
    "c.165-1G>A",
    "297-1G->A",
    "p.?"
  ],
  "297-1G->A": [
    "c.165-1G>A",
    "297-1G->A",
    "p.?"
  ],
  "2954delT": [
    "2954delT",
    "c.2822del",
    "p.Leu941GlnfsX27"
  ],
  "c.2822del": [
    "2954delT",
    "c.2822del",
    "p.Leu941GlnfsX27"
  ],
  "p.Leu941GlnfsX27": [
    "2954delT",
    "c.2822del",
    "p.Leu941GlnfsX27"
  ],
  "541del4": [
    "541del4",
    "c.409_412del",
    "p.Leu137TyrfsX15"
  ],
  "c.409_412del": [
    "541del4",
    "c.409_412del",
    "p.Leu137TyrfsX15"
  ],
  "p.Leu137TyrfsX15": [
    "541del4",
    "c.409_412del",
    "p.Leu137TyrfsX15"
  ],
  "c.2896del": [
    "c.2896del",
    "3028delA",
    "p.Thr966ArgfsX2"
  ],
  "3028delA": [
    "c.2896del",
    "3028delA",
    "p.Thr966ArgfsX2"
  ],
  "p.Thr966ArgfsX2": [
    "c.2896del",
    "3028delA",
    "p.Thr966ArgfsX2"
  ],
  "c.1703del": [
    "c.1703del",
    "1833delT",
    "p.Leu568CysfsX4"
  ],
  "1833delT": [
    "c.1703del",
    "1833delT",
    "p.Leu568CysfsX4"
  ],
  "p.Leu568CysfsX4": [
    "c.1703del",
    "1833delT",
    "p.Leu568CysfsX4"
  ],
  "c.3229_3230del": [
    "c.3229_3230del",
    "3359delCT",
    "p.Leu1077ValfsX78"
  ],
  "3359delCT": [
    "c.3229_3230del",
    "3359delCT",
    "p.Leu1077ValfsX78"
  ],
  "p.Leu1077ValfsX78": [
    "c.3229_3230del",
    "3359delCT",
    "p.Leu1077ValfsX78"
  ],
  "1002-2A->G": [
    "p.?",
    "1002-2A->G",
    "c.870-2A>G"
  ],
  "c.870-2A>G": [
    "p.?",
    "1002-2A->G",
    "c.870-2A>G"
  ],
  "9T": [
    "p.?",
    "9T",
    "c.1210-7_1210-6dup"
  ],
  "c.1210-7_1210-6dup": [
    "p.?",
    "9T",
    "c.1210-7_1210-6dup"
  ],
  "c.941G>A": [
    "c.941G>A",
    "p.Gly314Glu",
    "G314E",
    "1073G>A"
  ],
  "p.Gly314Glu": [
    "c.941G>A",
    "p.Gly314Glu",
    "G314E",
    "1073G>A"
  ],
  "G314E": [
    "c.941G>A",
    "p.Gly314Glu",
    "G314E",
    "1073G>A"
  ],
  "1073G>A": [
    "c.941G>A",
    "p.Gly314Glu",
    "G314E",
    "1073G>A"
  ],
  "L320V": [
    "L320V",
    "c.958T>G",
    "1090T>G",
    "p.Leu320Val"
  ],
  "c.958T>G": [
    "L320V",
    "c.958T>G",
    "1090T>G",
    "p.Leu320Val"
  ],
  "1090T>G": [
    "L320V",
    "c.958T>G",
    "1090T>G",
    "p.Leu320Val"
  ],
  "p.Leu320Val": [
    "L320V",
    "c.958T>G",
    "1090T>G",
    "p.Leu320Val"
  ],
  "p.Gln359Arg": [
    "p.Gln359Arg",
    "Q359R",
    "1208A>G",
    "c.1076A>G"
  ],
  "Q359R": [
    "p.Gln359Arg",
    "Q359R",
    "1208A>G",
    "c.1076A>G"
  ],
  "1208A>G": [
    "p.Gln359Arg",
    "Q359R",
    "1208A>G",
    "c.1076A>G"
  ],
  "c.1076A>G": [
    "p.Gln359Arg",
    "Q359R",
    "1208A>G",
    "c.1076A>G"
  ],
  "c.1546A>G": [
    "c.1546A>G",
    "p.Arg516Gly",
    "R516G",
    "1678A>G"
  ],
  "p.Arg516Gly": [
    "c.1546A>G",
    "p.Arg516Gly",
    "R516G",
    "1678A>G"
  ],
  "R516G": [
    "c.1546A>G",
    "p.Arg516Gly",
    "R516G",
    "1678A>G"
  ],
  "1678A>G": [
    "c.1546A>G",
    "p.Arg516Gly",
    "R516G",
    "1678A>G"
  ],
  "p.Gly646X": [
    "p.Gly646X",
    "G646X",
    "2068G>T",
    "c.1936G>T"
  ],
  "G646X": [
    "p.Gly646X",
    "G646X",
    "2068G>T",
    "c.1936G>T"
  ],
  "2068G>T": [
    "p.Gly646X",
    "G646X",
    "2068G>T",
    "c.1936G>T"
  ],
  "c.1936G>T": [
    "p.Gly646X",
    "G646X",
    "2068G>T",
    "c.1936G>T"
  ],
  "R933G": [
    "R933G",
    "2929A>G",
    "p.Arg933Gly",
    "c.2797A>G"
  ],
  "2929A>G": [
    "R933G",
    "2929A>G",
    "p.Arg933Gly",
    "c.2797A>G"
  ],
  "p.Arg933Gly": [
    "R933G",
    "2929A>G",
    "p.Arg933Gly",
    "c.2797A>G"
  ],
  "c.2797A>G": [
    "R933G",
    "2929A>G",
    "p.Arg933Gly",
    "c.2797A>G"
  ],
  "3256C>T": [
    "3256C>T",
    "Q1042X",
    "c.3124C>T",
    "p.Gln1042X"
  ],
  "Q1042X": [
    "3256C>T",
    "Q1042X",
    "c.3124C>T",
    "p.Gln1042X"
  ],
  "c.3124C>T": [
    "3256C>T",
    "Q1042X",
    "c.3124C>T",
    "p.Gln1042X"
  ],
  "p.Gln1042X": [
    "3256C>T",
    "Q1042X",
    "c.3124C>T",
    "p.Gln1042X"
  ],
  "c.310del": [
    "c.310del",
    "p.Arg104GlufsX3",
    "442delA",
    "441delA"
  ],
  "p.Arg104GlufsX3": [
    "c.310del",
    "p.Arg104GlufsX3",
    "442delA",
    "441delA"
  ],
  "442delA": [
    "c.310del",
    "p.Arg104GlufsX3",
    "442delA",
    "441delA"
  ],
  "441delA": [
    "c.310del",
    "p.Arg104GlufsX3",
    "442delA",
    "441delA"
  ],
  "p.Arg258Gly": [
    "p.Arg258Gly",
    "c.772A>G",
    "R258G",
    "904A>G"
  ],
  "c.772A>G": [
    "p.Arg258Gly",
    "c.772A>G",
    "R258G",
    "904A>G"
  ],
  "R258G": [
    "p.Arg258Gly",
    "c.772A>G",
    "R258G",
    "904A>G"
  ],
  "904A>G": [
    "p.Arg258Gly",
    "c.772A>G",
    "R258G",
    "904A>G"
  ],
  "c.4086dup": [
    "c.4086dup",
    "p.Lys1363X",
    "c.4086_4087insT",
    "4218insT"
  ],
  "p.Lys1363X": [
    "c.4086dup",
    "p.Lys1363X",
    "c.4086_4087insT",
    "4218insT"
  ],
  "c.4086_4087insT": [
    "c.4086dup",
    "p.Lys1363X",
    "c.4086_4087insT",
    "4218insT"
  ],
  "4218insT": [
    "c.4086dup",
    "p.Lys1363X",
    "c.4086_4087insT",
    "4218insT"
  ],
  "c.[(164+1_165-1)_(1584+1_1585-1)del;(2619+1_2620-1)_(2988+1_2989-1)del]": [
    "c.[(164+1_165-1)_(1584+1_1585-1)del;(2619+1_2620-1)_(2988+1_2989-1)del]",
    "CFTRdele3-10,14b-16",
    "p.?",
    "complex deletion of exons 3 through 10 and 14b through 16 (legacy numbering)|complex deletion of exons 3 through 11 and 16 through 18 (current numbering)"
  ],
  "CFTRdele3-10,14b-16": [
    "c.[(164+1_165-1)_(1584+1_1585-1)del;(2619+1_2620-1)_(2988+1_2989-1)del]",
    "CFTRdele3-10,14b-16",
    "p.?",
    "complex deletion of exons 3 through 10 and 14b through 16 (legacy numbering)|complex deletion of exons 3 through 11 and 16 through 18 (current numbering)"
  ],
  "complex deletion of exons 3 through 10 and 14b through 16 (legacy numbering)|complex deletion of exons 3 through 11 and 16 through 18 (current numbering)": [
    "c.[(164+1_165-1)_(1584+1_1585-1)del;(2619+1_2620-1)_(2988+1_2989-1)del]",
    "CFTRdele3-10,14b-16",
    "p.?",
    "complex deletion of exons 3 through 10 and 14b through 16 (legacy numbering)|complex deletion of exons 3 through 11 and 16 through 18 (current numbering)"
  ],
  "CFTR50kbdel": [
    "CFTR50kbdel",
    "complex deletion of exons 4 through 7 and 11 through 18 (legacy numbering)|complex deletion of exons 4 through 8 and 12 through 21 (current numbering)",
    "p.?",
    "c.[(273+1_274-1)_(1116+1_1117-1)del;(1584+1_1585-1)_(3468+1_3469-1)del]"
  ],
  "complex deletion of exons 4 through 7 and 11 through 18 (legacy numbering)|complex deletion of exons 4 through 8 and 12 through 21 (current numbering)": [
    "CFTR50kbdel",
    "complex deletion of exons 4 through 7 and 11 through 18 (legacy numbering)|complex deletion of exons 4 through 8 and 12 through 21 (current numbering)",
    "p.?",
    "c.[(273+1_274-1)_(1116+1_1117-1)del;(1584+1_1585-1)_(3468+1_3469-1)del]"
  ],
  "c.[(273+1_274-1)_(1116+1_1117-1)del;(1584+1_1585-1)_(3468+1_3469-1)del]": [
    "CFTR50kbdel",
    "complex deletion of exons 4 through 7 and 11 through 18 (legacy numbering)|complex deletion of exons 4 through 8 and 12 through 21 (current numbering)",
    "p.?",
    "c.[(273+1_274-1)_(1116+1_1117-1)del;(1584+1_1585-1)_(3468+1_3469-1)del]"
  ],
  "deletion of exon 18 (legacy numbering)|deletion of exon 21 (current numbering)": [
    "deletion of exon 18 (legacy numbering)|deletion of exon 21 (current numbering)",
    "CFTRdele18",
    "c.(3367+1_3368-1)_(3468+1_3469-1)del",
    "p.?"
  ],
  "CFTRdele18": [
    "deletion of exon 18 (legacy numbering)|deletion of exon 21 (current numbering)",
    "CFTRdele18",
    "c.(3367+1_3368-1)_(3468+1_3469-1)del",
    "p.?"
  ],
  "c.(3367+1_3368-1)_(3468+1_3469-1)del": [
    "deletion of exon 18 (legacy numbering)|deletion of exon 21 (current numbering)",
    "CFTRdele18",
    "c.(3367+1_3368-1)_(3468+1_3469-1)del",
    "p.?"
  ],
  "c.(3139+1_3140-1)_(3468+1_3469-1)del": [
    "c.(3139+1_3140-1)_(3468+1_3469-1)del",
    "p.?",
    "deletion of exons 17b and 18 (legacy numbering)|deletion of exons 20 and 21 (current numbering)",
    "CFTRdele17b,18"
  ],
  "deletion of exons 17b and 18 (legacy numbering)|deletion of exons 20 and 21 (current numbering)": [
    "c.(3139+1_3140-1)_(3468+1_3469-1)del",
    "p.?",
    "deletion of exons 17b and 18 (legacy numbering)|deletion of exons 20 and 21 (current numbering)",
    "CFTRdele17b,18"
  ],
  "CFTRdele17b,18": [
    "c.(3139+1_3140-1)_(3468+1_3469-1)del",
    "p.?",
    "deletion of exons 17b and 18 (legacy numbering)|deletion of exons 20 and 21 (current numbering)",
    "CFTRdele17b,18"
  ],
  "296+1G->A": [
    "296+1G->A",
    "p.?",
    "c.164+1G>A"
  ],
  "c.164+1G>A": [
    "296+1G->A",
    "p.?",
    "c.164+1G>A"
  ],
  "c.3469-2A>G": [
    "c.3469-2A>G",
    "3601-2A->G",
    "p.?"
  ],
  "3601-2A->G": [
    "c.3469-2A>G",
    "3601-2A->G",
    "p.?"
  ],
  "1524+1G->A": [
    "1524+1G->A",
    "c.1392+1G>A",
    "p.?"
  ],
  "c.1392+1G>A": [
    "1524+1G->A",
    "c.1392+1G>A",
    "p.?"
  ],
  "3171delC": [
    "3171delC",
    "p.Tyr1014ThrfsX9",
    "c.3039del"
  ],
  "p.Tyr1014ThrfsX9": [
    "3171delC",
    "p.Tyr1014ThrfsX9",
    "c.3039del"
  ],
  "c.3039del": [
    "3171delC",
    "p.Tyr1014ThrfsX9",
    "c.3039del"
  ],
  "c.1792_1798del": [
    "c.1792_1798del",
    "1924del7",
    "p.Lys598GlyfsX11"
  ],
  "1924del7": [
    "c.1792_1798del",
    "1924del7",
    "p.Lys598GlyfsX11"
  ],
  "p.Lys598GlyfsX11": [
    "c.1792_1798del",
    "1924del7",
    "p.Lys598GlyfsX11"
  ],
  "c.2997_3000del": [
    "c.2997_3000del",
    "p.Ile1000X",
    "3129del4"
  ],
  "p.Ile1000X": [
    "c.2997_3000del",
    "p.Ile1000X",
    "3129del4"
  ],
  "3129del4": [
    "c.2997_3000del",
    "p.Ile1000X",
    "3129del4"
  ],
  "3849+1G->A": [
    "3849+1G->A",
    "c.3717+1G>A",
    "p.?"
  ],
  "c.3717+1G>A": [
    "3849+1G->A",
    "c.3717+1G>A",
    "p.?"
  ],
  "175delC": [
    "175delC",
    "p.Leu15PhefsX10",
    "c.43del"
  ],
  "p.Leu15PhefsX10": [
    "175delC",
    "p.Leu15PhefsX10",
    "c.43del"
  ],
  "c.43del": [
    "175delC",
    "p.Leu15PhefsX10",
    "c.43del"
  ],
  "p.Lys163ArgfsX3": [
    "p.Lys163ArgfsX3",
    "c.488delA",
    "c.488del"
  ],
  "c.488delA": [
    "p.Lys163ArgfsX3",
    "c.488delA",
    "c.488del"
  ],
  "c.488del": [
    "p.Lys163ArgfsX3",
    "c.488delA",
    "c.488del"
  ],
  "c.164+28A>G": [
    "c.164+28A>G",
    "296+28A->G",
    "p.?"
  ],
  "296+28A->G": [
    "c.164+28A>G",
    "296+28A->G",
    "p.?"
  ],
  "p.Leu346Pro": [
    "p.Leu346Pro",
    "L346P",
    "1169T>G",
    "c.1037T>C"
  ],
  "L346P": [
    "p.Leu346Pro",
    "L346P",
    "1169T>G",
    "c.1037T>C"
  ],
  "1169T>G": [
    "p.Leu346Pro",
    "L346P",
    "1169T>G",
    "c.1037T>C"
  ],
  "c.1037T>C": [
    "p.Leu346Pro",
    "L346P",
    "1169T>G",
    "c.1037T>C"
  ],
  "A349V": [
    "A349V",
    "c.1046C>T",
    "1178C>T",
    "p.Ala349Val"
  ],
  "c.1046C>T": [
    "A349V",
    "c.1046C>T",
    "1178C>T",
    "p.Ala349Val"
  ],
  "1178C>T": [
    "A349V",
    "c.1046C>T",
    "1178C>T",
    "p.Ala349Val"
  ],
  "p.Ala349Val": [
    "A349V",
    "c.1046C>T",
    "1178C>T",
    "p.Ala349Val"
  ],
  "136C>T": [
    "136C>T",
    "p.Gln2X",
    "Q2X",
    "c.4C>T"
  ],
  "p.Gln2X": [
    "136C>T",
    "p.Gln2X",
    "Q2X",
    "c.4C>T"
  ],
  "Q2X": [
    "136C>T",
    "p.Gln2X",
    "Q2X",
    "c.4C>T"
  ],
  "c.4C>T": [
    "136C>T",
    "p.Gln2X",
    "Q2X",
    "c.4C>T"
  ],
  "1856T>A": [
    "1856T>A",
    "c.1724T>A",
    "p.Phe575Tyr",
    "F575Y"
  ],
  "c.1724T>A": [
    "1856T>A",
    "c.1724T>A",
    "p.Phe575Tyr",
    "F575Y"
  ],
  "p.Phe575Tyr": [
    "1856T>A",
    "c.1724T>A",
    "p.Phe575Tyr",
    "F575Y"
  ],
  "F575Y": [
    "1856T>A",
    "c.1724T>A",
    "p.Phe575Tyr",
    "F575Y"
  ],
  "c.1763A>T": [
    "c.1763A>T",
    "E588V",
    "p.Glu588Val",
    "1895A>T"
  ],
  "E588V": [
    "c.1763A>T",
    "E588V",
    "p.Glu588Val",
    "1895A>T"
  ],
  "p.Glu588Val": [
    "c.1763A>T",
    "E588V",
    "p.Glu588Val",
    "1895A>T"
  ],
  "1895A>T": [
    "c.1763A>T",
    "E588V",
    "p.Glu588Val",
    "1895A>T"
  ],
  "c.2735C>T": [
    "c.2735C>T",
    "S912L",
    "p.Ser912Leu",
    "2867C>T"
  ],
  "S912L": [
    "c.2735C>T",
    "S912L",
    "p.Ser912Leu",
    "2867C>T"
  ],
  "p.Ser912Leu": [
    "c.2735C>T",
    "S912L",
    "p.Ser912Leu",
    "2867C>T"
  ],
  "2867C>T": [
    "c.2735C>T",
    "S912L",
    "p.Ser912Leu",
    "2867C>T"
  ],
  "c.3719T>G": [
    "c.3719T>G",
    "p.Val1240Gly",
    "V1240G",
    "3851T>G"
  ],
  "p.Val1240Gly": [
    "c.3719T>G",
    "p.Val1240Gly",
    "V1240G",
    "3851T>G"
  ],
  "V1240G": [
    "c.3719T>G",
    "p.Val1240Gly",
    "V1240G",
    "3851T>G"
  ],
  "3851T>G": [
    "c.3719T>G",
    "p.Val1240Gly",
    "V1240G",
    "3851T>G"
  ],
  "p.Trp1274X": [
    "p.Trp1274X",
    "c.3822G>A",
    "3954G>A",
    "W1274X"
  ],
  "c.3822G>A": [
    "p.Trp1274X",
    "c.3822G>A",
    "3954G>A",
    "W1274X"
  ],
  "3954G>A": [
    "p.Trp1274X",
    "c.3822G>A",
    "3954G>A",
    "W1274X"
  ],
  "W1274X": [
    "p.Trp1274X",
    "c.3822G>A",
    "3954G>A",
    "W1274X"
  ],
  "4571T>C": [
    "4571T>C",
    "p.Leu1480Pro",
    "L1480P",
    "c.4439T>C"
  ],
  "p.Leu1480Pro": [
    "4571T>C",
    "p.Leu1480Pro",
    "L1480P",
    "c.4439T>C"
  ],
  "L1480P": [
    "4571T>C",
    "p.Leu1480Pro",
    "L1480P",
    "c.4439T>C"
  ],
  "c.4439T>C": [
    "4571T>C",
    "p.Leu1480Pro",
    "L1480P",
    "c.4439T>C"
  ],
  "A120T": [
    "A120T",
    "p.Ala120Thr",
    "c.358G>A",
    "490G>A"
  ],
  "p.Ala120Thr": [
    "A120T",
    "p.Ala120Thr",
    "c.358G>A",
    "490G>A"
  ],
  "c.358G>A": [
    "A120T",
    "p.Ala120Thr",
    "c.358G>A",
    "490G>A"
  ],
  "490G>A": [
    "A120T",
    "p.Ala120Thr",
    "c.358G>A",
    "490G>A"
  ],
  "c.445G>A": [
    "c.445G>A",
    "577G>A",
    "G149R",
    "p.Gly149Arg"
  ],
  "577G>A": [
    "c.445G>A",
    "577G>A",
    "G149R",
    "p.Gly149Arg"
  ],
  "G149R": [
    "c.445G>A",
    "577G>A",
    "G149R",
    "p.Gly149Arg"
  ],
  "p.Gly149Arg": [
    "c.445G>A",
    "577G>A",
    "G149R",
    "p.Gly149Arg"
  ],
  "p.Gly194Arg": [
    "p.Gly194Arg",
    "712G>A",
    "c.580G>A|c.580G>C",
    "G194R"
  ],
  "712G>A": [
    "p.Gly194Arg",
    "712G>A",
    "c.580G>A|c.580G>C",
    "G194R"
  ],
  "c.580G>A|c.580G>C": [
    "p.Gly194Arg",
    "712G>A",
    "c.580G>A|c.580G>C",
    "G194R"
  ],
  "G194R": [
    "p.Gly194Arg",
    "712G>A",
    "c.580G>A|c.580G>C",
    "G194R"
  ],
  "c.794T>G": [
    "c.794T>G",
    "p.Met265Arg",
    "M265R",
    "926T>G"
  ],
  "p.Met265Arg": [
    "c.794T>G",
    "p.Met265Arg",
    "M265R",
    "926T>G"
  ],
  "M265R": [
    "c.794T>G",
    "p.Met265Arg",
    "M265R",
    "926T>G"
  ],
  "926T>G": [
    "c.794T>G",
    "p.Met265Arg",
    "M265R",
    "926T>G"
  ],
  "c.(1392+1_1393-1)_(1584+1_1585-1)del": [
    "c.(1392+1_1393-1)_(1584+1_1585-1)del",
    "p.?",
    "deletion of exon 10 (legacy numbering)|deletion of exon 11 (current numbering)",
    "CFTRdele10"
  ],
  "deletion of exon 10 (legacy numbering)|deletion of exon 11 (current numbering)": [
    "c.(1392+1_1393-1)_(1584+1_1585-1)del",
    "p.?",
    "deletion of exon 10 (legacy numbering)|deletion of exon 11 (current numbering)",
    "CFTRdele10"
  ],
  "CFTRdele10": [
    "c.(1392+1_1393-1)_(1584+1_1585-1)del",
    "p.?",
    "deletion of exon 10 (legacy numbering)|deletion of exon 11 (current numbering)",
    "CFTRdele10"
  ],
  "c.(1766+1_1767-1)_(2619+1_2620-1)del": [
    "c.(1766+1_1767-1)_(2619+1_2620-1)del",
    "p.?",
    "deletion of exons 13 and 14a (legacy numbering)|deletion of exons 14 and 15 (current numbering)",
    "CFTRdele13,14a"
  ],
  "deletion of exons 13 and 14a (legacy numbering)|deletion of exons 14 and 15 (current numbering)": [
    "c.(1766+1_1767-1)_(2619+1_2620-1)del",
    "p.?",
    "deletion of exons 13 and 14a (legacy numbering)|deletion of exons 14 and 15 (current numbering)",
    "CFTRdele13,14a"
  ],
  "CFTRdele13,14a": [
    "c.(1766+1_1767-1)_(2619+1_2620-1)del",
    "p.?",
    "deletion of exons 13 and 14a (legacy numbering)|deletion of exons 14 and 15 (current numbering)",
    "CFTRdele13,14a"
  ],
  "deletion of exons 18 through 20 (legacy numbering)|deletion of exons 21 through 23 (current numbering)": [
    "deletion of exons 18 through 20 (legacy numbering)|deletion of exons 21 through 23 (current numbering)",
    "p.?",
    "c.(3367+1_3368-1)_(3873+1_3874-1)del",
    "CFTRdele18-20"
  ],
  "c.(3367+1_3368-1)_(3873+1_3874-1)del": [
    "deletion of exons 18 through 20 (legacy numbering)|deletion of exons 21 through 23 (current numbering)",
    "p.?",
    "c.(3367+1_3368-1)_(3873+1_3874-1)del",
    "CFTRdele18-20"
  ],
  "CFTRdele18-20": [
    "deletion of exons 18 through 20 (legacy numbering)|deletion of exons 21 through 23 (current numbering)",
    "p.?",
    "c.(3367+1_3368-1)_(3873+1_3874-1)del",
    "CFTRdele18-20"
  ],
  "c.(273+1_274-1)_(1209+1_1210-1)del": [
    "c.(273+1_274-1)_(1209+1_1210-1)del",
    "deletion of exons 4 through 8 (legacy numbering)|deletion of exons 4 through 9 (current numbering)",
    "CFTRdele4-8",
    "p.?"
  ],
  "deletion of exons 4 through 8 (legacy numbering)|deletion of exons 4 through 9 (current numbering)": [
    "c.(273+1_274-1)_(1209+1_1210-1)del",
    "deletion of exons 4 through 8 (legacy numbering)|deletion of exons 4 through 9 (current numbering)",
    "CFTRdele4-8",
    "p.?"
  ],
  "CFTRdele4-8": [
    "c.(273+1_274-1)_(1209+1_1210-1)del",
    "deletion of exons 4 through 8 (legacy numbering)|deletion of exons 4 through 9 (current numbering)",
    "CFTRdele4-8",
    "p.?"
  ],
  "406-2A->G": [
    "406-2A->G",
    "p.?",
    "c.274-2A>G"
  ],
  "c.274-2A>G": [
    "406-2A->G",
    "p.?",
    "c.274-2A>G"
  ],
  "c.761del": [
    "c.761del",
    "p.Lys254ArgfsX7",
    "892delA"
  ],
  "p.Lys254ArgfsX7": [
    "c.761del",
    "p.Lys254ArgfsX7",
    "892delA"
  ],
  "892delA": [
    "c.761del",
    "p.Lys254ArgfsX7",
    "892delA"
  ],
  "c.1083del": [
    "c.1083del",
    "p.Trp361CysfsX8",
    "1215delG"
  ],
  "p.Trp361CysfsX8": [
    "c.1083del",
    "p.Trp361CysfsX8",
    "1215delG"
  ],
  "1215delG": [
    "c.1083del",
    "p.Trp361CysfsX8",
    "1215delG"
  ],
  "p.Gly551ValfsX8": [
    "c.1652del",
    "p.Gly551ValfsX8",
    "1784delG"
  ],
  "1782delA": [
    "p.Gly551ValfsX8",
    "1782delA",
    "c.1650del"
  ],
  "c.1650del": [
    "p.Gly551ValfsX8",
    "1782delA",
    "c.1650del"
  ],
  "Q781X": [
    "Q781X",
    "p.Gln781X",
    "2473C>T",
    "c.2341C>T"
  ],
  "p.Gln781X": [
    "Q781X",
    "p.Gln781X",
    "2473C>T",
    "c.2341C>T"
  ],
  "2473C>T": [
    "Q781X",
    "p.Gln781X",
    "2473C>T",
    "c.2341C>T"
  ],
  "c.2341C>T": [
    "Q781X",
    "p.Gln781X",
    "2473C>T",
    "c.2341C>T"
  ],
  "310G>A": [
    "310G>A",
    "p.Glu60Lys",
    "E60K",
    "c.178G>A"
  ],
  "p.Glu60Lys": [
    "310G>A",
    "p.Glu60Lys",
    "E60K",
    "c.178G>A"
  ],
  "E60K": [
    "310G>A",
    "p.Glu60Lys",
    "E60K",
    "c.178G>A"
  ],
  "c.178G>A": [
    "310G>A",
    "p.Glu60Lys",
    "E60K",
    "c.178G>A"
  ],
  "W1098C": [
    "W1098C",
    "c.3294G>C|c.3294G>T",
    "3426G>C|3426G>T",
    "p.Trp1098Cys"
  ],
  "c.3294G>C|c.3294G>T": [
    "W1098C",
    "c.3294G>C|c.3294G>T",
    "3426G>C|3426G>T",
    "p.Trp1098Cys"
  ],
  "3426G>C|3426G>T": [
    "W1098C",
    "c.3294G>C|c.3294G>T",
    "3426G>C|3426G>T",
    "p.Trp1098Cys"
  ],
  "p.Trp1098Cys": [
    "W1098C",
    "c.3294G>C|c.3294G>T",
    "3426G>C|3426G>T",
    "p.Trp1098Cys"
  ],
  "W1145X": [
    "W1145X",
    "p.Trp1145X",
    "c.3434G>A|c.3435G>A",
    "3567G>A"
  ],
  "p.Trp1145X": [
    "W1145X",
    "p.Trp1145X",
    "c.3434G>A|c.3435G>A",
    "3567G>A"
  ],
  "c.3434G>A|c.3435G>A": [
    "W1145X",
    "p.Trp1145X",
    "c.3434G>A|c.3435G>A",
    "3567G>A"
  ],
  "3567G>A": [
    "W1145X",
    "p.Trp1145X",
    "c.3434G>A|c.3435G>A",
    "3567G>A"
  ],
  "3590T>A": [
    "3590T>A",
    "c.3458T>A",
    "V1153E",
    "p.Val1153Glu"
  ],
  "c.3458T>A": [
    "3590T>A",
    "c.3458T>A",
    "V1153E",
    "p.Val1153Glu"
  ],
  "V1153E": [
    "3590T>A",
    "c.3458T>A",
    "V1153E",
    "p.Val1153Glu"
  ],
  "p.Val1153Glu": [
    "3590T>A",
    "c.3458T>A",
    "V1153E",
    "p.Val1153Glu"
  ],
  "p.Ser1206X": [
    "p.Ser1206X",
    "S1206X",
    "c.3617C>G",
    "3749C>G"
  ],
  "S1206X": [
    "p.Ser1206X",
    "S1206X",
    "c.3617C>G",
    "3749C>G"
  ],
  "c.3617C>G": [
    "p.Ser1206X",
    "S1206X",
    "c.3617C>G",
    "3749C>G"
  ],
  "3749C>G": [
    "p.Ser1206X",
    "S1206X",
    "c.3617C>G",
    "3749C>G"
  ],
  "R1283M": [
    "R1283M",
    "c.3848G>T",
    "3980G>T",
    "p.Arg1283Met"
  ],
  "c.3848G>T": [
    "R1283M",
    "c.3848G>T",
    "3980G>T",
    "p.Arg1283Met"
  ],
  "3980G>T": [
    "R1283M",
    "c.3848G>T",
    "3980G>T",
    "p.Arg1283Met"
  ],
  "p.Arg1283Met": [
    "R1283M",
    "c.3848G>T",
    "3980G>T",
    "p.Arg1283Met"
  ],
  "p.Pro99Leu": [
    "p.Pro99Leu",
    "c.296C>T",
    "P99L",
    "428C>T"
  ],
  "c.296C>T": [
    "p.Pro99Leu",
    "c.296C>T",
    "P99L",
    "428C>T"
  ],
  "P99L": [
    "p.Pro99Leu",
    "c.296C>T",
    "P99L",
    "428C>T"
  ],
  "428C>T": [
    "p.Pro99Leu",
    "c.296C>T",
    "P99L",
    "428C>T"
  ],
  "p.Phe157X": [
    "p.Phe157X",
    "c.470_483del14|c.469_482del14",
    "602del14",
    "c.470_483del"
  ],
  "c.470_483del14|c.469_482del14": [
    "p.Phe157X",
    "c.470_483del14|c.469_482del14",
    "602del14",
    "c.470_483del"
  ],
  "602del14": [
    "p.Phe157X",
    "c.470_483del14|c.469_482del14",
    "602del14",
    "c.470_483del"
  ],
  "c.470_483del": [
    "p.Phe157X",
    "c.470_483del14|c.469_482del14",
    "602del14",
    "c.470_483del"
  ],
  "deletion of exon 15 (legacy numbering)|deletion of exon 17 (current numbering)": [
    "deletion of exon 15 (legacy numbering)|deletion of exon 17 (current numbering)",
    "c.(2657+1_2658-1)_(2908+1_2909-1)del",
    "p.?",
    "CFTRdele15"
  ],
  "c.(2657+1_2658-1)_(2908+1_2909-1)del": [
    "deletion of exon 15 (legacy numbering)|deletion of exon 17 (current numbering)",
    "c.(2657+1_2658-1)_(2908+1_2909-1)del",
    "p.?",
    "CFTRdele15"
  ],
  "CFTRdele15": [
    "deletion of exon 15 (legacy numbering)|deletion of exon 17 (current numbering)",
    "c.(2657+1_2658-1)_(2908+1_2909-1)del",
    "p.?",
    "CFTRdele15"
  ],
  "deletion of exon 20 (legacy numbering)|deletion of exon 23 (current numbering)": [
    "deletion of exon 20 (legacy numbering)|deletion of exon 23 (current numbering)",
    "CFTRdele20",
    "p.?",
    "c.(3717+1_3718-1)_(3873+1_3874-1)del"
  ],
  "CFTRdele20": [
    "deletion of exon 20 (legacy numbering)|deletion of exon 23 (current numbering)",
    "CFTRdele20",
    "p.?",
    "c.(3717+1_3718-1)_(3873+1_3874-1)del"
  ],
  "c.(3717+1_3718-1)_(3873+1_3874-1)del": [
    "deletion of exon 20 (legacy numbering)|deletion of exon 23 (current numbering)",
    "CFTRdele20",
    "p.?",
    "c.(3717+1_3718-1)_(3873+1_3874-1)del"
  ],
  "CFTRdele21": [
    "CFTRdele21",
    "deletion of exon 21 (legacy numbering)|deletion of exon 24 (current numbering)",
    "c.(3873+1_3874-1)_(3963+1_3964-1)del",
    "p.?"
  ],
  "deletion of exon 21 (legacy numbering)|deletion of exon 24 (current numbering)": [
    "CFTRdele21",
    "deletion of exon 21 (legacy numbering)|deletion of exon 24 (current numbering)",
    "c.(3873+1_3874-1)_(3963+1_3964-1)del",
    "p.?"
  ],
  "c.(3873+1_3874-1)_(3963+1_3964-1)del": [
    "CFTRdele21",
    "deletion of exon 21 (legacy numbering)|deletion of exon 24 (current numbering)",
    "c.(3873+1_3874-1)_(3963+1_3964-1)del",
    "p.?"
  ],
  "c.(3468+1_3469-1)_(3717+1_3718-1)dup": [
    "p.?",
    "c.(3468+1_3469-1)_(3717+1_3718-1)dup",
    "CFTRdup19",
    "duplication of exon 19 (legacy numbering)|duplication of exon 22 (current numbering)"
  ],
  "CFTRdup19": [
    "p.?",
    "c.(3468+1_3469-1)_(3717+1_3718-1)dup",
    "CFTRdup19",
    "duplication of exon 19 (legacy numbering)|duplication of exon 22 (current numbering)"
  ],
  "duplication of exon 19 (legacy numbering)|duplication of exon 22 (current numbering)": [
    "p.?",
    "c.(3468+1_3469-1)_(3717+1_3718-1)dup",
    "CFTRdup19",
    "duplication of exon 19 (legacy numbering)|duplication of exon 22 (current numbering)"
  ],
  "c.(1392+1_1393-1)_(1766+1_1767-1)dup": [
    "c.(1392+1_1393-1)_(1766+1_1767-1)dup",
    "p.?",
    "duplication of exons 10 through 12 (legacy numbering)|duplication of exons 11 through 13 (current numbering)",
    "CFTRdup10-12"
  ],
  "duplication of exons 10 through 12 (legacy numbering)|duplication of exons 11 through 13 (current numbering)": [
    "c.(1392+1_1393-1)_(1766+1_1767-1)dup",
    "p.?",
    "duplication of exons 10 through 12 (legacy numbering)|duplication of exons 11 through 13 (current numbering)",
    "CFTRdup10-12"
  ],
  "CFTRdup10-12": [
    "c.(1392+1_1393-1)_(1766+1_1767-1)dup",
    "p.?",
    "duplication of exons 10 through 12 (legacy numbering)|duplication of exons 11 through 13 (current numbering)",
    "CFTRdup10-12"
  ],
  "duplication of exons 8 through 10 (legacy numbering)|duplication of exons 9 through 11 (current numbering)": [
    "duplication of exons 8 through 10 (legacy numbering)|duplication of exons 9 through 11 (current numbering)",
    "c.(1116+1_1117-1)_(1584+1_1585-1)dup",
    "p.?",
    "CFTRdup8-10"
  ],
  "c.(1116+1_1117-1)_(1584+1_1585-1)dup": [
    "duplication of exons 8 through 10 (legacy numbering)|duplication of exons 9 through 11 (current numbering)",
    "c.(1116+1_1117-1)_(1584+1_1585-1)dup",
    "p.?",
    "CFTRdup8-10"
  ],
  "CFTRdup8-10": [
    "duplication of exons 8 through 10 (legacy numbering)|duplication of exons 9 through 11 (current numbering)",
    "c.(1116+1_1117-1)_(1584+1_1585-1)dup",
    "p.?",
    "CFTRdup8-10"
  ],
  "c.[4C>T;7A>T]": [
    "c.[4C>T;7A>T]",
    "Q2X in cis with R3W|[136C>T with 139A>T]",
    "Q2X;R3W"
  ],
  "Q2X in cis with R3W|[136C>T with 139A>T]": [
    "c.[4C>T;7A>T]",
    "Q2X in cis with R3W|[136C>T with 139A>T]",
    "Q2X;R3W"
  ],
  "Q2X;R3W": [
    "c.[4C>T;7A>T]",
    "Q2X in cis with R3W|[136C>T with 139A>T]",
    "Q2X;R3W"
  ],
  "W1282X;R1283M": [
    "W1282X;R1283M",
    "c.[3846G>A;3848G>T]",
    "W1282X in cis with R1283M|[3978G>A or3980G>T]"
  ],
  "c.[3846G>A;3848G>T]": [
    "W1282X;R1283M",
    "c.[3846G>A;3848G>T]",
    "W1282X in cis with R1283M|[3978G>A or3980G>T]"
  ],
  "W1282X in cis with R1283M|[3978G>A or3980G>T]": [
    "W1282X;R1283M",
    "c.[3846G>A;3848G>T]",
    "W1282X in cis with R1283M|[3978G>A or3980G>T]"
  ],
  "3271delGG": [
    "3271delGG",
    "c.3139_3139+1del",
    "p.?"
  ],
  "c.3139_3139+1del": [
    "3271delGG",
    "c.3139_3139+1del",
    "p.?"
  ],
  "1824delA": [
    "1824delA",
    "p.Asp565MetfsX7",
    "c.1692del"
  ],
  "p.Asp565MetfsX7": [
    "1824delA",
    "p.Asp565MetfsX7",
    "c.1692del"
  ],
  "c.1692del": [
    "1824delA",
    "p.Asp565MetfsX7",
    "c.1692del"
  ],
  "2522insC": [
    "2522insC",
    "c.2393dup",
    "p.Gln799SerfsX6"
  ],
  "c.2393dup": [
    "2522insC",
    "c.2393dup",
    "p.Gln799SerfsX6"
  ],
  "p.Gln799SerfsX6": [
    "2522insC",
    "c.2393dup",
    "p.Gln799SerfsX6"
  ],
  "p.Ser1347ProfsX13": [
    "p.Ser1347ProfsX13",
    "c.4035_4038dup",
    "p.S1347PfsX13"
  ],
  "c.4035_4038dup": [
    "p.Ser1347ProfsX13",
    "c.4035_4038dup",
    "p.S1347PfsX13"
  ],
  "p.S1347PfsX13": [
    "p.Ser1347ProfsX13",
    "c.4035_4038dup",
    "p.S1347PfsX13"
  ],
  "p.Leu581PhefsX8": [
    "p.Leu581PhefsX8",
    "1874insT",
    "c.1742dup"
  ],
  "1874insT": [
    "p.Leu581PhefsX8",
    "1874insT",
    "c.1742dup"
  ],
  "c.1742dup": [
    "p.Leu581PhefsX8",
    "1874insT",
    "c.1742dup"
  ],
  "p.Val1008SerfsX15": [
    "c.3021del",
    "p.Val1008SerfsX15",
    "3152delT"
  ],
  "c.3022del": [
    "p.Val1008SerfsX15",
    "c.3022del",
    "3154delG"
  ],
  "3154delG": [
    "p.Val1008SerfsX15",
    "c.3022del",
    "3154delG"
  ],
  "297-3C->T": [
    "297-3C->T",
    "c.165-3C>T",
    "p.?"
  ],
  "c.165-3C>T": [
    "297-3C->T",
    "c.165-3C>T",
    "p.?"
  ],
  "2603delT": [
    "2603delT",
    "c.2472del",
    "p.Asn825ThrfsX5"
  ],
  "c.2472del": [
    "2603delT",
    "c.2472del",
    "p.Asn825ThrfsX5"
  ],
  "p.Asn825ThrfsX5": [
    "2603delT",
    "c.2472del",
    "p.Asn825ThrfsX5"
  ],
  "c.1084_1088dup": [
    "c.1084_1088dup",
    "p.Ser364MetfsX7"
  ],
  "p.Ser364MetfsX7": [
    "c.1084_1088dup",
    "p.Ser364MetfsX7"
  ],
  "c.868C>T": [
    "c.868C>T",
    "p.Gln290X",
    "Q290X",
    "1000C>T"
  ],
  "p.Gln290X": [
    "c.868C>T",
    "p.Gln290X",
    "Q290X",
    "1000C>T"
  ],
  "Q290X": [
    "c.868C>T",
    "p.Gln290X",
    "Q290X",
    "1000C>T"
  ],
  "1000C>T": [
    "c.868C>T",
    "p.Gln290X",
    "Q290X",
    "1000C>T"
  ],
  "Y362X": [
    "Y362X",
    "c.1086T>A|c.1086T>G",
    "p.Tyr362X",
    "1218T>A|1218T>G"
  ],
  "c.1086T>A|c.1086T>G": [
    "Y362X",
    "c.1086T>A|c.1086T>G",
    "p.Tyr362X",
    "1218T>A|1218T>G"
  ],
  "p.Tyr362X": [
    "Y362X",
    "c.1086T>A|c.1086T>G",
    "p.Tyr362X",
    "1218T>A|1218T>G"
  ],
  "1218T>A|1218T>G": [
    "Y362X",
    "c.1086T>A|c.1086T>G",
    "p.Tyr362X",
    "1218T>A|1218T>G"
  ],
  "c.1219G>T": [
    "c.1219G>T",
    "E407X",
    "p.Glu407X",
    "1351G->T"
  ],
  "E407X": [
    "c.1219G>T",
    "E407X",
    "p.Glu407X",
    "1351G->T"
  ],
  "p.Glu407X": [
    "c.1219G>T",
    "E407X",
    "p.Glu407X",
    "1351G->T"
  ],
  "1351G->T": [
    "c.1219G>T",
    "E407X",
    "p.Glu407X",
    "1351G->T"
  ],
  "c.1366G>T": [
    "c.1366G>T",
    "V456F",
    "p.Val456Phe",
    "1498G>T"
  ],
  "V456F": [
    "c.1366G>T",
    "V456F",
    "p.Val456Phe",
    "1498G>T"
  ],
  "p.Val456Phe": [
    "c.1366G>T",
    "V456F",
    "p.Val456Phe",
    "1498G>T"
  ],
  "1498G>T": [
    "c.1366G>T",
    "V456F",
    "p.Val456Phe",
    "1498G>T"
  ],
  "176T>C": [
    "176T>C",
    "c.44T>C",
    "L15P",
    "p.Leu15Pro"
  ],
  "c.44T>C": [
    "176T>C",
    "c.44T>C",
    "L15P",
    "p.Leu15Pro"
  ],
  "L15P": [
    "176T>C",
    "c.44T>C",
    "L15P",
    "p.Leu15Pro"
  ],
  "p.Leu15Pro": [
    "176T>C",
    "c.44T>C",
    "L15P",
    "p.Leu15Pro"
  ],
  "p.Tyr563Asp": [
    "p.Tyr563Asp",
    "c.1687T>G",
    "1819T>G",
    "Y563D"
  ],
  "c.1687T>G": [
    "p.Tyr563Asp",
    "c.1687T>G",
    "1819T>G",
    "Y563D"
  ],
  "1819T>G": [
    "p.Tyr563Asp",
    "c.1687T>G",
    "1819T>G",
    "Y563D"
  ],
  "Y563D": [
    "p.Tyr563Asp",
    "c.1687T>G",
    "1819T>G",
    "Y563D"
  ],
  "p.Ile601Phe": [
    "p.Ile601Phe",
    "1933A>T",
    "c.1801A>T",
    "I601F"
  ],
  "1933A>T": [
    "p.Ile601Phe",
    "1933A>T",
    "c.1801A>T",
    "I601F"
  ],
  "c.1801A>T": [
    "p.Ile601Phe",
    "1933A>T",
    "c.1801A>T",
    "I601F"
  ],
  "I601F": [
    "p.Ile601Phe",
    "1933A>T",
    "c.1801A>T",
    "I601F"
  ],
  "p.Gly27Arg": [
    "p.Gly27Arg",
    "211G>A",
    "c.79G>A",
    "G27R"
  ],
  "211G>A": [
    "p.Gly27Arg",
    "211G>A",
    "c.79G>A",
    "G27R"
  ],
  "c.79G>A": [
    "p.Gly27Arg",
    "211G>A",
    "c.79G>A",
    "G27R"
  ],
  "G27R": [
    "p.Gly27Arg",
    "211G>A",
    "c.79G>A",
    "G27R"
  ],
  "2122G>T": [
    "2122G>T",
    "E664X",
    "c.1990G>T",
    "p.Glu664X"
  ],
  "E664X": [
    "2122G>T",
    "E664X",
    "c.1990G>T",
    "p.Glu664X"
  ],
  "c.1990G>T": [
    "2122G>T",
    "E664X",
    "c.1990G>T",
    "p.Glu664X"
  ],
  "p.Glu664X": [
    "2122G>T",
    "E664X",
    "c.1990G>T",
    "p.Glu664X"
  ],
  "224G>T": [
    "224G>T",
    "p.Arg31Leu",
    "R31L",
    "c.92G>T"
  ],
  "p.Arg31Leu": [
    "224G>T",
    "p.Arg31Leu",
    "R31L",
    "c.92G>T"
  ],
  "R31L": [
    "224G>T",
    "p.Arg31Leu",
    "R31L",
    "c.92G>T"
  ],
  "c.92G>T": [
    "224G>T",
    "p.Arg31Leu",
    "R31L",
    "c.92G>T"
  ],
  "c.2158C>T": [
    "c.2158C>T",
    "2290C>T",
    "Q720X",
    "p.Gln720X"
  ],
  "2290C>T": [
    "c.2158C>T",
    "2290C>T",
    "Q720X",
    "p.Gln720X"
  ],
  "Q720X": [
    "c.2158C>T",
    "2290C>T",
    "Q720X",
    "p.Gln720X"
  ],
  "p.Gln720X": [
    "c.2158C>T",
    "2290C>T",
    "Q720X",
    "p.Gln720X"
  ],
  "p.Ile748SerfsX28": [
    "p.Ile748SerfsX28",
    "2372del8",
    "c.2241_2248del",
    "2373del8|c.2240_2247delCGATACTG"
  ],
  "2372del8": [
    "p.Ile748SerfsX28",
    "2372del8",
    "c.2241_2248del",
    "2373del8|c.2240_2247delCGATACTG"
  ],
  "c.2241_2248del": [
    "p.Ile748SerfsX28",
    "2372del8",
    "c.2241_2248del",
    "2373del8|c.2240_2247delCGATACTG"
  ],
  "2373del8|c.2240_2247delCGATACTG": [
    "p.Ile748SerfsX28",
    "2372del8",
    "c.2241_2248del",
    "2373del8|c.2240_2247delCGATACTG"
  ],
  "2777G>A": [
    "2777G>A",
    "p.Trp882X",
    "W882X",
    "c.2645G>A|c.2646G>A"
  ],
  "p.Trp882X": [
    "2777G>A",
    "p.Trp882X",
    "W882X",
    "c.2645G>A|c.2646G>A"
  ],
  "W882X": [
    "2777G>A",
    "p.Trp882X",
    "W882X",
    "c.2645G>A|c.2646G>A"
  ],
  "c.2645G>A|c.2646G>A": [
    "2777G>A",
    "p.Trp882X",
    "W882X",
    "c.2645G>A|c.2646G>A"
  ],
  "c.236G>A": [
    "c.236G>A",
    "p.Trp79X",
    "368G>A",
    "W79X"
  ],
  "p.Trp79X": [
    "c.236G>A",
    "p.Trp79X",
    "368G>A",
    "W79X"
  ],
  "368G>A": [
    "c.236G>A",
    "p.Trp79X",
    "368G>A",
    "W79X"
  ],
  "W79X": [
    "c.236G>A",
    "p.Trp79X",
    "368G>A",
    "W79X"
  ],
  "p.Gln1281X": [
    "p.Gln1281X",
    "Q1281X",
    "c.3841C>T",
    "3973C>T"
  ],
  "Q1281X": [
    "p.Gln1281X",
    "Q1281X",
    "c.3841C>T",
    "3973C>T"
  ],
  "c.3841C>T": [
    "p.Gln1281X",
    "Q1281X",
    "c.3841C>T",
    "3973C>T"
  ],
  "3973C>T": [
    "p.Gln1281X",
    "Q1281X",
    "c.3841C>T",
    "3973C>T"
  ],
  "p.Gly91Arg": [
    "p.Gly91Arg",
    "G91R",
    "403G>A",
    "c.271G>A"
  ],
  "G91R": [
    "p.Gly91Arg",
    "G91R",
    "403G>A",
    "c.271G>A"
  ],
  "403G>A": [
    "p.Gly91Arg",
    "G91R",
    "403G>A",
    "c.271G>A"
  ],
  "c.271G>A": [
    "p.Gly91Arg",
    "G91R",
    "403G>A",
    "c.271G>A"
  ],
  "4103T>C": [
    "4103T>C",
    "p.Leu1324Pro",
    "L1324P",
    "c.3971T>C"
  ],
  "p.Leu1324Pro": [
    "4103T>C",
    "p.Leu1324Pro",
    "L1324P",
    "c.3971T>C"
  ],
  "L1324P": [
    "4103T>C",
    "p.Leu1324Pro",
    "L1324P",
    "c.3971T>C"
  ],
  "c.3971T>C": [
    "4103T>C",
    "p.Leu1324Pro",
    "L1324P",
    "c.3971T>C"
  ],
  "c.302T>G": [
    "c.302T>G",
    "434T>G",
    "p.Leu101X",
    "L101X"
  ],
  "434T>G": [
    "c.302T>G",
    "434T>G",
    "p.Leu101X",
    "L101X"
  ],
  "p.Leu101X": [
    "c.302T>G",
    "434T>G",
    "p.Leu101X",
    "L101X"
  ],
  "L101X": [
    "c.302T>G",
    "434T>G",
    "p.Leu101X",
    "L101X"
  ],
  "439G>T": [
    "439G>T",
    "c.307G>T",
    "G103X",
    "p.Gly103X"
  ],
  "c.307G>T": [
    "439G>T",
    "c.307G>T",
    "G103X",
    "p.Gly103X"
  ],
  "G103X": [
    "439G>T",
    "c.307G>T",
    "G103X",
    "p.Gly103X"
  ],
  "p.Gly103X": [
    "439G>T",
    "c.307G>T",
    "G103X",
    "p.Gly103X"
  ],
  "613T>G": [
    "613T>G",
    "p.Tyr161Asp",
    "c.481T>G",
    "Y161D"
  ],
  "p.Tyr161Asp": [
    "613T>G",
    "p.Tyr161Asp",
    "c.481T>G",
    "Y161D"
  ],
  "c.481T>G": [
    "613T>G",
    "p.Tyr161Asp",
    "c.481T>G",
    "Y161D"
  ],
  "Y161D": [
    "613T>G",
    "p.Tyr161Asp",
    "c.481T>G",
    "Y161D"
  ],
  "c.580G>T": [
    "c.580G>T",
    "712G>T",
    "G194X",
    "p.Gly194X"
  ],
  "712G>T": [
    "c.580G>T",
    "712G>T",
    "G194X",
    "p.Gly194X"
  ],
  "G194X": [
    "c.580G>T",
    "712G>T",
    "G194X",
    "p.Gly194X"
  ],
  "p.Gly194X": [
    "c.580G>T",
    "712G>T",
    "G194X",
    "p.Gly194X"
  ],
  "p.Cys225X": [
    "p.Cys225X",
    "C225X",
    "807T>A",
    "c.675T>A"
  ],
  "C225X": [
    "p.Cys225X",
    "C225X",
    "807T>A",
    "c.675T>A"
  ],
  "807T>A": [
    "p.Cys225X",
    "C225X",
    "807T>A",
    "c.675T>A"
  ],
  "c.675T>A": [
    "p.Cys225X",
    "C225X",
    "807T>A",
    "c.675T>A"
  ],
  "Q237E": [
    "Q237E",
    "p.Gln237Glu",
    "c.709C>G",
    "841C>G"
  ],
  "p.Gln237Glu": [
    "Q237E",
    "p.Gln237Glu",
    "c.709C>G",
    "841C>G"
  ],
  "c.709C>G": [
    "Q237E",
    "p.Gln237Glu",
    "c.709C>G",
    "841C>G"
  ],
  "841C>G": [
    "Q237E",
    "p.Gln237Glu",
    "c.709C>G",
    "841C>G"
  ],
  "962G>A": [
    "962G>A",
    "p.Trp277X",
    "c.830G>A|c.831G>A",
    "W277X"
  ],
  "p.Trp277X": [
    "962G>A",
    "p.Trp277X",
    "c.830G>A|c.831G>A",
    "W277X"
  ],
  "c.830G>A|c.831G>A": [
    "962G>A",
    "p.Trp277X",
    "c.830G>A|c.831G>A",
    "W277X"
  ],
  "W277X": [
    "962G>A",
    "p.Trp277X",
    "c.830G>A|c.831G>A",
    "W277X"
  ],
  "2556insAT": [
    "2556insAT",
    "c.2423_2424dup",
    "c.2421_2422dupAT|c.2422_2423insAT",
    "p.Ser809IlefsX13"
  ],
  "c.2423_2424dup": [
    "2556insAT",
    "c.2423_2424dup",
    "c.2421_2422dupAT|c.2422_2423insAT",
    "p.Ser809IlefsX13"
  ],
  "c.2421_2422dupAT|c.2422_2423insAT": [
    "2556insAT",
    "c.2423_2424dup",
    "c.2421_2422dupAT|c.2422_2423insAT",
    "p.Ser809IlefsX13"
  ],
  "p.Ser809IlefsX13": [
    "2556insAT",
    "c.2423_2424dup",
    "c.2421_2422dupAT|c.2422_2423insAT",
    "p.Ser809IlefsX13"
  ],
  "c.4147dup": [
    "c.4147dup",
    "4279insA",
    "c.4147_4148insA",
    "p.Ile1383AsnfsX3"
  ],
  "4279insA": [
    "c.4147dup",
    "4279insA",
    "c.4147_4148insA",
    "p.Ile1383AsnfsX3"
  ],
  "c.4147_4148insA": [
    "c.4147dup",
    "4279insA",
    "c.4147_4148insA",
    "p.Ile1383AsnfsX3"
  ],
  "p.Ile1383AsnfsX3": [
    "c.4147dup",
    "4279insA",
    "c.4147_4148insA",
    "p.Ile1383AsnfsX3"
  ],
  "CFTRdele14a": [
    "CFTRdele14a",
    "deletion of exon 14a (legacy numbering)|deletion of exon 15 (current numbering)|c.2490+827_2620-3551del",
    "p.?",
    "c.(2490+1_2491-1)_(2619+1_2620-1)del"
  ],
  "deletion of exon 14a (legacy numbering)|deletion of exon 15 (current numbering)|c.2490+827_2620-3551del": [
    "CFTRdele14a",
    "deletion of exon 14a (legacy numbering)|deletion of exon 15 (current numbering)|c.2490+827_2620-3551del",
    "p.?",
    "c.(2490+1_2491-1)_(2619+1_2620-1)del"
  ],
  "c.(2490+1_2491-1)_(2619+1_2620-1)del": [
    "CFTRdele14a",
    "deletion of exon 14a (legacy numbering)|deletion of exon 15 (current numbering)|c.2490+827_2620-3551del",
    "p.?",
    "c.(2490+1_2491-1)_(2619+1_2620-1)del"
  ],
  "CFTRdele14b,15": [
    "CFTRdele14b,15",
    "p.?",
    "c.(2619+1_2620-1)_(2908+1_2909-1)del",
    "deletion of exons 14b and 15 (legacy numbering)|deletion of exons 16 and 17 (current numbering)"
  ],
  "c.(2619+1_2620-1)_(2908+1_2909-1)del": [
    "CFTRdele14b,15",
    "p.?",
    "c.(2619+1_2620-1)_(2908+1_2909-1)del",
    "deletion of exons 14b and 15 (legacy numbering)|deletion of exons 16 and 17 (current numbering)"
  ],
  "deletion of exons 14b and 15 (legacy numbering)|deletion of exons 16 and 17 (current numbering)": [
    "CFTRdele14b,15",
    "p.?",
    "c.(2619+1_2620-1)_(2908+1_2909-1)del",
    "deletion of exons 14b and 15 (legacy numbering)|deletion of exons 16 and 17 (current numbering)"
  ],
  "c.987del": [
    "c.987del",
    "1119delA",
    "p.Gly330GlufsX39"
  ],
  "1119delA": [
    "c.987del",
    "1119delA",
    "p.Gly330GlufsX39"
  ],
  "p.Gly330GlufsX39": [
    "c.987del",
    "1119delA",
    "p.Gly330GlufsX39"
  ],
  "p.Leu548GlufsX19": [
    "p.Leu548GlufsX19",
    "1774delCT",
    "c.1642_1643del"
  ],
  "1774delCT": [
    "p.Leu548GlufsX19",
    "1774delCT",
    "c.1642_1643del"
  ],
  "c.1642_1643del": [
    "p.Leu548GlufsX19",
    "1774delCT",
    "c.1642_1643del"
  ],
  "c.3605del": [
    "c.3605del",
    "p.Asp1202AlafsX9",
    "3737delA"
  ],
  "p.Asp1202AlafsX9": [
    "c.3605del",
    "p.Asp1202AlafsX9",
    "3737delA"
  ],
  "3737delA": [
    "c.3605del",
    "p.Asp1202AlafsX9",
    "3737delA"
  ],
  "c.2502dup": [
    "c.2502dup",
    "2634insT",
    "p.Asp835X"
  ],
  "2634insT": [
    "c.2502dup",
    "2634insT",
    "p.Asp835X"
  ],
  "p.Asp835X": [
    "c.2502dup",
    "2634insT",
    "p.Asp835X"
  ],
  "c.2924_2925del": [
    "c.2924_2925del",
    "p.Arg975IlefsX10",
    "3056delGA"
  ],
  "p.Arg975IlefsX10": [
    "c.2924_2925del",
    "p.Arg975IlefsX10",
    "3056delGA"
  ],
  "3056delGA": [
    "c.2924_2925del",
    "p.Arg975IlefsX10",
    "3056delGA"
  ],
  "c.234dup": [
    "c.234dup",
    "p.Trp79LeufsX32",
    "366insC"
  ],
  "366insC": [
    "c.234dup",
    "p.Trp79LeufsX32",
    "366insC"
  ],
  "c.1469del": [
    "c.1469del",
    "p.Phe490SerfsX37",
    "1601delT"
  ],
  "p.Phe490SerfsX37": [
    "c.1469del",
    "p.Phe490SerfsX37",
    "1601delT"
  ],
  "1601delT": [
    "c.1469del",
    "p.Phe490SerfsX37",
    "1601delT"
  ],
  "p.Ile853TyrfsX43": [
    "p.Ile853TyrfsX43",
    "c.2556dupT",
    "c.2556dup"
  ],
  "c.2556dupT": [
    "p.Ile853TyrfsX43",
    "c.2556dupT",
    "c.2556dup"
  ],
  "c.2556dup": [
    "p.Ile853TyrfsX43",
    "c.2556dupT",
    "c.2556dup"
  ],
  "183delC": [
    "183delC",
    "p.Phe17LeufsX8",
    "c.51del"
  ],
  "p.Phe17LeufsX8": [
    "183delC",
    "p.Phe17LeufsX8",
    "c.51del"
  ],
  "c.51del": [
    "183delC",
    "p.Phe17LeufsX8",
    "c.51del"
  ],
  "1490T>C": [
    "1490T>C",
    "c.1358T>C",
    "L453S",
    "p.Leu453Ser"
  ],
  "c.1358T>C": [
    "1490T>C",
    "c.1358T>C",
    "L453S",
    "p.Leu453Ser"
  ],
  "L453S": [
    "1490T>C",
    "c.1358T>C",
    "L453S",
    "p.Leu453Ser"
  ],
  "p.Leu453Ser": [
    "1490T>C",
    "c.1358T>C",
    "L453S",
    "p.Leu453Ser"
  ],
  "p.Trp19X": [
    "p.Trp19X",
    "c.56G>A|c.57G>A",
    "179G>A",
    "W19X"
  ],
  "c.56G>A|c.57G>A": [
    "p.Trp19X",
    "c.56G>A|c.57G>A",
    "179G>A",
    "W19X"
  ],
  "179G>A": [
    "p.Trp19X",
    "c.56G>A|c.57G>A",
    "179G>A",
    "W19X"
  ],
  "W19X": [
    "p.Trp19X",
    "c.56G>A|c.57G>A",
    "179G>A",
    "W19X"
  ],
  "2365G>T": [
    "2365G>T",
    "p.Gly745X",
    "G745X",
    "c.2233G>T"
  ],
  "p.Gly745X": [
    "2365G>T",
    "p.Gly745X",
    "G745X",
    "c.2233G>T"
  ],
  "G745X": [
    "2365G>T",
    "p.Gly745X",
    "G745X",
    "c.2233G>T"
  ],
  "c.2233G>T": [
    "2365G>T",
    "p.Gly745X",
    "G745X",
    "c.2233G>T"
  ],
  "p.Phe1016Ser": [
    "p.Phe1016Ser",
    "3179T>C",
    "c.3047T>C",
    "F1016S"
  ],
  "3179T>C": [
    "p.Phe1016Ser",
    "3179T>C",
    "c.3047T>C",
    "F1016S"
  ],
  "c.3047T>C": [
    "p.Phe1016Ser",
    "3179T>C",
    "c.3047T>C",
    "F1016S"
  ],
  "F1016S": [
    "p.Phe1016Ser",
    "3179T>C",
    "c.3047T>C",
    "F1016S"
  ],
  "H1085P": [
    "H1085P",
    "3386A>C",
    "p.His1085Pro",
    "c.3254A>C"
  ],
  "3386A>C": [
    "H1085P",
    "3386A>C",
    "p.His1085Pro",
    "c.3254A>C"
  ],
  "p.His1085Pro": [
    "H1085P",
    "3386A>C",
    "p.His1085Pro",
    "c.3254A>C"
  ],
  "c.3254A>C": [
    "H1085P",
    "3386A>C",
    "p.His1085Pro",
    "c.3254A>C"
  ],
  "c.252T>A": [
    "c.252T>A",
    "Y84X",
    "p.Tyr84X",
    "384T>A"
  ],
  "Y84X": [
    "c.252T>A",
    "Y84X",
    "p.Tyr84X",
    "384T>A"
  ],
  "p.Tyr84X": [
    "c.252T>A",
    "Y84X",
    "p.Tyr84X",
    "384T>A"
  ],
  "384T>A": [
    "c.252T>A",
    "Y84X",
    "p.Tyr84X",
    "384T>A"
  ],
  "S1248X": [
    "S1248X",
    "p.Ser1248X",
    "3875C>A|3875C>G",
    "c.3743C>A|c.3743C>G"
  ],
  "p.Ser1248X": [
    "S1248X",
    "p.Ser1248X",
    "3875C>A|3875C>G",
    "c.3743C>A|c.3743C>G"
  ],
  "3875C>A|3875C>G": [
    "S1248X",
    "p.Ser1248X",
    "3875C>A|3875C>G",
    "c.3743C>A|c.3743C>G"
  ],
  "c.3743C>A|c.3743C>G": [
    "S1248X",
    "p.Ser1248X",
    "3875C>A|3875C>G",
    "c.3743C>A|c.3743C>G"
  ],
  "Q1291X": [
    "Q1291X",
    "p.Gln1291X",
    "c.3871C>T",
    "4003C>T"
  ],
  "p.Gln1291X": [
    "Q1291X",
    "p.Gln1291X",
    "c.3871C>T",
    "4003C>T"
  ],
  "c.3871C>T": [
    "Q1291X",
    "p.Gln1291X",
    "c.3871C>T",
    "4003C>T"
  ],
  "4003C>T": [
    "Q1291X",
    "p.Gln1291X",
    "c.3871C>T",
    "4003C>T"
  ],
  "L102R": [
    "L102R",
    "c.305T>G",
    "437T>G",
    "p.Leu102Arg"
  ],
  "c.305T>G": [
    "L102R",
    "c.305T>G",
    "437T>G",
    "p.Leu102Arg"
  ],
  "437T>G": [
    "L102R",
    "c.305T>G",
    "437T>G",
    "p.Leu102Arg"
  ],
  "p.Leu102Arg": [
    "L102R",
    "c.305T>G",
    "437T>G",
    "p.Leu102Arg"
  ],
  "459T>A": [
    "459T>A",
    "Y109X",
    "p.Tyr109X",
    "c.327T>A"
  ],
  "Y109X": [
    "459T>A",
    "Y109X",
    "p.Tyr109X",
    "c.327T>A"
  ],
  "p.Tyr109X": [
    "c.326_327del",
    "458delAT",
    "p.Tyr109X"
  ],
  "c.327T>A": [
    "459T>A",
    "Y109X",
    "p.Tyr109X",
    "c.327T>A"
  ],
  "482G>C": [
    "482G>C",
    "c.350G>C",
    "R117P",
    "p.Arg117Pro"
  ],
  "c.350G>C": [
    "482G>C",
    "c.350G>C",
    "R117P",
    "p.Arg117Pro"
  ],
  "R117P": [
    "482G>C",
    "c.350G>C",
    "R117P",
    "p.Arg117Pro"
  ],
  "p.Arg117Pro": [
    "482G>C",
    "c.350G>C",
    "R117P",
    "p.Arg117Pro"
  ],
  "738G>A": [
    "738G>A",
    "p.Trp202X",
    "c.606G>A",
    "W202X"
  ],
  "p.Trp202X": [
    "738G>A",
    "p.Trp202X",
    "c.606G>A",
    "W202X"
  ],
  "c.606G>A": [
    "738G>A",
    "p.Trp202X",
    "c.606G>A",
    "W202X"
  ],
  "W202X": [
    "738G>A",
    "p.Trp202X",
    "c.606G>A",
    "W202X"
  ],
  "CFTRdele17a": [
    "CFTRdele17a",
    "deletion of exon 17a (legacy numbering)|deletion of exon 19 (current numbering)",
    "p.?",
    "c.(2988+1_2989-1)_(3139+1_3140-1)del"
  ],
  "deletion of exon 17a (legacy numbering)|deletion of exon 19 (current numbering)": [
    "CFTRdele17a",
    "deletion of exon 17a (legacy numbering)|deletion of exon 19 (current numbering)",
    "p.?",
    "c.(2988+1_2989-1)_(3139+1_3140-1)del"
  ],
  "c.(2988+1_2989-1)_(3139+1_3140-1)del": [
    "CFTRdele17a",
    "deletion of exon 17a (legacy numbering)|deletion of exon 19 (current numbering)",
    "p.?",
    "c.(2988+1_2989-1)_(3139+1_3140-1)del"
  ],
  "CFTRdele22": [
    "CFTRdele22",
    "p.?",
    "c.(3963+1_3964-1)_(4136+1_4137-1)del",
    "deletion of exon 22 (legacy numbering)|deletion of exon 25 (current numbering)"
  ],
  "c.(3963+1_3964-1)_(4136+1_4137-1)del": [
    "CFTRdele22",
    "p.?",
    "c.(3963+1_3964-1)_(4136+1_4137-1)del",
    "deletion of exon 22 (legacy numbering)|deletion of exon 25 (current numbering)"
  ],
  "deletion of exon 22 (legacy numbering)|deletion of exon 25 (current numbering)": [
    "CFTRdele22",
    "p.?",
    "c.(3963+1_3964-1)_(4136+1_4137-1)del",
    "deletion of exon 22 (legacy numbering)|deletion of exon 25 (current numbering)"
  ],
  "deletion of exons 10 through 14b (legacy numbering)|deletion of exons 11 through 16 (current numbering)": [
    "deletion of exons 10 through 14b (legacy numbering)|deletion of exons 11 through 16 (current numbering)",
    "c.1392+12_2657+403delins35",
    "p.?",
    "CFTRdele10-14b"
  ],
  "c.1392+12_2657+403delins35": [
    "deletion of exons 10 through 14b (legacy numbering)|deletion of exons 11 through 16 (current numbering)",
    "c.1392+12_2657+403delins35",
    "p.?",
    "CFTRdele10-14b"
  ],
  "CFTRdele10-14b": [
    "deletion of exons 10 through 14b (legacy numbering)|deletion of exons 11 through 16 (current numbering)",
    "c.1392+12_2657+403delins35",
    "p.?",
    "CFTRdele10-14b"
  ],
  "deletion of exons 14a through 15 (legacy numbering)|deletion of exons 15 through 17 (current numbering)": [
    "deletion of exons 14a through 15 (legacy numbering)|deletion of exons 15 through 17 (current numbering)",
    "p.?",
    "c.(2490+1_2491-1)_(2908+1_2909-1)del",
    "CFTRdele14a-15"
  ],
  "c.(2490+1_2491-1)_(2908+1_2909-1)del": [
    "deletion of exons 14a through 15 (legacy numbering)|deletion of exons 15 through 17 (current numbering)",
    "p.?",
    "c.(2490+1_2491-1)_(2908+1_2909-1)del",
    "CFTRdele14a-15"
  ],
  "CFTRdele14a-15": [
    "deletion of exons 14a through 15 (legacy numbering)|deletion of exons 15 through 17 (current numbering)",
    "p.?",
    "c.(2490+1_2491-1)_(2908+1_2909-1)del",
    "CFTRdele14a-15"
  ],
  "296+1G->C": [
    "p.?",
    "296+1G->C",
    "c.164+1G>C"
  ],
  "c.164+1G>C": [
    "p.?",
    "296+1G->C",
    "c.164+1G>C"
  ],
  "c.1679+2T>C": [
    "p.?",
    "c.1679+2T>C",
    "1811+2T->C"
  ],
  "1811+2T->C": [
    "p.?",
    "c.1679+2T>C",
    "1811+2T->C"
  ],
  "1898+2T->A": [
    "1898+2T->A",
    "p.?",
    "c.1766+2T>A"
  ],
  "c.1766+2T>A": [
    "1898+2T->A",
    "p.?",
    "c.1766+2T>A"
  ],
  "c.2908+1G>A": [
    "c.2908+1G>A",
    "p.?",
    "3040+1G->A"
  ],
  "3040+1G->A": [
    "c.2908+1G>A",
    "p.?",
    "3040+1G->A"
  ],
  "621+2T->C": [
    "621+2T->C",
    "p.?",
    "c.489+2T>C"
  ],
  "c.489+2T>C": [
    "621+2T->C",
    "p.?",
    "c.489+2T>C"
  ],
  "2790-2A->G": [
    "2790-2A->G",
    "p.?",
    "c.2658-2A>G"
  ],
  "c.2658-2A>G": [
    "2790-2A->G",
    "p.?",
    "c.2658-2A>G"
  ],
  "c.1584+2T>C": [
    "c.1584+2T>C",
    "p.?",
    "1716+2T->C"
  ],
  "1716+2T->C": [
    "c.1584+2T>C",
    "p.?",
    "1716+2T->C"
  ],
  "c.580-2A>G": [
    "c.580-2A>G",
    "p.?",
    "712-2A->G"
  ],
  "712-2A->G": [
    "c.580-2A>G",
    "p.?",
    "712-2A->G"
  ],
  "297-2A->G": [
    "297-2A->G",
    "c.165-2A>G",
    "p.?"
  ],
  "c.165-2A>G": [
    "297-2A->G",
    "c.165-2A>G",
    "p.?"
  ],
  "c.1976del": [
    "c.1976del",
    "2108delA",
    "p.Asn659IlefsX4"
  ],
  "2108delA": [
    "c.1976del",
    "2108delA",
    "p.Asn659IlefsX4"
  ],
  "p.Asn659IlefsX4": [
    "c.1976del",
    "2108delA",
    "p.Asn659IlefsX4"
  ],
  "c.1302del": [
    "c.1302del",
    "p.Leu435PhefsX7",
    "1434delA"
  ],
  "p.Leu435PhefsX7": [
    "c.1302del",
    "p.Leu435PhefsX7",
    "1434delA"
  ],
  "1434delA": [
    "c.1302del",
    "p.Leu435PhefsX7",
    "1434delA"
  ],
  "1366delG": [
    "1366delG",
    "p.Ala412GlnfsX30",
    "c.1234del"
  ],
  "p.Ala412GlnfsX30": [
    "1366delG",
    "p.Ala412GlnfsX30",
    "c.1234del"
  ],
  "c.1234del": [
    "1366delG",
    "p.Ala412GlnfsX30",
    "c.1234del"
  ],
  "p.Gly458AspfsX11": [
    "p.Gly458AspfsX11",
    "1504delG",
    "c.1373del"
  ],
  "1504delG": [
    "p.Gly458AspfsX11",
    "1504delG",
    "c.1373del"
  ],
  "c.1373del": [
    "p.Gly458AspfsX11",
    "1504delG",
    "c.1373del"
  ],
  "p.Ile864MetfsX31": [
    "p.Ile864MetfsX31",
    "c.2592_2593del",
    "2723delTT"
  ],
  "c.2592_2593del": [
    "p.Ile864MetfsX31",
    "c.2592_2593del",
    "2723delTT"
  ],
  "2723delTT": [
    "p.Ile864MetfsX31",
    "c.2592_2593del",
    "2723delTT"
  ],
  "c.3600del": [
    "c.3600del",
    "3732delA",
    "p.Asp1201MetfsX10"
  ],
  "3732delA": [
    "c.3600del",
    "3732delA",
    "p.Asp1201MetfsX10"
  ],
  "p.Asp1201MetfsX10": [
    "c.3600del",
    "3732delA",
    "p.Asp1201MetfsX10"
  ],
  "4259del5": [
    "4259del5",
    "p.Leu1376SerfsX8",
    "c.4127_4131del"
  ],
  "p.Leu1376SerfsX8": [
    "4259del5",
    "p.Leu1376SerfsX8",
    "c.4127_4131del"
  ],
  "c.4127_4131del": [
    "4259del5",
    "p.Leu1376SerfsX8",
    "c.4127_4131del"
  ],
  "c.543_546del": [
    "c.543_546del",
    "675del4",
    "p.Leu183PhefsX5"
  ],
  "675del4": [
    "c.543_546del",
    "675del4",
    "p.Leu183PhefsX5"
  ],
  "p.Leu183PhefsX5": [
    "c.543_546del",
    "675del4",
    "p.Leu183PhefsX5"
  ],
  "c.777del": [
    "c.777del",
    "p.Val260X",
    "909delT"
  ],
  "p.Val260X": [
    "c.777del",
    "p.Val260X",
    "909delT"
  ],
  "909delT": [
    "c.777del",
    "p.Val260X",
    "909delT"
  ],
  "c.580-2A>C": [
    "c.580-2A>C",
    "p.?",
    "712-2A->C"
  ],
  "712-2A->C": [
    "c.580-2A>C",
    "p.?",
    "712-2A->C"
  ],
  "p.Tyr852LeufsX44": [
    "p.Tyr852LeufsX44",
    "c.2554dup",
    "2686dupT"
  ],
  "c.2554dup": [
    "p.Tyr852LeufsX44",
    "c.2554dup",
    "2686dupT"
  ],
  "2686dupT": [
    "p.Tyr852LeufsX44",
    "c.2554dup",
    "2686dupT"
  ],
  "604insA": [
    "604insA",
    "c.472dup",
    "p.Ser158LysfsX5"
  ],
  "c.472dup": [
    "604insA",
    "c.472dup",
    "p.Ser158LysfsX5"
  ],
  "p.Ser158LysfsX5": [
    "604insA",
    "c.472dup",
    "p.Ser158LysfsX5"
  ],
  "c.708del": [
    "c.708del",
    "p.Gln237ArgfsX4",
    "840delT"
  ],
  "p.Gln237ArgfsX4": [
    "c.708del",
    "p.Gln237ArgfsX4",
    "840delT"
  ],
  "840delT": [
    "c.708del",
    "p.Gln237ArgfsX4",
    "840delT"
  ],
  "p.Glu292X": [
    "p.Glu292X",
    "E292X",
    "1006G>T",
    "c.874G>T"
  ],
  "E292X": [
    "p.Glu292X",
    "E292X",
    "1006G>T",
    "c.874G>T"
  ],
  "1006G>T": [
    "p.Glu292X",
    "E292X",
    "1006G>T",
    "c.874G>T"
  ],
  "c.874G>T": [
    "p.Glu292X",
    "E292X",
    "1006G>T",
    "c.874G>T"
  ],
  "c.1301_1307del": [
    "c.1301_1307del",
    "1429del7",
    "p.Ser434LeufsX6",
    "1433delCACTTCT"
  ],
  "1429del7": [
    "c.1301_1307del",
    "1429del7",
    "p.Ser434LeufsX6",
    "1433delCACTTCT"
  ],
  "p.Ser434LeufsX6": [
    "c.1301_1307del",
    "1429del7",
    "p.Ser434LeufsX6",
    "1433delCACTTCT"
  ],
  "1433delCACTTCT": [
    "c.1301_1307del",
    "1429del7",
    "p.Ser434LeufsX6",
    "1433delCACTTCT"
  ],
  "c.1420G>A": [
    "c.1420G>A",
    "p.Glu474Lys",
    "E474K",
    "1552G>A"
  ],
  "p.Glu474Lys": [
    "c.1420G>A",
    "p.Glu474Lys",
    "E474K",
    "1552G>A"
  ],
  "E474K": [
    "c.1420G>A",
    "p.Glu474Lys",
    "E474K",
    "1552G>A"
  ],
  "1552G>A": [
    "c.1420G>A",
    "p.Glu474Lys",
    "E474K",
    "1552G>A"
  ],
  "p.Glu514X": [
    "p.Glu514X",
    "E514X",
    "1672G>T",
    "c.1540G>T"
  ],
  "E514X": [
    "p.Glu514X",
    "E514X",
    "1672G>T",
    "c.1540G>T"
  ],
  "1672G>T": [
    "p.Glu514X",
    "E514X",
    "1672G>T",
    "c.1540G>T"
  ],
  "c.1540G>T": [
    "p.Glu514X",
    "E514X",
    "1672G>T",
    "c.1540G>T"
  ],
  "Y563X": [
    "Y563X",
    "p.Tyr563X",
    "1821C>A",
    "c.1689C>A"
  ],
  "p.Tyr563X": [
    "Y563X",
    "p.Tyr563X",
    "1821C>A",
    "c.1689C>A"
  ],
  "1821C>A": [
    "Y563X",
    "p.Tyr563X",
    "1821C>A",
    "c.1689C>A"
  ],
  "c.1689C>A": [
    "Y563X",
    "p.Tyr563X",
    "1821C>A",
    "c.1689C>A"
  ],
  "c.1954C>T": [
    "c.1954C>T",
    "p.Gln652X",
    "Q652X",
    "2086C>T"
  ],
  "p.Gln652X": [
    "c.1954C>T",
    "p.Gln652X",
    "Q652X",
    "2086C>T"
  ],
  "Q652X": [
    "c.1954C>T",
    "p.Gln652X",
    "Q652X",
    "2086C>T"
  ],
  "2086C>T": [
    "c.1954C>T",
    "p.Gln652X",
    "Q652X",
    "2086C>T"
  ],
  "Q685X": [
    "Q685X",
    "2185C>T",
    "c.2053C>T",
    "p.Gln685X"
  ],
  "2185C>T": [
    "Q685X",
    "2185C>T",
    "c.2053C>T",
    "p.Gln685X"
  ],
  "c.2053C>T": [
    "Q685X",
    "2185C>T",
    "c.2053C>T",
    "p.Gln685X"
  ],
  "p.Gln685X": [
    "Q685X",
    "2185C>T",
    "c.2053C>T",
    "p.Gln685X"
  ],
  "Q715X": [
    "Q715X",
    "c.2143C>T",
    "p.Gln715X",
    "2275C>T"
  ],
  "c.2143C>T": [
    "Q715X",
    "c.2143C>T",
    "p.Gln715X",
    "2275C>T"
  ],
  "p.Gln715X": [
    "Q715X",
    "c.2143C>T",
    "p.Gln715X",
    "2275C>T"
  ],
  "2275C>T": [
    "Q715X",
    "c.2143C>T",
    "p.Gln715X",
    "2275C>T"
  ],
  "2902G>A": [
    "2902G>A",
    "c.2770G>A",
    "D924N",
    "p.Asp924Asn"
  ],
  "c.2770G>A": [
    "2902G>A",
    "c.2770G>A",
    "D924N",
    "p.Asp924Asn"
  ],
  "D924N": [
    "2902G>A",
    "c.2770G>A",
    "D924N",
    "p.Asp924Asn"
  ],
  "p.Asp924Asn": [
    "2902G>A",
    "c.2770G>A",
    "D924N",
    "p.Asp924Asn"
  ],
  "3064A>T": [
    "3064A>T",
    "c.2932A>T",
    "p.Lys978X",
    "K978X"
  ],
  "c.2932A>T": [
    "3064A>T",
    "c.2932A>T",
    "p.Lys978X",
    "K978X"
  ],
  "p.Lys978X": [
    "3064A>T",
    "c.2932A>T",
    "p.Lys978X",
    "K978X"
  ],
  "K978X": [
    "3064A>T",
    "c.2932A>T",
    "p.Lys978X",
    "K978X"
  ],
  "c.3189G>A": [
    "c.3189G>A",
    "W1063X",
    "3321G>A",
    "p.Trp1063X"
  ],
  "W1063X": [
    "c.3189G>A",
    "W1063X",
    "3321G>A",
    "p.Trp1063X"
  ],
  "3321G>A": [
    "c.3189G>A",
    "W1063X",
    "3321G>A",
    "p.Trp1063X"
  ],
  "p.Trp1063X": [
    "c.3189G>A",
    "W1063X",
    "3321G>A",
    "p.Trp1063X"
  ],
  "p.Lys68X": [
    "p.Lys68X",
    "334A>T",
    "K68X",
    "c.202A>T"
  ],
  "334A>T": [
    "p.Lys68X",
    "334A>T",
    "K68X",
    "c.202A>T"
  ],
  "K68X": [
    "p.Lys68X",
    "334A>T",
    "K68X",
    "c.202A>T"
  ],
  "c.202A>T": [
    "p.Lys68X",
    "334A>T",
    "K68X",
    "c.202A>T"
  ],
  "K1302X": [
    "K1302X",
    "c.3904A>T",
    "p.Lys1302X",
    "4036A>T"
  ],
  "c.3904A>T": [
    "K1302X",
    "c.3904A>T",
    "p.Lys1302X",
    "4036A>T"
  ],
  "p.Lys1302X": [
    "K1302X",
    "c.3904A>T",
    "p.Lys1302X",
    "4036A>T"
  ],
  "4036A>T": [
    "K1302X",
    "c.3904A>T",
    "p.Lys1302X",
    "4036A>T"
  ],
  "4054G>T": [
    "4054G>T",
    "E1308X",
    "p.Glu1308X",
    "c.3922G>T"
  ],
  "E1308X": [
    "4054G>T",
    "E1308X",
    "p.Glu1308X",
    "c.3922G>T"
  ],
  "p.Glu1308X": [
    "4054G>T",
    "E1308X",
    "p.Glu1308X",
    "c.3922G>T"
  ],
  "c.3922G>T": [
    "4054G>T",
    "E1308X",
    "p.Glu1308X",
    "c.3922G>T"
  ],
  "Q1309X": [
    "Q1309X",
    "p.Gln1309X",
    "4057C>T",
    "c.3925C>T"
  ],
  "p.Gln1309X": [
    "Q1309X",
    "p.Gln1309X",
    "4057C>T",
    "c.3925C>T"
  ],
  "4057C>T": [
    "Q1309X",
    "p.Gln1309X",
    "4057C>T",
    "c.3925C>T"
  ],
  "c.3925C>T": [
    "Q1309X",
    "p.Gln1309X",
    "4057C>T",
    "c.3925C>T"
  ],
  "p.Gln207X": [
    "p.Gln207X",
    "751C>T",
    "c.619C>T",
    "Q207X"
  ],
  "751C>T": [
    "p.Gln207X",
    "751C>T",
    "c.619C>T",
    "Q207X"
  ],
  "c.619C>T": [
    "p.Gln207X",
    "751C>T",
    "c.619C>T",
    "Q207X"
  ],
  "Q207X": [
    "p.Gln207X",
    "751C>T",
    "c.619C>T",
    "Q207X"
  ],
  "c.647G>A|c.648G>A": [
    "c.647G>A|c.648G>A",
    "W216X",
    "779G>A",
    "p.Trp216X"
  ],
  "W216X": [
    "c.647G>A|c.648G>A",
    "W216X",
    "779G>A",
    "p.Trp216X"
  ],
  "779G>A": [
    "c.647G>A|c.648G>A",
    "W216X",
    "779G>A",
    "p.Trp216X"
  ],
  "p.Trp216X": [
    "c.647G>A|c.648G>A",
    "W216X",
    "779G>A",
    "p.Trp216X"
  ],
  "3349insT": [
    "3349insT",
    "p.Tyr1073LeufsX3",
    "c.3217_3218insT",
    "c.3217dup"
  ],
  "p.Tyr1073LeufsX3": [
    "3349insT",
    "p.Tyr1073LeufsX3",
    "c.3217_3218insT",
    "c.3217dup"
  ],
  "c.3217_3218insT": [
    "3349insT",
    "p.Tyr1073LeufsX3",
    "c.3217_3218insT",
    "c.3217dup"
  ],
  "c.3217dup": [
    "3349insT",
    "p.Tyr1073LeufsX3",
    "c.3217_3218insT",
    "c.3217dup"
  ],
  "CFTRdele17b": [
    "CFTRdele17b",
    "deletion of exon 17b (legacy numbering)|deletion of exon 20 (current numbering)",
    "c.(3139+1_3140-1)_(3367+1_3368-1)del",
    "p.?"
  ],
  "deletion of exon 17b (legacy numbering)|deletion of exon 20 (current numbering)": [
    "CFTRdele17b",
    "deletion of exon 17b (legacy numbering)|deletion of exon 20 (current numbering)",
    "c.(3139+1_3140-1)_(3367+1_3368-1)del",
    "p.?"
  ],
  "c.(3139+1_3140-1)_(3367+1_3368-1)del": [
    "CFTRdele17b",
    "deletion of exon 17b (legacy numbering)|deletion of exon 20 (current numbering)",
    "c.(3139+1_3140-1)_(3367+1_3368-1)del",
    "p.?"
  ],
  "duplication of exons 1 through 3 (legacy and current numbering)": [
    "duplication of exons 1 through 3 (legacy and current numbering)",
    "c.(?_1)_(273+1_274-1)dup",
    "CFTRdup1-3",
    "p.?"
  ],
  "c.(?_1)_(273+1_274-1)dup": [
    "duplication of exons 1 through 3 (legacy and current numbering)",
    "c.(?_1)_(273+1_274-1)dup",
    "CFTRdup1-3",
    "p.?"
  ],
  "CFTRdup1-3": [
    "duplication of exons 1 through 3 (legacy and current numbering)",
    "c.(?_1)_(273+1_274-1)dup",
    "CFTRdup1-3",
    "p.?"
  ],
  "F508C;S1251N": [
    "F508C;S1251N",
    "F508C in cis with S1251N|[1655T>G with 3884G>A]",
    "c.[1523T>G;3752G>A]"
  ],
  "F508C in cis with S1251N|[1655T>G with 3884G>A]": [
    "F508C;S1251N",
    "F508C in cis with S1251N|[1655T>G with 3884G>A]",
    "c.[1523T>G;3752G>A]"
  ],
  "c.[1523T>G;3752G>A]": [
    "F508C;S1251N",
    "F508C in cis with S1251N|[1655T>G with 3884G>A]",
    "c.[1523T>G;3752G>A]"
  ],
  "406-1G->C": [
    "406-1G->C",
    "p.?",
    "c.274-1G>C"
  ],
  "c.274-1G>C": [
    "406-1G->C",
    "p.?",
    "c.274-1G>C"
  ],
  "c.2620-2A>G": [
    "c.2620-2A>G",
    "p.?",
    "2752-2A->G"
  ],
  "2752-2A->G": [
    "c.2620-2A>G",
    "p.?",
    "2752-2A->G"
  ],
  "876-2A->G": [
    "876-2A->G",
    "c.744-2A>G",
    "p.?"
  ],
  "c.744-2A>G": [
    "876-2A->G",
    "c.744-2A>G",
    "p.?"
  ],
  "3940delG": [
    "3940delG",
    "p.Asp1270MetfsX8",
    "c.3808del"
  ],
  "p.Asp1270MetfsX8": [
    "3940delG",
    "p.Asp1270MetfsX8",
    "c.3808del"
  ],
  "c.3808del": [
    "3940delG",
    "p.Asp1270MetfsX8",
    "c.3808del"
  ],
  "630delG": [
    "630delG",
    "c.498del",
    "p.Lys166AsnfsX7"
  ],
  "c.498del": [
    "630delG",
    "c.498del",
    "p.Lys166AsnfsX7"
  ],
  "p.Lys166AsnfsX7": [
    "630delG",
    "c.498del",
    "p.Lys166AsnfsX7"
  ],
  "c.874_875del": [
    "c.874_875del",
    "p.Glu292ThrfsX15",
    "1006_1007delGA"
  ],
  "p.Glu292ThrfsX15": [
    "c.874_875del",
    "p.Glu292ThrfsX15",
    "1006_1007delGA"
  ],
  "1006_1007delGA": [
    "c.874_875del",
    "p.Glu292ThrfsX15",
    "1006_1007delGA"
  ],
  "593insT": [
    "593insT",
    "p.Ala155SerfsX4",
    "c.461dup"
  ],
  "p.Ala155SerfsX4": [
    "593insT",
    "p.Ala155SerfsX4",
    "c.461dup"
  ],
  "c.461dup": [
    "593insT",
    "p.Ala155SerfsX4",
    "c.461dup"
  ],
  "c.764del": [
    "c.764del",
    "p.Ile255ThrfsX6",
    "896delT"
  ],
  "p.Ile255ThrfsX6": [
    "c.764del",
    "p.Ile255ThrfsX6",
    "896delT"
  ],
  "896delT": [
    "c.764del",
    "p.Ile255ThrfsX6",
    "896delT"
  ],
  "p.Asp648ValfsX15": [
    "p.Asp648ValfsX15",
    "2075delA",
    "c.1943del"
  ],
  "2075delA": [
    "p.Asp648ValfsX15",
    "2075delA",
    "c.1943del"
  ],
  "c.1943del": [
    "p.Asp648ValfsX15",
    "2075delA",
    "c.1943del"
  ],
  "p.Leu184PhefsX5": [
    "p.Leu184PhefsX5",
    "c.550del",
    "681delC"
  ],
  "c.550del": [
    "p.Leu184PhefsX5",
    "c.550del",
    "681delC"
  ],
  "681delC": [
    "p.Leu184PhefsX5",
    "c.550del",
    "681delC"
  ],
  "1199delG": [
    "1199delG",
    "p.Ala357LeufsX12",
    "c.1069del"
  ],
  "p.Ala357LeufsX12": [
    "1199delG",
    "p.Ala357LeufsX12",
    "c.1069del"
  ],
  "c.1069del": [
    "1199delG",
    "p.Ala357LeufsX12",
    "c.1069del"
  ],
  "2634delT": [
    "2634delT",
    "p.Phe834LeufsX10",
    "c.2502del"
  ],
  "p.Phe834LeufsX10": [
    "2634delT",
    "p.Phe834LeufsX10",
    "c.2502del"
  ],
  "c.2502del": [
    "2634delT",
    "p.Phe834LeufsX10",
    "c.2502del"
  ],
  "3528delC": [
    "3528delC",
    "c.3397del",
    "p.Leu1133X"
  ],
  "c.3397del": [
    "3528delC",
    "c.3397del",
    "p.Leu1133X"
  ],
  "p.Leu1133X": [
    "3528delC",
    "c.3397del",
    "p.Leu1133X"
  ],
  "c.3530del": [
    "c.3530del",
    "p.Lys1177SerfsX15",
    "3662delA"
  ],
  "3662delA": [
    "c.3530del",
    "p.Lys1177SerfsX15",
    "3662delA"
  ],
  "p.Leu327GlnfsX42": [
    "p.Leu327GlnfsX42",
    "c.980del",
    "1112delT"
  ],
  "c.980del": [
    "p.Leu327GlnfsX42",
    "c.980del",
    "1112delT"
  ],
  "1112delT": [
    "p.Leu327GlnfsX42",
    "c.980del",
    "1112delT"
  ],
  "1802delC": [
    "1802delC",
    "p.Ser557PhefsX2",
    "c.1670del"
  ],
  "p.Ser557PhefsX2": [
    "1802delC",
    "p.Ser557PhefsX2",
    "c.1670del"
  ],
  "c.1670del": [
    "1802delC",
    "p.Ser557PhefsX2",
    "c.1670del"
  ],
  "c.49_50dup": [
    "c.49_50dup",
    "p.Trp19AlafsX7",
    "181_182dup"
  ],
  "p.Trp19AlafsX7": [
    "c.49_50dup",
    "p.Trp19AlafsX7",
    "181_182dup"
  ],
  "181_182dup": [
    "c.49_50dup",
    "p.Trp19AlafsX7",
    "181_182dup"
  ],
  "c.4139del": [
    "c.4139del",
    "4271delC",
    "p.Thr1380AsnfsX4"
  ],
  "4271delC": [
    "c.4139del",
    "4271delC",
    "p.Thr1380AsnfsX4"
  ],
  "p.Thr1380AsnfsX4": [
    "c.4139del",
    "4271delC",
    "p.Thr1380AsnfsX4"
  ],
  "c.3618_3619del": [
    "c.3618_3619del",
    "p.Gly1208ProfsX56",
    "3750delAG"
  ],
  "p.Gly1208ProfsX56": [
    "c.3618_3619del",
    "p.Gly1208ProfsX56",
    "3750delAG"
  ],
  "3750delAG": [
    "c.3618_3619del",
    "p.Gly1208ProfsX56",
    "3750delAG"
  ],
  "c.164+4dup": [
    "c.164+4dup",
    "p.?",
    "296+3insT"
  ],
  "296+3insT": [
    "c.164+4dup",
    "p.?",
    "296+3insT"
  ],
  "710_711+5del7": [
    "710_711+5del7",
    "p.?",
    "c.578_579+5del"
  ],
  "c.578_579+5del": [
    "710_711+5del7",
    "p.?",
    "c.578_579+5del"
  ],
  "3271+1delG": [
    "3271+1delG",
    "p.?",
    "c.3139+1del"
  ],
  "c.3139+1del": [
    "3271+1delG",
    "p.?",
    "c.3139+1del"
  ],
  "c.3883_3884insG": [
    "c.3883_3884insG",
    "p.Ile1295SerfsX7"
  ],
  "p.Ile1295SerfsX7": [
    "c.3883_3884insG",
    "p.Ile1295SerfsX7"
  ],
  "p.Ser686AsnfsX37": [
    "p.Ser686AsnfsX37",
    "c.2053_2054insAA"
  ],
  "c.2053_2054insAA": [
    "p.Ser686AsnfsX37",
    "c.2053_2054insAA"
  ],
  "p.Gln552HisfsX7": [
    "p.Gln552HisfsX7",
    "c.1656del",
    "1787delA"
  ],
  "c.1656del": [
    "p.Gln552HisfsX7",
    "c.1656del",
    "1787delA"
  ],
  "1787delA": [
    "p.Gln552HisfsX7",
    "c.1656del",
    "1787delA"
  ],
  "D443fs": [
    "D443fs",
    "c.1329_1350del",
    "p.Asp443GlufsX19"
  ],
  "c.1329_1350del": [
    "D443fs",
    "c.1329_1350del",
    "p.Asp443GlufsX19"
  ],
  "p.Asp443GlufsX19": [
    "D443fs",
    "c.1329_1350del",
    "p.Asp443GlufsX19"
  ],
  "c.1068G>A": [
    "c.1068G>A",
    "1200G>A",
    "W356X",
    "p.Trp356X"
  ],
  "1200G>A": [
    "c.1068G>A",
    "1200G>A",
    "W356X",
    "p.Trp356X"
  ],
  "W356X": [
    "c.1068G>A",
    "1200G>A",
    "W356X",
    "p.Trp356X"
  ],
  "p.Trp356X": [
    "p.Trp356X",
    "1200_1219del20",
    "c.1068_1087del"
  ],
  "p.Trp361X": [
    "p.Trp361X",
    "c.1082G>A|c.1083G>A",
    "1214G>A|1215G>A",
    "W361X"
  ],
  "c.1082G>A|c.1083G>A": [
    "p.Trp361X",
    "c.1082G>A|c.1083G>A",
    "1214G>A|1215G>A",
    "W361X"
  ],
  "1214G>A|1215G>A": [
    "p.Trp361X",
    "c.1082G>A|c.1083G>A",
    "1214G>A|1215G>A",
    "W361X"
  ],
  "W361X": [
    "p.Trp361X",
    "c.1082G>A|c.1083G>A",
    "1214G>A|1215G>A",
    "W361X"
  ],
  "1273A>T": [
    "1273A>T",
    "K381X",
    "p.Lys381X",
    "c.1141A>T"
  ],
  "K381X": [
    "1273A>T",
    "K381X",
    "p.Lys381X",
    "c.1141A>T"
  ],
  "p.Lys381X": [
    "1273A>T",
    "K381X",
    "p.Lys381X",
    "c.1141A>T"
  ],
  "c.1141A>T": [
    "1273A>T",
    "K381X",
    "p.Lys381X",
    "c.1141A>T"
  ],
  "1863C>A": [
    "1863C>A",
    "Y577X",
    "p.Tyr577X",
    "c.1731C>A"
  ],
  "Y577X": [
    "1863C>A",
    "Y577X",
    "p.Tyr577X",
    "c.1731C>A"
  ],
  "p.Tyr577X": [
    "1863C>A",
    "Y577X",
    "p.Tyr577X",
    "c.1731C>A"
  ],
  "c.1731C>A": [
    "1863C>A",
    "Y577X",
    "p.Tyr577X",
    "c.1731C>A"
  ],
  "p.Lys598X": [
    "p.Lys598X",
    "K598X",
    "c.1792A>T",
    "1924A>T"
  ],
  "K598X": [
    "p.Lys598X",
    "K598X",
    "c.1792A>T",
    "1924A>T"
  ],
  "c.1792A>T": [
    "p.Lys598X",
    "K598X",
    "c.1792A>T",
    "1924A>T"
  ],
  "1924A>T": [
    "p.Lys598X",
    "K598X",
    "c.1792A>T",
    "1924A>T"
  ],
  "2098G>T": [
    "2098G>T",
    "p.Glu656X",
    "c.1966G>T",
    "E656X"
  ],
  "p.Glu656X": [
    "2098G>T",
    "p.Glu656X",
    "c.1966G>T",
    "E656X"
  ],
  "c.1966G>T": [
    "2098G>T",
    "p.Glu656X",
    "c.1966G>T",
    "E656X"
  ],
  "E656X": [
    "2098G>T",
    "p.Glu656X",
    "c.1966G>T",
    "E656X"
  ],
  "W679X": [
    "W679X",
    "c.2036G>A|c.2037G>A",
    "2168G>A",
    "p.Trp679X"
  ],
  "c.2036G>A|c.2037G>A": [
    "W679X",
    "c.2036G>A|c.2037G>A",
    "2168G>A",
    "p.Trp679X"
  ],
  "2168G>A": [
    "W679X",
    "c.2036G>A|c.2037G>A",
    "2168G>A",
    "p.Trp679X"
  ],
  "p.Trp679X": [
    "W679X",
    "c.2036G>A|c.2037G>A",
    "2168G>A",
    "p.Trp679X"
  ],
  "c.97G>T": [
    "c.97G>T",
    "229G>T",
    "p.Glu33X",
    "E33X"
  ],
  "229G>T": [
    "c.97G>T",
    "229G>T",
    "p.Glu33X",
    "E33X"
  ],
  "p.Glu33X": [
    "c.97G>T",
    "229G>T",
    "p.Glu33X",
    "E33X"
  ],
  "E33X": [
    "c.97G>T",
    "229G>T",
    "p.Glu33X",
    "E33X"
  ],
  "p.Ser962X": [
    "p.Ser962X",
    "S962X",
    "3017C>A|3017C>G",
    "c.2885C>A|c.2885C>G"
  ],
  "S962X": [
    "p.Ser962X",
    "S962X",
    "3017C>A|3017C>G",
    "c.2885C>A|c.2885C>G"
  ],
  "3017C>A|3017C>G": [
    "p.Ser962X",
    "S962X",
    "3017C>A|3017C>G",
    "c.2885C>A|c.2885C>G"
  ],
  "c.2885C>A|c.2885C>G": [
    "p.Ser962X",
    "S962X",
    "3017C>A|3017C>G",
    "c.2885C>A|c.2885C>G"
  ],
  "3068A>T": [
    "3068A>T",
    "D979V",
    "p.Asp979Val",
    "c.2936A>T"
  ],
  "D979V": [
    "3068A>T",
    "D979V",
    "p.Asp979Val",
    "c.2936A>T"
  ],
  "p.Asp979Val": [
    "3068A>T",
    "D979V",
    "p.Asp979Val",
    "c.2936A>T"
  ],
  "c.2936A>T": [
    "3068A>T",
    "D979V",
    "p.Asp979Val",
    "c.2936A>T"
  ],
  "3514A>T": [
    "3514A>T",
    "R1128X",
    "p.Arg1128X",
    "c.3382A>T"
  ],
  "R1128X": [
    "3514A>T",
    "R1128X",
    "p.Arg1128X",
    "c.3382A>T"
  ],
  "p.Arg1128X": [
    "3514A>T",
    "R1128X",
    "p.Arg1128X",
    "c.3382A>T"
  ],
  "c.3382A>T": [
    "3514A>T",
    "R1128X",
    "p.Arg1128X",
    "c.3382A>T"
  ],
  "Q1144X": [
    "Q1144X",
    "p.Gln1144X",
    "c.3430C>T",
    "3562C>T"
  ],
  "p.Gln1144X": [
    "Q1144X",
    "p.Gln1144X",
    "c.3430C>T",
    "3562C>T"
  ],
  "c.3430C>T": [
    "Q1144X",
    "p.Gln1144X",
    "c.3430C>T",
    "3562C>T"
  ],
  "3562C>T": [
    "Q1144X",
    "p.Gln1144X",
    "c.3430C>T",
    "3562C>T"
  ],
  "p.Glu1266X": [
    "p.Glu1266X",
    "c.3796G>T",
    "3928G>T",
    "E1266X"
  ],
  "c.3796G>T": [
    "p.Glu1266X",
    "c.3796G>T",
    "3928G>T",
    "E1266X"
  ],
  "3928G>T": [
    "p.Glu1266X",
    "c.3796G>T",
    "3928G>T",
    "E1266X"
  ],
  "E1266X": [
    "p.Glu1266X",
    "c.3796G>T",
    "3928G>T",
    "E1266X"
  ],
  "c.3838C>T": [
    "c.3838C>T",
    "Q1280X",
    "p.Gln1280X",
    "3970C>T"
  ],
  "Q1280X": [
    "c.3838C>T",
    "Q1280X",
    "p.Gln1280X",
    "3970C>T"
  ],
  "p.Gln1280X": [
    "c.3838C>T",
    "Q1280X",
    "p.Gln1280X",
    "3970C>T"
  ],
  "3970C>T": [
    "c.3838C>T",
    "Q1280X",
    "p.Gln1280X",
    "3970C>T"
  ],
  "4300C>T": [
    "4300C>T",
    "Q1390X",
    "p.Gln1390X",
    "c.4168C>T"
  ],
  "Q1390X": [
    "4300C>T",
    "Q1390X",
    "p.Gln1390X",
    "c.4168C>T"
  ],
  "p.Gln1390X": [
    "4300C>T",
    "Q1390X",
    "p.Gln1390X",
    "c.4168C>T"
  ],
  "c.4168C>T": [
    "4300C>T",
    "Q1390X",
    "p.Gln1390X",
    "c.4168C>T"
  ],
  "667C>T": [
    "667C>T",
    "Q179X",
    "c.535C>T",
    "p.Gln179X"
  ],
  "Q179X": [
    "667C>T",
    "Q179X",
    "c.535C>T",
    "p.Gln179X"
  ],
  "c.535C>T": [
    "667C>T",
    "Q179X",
    "c.535C>T",
    "p.Gln179X"
  ],
  "p.Gln179X": [
    "667C>T",
    "Q179X",
    "c.535C>T",
    "p.Gln179X"
  ],
  "p.Leu1346MetfsX6": [
    "p.Leu1346MetfsX6",
    "c.4036_4042del",
    "4168delCTAAGCC"
  ],
  "c.4036_4042del": [
    "p.Leu1346MetfsX6",
    "c.4036_4042del",
    "4168delCTAAGCC"
  ],
  "4168delCTAAGCC": [
    "p.Leu1346MetfsX6",
    "c.4036_4042del",
    "4168delCTAAGCC"
  ],
  "CFTRdele3": [
    "CFTRdele3",
    "p.?",
    "c.(164+1_165-1)_(273+1_274-1)del",
    "deletion of exon 3 (legacy and current numbering)"
  ],
  "c.(164+1_165-1)_(273+1_274-1)del": [
    "CFTRdele3",
    "p.?",
    "c.(164+1_165-1)_(273+1_274-1)del",
    "deletion of exon 3 (legacy and current numbering)"
  ],
  "deletion of exon 3 (legacy and current numbering)": [
    "CFTRdele3",
    "p.?",
    "c.(164+1_165-1)_(273+1_274-1)del",
    "deletion of exon 3 (legacy and current numbering)"
  ],
  "CFTRdele4": [
    "p.?",
    "CFTRdele4",
    "deletion of exon 4 (legacy and current numbering)",
    "c.(273+1_274-1)_(489+1_490-1)del"
  ],
  "deletion of exon 4 (legacy and current numbering)": [
    "p.?",
    "CFTRdele4",
    "deletion of exon 4 (legacy and current numbering)",
    "c.(273+1_274-1)_(489+1_490-1)del"
  ],
  "c.(273+1_274-1)_(489+1_490-1)del": [
    "p.?",
    "CFTRdele4",
    "deletion of exon 4 (legacy and current numbering)",
    "c.(273+1_274-1)_(489+1_490-1)del"
  ],
  "deletion of exon 8 (legacy numbering)|deletion of exon 9 (current numbering)": [
    "deletion of exon 8 (legacy numbering)|deletion of exon 9 (current numbering)",
    "CFTRdele8",
    "c.(1116+1_1117-1)_(1209+1_1210-1)del",
    "p.?"
  ],
  "CFTRdele8": [
    "deletion of exon 8 (legacy numbering)|deletion of exon 9 (current numbering)",
    "CFTRdele8",
    "c.(1116+1_1117-1)_(1209+1_1210-1)del",
    "p.?"
  ],
  "c.(1116+1_1117-1)_(1209+1_1210-1)del": [
    "deletion of exon 8 (legacy numbering)|deletion of exon 9 (current numbering)",
    "CFTRdele8",
    "c.(1116+1_1117-1)_(1209+1_1210-1)del",
    "p.?"
  ],
  "CFTRdele1-10": [
    "CFTRdele1-10",
    "p.?",
    "deletion of exons 1 through 10 (legacy numbering)|deletion of exons 1 through 11 (current numbering)",
    "c.(?_-1)_(1584+1_1585-1)del"
  ],
  "deletion of exons 1 through 10 (legacy numbering)|deletion of exons 1 through 11 (current numbering)": [
    "CFTRdele1-10",
    "p.?",
    "deletion of exons 1 through 10 (legacy numbering)|deletion of exons 1 through 11 (current numbering)",
    "c.(?_-1)_(1584+1_1585-1)del"
  ],
  "c.(?_-1)_(1584+1_1585-1)del": [
    "CFTRdele1-10",
    "p.?",
    "deletion of exons 1 through 10 (legacy numbering)|deletion of exons 1 through 11 (current numbering)",
    "c.(?_-1)_(1584+1_1585-1)del"
  ],
  "deletion of exons 1 through 9 (legacy numbering)|deletion of exons 1 through 10 (current numbering)": [
    "p.?",
    "deletion of exons 1 through 9 (legacy numbering)|deletion of exons 1 through 10 (current numbering)",
    "c.(?_1)_(1392+1_1393-1)del",
    "CFTRdele1-9"
  ],
  "c.(?_1)_(1392+1_1393-1)del": [
    "p.?",
    "deletion of part of the promoter through exon 9 (legacy numbering)|deletion of part of the promoter through exon 10 (current numbering)",
    "CFTRdelePr-9",
    "c.(?_1)_(1392+1_1393-1)del"
  ],
  "CFTRdele1-9": [
    "p.?",
    "deletion of exons 1 through 9 (legacy numbering)|deletion of exons 1 through 10 (current numbering)",
    "c.(?_1)_(1392+1_1393-1)del",
    "CFTRdele1-9"
  ],
  "CFTRdele16-20": [
    "CFTRdele16-20",
    "p.?",
    "deletion of exons 16 through 20 (legacy numbering)|deletion of exons 16 through 23 (current numbering)",
    "c.(2908+1_2909-1)_(3873+1_3874-1)del"
  ],
  "deletion of exons 16 through 20 (legacy numbering)|deletion of exons 16 through 23 (current numbering)": [
    "CFTRdele16-20",
    "p.?",
    "deletion of exons 16 through 20 (legacy numbering)|deletion of exons 16 through 23 (current numbering)",
    "c.(2908+1_2909-1)_(3873+1_3874-1)del"
  ],
  "c.(2908+1_2909-1)_(3873+1_3874-1)del": [
    "CFTRdele16-20",
    "p.?",
    "deletion of exons 16 through 20 (legacy numbering)|deletion of exons 16 through 23 (current numbering)",
    "c.(2908+1_2909-1)_(3873+1_3874-1)del"
  ],
  "c.(53+1_54-1)_(1584+1_1585-1)del": [
    "c.(53+1_54-1)_(1584+1_1585-1)del",
    "p.?",
    "deletion of exons 2 through 10 (legacy numbering)|deletion of exons 2 through 11 (current numbering)",
    "CFTRdele2-10"
  ],
  "deletion of exons 2 through 10 (legacy numbering)|deletion of exons 2 through 11 (current numbering)": [
    "c.(53+1_54-1)_(1584+1_1585-1)del",
    "p.?",
    "deletion of exons 2 through 10 (legacy numbering)|deletion of exons 2 through 11 (current numbering)",
    "CFTRdele2-10"
  ],
  "CFTRdele2-10": [
    "c.(53+1_54-1)_(1584+1_1585-1)del",
    "p.?",
    "deletion of exons 2 through 10 (legacy numbering)|deletion of exons 2 through 11 (current numbering)",
    "CFTRdele2-10"
  ],
  "c.273+7983_743+362delinsACCTCG": [
    "c.273+7983_743+362delinsACCTCG",
    "p.?",
    "CFTRdele4-6ains6",
    "deletion of exons 4 through 6a and insertion of 6 nucleotides (legacy numbering)|deletion of exons 4 through 7 and insertion of 6 nucleotides (current numbering)"
  ],
  "CFTRdele4-6ains6": [
    "c.273+7983_743+362delinsACCTCG",
    "p.?",
    "CFTRdele4-6ains6",
    "deletion of exons 4 through 6a and insertion of 6 nucleotides (legacy numbering)|deletion of exons 4 through 7 and insertion of 6 nucleotides (current numbering)"
  ],
  "deletion of exons 4 through 6a and insertion of 6 nucleotides (legacy numbering)|deletion of exons 4 through 7 and insertion of 6 nucleotides (current numbering)": [
    "c.273+7983_743+362delinsACCTCG",
    "p.?",
    "CFTRdele4-6ains6",
    "deletion of exons 4 through 6a and insertion of 6 nucleotides (legacy numbering)|deletion of exons 4 through 7 and insertion of 6 nucleotides (current numbering)"
  ],
  "CFTRdele4-8,12-21": [
    "CFTRdele4-8,12-21",
    "deletion of exons 4 through 8 and 12 through 21 (legacy numbering)|deletion of exons 4 through 9 and 13 through 24 (current numbering)",
    "p.?",
    "c.[(273+1_274-1)_(1209+1_1210-1)del;(1679+1_1680-1)_(3963+1_3964-1)del]"
  ],
  "deletion of exons 4 through 8 and 12 through 21 (legacy numbering)|deletion of exons 4 through 9 and 13 through 24 (current numbering)": [
    "CFTRdele4-8,12-21",
    "deletion of exons 4 through 8 and 12 through 21 (legacy numbering)|deletion of exons 4 through 9 and 13 through 24 (current numbering)",
    "p.?",
    "c.[(273+1_274-1)_(1209+1_1210-1)del;(1679+1_1680-1)_(3963+1_3964-1)del]"
  ],
  "c.[(273+1_274-1)_(1209+1_1210-1)del;(1679+1_1680-1)_(3963+1_3964-1)del]": [
    "CFTRdele4-8,12-21",
    "deletion of exons 4 through 8 and 12 through 21 (legacy numbering)|deletion of exons 4 through 9 and 13 through 24 (current numbering)",
    "p.?",
    "c.[(273+1_274-1)_(1209+1_1210-1)del;(1679+1_1680-1)_(3963+1_3964-1)del]"
  ],
  "deletion of exons 8 and 9 (legacy numbering)|deletion of exons 9 and 10 (current numbering)": [
    "deletion of exons 8 and 9 (legacy numbering)|deletion of exons 9 and 10 (current numbering)",
    "CFTRdele8,9",
    "p.?",
    "c.(1116+1_1117-1)_(1392+1_1393-1)del"
  ],
  "CFTRdele8,9": [
    "deletion of exons 8 and 9 (legacy numbering)|deletion of exons 9 and 10 (current numbering)",
    "CFTRdele8,9",
    "p.?",
    "c.(1116+1_1117-1)_(1392+1_1393-1)del"
  ],
  "c.(1116+1_1117-1)_(1392+1_1393-1)del": [
    "deletion of exons 8 and 9 (legacy numbering)|deletion of exons 9 and 10 (current numbering)",
    "CFTRdele8,9",
    "p.?",
    "c.(1116+1_1117-1)_(1392+1_1393-1)del"
  ],
  "c.(?_1)_(273+1_274-1)del": [
    "c.(?_1)_(273+1_274-1)del",
    "p.?",
    "deletion of part of the promoter through exon 3 (legacy and current numbering)",
    "CFTRdelePr-3"
  ],
  "deletion of part of the promoter through exon 3 (legacy and current numbering)": [
    "c.(?_1)_(273+1_274-1)del",
    "p.?",
    "deletion of part of the promoter through exon 3 (legacy and current numbering)",
    "CFTRdelePr-3"
  ],
  "CFTRdelePr-3": [
    "c.(?_1)_(273+1_274-1)del",
    "p.?",
    "deletion of part of the promoter through exon 3 (legacy and current numbering)",
    "CFTRdelePr-3"
  ],
  "CFTRdup2": [
    "CFTRdup2",
    "duplication of exon 2 (legacy and current numbering)",
    "p.?",
    "c.54-4235_164+377dup"
  ],
  "duplication of exon 2 (legacy and current numbering)": [
    "CFTRdup2",
    "duplication of exon 2 (legacy and current numbering)",
    "p.?",
    "c.54-4235_164+377dup"
  ],
  "c.54-4235_164+377dup": [
    "CFTRdup2",
    "duplication of exon 2 (legacy and current numbering)",
    "p.?",
    "c.54-4235_164+377dup"
  ],
  "CFTRdup4-10": [
    "CFTRdup4-10",
    "p.?",
    "c.(273+1_274-1)_(1584+1_1585-1)dup",
    "duplication of exons 4 through 9 (legacy numbering)|duplication of exons 4 through 10 (current numbering)"
  ],
  "c.(273+1_274-1)_(1584+1_1585-1)dup": [
    "CFTRdup4-10",
    "p.?",
    "c.(273+1_274-1)_(1584+1_1585-1)dup",
    "duplication of exons 4 through 9 (legacy numbering)|duplication of exons 4 through 10 (current numbering)"
  ],
  "duplication of exons 4 through 9 (legacy numbering)|duplication of exons 4 through 10 (current numbering)": [
    "CFTRdup4-10",
    "p.?",
    "c.(273+1_274-1)_(1584+1_1585-1)dup",
    "duplication of exons 4 through 9 (legacy numbering)|duplication of exons 4 through 10 (current numbering)"
  ],
  "duplication of exons 6b and 7 (legacy numbering)|duplication of exons 7 and 8 (current numbering)": [
    "duplication of exons 6b and 7 (legacy numbering)|duplication of exons 7 and 8 (current numbering)",
    "CFTRdup6b,7",
    "p.?",
    "c.(743+1_744-1)_(1116+1_1117-1)dup"
  ],
  "CFTRdup6b,7": [
    "duplication of exons 6b and 7 (legacy numbering)|duplication of exons 7 and 8 (current numbering)",
    "CFTRdup6b,7",
    "p.?",
    "c.(743+1_744-1)_(1116+1_1117-1)dup"
  ],
  "c.(743+1_744-1)_(1116+1_1117-1)dup": [
    "duplication of exons 6b and 7 (legacy numbering)|duplication of exons 7 and 8 (current numbering)",
    "CFTRdup6b,7",
    "p.?",
    "c.(743+1_744-1)_(1116+1_1117-1)dup"
  ],
  "3600+1G->T": [
    "3600+1G->T",
    "c.3468+1G>T",
    "p.?"
  ],
  "c.3468+1G>T": [
    "3600+1G->T",
    "c.3468+1G>T",
    "p.?"
  ],
  "296+2T->G": [
    "296+2T->G",
    "p.?",
    "c.164+2T>G"
  ],
  "c.164+2T>G": [
    "296+2T->G",
    "p.?",
    "c.164+2T>G"
  ],
  "c.489+1G>A": [
    "c.489+1G>A",
    "621+1G->A",
    "p.?"
  ],
  "621+1G->A": [
    "c.489+1G>A",
    "621+1G->A",
    "p.?"
  ],
  "c.1585-1G>T": [
    "c.1585-1G>T",
    "p.?",
    "1717-1G->T"
  ],
  "1717-1G->T": [
    "c.1585-1G>T",
    "p.?",
    "1717-1G->T"
  ],
  "c.2619+2T>C": [
    "c.2619+2T>C",
    "p.?",
    "2751+2T->C"
  ],
  "2751+2T->C": [
    "c.2619+2T>C",
    "p.?",
    "2751+2T->C"
  ],
  "1001+1G->C": [
    "p.?",
    "1001+1G->C",
    "c.869+1G>C"
  ],
  "c.869+1G>C": [
    "p.?",
    "1001+1G->C",
    "c.869+1G>C"
  ],
  "296+2T->C": [
    "p.?",
    "296+2T->C",
    "c.164+2T>C"
  ],
  "c.164+2T>C": [
    "p.?",
    "296+2T->C",
    "c.164+2T>C"
  ],
  "c.54-1G>A": [
    "c.54-1G>A",
    "p.?",
    "186-1G->A"
  ],
  "186-1G->A": [
    "c.54-1G>A",
    "p.?",
    "186-1G->A"
  ],
  "875+2T->C": [
    "875+2T->C",
    "p.?",
    "c.743+2T>C"
  ],
  "c.743+2T>C": [
    "875+2T->C",
    "p.?",
    "c.743+2T>C"
  ],
  "c.3365del": [
    "c.3365del",
    "3497delC",
    "p.Thr1122LysfsX12"
  ],
  "3497delC": [
    "c.3365del",
    "3497delC",
    "p.Thr1122LysfsX12"
  ],
  "p.Thr1122LysfsX12": [
    "c.3365del",
    "3497delC",
    "p.Thr1122LysfsX12"
  ],
  "1540del10": [
    "1540del10",
    "c.1409_1418del",
    "p.Val470GlufsX54"
  ],
  "c.1409_1418del": [
    "1540del10",
    "c.1409_1418del",
    "p.Val470GlufsX54"
  ],
  "p.Val470GlufsX54": [
    "1540del10",
    "c.1409_1418del",
    "p.Val470GlufsX54"
  ],
  "c.1920_1921dup": [
    "c.1920_1921dup",
    "p.Ser641IlefsX23",
    "2053insTA"
  ],
  "p.Ser641IlefsX23": [
    "c.1920_1921dup",
    "p.Ser641IlefsX23",
    "2053insTA"
  ],
  "2053insTA": [
    "c.1920_1921dup",
    "p.Ser641IlefsX23",
    "2053insTA"
  ],
  "1353delA": [
    "1353delA",
    "c.1221del",
    "p.Glu407AspfsX35"
  ],
  "c.1221del": [
    "1353delA",
    "c.1221del",
    "p.Glu407AspfsX35"
  ],
  "p.Glu407AspfsX35": [
    "1353delA",
    "c.1221del",
    "p.Glu407AspfsX35"
  ],
  "c.142_145del": [
    "c.142_145del",
    "p.Asn48TyrfsX42",
    "c.142_145delAATC"
  ],
  "p.Asn48TyrfsX42": [
    "c.142_145del",
    "p.Asn48TyrfsX42",
    "c.142_145delAATC"
  ],
  "c.142_145delAATC": [
    "c.142_145del",
    "p.Asn48TyrfsX42",
    "c.142_145delAATC"
  ],
  "c.2089dup": [
    "c.2089dup",
    "2221insA",
    "p.Arg697LysfsX33"
  ],
  "2221insA": [
    "c.2089dup",
    "2221insA",
    "p.Arg697LysfsX33"
  ],
  "p.Arg697LysfsX33": [
    "c.2089dup",
    "2221insA",
    "p.Arg697LysfsX33"
  ],
  "p.Val754GlyfsX17": [
    "p.Val754GlyfsX17",
    "c.2261delT",
    "c.2261del"
  ],
  "c.2261delT": [
    "p.Val754GlyfsX17",
    "c.2261delT",
    "c.2261del"
  ],
  "c.2261del": [
    "p.Val754GlyfsX17",
    "c.2261delT",
    "c.2261del"
  ],
  "3667del4": [
    "3667del4",
    "p.Thr1179AsnfsX12",
    "c.3536_3539del"
  ],
  "p.Thr1179AsnfsX12": [
    "3667del4",
    "p.Thr1179AsnfsX12",
    "c.3536_3539del"
  ],
  "c.3536_3539del": [
    "3667del4",
    "p.Thr1179AsnfsX12",
    "c.3536_3539del"
  ],
  "c.601del": [
    "c.601del",
    "733delG",
    "p.Val201CysfsX14"
  ],
  "733delG": [
    "c.601del",
    "733delG",
    "p.Val201CysfsX14"
  ],
  "p.Val201CysfsX14": [
    "c.601del",
    "733delG",
    "p.Val201CysfsX14"
  ],
  "c.717del": [
    "c.717del",
    "849delG",
    "p.Leu240X"
  ],
  "849delG": [
    "c.717del",
    "849delG",
    "p.Leu240X"
  ],
  "p.Leu240X": [
    "p.Leu240X",
    "L240X",
    "c.714del"
  ],
  "p.Ile444X": [
    "p.Ile444X",
    "1460delAT",
    "c.1330_1331del"
  ],
  "1460delAT": [
    "p.Ile444X",
    "1460delAT",
    "c.1330_1331del"
  ],
  "c.1330_1331del": [
    "p.Ile444X",
    "1460delAT",
    "c.1330_1331del"
  ],
  "c.156_163dup": [
    "c.156_163dup",
    "p.Arg55AsnfsX39",
    "295ins8"
  ],
  "p.Arg55AsnfsX39": [
    "c.156_163dup",
    "p.Arg55AsnfsX39",
    "295ins8"
  ],
  "295ins8": [
    "c.156_163dup",
    "p.Arg55AsnfsX39",
    "295ins8"
  ],
  "2335delA": [
    "2335delA",
    "p.Arg735GlyfsX4",
    "c.2203del"
  ],
  "p.Arg735GlyfsX4": [
    "2335delA",
    "p.Arg735GlyfsX4",
    "c.2203del"
  ],
  "c.2203del": [
    "2335delA",
    "p.Arg735GlyfsX4",
    "c.2203del"
  ],
  "c.2425del": [
    "c.2425del",
    "2557delT",
    "p.Ser809GlnfsX12"
  ],
  "2557delT": [
    "c.2425del",
    "2557delT",
    "p.Ser809GlnfsX12"
  ],
  "p.Ser809GlnfsX12": [
    "c.2425del",
    "2557delT",
    "p.Ser809GlnfsX12"
  ],
  "2937_2942delinsTCAGA": [
    "2937_2942delinsTCAGA",
    "c.2805_2810del",
    "p.Pro936_Leu937del"
  ],
  "c.2805_2810del": [
    "2937_2942delinsTCAGA",
    "c.2805_2810del",
    "p.Pro936_Leu937del"
  ],
  "p.Pro936_Leu937del": [
    "2937_2942delinsTCAGA",
    "c.2805_2810del",
    "p.Pro936_Leu937del"
  ],
  "p.Thr940AsnfsX33": [
    "p.Thr940AsnfsX33",
    "c.2819_2823del",
    "2949del5"
  ],
  "c.2819_2823del": [
    "p.Thr940AsnfsX33",
    "c.2819_2823del",
    "2949del5"
  ],
  "2949del5": [
    "p.Thr940AsnfsX33",
    "c.2819_2823del",
    "2949del5"
  ],
  "c.3011del": [
    "c.3011del",
    "3143delC",
    "p.Ala1004ValfsX2"
  ],
  "3143delC": [
    "c.3011del",
    "3143delC",
    "p.Ala1004ValfsX2"
  ],
  "p.Ala1004ValfsX2": [
    "c.3011del",
    "3143delC",
    "p.Ala1004ValfsX2"
  ],
  "p.Leu102ThrfsX9": [
    "p.Leu102ThrfsX9",
    "435insA",
    "c.303dup"
  ],
  "435insA": [
    "p.Leu102ThrfsX9",
    "435insA",
    "c.303dup"
  ],
  "c.303dup": [
    "p.Leu102ThrfsX9",
    "435insA",
    "c.303dup"
  ],
  "556delA": [
    "556delA",
    "c.424del",
    "p.Ile142PhefsX11"
  ],
  "c.424del": [
    "556delA",
    "c.424del",
    "p.Ile142PhefsX11"
  ],
  "p.Ile142PhefsX11": [
    "556delA",
    "c.424del",
    "p.Ile142PhefsX11"
  ],
  "c.49_50delTT": [
    "c.49_50delTT",
    "p.Phe17GlnfsX27",
    "c.49_50del"
  ],
  "p.Phe17GlnfsX27": [
    "c.49_50delTT",
    "p.Phe17GlnfsX27",
    "c.49_50del"
  ],
  "c.49_50del": [
    "c.49_50delTT",
    "p.Phe17GlnfsX27",
    "c.49_50del"
  ],
  "1601delTC": [
    "1601delTC",
    "p.Phe490LeufsX13",
    "c.1470_1471del"
  ],
  "p.Phe490LeufsX13": [
    "1601delTC",
    "p.Phe490LeufsX13",
    "c.1470_1471del"
  ],
  "c.1470_1471del": [
    "1601delTC",
    "p.Phe490LeufsX13",
    "c.1470_1471del"
  ],
  "c.332del": [
    "c.332del",
    "464delC",
    "p.Pro111ArgfsX13"
  ],
  "464delC": [
    "c.332del",
    "464delC",
    "p.Pro111ArgfsX13"
  ],
  "p.Pro111ArgfsX13": [
    "c.332del",
    "464delC",
    "p.Pro111ArgfsX13"
  ],
  "c.3468+5G>A": [
    "p.?",
    "c.3468+5G>A",
    "3600+5G->A"
  ],
  "3600+5G->A": [
    "p.?",
    "c.3468+5G>A",
    "3600+5G->A"
  ],
  "622-1G->C": [
    "622-1G->C",
    "p.?",
    "c.490-1G>C"
  ],
  "c.490-1G>C": [
    "622-1G->C",
    "p.?",
    "c.490-1G>C"
  ],
  "c.3139+1G>A": [
    "c.3139+1G>A",
    "p.?",
    "3271+1G->A"
  ],
  "3271+1G->A": [
    "c.3139+1G>A",
    "p.?",
    "3271+1G->A"
  ],
  "c.3367+1G>A": [
    "c.3367+1G>A",
    "p.?",
    "3499+1G->A"
  ],
  "3499+1G->A": [
    "c.3367+1G>A",
    "p.?",
    "3499+1G->A"
  ],
  "1248+1G->C": [
    "1248+1G->C",
    "p.?",
    "c.1116+1G>C"
  ],
  "c.1116+1G>C": [
    "1248+1G->C",
    "p.?",
    "c.1116+1G>C"
  ],
  "c.1210-1del": [
    "c.1210-1del",
    "p.?",
    "1342-1delG"
  ],
  "1342-1delG": [
    "c.1210-1del",
    "p.?",
    "1342-1delG"
  ],
  "1309delG": [
    "1309delG",
    "c.1177del",
    "p.Val393X"
  ],
  "c.1177del": [
    "1309delG",
    "c.1177del",
    "p.Val393X"
  ],
  "p.Val393X": [
    "1309delG",
    "c.1177del",
    "p.Val393X"
  ],
  "1465_1466insTAAT": [
    "1465_1466insTAAT",
    "c.1333_1334insTAAT",
    "p.Asn445IlefsX38"
  ],
  "c.1333_1334insTAAT": [
    "1465_1466insTAAT",
    "c.1333_1334insTAAT",
    "p.Asn445IlefsX38"
  ],
  "p.Asn445IlefsX38": [
    "1465_1466insTAAT",
    "c.1333_1334insTAAT",
    "p.Asn445IlefsX38"
  ],
  "1289insTA": [
    "1289insTA",
    "c.1157_1158insTA",
    "p.Leu387ThrfsX2"
  ],
  "c.1157_1158insTA": [
    "1289insTA",
    "c.1157_1158insTA",
    "p.Leu387ThrfsX2"
  ],
  "p.Leu387ThrfsX2": [
    "1289insTA",
    "c.1157_1158insTA",
    "p.Leu387ThrfsX2"
  ],
  "c.2089del": [
    "c.2089del",
    "c.2089delA",
    "p.Arg697GlyfsX25"
  ],
  "c.2089delA": [
    "c.2089del",
    "c.2089delA",
    "p.Arg697GlyfsX25"
  ],
  "p.Arg697GlyfsX25": [
    "c.2089del",
    "c.2089delA",
    "p.Arg697GlyfsX25"
  ],
  "3617delGA": [
    "3617delGA",
    "p.Val1163LeufsX2",
    "c.3486_3487del"
  ],
  "p.Val1163LeufsX2": [
    "3617delGA",
    "p.Val1163LeufsX2",
    "c.3486_3487del"
  ],
  "c.3486_3487del": [
    "3617delGA",
    "p.Val1163LeufsX2",
    "c.3486_3487del"
  ],
  "p.Lys14AsnfsX11": [
    "p.Lys14AsnfsX11",
    "c.42del",
    "174delA"
  ],
  "c.42del": [
    "p.Lys14AsnfsX11",
    "c.42del",
    "174delA"
  ],
  "174delA": [
    "p.Lys14AsnfsX11",
    "c.42del",
    "174delA"
  ],
  "p.Val1160X": [
    "p.Val1160X",
    "c.3477del",
    "c.3477delT"
  ],
  "c.3477del": [
    "p.Val1160X",
    "c.3477del",
    "c.3477delT"
  ],
  "c.3477delT": [
    "p.Val1160X",
    "c.3477del",
    "c.3477delT"
  ],
  "1044C>G": [
    "1044C>G",
    "c.912C>G",
    "p.Tyr304X",
    "Y304X"
  ],
  "c.912C>G": [
    "1044C>G",
    "c.912C>G",
    "p.Tyr304X",
    "Y304X"
  ],
  "p.Tyr304X": [
    "c.912delinsGG",
    "c.912delCinsGG",
    "p.Tyr304X"
  ],
  "Y304X": [
    "1044C>G",
    "c.912C>G",
    "p.Tyr304X",
    "Y304X"
  ],
  "c.1114C>T": [
    "c.1114C>T",
    "Q372X",
    "1246C>T",
    "p.Gln372X"
  ],
  "Q372X": [
    "c.1114C>T",
    "Q372X",
    "1246C>T",
    "p.Gln372X"
  ],
  "1246C>T": [
    "c.1114C>T",
    "Q372X",
    "1246C>T",
    "p.Gln372X"
  ],
  "p.Gln372X": [
    "c.1114C>T",
    "Q372X",
    "1246C>T",
    "p.Gln372X"
  ],
  "c.1132C>T": [
    "c.1132C>T",
    "p.Gln378X",
    "Q378X",
    "1264C>T"
  ],
  "p.Gln378X": [
    "c.1132C>T",
    "p.Gln378X",
    "Q378X",
    "1264C>T"
  ],
  "Q378X": [
    "c.1132C>T",
    "p.Gln378X",
    "Q378X",
    "1264C>T"
  ],
  "1264C>T": [
    "c.1132C>T",
    "p.Gln378X",
    "Q378X",
    "1264C>T"
  ],
  "1336G>T": [
    "1336G>T",
    "E402X",
    "c.1204G>T",
    "p.Glu402X"
  ],
  "E402X": [
    "1336G>T",
    "E402X",
    "c.1204G>T",
    "p.Glu402X"
  ],
  "c.1204G>T": [
    "1336G>T",
    "E402X",
    "c.1204G>T",
    "p.Glu402X"
  ],
  "p.Glu402X": [
    "1336G>T",
    "E402X",
    "c.1204G>T",
    "p.Glu402X"
  ],
  "K442X": [
    "K442X",
    "1456A>T",
    "c.1324A>T",
    "p.Lys442X"
  ],
  "1456A>T": [
    "K442X",
    "1456A>T",
    "c.1324A>T",
    "p.Lys442X"
  ],
  "c.1324A>T": [
    "K442X",
    "1456A>T",
    "c.1324A>T",
    "p.Lys442X"
  ],
  "p.Lys442X": [
    "K442X",
    "1456A>T",
    "c.1324A>T",
    "p.Lys442X"
  ],
  "E528X": [
    "E528X",
    "c.1582G>T",
    "p.Glu528X",
    "1714G>T"
  ],
  "c.1582G>T": [
    "E528X",
    "c.1582G>T",
    "p.Glu528X",
    "1714G>T"
  ],
  "p.Glu528X": [
    "E528X",
    "c.1582G>T",
    "p.Glu528X",
    "1714G>T"
  ],
  "1714G>T": [
    "E528X",
    "c.1582G>T",
    "p.Glu528X",
    "1714G>T"
  ],
  "p.Leu568X": [
    "p.Leu568X",
    "1835T>A",
    "L568X",
    "c.1703T>A"
  ],
  "1835T>A": [
    "p.Leu568X",
    "1835T>A",
    "L568X",
    "c.1703T>A"
  ],
  "L568X": [
    "p.Leu568X",
    "1835T>A",
    "L568X",
    "c.1703T>A"
  ],
  "c.1703T>A": [
    "p.Leu568X",
    "1835T>A",
    "L568X",
    "c.1703T>A"
  ],
  "p.Tyr569X": [
    "p.Tyr569X",
    "c.1707T>A",
    "Y569X",
    "1839T>A"
  ],
  "c.1707T>A": [
    "p.Tyr569X",
    "c.1707T>A",
    "Y569X",
    "1839T>A"
  ],
  "Y569X": [
    "p.Tyr569X",
    "c.1707T>A",
    "Y569X",
    "1839T>A"
  ],
  "1839T>A": [
    "p.Tyr569X",
    "c.1707T>A",
    "Y569X",
    "1839T>A"
  ],
  "E588X": [
    "E588X",
    "1894G>T",
    "p.Glu588X",
    "c.1762G>T"
  ],
  "1894G>T": [
    "E588X",
    "1894G>T",
    "p.Glu588X",
    "c.1762G>T"
  ],
  "p.Glu588X": [
    "E588X",
    "1894G>T",
    "p.Glu588X",
    "c.1762G>T"
  ],
  "c.1762G>T": [
    "E588X",
    "1894G>T",
    "p.Glu588X",
    "c.1762G>T"
  ],
  "2111C>A|2111C>G": [
    "2111C>A|2111C>G",
    "S660X",
    "p.Ser660X",
    "c.1979C>A|c.1979C>G"
  ],
  "S660X": [
    "2111C>A|2111C>G",
    "S660X",
    "p.Ser660X",
    "c.1979C>A|c.1979C>G"
  ],
  "p.Ser660X": [
    "2111C>A|2111C>G",
    "S660X",
    "p.Ser660X",
    "c.1979C>A|c.1979C>G"
  ],
  "c.1979C>A|c.1979C>G": [
    "2111C>A|2111C>G",
    "S660X",
    "p.Ser660X",
    "c.1979C>A|c.1979C>G"
  ],
  "c.2062A>T": [
    "c.2062A>T",
    "p.Lys688X",
    "2194A>T",
    "K688X"
  ],
  "p.Lys688X": [
    "c.2062A>T",
    "p.Lys688X",
    "2194A>T",
    "K688X"
  ],
  "2194A>T": [
    "c.2062A>T",
    "p.Lys688X",
    "2194A>T",
    "K688X"
  ],
  "K688X": [
    "c.2062A>T",
    "p.Lys688X",
    "2194A>T",
    "K688X"
  ],
  "Q30X": [
    "Q30X",
    "p.Gln30X",
    "c.88C>T",
    "220C>T"
  ],
  "p.Gln30X": [
    "Q30X",
    "p.Gln30X",
    "c.88C>T",
    "220C>T"
  ],
  "c.88C>T": [
    "Q30X",
    "p.Gln30X",
    "c.88C>T",
    "220C>T"
  ],
  "220C>T": [
    "Q30X",
    "p.Gln30X",
    "c.88C>T",
    "220C>T"
  ],
  "c.2156T>A": [
    "c.2156T>A",
    "p.Leu719X",
    "2288T>A",
    "L719X"
  ],
  "p.Leu719X": [
    "c.2156T>A",
    "p.Leu719X",
    "2288T>A",
    "L719X"
  ],
  "2288T>A": [
    "c.2156T>A",
    "p.Leu719X",
    "2288T>A",
    "L719X"
  ],
  "L719X": [
    "c.2156T>A",
    "p.Leu719X",
    "2288T>A",
    "L719X"
  ],
  "2320G>T": [
    "2320G>T",
    "p.Glu730X",
    "c.2188G>T",
    "E730X"
  ],
  "p.Glu730X": [
    "2320G>T",
    "p.Glu730X",
    "c.2188G>T",
    "E730X"
  ],
  "c.2188G>T": [
    "2320G>T",
    "p.Glu730X",
    "c.2188G>T",
    "E730X"
  ],
  "E730X": [
    "2320G>T",
    "p.Glu730X",
    "c.2188G>T",
    "E730X"
  ],
  "2431C>T": [
    "2431C>T",
    "c.2299C>T",
    "Q767X",
    "p.Gln767X"
  ],
  "c.2299C>T": [
    "2431C>T",
    "c.2299C>T",
    "Q767X",
    "p.Gln767X"
  ],
  "Q767X": [
    "2431C>T",
    "c.2299C>T",
    "Q767X",
    "p.Gln767X"
  ],
  "p.Gln767X": [
    "2431C>T",
    "c.2299C>T",
    "Q767X",
    "p.Gln767X"
  ],
  "p.Gln779X": [
    "p.Gln779X",
    "c.2335C>T",
    "Q779X",
    "2467C>T"
  ],
  "c.2335C>T": [
    "p.Gln779X",
    "c.2335C>T",
    "Q779X",
    "2467C>T"
  ],
  "Q779X": [
    "p.Gln779X",
    "c.2335C>T",
    "Q779X",
    "2467C>T"
  ],
  "2467C>T": [
    "p.Gln779X",
    "c.2335C>T",
    "Q779X",
    "2467C>T"
  ],
  "R810X": [
    "R810X",
    "c.2428A>T",
    "2560A>T",
    "p.Arg810X"
  ],
  "c.2428A>T": [
    "R810X",
    "c.2428A>T",
    "2560A>T",
    "p.Arg810X"
  ],
  "2560A>T": [
    "R810X",
    "c.2428A>T",
    "2560A>T",
    "p.Arg810X"
  ],
  "p.Arg810X": [
    "R810X",
    "c.2428A>T",
    "2560A>T",
    "p.Arg810X"
  ],
  "p.Gln814X": [
    "p.Gln814X",
    "c.2440C>T",
    "Q814X",
    "2572C>T"
  ],
  "c.2440C>T": [
    "p.Gln814X",
    "c.2440C>T",
    "Q814X",
    "2572C>T"
  ],
  "Q814X": [
    "p.Gln814X",
    "c.2440C>T",
    "Q814X",
    "2572C>T"
  ],
  "2572C>T": [
    "p.Gln814X",
    "c.2440C>T",
    "Q814X",
    "2572C>T"
  ],
  "E815X": [
    "E815X",
    "2575G>T",
    "c.2443G>T",
    "p.Glu815X"
  ],
  "2575G>T": [
    "E815X",
    "2575G>T",
    "c.2443G>T",
    "p.Glu815X"
  ],
  "c.2443G>T": [
    "E815X",
    "2575G>T",
    "c.2443G>T",
    "p.Glu815X"
  ],
  "p.Glu815X": [
    "E815X",
    "2575G>T",
    "c.2443G>T",
    "p.Glu815X"
  ],
  "2608G>T": [
    "2608G>T",
    "p.Glu826X",
    "E826X",
    "c.2476G>T"
  ],
  "p.Glu826X": [
    "2608G>T",
    "p.Glu826X",
    "E826X",
    "c.2476G>T"
  ],
  "E826X": [
    "2608G>T",
    "p.Glu826X",
    "E826X",
    "c.2476G>T"
  ],
  "c.2476G>T": [
    "2608G>T",
    "p.Glu826X",
    "E826X",
    "c.2476G>T"
  ],
  "c.2488A>T": [
    "c.2488A>T",
    "p.Lys830X",
    "K830X",
    "2620A>T"
  ],
  "p.Lys830X": [
    "c.2488A>T",
    "p.Lys830X",
    "K830X",
    "2620A>T"
  ],
  "K830X": [
    "c.2488A>T",
    "p.Lys830X",
    "K830X",
    "2620A>T"
  ],
  "2620A>T": [
    "c.2488A>T",
    "p.Lys830X",
    "K830X",
    "2620A>T"
  ],
  "p.Glu56X": [
    "p.Glu56X",
    "c.166G>T",
    "E56X",
    "298G>T"
  ],
  "c.166G>T": [
    "p.Glu56X",
    "c.166G>T",
    "E56X",
    "298G>T"
  ],
  "E56X": [
    "p.Glu56X",
    "c.166G>T",
    "E56X",
    "298G>T"
  ],
  "298G>T": [
    "p.Glu56X",
    "c.166G>T",
    "E56X",
    "298G>T"
  ],
  "G1003X": [
    "G1003X",
    "p.Gly1003X",
    "3139G>T",
    "c.3007G>T"
  ],
  "p.Gly1003X": [
    "G1003X",
    "p.Gly1003X",
    "3139G>T",
    "c.3007G>T"
  ],
  "3139G>T": [
    "G1003X",
    "p.Gly1003X",
    "3139G>T",
    "c.3007G>T"
  ],
  "c.3007G>T": [
    "G1003X",
    "p.Gly1003X",
    "3139G>T",
    "c.3007G>T"
  ],
  "L1011X": [
    "L1011X",
    "c.3032T>G",
    "p.Leu1011X",
    "3164T>G"
  ],
  "c.3032T>G": [
    "L1011X",
    "c.3032T>G",
    "p.Leu1011X",
    "3164T>G"
  ],
  "p.Leu1011X": [
    "L1011X",
    "c.3032T>G",
    "p.Leu1011X",
    "3164T>G"
  ],
  "3164T>G": [
    "L1011X",
    "c.3032T>G",
    "p.Leu1011X",
    "3164T>G"
  ],
  "3678C>G": [
    "3678C>G",
    "Y1182X",
    "c.3546C>G",
    "p.Tyr1182X"
  ],
  "Y1182X": [
    "3678C>G",
    "Y1182X",
    "c.3546C>G",
    "p.Tyr1182X"
  ],
  "c.3546C>G": [
    "3678C>G",
    "Y1182X",
    "c.3546C>G",
    "p.Tyr1182X"
  ],
  "p.Tyr1182X": [
    "3678C>G",
    "Y1182X",
    "c.3546C>G",
    "p.Tyr1182X"
  ],
  "c.253G>T": [
    "c.253G>T",
    "p.Gly85X",
    "385G>T",
    "G85X"
  ],
  "p.Gly85X": [
    "c.253G>T",
    "p.Gly85X",
    "385G>T",
    "G85X"
  ],
  "385G>T": [
    "c.253G>T",
    "p.Gly85X",
    "385G>T",
    "G85X"
  ],
  "G85X": [
    "c.253G>T",
    "p.Gly85X",
    "385G>T",
    "G85X"
  ],
  "p.Gly1247X": [
    "p.Gly1247X",
    "3871G>T",
    "G1247X",
    "c.3739G>T"
  ],
  "3871G>T": [
    "p.Gly1247X",
    "3871G>T",
    "G1247X",
    "c.3739G>T"
  ],
  "G1247X": [
    "p.Gly1247X",
    "3871G>T",
    "G1247X",
    "c.3739G>T"
  ],
  "c.3739G>T": [
    "p.Gly1247X",
    "3871G>T",
    "G1247X",
    "c.3739G>T"
  ],
  "c.3859G>T": [
    "c.3859G>T",
    "p.Gly1287X",
    "3991G>T",
    "G1287X"
  ],
  "p.Gly1287X": [
    "c.3859G>T",
    "p.Gly1287X",
    "3991G>T",
    "G1287X"
  ],
  "3991G>T": [
    "c.3859G>T",
    "p.Gly1287X",
    "3991G>T",
    "G1287X"
  ],
  "G1287X": [
    "c.3859G>T",
    "p.Gly1287X",
    "3991G>T",
    "G1287X"
  ],
  "4053T>A": [
    "4053T>A",
    "Y1307X",
    "c.3921T>A",
    "p.Tyr1307X"
  ],
  "Y1307X": [
    "4053T>A",
    "Y1307X",
    "c.3921T>A",
    "p.Tyr1307X"
  ],
  "c.3921T>A": [
    "4053T>A",
    "Y1307X",
    "c.3921T>A",
    "p.Tyr1307X"
  ],
  "p.Tyr1307X": [
    "4053T>A",
    "Y1307X",
    "c.3921T>A",
    "p.Tyr1307X"
  ],
  "p.Trp1316X": [
    "p.Trp1316X",
    "c.3947G>A",
    "W1316X",
    "4079G>A"
  ],
  "c.3947G>A": [
    "p.Trp1316X",
    "c.3947G>A",
    "W1316X",
    "4079G>A"
  ],
  "W1316X": [
    "p.Trp1316X",
    "c.3947G>A",
    "W1316X",
    "4079G>A"
  ],
  "4079G>A": [
    "p.Trp1316X",
    "c.3947G>A",
    "W1316X",
    "4079G>A"
  ],
  "Y1381X": [
    "Y1381X",
    "4275C>A|4275C>G",
    "c.4143C>A|c.4143C>G",
    "p.Tyr1381X"
  ],
  "4275C>A|4275C>G": [
    "Y1381X",
    "4275C>A|4275C>G",
    "c.4143C>A|c.4143C>G",
    "p.Tyr1381X"
  ],
  "c.4143C>A|c.4143C>G": [
    "Y1381X",
    "4275C>A|4275C>G",
    "c.4143C>A|c.4143C>G",
    "p.Tyr1381X"
  ],
  "p.Tyr1381X": [
    "Y1381X",
    "4275C>A|4275C>G",
    "c.4143C>A|c.4143C>G",
    "p.Tyr1381X"
  ],
  "4333G>T": [
    "4333G>T",
    "c.4201G>T",
    "p.Glu1401X",
    "E1401X"
  ],
  "c.4201G>T": [
    "4333G>T",
    "c.4201G>T",
    "p.Glu1401X",
    "E1401X"
  ],
  "p.Glu1401X": [
    "4333G>T",
    "c.4201G>T",
    "p.Glu1401X",
    "E1401X"
  ],
  "E1401X": [
    "4333G>T",
    "c.4201G>T",
    "p.Glu1401X",
    "E1401X"
  ],
  "Q151X": [
    "Q151X",
    "583C>T",
    "c.451C>T",
    "p.Gln151X"
  ],
  "583C>T": [
    "Q151X",
    "583C>T",
    "c.451C>T",
    "p.Gln151X"
  ],
  "c.451C>T": [
    "Q151X",
    "583C>T",
    "c.451C>T",
    "p.Gln151X"
  ],
  "p.Gln151X": [
    "Q151X",
    "583C>T",
    "c.451C>T",
    "p.Gln151X"
  ],
  "c.(1679+1_1680-1)_(1766+1_1767-1)del": [
    "c.(1679+1_1680-1)_(1766+1_1767-1)del",
    "p.?",
    "CFTRdele12",
    "deletion of exon 12 (legacy numbering)|deletion of exon 13 (current numbering)"
  ],
  "CFTRdele12": [
    "c.(1679+1_1680-1)_(1766+1_1767-1)del",
    "p.?",
    "CFTRdele12",
    "deletion of exon 12 (legacy numbering)|deletion of exon 13 (current numbering)"
  ],
  "deletion of exon 12 (legacy numbering)|deletion of exon 13 (current numbering)": [
    "c.(1679+1_1680-1)_(1766+1_1767-1)del",
    "p.?",
    "CFTRdele12",
    "deletion of exon 12 (legacy numbering)|deletion of exon 13 (current numbering)"
  ],
  "c.(870-1053_870-126)_(1116+186_1117-409)del": [
    "c.(870-1053_870-126)_(1116+186_1117-409)del",
    "p.?",
    "deletion of exon 7 (legacy numbering)|deletion of exon 8 (current numbering)",
    "CFTRdele7"
  ],
  "deletion of exon 7 (legacy numbering)|deletion of exon 8 (current numbering)": [
    "c.(870-1053_870-126)_(1116+186_1117-409)del",
    "p.?",
    "deletion of exon 7 (legacy numbering)|deletion of exon 8 (current numbering)",
    "CFTRdele7"
  ],
  "CFTRdele7": [
    "c.(870-1053_870-126)_(1116+186_1117-409)del",
    "p.?",
    "deletion of exon 7 (legacy numbering)|deletion of exon 8 (current numbering)",
    "CFTRdele7"
  ],
  "deletion of exons 1 through 24 (legacy numbering)|deletion of exons 1 through 27 (current numbering)|deletion of entire CFTR gene": [
    "p.?",
    "deletion of exons 1 through 24 (legacy numbering)|deletion of exons 1 through 27 (current numbering)|deletion of entire CFTR gene",
    "c.(?_-1)_(*1_?)del",
    "CFTRdele1-24"
  ],
  "c.(?_-1)_(*1_?)del": [
    "p.?",
    "deletion of exons 1 through 24 (legacy numbering)|deletion of exons 1 through 27 (current numbering)|deletion of entire CFTR gene",
    "c.(?_-1)_(*1_?)del",
    "CFTRdele1-24"
  ],
  "CFTRdele1-24": [
    "p.?",
    "deletion of exons 1 through 24 (legacy numbering)|deletion of exons 1 through 27 (current numbering)|deletion of entire CFTR gene",
    "c.(?_-1)_(*1_?)del",
    "CFTRdele1-24"
  ],
  "CFTRdele11-18": [
    "CFTRdele11-18",
    "deletion of exons 11 through 18 (legacy numbering)|deletion of exons 12 through 21 (current numbering)",
    "p.?",
    "c.(1584+1_1585-1)_(3468+1_3469-1)del"
  ],
  "deletion of exons 11 through 18 (legacy numbering)|deletion of exons 12 through 21 (current numbering)": [
    "CFTRdele11-18",
    "deletion of exons 11 through 18 (legacy numbering)|deletion of exons 12 through 21 (current numbering)",
    "p.?",
    "c.(1584+1_1585-1)_(3468+1_3469-1)del"
  ],
  "c.(1584+1_1585-1)_(3468+1_3469-1)del": [
    "CFTRdele11-18",
    "deletion of exons 11 through 18 (legacy numbering)|deletion of exons 12 through 21 (current numbering)",
    "p.?",
    "c.(1584+1_1585-1)_(3468+1_3469-1)del"
  ],
  "CFTRdele14a-17b": [
    "CFTRdele14a-17b",
    "c.(2490+1_2491-1)_(3367+1_3368-1)del",
    "p.?",
    "deletion of exons 14a through 17b (legacy numbering)|deletion of exons 15 through 20 (current numbering)"
  ],
  "c.(2490+1_2491-1)_(3367+1_3368-1)del": [
    "CFTRdele14a-17b",
    "c.(2490+1_2491-1)_(3367+1_3368-1)del",
    "p.?",
    "deletion of exons 14a through 17b (legacy numbering)|deletion of exons 15 through 20 (current numbering)"
  ],
  "deletion of exons 14a through 17b (legacy numbering)|deletion of exons 15 through 20 (current numbering)": [
    "CFTRdele14a-17b",
    "c.(2490+1_2491-1)_(3367+1_3368-1)del",
    "p.?",
    "deletion of exons 14a through 17b (legacy numbering)|deletion of exons 15 through 20 (current numbering)"
  ],
  "deletion of exons 16 and 17a (legacy numbering)|deletion of exons 18 and 19 (current numbering)": [
    "deletion of exons 16 and 17a (legacy numbering)|deletion of exons 18 and 19 (current numbering)",
    "c.(2908+1_2909-1)_(3139+1_3140-1)del",
    "p.?",
    "CFTRdele16,17a"
  ],
  "c.(2908+1_2909-1)_(3139+1_3140-1)del": [
    "deletion of exons 16 and 17a (legacy numbering)|deletion of exons 18 and 19 (current numbering)",
    "c.(2908+1_2909-1)_(3139+1_3140-1)del",
    "p.?",
    "CFTRdele16,17a"
  ],
  "CFTRdele16,17a": [
    "deletion of exons 16 and 17a (legacy numbering)|deletion of exons 18 and 19 (current numbering)",
    "c.(2908+1_2909-1)_(3139+1_3140-1)del",
    "p.?",
    "CFTRdele16,17a"
  ],
  "deletion of exons 2 through 6b (legacy numbering)|deletion of exons 2 through 7 (current numbering)": [
    "deletion of exons 2 through 6b (legacy numbering)|deletion of exons 2 through 7 (current numbering)",
    "p.?",
    "CFTRdele2-6b",
    "c.(53+1_54-1)_(869+1_870-1)del"
  ],
  "CFTRdele2-6b": [
    "deletion of exons 2 through 6b (legacy numbering)|deletion of exons 2 through 7 (current numbering)",
    "p.?",
    "CFTRdele2-6b",
    "c.(53+1_54-1)_(869+1_870-1)del"
  ],
  "c.(53+1_54-1)_(869+1_870-1)del": [
    "deletion of exons 2 through 6b (legacy numbering)|deletion of exons 2 through 7 (current numbering)",
    "p.?",
    "CFTRdele2-6b",
    "c.(53+1_54-1)_(869+1_870-1)del"
  ],
  "deletion of exons 9 and 10 (legacy numbering)|deletion of exons 10 and 11 (current numbering)": [
    "deletion of exons 9 and 10 (legacy numbering)|deletion of exons 10 and 11 (current numbering)",
    "c.(1209+1_1210-1)_(1584+1_1585-1)del",
    "CFTRdele9,10",
    "p.?"
  ],
  "c.(1209+1_1210-1)_(1584+1_1585-1)del": [
    "deletion of exons 9 and 10 (legacy numbering)|deletion of exons 10 and 11 (current numbering)",
    "c.(1209+1_1210-1)_(1584+1_1585-1)del",
    "CFTRdele9,10",
    "p.?"
  ],
  "CFTRdele9,10": [
    "deletion of exons 9 and 10 (legacy numbering)|deletion of exons 10 and 11 (current numbering)",
    "c.(1209+1_1210-1)_(1584+1_1585-1)del",
    "CFTRdele9,10",
    "p.?"
  ],
  "duplication of exons 16 and 17a (legacy numbering)|duplication of exons 18 and 19 (current numbering)": [
    "duplication of exons 16 and 17a (legacy numbering)|duplication of exons 18 and 19 (current numbering)",
    "p.?",
    "c.(2908+1_2909-1)_(3139+1_3140-1)dup",
    "CFTRdup16,17a"
  ],
  "c.(2908+1_2909-1)_(3139+1_3140-1)dup": [
    "duplication of exons 16 and 17a (legacy numbering)|duplication of exons 18 and 19 (current numbering)",
    "p.?",
    "c.(2908+1_2909-1)_(3139+1_3140-1)dup",
    "CFTRdup16,17a"
  ],
  "CFTRdup16,17a": [
    "duplication of exons 16 and 17a (legacy numbering)|duplication of exons 18 and 19 (current numbering)",
    "p.?",
    "c.(2908+1_2909-1)_(3139+1_3140-1)dup",
    "CFTRdup16,17a"
  ],
  "duplication of exons 22 through 24 (legacy numbering)|duplication of exons 25 through 27 (current numbering)": [
    "duplication of exons 22 through 24 (legacy numbering)|duplication of exons 25 through 27 (current numbering)",
    "CFTRdup22-24",
    "p.?",
    "c.(3963+1_3964-1)_(*1_?)dup"
  ],
  "CFTRdup22-24": [
    "duplication of exons 22 through 24 (legacy numbering)|duplication of exons 25 through 27 (current numbering)",
    "CFTRdup22-24",
    "p.?",
    "c.(3963+1_3964-1)_(*1_?)dup"
  ],
  "c.(3963+1_3964-1)_(*1_?)dup": [
    "duplication of exons 22 through 24 (legacy numbering)|duplication of exons 25 through 27 (current numbering)",
    "CFTRdup22-24",
    "p.?",
    "c.(3963+1_3964-1)_(*1_?)dup"
  ],
  "CFTRdup6b-16": [
    "CFTRdup6b-16",
    "c.(743+1_744-1)_(2988+1_2989-1)dup",
    "duplication of exons 6b through 16 (legacy numbering)|duplication of exons 6b through 18 (current numbering)",
    "p.?"
  ],
  "c.(743+1_744-1)_(2988+1_2989-1)dup": [
    "CFTRdup6b-16",
    "c.(743+1_744-1)_(2988+1_2989-1)dup",
    "duplication of exons 6b through 16 (legacy numbering)|duplication of exons 6b through 18 (current numbering)",
    "p.?"
  ],
  "duplication of exons 6b through 16 (legacy numbering)|duplication of exons 6b through 18 (current numbering)": [
    "CFTRdup6b-16",
    "c.(743+1_744-1)_(2988+1_2989-1)dup",
    "duplication of exons 6b through 16 (legacy numbering)|duplication of exons 6b through 18 (current numbering)",
    "p.?"
  ],
  "c.1680-2A>C": [
    "c.1680-2A>C",
    "p.?",
    "1812-2A->C"
  ],
  "1812-2A->C": [
    "c.1680-2A>C",
    "p.?",
    "1812-2A->C"
  ],
  "3272-1G->A": [
    "3272-1G->A",
    "p.?",
    "c.3140-1G>A"
  ],
  "c.3140-1G>A": [
    "3272-1G->A",
    "p.?",
    "c.3140-1G>A"
  ],
  "c.1210-1G>C": [
    "c.1210-1G>C",
    "p.?",
    "1342-1G->C"
  ],
  "1342-1G->C": [
    "c.1210-1G>C",
    "p.?",
    "1342-1G->C"
  ],
  "3271+2T->C": [
    "p.?",
    "3271+2T->C",
    "c.3139+2T>C"
  ],
  "c.3139+2T>C": [
    "p.?",
    "3271+2T->C",
    "c.3139+2T>C"
  ],
  "3600+1G->A": [
    "3600+1G->A",
    "c.3468+1G>A",
    "p.?"
  ],
  "c.3468+1G>A": [
    "3600+1G->A",
    "c.3468+1G>A",
    "p.?"
  ],
  "c.489+2T>G": [
    "c.489+2T>G",
    "p.?",
    "621+2T->G"
  ],
  "621+2T->G": [
    "c.489+2T>G",
    "p.?",
    "621+2T->G"
  ],
  "185+2T->C": [
    "185+2T->C",
    "c.53+2T>C",
    "p.?"
  ],
  "c.53+2T>C": [
    "185+2T->C",
    "c.53+2T>C",
    "p.?"
  ],
  "c.579_579+3del": [
    "c.579_579+3del",
    "710del4",
    "p.?"
  ],
  "710del4": [
    "c.579_579+3del",
    "710del4",
    "p.?"
  ],
  "1341+1G->T": [
    "1341+1G->T",
    "c.1209+1G>T",
    "p.?"
  ],
  "c.1209+1G>T": [
    "1341+1G->T",
    "c.1209+1G>T",
    "p.?"
  ],
  "c.53+2T>G": [
    "c.53+2T>G",
    "p.?",
    "185+2T->G"
  ],
  "185+2T->G": [
    "c.53+2T>G",
    "p.?",
    "185+2T->G"
  ],
  "c.273+2T>G": [
    "c.273+2T>G",
    "p.?",
    "405+2T->G"
  ],
  "405+2T->G": [
    "c.273+2T>G",
    "p.?",
    "405+2T->G"
  ],
  "982delA": [
    "982delA",
    "p.Met284X",
    "c.850del"
  ],
  "p.Met284X": [
    "982delA",
    "p.Met284X",
    "c.850del"
  ],
  "c.850del": [
    "982delA",
    "p.Met284X",
    "c.850del"
  ],
  "1058delC": [
    "1058delC",
    "c.927del",
    "p.Phe310SerfsX18"
  ],
  "c.927del": [
    "1058delC",
    "c.927del",
    "p.Phe310SerfsX18"
  ],
  "p.Phe310SerfsX18": [
    "1058delC",
    "c.927del",
    "p.Phe310SerfsX18"
  ],
  "c.393del": [
    "c.393del",
    "p.Phe131LeufsX3",
    "525delT"
  ],
  "p.Phe131LeufsX3": [
    "c.393del",
    "p.Phe131LeufsX3",
    "525delT"
  ],
  "525delT": [
    "c.393del",
    "p.Phe131LeufsX3",
    "525delT"
  ],
  "c.1375_1385del": [
    "c.1375_1385del",
    "p.Ser459ArgfsX19"
  ],
  "p.Ser459ArgfsX19": [
    "c.1375_1385del",
    "p.Ser459ArgfsX19"
  ],
  "284delA": [
    "284delA",
    "p.Lys52AsnfsX39",
    "c.156del"
  ],
  "p.Lys52AsnfsX39": [
    "284delA",
    "p.Lys52AsnfsX39",
    "c.156del"
  ],
  "c.156del": [
    "284delA",
    "p.Lys52AsnfsX39",
    "c.156del"
  ],
  "p.Ile661SerfsX2": [
    "p.Ile661SerfsX2",
    "2113delA",
    "c.1981del"
  ],
  "2113delA": [
    "p.Ile661SerfsX2",
    "2113delA",
    "c.1981del"
  ],
  "c.1981del": [
    "p.Ile661SerfsX2",
    "2113delA",
    "c.1981del"
  ],
  "c.2909del": [
    "c.2909del",
    "3041delG",
    "p.Gly970ValfsX11"
  ],
  "3041delG": [
    "c.2909del",
    "3041delG",
    "p.Gly970ValfsX11"
  ],
  "p.Gly970ValfsX11": [
    "c.2909del",
    "3041delG",
    "p.Gly970ValfsX11"
  ],
  "3396delC": [
    "3396delC",
    "c.3264del",
    "p.Trp1089GlyfsX13"
  ],
  "c.3264del": [
    "3396delC",
    "c.3264del",
    "p.Trp1089GlyfsX13"
  ],
  "p.Trp1089GlyfsX13": [
    "3396delC",
    "c.3264del",
    "p.Trp1089GlyfsX13"
  ],
  "c.3389_3402del": [
    "c.3389_3402del",
    "3521del14",
    "p.Gly1130ValfsX21"
  ],
  "3521del14": [
    "c.3389_3402del",
    "3521del14",
    "p.Gly1130ValfsX21"
  ],
  "p.Gly1130ValfsX21": [
    "c.3389_3402del",
    "3521del14",
    "p.Gly1130ValfsX21"
  ],
  "c.3492dup": [
    "c.3492dup",
    "p.Lys1165X",
    "3622insT"
  ],
  "p.Lys1165X": [
    "c.3493A>T",
    "p.Lys1165X",
    "K1165X",
    "3625A>T"
  ],
  "3622insT": [
    "c.3492dup",
    "p.Lys1165X",
    "3622insT"
  ],
  "489delC": [
    "489delC",
    "p.Ile119MetfsX5",
    "c.357del"
  ],
  "p.Ile119MetfsX5": [
    "489delC",
    "p.Ile119MetfsX5",
    "c.357del"
  ],
  "c.357del": [
    "489delC",
    "p.Ile119MetfsX5",
    "c.357del"
  ],
  "p.Lys1200SerfsX12": [
    "p.Lys1200SerfsX12",
    "3730A->TCT",
    "c.3598delinsTCT"
  ],
  "3730A->TCT": [
    "p.Lys1200SerfsX12",
    "3730A->TCT",
    "c.3598delinsTCT"
  ],
  "c.3598delinsTCT": [
    "p.Lys1200SerfsX12",
    "3730A->TCT",
    "c.3598delinsTCT"
  ],
  "c.548del": [
    "c.548del",
    "680delT",
    "p.Leu183ProfsX6"
  ],
  "680delT": [
    "c.548del",
    "680delT",
    "p.Leu183ProfsX6"
  ],
  "p.Leu183ProfsX6": [
    "c.548del",
    "680delT",
    "p.Leu183ProfsX6"
  ],
  "c.1093_1094del": [
    "c.1093_1094del",
    "1221delCT",
    "p.Leu365TrpfsX16"
  ],
  "1221delCT": [
    "c.1093_1094del",
    "1221delCT",
    "p.Leu365TrpfsX16"
  ],
  "p.Leu365TrpfsX16": [
    "c.1093_1094del",
    "1221delCT",
    "p.Leu365TrpfsX16"
  ],
  "c.1159_1160del": [
    "c.1159_1160del",
    "1291delTT",
    "p.Leu387AsnfsX23"
  ],
  "1291delTT": [
    "c.1159_1160del",
    "1291delTT",
    "p.Leu387AsnfsX23"
  ],
  "p.Leu387AsnfsX23": [
    "c.1159_1160del",
    "1291delTT",
    "p.Leu387AsnfsX23"
  ],
  "1556delT": [
    "1556delT",
    "c.1424del",
    "p.Leu475ArgfsX52"
  ],
  "c.1424del": [
    "1556delT",
    "c.1424del",
    "p.Leu475ArgfsX52"
  ],
  "p.Leu475ArgfsX52": [
    "1556delT",
    "c.1424del",
    "p.Leu475ArgfsX52"
  ],
  "c.1446dup": [
    "c.1446dup",
    "1576insT",
    "p.Lys483X"
  ],
  "1576insT": [
    "c.1446dup",
    "1576insT",
    "p.Lys483X"
  ],
  "p.Lys483X": [
    "c.1446dup",
    "1576insT",
    "p.Lys483X"
  ],
  "1813insC": [
    "1813insC",
    "c.1682dup",
    "p.Val562SerfsX6"
  ],
  "c.1682dup": [
    "1813insC",
    "c.1682dup",
    "p.Val562SerfsX6"
  ],
  "p.Val562SerfsX6": [
    "1813insC",
    "c.1682dup",
    "p.Val562SerfsX6"
  ],
  "c.1786_1787del": [
    "c.1786_1787del",
    "p.Ala596X",
    "1918delGC"
  ],
  "p.Ala596X": [
    "c.1786_1787del",
    "p.Ala596X",
    "1918delGC"
  ],
  "1918delGC": [
    "c.1786_1787del",
    "p.Ala596X",
    "1918delGC"
  ],
  "c.1807delG": [
    "c.1807delG",
    "c.1807del",
    "p.Val603SerfsX8"
  ],
  "c.1807del": [
    "c.1807delG",
    "c.1807del",
    "p.Val603SerfsX8"
  ],
  "p.Val603SerfsX8": [
    "c.1807delG",
    "c.1807del",
    "p.Val603SerfsX8"
  ],
  "p.Ile616AsnfsX6": [
    "p.Ile616AsnfsX6",
    "1978dupA",
    "c.1846dup"
  ],
  "1978dupA": [
    "p.Ile616AsnfsX6",
    "1978dupA",
    "c.1846dup"
  ],
  "c.1846dup": [
    "p.Ile616AsnfsX6",
    "1978dupA",
    "c.1846dup"
  ],
  "p.Ser686TyrfsX36": [
    "p.Ser686TyrfsX36",
    "c.2057_2058delinsA",
    "2189CT->A"
  ],
  "c.2057_2058delinsA": [
    "p.Ser686TyrfsX36",
    "c.2057_2058delinsA",
    "2189CT->A"
  ],
  "2189CT->A": [
    "p.Ser686TyrfsX36",
    "c.2057_2058delinsA",
    "2189CT->A"
  ],
  "c.2148del": [
    "c.2148del",
    "p.Thr717LeufsX5",
    "c.2148delG"
  ],
  "p.Thr717LeufsX5": [
    "c.2148del",
    "p.Thr717LeufsX5",
    "c.2148delG"
  ],
  "c.2148delG": [
    "c.2148del",
    "p.Thr717LeufsX5",
    "c.2148delG"
  ],
  "p.His784SerfsX21": [
    "p.His784SerfsX21",
    "2481-2482insT",
    "c.2349dup"
  ],
  "2481-2482insT": [
    "p.His784SerfsX21",
    "2481-2482insT",
    "c.2349dup"
  ],
  "c.2349dup": [
    "p.His784SerfsX21",
    "2481-2482insT",
    "c.2349dup"
  ],
  "p.Leu859X": [
    "p.Leu859X",
    "c.2576_2588del",
    "2708del13"
  ],
  "c.2576_2588del": [
    "p.Leu859X",
    "c.2576_2588del",
    "2708del13"
  ],
  "2708del13": [
    "p.Leu859X",
    "c.2576_2588del",
    "2708del13"
  ],
  "156insG": [
    "156insG",
    "c.25dup",
    "p.Ala9GlyfsX36"
  ],
  "c.25dup": [
    "156insG",
    "c.25dup",
    "p.Ala9GlyfsX36"
  ],
  "p.Ala9GlyfsX36": [
    "156insG",
    "c.25dup",
    "p.Ala9GlyfsX36"
  ],
  "c.2705del": [
    "c.2705del",
    "p.Ser902ThrfsX4",
    "2837delG"
  ],
  "p.Ser902ThrfsX4": [
    "c.2705del",
    "p.Ser902ThrfsX4",
    "2837delG"
  ],
  "2837delG": [
    "c.2705del",
    "p.Ser902ThrfsX4",
    "2837delG"
  ],
  "2907delTT": [
    "2907delTT",
    "c.2776_2777del",
    "p.Leu926AlafsX48"
  ],
  "c.2776_2777del": [
    "2907delTT",
    "c.2776_2777del",
    "p.Leu926AlafsX48"
  ],
  "p.Leu926AlafsX48": [
    "2907delTT",
    "c.2776_2777del",
    "p.Leu926AlafsX48"
  ],
  "c.2964dup": [
    "c.2964dup",
    "3095insT",
    "p.Leu989SerfsX5"
  ],
  "3095insT": [
    "c.2964dup",
    "3095insT",
    "p.Leu989SerfsX5"
  ],
  "p.Leu989SerfsX5": [
    "c.2964dup",
    "3095insT",
    "p.Leu989SerfsX5"
  ],
  "3293delA": [
    "3293delA",
    "p.His1054LeufsX6",
    "c.3161del"
  ],
  "p.His1054LeufsX6": [
    "3293delA",
    "p.His1054LeufsX6",
    "c.3161del"
  ],
  "c.3161del": [
    "3293delA",
    "p.His1054LeufsX6",
    "c.3161del"
  ],
  "p.Thr1076IlefsX78": [
    "p.Thr1076IlefsX78",
    "c.3227_3231del",
    "3359delCTCTG"
  ],
  "c.3227_3231del": [
    "p.Thr1076IlefsX78",
    "c.3227_3231del",
    "3359delCTCTG"
  ],
  "3359delCTCTG": [
    "p.Thr1076IlefsX78",
    "c.3227_3231del",
    "3359delCTCTG"
  ],
  "3532AC->GTA": [
    "3532AC->GTA",
    "c.3400_3401delinsGTA",
    "p.Thr1134ValfsX22"
  ],
  "c.3400_3401delinsGTA": [
    "3532AC->GTA",
    "c.3400_3401delinsGTA",
    "p.Thr1134ValfsX22"
  ],
  "p.Thr1134ValfsX22": [
    "3532AC->GTA",
    "c.3400_3401delinsGTA",
    "p.Thr1134ValfsX22"
  ],
  "p.Ser1206GlnfsX5": [
    "p.Ser1206GlnfsX5",
    "3747delC",
    "c.3615del"
  ],
  "3747delC": [
    "p.Ser1206GlnfsX5",
    "3747delC",
    "c.3615del"
  ],
  "c.3615del": [
    "p.Ser1206GlnfsX5",
    "3747delC",
    "c.3615del"
  ],
  "c.3932_3933delinsAATATG": [
    "c.3932_3933delinsAATATG",
    "4064-4065delinsAATATG",
    "p.Ser1311LysfsX12"
  ],
  "4064-4065delinsAATATG": [
    "c.3932_3933delinsAATATG",
    "4064-4065delinsAATATG",
    "p.Ser1311LysfsX12"
  ],
  "p.Ser1311LysfsX12": [
    "c.3932_3933delinsAATATG",
    "4064-4065delinsAATATG",
    "p.Ser1311LysfsX12"
  ],
  "c.3976del": [
    "c.3976del",
    "p.Ser1326LeufsX2",
    "4108delT"
  ],
  "p.Ser1326LeufsX2": [
    "c.3976del",
    "p.Ser1326LeufsX2",
    "4108delT"
  ],
  "4108delT": [
    "c.3976del",
    "p.Ser1326LeufsX2",
    "4108delT"
  ],
  "p.Gly1349AlafsX5": [
    "p.Gly1349AlafsX5",
    "c.4046del",
    "4177delG"
  ],
  "c.4046del": [
    "p.Gly1349AlafsX5",
    "c.4046del",
    "4177delG"
  ],
  "4177delG": [
    "p.Gly1349AlafsX5",
    "c.4046del",
    "4177delG"
  ],
  "4222delG": [
    "4222delG",
    "p.Ala1364ArgfsX16",
    "c.4090del"
  ],
  "p.Ala1364ArgfsX16": [
    "4222delG",
    "p.Ala1364ArgfsX16",
    "c.4090del"
  ],
  "c.4090del": [
    "4222delG",
    "p.Ala1364ArgfsX16",
    "c.4090del"
  ],
  "542del7": [
    "542del7",
    "c.410_416del",
    "p.Leu137ProfsX14"
  ],
  "c.410_416del": [
    "542del7",
    "c.410_416del",
    "p.Leu137ProfsX14"
  ],
  "p.Leu137ProfsX14": [
    "542del7",
    "c.410_416del",
    "p.Leu137ProfsX14"
  ],
  "c.522_526del": [
    "c.522_526del",
    "654del5",
    "p.Ile175TyrfsX6"
  ],
  "654del5": [
    "c.522_526del",
    "654del5",
    "p.Ile175TyrfsX6"
  ],
  "p.Ile175TyrfsX6": [
    "c.522_526del",
    "654del5",
    "p.Ile175TyrfsX6"
  ],
  "675del14": [
    "675del14",
    "c.543_556del",
    "p.Ser182GlnfsX6"
  ],
  "c.543_556del": [
    "675del14",
    "c.543_556del",
    "p.Ser182GlnfsX6"
  ],
  "p.Ser182GlnfsX6": [
    "675del14",
    "c.543_556del",
    "p.Ser182GlnfsX6"
  ],
  "c.551_555del": [
    "c.551_555del",
    "c.551_555delTTTCC",
    "p.Leu184GlnfsX7"
  ],
  "c.551_555delTTTCC": [
    "c.551_555del",
    "c.551_555delTTTCC",
    "p.Leu184GlnfsX7"
  ],
  "p.Leu184GlnfsX7": [
    "c.551_555del",
    "c.551_555delTTTCC",
    "p.Leu184GlnfsX7"
  ],
  "p.Gly194AlafsX63": [
    "p.Gly194AlafsX63",
    "c.581_582del",
    "713delGA"
  ],
  "c.581_582del": [
    "p.Gly194AlafsX63",
    "c.581_582del",
    "713delGA"
  ],
  "713delGA": [
    "p.Gly194AlafsX63",
    "c.581_582del",
    "713delGA"
  ],
  "p.Trp202AspfsX55": [
    "p.Trp202AspfsX55",
    "c.604_605delTG",
    "c.604_605del"
  ],
  "c.604_605delTG": [
    "p.Trp202AspfsX55",
    "c.604_605delTG",
    "c.604_605del"
  ],
  "c.604_605del": [
    "p.Trp202AspfsX55",
    "c.604_605delTG",
    "c.604_605del"
  ],
  "c.708dup": [
    "c.708dup",
    "840insT",
    "p.Gln237SerfsX21"
  ],
  "840insT": [
    "c.708dup",
    "840insT",
    "p.Gln237SerfsX21"
  ],
  "p.Gln237SerfsX21": [
    "c.708dup",
    "840insT",
    "p.Gln237SerfsX21"
  ],
  "2655del26": [
    "2655del26",
    "p.Ala842SerfsX45",
    "c.2523_2548del"
  ],
  "p.Ala842SerfsX45": [
    "2655del26",
    "p.Ala842SerfsX45",
    "c.2523_2548del"
  ],
  "c.2523_2548del": [
    "2655del26",
    "p.Ala842SerfsX45",
    "c.2523_2548del"
  ],
  "4160insG": [
    "4160insG",
    "p.Cys1344LeufsX15",
    "c.4028dup"
  ],
  "p.Cys1344LeufsX15": [
    "4160insG",
    "p.Cys1344LeufsX15",
    "c.4028dup"
  ],
  "c.4028dup": [
    "4160insG",
    "p.Cys1344LeufsX15",
    "c.4028dup"
  ],
  "M1L": [
    "M1L",
    "p.?",
    "c.1A>C"
  ],
  "c.1A>C": [
    "M1L",
    "p.?",
    "c.1A>C"
  ],
  "c.1680-1G>C": [
    "c.1680-1G>C",
    "p.?",
    "1812-1G->C"
  ],
  "1812-1G->C": [
    "c.1680-1G>C",
    "p.?",
    "1812-1G->C"
  ],
  "1001+2T->A": [
    "1001+2T->A",
    "p.?",
    "c.869+2T>A"
  ],
  "c.869+2T>A": [
    "1001+2T->A",
    "p.?",
    "c.869+2T>A"
  ],
  "c.3963+1G>T": [
    "p.?",
    "c.3963+1G>T",
    "4095+1G->T"
  ],
  "4095+1G->T": [
    "p.?",
    "c.3963+1G>T",
    "4095+1G->T"
  ],
  "4096-1G->A": [
    "4096-1G->A",
    "p.?",
    "c.3964-1G>A"
  ],
  "c.3964-1G>A": [
    "4096-1G->A",
    "p.?",
    "c.3964-1G>A"
  ],
  "c.2909-1G>C": [
    "c.2909-1G>C",
    "p.?",
    "3041-1G->C"
  ],
  "3041-1G->C": [
    "c.2909-1G>C",
    "p.?",
    "3041-1G->C"
  ],
  "c.3469-1G>C": [
    "c.3469-1G>C",
    "p.?",
    "3601-1G->C"
  ],
  "3601-1G->C": [
    "c.3469-1G>C",
    "p.?",
    "3601-1G->C"
  ],
  "711+2T->C": [
    "711+2T->C",
    "p.?",
    "c.579+2T>C"
  ],
  "c.579+2T>C": [
    "711+2T->C",
    "p.?",
    "c.579+2T>C"
  ],
  "c.869+2T>G": [
    "c.869+2T>G",
    "p.?",
    "1001+2T->G"
  ],
  "1001+2T->G": [
    "c.869+2T>G",
    "p.?",
    "1001+2T->G"
  ],
  "1716+2delT": [
    "1716+2delT",
    "c.1584+2del",
    "p.?"
  ],
  "c.1584+2del": [
    "1716+2delT",
    "c.1584+2del",
    "p.?"
  ],
  "3499+2T->A": [
    "3499+2T->A",
    "p.?",
    "c.3367+2T>A"
  ],
  "c.3367+2T>A": [
    "3499+2T->A",
    "p.?",
    "c.3367+2T>A"
  ],
  "3041-1G->A": [
    "3041-1G->A",
    "c.2909-1G>A",
    "p.?"
  ],
  "c.2909-1G>A": [
    "3041-1G->A",
    "c.2909-1G>A",
    "p.?"
  ],
  "p.Asn1303LysfsX6": [
    "p.Asn1303LysfsX6",
    "4040dupA",
    "c.3908dup"
  ],
  "4040dupA": [
    "p.Asn1303LysfsX6",
    "4040dupA",
    "c.3908dup"
  ],
  "c.3908dup": [
    "p.Asn1303LysfsX6",
    "4040dupA",
    "c.3908dup"
  ],
  "p.Tyr515AlafsX8": [
    "p.Tyr515AlafsX8",
    "c.1543_1555del",
    "1675_1687del13"
  ],
  "c.1543_1555del": [
    "p.Tyr515AlafsX8",
    "c.1543_1555del",
    "1675_1687del13"
  ],
  "1675_1687del13": [
    "p.Tyr515AlafsX8",
    "c.1543_1555del",
    "1675_1687del13"
  ],
  "c.3231_3232delGT": [
    "c.3231_3232delGT",
    "c.3231_3232del",
    "p.Phe1078ProfsX77"
  ],
  "c.3231_3232del": [
    "c.3231_3232delGT",
    "c.3231_3232del",
    "p.Phe1078ProfsX77"
  ],
  "p.Phe1078ProfsX77": [
    "c.3231_3232delGT",
    "c.3231_3232del",
    "p.Phe1078ProfsX77"
  ],
  "c.3322del": [
    "c.3322del",
    "3454delG",
    "p.Val1108SerfsX13"
  ],
  "3454delG": [
    "c.3322del",
    "3454delG",
    "p.Val1108SerfsX13"
  ],
  "p.Val1108SerfsX13": [
    "c.3322del",
    "3454delG",
    "p.Val1108SerfsX13"
  ],
  "p.Leu1279AlafsX22": [
    "p.Leu1279AlafsX22",
    "3967delTT",
    "c.3835_3836del"
  ],
  "3967delTT": [
    "p.Leu1279AlafsX22",
    "3967delTT",
    "c.3835_3836del"
  ],
  "c.3835_3836del": [
    "p.Leu1279AlafsX22",
    "3967delTT",
    "c.3835_3836del"
  ],
  "p.Lys14PhefsX29": [
    "p.Lys14PhefsX29",
    "c.40_44del",
    "c.40_44delAAACT"
  ],
  "c.40_44del": [
    "p.Lys14PhefsX29",
    "c.40_44del",
    "c.40_44delAAACT"
  ],
  "c.40_44delAAACT": [
    "p.Lys14PhefsX29",
    "c.40_44del",
    "c.40_44delAAACT"
  ],
  "c.4028del": [
    "c.4028del",
    "p.Gly1343AlafsX4",
    "c.4028delG"
  ],
  "p.Gly1343AlafsX4": [
    "c.4028del",
    "p.Gly1343AlafsX4",
    "c.4028delG"
  ],
  "c.4028delG": [
    "c.4028del",
    "p.Gly1343AlafsX4",
    "c.4028delG"
  ],
  "c.1608del": [
    "c.1608del",
    "p.Asp537ThrfsX3",
    "c.1608delA"
  ],
  "p.Asp537ThrfsX3": [
    "c.1608del",
    "p.Asp537ThrfsX3",
    "c.1608delA"
  ],
  "c.1608delA": [
    "c.1608del",
    "p.Asp537ThrfsX3",
    "c.1608delA"
  ],
  "p.Leu570ArgfsX17": [
    "p.Leu570ArgfsX17",
    "c.1708_1712del",
    "c.1708_1712delTTATT"
  ],
  "c.1708_1712del": [
    "p.Leu570ArgfsX17",
    "c.1708_1712del",
    "c.1708_1712delTTATT"
  ],
  "c.1708_1712delTTATT": [
    "p.Leu570ArgfsX17",
    "c.1708_1712del",
    "c.1708_1712delTTATT"
  ],
  "1857delT": [
    "1857delT",
    "p.Phe575LeufsX4",
    "c.1725del"
  ],
  "p.Phe575LeufsX4": [
    "p.Phe575LeufsX4",
    "c.1725_1727delinsAT"
  ],
  "c.1725del": [
    "1857delT",
    "p.Phe575LeufsX4",
    "c.1725del"
  ],
  "c.2357dup": [
    "c.2357dup",
    "p.Thr787AspfsX18",
    "c.2357dupA"
  ],
  "p.Thr787AspfsX18": [
    "c.2357dup",
    "p.Thr787AspfsX18",
    "c.2357dupA"
  ],
  "c.2357dupA": [
    "c.2357dup",
    "p.Thr787AspfsX18",
    "c.2357dupA"
  ],
  "p.Tyr109MetfsX15": [
    "p.Tyr109MetfsX15",
    "c.324delC",
    "c.324del"
  ],
  "c.324delC": [
    "p.Tyr109MetfsX15",
    "c.324delC",
    "c.324del"
  ],
  "c.324del": [
    "p.Tyr109MetfsX15",
    "c.324delC",
    "c.324del"
  ],
  "p.Lys1165AsnfsX27": [
    "p.Lys1165AsnfsX27",
    "c.3495delG",
    "c.3495del"
  ],
  "c.3495delG": [
    "p.Lys1165AsnfsX27",
    "c.3495delG",
    "c.3495del"
  ],
  "c.3495del": [
    "p.Lys1165AsnfsX27",
    "c.3495delG",
    "c.3495del"
  ],
  "538insAC": [
    "538insAC",
    "c.405_406dup",
    "p.Leu136HisfsX18"
  ],
  "c.405_406dup": [
    "538insAC",
    "c.405_406dup",
    "p.Leu136HisfsX18"
  ],
  "p.Leu136HisfsX18": [
    "538insAC",
    "c.405_406dup",
    "p.Leu136HisfsX18"
  ],
  "c.433del": [
    "c.433del",
    "p.Leu145PhefsX8",
    "565delC"
  ],
  "p.Leu145PhefsX8": [
    "c.433del",
    "p.Leu145PhefsX8",
    "565delC"
  ],
  "565delC": [
    "c.433del",
    "p.Leu145PhefsX8",
    "565delC"
  ],
  "c.494del": [
    "c.494del",
    "624delT",
    "p.Leu165X"
  ],
  "624delT": [
    "c.494del",
    "624delT",
    "p.Leu165X"
  ],
  "p.Leu165X": [
    "626T>A",
    "c.494T>A",
    "p.Leu165X",
    "L165X"
  ],
  "p.Glu407AsnfsX35": [
    "p.Glu407AsnfsX35",
    "c.1219del",
    "c.1219delG"
  ],
  "c.1219del": [
    "p.Glu407AsnfsX35",
    "c.1219del",
    "c.1219delG"
  ],
  "c.1219delG": [
    "p.Glu407AsnfsX35",
    "c.1219del",
    "c.1219delG"
  ],
  "p.Ser478X": [
    "p.Ser478X",
    "c.1433_1434del",
    "1565delCA"
  ],
  "c.1433_1434del": [
    "p.Ser478X",
    "c.1433_1434del",
    "1565delCA"
  ],
  "1565delCA": [
    "p.Ser478X",
    "c.1433_1434del",
    "1565delCA"
  ],
  "p.Val510PhefsX17": [
    "p.Val510PhefsX17",
    "c.1528del",
    "1660delG"
  ],
  "c.1528del": [
    "p.Val510PhefsX17",
    "c.1528del",
    "1660delG"
  ],
  "1660delG": [
    "p.Val510PhefsX17",
    "c.1528del",
    "1660delG"
  ],
  "p.Asp572LeufsX16": [
    "p.Asp572LeufsX16",
    "c.1714_1715del",
    "1845delAG/1846delGA"
  ],
  "c.1714_1715del": [
    "p.Asp572LeufsX16",
    "c.1714_1715del",
    "1845delAG/1846delGA"
  ],
  "1845delAG/1846delGA": [
    "p.Asp572LeufsX16",
    "c.1714_1715del",
    "1845delAG/1846delGA"
  ],
  "c.1853_1863del": [
    "c.1853_1863del",
    "p.Ile618ArgfsX2"
  ],
  "p.Ile618ArgfsX2": [
    "c.1853_1863del",
    "p.Ile618ArgfsX2"
  ],
  "p.Thr682LysfsX40": [
    "p.Thr682LysfsX40",
    "c.2045delC",
    "c.2045del"
  ],
  "c.2045delC": [
    "p.Thr682LysfsX40",
    "c.2045delC",
    "c.2045del"
  ],
  "c.2045del": [
    "p.Thr682LysfsX40",
    "c.2045delC",
    "c.2045del"
  ],
  "c.2274_2275delinsT": [
    "c.2274_2275delinsT",
    "p.Thr760ArgfsX11",
    "2406_2407delinsT"
  ],
  "p.Thr760ArgfsX11": [
    "2409delC",
    "c.2277del",
    "p.Thr760ArgfsX11"
  ],
  "2406_2407delinsT": [
    "c.2274_2275delinsT",
    "p.Thr760ArgfsX11",
    "2406_2407delinsT"
  ],
  "p.Gln779LysfsX24": [
    "p.Gln779LysfsX24",
    "c.2335del",
    "2466delC"
  ],
  "c.2335del": [
    "p.Gln779LysfsX24",
    "c.2335del",
    "2466delC"
  ],
  "2466delC": [
    "p.Gln779LysfsX24",
    "c.2335del",
    "2466delC"
  ],
  "p.Gln781PhefsX20": [
    "p.Gln781PhefsX20",
    "c.2340_2346del",
    "2472_2478del7"
  ],
  "c.2340_2346del": [
    "p.Gln781PhefsX20",
    "c.2340_2346del",
    "2472_2478del7"
  ],
  "2472_2478del7": [
    "p.Gln781PhefsX20",
    "c.2340_2346del",
    "2472_2478del7"
  ],
  "c.2879_2882del": [
    "c.2879_2882del",
    "c.2879_2882delCTAT",
    "p.Pro960ArgfsX7"
  ],
  "c.2879_2882delCTAT": [
    "c.2879_2882del",
    "c.2879_2882delCTAT",
    "p.Pro960ArgfsX7"
  ],
  "p.Pro960ArgfsX7": [
    "c.2879_2882del",
    "c.2879_2882delCTAT",
    "p.Pro960ArgfsX7"
  ],
  "c.3180delA": [
    "c.3180delA",
    "c.3180del",
    "p.Gly1061AspfsX22"
  ],
  "c.3180del": [
    "c.3180delA",
    "c.3180del",
    "p.Gly1061AspfsX22"
  ],
  "p.Gly1061AspfsX22": [
    "c.3180delA",
    "c.3180del",
    "p.Gly1061AspfsX22"
  ],
  "c.3325delA": [
    "c.3325delA",
    "c.3325del",
    "p.Ile1109SerfsX12"
  ],
  "c.3325del": [
    "c.3325delA",
    "c.3325del",
    "p.Ile1109SerfsX12"
  ],
  "p.Ile1109SerfsX12": [
    "p.Ile1109SerfsX12",
    "c.3324del",
    "3456delC"
  ],
  "p.Leu1143ValfsX14": [
    "p.Leu1143ValfsX14",
    "c.3426_3427insGTAA"
  ],
  "c.3426_3427insGTAA": [
    "p.Leu1143ValfsX14",
    "c.3426_3427insGTAA"
  ],
  "4332delTG": [
    "4332delTG",
    "p.Cys1400X",
    "c.4200_4201del"
  ],
  "c.4200_4201del": [
    "4332delTG",
    "p.Cys1400X",
    "c.4200_4201del"
  ],
  "c.4delC": [
    "c.4delC",
    "p.Gln2ArgfsX23",
    "c.4del"
  ],
  "p.Gln2ArgfsX23": [
    "c.4delC",
    "p.Gln2ArgfsX23",
    "c.4del"
  ],
  "c.4del": [
    "c.4delC",
    "p.Gln2ArgfsX23",
    "c.4del"
  ],
  "p.Tyr275ThrfsX10": [
    "p.Tyr275ThrfsX10",
    "c.822del",
    "954delA"
  ],
  "c.822del": [
    "p.Tyr275ThrfsX10",
    "c.822del",
    "954delA"
  ],
  "954delA": [
    "p.Tyr275ThrfsX10",
    "c.822del",
    "954delA"
  ],
  "c.1312dupA": [
    "c.1312dupA",
    "c.1312dup",
    "p.Thr438AsnfsX8"
  ],
  "c.1312dup": [
    "c.1312dupA",
    "c.1312dup",
    "p.Thr438AsnfsX8"
  ],
  "p.Thr438AsnfsX8": [
    "c.1312dupA",
    "c.1312dup",
    "p.Thr438AsnfsX8"
  ],
  "c.1573del": [
    "c.1573del",
    "p.Gln525AsnfsX2",
    "c.1573delC"
  ],
  "p.Gln525AsnfsX2": [
    "c.1573del",
    "p.Gln525AsnfsX2",
    "c.1573delC"
  ],
  "c.1573delC": [
    "c.1573del",
    "p.Gln525AsnfsX2",
    "c.1573delC"
  ],
  "p.Pro936GlnfsX6": [
    "p.Pro936GlnfsX6",
    "c.2805_2810delinsTCAGA"
  ],
  "c.2805_2810delinsTCAGA": [
    "p.Pro936GlnfsX6",
    "c.2805_2810delinsTCAGA"
  ],
  "c.2929_2930insA": [
    "c.2929_2930insA",
    "p.Ser977TyrfsX9",
    "3061insA"
  ],
  "p.Ser977TyrfsX9": [
    "c.2929_2930insA",
    "p.Ser977TyrfsX9",
    "3061insA"
  ],
  "3061insA": [
    "c.2929_2930insA",
    "p.Ser977TyrfsX9",
    "3061insA"
  ],
  "c.3525_3537del": [
    "c.3525_3537del",
    "p.Thr1176AsnfsX12"
  ],
  "p.Thr1176AsnfsX12": [
    "c.3525_3537del",
    "p.Thr1176AsnfsX12"
  ],
  "p.Gly1208AlafsX3": [
    "3755delG",
    "p.Gly1208AlafsX3",
    "c.3623del"
  ],
  "3750delA": [
    "p.Gly1208AlafsX3",
    "3750delA",
    "c.3618del"
  ],
  "c.3618del": [
    "p.Gly1208AlafsX3",
    "3750delA",
    "c.3618del"
  ],
  "3755delG": [
    "3755delG",
    "p.Gly1208AlafsX3",
    "c.3623del"
  ],
  "c.3623del": [
    "3755delG",
    "p.Gly1208AlafsX3",
    "c.3623del"
  ],
  "p.Asn186LysfsX3": [
    "p.Asn186LysfsX3",
    "c.558del",
    "690delC"
  ],
  "c.558del": [
    "p.Asn186LysfsX3",
    "c.558del",
    "690delC"
  ],
  "690delC": [
    "p.Asn186LysfsX3",
    "c.558del",
    "690delC"
  ],
  "L240X": [
    "p.Leu240X",
    "L240X",
    "c.714del"
  ],
  "c.714del": [
    "p.Leu240X",
    "L240X",
    "c.714del"
  ],
  "c.775delinsGCTGGGAAGAT": [
    "c.775delinsGCTGGGAAGAT",
    "p.Leu259AlafsX12"
  ],
  "p.Leu259AlafsX12": [
    "c.775delinsGCTGGGAAGAT",
    "p.Leu259AlafsX12"
  ],
  "M1I": [
    "M1I",
    "p.?",
    "c.3G>A"
  ],
  "c.3G>A": [
    "M1I",
    "p.?",
    "c.3G>A"
  ],
  "L320X": [
    "L320X",
    "p.Leu320X",
    "c.959T>A",
    "1091T>A"
  ],
  "p.Leu320X": [
    "L320X",
    "p.Leu320X",
    "c.959T>A",
    "1091T>A"
  ],
  "c.959T>A": [
    "L320X",
    "p.Leu320X",
    "c.959T>A",
    "1091T>A"
  ],
  "1091T>A": [
    "L320X",
    "p.Leu320X",
    "c.959T>A",
    "1091T>A"
  ],
  "K329X": [
    "K329X",
    "1117A>T",
    "p.Lys329X",
    "c.985A>T"
  ],
  "1117A>T": [
    "K329X",
    "1117A>T",
    "p.Lys329X",
    "c.985A>T"
  ],
  "p.Lys329X": [
    "K329X",
    "1117A>T",
    "p.Lys329X",
    "c.985A>T"
  ],
  "c.985A>T": [
    "K329X",
    "1117A>T",
    "p.Lys329X",
    "c.985A>T"
  ],
  "1258C>T": [
    "1258C>T",
    "c.1126C>T",
    "p.Gln376X",
    "Q376X"
  ],
  "c.1126C>T": [
    "1258C>T",
    "c.1126C>T",
    "p.Gln376X",
    "Q376X"
  ],
  "p.Gln376X": [
    "1258C>T",
    "c.1126C>T",
    "p.Gln376X",
    "Q376X"
  ],
  "Q376X": [
    "1258C>T",
    "c.1126C>T",
    "p.Gln376X",
    "Q376X"
  ],
  "Q452X": [
    "Q452X",
    "1486C>T",
    "c.1354C>T",
    "p.Gln452X"
  ],
  "1486C>T": [
    "Q452X",
    "1486C>T",
    "c.1354C>T",
    "p.Gln452X"
  ],
  "c.1354C>T": [
    "Q452X",
    "1486C>T",
    "c.1354C>T",
    "p.Gln452X"
  ],
  "p.Gln452X": [
    "Q452X",
    "1486C>T",
    "c.1354C>T",
    "p.Gln452X"
  ],
  "E479X": [
    "E479X",
    "p.Glu479X",
    "c.1435G>T",
    "1567G>T"
  ],
  "p.Glu479X": [
    "E479X",
    "p.Glu479X",
    "c.1435G>T",
    "1567G>T"
  ],
  "c.1435G>T": [
    "E479X",
    "p.Glu479X",
    "c.1435G>T",
    "1567G>T"
  ],
  "1567G>T": [
    "E479X",
    "p.Glu479X",
    "c.1435G>T",
    "1567G>T"
  ],
  "p.Glu504X": [
    "p.Glu504X",
    "E504X",
    "1642G>T",
    "c.1510G>T"
  ],
  "E504X": [
    "p.Glu504X",
    "E504X",
    "1642G>T",
    "c.1510G>T"
  ],
  "1642G>T": [
    "p.Glu504X",
    "E504X",
    "1642G>T",
    "c.1510G>T"
  ],
  "c.1510G>T": [
    "p.Glu504X",
    "E504X",
    "1642G>T",
    "c.1510G>T"
  ],
  "Y517X": [
    "Y517X",
    "1683C>A|1683C>G",
    "p.Tyr517X",
    "c.1551C>A|c.1551C>G"
  ],
  "1683C>A|1683C>G": [
    "Y517X",
    "1683C>A|1683C>G",
    "p.Tyr517X",
    "c.1551C>A|c.1551C>G"
  ],
  "p.Tyr517X": [
    "Y517X",
    "1683C>A|1683C>G",
    "p.Tyr517X",
    "c.1551C>A|c.1551C>G"
  ],
  "c.1551C>A|c.1551C>G": [
    "Y517X",
    "1683C>A|1683C>G",
    "p.Tyr517X",
    "c.1551C>A|c.1551C>G"
  ],
  "E527X": [
    "E527X",
    "c.1579G>T",
    "1711G>T",
    "p.Glu527X"
  ],
  "c.1579G>T": [
    "E527X",
    "c.1579G>T",
    "1711G>T",
    "p.Glu527X"
  ],
  "1711G>T": [
    "E527X",
    "c.1579G>T",
    "1711G>T",
    "p.Glu527X"
  ],
  "p.Glu527X": [
    "E527X",
    "c.1579G>T",
    "1711G>T",
    "p.Glu527X"
  ],
  "c.40A>T": [
    "c.40A>T",
    "K14X",
    "p.Lys14X",
    "172A>T"
  ],
  "K14X": [
    "c.40A>T",
    "K14X",
    "p.Lys14X",
    "172A>T"
  ],
  "p.Lys14X": [
    "c.40A>T",
    "K14X",
    "p.Lys14X",
    "172A>T"
  ],
  "172A>T": [
    "c.40A>T",
    "K14X",
    "p.Lys14X",
    "172A>T"
  ],
  "p.Lys536X": [
    "p.Lys536X",
    "c.1606A>T",
    "K536X",
    "1738A>T"
  ],
  "c.1606A>T": [
    "p.Lys536X",
    "c.1606A>T",
    "K536X",
    "1738A>T"
  ],
  "K536X": [
    "p.Lys536X",
    "c.1606A>T",
    "K536X",
    "1738A>T"
  ],
  "1738A>T": [
    "p.Lys536X",
    "c.1606A>T",
    "K536X",
    "1738A>T"
  ],
  "R555X": [
    "R555X",
    "c.1663A>T",
    "p.Arg555X",
    "1795A>T"
  ],
  "c.1663A>T": [
    "R555X",
    "c.1663A>T",
    "p.Arg555X",
    "1795A>T"
  ],
  "p.Arg555X": [
    "R555X",
    "c.1663A>T",
    "p.Arg555X",
    "1795A>T"
  ],
  "1795A>T": [
    "R555X",
    "c.1663A>T",
    "p.Arg555X",
    "1795A>T"
  ],
  "L570X": [
    "L570X",
    "p.Leu570X",
    "1841T>A",
    "c.1709T>A"
  ],
  "p.Leu570X": [
    "L570X",
    "p.Leu570X",
    "1841T>A",
    "c.1709T>A"
  ],
  "1841T>A": [
    "L570X",
    "p.Leu570X",
    "1841T>A",
    "c.1709T>A"
  ],
  "c.1709T>A": [
    "L570X",
    "p.Leu570X",
    "1841T>A",
    "c.1709T>A"
  ],
  "p.Leu581X": [
    "p.Leu581X",
    "c.1742T>A",
    "1874T>A",
    "L581X"
  ],
  "c.1742T>A": [
    "p.Leu581X",
    "c.1742T>A",
    "1874T>A",
    "L581X"
  ],
  "1874T>A": [
    "p.Leu581X",
    "c.1742T>A",
    "1874T>A",
    "L581X"
  ],
  "L581X": [
    "p.Leu581X",
    "c.1742T>A",
    "1874T>A",
    "L581X"
  ],
  "2024C>G": [
    "2024C>G",
    "p.Ser631X",
    "S631X",
    "c.1892C>G"
  ],
  "p.Ser631X": [
    "2024C>G",
    "p.Ser631X",
    "S631X",
    "c.1892C>G"
  ],
  "S631X": [
    "2024C>G",
    "p.Ser631X",
    "S631X",
    "c.1892C>G"
  ],
  "c.1892C>G": [
    "2024C>G",
    "p.Ser631X",
    "S631X",
    "c.1892C>G"
  ],
  "c.1900C>T": [
    "c.1900C>T",
    "Q634X",
    "2032C>T",
    "p.Gln634X"
  ],
  "Q634X": [
    "c.1900C>T",
    "Q634X",
    "2032C>T",
    "p.Gln634X"
  ],
  "2032C>T": [
    "c.1900C>T",
    "Q634X",
    "2032C>T",
    "p.Gln634X"
  ],
  "p.Gln634X": [
    "c.1900C>T",
    "Q634X",
    "2032C>T",
    "p.Gln634X"
  ],
  "p.Arg657X": [
    "p.Arg657X",
    "2101A>T",
    "c.1969A>T",
    "R657X"
  ],
  "2101A>T": [
    "p.Arg657X",
    "2101A>T",
    "c.1969A>T",
    "R657X"
  ],
  "c.1969A>T": [
    "p.Arg657X",
    "2101A>T",
    "c.1969A>T",
    "R657X"
  ],
  "R657X": [
    "p.Arg657X",
    "2101A>T",
    "c.1969A>T",
    "R657X"
  ],
  "p.Glu692X": [
    "p.Glu692X",
    "c.2074G>T",
    "E692X",
    "2206G>T"
  ],
  "c.2074G>T": [
    "p.Glu692X",
    "c.2074G>T",
    "E692X",
    "2206G>T"
  ],
  "E692X": [
    "p.Glu692X",
    "c.2074G>T",
    "E692X",
    "2206G>T"
  ],
  "2206G>T": [
    "p.Glu692X",
    "c.2074G>T",
    "E692X",
    "2206G>T"
  ],
  "c.114C>G": [
    "c.114C>G",
    "246C>G",
    "Y38X",
    "p.Tyr38X"
  ],
  "246C>G": [
    "c.114C>G",
    "246C>G",
    "Y38X",
    "p.Tyr38X"
  ],
  "Y38X": [
    "c.114C>G",
    "246C>G",
    "Y38X",
    "p.Tyr38X"
  ],
  "p.Tyr38X": [
    "c.114C>G",
    "246C>G",
    "Y38X",
    "p.Tyr38X"
  ],
  "2527C>T": [
    "2527C>T",
    "Q799X",
    "c.2395C>T",
    "p.Gln799X"
  ],
  "Q799X": [
    "2527C>T",
    "Q799X",
    "c.2395C>T",
    "p.Gln799X"
  ],
  "c.2395C>T": [
    "2527C>T",
    "Q799X",
    "c.2395C>T",
    "p.Gln799X"
  ],
  "p.Gln799X": [
    "2527C>T",
    "Q799X",
    "c.2395C>T",
    "p.Gln799X"
  ],
  "2567T>A": [
    "2567T>A",
    "c.2435T>A",
    "p.Leu812X",
    "L812X"
  ],
  "c.2435T>A": [
    "2567T>A",
    "c.2435T>A",
    "p.Leu812X",
    "L812X"
  ],
  "p.Leu812X": [
    "2567T>A",
    "c.2435T>A",
    "p.Leu812X",
    "L812X"
  ],
  "L812X": [
    "2567T>A",
    "c.2435T>A",
    "p.Leu812X",
    "L812X"
  ],
  "c.154A>T": [
    "c.154A>T",
    "p.Lys52X",
    "K52X",
    "286A>T"
  ],
  "p.Lys52X": [
    "c.154A>T",
    "p.Lys52X",
    "K52X",
    "286A>T"
  ],
  "K52X": [
    "c.154A>T",
    "p.Lys52X",
    "K52X",
    "286A>T"
  ],
  "286A>T": [
    "c.154A>T",
    "p.Lys52X",
    "K52X",
    "286A>T"
  ],
  "292G>T": [
    "292G>T",
    "c.160G>T",
    "p.Glu54X",
    "E54X"
  ],
  "c.160G>T": [
    "292G>T",
    "c.160G>T",
    "p.Glu54X",
    "E54X"
  ],
  "p.Glu54X": [
    "292G>T",
    "c.160G>T",
    "p.Glu54X",
    "E54X"
  ],
  "E54X": [
    "292G>T",
    "c.160G>T",
    "p.Glu54X",
    "E54X"
  ],
  "K946X": [
    "K946X",
    "c.2836A>T",
    "p.Lys946X",
    "2968A>T"
  ],
  "c.2836A>T": [
    "K946X",
    "c.2836A>T",
    "p.Lys946X",
    "2968A>T"
  ],
  "p.Lys946X": [
    "K946X",
    "c.2836A>T",
    "p.Lys946X",
    "2968A>T"
  ],
  "2968A>T": [
    "K946X",
    "c.2836A>T",
    "p.Lys946X",
    "2968A>T"
  ],
  "p.Lys951X": [
    "p.Lys951X",
    "2983A>T",
    "K951X",
    "c.2851A>T"
  ],
  "2983A>T": [
    "p.Lys951X",
    "2983A>T",
    "K951X",
    "c.2851A>T"
  ],
  "K951X": [
    "p.Lys951X",
    "2983A>T",
    "K951X",
    "c.2851A>T"
  ],
  "c.2851A>T": [
    "p.Lys951X",
    "2983A>T",
    "K951X",
    "c.2851A>T"
  ],
  "3118C>T": [
    "3118C>T",
    "p.Gln996X",
    "Q996X",
    "c.2986C>T"
  ],
  "p.Gln996X": [
    "3118C>T",
    "p.Gln996X",
    "Q996X",
    "c.2986C>T"
  ],
  "Q996X": [
    "3118C>T",
    "p.Gln996X",
    "Q996X",
    "c.2986C>T"
  ],
  "c.2986C>T": [
    "3118C>T",
    "p.Gln996X",
    "Q996X",
    "c.2986C>T"
  ],
  "3166C>T": [
    "3166C>T",
    "p.Gln1012X",
    "c.3034C>T",
    "Q1012X"
  ],
  "p.Gln1012X": [
    "3166C>T",
    "p.Gln1012X",
    "c.3034C>T",
    "Q1012X"
  ],
  "c.3034C>T": [
    "3166C>T",
    "p.Gln1012X",
    "c.3034C>T",
    "Q1012X"
  ],
  "Q1012X": [
    "3166C>T",
    "p.Gln1012X",
    "c.3034C>T",
    "Q1012X"
  ],
  "3242C>A": [
    "3242C>A",
    "c.3110C>A",
    "S1037X",
    "p.Ser1037X"
  ],
  "c.3110C>A": [
    "3242C>A",
    "c.3110C>A",
    "S1037X",
    "p.Ser1037X"
  ],
  "S1037X": [
    "3242C>A",
    "c.3110C>A",
    "S1037X",
    "p.Ser1037X"
  ],
  "p.Ser1037X": [
    "3242C>A",
    "c.3110C>A",
    "S1037X",
    "p.Ser1037X"
  ],
  "c.3112C>T": [
    "c.3112C>T",
    "p.Gln1038X",
    "Q1038X",
    "3244C>T"
  ],
  "p.Gln1038X": [
    "c.3112C>T",
    "p.Gln1038X",
    "Q1038X",
    "3244C>T"
  ],
  "Q1038X": [
    "c.3112C>T",
    "p.Gln1038X",
    "Q1038X",
    "3244C>T"
  ],
  "3244C>T": [
    "c.3112C>T",
    "p.Gln1038X",
    "Q1038X",
    "3244C>T"
  ],
  "3262G>T": [
    "3262G>T",
    "c.3130G>T",
    "E1044X",
    "p.Glu1044X"
  ],
  "c.3130G>T": [
    "3262G>T",
    "c.3130G>T",
    "E1044X",
    "p.Glu1044X"
  ],
  "E1044X": [
    "3262G>T",
    "c.3130G>T",
    "E1044X",
    "p.Glu1044X"
  ],
  "p.Glu1044X": [
    "3262G>T",
    "c.3130G>T",
    "E1044X",
    "p.Glu1044X"
  ],
  "p.Glu1046X": [
    "p.Glu1046X",
    "c.3136G>T",
    "E1046X",
    "3268G>T"
  ],
  "c.3136G>T": [
    "p.Glu1046X",
    "c.3136G>T",
    "E1046X",
    "3268G>T"
  ],
  "E1046X": [
    "p.Glu1046X",
    "c.3136G>T",
    "E1046X",
    "3268G>T"
  ],
  "3268G>T": [
    "p.Glu1046X",
    "c.3136G>T",
    "E1046X",
    "3268G>T"
  ],
  "p.Leu1059X": [
    "p.Leu1059X",
    "3308T>G",
    "L1059X",
    "c.3176T>G"
  ],
  "3308T>G": [
    "p.Leu1059X",
    "3308T>G",
    "L1059X",
    "c.3176T>G"
  ],
  "L1059X": [
    "p.Leu1059X",
    "3308T>G",
    "L1059X",
    "c.3176T>G"
  ],
  "c.3176T>G": [
    "p.Leu1059X",
    "3308T>G",
    "L1059X",
    "c.3176T>G"
  ],
  "Q1100X": [
    "Q1100X",
    "p.Gln1100X",
    "c.3298C>T",
    "3430C>T"
  ],
  "p.Gln1100X": [
    "Q1100X",
    "p.Gln1100X",
    "c.3298C>T",
    "3430C>T"
  ],
  "c.3298C>T": [
    "Q1100X",
    "p.Gln1100X",
    "c.3298C>T",
    "3430C>T"
  ],
  "3430C>T": [
    "Q1100X",
    "p.Gln1100X",
    "c.3298C>T",
    "3430C>T"
  ],
  "c.3493A>T": [
    "c.3493A>T",
    "p.Lys1165X",
    "K1165X",
    "3625A>T"
  ],
  "K1165X": [
    "c.3493A>T",
    "p.Lys1165X",
    "K1165X",
    "3625A>T"
  ],
  "3625A>T": [
    "c.3493A>T",
    "p.Lys1165X",
    "K1165X",
    "3625A>T"
  ],
  "3665C>A|3665C>G": [
    "3665C>A|3665C>G",
    "p.Ser1178X",
    "c.3533C>A|c.3533C>G",
    "S1178X"
  ],
  "p.Ser1178X": [
    "3665C>A|3665C>G",
    "p.Ser1178X",
    "c.3533C>A|c.3533C>G",
    "S1178X"
  ],
  "c.3533C>A|c.3533C>G": [
    "3665C>A|3665C>G",
    "p.Ser1178X",
    "c.3533C>A|c.3533C>G",
    "S1178X"
  ],
  "S1178X": [
    "3665C>A|3665C>G",
    "p.Ser1178X",
    "c.3533C>A|c.3533C>G",
    "S1178X"
  ],
  "3688C>T": [
    "3688C>T",
    "p.Gln1186X",
    "Q1186X",
    "c.3556C>T"
  ],
  "p.Gln1186X": [
    "3688C>T",
    "p.Gln1186X",
    "Q1186X",
    "c.3556C>T"
  ],
  "Q1186X": [
    "3688C>T",
    "p.Gln1186X",
    "Q1186X",
    "c.3556C>T"
  ],
  "c.3556C>T": [
    "3688C>T",
    "p.Gln1186X",
    "Q1186X",
    "c.3556C>T"
  ],
  "c.3728T>A": [
    "c.3728T>A",
    "L1243X",
    "3860T>A",
    "p.Leu1243X"
  ],
  "L1243X": [
    "c.3728T>A",
    "L1243X",
    "3860T>A",
    "p.Leu1243X"
  ],
  "3860T>A": [
    "c.3728T>A",
    "L1243X",
    "3860T>A",
    "p.Leu1243X"
  ],
  "p.Leu1243X": [
    "c.3728T>A",
    "L1243X",
    "3860T>A",
    "p.Leu1243X"
  ],
  "3905T>A": [
    "3905T>A",
    "c.3773T>A",
    "L1253X",
    "p.Leu1253X"
  ],
  "c.3773T>A": [
    "3905T>A",
    "c.3773T>A",
    "L1253X",
    "p.Leu1253X"
  ],
  "L1253X": [
    "3905T>A",
    "c.3773T>A",
    "L1253X",
    "p.Leu1253X"
  ],
  "p.Leu1253X": [
    "3905T>A",
    "c.3773T>A",
    "L1253X",
    "p.Leu1253X"
  ],
  "K1351X": [
    "K1351X",
    "c.4051A>T",
    "p.Lys1351X",
    "4183A>T"
  ],
  "c.4051A>T": [
    "K1351X",
    "c.4051A>T",
    "p.Lys1351X",
    "4183A>T"
  ],
  "p.Lys1351X": [
    "K1351X",
    "c.4051A>T",
    "p.Lys1351X",
    "4183A>T"
  ],
  "4183A>T": [
    "K1351X",
    "c.4051A>T",
    "p.Lys1351X",
    "4183A>T"
  ],
  "4332T>A": [
    "4332T>A",
    "c.4200T>A",
    "p.Cys1400X",
    "C1400X"
  ],
  "c.4200T>A": [
    "4332T>A",
    "c.4200T>A",
    "p.Cys1400X",
    "C1400X"
  ],
  "C1400X": [
    "4332T>A",
    "c.4200T>A",
    "p.Cys1400X",
    "C1400X"
  ],
  "c.4225G>T": [
    "c.4225G>T",
    "4357G>T",
    "E1409X",
    "p.Glu1409X"
  ],
  "4357G>T": [
    "c.4225G>T",
    "4357G>T",
    "E1409X",
    "p.Glu1409X"
  ],
  "E1409X": [
    "c.4225G>T",
    "4357G>T",
    "E1409X",
    "p.Glu1409X"
  ],
  "p.Glu1409X": [
    "c.4225G>T",
    "4357G>T",
    "E1409X",
    "p.Glu1409X"
  ],
  "p.Cys1410X": [
    "p.Cys1410X",
    "4362C>A",
    "c.4230C>A",
    "C1410X"
  ],
  "4362C>A": [
    "p.Cys1410X",
    "4362C>A",
    "c.4230C>A",
    "C1410X"
  ],
  "c.4230C>A": [
    "p.Cys1410X",
    "4362C>A",
    "c.4230C>A",
    "C1410X"
  ],
  "C1410X": [
    "p.Cys1410X",
    "4362C>A",
    "c.4230C>A",
    "C1410X"
  ],
  "442A>T": [
    "442A>T",
    "c.310A>T",
    "p.Arg104X",
    "R104X"
  ],
  "c.310A>T": [
    "442A>T",
    "c.310A>T",
    "p.Arg104X",
    "R104X"
  ],
  "p.Arg104X": [
    "442A>T",
    "c.310A>T",
    "p.Arg104X",
    "R104X"
  ],
  "R104X": [
    "442A>T",
    "c.310A>T",
    "p.Arg104X",
    "R104X"
  ],
  "472A>T": [
    "472A>T",
    "p.Lys114X",
    "K114X",
    "c.340A>T"
  ],
  "p.Lys114X": [
    "472A>T",
    "p.Lys114X",
    "K114X",
    "c.340A>T"
  ],
  "K114X": [
    "472A>T",
    "p.Lys114X",
    "K114X",
    "c.340A>T"
  ],
  "c.340A>T": [
    "472A>T",
    "p.Lys114X",
    "K114X",
    "c.340A>T"
  ],
  "L159X": [
    "L159X",
    "c.476T>A",
    "608T>A",
    "p.Leu159X"
  ],
  "c.476T>A": [
    "L159X",
    "c.476T>A",
    "608T>A",
    "p.Leu159X"
  ],
  "608T>A": [
    "L159X",
    "c.476T>A",
    "608T>A",
    "p.Leu159X"
  ],
  "p.Leu159X": [
    "L159X",
    "c.476T>A",
    "608T>A",
    "p.Leu159X"
  ],
  "626T>A": [
    "626T>A",
    "c.494T>A",
    "p.Leu165X",
    "L165X"
  ],
  "c.494T>A": [
    "626T>A",
    "c.494T>A",
    "p.Leu165X",
    "L165X"
  ],
  "L165X": [
    "626T>A",
    "c.494T>A",
    "p.Leu165X",
    "L165X"
  ],
  "841C>T": [
    "841C>T",
    "p.Gln237X",
    "c.709C>T",
    "Q237X"
  ],
  "p.Gln237X": [
    "841C>T",
    "p.Gln237X",
    "c.709C>T",
    "Q237X"
  ],
  "c.709C>T": [
    "841C>T",
    "p.Gln237X",
    "c.709C>T",
    "Q237X"
  ],
  "Q237X": [
    "841C>T",
    "p.Gln237X",
    "c.709C>T",
    "Q237X"
  ],
  "Y247X": [
    "Y247X",
    "p.Tyr247X",
    "873C>G|873C>A",
    "c.741C>G|c.741C>A"
  ],
  "p.Tyr247X": [
    "Y247X",
    "p.Tyr247X",
    "873C>G|873C>A",
    "c.741C>G|c.741C>A"
  ],
  "873C>G|873C>A": [
    "Y247X",
    "p.Tyr247X",
    "873C>G|873C>A",
    "c.741C>G|c.741C>A"
  ],
  "c.741C>G|c.741C>A": [
    "Y247X",
    "p.Tyr247X",
    "873C>G|873C>A",
    "c.741C>G|c.741C>A"
  ],
  "Q250X": [
    "Q250X",
    "880C>T",
    "p.Gln250X",
    "c.748C>T"
  ],
  "880C>T": [
    "Q250X",
    "880C>T",
    "p.Gln250X",
    "c.748C>T"
  ],
  "p.Gln250X": [
    "Q250X",
    "880C>T",
    "p.Gln250X",
    "c.748C>T"
  ],
  "c.748C>T": [
    "Q250X",
    "880C>T",
    "p.Gln250X",
    "c.748C>T"
  ],
  "c.808C>T": [
    "c.808C>T",
    "940C>T",
    "p.Gln270X",
    "Q270X"
  ],
  "940C>T": [
    "c.808C>T",
    "940C>T",
    "p.Gln270X",
    "Q270X"
  ],
  "p.Gln270X": [
    "c.808C>T",
    "940C>T",
    "p.Gln270X",
    "Q270X"
  ],
  "Q270X": [
    "c.808C>T",
    "940C>T",
    "p.Gln270X",
    "Q270X"
  ],
  "967G>T": [
    "967G>T",
    "E279X",
    "c.835G>T",
    "p.Glu279X"
  ],
  "E279X": [
    "967G>T",
    "E279X",
    "c.835G>T",
    "p.Glu279X"
  ],
  "c.835G>T": [
    "967G>T",
    "E279X",
    "c.835G>T",
    "p.Glu279X"
  ],
  "p.Glu279X": [
    "967G>T",
    "E279X",
    "c.835G>T",
    "p.Glu279X"
  ],
  "R289X": [
    "R289X",
    "997A>T",
    "p.Arg289X",
    "c.865A>T"
  ],
  "997A>T": [
    "R289X",
    "997A>T",
    "p.Arg289X",
    "c.865A>T"
  ],
  "p.Arg289X": [
    "R289X",
    "997A>T",
    "p.Arg289X",
    "c.865A>T"
  ],
  "c.865A>T": [
    "R289X",
    "997A>T",
    "p.Arg289X",
    "c.865A>T"
  ],
  "CFTRdele13": [
    "CFTRdele13",
    "c.(1766+1_1767-1)_(2490+1_2491-1)del",
    "p.?",
    "deletion of exon 13 (legacy numbering)|deletion of exon 14 (current numbering)"
  ],
  "c.(1766+1_1767-1)_(2490+1_2491-1)del": [
    "CFTRdele13",
    "c.(1766+1_1767-1)_(2490+1_2491-1)del",
    "p.?",
    "deletion of exon 13 (legacy numbering)|deletion of exon 14 (current numbering)"
  ],
  "deletion of exon 13 (legacy numbering)|deletion of exon 14 (current numbering)": [
    "CFTRdele13",
    "c.(1766+1_1767-1)_(2490+1_2491-1)del",
    "p.?",
    "deletion of exon 13 (legacy numbering)|deletion of exon 14 (current numbering)"
  ],
  "CFTRdele14b": [
    "CFTRdele14b",
    "p.?",
    "deletion of exon 14b (legacy numbering)|deletion of exon 16 (current numbering)",
    "c.(2619+1_2620-1)_(2657+1_2658-1)del"
  ],
  "deletion of exon 14b (legacy numbering)|deletion of exon 16 (current numbering)": [
    "CFTRdele14b",
    "p.?",
    "deletion of exon 14b (legacy numbering)|deletion of exon 16 (current numbering)",
    "c.(2619+1_2620-1)_(2657+1_2658-1)del"
  ],
  "c.(2619+1_2620-1)_(2657+1_2658-1)del": [
    "CFTRdele14b",
    "p.?",
    "deletion of exon 14b (legacy numbering)|deletion of exon 16 (current numbering)",
    "c.(2619+1_2620-1)_(2657+1_2658-1)del"
  ],
  "CFTRdele23": [
    "CFTRdele23",
    "deletion of exon 23 (legacy numbering)|deletion of exon 26 (current numbering)",
    "p.?",
    "c.(4136+1_4137-1)_(4242+1_4243-1)del"
  ],
  "deletion of exon 23 (legacy numbering)|deletion of exon 26 (current numbering)": [
    "CFTRdele23",
    "deletion of exon 23 (legacy numbering)|deletion of exon 26 (current numbering)",
    "p.?",
    "c.(4136+1_4137-1)_(4242+1_4243-1)del"
  ],
  "c.(4136+1_4137-1)_(4242+1_4243-1)del": [
    "CFTRdele23",
    "deletion of exon 23 (legacy numbering)|deletion of exon 26 (current numbering)",
    "p.?",
    "c.(4136+1_4137-1)_(4242+1_4243-1)del"
  ],
  "c.(743+1_744-1)_(869+1_870-1)del": [
    "c.(743+1_744-1)_(869+1_870-1)del",
    "p.?",
    "deletion of exon 6b (legacy numbering)|deletion of exon 7 (current numbering)",
    "CFTRdele6b"
  ],
  "deletion of exon 6b (legacy numbering)|deletion of exon 7 (current numbering)": [
    "c.(743+1_744-1)_(869+1_870-1)del",
    "p.?",
    "deletion of exon 6b (legacy numbering)|deletion of exon 7 (current numbering)",
    "CFTRdele6b"
  ],
  "CFTRdele6b": [
    "c.(743+1_744-1)_(869+1_870-1)del",
    "p.?",
    "deletion of exon 6b (legacy numbering)|deletion of exon 7 (current numbering)",
    "CFTRdele6b"
  ],
  "CFTRdele1,10": [
    "CFTRdele1,10",
    "deletion of exons 1 and 10 (legacy numbering)|deletion of exons 1 and 11 (current numbering)",
    "p.?",
    "c.[(?_1)_(53+1_54-1)del;(1392+1_1393-1)_(1584+1_1585-1)del]"
  ],
  "deletion of exons 1 and 10 (legacy numbering)|deletion of exons 1 and 11 (current numbering)": [
    "CFTRdele1,10",
    "deletion of exons 1 and 10 (legacy numbering)|deletion of exons 1 and 11 (current numbering)",
    "p.?",
    "c.[(?_1)_(53+1_54-1)del;(1392+1_1393-1)_(1584+1_1585-1)del]"
  ],
  "c.[(?_1)_(53+1_54-1)del;(1392+1_1393-1)_(1584+1_1585-1)del]": [
    "CFTRdele1,10",
    "deletion of exons 1 and 10 (legacy numbering)|deletion of exons 1 and 11 (current numbering)",
    "p.?",
    "c.[(?_1)_(53+1_54-1)del;(1392+1_1393-1)_(1584+1_1585-1)del]"
  ],
  "c.[(?_1)_(53+1_54-1)del;(1584+1_1585-1)_(*1_?)del]": [
    "c.[(?_1)_(53+1_54-1)del;(1584+1_1585-1)_(*1_?)del]",
    "deletion of exons 1 and 11 through 24 (legacy numbering)|deletion of exons 1 and 12 through 27 (current numbering)",
    "p.?",
    "CFTRdele1,11-24"
  ],
  "deletion of exons 1 and 11 through 24 (legacy numbering)|deletion of exons 1 and 12 through 27 (current numbering)": [
    "c.[(?_1)_(53+1_54-1)del;(1584+1_1585-1)_(*1_?)del]",
    "deletion of exons 1 and 11 through 24 (legacy numbering)|deletion of exons 1 and 12 through 27 (current numbering)",
    "p.?",
    "CFTRdele1,11-24"
  ],
  "CFTRdele1,11-24": [
    "c.[(?_1)_(53+1_54-1)del;(1584+1_1585-1)_(*1_?)del]",
    "deletion of exons 1 and 11 through 24 (legacy numbering)|deletion of exons 1 and 12 through 27 (current numbering)",
    "p.?",
    "CFTRdele1,11-24"
  ],
  "CFTRdele11-15,17a,17b": [
    "CFTRdele11-15,17a,17b",
    "p.?",
    "deletion of exons 11 through 15, 17a, and 17b (legacy numbering)|deletion of exons 12-17, 19, and 20 (current numbering)",
    "c.[(1584+1_1585-1)_(2908+1_2909-1)del;(2988+1_2989-1)_(3367+1_3368-1)del]"
  ],
  "deletion of exons 11 through 15, 17a, and 17b (legacy numbering)|deletion of exons 12-17, 19, and 20 (current numbering)": [
    "CFTRdele11-15,17a,17b",
    "p.?",
    "deletion of exons 11 through 15, 17a, and 17b (legacy numbering)|deletion of exons 12-17, 19, and 20 (current numbering)",
    "c.[(1584+1_1585-1)_(2908+1_2909-1)del;(2988+1_2989-1)_(3367+1_3368-1)del]"
  ],
  "c.[(1584+1_1585-1)_(2908+1_2909-1)del;(2988+1_2989-1)_(3367+1_3368-1)del]": [
    "CFTRdele11-15,17a,17b",
    "p.?",
    "deletion of exons 11 through 15, 17a, and 17b (legacy numbering)|deletion of exons 12-17, 19, and 20 (current numbering)",
    "c.[(1584+1_1585-1)_(2908+1_2909-1)del;(2988+1_2989-1)_(3367+1_3368-1)del]"
  ],
  "c.[(1679+1_1680-1)_(2490+1_2491-1)del;(2908+1_2909-1)_(2988+1_2909-1)del]": [
    "p.?",
    "c.[(1679+1_1680-1)_(2490+1_2491-1)del;(2908+1_2909-1)_(2988+1_2909-1)del]",
    "deletion of exons 12, 13, and 16 (legacy numbering)|deletion of exons 13, 14, and 18 (current numbering)",
    "CFTRdele12,13,16"
  ],
  "deletion of exons 12, 13, and 16 (legacy numbering)|deletion of exons 13, 14, and 18 (current numbering)": [
    "p.?",
    "c.[(1679+1_1680-1)_(2490+1_2491-1)del;(2908+1_2909-1)_(2988+1_2909-1)del]",
    "deletion of exons 12, 13, and 16 (legacy numbering)|deletion of exons 13, 14, and 18 (current numbering)",
    "CFTRdele12,13,16"
  ],
  "CFTRdele12,13,16": [
    "p.?",
    "c.[(1679+1_1680-1)_(2490+1_2491-1)del;(2908+1_2909-1)_(2988+1_2909-1)del]",
    "deletion of exons 12, 13, and 16 (legacy numbering)|deletion of exons 13, 14, and 18 (current numbering)",
    "CFTRdele12,13,16"
  ],
  "CFTRdele14b-20": [
    "CFTRdele14b-20",
    "p.?",
    "deletion of exons 14b through 20 (legacy numbering)|deletion of exons 16 through 23 (current numbering)",
    "c.(2619+1_2620-1)_(3873+1_3874-1)del"
  ],
  "deletion of exons 14b through 20 (legacy numbering)|deletion of exons 16 through 23 (current numbering)": [
    "CFTRdele14b-20",
    "p.?",
    "deletion of exons 14b through 20 (legacy numbering)|deletion of exons 16 through 23 (current numbering)",
    "c.(2619+1_2620-1)_(3873+1_3874-1)del"
  ],
  "c.(2619+1_2620-1)_(3873+1_3874-1)del": [
    "CFTRdele14b-20",
    "p.?",
    "deletion of exons 14b through 20 (legacy numbering)|deletion of exons 16 through 23 (current numbering)",
    "c.(2619+1_2620-1)_(3873+1_3874-1)del"
  ],
  "deletion of exons 16 through 17b (legacy numbering)|deletion of exons 18 through 20 (current numbering)": [
    "deletion of exons 16 through 17b (legacy numbering)|deletion of exons 18 through 20 (current numbering)",
    "IVS15+1085_IVS17B+260del7201",
    "c.2908+1085_3367+260del",
    "p.?"
  ],
  "IVS15+1085_IVS17B+260del7201": [
    "deletion of exons 16 through 17b (legacy numbering)|deletion of exons 18 through 20 (current numbering)",
    "IVS15+1085_IVS17B+260del7201",
    "c.2908+1085_3367+260del",
    "p.?"
  ],
  "c.2908+1085_3367+260del": [
    "deletion of exons 16 through 17b (legacy numbering)|deletion of exons 18 through 20 (current numbering)",
    "IVS15+1085_IVS17B+260del7201",
    "c.2908+1085_3367+260del",
    "p.?"
  ],
  "c.(2908+1_2909-15)_(3468+10_3469-1)del": [
    "c.(2908+1_2909-15)_(3468+10_3469-1)del",
    "p.?",
    "deletion of exons 16 through 18 (legacy numbering)|deletion of exons 16 through 21 (current numbering)",
    "CFTRdele16-18"
  ],
  "deletion of exons 16 through 18 (legacy numbering)|deletion of exons 16 through 21 (current numbering)": [
    "c.(2908+1_2909-15)_(3468+10_3469-1)del",
    "p.?",
    "deletion of exons 16 through 18 (legacy numbering)|deletion of exons 16 through 21 (current numbering)",
    "CFTRdele16-18"
  ],
  "CFTRdele16-18": [
    "c.(2908+1_2909-15)_(3468+10_3469-1)del",
    "p.?",
    "deletion of exons 16 through 18 (legacy numbering)|deletion of exons 16 through 21 (current numbering)",
    "CFTRdele16-18"
  ],
  "CFTRdele18-24": [
    "CFTRdele18-24",
    "c.(3367+1_3368-1)_(*1_?)del",
    "p.?",
    "deletion of exons 18 through 24 (legacy numbering)|deletion of exons 21 through 27 (current numbering)"
  ],
  "c.(3367+1_3368-1)_(*1_?)del": [
    "CFTRdele18-24",
    "c.(3367+1_3368-1)_(*1_?)del",
    "p.?",
    "deletion of exons 18 through 24 (legacy numbering)|deletion of exons 21 through 27 (current numbering)"
  ],
  "deletion of exons 18 through 24 (legacy numbering)|deletion of exons 21 through 27 (current numbering)": [
    "CFTRdele18-24",
    "c.(3367+1_3368-1)_(*1_?)del",
    "p.?",
    "deletion of exons 18 through 24 (legacy numbering)|deletion of exons 21 through 27 (current numbering)"
  ],
  "deletion of exons 19 through 24 (legacy numbering)|deletion of exons 22 through 27 (current numbering)": [
    "deletion of exons 19 through 24 (legacy numbering)|deletion of exons 22 through 27 (current numbering)",
    "CFTRdele19-24",
    "c.(3468+1_3469-1)_(*1_?)del",
    "p.?"
  ],
  "CFTRdele19-24": [
    "deletion of exons 19 through 24 (legacy numbering)|deletion of exons 22 through 27 (current numbering)",
    "CFTRdele19-24",
    "c.(3468+1_3469-1)_(*1_?)del",
    "p.?"
  ],
  "c.(3468+1_3469-1)_(*1_?)del": [
    "deletion of exons 19 through 24 (legacy numbering)|deletion of exons 22 through 27 (current numbering)",
    "CFTRdele19-24",
    "c.(3468+1_3469-1)_(*1_?)del",
    "p.?"
  ],
  "c.(53+1_54-1)_(4136+1_4137-1)del": [
    "p.?",
    "c.(53+1_54-1)_(4136+1_4137-1)del",
    "deletion of exons 2 through 22 (legacy numbering)|deletion of exons 2 through 25 (current numbering)",
    "CFTRdele2-22"
  ],
  "deletion of exons 2 through 22 (legacy numbering)|deletion of exons 2 through 25 (current numbering)": [
    "p.?",
    "c.(53+1_54-1)_(4136+1_4137-1)del",
    "deletion of exons 2 through 22 (legacy numbering)|deletion of exons 2 through 25 (current numbering)",
    "CFTRdele2-22"
  ],
  "CFTRdele2-22": [
    "p.?",
    "c.(53+1_54-1)_(4136+1_4137-1)del",
    "deletion of exons 2 through 22 (legacy numbering)|deletion of exons 2 through 25 (current numbering)",
    "CFTRdele2-22"
  ],
  "CFTRdele2-7": [
    "CFTRdele2-7",
    "deletion of exons 2 through 7 (legacy numbering)|deletion of exons 2 through 8 (current numbering)",
    "p.?",
    "c.(53+1_54-1)_(1116+1_1117-1)del"
  ],
  "deletion of exons 2 through 7 (legacy numbering)|deletion of exons 2 through 8 (current numbering)": [
    "CFTRdele2-7",
    "deletion of exons 2 through 7 (legacy numbering)|deletion of exons 2 through 8 (current numbering)",
    "p.?",
    "c.(53+1_54-1)_(1116+1_1117-1)del"
  ],
  "c.(53+1_54-1)_(1116+1_1117-1)del": [
    "CFTRdele2-7",
    "deletion of exons 2 through 7 (legacy numbering)|deletion of exons 2 through 8 (current numbering)",
    "p.?",
    "c.(53+1_54-1)_(1116+1_1117-1)del"
  ],
  "CFTRdele2-8": [
    "CFTRdele2-8",
    "deletion of exons 2 through 8 (legacy numbering)|deletion of exons 2 through 9 (current numbering)",
    "c.(53+1_54-1)_(1209+1_1210-1)del",
    "p.?"
  ],
  "deletion of exons 2 through 8 (legacy numbering)|deletion of exons 2 through 9 (current numbering)": [
    "CFTRdele2-8",
    "deletion of exons 2 through 8 (legacy numbering)|deletion of exons 2 through 9 (current numbering)",
    "c.(53+1_54-1)_(1209+1_1210-1)del",
    "p.?"
  ],
  "c.(53+1_54-1)_(1209+1_1210-1)del": [
    "CFTRdele2-8",
    "deletion of exons 2 through 8 (legacy numbering)|deletion of exons 2 through 9 (current numbering)",
    "c.(53+1_54-1)_(1209+1_1210-1)del",
    "p.?"
  ],
  "deletion of exons 2 through 9 (legacy numbering)|deletion of exons 2 through 10 (current numbering)": [
    "deletion of exons 2 through 9 (legacy numbering)|deletion of exons 2 through 10 (current numbering)",
    "CFTRdele2-9",
    "p.?",
    "c.53+9713_1392+2669del"
  ],
  "CFTRdele2-9": [
    "deletion of exons 2 through 9 (legacy numbering)|deletion of exons 2 through 10 (current numbering)",
    "CFTRdele2-9",
    "p.?",
    "c.53+9713_1392+2669del"
  ],
  "c.53+9713_1392+2669del": [
    "deletion of exons 2 through 9 (legacy numbering)|deletion of exons 2 through 10 (current numbering)",
    "CFTRdele2-9",
    "p.?",
    "c.53+9713_1392+2669del"
  ],
  "deletion of exons 2, 3, and 10 (legacy numbering)|deletion of exons 2, 3, and 11 (current numbering)": [
    "deletion of exons 2, 3, and 10 (legacy numbering)|deletion of exons 2, 3, and 11 (current numbering)",
    "p.?",
    "c.[(53+1_54)_(273_274-1)del;(1392+1_1393-1)_(1584+1_1585-1)del]",
    "CFTRdele2,3,10"
  ],
  "c.[(53+1_54)_(273_274-1)del;(1392+1_1393-1)_(1584+1_1585-1)del]": [
    "deletion of exons 2, 3, and 10 (legacy numbering)|deletion of exons 2, 3, and 11 (current numbering)",
    "p.?",
    "c.[(53+1_54)_(273_274-1)del;(1392+1_1393-1)_(1584+1_1585-1)del]",
    "CFTRdele2,3,10"
  ],
  "CFTRdele2,3,10": [
    "deletion of exons 2, 3, and 10 (legacy numbering)|deletion of exons 2, 3, and 11 (current numbering)",
    "p.?",
    "c.[(53+1_54)_(273_274-1)del;(1392+1_1393-1)_(1584+1_1585-1)del]",
    "CFTRdele2,3,10"
  ],
  "c.(3717+1_3718-1)_(4242+1_4243-1)del": [
    "c.(3717+1_3718-1)_(4242+1_4243-1)del",
    "p.?",
    "CFTRdele20-23",
    "deletion of exons 20 through 23 (legacy numbering)|deletion of exons 23 through 26 (current numbering)"
  ],
  "CFTRdele20-23": [
    "c.(3717+1_3718-1)_(4242+1_4243-1)del",
    "p.?",
    "CFTRdele20-23",
    "deletion of exons 20 through 23 (legacy numbering)|deletion of exons 23 through 26 (current numbering)"
  ],
  "deletion of exons 20 through 23 (legacy numbering)|deletion of exons 23 through 26 (current numbering)": [
    "c.(3717+1_3718-1)_(4242+1_4243-1)del",
    "p.?",
    "CFTRdele20-23",
    "deletion of exons 20 through 23 (legacy numbering)|deletion of exons 23 through 26 (current numbering)"
  ],
  "c.(4136+1_4137-1)_(*1_?)del": [
    "p.?",
    "c.(4136+1_4137-1)_(*1_?)del",
    "CFTRdele23,24",
    "deletion of exons 23 and 24 (legacy numbering)|deletion of exons 26 and 27 (current numbering)"
  ],
  "CFTRdele23,24": [
    "p.?",
    "c.(4136+1_4137-1)_(*1_?)del",
    "CFTRdele23,24",
    "deletion of exons 23 and 24 (legacy numbering)|deletion of exons 26 and 27 (current numbering)"
  ],
  "deletion of exons 23 and 24 (legacy numbering)|deletion of exons 26 and 27 (current numbering)": [
    "p.?",
    "c.(4136+1_4137-1)_(*1_?)del",
    "CFTRdele23,24",
    "deletion of exons 23 and 24 (legacy numbering)|deletion of exons 26 and 27 (current numbering)"
  ],
  "c.(489+1_490-1)_(743+1_744-1)del": [
    "c.(489+1_490-1)_(743+1_744-1)del",
    "CFTRdele5,6a",
    "p.?",
    "deletion of exons 5 and 6a (legacy numbering)|deletion of exons 5 and 6 (current numbering)"
  ],
  "CFTRdele5,6a": [
    "c.(489+1_490-1)_(743+1_744-1)del",
    "CFTRdele5,6a",
    "p.?",
    "deletion of exons 5 and 6a (legacy numbering)|deletion of exons 5 and 6 (current numbering)"
  ],
  "deletion of exons 5 and 6a (legacy numbering)|deletion of exons 5 and 6 (current numbering)": [
    "c.(489+1_490-1)_(743+1_744-1)del",
    "CFTRdele5,6a",
    "p.?",
    "deletion of exons 5 and 6a (legacy numbering)|deletion of exons 5 and 6 (current numbering)"
  ],
  "deletion of exons 7 and 8 (legacy numbering)|deletion of exons 8 and 9 (current numbering)": [
    "deletion of exons 7 and 8 (legacy numbering)|deletion of exons 8 and 9 (current numbering)",
    "p.?",
    "c.(870-1053_870-126)_(1209+1_1210-1)del",
    "CFTRdele7,8"
  ],
  "c.(870-1053_870-126)_(1209+1_1210-1)del": [
    "deletion of exons 7 and 8 (legacy numbering)|deletion of exons 8 and 9 (current numbering)",
    "p.?",
    "c.(870-1053_870-126)_(1209+1_1210-1)del",
    "CFTRdele7,8"
  ],
  "CFTRdele7,8": [
    "deletion of exons 7 and 8 (legacy numbering)|deletion of exons 8 and 9 (current numbering)",
    "p.?",
    "c.(870-1053_870-126)_(1209+1_1210-1)del",
    "CFTRdele7,8"
  ],
  "deletion of part of the promoter through exon 9 (legacy numbering)|deletion of part of the promoter through exon 10 (current numbering)": [
    "p.?",
    "deletion of part of the promoter through exon 9 (legacy numbering)|deletion of part of the promoter through exon 10 (current numbering)",
    "CFTRdelePr-9",
    "c.(?_1)_(1392+1_1393-1)del"
  ],
  "CFTRdelePr-9": [
    "p.?",
    "deletion of part of the promoter through exon 9 (legacy numbering)|deletion of part of the promoter through exon 10 (current numbering)",
    "CFTRdelePr-9",
    "c.(?_1)_(1392+1_1393-1)del"
  ],
  "duplication of exon 1 (legacy and current numbering)": [
    "duplication of exon 1 (legacy and current numbering)",
    "p.?",
    "c.(?_1)_(53+1_54-1)dup",
    "CFTRdup1"
  ],
  "c.(?_1)_(53+1_54-1)dup": [
    "duplication of exon 1 (legacy and current numbering)",
    "p.?",
    "c.(?_1)_(53+1_54-1)dup",
    "CFTRdup1"
  ],
  "CFTRdup1": [
    "duplication of exon 1 (legacy and current numbering)",
    "p.?",
    "c.(?_1)_(53+1_54-1)dup",
    "CFTRdup1"
  ],
  "duplication of exons 14a through 19 (legacy numbering)|duplication of exons 15 through 22 (current numbering)": [
    "duplication of exons 14a through 19 (legacy numbering)|duplication of exons 15 through 22 (current numbering)",
    "CFTRdup14a-19",
    "p.?",
    "c.(2490+1_2491-1)_(3717+1_3718-1)dup"
  ],
  "CFTRdup14a-19": [
    "duplication of exons 14a through 19 (legacy numbering)|duplication of exons 15 through 22 (current numbering)",
    "CFTRdup14a-19",
    "p.?",
    "c.(2490+1_2491-1)_(3717+1_3718-1)dup"
  ],
  "c.(2490+1_2491-1)_(3717+1_3718-1)dup": [
    "duplication of exons 14a through 19 (legacy numbering)|duplication of exons 15 through 22 (current numbering)",
    "CFTRdup14a-19",
    "p.?",
    "c.(2490+1_2491-1)_(3717+1_3718-1)dup"
  ],
  "CFTRdup14b-17b": [
    "CFTRdup14b-17b",
    "p.?",
    "duplication of exons 14b through 17b (legacy numbering)|duplication of exons 16 through 20 (current numbering)",
    "c.(2619+1_2620-1)_(3367+1_3368-1)dup"
  ],
  "duplication of exons 14b through 17b (legacy numbering)|duplication of exons 16 through 20 (current numbering)": [
    "CFTRdup14b-17b",
    "p.?",
    "duplication of exons 14b through 17b (legacy numbering)|duplication of exons 16 through 20 (current numbering)",
    "c.(2619+1_2620-1)_(3367+1_3368-1)dup"
  ],
  "c.(2619+1_2620-1)_(3367+1_3368-1)dup": [
    "CFTRdup14b-17b",
    "p.?",
    "duplication of exons 14b through 17b (legacy numbering)|duplication of exons 16 through 20 (current numbering)",
    "c.(2619+1_2620-1)_(3367+1_3368-1)dup"
  ],
  "duplication of exons 16 through 18 (legacy numbering)|duplication of exons 18 through 21 (current numbering)": [
    "duplication of exons 16 through 18 (legacy numbering)|duplication of exons 18 through 21 (current numbering)",
    "p.?",
    "c.(2908+1_2909-1)_(3468+1_3469-1)dup",
    "CFTRdup16-18"
  ],
  "c.(2908+1_2909-1)_(3468+1_3469-1)dup": [
    "duplication of exons 16 through 18 (legacy numbering)|duplication of exons 18 through 21 (current numbering)",
    "p.?",
    "c.(2908+1_2909-1)_(3468+1_3469-1)dup",
    "CFTRdup16-18"
  ],
  "CFTRdup16-18": [
    "duplication of exons 16 through 18 (legacy numbering)|duplication of exons 18 through 21 (current numbering)",
    "p.?",
    "c.(2908+1_2909-1)_(3468+1_3469-1)dup",
    "CFTRdup16-18"
  ],
  "CFTRdup16-20": [
    "CFTRdup16-20",
    "p.?",
    "c.(2908+1_2909-1)_(3873+1_3874-1)dup",
    "duplication of exons 16 through 20 (legacy numbering)|duplication of exons 16 through 23 (current numbering)"
  ],
  "c.(2908+1_2909-1)_(3873+1_3874-1)dup": [
    "CFTRdup16-20",
    "p.?",
    "c.(2908+1_2909-1)_(3873+1_3874-1)dup",
    "duplication of exons 16 through 20 (legacy numbering)|duplication of exons 16 through 23 (current numbering)"
  ],
  "duplication of exons 16 through 20 (legacy numbering)|duplication of exons 16 through 23 (current numbering)": [
    "CFTRdup16-20",
    "p.?",
    "c.(2908+1_2909-1)_(3873+1_3874-1)dup",
    "duplication of exons 16 through 20 (legacy numbering)|duplication of exons 16 through 23 (current numbering)"
  ],
  "CFTRdup16-22": [
    "p.?",
    "CFTRdup16-22",
    "duplication of exons 16 through 22 (legacy numbering)|duplication of exons 16 through 25 (current numbering)",
    "c.(2908+1_2909-1)_(4136+1_4137-1)del"
  ],
  "duplication of exons 16 through 22 (legacy numbering)|duplication of exons 16 through 25 (current numbering)": [
    "p.?",
    "CFTRdup16-22",
    "duplication of exons 16 through 22 (legacy numbering)|duplication of exons 16 through 25 (current numbering)",
    "c.(2908+1_2909-1)_(4136+1_4137-1)del"
  ],
  "c.(2908+1_2909-1)_(4136+1_4137-1)del": [
    "p.?",
    "CFTRdup16-22",
    "duplication of exons 16 through 22 (legacy numbering)|duplication of exons 16 through 25 (current numbering)",
    "c.(2908+1_2909-1)_(4136+1_4137-1)del"
  ],
  "CFTRdup2-4": [
    "CFTRdup2-4",
    "c.(53+1_54-1)_(489+1_490-1)dup",
    "duplication of exons 2 through 4 (legacy numbering and current numbering)",
    "p.?"
  ],
  "c.(53+1_54-1)_(489+1_490-1)dup": [
    "CFTRdup2-4",
    "c.(53+1_54-1)_(489+1_490-1)dup",
    "duplication of exons 2 through 4 (legacy numbering and current numbering)",
    "p.?"
  ],
  "duplication of exons 2 through 4 (legacy numbering and current numbering)": [
    "CFTRdup2-4",
    "c.(53+1_54-1)_(489+1_490-1)dup",
    "duplication of exons 2 through 4 (legacy numbering and current numbering)",
    "p.?"
  ],
  "c.(3963+1_3964-1)_(4242+1_4243-1)dup": [
    "p.?",
    "c.(3963+1_3964-1)_(4242+1_4243-1)dup",
    "duplication of exons 22 and 23 (legacy numbering)|duplication of exons 25 and 26 (current numbering)",
    "CFTRdup22,23"
  ],
  "duplication of exons 22 and 23 (legacy numbering)|duplication of exons 25 and 26 (current numbering)": [
    "p.?",
    "c.(3963+1_3964-1)_(4242+1_4243-1)dup",
    "duplication of exons 22 and 23 (legacy numbering)|duplication of exons 25 and 26 (current numbering)",
    "CFTRdup22,23"
  ],
  "CFTRdup22,23": [
    "p.?",
    "c.(3963+1_3964-1)_(4242+1_4243-1)dup",
    "duplication of exons 22 and 23 (legacy numbering)|duplication of exons 25 and 26 (current numbering)",
    "CFTRdup22,23"
  ],
  "duplication of exons 4 through 19 (legacy numbering)|duplication of exons 4 through 22 (current numbering)": [
    "duplication of exons 4 through 19 (legacy numbering)|duplication of exons 4 through 22 (current numbering)",
    "p.?",
    "c.(273+1_274-1)_(3717+1_3718-1)del",
    "CFTRdup4-19"
  ],
  "c.(273+1_274-1)_(3717+1_3718-1)del": [
    "duplication of exons 4 through 19 (legacy numbering)|duplication of exons 4 through 22 (current numbering)",
    "p.?",
    "c.(273+1_274-1)_(3717+1_3718-1)del",
    "CFTRdup4-19"
  ],
  "CFTRdup4-19": [
    "duplication of exons 4 through 19 (legacy numbering)|duplication of exons 4 through 22 (current numbering)",
    "p.?",
    "c.(273+1_274-1)_(3717+1_3718-1)del",
    "CFTRdup4-19"
  ],
  "CFTRdup4-8": [
    "CFTRdup4-8",
    "duplication of exons 4 through 8 (legacy numbering)|duplication of exons 4 through 9 (current numbering)",
    "c.(273+1_274-1)_(1209+1_1210-1)dup",
    "p.?"
  ],
  "duplication of exons 4 through 8 (legacy numbering)|duplication of exons 4 through 9 (current numbering)": [
    "CFTRdup4-8",
    "duplication of exons 4 through 8 (legacy numbering)|duplication of exons 4 through 9 (current numbering)",
    "c.(273+1_274-1)_(1209+1_1210-1)dup",
    "p.?"
  ],
  "c.(273+1_274-1)_(1209+1_1210-1)dup": [
    "CFTRdup4-8",
    "duplication of exons 4 through 8 (legacy numbering)|duplication of exons 4 through 9 (current numbering)",
    "c.(273+1_274-1)_(1209+1_1210-1)dup",
    "p.?"
  ],
  "duplication of exons 6a and 6b (legacy numbering)|duplication of exons 6 and 7 (current numbering)": [
    "duplication of exons 6a and 6b (legacy numbering)|duplication of exons 6 and 7 (current numbering)",
    "CFTRdup6a,6b",
    "p.?",
    "c.(579+1_580-1)_(869+1_870-1)dup"
  ],
  "CFTRdup6a,6b": [
    "duplication of exons 6a and 6b (legacy numbering)|duplication of exons 6 and 7 (current numbering)",
    "CFTRdup6a,6b",
    "p.?",
    "c.(579+1_580-1)_(869+1_870-1)dup"
  ],
  "c.(579+1_580-1)_(869+1_870-1)dup": [
    "duplication of exons 6a and 6b (legacy numbering)|duplication of exons 6 and 7 (current numbering)",
    "CFTRdup6a,6b",
    "p.?",
    "c.(579+1_580-1)_(869+1_870-1)dup"
  ],
  "c.3281_3367+268delinsTGTTAA": [
    "p.?",
    "c.3281_3367+268delinsTGTTAA",
    "3413_3499+268del355PBins6PB",
    "partial deletion of exon 17b (legacy numbering) with insertion of TGTTAA|partial deletion of exon 20 (current numbering) with insertion of TGTTAA"
  ],
  "3413_3499+268del355PBins6PB": [
    "p.?",
    "c.3281_3367+268delinsTGTTAA",
    "3413_3499+268del355PBins6PB",
    "partial deletion of exon 17b (legacy numbering) with insertion of TGTTAA|partial deletion of exon 20 (current numbering) with insertion of TGTTAA"
  ],
  "partial deletion of exon 17b (legacy numbering) with insertion of TGTTAA|partial deletion of exon 20 (current numbering) with insertion of TGTTAA": [
    "p.?",
    "c.3281_3367+268delinsTGTTAA",
    "3413_3499+268del355PBins6PB",
    "partial deletion of exon 17b (legacy numbering) with insertion of TGTTAA|partial deletion of exon 20 (current numbering) with insertion of TGTTAA"
  ],
  "3499+1G->T": [
    "3499+1G->T",
    "c.3367+1G>T",
    "p.?"
  ],
  "c.3367+1G>T": [
    "3499+1G->T",
    "c.3367+1G>T",
    "p.?"
  ],
  "c.3963+1G>C": [
    "c.3963+1G>C",
    "p.?",
    "4095+1G->C"
  ],
  "4095+1G->C": [
    "c.3963+1G>C",
    "p.?",
    "4095+1G->C"
  ],
  "c.1116_1116+1insATCAA": [
    "c.1116_1116+1insATCAA",
    "p.?",
    "1248insATCAA"
  ],
  "1248insATCAA": [
    "c.1116_1116+1insATCAA",
    "p.?",
    "1248insATCAA"
  ],
  "c.1209+1G>C": [
    "p.?",
    "c.1209+1G>C",
    "1341+1G->C"
  ],
  "1341+1G->C": [
    "p.?",
    "c.1209+1G>C",
    "1341+1G->C"
  ],
  "c.1209+2T>G": [
    "c.1209+2T>G",
    "p.?",
    "1341+2T->G"
  ],
  "1341+2T->G": [
    "c.1209+2T>G",
    "p.?",
    "1341+2T->G"
  ],
  "c.1210-1G>T": [
    "c.1210-1G>T",
    "p.?",
    "1342-1G->T"
  ],
  "1342-1G->T": [
    "c.1210-1G>T",
    "p.?",
    "1342-1G->T"
  ],
  "1524+1delG": [
    "1524+1delG",
    "p.?",
    "c.1392+1del"
  ],
  "c.1392+1del": [
    "1524+1delG",
    "p.?",
    "c.1392+1del"
  ],
  "c.1766+2del": [
    "c.1766+2del",
    "p.?",
    "1898+2delT"
  ],
  "1898+2delT": [
    "c.1766+2del",
    "p.?",
    "1898+2delT"
  ],
  "2751+2T->A": [
    "2751+2T->A",
    "p.?",
    "c.2619+2T>A"
  ],
  "c.2619+2T>A": [
    "2751+2T->A",
    "p.?",
    "c.2619+2T>A"
  ],
  "c.2620-1G>T": [
    "c.2620-1G>T",
    "p.?",
    "2752-1G->T"
  ],
  "2752-1G->T": [
    "c.2620-1G>T",
    "p.?",
    "2752-1G->T"
  ],
  "406-2A->C": [
    "406-2A->C",
    "p.?",
    "c.274-2A>C"
  ],
  "c.274-2A>C": [
    "406-2A->C",
    "p.?",
    "c.274-2A>C"
  ],
  "c.2989-2A>T": [
    "c.2989-2A>T",
    "p.?",
    "3121-2A->T"
  ],
  "3121-2A->T": [
    "c.2989-2A>T",
    "p.?",
    "3121-2A->T"
  ],
  "c.3367+2T>C": [
    "c.3367+2T>C",
    "p.?",
    "3499+2T->C"
  ],
  "3499+2T->C": [
    "c.3367+2T>C",
    "p.?",
    "3499+2T->C"
  ],
  "3500-1G->A": [
    "3500-1G->A",
    "p.?",
    "c.3368-1G>A"
  ],
  "c.3368-1G>A": [
    "3500-1G->A",
    "p.?",
    "c.3368-1G>A"
  ],
  "c.3963+1G>A": [
    "c.3963+1G>A",
    "4095+1G->A",
    "p.?"
  ],
  "4095+1G->A": [
    "c.3963+1G>A",
    "4095+1G->A",
    "p.?"
  ],
  "c.490-2A>C": [
    "c.490-2A>C",
    "622-2A->C",
    "p.?"
  ],
  "622-2A->C": [
    "c.490-2A>C",
    "622-2A->C",
    "p.?"
  ],
  "c.54-2A>G": [
    "c.54-2A>G",
    "186-2A->G",
    "p.?"
  ],
  "186-2A->G": [
    "c.54-2A>G",
    "186-2A->G",
    "p.?"
  ],
  "2623-2A->G": [
    "2623-2A->G",
    "p.?",
    "c.2491-2A>G"
  ],
  "c.2491-2A>G": [
    "2623-2A->G",
    "p.?",
    "c.2491-2A>G"
  ],
  "c.2989-1G>T": [
    "c.2989-1G>T",
    "3121-1G->T",
    "p.?"
  ],
  "3121-1G->T": [
    "c.2989-1G>T",
    "3121-1G->T",
    "p.?"
  ],
  "c.2989-2A>C": [
    "p.?",
    "c.2989-2A>C",
    "3121-2A->C"
  ],
  "3121-2A->C": [
    "p.?",
    "c.2989-2A>C",
    "3121-2A->C"
  ],
  "3601-1G->A": [
    "3601-1G->A",
    "p.?",
    "c.3469-1G>A"
  ],
  "c.3469-1G>A": [
    "3601-1G->A",
    "p.?",
    "c.3469-1G>A"
  ],
  "p.Arg658LysfsX7": [
    "p.Arg658LysfsX7",
    "c.1972dup",
    "2104insA"
  ],
  "c.1972dup": [
    "p.Arg658LysfsX7",
    "c.1972dup",
    "2104insA"
  ],
  "2104insA": [
    "p.Arg658LysfsX7",
    "c.1972dup",
    "2104insA"
  ],
  "2215delG": [
    "2215delG",
    "c.2083del",
    "p.Glu695LysfsX27"
  ],
  "c.2083del": [
    "2215delG",
    "c.2083del",
    "p.Glu695LysfsX27"
  ],
  "p.Glu695LysfsX27": [
    "2215delG",
    "c.2083del",
    "p.Glu695LysfsX27"
  ],
  "2640delT": [
    "2640delT",
    "p.Asp836GlufsX8",
    "c.2508del"
  ],
  "p.Asp836GlufsX8": [
    "2640delT",
    "p.Asp836GlufsX8",
    "c.2508del"
  ],
  "c.2508del": [
    "2640delT",
    "p.Asp836GlufsX8",
    "c.2508del"
  ],
  "c.1025_1026insTA": [
    "c.1025_1026insTA",
    "p.Cys343ThrfsX27",
    "1157insTA"
  ],
  "p.Cys343ThrfsX27": [
    "c.1025_1026insTA",
    "p.Cys343ThrfsX27",
    "1157insTA"
  ],
  "1157insTA": [
    "c.1025_1026insTA",
    "p.Cys343ThrfsX27",
    "1157insTA"
  ],
  "p.Asp373GlufsX9": [
    "p.Asp373GlufsX9",
    "c.1118dup",
    "1249insA"
  ],
  "c.1118dup": [
    "p.Asp373GlufsX9",
    "c.1118dup",
    "1249insA"
  ],
  "1249insA": [
    "p.Asp373GlufsX9",
    "c.1118dup",
    "1249insA"
  ],
  "c.112_113del": [
    "c.112_113del",
    "p.Tyr38ProfsX6",
    "241delAT"
  ],
  "p.Tyr38ProfsX6": [
    "c.112_113del",
    "p.Tyr38ProfsX6",
    "241delAT"
  ],
  "241delAT": [
    "c.112_113del",
    "p.Tyr38ProfsX6",
    "241delAT"
  ],
  "1262delA": [
    "1262delA",
    "c.1130del",
    "p.Lys377SerfsX11"
  ],
  "c.1130del": [
    "1262delA",
    "c.1130del",
    "p.Lys377SerfsX11"
  ],
  "p.Lys377SerfsX11": [
    "1262delA",
    "c.1130del",
    "p.Lys377SerfsX11"
  ],
  "c.1157dup": [
    "c.1157dup",
    "p.Asn386LysfsX25",
    "1288insA"
  ],
  "p.Asn386LysfsX25": [
    "c.1157dup",
    "p.Asn386LysfsX25",
    "1288insA"
  ],
  "1288insA": [
    "c.1157dup",
    "p.Asn386LysfsX25",
    "1288insA"
  ],
  "c.1162_1168del": [
    "c.1162_1168del",
    "1294del7",
    "p.Thr388GlnfsX3"
  ],
  "1294del7": [
    "c.1162_1168del",
    "1294del7",
    "p.Thr388GlnfsX3"
  ],
  "p.Thr388GlnfsX3": [
    "c.1162_1168del",
    "1294del7",
    "p.Thr388GlnfsX3"
  ],
  "1380insT": [
    "1380insT",
    "c.1248dup",
    "p.Asn417X"
  ],
  "c.1248dup": [
    "1380insT",
    "c.1248dup",
    "p.Asn417X"
  ],
  "p.Asn417X": [
    "1380insT",
    "c.1248dup",
    "p.Asn417X"
  ],
  "1498delG": [
    "1498delG",
    "p.Val456LeufsX13",
    "c.1366del"
  ],
  "p.Val456LeufsX13": [
    "1498delG",
    "p.Val456LeufsX13",
    "c.1366del"
  ],
  "c.1366del": [
    "1498delG",
    "p.Val456LeufsX13",
    "c.1366del"
  ],
  "c.1439del": [
    "c.1439del",
    "p.Gly480ValfsX47",
    "1571delG"
  ],
  "p.Gly480ValfsX47": [
    "c.1439del",
    "p.Gly480ValfsX47",
    "1571delG"
  ],
  "1571delG": [
    "c.1439del",
    "p.Gly480ValfsX47",
    "1571delG"
  ],
  "c.1616_1617dup": [
    "c.1616_1617dup",
    "1749insTA",
    "p.Val540X"
  ],
  "1749insTA": [
    "c.1616_1617dup",
    "1749insTA",
    "p.Val540X"
  ],
  "p.Val540X": [
    "c.1616_1617dup",
    "1749insTA",
    "p.Val540X"
  ],
  "c.1674del": [
    "c.1674del",
    "p.Ala559GlnfsX13",
    "1806delA"
  ],
  "p.Ala559GlnfsX13": [
    "1807delG",
    "p.Ala559GlnfsX13",
    "c.1675del"
  ],
  "1806delA": [
    "c.1674del",
    "p.Ala559GlnfsX13",
    "1806delA"
  ],
  "1874_1875insTT": [
    "1874_1875insTT",
    "p.Leu581PhefsX2",
    "c.1741_1742dup"
  ],
  "p.Leu581PhefsX2": [
    "1874_1875insTT",
    "p.Leu581PhefsX2",
    "c.1741_1742dup"
  ],
  "c.1741_1742dup": [
    "1874_1875insTT",
    "p.Leu581PhefsX2",
    "c.1741_1742dup"
  ],
  "1932delG": [
    "1932delG",
    "p.Ile601PhefsX10",
    "c.1800del"
  ],
  "p.Ile601PhefsX10": [
    "1932delG",
    "p.Ile601PhefsX10",
    "c.1800del"
  ],
  "c.1800del": [
    "1932delG",
    "p.Ile601PhefsX10",
    "c.1800del"
  ],
  "p.Thr604PhefsX5": [
    "p.Thr604PhefsX5",
    "c.1810_1826del",
    "1942del17"
  ],
  "c.1810_1826del": [
    "p.Thr604PhefsX5",
    "c.1810_1826del",
    "1942del17"
  ],
  "1942del17": [
    "p.Thr604PhefsX5",
    "c.1810_1826del",
    "1942del17"
  ],
  "p.Ile616TyrfsX2": [
    "p.Ile616TyrfsX2",
    "1978delA",
    "c.1846del"
  ],
  "1978delA": [
    "p.Ile616TyrfsX2",
    "1978delA",
    "c.1846del"
  ],
  "c.1846del": [
    "p.Ile616TyrfsX2",
    "1978delA",
    "c.1846del"
  ],
  "p.Ser63PhefsX6": [
    "p.Ser63PhefsX6",
    "317insC",
    "c.185dup"
  ],
  "317insC": [
    "p.Ser63PhefsX6",
    "317insC",
    "c.185dup"
  ],
  "c.185dup": [
    "p.Ser63PhefsX6",
    "317insC",
    "c.185dup"
  ],
  "p.Tyr625PhefsX16": [
    "p.Tyr625PhefsX16",
    "c.1874_1875del",
    "2005delTA"
  ],
  "c.1874_1875del": [
    "p.Tyr625PhefsX16",
    "c.1874_1875del",
    "2005delTA"
  ],
  "2005delTA": [
    "p.Tyr625PhefsX16",
    "c.1874_1875del",
    "2005delTA"
  ],
  "c.1977_1986del": [
    "c.1977_1986del",
    "2109-2118del10",
    "p.Asn659LysfsX10"
  ],
  "2109-2118del10": [
    "c.1977_1986del",
    "2109-2118del10",
    "p.Asn659LysfsX10"
  ],
  "p.Asn659LysfsX10": [
    "c.1977_1986del",
    "2109-2118del10",
    "p.Asn659LysfsX10"
  ],
  "p.Thr663ProfsX21": [
    "p.Thr663ProfsX21",
    "2118del14",
    "c.1987_2000del"
  ],
  "2118del14": [
    "p.Thr663ProfsX21",
    "2118del14",
    "c.1987_2000del"
  ],
  "c.1987_2000del": [
    "p.Thr663ProfsX21",
    "2118del14",
    "c.1987_2000del"
  ],
  "p.His667ProfsX21": [
    "p.His667ProfsX21",
    "2132delAC",
    "c.2000_2001del"
  ],
  "2132delAC": [
    "p.His667ProfsX21",
    "2132delAC",
    "c.2000_2001del"
  ],
  "c.2000_2001del": [
    "p.His667ProfsX21",
    "2132delAC",
    "c.2000_2001del"
  ],
  "c.2044dup": [
    "c.2044dup",
    "2175insA",
    "p.Thr682AsnfsX7"
  ],
  "2175insA": [
    "c.2044dup",
    "2175insA",
    "p.Thr682AsnfsX7"
  ],
  "p.Thr682AsnfsX7": [
    "c.2044dup",
    "2175insA",
    "p.Thr682AsnfsX7"
  ],
  "2409delC": [
    "2409delC",
    "c.2277del",
    "p.Thr760ArgfsX11"
  ],
  "c.2277del": [
    "2409delC",
    "c.2277del",
    "p.Thr760ArgfsX11"
  ],
  "p.Val769CysfsX10": [
    "p.Val769CysfsX10",
    "c.2303dup",
    "2435insC"
  ],
  "c.2303dup": [
    "p.Val769CysfsX10",
    "c.2303dup",
    "2435insC"
  ],
  "2435insC": [
    "p.Val769CysfsX10",
    "c.2303dup",
    "2435insC"
  ],
  "p.His775LeufsX3": [
    "p.His775LeufsX3",
    "2456delAC",
    "c.2324_2325del"
  ],
  "2456delAC": [
    "p.His775LeufsX3",
    "2456delAC",
    "c.2324_2325del"
  ],
  "c.2324_2325del": [
    "p.His775LeufsX3",
    "2456delAC",
    "c.2324_2325del"
  ],
  "p.Val794CysfsX9": [
    "p.Val794CysfsX9",
    "2512delG",
    "c.2380del"
  ],
  "2512delG": [
    "p.Val794CysfsX9",
    "2512delG",
    "c.2380del"
  ],
  "c.2380del": [
    "p.Val794CysfsX9",
    "2512delG",
    "c.2380del"
  ],
  "p.Glu819X": [
    "p.Glu819X",
    "c.2454_2455insT",
    "2586-2687insT"
  ],
  "c.2454_2455insT": [
    "p.Glu819X",
    "c.2454_2455insT",
    "2586-2687insT"
  ],
  "2586-2687insT": [
    "p.Glu819X",
    "c.2454_2455insT",
    "2586-2687insT"
  ],
  "p.Ala872GlufsX34": [
    "p.Ala872GlufsX34",
    "c.2615del",
    "2747delC"
  ],
  "c.2615del": [
    "p.Ala872GlufsX34",
    "c.2615del",
    "2747delC"
  ],
  "2747delC": [
    "p.Ala872GlufsX34",
    "c.2615del",
    "2747delC"
  ],
  "c.2732_2733insA": [
    "c.2732_2733insA",
    "p.Ser911ArgfsX64"
  ],
  "p.Ser911ArgfsX64": [
    "c.2732_2733insA",
    "p.Ser911ArgfsX64"
  ],
  "p.Ser912IlefsX63": [
    "p.Ser912IlefsX63",
    "c.2733insA",
    "c.2733_2734insA"
  ],
  "c.2733insA": [
    "p.Ser912IlefsX63",
    "c.2733insA",
    "c.2733_2734insA"
  ],
  "c.2733_2734insA": [
    "p.Ser912IlefsX63",
    "c.2733insA",
    "c.2733_2734insA"
  ],
  "2935del11": [
    "2935del11",
    "c.2803_2813del",
    "p.Leu935AlafsX36"
  ],
  "c.2803_2813del": [
    "2935del11",
    "c.2803_2813del",
    "p.Leu935AlafsX36"
  ],
  "p.Leu935AlafsX36": [
    "2935del11",
    "c.2803_2813del",
    "p.Leu935AlafsX36"
  ],
  "2948delA": [
    "2948delA",
    "p.His939LeufsX3",
    "c.2816del"
  ],
  "p.His939LeufsX3": [
    "2948delA",
    "p.His939LeufsX3",
    "c.2816del"
  ],
  "c.2816del": [
    "2948delA",
    "p.His939LeufsX3",
    "c.2816del"
  ],
  "p.Leu941SerfsX34": [
    "p.Leu941SerfsX34",
    "2951insA",
    "c.2819_2820insA"
  ],
  "2951insA": [
    "p.Leu941SerfsX34",
    "2951insA",
    "c.2819_2820insA"
  ],
  "c.2819_2820insA": [
    "p.Leu941SerfsX34",
    "2951insA",
    "c.2819_2820insA"
  ],
  "415insA": [
    "415insA",
    "p.Ala96SerfsX15",
    "c.285dup"
  ],
  "p.Ala96SerfsX15": [
    "415insA",
    "p.Ala96SerfsX15",
    "c.285dup"
  ],
  "c.285dup": [
    "415insA",
    "p.Ala96SerfsX15",
    "c.285dup"
  ],
  "p.Pro960LeufsX8": [
    "p.Pro960LeufsX8",
    "c.2879del",
    "3011delC"
  ],
  "c.2879del": [
    "p.Pro960LeufsX8",
    "c.2879del",
    "3011delC"
  ],
  "3011delC": [
    "p.Pro960LeufsX8",
    "c.2879del",
    "3011delC"
  ],
  "3015_3018dupGTCA": [
    "3015_3018dupGTCA",
    "p.Thr963ValfsX13",
    "c.2883_2886dup"
  ],
  "p.Thr963ValfsX13": [
    "3015_3018dupGTCA",
    "p.Thr963ValfsX13",
    "c.2883_2886dup"
  ],
  "c.2883_2886dup": [
    "3015_3018dupGTCA",
    "p.Thr963ValfsX13",
    "c.2883_2886dup"
  ],
  "3029delC": [
    "3029delC",
    "c.2897del",
    "p.Thr966SerfsX2"
  ],
  "c.2897del": [
    "3029delC",
    "c.2897del",
    "p.Thr966SerfsX2"
  ],
  "p.Thr966SerfsX2": [
    "3029delC",
    "c.2897del",
    "p.Thr966SerfsX2"
  ],
  "3031-3032delinsA": [
    "3031-3032delinsA",
    "c.2899_2900delinsA",
    "p.Leu967ArgfsX14"
  ],
  "c.2899_2900delinsA": [
    "3031-3032delinsA",
    "c.2899_2900delinsA",
    "p.Leu967ArgfsX14"
  ],
  "p.Leu967ArgfsX14": [
    "3031-3032delinsA",
    "c.2899_2900delinsA",
    "p.Leu967ArgfsX14"
  ],
  "p.Met1028TyrfsX19": [
    "p.Met1028TyrfsX19",
    "c.3081dup",
    "3213-3214insT"
  ],
  "c.3081dup": [
    "p.Met1028TyrfsX19",
    "c.3081dup",
    "3213-3214insT"
  ],
  "3213-3214insT": [
    "p.Met1028TyrfsX19",
    "c.3081dup",
    "3213-3214insT"
  ],
  "3238delA": [
    "3238delA",
    "c.3106del",
    "p.Thr1036ProfsX24"
  ],
  "c.3106del": [
    "3238delA",
    "c.3106del",
    "p.Thr1036ProfsX24"
  ],
  "p.Thr1036ProfsX24": [
    "3238delA",
    "c.3106del",
    "p.Thr1036ProfsX24"
  ],
  "c.3290_3305del": [
    "c.3290_3305del",
    "3422del16",
    "p.Arg1097GlnfsX2"
  ],
  "3422del16": [
    "c.3290_3305del",
    "3422del16",
    "p.Arg1097GlnfsX2"
  ],
  "p.Arg1097GlnfsX2": [
    "c.3290_3305del",
    "3422del16",
    "p.Arg1097GlnfsX2"
  ],
  "3425delG": [
    "3425delG",
    "p.Trp1098CysfsX4",
    "c.3294del"
  ],
  "p.Trp1098CysfsX4": [
    "3425delG",
    "p.Trp1098CysfsX4",
    "c.3294del"
  ],
  "c.3294del": [
    "3425delG",
    "p.Trp1098CysfsX4",
    "c.3294del"
  ],
  "p.Met1105IlefsX16": [
    "p.Met1105IlefsX16",
    "3447delG",
    "c.3315del"
  ],
  "3447delG": [
    "p.Met1105IlefsX16",
    "3447delG",
    "c.3315del"
  ],
  "c.3315del": [
    "p.Met1105IlefsX16",
    "3447delG",
    "c.3315del"
  ],
  "3516del5": [
    "3516del5",
    "c.3384_3388del",
    "p.Val1129TyrfsX25"
  ],
  "c.3384_3388del": [
    "3516del5",
    "c.3384_3388del",
    "p.Val1129TyrfsX25"
  ],
  "p.Val1129TyrfsX25": [
    "3516del5",
    "c.3384_3388del",
    "p.Val1129TyrfsX25"
  ],
  "p.Thr1142LysfsX15": [
    "p.Thr1142LysfsX15",
    "c.3421_3424dup",
    "3556insAGTA"
  ],
  "c.3421_3424dup": [
    "p.Thr1142LysfsX15",
    "c.3421_3424dup",
    "3556insAGTA"
  ],
  "3556insAGTA": [
    "p.Thr1142LysfsX15",
    "c.3421_3424dup",
    "3556insAGTA"
  ],
  "p.Lys1180ThrfsX7": [
    "p.Lys1180ThrfsX7",
    "c.3539_3554del"
  ],
  "c.3539_3554del": [
    "p.Lys1180ThrfsX7",
    "c.3539_3554del"
  ],
  "3731-3732AA->G": [
    "3731-3732AA->G",
    "c.3599_3600delinsG",
    "p.Lys1200ArgfsX11"
  ],
  "c.3599_3600delinsG": [
    "3731-3732AA->G",
    "c.3599_3600delinsG",
    "p.Lys1200ArgfsX11"
  ],
  "p.Lys1200ArgfsX11": [
    "3731-3732AA->G",
    "c.3599_3600delinsG",
    "p.Lys1200ArgfsX11"
  ],
  "3755dupG": [
    "3755dupG",
    "p.Gln1209ProfsX56",
    "c.3623dup"
  ],
  "p.Gln1209ProfsX56": [
    "3755dupG",
    "p.Gln1209ProfsX56",
    "c.3623dup"
  ],
  "c.3623dup": [
    "3755dupG",
    "p.Gln1209ProfsX56",
    "c.3623dup"
  ],
  "c.3658dup": [
    "c.3658dup",
    "p.Thr1220AsnfsX45",
    "3789insA"
  ],
  "p.Thr1220AsnfsX45": [
    "c.3658dup",
    "p.Thr1220AsnfsX45",
    "3789insA"
  ],
  "3789insA": [
    "c.3658dup",
    "p.Thr1220AsnfsX45",
    "3789insA"
  ],
  "c.367dup": [
    "c.367dup",
    "p.Leu123ProfsX36",
    "499dupC"
  ],
  "p.Leu123ProfsX36": [
    "c.367dup",
    "p.Leu123ProfsX36",
    "499dupC"
  ],
  "499dupC": [
    "c.367dup",
    "p.Leu123ProfsX36",
    "499dupC"
  ],
  "p.Leu1242SerfsX17": [
    "p.Leu1242SerfsX17",
    "3856delC",
    "c.3724del"
  ],
  "3856delC": [
    "p.Leu1242SerfsX17",
    "3856delC",
    "c.3724del"
  ],
  "c.3724del": [
    "p.Leu1242SerfsX17",
    "3856delC",
    "c.3724del"
  ],
  "c.3754dup": [
    "c.3754dup",
    "p.Thr1252AsnfsX13",
    "3886insA"
  ],
  "p.Thr1252AsnfsX13": [
    "c.3754dup",
    "p.Thr1252AsnfsX13",
    "3886insA"
  ],
  "3886insA": [
    "c.3754dup",
    "p.Thr1252AsnfsX13",
    "3886insA"
  ],
  "3889dupT": [
    "3889dupT",
    "c.3758dup",
    "p.Leu1253PhefsX12"
  ],
  "c.3758dup": [
    "3889dupT",
    "c.3758dup",
    "p.Leu1253PhefsX12"
  ],
  "p.Leu1253PhefsX12": [
    "3889dupT",
    "c.3758dup",
    "p.Leu1253PhefsX12"
  ],
  "c.3767dup": [
    "p.Leu1258PhefsX7",
    "c.3767dup",
    "3898insC"
  ],
  "3898insC": [
    "p.Leu1258PhefsX7",
    "c.3767dup",
    "3898insC"
  ],
  "c.3773del": [
    "c.3773del",
    "p.Leu1258X",
    "3905delT"
  ],
  "p.Leu1258X": [
    "c.3773del",
    "p.Leu1258X",
    "3905delT"
  ],
  "3905delT": [
    "c.3773del",
    "p.Leu1258X",
    "3905delT"
  ],
  "c.3827del": [
    "c.3827del",
    "p.Ser1276X",
    "3959delC"
  ],
  "p.Ser1276X": [
    "c.3827del",
    "p.Ser1276X",
    "3959delC"
  ],
  "3959delC": [
    "c.3827del",
    "p.Ser1276X",
    "3959delC"
  ],
  "p.Ile1277X": [
    "p.Ile1277X",
    "3960-3961delA",
    "c.3829del"
  ],
  "3960-3961delA": [
    "p.Ile1277X",
    "3960-3961delA",
    "c.3829del"
  ],
  "c.3829del": [
    "p.Ile1277X",
    "3960-3961delA",
    "c.3829del"
  ],
  "p.Asp1320MetfsX8": [
    "p.Asp1320MetfsX8",
    "c.3957del",
    "4089delA"
  ],
  "c.3957del": [
    "p.Asp1320MetfsX8",
    "c.3957del",
    "4089delA"
  ],
  "4089delA": [
    "p.Asp1320MetfsX8",
    "c.3957del",
    "4089delA"
  ],
  "c.4033_4034del": [
    "c.4033_4034del",
    "4165delGT",
    "p.Val1345ProfsX13"
  ],
  "4165delGT": [
    "c.4033_4034del",
    "4165delGT",
    "p.Val1345ProfsX13"
  ],
  "p.Val1345ProfsX13": [
    "c.4033_4034del",
    "4165delGT",
    "p.Val1345ProfsX13"
  ],
  "c.4065_4066del": [
    "c.4065_4066del",
    "p.Leu1356GlyfsX2",
    "4197_4198delCT"
  ],
  "p.Leu1356GlyfsX2": [
    "c.4065_4066del",
    "p.Leu1356GlyfsX2",
    "4197_4198delCT"
  ],
  "4197_4198delCT": [
    "c.4065_4066del",
    "p.Leu1356GlyfsX2",
    "4197_4198delCT"
  ],
  "c.4071_4073delinsAA": [
    "c.4071_4073delinsAA",
    "4203TAG->AA",
    "p.Arg1358AsnfsX22"
  ],
  "4203TAG->AA": [
    "c.4071_4073delinsAA",
    "4203TAG->AA",
    "p.Arg1358AsnfsX22"
  ],
  "p.Arg1358AsnfsX22": [
    "c.4071_4073delinsAA",
    "4203TAG->AA",
    "p.Arg1358AsnfsX22"
  ],
  "c.450dup": [
    "c.450dup",
    "582insG",
    "p.Gln151AlafsX8"
  ],
  "582insG": [
    "c.450dup",
    "582insG",
    "p.Gln151AlafsX8"
  ],
  "p.Gln151AlafsX8": [
    "c.450dup",
    "582insG",
    "p.Gln151AlafsX8"
  ],
  "605insT": [
    "605insT",
    "p.Leu159PhefsX4",
    "c.476dup"
  ],
  "p.Leu159PhefsX4": [
    "605insT",
    "p.Leu159PhefsX4",
    "c.476dup"
  ],
  "c.476dup": [
    "605insT",
    "p.Leu159PhefsX4",
    "c.476dup"
  ],
  "746insC": [
    "746insC",
    "c.614dup",
    "p.Leu206PhefsX52"
  ],
  "c.614dup": [
    "746insC",
    "c.614dup",
    "p.Leu206PhefsX52"
  ],
  "p.Leu206PhefsX52": [
    "746insC",
    "c.614dup",
    "p.Leu206PhefsX52"
  ],
  "p.Arg258AsnfsX3": [
    "p.Arg258AsnfsX3",
    "c.773del",
    "905delG"
  ],
  "c.773del": [
    "p.Arg258AsnfsX3",
    "c.773del",
    "905delG"
  ],
  "905delG": [
    "p.Arg258AsnfsX3",
    "c.773del",
    "905delG"
  ],
  "c.905_906insA": [
    "c.905_906insA",
    "p.Arg303GlufsX5",
    "1037insA"
  ],
  "p.Arg303GlufsX5": [
    "c.905_906insA",
    "p.Arg303GlufsX5",
    "1037insA"
  ],
  "1037insA": [
    "c.905_906insA",
    "p.Arg303GlufsX5",
    "1037insA"
  ],
  "c.908_911del": [
    "c.908_911del",
    "p.Arg303ThrfsX24",
    "1040del4"
  ],
  "p.Arg303ThrfsX24": [
    "c.908_911del",
    "p.Arg303ThrfsX24",
    "1040del4"
  ],
  "1040del4": [
    "c.908_911del",
    "p.Arg303ThrfsX24",
    "1040del4"
  ],
  "c.982delA": [
    "c.982delA",
    "p.Ile328SerfsX41",
    "c.982del"
  ],
  "p.Ile328SerfsX41": [
    "c.982delA",
    "p.Ile328SerfsX41",
    "c.982del"
  ],
  "c.982del": [
    "c.982delA",
    "p.Ile328SerfsX41",
    "c.982del"
  ],
  "1185delTC": [
    "1185delTC",
    "c.1053_1054del",
    "p.Arg352AlafsX11"
  ],
  "c.1053_1054del": [
    "1185delTC",
    "c.1053_1054del",
    "p.Arg352AlafsX11"
  ],
  "p.Arg352AlafsX11": [
    "1185delTC",
    "c.1053_1054del",
    "p.Arg352AlafsX11"
  ],
  "308insA": [
    "308insA",
    "c.177dup",
    "p.Glu60ArgfsX9"
  ],
  "c.177dup": [
    "308insA",
    "c.177dup",
    "p.Glu60ArgfsX9"
  ],
  "p.Glu60ArgfsX9": [
    "308insA",
    "c.177dup",
    "p.Glu60ArgfsX9"
  ],
  "2222delG": [
    "2222delG",
    "p.Lys698ArgfsX24",
    "c.2091del"
  ],
  "p.Lys698ArgfsX24": [
    "2222delG",
    "p.Lys698ArgfsX24",
    "c.2091del"
  ],
  "c.2091del": [
    "2222delG",
    "p.Lys698ArgfsX24",
    "c.2091del"
  ],
  "p.Glu831GlyfsX5": [
    "p.Glu831GlyfsX5",
    "c.2489_2490insA",
    "c.2489dup"
  ],
  "c.2489_2490insA": [
    "p.Glu831GlyfsX5",
    "c.2489_2490insA",
    "c.2489dup"
  ],
  "c.2489dup": [
    "p.Glu831GlyfsX5",
    "c.2489_2490insA",
    "c.2489dup"
  ],
  "2694delT": [
    "2694delT",
    "p.Val855SerfsX5",
    "c.2562del"
  ],
  "p.Val855SerfsX5": [
    "2694delT",
    "p.Val855SerfsX5",
    "c.2562del"
  ],
  "c.2562del": [
    "2694delT",
    "p.Val855SerfsX5",
    "c.2562del"
  ],
  "p.Trp882CysfsX25": [
    "p.Trp882CysfsX25",
    "2777insTG",
    "c.2644_2645dup"
  ],
  "2777insTG": [
    "p.Trp882CysfsX25",
    "2777insTG",
    "c.2644_2645dup"
  ],
  "c.2644_2645dup": [
    "p.Trp882CysfsX25",
    "2777insTG",
    "c.2644_2645dup"
  ],
  "2909delT": [
    "2909delT",
    "p.Leu926CysfsX16",
    "c.2777del"
  ],
  "p.Leu926CysfsX16": [
    "2909delT",
    "p.Leu926CysfsX16",
    "c.2777del"
  ],
  "c.2777del": [
    "2909delT",
    "p.Leu926CysfsX16",
    "c.2777del"
  ],
  "p.Gly1003GlufsX3": [
    "p.Gly1003GlufsX3",
    "c.3008del",
    "3139delG"
  ],
  "c.3008del": [
    "p.Gly1003GlufsX3",
    "c.3008del",
    "3139delG"
  ],
  "3139delG": [
    "p.Gly1003GlufsX3",
    "c.3008del",
    "3139delG"
  ],
  "c.3324del": [
    "p.Ile1109SerfsX12",
    "c.3324del",
    "3456delC"
  ],
  "3456delC": [
    "p.Ile1109SerfsX12",
    "c.3324del",
    "3456delC"
  ],
  "p.Phe1166SerfsX26": [
    "p.Phe1166SerfsX26",
    "c.3497del",
    "3629delT"
  ],
  "c.3497del": [
    "p.Phe1166SerfsX26",
    "c.3497del",
    "3629delT"
  ],
  "3629delT": [
    "p.Phe1166SerfsX26",
    "c.3497del",
    "3629delT"
  ],
  "c.3592del": [
    "c.3592del",
    "p.Val1198X",
    "3724delG"
  ],
  "p.Val1198X": [
    "c.3592del",
    "p.Val1198X",
    "3724delG"
  ],
  "3724delG": [
    "c.3592del",
    "p.Val1198X",
    "3724delG"
  ],
  "p.Gly1237AlafsX22": [
    "p.Gly1237AlafsX22",
    "3840delT",
    "c.3708del"
  ],
  "3840delT": [
    "p.Gly1237AlafsX22",
    "3840delT",
    "c.3708del"
  ],
  "c.3708del": [
    "p.Gly1237AlafsX22",
    "3840delT",
    "c.3708del"
  ],
  "4006delA": [
    "4006delA",
    "c.3876del",
    "p.Val1293TyrfsX35"
  ],
  "c.3876del": [
    "4006delA",
    "c.3876del",
    "p.Val1293TyrfsX35"
  ],
  "p.Val1293TyrfsX35": [
    "4006delA",
    "c.3876del",
    "p.Val1293TyrfsX35"
  ],
  "c.387del": [
    "c.387del",
    "519delT",
    "p.Leu130SerfsX4"
  ],
  "519delT": [
    "c.387del",
    "519delT",
    "p.Leu130SerfsX4"
  ],
  "p.Leu130SerfsX4": [
    "c.387del",
    "519delT",
    "p.Leu130SerfsX4"
  ],
  "c.4040_4041del": [
    "c.4040_4041del",
    "p.Ser1347ThrfsX11",
    "4172delGC"
  ],
  "p.Ser1347ThrfsX11": [
    "c.4040_4041del",
    "p.Ser1347ThrfsX11",
    "4172delGC"
  ],
  "4172delGC": [
    "c.4040_4041del",
    "p.Ser1347ThrfsX11",
    "4172delGC"
  ],
  "c.805_806del": [
    "c.805_806del",
    "936delTA",
    "p.Ile269ProfsX4"
  ],
  "936delTA": [
    "c.805_806del",
    "936delTA",
    "p.Ile269ProfsX4"
  ],
  "p.Ile269ProfsX4": [
    "c.805_806del",
    "936delTA",
    "p.Ile269ProfsX4"
  ],
  "p.Gln30ThrfsX15": [
    "p.Gln30ThrfsX15",
    "218insA",
    "c.87dup"
  ],
  "218insA": [
    "p.Gln30ThrfsX15",
    "218insA",
    "c.87dup"
  ],
  "c.87dup": [
    "p.Gln30ThrfsX15",
    "218insA",
    "c.87dup"
  ],
  "p.Leu454AlafsX6": [
    "p.Leu454AlafsX6",
    "c.1360_1387del",
    "1491-1500del"
  ],
  "c.1360_1387del": [
    "p.Leu454AlafsX6",
    "c.1360_1387del",
    "1491-1500del"
  ],
  "1491-1500del": [
    "p.Leu454AlafsX6",
    "c.1360_1387del",
    "1491-1500del"
  ],
  "p.Ala1391HisfsX7": [
    "p.Ala1391HisfsX7",
    "c.4170del",
    "4301delA"
  ],
  "c.4170del": [
    "p.Ala1391HisfsX7",
    "c.4170del",
    "4301delA"
  ],
  "4301delA": [
    "p.Ala1391HisfsX7",
    "c.4170del",
    "4301delA"
  ],
  "749delT": [
    "749delT",
    "c.617del",
    "p.Leu206CysfsX9"
  ],
  "c.617del": [
    "749delT",
    "c.617del",
    "p.Leu206CysfsX9"
  ],
  "p.Leu206CysfsX9": [
    "749delT",
    "c.617del",
    "p.Leu206CysfsX9"
  ],
  "c.234delC": [
    "c.234delC",
    "c.234del",
    "p.Trp79GlyfsX12"
  ],
  "c.234del": [
    "c.234delC",
    "c.234del",
    "p.Trp79GlyfsX12"
  ],
  "p.Trp79GlyfsX12": [
    "c.234delC",
    "c.234del",
    "p.Trp79GlyfsX12"
  ],
  "4048insCC": [
    "4048insCC",
    "p.Tyr1307ProfsX22",
    "c.3917_3918dup"
  ],
  "p.Tyr1307ProfsX22": [
    "4048insCC",
    "p.Tyr1307ProfsX22",
    "c.3917_3918dup"
  ],
  "c.3917_3918dup": [
    "4048insCC",
    "p.Tyr1307ProfsX22",
    "c.3917_3918dup"
  ],
  "T388X": [
    "T388X",
    "c.1162_1163delinsTA",
    "p.Thr388X"
  ],
  "c.1162_1163delinsTA": [
    "T388X",
    "c.1162_1163delinsTA",
    "p.Thr388X"
  ],
  "p.Thr388X": [
    "T388X",
    "c.1162_1163delinsTA",
    "p.Thr388X"
  ],
  "p.Lys716X": [
    "p.Lys716X",
    "c.2145_2146delinsGT|c.2146A>T",
    "K716X"
  ],
  "c.2145_2146delinsGT|c.2146A>T": [
    "p.Lys716X",
    "c.2145_2146delinsGT|c.2146A>T",
    "K716X"
  ],
  "K716X": [
    "p.Lys716X",
    "c.2145_2146delinsGT|c.2146A>T",
    "K716X"
  ],
  "c.2655_2657+13del": [
    "c.2655_2657+13del",
    "2787del16",
    "p.?"
  ],
  "2787del16": [
    "c.2655_2657+13del",
    "2787del16",
    "p.?"
  ],
  "c.2982_2988+2del": [
    "c.2982_2988+2del",
    "c.2982_2988+2delCATCCAGGT",
    "p.?"
  ],
  "c.2982_2988+2delCATCCAGGT": [
    "c.2982_2988+2del",
    "c.2982_2988+2delCATCCAGGT",
    "p.?"
  ],
  "M1K": [
    "M1K",
    "p.?",
    "c.2T>A"
  ],
  "c.2T>A": [
    "M1K",
    "p.?",
    "c.2T>A"
  ],
  "3165dupA": [
    "3165dupA",
    "p.Gln1012ThrfsX35",
    "c.3033dup"
  ],
  "p.Gln1012ThrfsX35": [
    "3165dupA",
    "p.Gln1012ThrfsX35",
    "c.3033dup"
  ],
  "c.3033dup": [
    "c.3033dup"
  ],
  "3271+1G->T": [
    "3271+1G->T",
    "p.?",
    "c.3139+1G>T"
  ],
  "c.3139+1G>T": [
    "3271+1G->T",
    "p.?",
    "c.3139+1G>T"
  ],
  "c.1116+1G>T": [
    "c.1116+1G>T",
    "p.?",
    "1248+1G->T"
  ],
  "1248+1G->T": [
    "c.1116+1G>T",
    "p.?",
    "1248+1G->T"
  ],
  "1248+2T->C": [
    "1248+2T->C",
    "p.?",
    "c.1116+2T>C"
  ],
  "c.1116+2T>C": [
    "1248+2T->C",
    "p.?",
    "c.1116+2T>C"
  ],
  "c.3368-2A>T": [
    "p.?",
    "c.3368-2A>T",
    "3500-2A->T"
  ],
  "3500-2A->T": [
    "p.?",
    "c.3368-2A>T",
    "3500-2A->T"
  ],
  "c.2908+1G>T": [
    "c.2908+1G>T",
    "3040+1G->T",
    "p.?"
  ],
  "3040+1G->T": [
    "c.2908+1G>T",
    "3040+1G->T",
    "p.?"
  ],
  "1248+2T->A": [
    "p.?",
    "1248+2T->A",
    "c.1116+2T>A"
  ],
  "c.1116+2T>A": [
    "p.?",
    "1248+2T->A",
    "c.1116+2T>A"
  ],
  "c.1209+2T>A": [
    "p.?",
    "c.1209+2T>A",
    "1341+2T->A"
  ],
  "1341+2T->A": [
    "p.?",
    "c.1209+2T>A",
    "1341+2T->A"
  ],
  "1342-1G->A": [
    "1342-1G->A",
    "p.?",
    "c.1210-1G>A"
  ],
  "c.1210-1G>A": [
    "1342-1G->A",
    "p.?",
    "c.1210-1G>A"
  ],
  "1525-1G->C": [
    "1525-1G->C",
    "c.1393-1G>C",
    "p.?"
  ],
  "c.1393-1G>C": [
    "1525-1G->C",
    "c.1393-1G>C",
    "p.?"
  ],
  "c.1393-1G>T": [
    "p.?",
    "c.1393-1G>T",
    "1525-1G->T"
  ],
  "1525-1G->T": [
    "p.?",
    "c.1393-1G>T",
    "1525-1G->T"
  ],
  "1716+1G->T": [
    "1716+1G->T",
    "p.?",
    "c.1584+1G>T"
  ],
  "c.1584+1G>T": [
    "1716+1G->T",
    "p.?",
    "c.1584+1G>T"
  ],
  "296+2T->A": [
    "296+2T->A",
    "p.?",
    "c.164+2T>A"
  ],
  "c.164+2T>A": [
    "296+2T->A",
    "p.?",
    "c.164+2T>A"
  ],
  "1899-1G->A": [
    "1899-1G->A",
    "p.?",
    "c.1767-1G>A"
  ],
  "c.1767-1G>A": [
    "1899-1G->A",
    "p.?",
    "c.1767-1G>A"
  ],
  "c.1767-2A>G": [
    "c.1767-2A>G",
    "1898-2A->G",
    "p.?"
  ],
  "1898-2A->G": [
    "c.1767-2A>G",
    "1898-2A->G",
    "p.?"
  ],
  "2623-1G->C": [
    "p.?",
    "2623-1G->C",
    "c.2491-1G>C"
  ],
  "c.2491-1G>C": [
    "p.?",
    "2623-1G->C",
    "c.2491-1G>C"
  ],
  "2751+1G->A": [
    "2751+1G->A",
    "p.?",
    "c.2619+1G>A"
  ],
  "c.2619+1G>A": [
    "2751+1G->A",
    "p.?",
    "c.2619+1G>A"
  ],
  "c.2658-1G>T": [
    "p.?",
    "c.2658-1G>T",
    "2790-1G->T"
  ],
  "2790-1G->T": [
    "p.?",
    "c.2658-1G>T",
    "2790-1G->T"
  ],
  "c.2988+1G>C": [
    "c.2988+1G>C",
    "p.?",
    "3120+1G->C"
  ],
  "3120+1G->C": [
    "c.2988+1G>C",
    "p.?",
    "3120+1G->C"
  ],
  "c.3139+1G>C": [
    "c.3139+1G>C",
    "p.?",
    "3271+1G->C"
  ],
  "3271+1G->C": [
    "c.3139+1G>C",
    "p.?",
    "3271+1G->C"
  ],
  "3601-1G->T": [
    "p.?",
    "3601-1G->T",
    "c.3469-1G>T"
  ],
  "c.3469-1G>T": [
    "p.?",
    "3601-1G->T",
    "c.3469-1G>T"
  ],
  "3601-2A->C": [
    "3601-2A->C",
    "p.?",
    "c.3469-2A>C"
  ],
  "c.3469-2A>C": [
    "3601-2A->C",
    "p.?",
    "c.3469-2A>C"
  ],
  "4006-2A->G": [
    "p.?",
    "4006-2A->G",
    "c.3874-2A>G"
  ],
  "c.3874-2A>G": [
    "p.?",
    "4006-2A->G",
    "c.3874-2A>G"
  ],
  "c.4136+2T>G": [
    "p.?",
    "c.4136+2T>G",
    "4268+2T->G"
  ],
  "4268+2T->G": [
    "p.?",
    "c.4136+2T>G",
    "4268+2T->G"
  ],
  "622-1G->T": [
    "622-1G->T",
    "p.?",
    "c.490-1G>T"
  ],
  "c.490-1G>T": [
    "622-1G->T",
    "p.?",
    "c.490-1G>T"
  ],
  "c.743+2T>A": [
    "c.743+2T>A",
    "p.?",
    "875+2T->A"
  ],
  "875+2T->A": [
    "c.743+2T>A",
    "p.?",
    "875+2T->A"
  ],
  "c.870-2A>C": [
    "p.?",
    "c.870-2A>C",
    "1002-2A->C"
  ],
  "1002-2A->C": [
    "p.?",
    "c.870-2A>C",
    "1002-2A->C"
  ],
  "4005+1G->T": [
    "p.?",
    "4005+1G->T",
    "c.3873+1G>T"
  ],
  "c.3873+1G>T": [
    "p.?",
    "4005+1G->T",
    "c.3873+1G>T"
  ],
  "c.1210-2_1210-1del": [
    "c.1210-2_1210-1del",
    "p.?",
    "1342-2delAG"
  ],
  "1342-2delAG": [
    "c.1210-2_1210-1del",
    "p.?",
    "1342-2delAG"
  ],
  "c.1871_1878del": [
    "c.1871_1878del",
    "p.Ser624IlefsX15",
    "2003del8"
  ],
  "p.Ser624IlefsX15": [
    "c.1871_1878del",
    "p.Ser624IlefsX15",
    "2003del8"
  ],
  "2003del8": [
    "c.1871_1878del",
    "p.Ser624IlefsX15",
    "2003del8"
  ],
  "p.Asn635IlefsX28": [
    "p.Asn635IlefsX28",
    "c.1904del",
    "2036delA"
  ],
  "c.1904del": [
    "p.Asn635IlefsX28",
    "c.1904del",
    "2036delA"
  ],
  "2036delA": [
    "p.Asn635IlefsX28",
    "c.1904del",
    "2036delA"
  ],
  "2967delG": [
    "2967delG",
    "c.2835del",
    "p.Ile947PhefsX21"
  ],
  "c.2835del": [
    "2967delG",
    "c.2835del",
    "p.Ile947PhefsX21"
  ],
  "p.Ile947PhefsX21": [
    "c.2839del",
    "p.Ile947PhefsX21",
    "c.2839delA"
  ],
  "p.Gly1298GlufsX30": [
    "p.Gly1298GlufsX30",
    "c.3893del",
    "c.3893delG"
  ],
  "c.3893del": [
    "p.Gly1298GlufsX30",
    "c.3893del",
    "c.3893delG"
  ],
  "c.3893delG": [
    "p.Gly1298GlufsX30",
    "c.3893del",
    "c.3893delG"
  ],
  "c.3380_3383del": [
    "c.3380_3383del",
    "p.Gly1127GlufsX6"
  ],
  "p.Gly1127GlufsX6": [
    "c.3380_3383del",
    "p.Gly1127GlufsX6"
  ],
  "1200_1219del20": [
    "p.Trp356X",
    "1200_1219del20",
    "c.1068_1087del"
  ],
  "c.1068_1087del": [
    "p.Trp356X",
    "1200_1219del20",
    "c.1068_1087del"
  ],
  "1204_1205delGT": [
    "1204_1205delGT",
    "c.1072_1073del"
  ],
  "c.1072_1073del": [
    "1204_1205delGT",
    "c.1072_1073del"
  ],
  "1212delA": [
    "p.Trp361GlyfsX8",
    "1212delA",
    "c.1080del"
  ],
  "c.1080del": [
    "p.Trp361GlyfsX8",
    "1212delA",
    "c.1080del"
  ],
  "c.1115delA": [
    "c.1115delA",
    "p.Gln372ArgfsX16",
    "c.1115del"
  ],
  "p.Gln372ArgfsX16": [
    "c.1115delA",
    "p.Gln372ArgfsX16",
    "c.1115del"
  ],
  "c.1115del": [
    "c.1115delA",
    "p.Gln372ArgfsX16",
    "c.1115del"
  ],
  "c.1190dupT": [
    "c.1190dupT",
    "p.Thr398AsnfsX13",
    "c.1190dup"
  ],
  "p.Thr398AsnfsX13": [
    "c.1190dupT",
    "p.Thr398AsnfsX13",
    "c.1190dup"
  ],
  "c.1190dup": [
    "c.1190dupT",
    "p.Thr398AsnfsX13",
    "c.1190dup"
  ],
  "c.1208del": [
    "c.1208del",
    "p.Glu403GlyfsX39",
    "1340delA"
  ],
  "p.Glu403GlyfsX39": [
    "c.1208del",
    "p.Glu403GlyfsX39",
    "1340delA"
  ],
  "1340delA": [
    "c.1208del",
    "p.Glu403GlyfsX39",
    "1340delA"
  ],
  "p.Asn415ThrfsX27": [
    "p.Asn415ThrfsX27",
    "c.1244delA",
    "c.1244del"
  ],
  "c.1244delA": [
    "p.Asn415ThrfsX27",
    "c.1244delA",
    "c.1244del"
  ],
  "c.1244del": [
    "p.Asn415ThrfsX27",
    "c.1244delA",
    "c.1244del"
  ],
  "p.Thr421IlefsX21": [
    "p.Thr421IlefsX21",
    "c.1262delC",
    "c.1262del"
  ],
  "c.1262delC": [
    "p.Thr421IlefsX21",
    "c.1262delC",
    "c.1262del"
  ],
  "c.1262del": [
    "p.Thr421IlefsX21",
    "c.1262delC",
    "c.1262del"
  ],
  "c.147_150del": [
    "c.147_150del",
    "c.147_150delATCT",
    "p.Ser50LysfsX40"
  ],
  "c.147_150delATCT": [
    "c.147_150del",
    "c.147_150delATCT",
    "p.Ser50LysfsX40"
  ],
  "p.Ser50LysfsX40": [
    "c.147_150del",
    "c.147_150delATCT",
    "p.Ser50LysfsX40"
  ],
  "c.1486del": [
    "c.1486del",
    "c.1486delT",
    "p.Trp496GlyfsX31"
  ],
  "c.1486delT": [
    "c.1486del",
    "c.1486delT",
    "p.Trp496GlyfsX31"
  ],
  "p.Trp496GlyfsX31": [
    "c.1486del",
    "c.1486delT",
    "p.Trp496GlyfsX31"
  ],
  "p.Arg516IlefsX51": [
    "p.Arg516IlefsX51",
    "c.1547_1548delGA",
    "c.1547_1548del"
  ],
  "c.1547_1548delGA": [
    "p.Arg516IlefsX51",
    "c.1547_1548delGA",
    "c.1547_1548del"
  ],
  "c.1547_1548del": [
    "p.Arg516IlefsX51",
    "c.1547_1548delGA",
    "c.1547_1548del"
  ],
  "p.Glu528ArgfsX40": [
    "p.Glu528ArgfsX40",
    "c.1581dup",
    "c.1581dupA"
  ],
  "c.1581dup": [
    "p.Glu528ArgfsX40",
    "c.1581dup",
    "c.1581dupA"
  ],
  "c.1581dupA": [
    "p.Glu528ArgfsX40",
    "c.1581dup",
    "c.1581dupA"
  ],
  "1759delG": [
    "1759delG",
    "p.Glu543LysfsX6",
    "c.1627del"
  ],
  "p.Glu543LysfsX6": [
    "1759delG",
    "p.Glu543LysfsX6",
    "c.1627del"
  ],
  "c.1627del": [
    "1759delG",
    "p.Glu543LysfsX6",
    "c.1627del"
  ],
  "c.1652del": [
    "c.1652del",
    "p.Gly551ValfsX8",
    "1784delG"
  ],
  "1784delG": [
    "c.1652del",
    "p.Gly551ValfsX8",
    "1784delG"
  ],
  "1807delG": [
    "1807delG",
    "p.Ala559GlnfsX13",
    "c.1675del"
  ],
  "c.1675del": [
    "1807delG",
    "p.Ala559GlnfsX13",
    "c.1675del"
  ],
  "c.1725_1727delinsAT": [
    "p.Phe575LeufsX4",
    "c.1725_1727delinsAT"
  ],
  "1870delG": [
    "1870delG",
    "c.1738del",
    "p.Val580PhefsX2"
  ],
  "c.1738del": [
    "1870delG",
    "c.1738del",
    "p.Val580PhefsX2"
  ],
  "p.Val580PhefsX2": [
    "1870delG",
    "c.1738del",
    "p.Val580PhefsX2"
  ],
  "c.174dup": [
    "c.174dup",
    "305insT",
    "p.Arg59X"
  ],
  "305insT": [
    "c.174dup",
    "305insT",
    "p.Arg59X"
  ],
  "p.Arg59X": [
    "c.174dup",
    "305insT",
    "p.Arg59X"
  ],
  "p.Glu585LysfsX10": [
    "p.Glu585LysfsX10",
    "c.1753del",
    "c.1753delG"
  ],
  "c.1753del": [
    "p.Glu585LysfsX10",
    "c.1753del",
    "c.1753delG"
  ],
  "c.1753delG": [
    "p.Glu585LysfsX10",
    "c.1753del",
    "c.1753delG"
  ],
  "2025dupA": [
    "2025dupA",
    "p.Glu632ArgfsX10",
    "c.1893dup"
  ],
  "p.Glu632ArgfsX10": [
    "2025dupA",
    "p.Glu632ArgfsX10",
    "c.1893dup"
  ],
  "c.1893dup": [
    "2025dupA",
    "p.Glu632ArgfsX10",
    "c.1893dup"
  ],
  "p.Glu632ThrfsX9": [
    "p.Glu632ThrfsX9",
    "c.1894_1895del"
  ],
  "c.1894_1895del": [
    "p.Glu632ThrfsX9",
    "c.1894_1895del"
  ],
  "c.1970delG": [
    "c.1970delG",
    "c.1970del",
    "p.Arg657LysfsX6"
  ],
  "c.1970del": [
    "c.1970delG",
    "c.1970del",
    "p.Arg657LysfsX6"
  ],
  "p.Arg657LysfsX6": [
    "c.1970delG",
    "c.1970del",
    "p.Arg657LysfsX6"
  ],
  "p.Ser678LeufsX10": [
    "p.Ser678LeufsX10",
    "c.2032_2033del",
    "c.2032_2033delTC"
  ],
  "c.2032_2033del": [
    "p.Ser678LeufsX10",
    "c.2032_2033del",
    "c.2032_2033delTC"
  ],
  "c.2032_2033delTC": [
    "p.Ser678LeufsX10",
    "c.2032_2033del",
    "c.2032_2033delTC"
  ],
  "p.Lys684AsnfsX37": [
    "p.Lys684AsnfsX37",
    "2184del4",
    "c.2052_2055del"
  ],
  "2184del4": [
    "p.Lys684AsnfsX37",
    "2184del4",
    "c.2052_2055del"
  ],
  "c.2052_2055del": [
    "p.Lys684AsnfsX37",
    "2184del4",
    "c.2052_2055del"
  ],
  "c.2053delC": [
    "c.2053delC",
    "c.2053del",
    "p.Gln685AsnfsX37"
  ],
  "c.2053del": [
    "c.2053delC",
    "c.2053del",
    "p.Gln685AsnfsX37"
  ],
  "p.Gln685AsnfsX37": [
    "c.2053delC",
    "c.2053del",
    "p.Gln685AsnfsX37"
  ],
  "2193ins4": [
    "2193ins4",
    "p.Lys688PhefsX2",
    "c.2058_2061dup"
  ],
  "p.Lys688PhefsX2": [
    "2193ins4",
    "p.Lys688PhefsX2",
    "c.2058_2061dup"
  ],
  "c.2058_2061dup": [
    "2193ins4",
    "p.Lys688PhefsX2",
    "c.2058_2061dup"
  ],
  "c.2158_2173del": [
    "c.2158_2173del",
    "2290del16",
    "p.Gln720LysfsX8"
  ],
  "2290del16": [
    "c.2158_2173del",
    "2290del16",
    "p.Gln720LysfsX8"
  ],
  "p.Gln720LysfsX8": [
    "c.2158_2173del",
    "2290del16",
    "p.Gln720LysfsX8"
  ],
  "c.2250del": [
    "c.2250del",
    "c.2250delT",
    "p.Arg751AlafsX4"
  ],
  "c.2250delT": [
    "c.2250del",
    "c.2250delT",
    "p.Arg751AlafsX4"
  ],
  "p.Arg751AlafsX4": [
    "c.2250del",
    "c.2250delT",
    "p.Arg751AlafsX4"
  ],
  "2429delG": [
    "2429delG",
    "c.2298del",
    "p.Arg766SerfsX5"
  ],
  "c.2298del": [
    "2429delG",
    "c.2298del",
    "p.Arg766SerfsX5"
  ],
  "p.Arg766SerfsX5": [
    "2429delG",
    "c.2298del",
    "p.Arg766SerfsX5"
  ],
  "p.Lys793SerfsX11": [
    "p.Lys793SerfsX11",
    "c.2378_2379del",
    "2510delAA"
  ],
  "c.2378_2379del": [
    "p.Lys793SerfsX11",
    "c.2378_2379del",
    "2510delAA"
  ],
  "2510delAA": [
    "p.Lys793SerfsX11",
    "c.2378_2379del",
    "2510delAA"
  ],
  "p.Leu812TyrfsX10": [
    "p.Leu812TyrfsX10",
    "c.2433_2437delinsATA"
  ],
  "c.2433_2437delinsATA": [
    "p.Leu812TyrfsX10",
    "c.2433_2437delinsATA"
  ],
  "c.243delT": [
    "c.243delT",
    "p.Phe81LeufsX10",
    "c.243del"
  ],
  "p.Phe81LeufsX10": [
    "c.243delT",
    "p.Phe81LeufsX10",
    "c.243del"
  ],
  "c.243del": [
    "c.243delT",
    "p.Phe81LeufsX10",
    "c.243del"
  ],
  "c.2467_2470del": [
    "c.2467_2470del",
    "c.2467_2470delGAAA",
    "p.Glu823LeufsX6"
  ],
  "c.2467_2470delGAAA": [
    "c.2467_2470del",
    "c.2467_2470delGAAA",
    "p.Glu823LeufsX6"
  ],
  "p.Glu823LeufsX6": [
    "c.2467_2470del",
    "c.2467_2470delGAAA",
    "p.Glu823LeufsX6"
  ],
  "379-381insT": [
    "379-381insT",
    "c.248dup",
    "p.Tyr84LeufsX27"
  ],
  "c.248dup": [
    "379-381insT",
    "c.248dup",
    "p.Tyr84LeufsX27"
  ],
  "p.Tyr84LeufsX27": [
    "379-381insT",
    "c.248dup",
    "p.Tyr84LeufsX27"
  ],
  "c.2493delG": [
    "c.2493delG",
    "c.2493del",
    "p.Glu831AspfsX13"
  ],
  "c.2493del": [
    "c.2493delG",
    "c.2493del",
    "p.Glu831AspfsX13"
  ],
  "p.Glu831AspfsX13": [
    "c.2493delG",
    "c.2493del",
    "p.Glu831AspfsX13"
  ],
  "c.2540del": [
    "c.2540del",
    "p.Asn847ThrfsX13",
    "2672delA"
  ],
  "p.Asn847ThrfsX13": [
    "c.2540del",
    "p.Asn847ThrfsX13",
    "2672delA"
  ],
  "2672delA": [
    "c.2540del",
    "p.Asn847ThrfsX13",
    "2672delA"
  ],
  "c.2573del": [
    "c.2573del",
    "c.2573delG",
    "p.Ser858ThrfsX2"
  ],
  "c.2573delG": [
    "c.2573del",
    "c.2573delG",
    "p.Ser858ThrfsX2"
  ],
  "p.Ser858ThrfsX2": [
    "c.2573del",
    "c.2573delG",
    "p.Ser858ThrfsX2"
  ],
  "c.2605del": [
    "c.2605del",
    "p.Ile869PhefsX37",
    "2737delA"
  ],
  "p.Ile869PhefsX37": [
    "c.2605del",
    "p.Ile869PhefsX37",
    "2737delA"
  ],
  "2737delA": [
    "c.2605del",
    "p.Ile869PhefsX37",
    "2737delA"
  ],
  "c.2745_2746delGT": [
    "c.2745_2746delGT",
    "p.Phe916LeufsX58",
    "c.2745_2746del"
  ],
  "p.Phe916LeufsX58": [
    "c.2745_2746delGT",
    "p.Phe916LeufsX58",
    "c.2745_2746del"
  ],
  "c.2745_2746del": [
    "c.2745_2746delGT",
    "p.Phe916LeufsX58",
    "c.2745_2746del"
  ],
  "p.Thr940ValfsX30": [
    "p.Thr940ValfsX30",
    "c.2818_2831del"
  ],
  "c.2818_2831del": [
    "p.Thr940ValfsX30",
    "c.2818_2831del"
  ],
  "c.2839del": [
    "c.2839del",
    "p.Ile947PhefsX21",
    "c.2839delA"
  ],
  "c.2839delA": [
    "c.2839del",
    "p.Ile947PhefsX21",
    "c.2839delA"
  ],
  "2975delT": [
    "2975delT",
    "c.2843del",
    "p.Leu948TyrfsX20"
  ],
  "c.2843del": [
    "2975delT",
    "c.2843del",
    "p.Leu948TyrfsX20"
  ],
  "p.Leu948TyrfsX20": [
    "2975delT",
    "c.2843del",
    "p.Leu948TyrfsX20"
  ],
  "p.Phe976TrpfsX4": [
    "p.Phe976TrpfsX4",
    "c.2909_2924dup",
    "c.2909_2924dup16"
  ],
  "c.2909_2924dup": [
    "p.Phe976TrpfsX4",
    "c.2909_2924dup",
    "c.2909_2924dup16"
  ],
  "c.2909_2924dup16": [
    "p.Phe976TrpfsX4",
    "c.2909_2924dup",
    "c.2909_2924dup16"
  ],
  "c.2958_2961del": [
    "c.2958_2961del",
    "3090del4",
    "p.Pro988LeufsX11"
  ],
  "3090del4": [
    "c.2958_2961del",
    "3090del4",
    "p.Pro988LeufsX11"
  ],
  "p.Pro988LeufsX11": [
    "c.2958_2961del",
    "3090del4",
    "p.Pro988LeufsX11"
  ],
  "c.2994del": [
    "c.2994del",
    "3126delA",
    "p.Leu998PhefsX2"
  ],
  "3126delA": [
    "c.2994del",
    "3126delA",
    "p.Leu998PhefsX2"
  ],
  "p.Leu998PhefsX2": [
    "c.2994del",
    "3126delA",
    "p.Leu998PhefsX2"
  ],
  "c.3021del": [
    "c.3021del",
    "p.Val1008SerfsX15",
    "3152delT"
  ],
  "3152delT": [
    "c.3021del",
    "p.Val1008SerfsX15",
    "3152delT"
  ],
  "Q1042TfsX5": [
    "Q1042TfsX5",
    "c.3123dup",
    "p.Gln1042ThrfsX5"
  ],
  "c.3123dup": [
    "Q1042TfsX5",
    "c.3123dup",
    "p.Gln1042ThrfsX5"
  ],
  "p.Gln1042ThrfsX5": [
    "Q1042TfsX5",
    "c.3123dup",
    "p.Gln1042ThrfsX5"
  ],
  "c.3227del": [
    "c.3227del",
    "3359delC",
    "p.Thr1076IlefsX7"
  ],
  "3359delC": [
    "c.3227del",
    "3359delC",
    "p.Thr1076IlefsX7"
  ],
  "p.Thr1076IlefsX7": [
    "c.3227del",
    "3359delC",
    "p.Thr1076IlefsX7"
  ],
  "c.326_327del": [
    "c.326_327del",
    "458delAT",
    "p.Tyr109X"
  ],
  "458delAT": [
    "c.326_327del",
    "458delAT",
    "p.Tyr109X"
  ],
  "c.3321del": [
    "c.3321del",
    "p.Phe1107LeufsX14",
    "3453delT"
  ],
  "p.Phe1107LeufsX14": [
    "c.3321del",
    "p.Phe1107LeufsX14",
    "3453delT"
  ],
  "3453delT": [
    "c.3321del",
    "p.Phe1107LeufsX14",
    "3453delT"
  ],
  "p.Val1108CysfsX48": [
    "p.Val1108CysfsX48",
    "c.3321dup"
  ],
  "c.3321dup": [
    "p.Val1108CysfsX48",
    "c.3321dup"
  ],
  "c.3322_3323delGT": [
    "c.3322_3323delGT",
    "p.Val1108HisfsX47",
    "c.3322_3323del"
  ],
  "p.Val1108HisfsX47": [
    "c.3322_3323delGT",
    "p.Val1108HisfsX47",
    "c.3322_3323del"
  ],
  "c.3322_3323del": [
    "c.3322_3323delGT",
    "p.Val1108HisfsX47",
    "c.3322_3323del"
  ],
  "c.3344_3345insA": [
    "c.3344_3345insA",
    "p.Phe1116LeufsX40"
  ],
  "p.Phe1116LeufsX40": [
    "c.3344_3345insA",
    "p.Phe1116LeufsX40"
  ],
  "c.3411_3414delGAAT": [
    "c.3411_3414delGAAT",
    "p.Met1137IlefsX3",
    "c.3411_3414del"
  ],
  "p.Met1137IlefsX3": [
    "c.3411_3414delGAAT",
    "p.Met1137IlefsX3",
    "c.3411_3414del"
  ],
  "c.3411_3414del": [
    "c.3411_3414delGAAT",
    "p.Met1137IlefsX3",
    "c.3411_3414del"
  ],
  "p.Ser1161GlyfsX30": [
    "p.Ser1161GlyfsX30",
    "3613AGCCGA->GG",
    "c.3481_3486delinsGG"
  ],
  "3613AGCCGA->GG": [
    "p.Ser1161GlyfsX30",
    "3613AGCCGA->GG",
    "c.3481_3486delinsGG"
  ],
  "c.3481_3486delinsGG": [
    "p.Ser1161GlyfsX30",
    "3613AGCCGA->GG",
    "c.3481_3486delinsGG"
  ],
  "c.3524del": [
    "c.3524del",
    "c.3524delC",
    "p.Pro1175LeufsX17"
  ],
  "c.3524delC": [
    "c.3524del",
    "c.3524delC",
    "p.Pro1175LeufsX17"
  ],
  "p.Pro1175LeufsX17": [
    "c.3524del",
    "c.3524delC",
    "p.Pro1175LeufsX17"
  ],
  "p.Ser118LeufsX6": [
    "p.Ser118LeufsX6",
    "c.353del",
    "c.353delC"
  ],
  "c.353del": [
    "p.Ser118LeufsX6",
    "c.353del",
    "c.353delC"
  ],
  "c.353delC": [
    "p.Ser118LeufsX6",
    "c.353del",
    "c.353delC"
  ],
  "p.Ser1188X": [
    "p.Ser1188X",
    "c.3563del",
    "3695delC"
  ],
  "c.3563del": [
    "p.Ser1188X",
    "c.3563del",
    "3695delC"
  ],
  "3695delC": [
    "p.Ser1188X",
    "c.3563del",
    "3695delC"
  ],
  "c.3569_3570del": [
    "c.3569_3570del",
    "c.3569_3570delTT",
    "p.Val1190AspfsX4"
  ],
  "c.3569_3570delTT": [
    "c.3569_3570del",
    "c.3569_3570delTT",
    "p.Val1190AspfsX4"
  ],
  "p.Val1190AspfsX4": [
    "c.3569_3570del",
    "c.3569_3570delTT",
    "p.Val1190AspfsX4"
  ],
  "p.Arg1239GlyfsX20": [
    "p.Arg1239GlyfsX20",
    "c.3715del",
    "3847delA"
  ],
  "c.3715del": [
    "p.Arg1239GlyfsX20",
    "c.3715del",
    "3847delA"
  ],
  "3847delA": [
    "p.Arg1239GlyfsX20",
    "c.3715del",
    "3847delA"
  ],
  "3892delTT": [
    "3892delTT",
    "p.Leu1254IlefsX10",
    "c.3760_3761del"
  ],
  "p.Leu1254IlefsX10": [
    "3892delTT",
    "p.Leu1254IlefsX10",
    "c.3760_3761del"
  ],
  "c.3760_3761del": [
    "3892delTT",
    "p.Leu1254IlefsX10",
    "c.3760_3761del"
  ],
  "c.381_382dup": [
    "c.381_382dup",
    "p.Cys128TyrfsX7"
  ],
  "p.Cys128TyrfsX7": [
    "c.381_382dup",
    "p.Cys128TyrfsX7"
  ],
  "c.3889delT": [
    "c.3889delT",
    "c.3889del",
    "p.Ser1297LeufsX31"
  ],
  "c.3889del": [
    "c.3889delT",
    "c.3889del",
    "p.Ser1297LeufsX31"
  ],
  "p.Ser1297LeufsX31": [
    "c.3889delT",
    "c.3889del",
    "p.Ser1297LeufsX31"
  ],
  "526_527delAT": [
    "526_527delAT",
    "c.394_398del",
    "p.Ile132GlufsX25"
  ],
  "c.394_398del": [
    "526_527delAT",
    "c.394_398del",
    "p.Ile132GlufsX25"
  ],
  "p.Ile132GlufsX25": [
    "526_527delAT",
    "c.394_398del",
    "p.Ile132GlufsX25"
  ],
  "c.3957_3958insAGGG": [
    "c.3957_3958insAGGG",
    "4089ins4",
    "p.Asp1320ArgfsX3"
  ],
  "4089ins4": [
    "c.3957_3958insAGGG",
    "4089ins4",
    "p.Asp1320ArgfsX3"
  ],
  "p.Asp1320ArgfsX3": [
    "c.3957_3958insAGGG",
    "4089ins4",
    "p.Asp1320ArgfsX3"
  ],
  "p.Gln1330ValfsX6": [
    "p.Gln1330ValfsX6",
    "4120delCA",
    "c.3988_3989del"
  ],
  "4120delCA": [
    "p.Gln1330ValfsX6",
    "4120delCA",
    "c.3988_3989del"
  ],
  "c.3988_3989del": [
    "p.Gln1330ValfsX6",
    "4120delCA",
    "c.3988_3989del"
  ],
  "c.3999del": [
    "c.3999del",
    "p.Lys1334SerfsX13",
    "c.3999delG"
  ],
  "p.Lys1334SerfsX13": [
    "c.3999del",
    "p.Lys1334SerfsX13",
    "c.3999delG"
  ],
  "c.3999delG": [
    "c.3999del",
    "p.Lys1334SerfsX13",
    "c.3999delG"
  ],
  "c.4036dup": [
    "c.4036dup",
    "p.Leu1346ProfsX13",
    "c.4036dupC"
  ],
  "p.Leu1346ProfsX13": [
    "c.4036dup",
    "p.Leu1346ProfsX13",
    "c.4036dupC"
  ],
  "c.4036dupC": [
    "c.4036dup",
    "p.Leu1346ProfsX13",
    "c.4036dupC"
  ],
  "4168delCTAAG": [
    "4168delCTAAG",
    "p.Leu1346ProfsX11",
    "c.4037_4041del"
  ],
  "p.Leu1346ProfsX11": [
    "4168delCTAAG",
    "p.Leu1346ProfsX11",
    "c.4037_4041del"
  ],
  "c.4037_4041del": [
    "4168delCTAAG",
    "p.Leu1346ProfsX11",
    "c.4037_4041del"
  ],
  "c.4078del": [
    "c.4078del",
    "p.Val1360PhefsX20",
    "c.4078delG"
  ],
  "p.Val1360PhefsX20": [
    "c.4078del",
    "p.Val1360PhefsX20",
    "c.4078delG"
  ],
  "c.4078delG": [
    "c.4078del",
    "p.Val1360PhefsX20",
    "c.4078delG"
  ],
  "p.Leu1369ArgfsX16": [
    "p.Leu1369ArgfsX16",
    "4237-4242delinsAGAA",
    "c.4105_4110delinsAGAA"
  ],
  "4237-4242delinsAGAA": [
    "p.Leu1369ArgfsX16",
    "4237-4242delinsAGAA",
    "c.4105_4110delinsAGAA"
  ],
  "c.4105_4110delinsAGAA": [
    "p.Leu1369ArgfsX16",
    "4237-4242delinsAGAA",
    "c.4105_4110delinsAGAA"
  ],
  "p.Leu1388ProfsX5": [
    "p.Leu1388ProfsX5",
    "c.4163_4167delTAAAA",
    "c.4163_4167del"
  ],
  "c.4163_4167delTAAAA": [
    "p.Leu1388ProfsX5",
    "c.4163_4167delTAAAA",
    "c.4163_4167del"
  ],
  "c.4163_4167del": [
    "p.Leu1388ProfsX5",
    "c.4163_4167delTAAAA",
    "c.4163_4167del"
  ],
  "c.43dup": [
    "c.43dup",
    "p.Leu15ProfsX30",
    "c.43dupC"
  ],
  "p.Leu15ProfsX30": [
    "c.43dup",
    "p.Leu15ProfsX30",
    "c.43dupC"
  ],
  "c.43dupC": [
    "c.43dup",
    "p.Leu15ProfsX30",
    "c.43dupC"
  ],
  "c.450delG": [
    "c.450delG",
    "c.450del",
    "p.Met150IlefsX3"
  ],
  "c.450del": [
    "c.450delG",
    "c.450del",
    "p.Met150IlefsX3"
  ],
  "p.Met150IlefsX3": [
    "c.450delG",
    "c.450del",
    "p.Met150IlefsX3"
  ],
  "583delC": [
    "583delC",
    "c.451del",
    "p.Gln151ArgfsX2"
  ],
  "c.451del": [
    "583delC",
    "c.451del",
    "p.Gln151ArgfsX2"
  ],
  "p.Gln151ArgfsX2": [
    "583delC",
    "c.451del",
    "p.Gln151ArgfsX2"
  ],
  "c.560delA": [
    "c.560delA",
    "p.Asn187ThrfsX2",
    "c.560del"
  ],
  "p.Asn187ThrfsX2": [
    "c.560delA",
    "p.Asn187ThrfsX2",
    "c.560del"
  ],
  "c.560del": [
    "c.560delA",
    "p.Asn187ThrfsX2",
    "c.560del"
  ],
  "p.Asp192GlufsX23": [
    "p.Asp192GlufsX23",
    "708delT",
    "c.576del"
  ],
  "708delT": [
    "p.Asp192GlufsX23",
    "708delT",
    "c.576del"
  ],
  "c.576del": [
    "p.Asp192GlufsX23",
    "708delT",
    "c.576del"
  ],
  "p.Glu217GlyfsX11": [
    "p.Glu217GlyfsX11",
    "c.650_659del"
  ],
  "c.650_659del": [
    "p.Glu217GlyfsX11",
    "c.650_659del"
  ],
  "p.Leu24X": [
    "p.Leu24X",
    "c.71_72delinsA",
    "c.71_72delTGinsA"
  ],
  "c.71_72delinsA": [
    "p.Leu24X",
    "c.71_72delinsA",
    "c.71_72delTGinsA"
  ],
  "c.71_72delTGinsA": [
    "p.Leu24X",
    "c.71_72delinsA",
    "c.71_72delTGinsA"
  ],
  "c.713_714insA": [
    "c.713_714insA",
    "p.Gly239TrpfsX19",
    "845_846insA"
  ],
  "p.Gly239TrpfsX19": [
    "c.713_714insA",
    "p.Gly239TrpfsX19",
    "845_846insA"
  ],
  "845_846insA": [
    "c.713_714insA",
    "p.Gly239TrpfsX19",
    "845_846insA"
  ],
  "c.811delT": [
    "c.811delT",
    "p.Ser271LeufsX14",
    "c.811del"
  ],
  "p.Ser271LeufsX14": [
    "c.811delT",
    "p.Ser271LeufsX14",
    "c.811del"
  ],
  "c.811del": [
    "c.811delT",
    "p.Ser271LeufsX14",
    "c.811del"
  ],
  "p.Arg289AsnfsX17": [
    "p.Arg289AsnfsX17",
    "c.865_869del",
    "c.865_869delAGACA"
  ],
  "c.865_869del": [
    "p.Arg289AsnfsX17",
    "c.865_869del",
    "c.865_869delAGACA"
  ],
  "c.865_869delAGACA": [
    "p.Arg289AsnfsX17",
    "c.865_869del",
    "c.865_869delAGACA"
  ],
  "c.912delinsGG": [
    "c.912delinsGG",
    "c.912delCinsGG",
    "p.Tyr304X"
  ],
  "c.912delCinsGG": [
    "c.912delinsGG",
    "c.912delCinsGG",
    "p.Tyr304X"
  ],
  "p.Ser313ArgfsX50": [
    "p.Ser313ArgfsX50",
    "c.937_938delTC",
    "c.937_938del"
  ],
  "c.937_938delTC": [
    "p.Ser313ArgfsX50",
    "c.937_938delTC",
    "c.937_938del"
  ],
  "c.937_938del": [
    "p.Ser313ArgfsX50",
    "c.937_938delTC",
    "c.937_938del"
  ],
  "c.942del": [
    "c.942del",
    "p.Phe315SerfsX13",
    "c.942delG"
  ],
  "p.Phe315SerfsX13": [
    "c.942del",
    "p.Phe315SerfsX13",
    "c.942delG"
  ],
  "c.942delG": [
    "c.942del",
    "p.Phe315SerfsX13",
    "c.942delG"
  ],
  "c.972delC": [
    "c.972delC",
    "c.972del",
    "p.Tyr325MetfsX3"
  ],
  "c.972del": [
    "c.972delC",
    "c.972del",
    "p.Tyr325MetfsX3"
  ],
  "p.Tyr325MetfsX3": [
    "c.972delC",
    "c.972del",
    "p.Tyr325MetfsX3"
  ],
  "c.991_995del": [
    "c.991_995del",
    "p.Ile331ProfsX31"
  ],
  "p.Ile331ProfsX31": [
    "c.991_995del",
    "p.Ile331ProfsX31"
  ],
  "c.3678delA": [
    "c.3678delA",
    "c.3678del",
    "p.Leu1227X"
  ],
  "c.3678del": [
    "c.3678delA",
    "c.3678del",
    "p.Leu1227X"
  ],
  "p.Leu1227X": [
    "c.3678delA",
    "c.3678del",
    "p.Leu1227X"
  ],
  "c.1530_1531delTT": [
    "c.1530_1531delTT",
    "p.Ser511LeufsX2",
    "c.1530_1531del"
  ],
  "p.Ser511LeufsX2": [
    "c.1530_1531delTT",
    "p.Ser511LeufsX2",
    "c.1530_1531del"
  ],
  "c.1530_1531del": [
    "c.1530_1531delTT",
    "p.Ser511LeufsX2",
    "c.1530_1531del"
  ],
  "c.2538delG": [
    "c.2538delG",
    "c.2538del",
    "p.Trp846X"
  ],
  "c.2538del": [
    "c.2538delG",
    "c.2538del",
    "p.Trp846X"
  ],
  "3089insTC": [
    "3089insTC",
    "c.2959_2960dup",
    "p.Pro988CysfsX13"
  ],
  "c.2959_2960dup": [
    "3089insTC",
    "c.2959_2960dup",
    "p.Pro988CysfsX13"
  ],
  "p.Pro988CysfsX13": [
    "3089insTC",
    "c.2959_2960dup",
    "p.Pro988CysfsX13"
  ],
  "1474delA": [
    "1474delA",
    "c.1342del",
    "p.Ile448X"
  ],
  "c.1342del": [
    "1474delA",
    "c.1342del",
    "p.Ile448X"
  ],
  "p.Ile448X": [
    "1474delA",
    "c.1342del",
    "p.Ile448X"
  ],
  "1784insATCAT": [
    "1784insATCAT",
    "c.1652_1653insATCAT",
    "p.Gln552SerfsX9"
  ],
  "c.1652_1653insATCAT": [
    "1784insATCAT",
    "c.1652_1653insATCAT",
    "p.Gln552SerfsX9"
  ],
  "p.Gln552SerfsX9": [
    "1784insATCAT",
    "c.1652_1653insATCAT",
    "p.Gln552SerfsX9"
  ],
  "2114delT": [
    "2114delT",
    "p.Ile661ThrfsX2",
    "c.1982del"
  ],
  "p.Ile661ThrfsX2": [
    "2114delT",
    "p.Ile661ThrfsX2",
    "c.1982del"
  ],
  "c.1982del": [
    "2114delT",
    "p.Ile661ThrfsX2",
    "c.1982del"
  ],
  "c.2337del": [
    "c.2337del",
    "p.Gly780ValfsX23",
    "c.2337delA"
  ],
  "p.Gly780ValfsX23": [
    "c.2337del",
    "p.Gly780ValfsX23",
    "c.2337delA"
  ],
  "c.2337delA": [
    "c.2337del",
    "p.Gly780ValfsX23",
    "c.2337delA"
  ],
  "c.2341delC": [
    "c.2341delC",
    "c.2341del",
    "p.Gln781ArgfsX22"
  ],
  "c.2341del": [
    "c.2341delC",
    "c.2341del",
    "p.Gln781ArgfsX22"
  ],
  "p.Gln781ArgfsX22": [
    "c.2341delC",
    "c.2341del",
    "p.Gln781ArgfsX22"
  ],
  "c.264_268del": [
    "c.264_268del",
    "c.264_268delATATT",
    "p.Leu88PhefsX21"
  ],
  "c.264_268delATATT": [
    "c.264_268del",
    "c.264_268delATATT",
    "p.Leu88PhefsX21"
  ],
  "p.Leu88PhefsX21": [
    "c.264_268del",
    "c.264_268delATATT",
    "p.Leu88PhefsX21"
  ],
  "c.2789del": [
    "c.2789del",
    "c.2789delG",
    "p.Gly930AspfsX12"
  ],
  "c.2789delG": [
    "c.2789del",
    "c.2789delG",
    "p.Gly930AspfsX12"
  ],
  "p.Gly930AspfsX12": [
    "c.2789del",
    "c.2789delG",
    "p.Gly930AspfsX12"
  ],
  "3012delT": [
    "3012delT",
    "p.Met961CysfsX7",
    "c.2880del"
  ],
  "p.Met961CysfsX7": [
    "3012delT",
    "p.Met961CysfsX7",
    "c.2880del"
  ],
  "c.2880del": [
    "3012delT",
    "p.Met961CysfsX7",
    "c.2880del"
  ],
  "p.Ala1067ProfsX16": [
    "p.Ala1067ProfsX16",
    "c.3199del",
    "c.3199delG"
  ],
  "c.3199del": [
    "p.Ala1067ProfsX16",
    "c.3199del",
    "c.3199delG"
  ],
  "c.3199delG": [
    "p.Ala1067ProfsX16",
    "c.3199del",
    "c.3199delG"
  ],
  "p.Val1212AlafsX16": [
    "p.Val1212AlafsX16",
    "c.3635del",
    "c.3635delT"
  ],
  "c.3635del": [
    "p.Val1212AlafsX16",
    "c.3635del",
    "c.3635delT"
  ],
  "c.3635delT": [
    "p.Val1212AlafsX16",
    "c.3635del",
    "c.3635delT"
  ],
  "p.His139LeufsX15": [
    "p.His139LeufsX15",
    "547insTA",
    "c.415_416insTA"
  ],
  "547insTA": [
    "p.His139LeufsX15",
    "547insTA",
    "c.415_416insTA"
  ],
  "c.415_416insTA": [
    "p.His139LeufsX15",
    "547insTA",
    "c.415_416insTA"
  ],
  "c.4187delC": [
    "c.4187delC",
    "p.Thr1396LysfsX2",
    "c.4187del"
  ],
  "p.Thr1396LysfsX2": [
    "c.4187delC",
    "p.Thr1396LysfsX2",
    "c.4187del"
  ],
  "c.4187del": [
    "c.4187delC",
    "p.Thr1396LysfsX2",
    "c.4187del"
  ],
  "c.583del": [
    "c.583del",
    "c.583delC",
    "p.Ala196HisfsX19"
  ],
  "c.583delC": [
    "c.583del",
    "c.583delC",
    "p.Ala196HisfsX19"
  ],
  "p.Ala196HisfsX19": [
    "c.583del",
    "c.583delC",
    "p.Ala196HisfsX19"
  ],
  "p.Gln30AlafsX14": [
    "p.Gln30AlafsX14",
    "c.88_89delCA",
    "c.88_89del"
  ],
  "c.88_89delCA": [
    "p.Gln30AlafsX14",
    "c.88_89delCA",
    "c.88_89del"
  ],
  "c.88_89del": [
    "p.Gln30AlafsX14",
    "c.88_89delCA",
    "c.88_89del"
  ],
  "1027delG": [
    "1027delG",
    "p.Ala299GlnfsX4",
    "c.895del"
  ],
  "p.Ala299GlnfsX4": [
    "1027delG",
    "p.Ala299GlnfsX4",
    "c.895del"
  ],
  "c.895del": [
    "1027delG",
    "p.Ala299GlnfsX4",
    "c.895del"
  ],
  "p.Ser531X": [
    "p.Ser531X",
    "S531X",
    "c.1592_1593delinsG"
  ],
  "S531X": [
    "p.Ser531X",
    "S531X",
    "c.1592_1593delinsG"
  ],
  "c.1592_1593delinsG": [
    "p.Ser531X",
    "S531X",
    "c.1592_1593delinsG"
  ],
  "994del9": [
    "994del9",
    "p.?",
    "c.863_869+2del"
  ],
  "c.863_869+2del": [
    "994del9",
    "p.?",
    "c.863_869+2del"
  ],
  "c.1579_1584+11del": [
    "c.1579_1584+11del",
    "p.?",
    "1710del17bp"
  ],
  "1710del17bp": [
    "c.1579_1584+11del",
    "p.?",
    "1710del17bp"
  ],
  "875insTACA": [
    "875insTACA",
    "c.743_743+1insTACA",
    "p.?"
  ],
  "c.743_743+1insTACA": [
    "875insTACA",
    "c.743_743+1insTACA",
    "p.?"
  ],
  "M1R": [
    "M1R",
    "c.2T>G",
    "p.?"
  ],
  "c.2T>G": [
    "M1R",
    "c.2T>G",
    "p.?"
  ],
  "c.273+7982del18652": [
    "c.273+7982del18652",
    "p.?",
    "405+7982del18652"
  ],
  "405+7982del18652": [
    "c.273+7982del18652",
    "p.?",
    "405+7982del18652"
  ],
  "1419delC": [
    "1419delC",
    "p.Phe430SerfsX12",
    "c.1287del"
  ],
  "p.Phe430SerfsX12": [
    "1419delC",
    "p.Phe430SerfsX12",
    "c.1287del"
  ],
  "c.1287del": [
    "1419delC",
    "p.Phe430SerfsX12",
    "c.1287del"
  ],
  "IVS11-1G->C": [
    "IVS11-1G->C"
  ],
  "c.3407_3422del16": [
    "c.3407_3422del16"
  ],
  "CFTRdelePr-1": [
    "CFTRdelePr-1"
  ],
  "3121-977_3499+248del2515": [
    "3121-977_3499+248del2515"
  ],
  "IVSI-5842_IVS4+401del": [
    "IVSI-5842_IVS4+401del"
  ],
  "*Represents the allele frequency within the CFTR2 database. This is subject to regional and ethnic variability of variant distribution and may differ from the worldwide frequency.": [
    "*Represents the allele frequency within the CFTR2 database. This is subject to regional and ethnic variability of variant distribution and may differ from the worldwide frequency."
  ],
  "Permitted use available to clinicians, patients, and family members for clinical, research, and educational uses only. All other rights reserved.": [
    "Permitted use available to clinicians, patients, and family members for clinical, research, and educational uses only. All other rights reserved."
  ],
  "Please use the following reference when citing this document: The Clinical and Functional TRanslation of CFTR (CFTR2); available at https://cftr2.org.": [
    "Please use the following reference when citing this document: The Clinical and Functional TRanslation of CFTR (CFTR2); available at https://cftr2.org."
  ],
  "\u00a9Copyright 2011 US CF Foundation, Johns Hopkins University, The Hospital for Sick Children.": [
    "\u00a9Copyright 2011 US CF Foundation, Johns Hopkins University, The Hospital for Sick Children."
  ]
}
eligible_mutations = ['D1152H', 'L206W', 'R1066H', 'S945L', 'F508del', 'L997F', 'R117C', 'T338I', 'G85E', 'M1101K', 'R347H', 'V232D', 'A455E', 'L1077P', 'P5L', 'R347P', 'N1303K', 'F200L', 'I1139V', 'P574H', 'S1045Y', 'F31del', 'I1257', 'P67L', 'S108F', 'F311L', 'I1269N', 'P750L', 'S1118F', 'F508C', 'I1366N', 'Q129R', 'S1159P', 'F508C;S1251N', 'I148N', 'Q1313K', 'F575Y', 'I1487', 'Q23E', 'S1235R', 'F587I', 'I175V', 'Q237H', 'S1251N', 'G1047R', 'I331N', 'Q359R', 'S1255P', 'G1061R', 'I336K', 'Q327H', 'S13F']
all_known_names = list(alias_lookup.keys())

def check_mutation(mutation):
    mutation = mutation.strip()
    if mutation in eligible_mutations:
        return True, mutation
    if mutation in alias_lookup:
        for alt in alias_lookup[mutation]:
            if alt in eligible_mutations:
                return True, alt
    return False, None

def suggest_similar_mutations(input_mutation, cutoff=0.7):
    return get_close_matches(input_mutation.strip(), all_known_names, n=5, cutoff=cutoff)

st.title("Trikafta Eligibility Checker")
st.write("Enter your patient's two CFTR mutations below to check eligibility for Trikafta.")

mutation1 = st.text_input("Enter First Mutation:")
mutation2 = st.text_input("Enter Second Mutation:")

if st.button("Check Eligibility"):
    if not mutation1 and not mutation2:
        st.warning("Please enter at least one mutation.")
    else:
        eligible1, match1 = check_mutation(mutation1)
        eligible2, match2 = check_mutation(mutation2)

        if eligible1 or eligible2:
            st.success("✅ Patient is eligible for Trikafta!")
            st.write("**Matched Mutation(s):**")
            if eligible1:
                st.write(f"- {mutation1} (matched to {match1})")
            if eligible2:
                st.write(f"- {mutation2} (matched to {match2})")
        else:
            st.error("❌ Patient is NOT eligible for Trikafta based on entered mutations.")
            st.write("### 🔍 Did you mean one of these?")
            if not eligible1:
                suggestions1 = suggest_similar_mutations(mutation1)
                if suggestions1:
                    st.write(f"Suggestions for '{mutation1}':", suggestions1)
            if not eligible2:
                suggestions2 = suggest_similar_mutations(mutation2)
                if suggestions2:
                    st.write(f"Suggestions for '{mutation2}':", suggestions2)

st.markdown("---")
st.caption("Built for CF clinics – 2025")
