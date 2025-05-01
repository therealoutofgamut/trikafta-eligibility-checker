
import streamlit as st

alias_lookup = {
  "Date: 25 September 2024": [
    "Date: 25 September 2024"
  ],
  "Number of patients in CFTR2: 122,935": [
    "Number of patients in CFTR2: 122,935"
  ],
  "Number of variants annotated: 1,167": [
    "Number of variants annotated: 1,167"
  ],
  "CF-causing: 1,085": [
    "CF-causing: 1,085"
  ],
  "Varying clinical consequence: 55": [
    "Varying clinical consequence: 55"
  ],
  "Non CF-causing: 27": [
    "Non CF-causing: 27"
  ],
  "CFTR reference transcript: NM_000492.4": [
    "CFTR reference transcript: NM_000492.4"
  ],
  "This detailed medical and genetics information is complicated and potentially confusing. We encourage you to discuss this information with your doctor, a genetic counselor, or a CF specialist. The information shown is for educational purposes only and is not intended for diagnostic use. You should not make any medical or reproductive decisions or change your health behavior based on this information without talking to your doctor.": [
    "This detailed medical and genetics information is complicated and potentially confusing. We encourage you to discuss this information with your doctor, a genetic counselor, or a CF specialist. The information shown is for educational purposes only and is not intended for diagnostic use. You should not make any medical or reproductive decisions or change your health behavior based on this information without talking to your doctor."
  ],
  "Allele frequency in CFTR2* (of 211106 identified alleles)": [
    "Allele frequency in CFTR2* (of 211106 identified alleles)",
    "# alleles reported in CFTR2",
    "Variant protein name",
    "Variant final determination 25 September 2024 (current version)",
    "Variant cDNA name",
    "Variant legacy name",
    "Variant final determination 7 April 2023 (previous version)",
    "Change from previous?",
    "Variant alternative names (other names that may have been used in the past)"
  ],
  "# alleles reported in CFTR2": [
    "Allele frequency in CFTR2* (of 211106 identified alleles)",
    "# alleles reported in CFTR2",
    "Variant protein name",
    "Variant final determination 25 September 2024 (current version)",
    "Variant cDNA name",
    "Variant legacy name",
    "Variant final determination 7 April 2023 (previous version)",
    "Change from previous?",
    "Variant alternative names (other names that may have been used in the past)"
  ],
  "Variant protein name": [
    "Allele frequency in CFTR2* (of 211106 identified alleles)",
    "# alleles reported in CFTR2",
    "Variant protein name",
    "Variant final determination 25 September 2024 (current version)",
    "Variant cDNA name",
    "Variant legacy name",
    "Variant final determination 7 April 2023 (previous version)",
    "Change from previous?",
    "Variant alternative names (other names that may have been used in the past)"
  ],
  "Variant final determination 25 September 2024 (current version)": [
    "Allele frequency in CFTR2* (of 211106 identified alleles)",
    "# alleles reported in CFTR2",
    "Variant protein name",
    "Variant final determination 25 September 2024 (current version)",
    "Variant cDNA name",
    "Variant legacy name",
    "Variant final determination 7 April 2023 (previous version)",
    "Change from previous?",
    "Variant alternative names (other names that may have been used in the past)"
  ],
  "Variant cDNA name": [
    "Allele frequency in CFTR2* (of 211106 identified alleles)",
    "# alleles reported in CFTR2",
    "Variant protein name",
    "Variant final determination 25 September 2024 (current version)",
    "Variant cDNA name",
    "Variant legacy name",
    "Variant final determination 7 April 2023 (previous version)",
    "Change from previous?",
    "Variant alternative names (other names that may have been used in the past)"
  ],
  "Variant legacy name": [
    "Allele frequency in CFTR2* (of 211106 identified alleles)",
    "# alleles reported in CFTR2",
    "Variant protein name",
    "Variant final determination 25 September 2024 (current version)",
    "Variant cDNA name",
    "Variant legacy name",
    "Variant final determination 7 April 2023 (previous version)",
    "Change from previous?",
    "Variant alternative names (other names that may have been used in the past)"
  ],
  "Variant final determination 7 April 2023 (previous version)": [
    "Allele frequency in CFTR2* (of 211106 identified alleles)",
    "# alleles reported in CFTR2",
    "Variant protein name",
    "Variant final determination 25 September 2024 (current version)",
    "Variant cDNA name",
    "Variant legacy name",
    "Variant final determination 7 April 2023 (previous version)",
    "Change from previous?",
    "Variant alternative names (other names that may have been used in the past)"
  ],
  "Change from previous?": [
    "Allele frequency in CFTR2* (of 211106 identified alleles)",
    "# alleles reported in CFTR2",
    "Variant protein name",
    "Variant final determination 25 September 2024 (current version)",
    "Variant cDNA name",
    "Variant legacy name",
    "Variant final determination 7 April 2023 (previous version)",
    "Change from previous?",
    "Variant alternative names (other names that may have been used in the past)"
  ],
  "Variant alternative names (other names that may have been used in the past)": [
    "Allele frequency in CFTR2* (of 211106 identified alleles)",
    "# alleles reported in CFTR2",
    "Variant protein name",
    "Variant final determination 25 September 2024 (current version)",
    "Variant cDNA name",
    "Variant legacy name",
    "Variant final determination 7 April 2023 (previous version)",
    "Change from previous?",
    "Variant alternative names (other names that may have been used in the past)"
  ],
  "c.1521_1523del": [
    "c.1521_1523del",
    "0.650682595473364",
    "No",
    "137363",
    "F508del",
    "p.Phe508del",
    "CF-causing",
    "c.1521_1523del|1653delCTT"
  ],
  "0.650682595473364": [
    "c.1521_1523del",
    "0.650682595473364",
    "No",
    "137363",
    "F508del",
    "p.Phe508del",
    "CF-causing",
    "c.1521_1523del|1653delCTT"
  ],
  "No": [
    "1419delC",
    "No",
    "CF-causing",
    "c.1287del",
    "0",
    "p.Phe430SerfsX12"
  ],
  "137363": [
    "c.1521_1523del",
    "0.650682595473364",
    "No",
    "137363",
    "F508del",
    "p.Phe508del",
    "CF-causing",
    "c.1521_1523del|1653delCTT"
  ],
  "F508del": [
    "c.1521_1523del",
    "0.650682595473364",
    "No",
    "137363",
    "F508del",
    "p.Phe508del",
    "CF-causing",
    "c.1521_1523del|1653delCTT"
  ],
  "p.Phe508del": [
    "c.1521_1523del",
    "0.650682595473364",
    "No",
    "137363",
    "F508del",
    "p.Phe508del",
    "CF-causing",
    "c.1521_1523del|1653delCTT"
  ],
  "CF-causing": [
    "1419delC",
    "No",
    "CF-causing",
    "c.1287del",
    "0",
    "p.Phe430SerfsX12"
  ],
  "c.1521_1523del|1653delCTT": [
    "c.1521_1523del",
    "0.650682595473364",
    "No",
    "137363",
    "F508del",
    "p.Phe508del",
    "CF-causing",
    "c.1521_1523del|1653delCTT"
  ],
  "0.027246975453089916": [
    "0.027246975453089916",
    "No",
    "p.Gly542X",
    "CF-causing",
    "1756G>T",
    "c.1624G>T",
    "G542X",
    "5752"
  ],
  "p.Gly542X": [
    "0.027246975453089916",
    "No",
    "p.Gly542X",
    "CF-causing",
    "1756G>T",
    "c.1624G>T",
    "G542X",
    "5752"
  ],
  "1756G>T": [
    "0.027246975453089916",
    "No",
    "p.Gly542X",
    "CF-causing",
    "1756G>T",
    "c.1624G>T",
    "G542X",
    "5752"
  ],
  "c.1624G>T": [
    "0.027246975453089916",
    "No",
    "p.Gly542X",
    "CF-causing",
    "1756G>T",
    "c.1624G>T",
    "G542X",
    "5752"
  ],
  "G542X": [
    "0.027246975453089916",
    "No",
    "p.Gly542X",
    "CF-causing",
    "1756G>T",
    "c.1624G>T",
    "G542X",
    "5752"
  ],
  "5752": [
    "0.027246975453089916",
    "No",
    "p.Gly542X",
    "CF-causing",
    "1756G>T",
    "c.1624G>T",
    "G542X",
    "5752"
  ],
  "3831": [
    "No",
    "3831",
    "p.Gly551Asp",
    "CF-causing",
    "c.1652G>A",
    "0.01814728146049852",
    "1784G>A",
    "G551D"
  ],
  "p.Gly551Asp": [
    "No",
    "3831",
    "p.Gly551Asp",
    "CF-causing",
    "c.1652G>A",
    "0.01814728146049852",
    "1784G>A",
    "G551D"
  ],
  "c.1652G>A": [
    "No",
    "3831",
    "p.Gly551Asp",
    "CF-causing",
    "c.1652G>A",
    "0.01814728146049852",
    "1784G>A",
    "G551D"
  ],
  "0.01814728146049852": [
    "No",
    "3831",
    "p.Gly551Asp",
    "CF-causing",
    "c.1652G>A",
    "0.01814728146049852",
    "1784G>A",
    "G551D"
  ],
  "1784G>A": [
    "No",
    "3831",
    "p.Gly551Asp",
    "CF-causing",
    "c.1652G>A",
    "0.01814728146049852",
    "1784G>A",
    "G551D"
  ],
  "G551D": [
    "No",
    "3831",
    "p.Gly551Asp",
    "CF-causing",
    "c.1652G>A",
    "0.01814728146049852",
    "1784G>A",
    "G551D"
  ],
  "0.01682093355944407": [
    "0.01682093355944407",
    "N1303K",
    "p.Asn1303Lys",
    "No",
    "4041C>G",
    "3551",
    "CF-causing",
    "c.3909C>G"
  ],
  "N1303K": [
    "0.01682093355944407",
    "N1303K",
    "p.Asn1303Lys",
    "No",
    "4041C>G",
    "3551",
    "CF-causing",
    "c.3909C>G"
  ],
  "p.Asn1303Lys": [
    "0.01682093355944407",
    "N1303K",
    "p.Asn1303Lys",
    "No",
    "4041C>G",
    "3551",
    "CF-causing",
    "c.3909C>G"
  ],
  "4041C>G": [
    "0.01682093355944407",
    "N1303K",
    "p.Asn1303Lys",
    "No",
    "4041C>G",
    "3551",
    "CF-causing",
    "c.3909C>G"
  ],
  "3551": [
    "0.01682093355944407",
    "N1303K",
    "p.Asn1303Lys",
    "No",
    "4041C>G",
    "3551",
    "CF-causing",
    "c.3909C>G"
  ],
  "c.3909C>G": [
    "0.01682093355944407",
    "N1303K",
    "p.Asn1303Lys",
    "No",
    "4041C>G",
    "3551",
    "CF-causing",
    "c.3909C>G"
  ],
  "W1282X": [
    "W1282X",
    "No",
    "c.3845G>A|c.3846G>A",
    "0.011842391973700416",
    "3978G>A",
    "CF-causing",
    "p.Trp1282X",
    "2500"
  ],
  "c.3845G>A|c.3846G>A": [
    "W1282X",
    "No",
    "c.3845G>A|c.3846G>A",
    "0.011842391973700416",
    "3978G>A",
    "CF-causing",
    "p.Trp1282X",
    "2500"
  ],
  "0.011842391973700416": [
    "W1282X",
    "No",
    "c.3845G>A|c.3846G>A",
    "0.011842391973700416",
    "3978G>A",
    "CF-causing",
    "p.Trp1282X",
    "2500"
  ],
  "3978G>A": [
    "W1282X",
    "No",
    "c.3845G>A|c.3846G>A",
    "0.011842391973700416",
    "3978G>A",
    "CF-causing",
    "p.Trp1282X",
    "2500"
  ],
  "p.Trp1282X": [
    "W1282X",
    "No",
    "c.3845G>A|c.3846G>A",
    "0.011842391973700416",
    "3978G>A",
    "CF-causing",
    "p.Trp1282X",
    "2500"
  ],
  "2500": [
    "W1282X",
    "No",
    "c.3845G>A|c.3846G>A",
    "0.011842391973700416",
    "3978G>A",
    "CF-causing",
    "p.Trp1282X",
    "2500"
  ],
  "0.010714996257804137": [
    "0.010714996257804137",
    "No",
    "482G>A",
    "p.Arg117His",
    "2262",
    "Varying clinical consequence",
    "R117H",
    "c.350G>A"
  ],
  "482G>A": [
    "0.010714996257804137",
    "No",
    "482G>A",
    "p.Arg117His",
    "2262",
    "Varying clinical consequence",
    "R117H",
    "c.350G>A"
  ],
  "p.Arg117His": [
    "0.010714996257804137",
    "No",
    "482G>A",
    "p.Arg117His",
    "2262",
    "Varying clinical consequence",
    "R117H",
    "c.350G>A"
  ],
  "2262": [
    "0.010714996257804137",
    "No",
    "482G>A",
    "p.Arg117His",
    "2262",
    "Varying clinical consequence",
    "R117H",
    "c.350G>A"
  ],
  "Varying clinical consequence": [
    "c.2770G>A",
    "2902G>A",
    "4",
    "Varying clinical consequence",
    "Yes",
    "D924N",
    "p.Asp924Asn",
    "Unknown significance",
    "1.8947827157920666e-05"
  ],
  "R117H": [
    "0.010714996257804137",
    "No",
    "482G>A",
    "p.Arg117His",
    "2262",
    "Varying clinical consequence",
    "R117H",
    "c.350G>A"
  ],
  "c.350G>A": [
    "0.010714996257804137",
    "No",
    "482G>A",
    "p.Arg117His",
    "2262",
    "Varying clinical consequence",
    "R117H",
    "c.350G>A"
  ],
  "c.3717+12191C>T|3850-2477C->T|3849+12191C->T": [
    "c.3717+12191C>T|3850-2477C->T|3849+12191C->T",
    "p.?",
    "0.00942654401106553",
    "No",
    "c.3718-2477C>T",
    "CF-causing",
    "3849+10kbC->T",
    "1990"
  ],
  "p.?": [
    "c.273+7982del18652",
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "405+7982del18652"
  ],
  "0.00942654401106553": [
    "c.3717+12191C>T|3850-2477C->T|3849+12191C->T",
    "p.?",
    "0.00942654401106553",
    "No",
    "c.3718-2477C>T",
    "CF-causing",
    "3849+10kbC->T",
    "1990"
  ],
  "c.3718-2477C>T": [
    "c.3717+12191C>T|3850-2477C->T|3849+12191C->T",
    "p.?",
    "0.00942654401106553",
    "No",
    "c.3718-2477C>T",
    "CF-causing",
    "3849+10kbC->T",
    "1990"
  ],
  "3849+10kbC->T": [
    "c.3717+12191C>T|3850-2477C->T|3849+12191C->T",
    "p.?",
    "0.00942654401106553",
    "No",
    "c.3718-2477C>T",
    "CF-causing",
    "3849+10kbC->T",
    "1990"
  ],
  "1990": [
    "c.3717+12191C>T|3850-2477C->T|3849+12191C->T",
    "p.?",
    "0.00942654401106553",
    "No",
    "c.3718-2477C>T",
    "CF-causing",
    "3849+10kbC->T",
    "1990"
  ],
  "0.008810739628433109": [
    "p.?",
    "No",
    "0.008810739628433109",
    "c.489+1G>T",
    "CF-causing",
    "1860",
    "621+1G->T"
  ],
  "c.489+1G>T": [
    "p.?",
    "No",
    "0.008810739628433109",
    "c.489+1G>T",
    "CF-causing",
    "1860",
    "621+1G->T"
  ],
  "1860": [
    "p.?",
    "No",
    "0.008810739628433109",
    "c.489+1G>T",
    "CF-causing",
    "1860",
    "621+1G->T"
  ],
  "621+1G->T": [
    "p.?",
    "No",
    "0.008810739628433109",
    "c.489+1G>T",
    "CF-causing",
    "1860",
    "621+1G->T"
  ],
  "p.Arg553X": [
    "p.Arg553X",
    "No",
    "1789C>T",
    "0.008526522221064299",
    "CF-causing",
    "c.1657C>T",
    "1800",
    "R553X"
  ],
  "1789C>T": [
    "p.Arg553X",
    "No",
    "1789C>T",
    "0.008526522221064299",
    "CF-causing",
    "c.1657C>T",
    "1800",
    "R553X"
  ],
  "0.008526522221064299": [
    "p.Arg553X",
    "No",
    "1789C>T",
    "0.008526522221064299",
    "CF-causing",
    "c.1657C>T",
    "1800",
    "R553X"
  ],
  "c.1657C>T": [
    "p.Arg553X",
    "No",
    "1789C>T",
    "0.008526522221064299",
    "CF-causing",
    "c.1657C>T",
    "1800",
    "R553X"
  ],
  "1800": [
    "p.Arg553X",
    "No",
    "1789C>T",
    "0.008526522221064299",
    "CF-causing",
    "c.1657C>T",
    "1800",
    "R553X"
  ],
  "R553X": [
    "p.Arg553X",
    "No",
    "1789C>T",
    "0.008526522221064299",
    "CF-causing",
    "c.1657C>T",
    "1800",
    "R553X"
  ],
  "c.2657+5G>A": [
    "c.2657+5G>A",
    "p.?",
    "No",
    "2789+5G->A",
    "0.008431783085274695",
    "CF-causing",
    "1780"
  ],
  "2789+5G->A": [
    "c.2657+5G>A",
    "p.?",
    "No",
    "2789+5G->A",
    "0.008431783085274695",
    "CF-causing",
    "1780"
  ],
  "0.008431783085274695": [
    "c.2657+5G>A",
    "p.?",
    "No",
    "2789+5G->A",
    "0.008431783085274695",
    "CF-causing",
    "1780"
  ],
  "1780": [
    "c.2657+5G>A",
    "p.?",
    "No",
    "2789+5G->A",
    "0.008431783085274695",
    "CF-causing",
    "1780"
  ],
  "c.1585-1G>A": [
    "c.1585-1G>A",
    "p.?",
    "No",
    "CF-causing",
    "1717-1G->A",
    "0.008218620029748089",
    "1735"
  ],
  "1717-1G->A": [
    "c.1585-1G>A",
    "p.?",
    "No",
    "CF-causing",
    "1717-1G->A",
    "0.008218620029748089",
    "1735"
  ],
  "0.008218620029748089": [
    "c.1585-1G>A",
    "p.?",
    "No",
    "CF-causing",
    "1717-1G->A",
    "0.008218620029748089",
    "1735"
  ],
  "1735": [
    "c.1585-1G>A",
    "p.?",
    "No",
    "CF-causing",
    "1717-1G->A",
    "0.008218620029748089",
    "1735"
  ],
  "1321": [
    "p.?",
    "No",
    "1321",
    "0.006257519918903299",
    "c.(53+1_54-1)_(273+1_274-1)del",
    "CF-causing",
    "deletion of exons 2 and 3 (legacy and current numbering)",
    "CFTRdele2,3"
  ],
  "0.006257519918903299": [
    "p.?",
    "No",
    "1321",
    "0.006257519918903299",
    "c.(53+1_54-1)_(273+1_274-1)del",
    "CF-causing",
    "deletion of exons 2 and 3 (legacy and current numbering)",
    "CFTRdele2,3"
  ],
  "c.(53+1_54-1)_(273+1_274-1)del": [
    "p.?",
    "No",
    "1321",
    "0.006257519918903299",
    "c.(53+1_54-1)_(273+1_274-1)del",
    "CF-causing",
    "deletion of exons 2 and 3 (legacy and current numbering)",
    "CFTRdele2,3"
  ],
  "deletion of exons 2 and 3 (legacy and current numbering)": [
    "p.?",
    "No",
    "1321",
    "0.006257519918903299",
    "c.(53+1_54-1)_(273+1_274-1)del",
    "CF-causing",
    "deletion of exons 2 and 3 (legacy and current numbering)",
    "CFTRdele2,3"
  ],
  "CFTRdele2,3": [
    "p.?",
    "No",
    "1321",
    "0.006257519918903299",
    "c.(53+1_54-1)_(273+1_274-1)del",
    "CF-causing",
    "deletion of exons 2 and 3 (legacy and current numbering)",
    "CFTRdele2,3"
  ],
  "3586G>C": [
    "3586G>C",
    "No",
    "D1152H",
    "0.005613293795533997",
    "Varying clinical consequence",
    "1185",
    "p.Asp1152His",
    "c.3454G>C"
  ],
  "D1152H": [
    "3586G>C",
    "No",
    "D1152H",
    "0.005613293795533997",
    "Varying clinical consequence",
    "1185",
    "p.Asp1152His",
    "c.3454G>C"
  ],
  "0.005613293795533997": [
    "3586G>C",
    "No",
    "D1152H",
    "0.005613293795533997",
    "Varying clinical consequence",
    "1185",
    "p.Asp1152His",
    "c.3454G>C"
  ],
  "1185": [
    "3586G>C",
    "No",
    "D1152H",
    "0.005613293795533997",
    "Varying clinical consequence",
    "1185",
    "p.Asp1152His",
    "c.3454G>C"
  ],
  "p.Asp1152His": [
    "3586G>C",
    "No",
    "D1152H",
    "0.005613293795533997",
    "Varying clinical consequence",
    "1185",
    "p.Asp1152His",
    "c.3454G>C"
  ],
  "c.3454G>C": [
    "3586G>C",
    "No",
    "D1152H",
    "0.005613293795533997",
    "Varying clinical consequence",
    "1185",
    "p.Asp1152His",
    "c.3454G>C"
  ],
  "0.005248548122744025": [
    "0.005248548122744025",
    "G85E",
    "No",
    "c.254G>A",
    "386G>A",
    "CF-causing",
    "1108",
    "p.Gly85Glu"
  ],
  "G85E": [
    "0.005248548122744025",
    "G85E",
    "No",
    "c.254G>A",
    "386G>A",
    "CF-causing",
    "1108",
    "p.Gly85Glu"
  ],
  "c.254G>A": [
    "0.005248548122744025",
    "G85E",
    "No",
    "c.254G>A",
    "386G>A",
    "CF-causing",
    "1108",
    "p.Gly85Glu"
  ],
  "386G>A": [
    "0.005248548122744025",
    "G85E",
    "No",
    "c.254G>A",
    "386G>A",
    "CF-causing",
    "1108",
    "p.Gly85Glu"
  ],
  "1108": [
    "0.005248548122744025",
    "G85E",
    "No",
    "c.254G>A",
    "386G>A",
    "CF-causing",
    "1108",
    "p.Gly85Glu"
  ],
  "p.Gly85Glu": [
    "0.005248548122744025",
    "G85E",
    "No",
    "c.254G>A",
    "386G>A",
    "CF-causing",
    "1108",
    "p.Gly85Glu"
  ],
  "R1162X": [
    "No",
    "R1162X",
    "c.3484C>T",
    "CF-causing",
    "3616C>T",
    "1080",
    "p.Arg1162X",
    "0.00511591333263858"
  ],
  "c.3484C>T": [
    "No",
    "R1162X",
    "c.3484C>T",
    "CF-causing",
    "3616C>T",
    "1080",
    "p.Arg1162X",
    "0.00511591333263858"
  ],
  "3616C>T": [
    "No",
    "R1162X",
    "c.3484C>T",
    "CF-causing",
    "3616C>T",
    "1080",
    "p.Arg1162X",
    "0.00511591333263858"
  ],
  "1080": [
    "No",
    "R1162X",
    "c.3484C>T",
    "CF-causing",
    "3616C>T",
    "1080",
    "p.Arg1162X",
    "0.00511591333263858"
  ],
  "p.Arg1162X": [
    "No",
    "R1162X",
    "c.3484C>T",
    "CF-causing",
    "3616C>T",
    "1080",
    "p.Arg1162X",
    "0.00511591333263858"
  ],
  "0.00511591333263858": [
    "No",
    "R1162X",
    "c.3484C>T",
    "CF-causing",
    "3616C>T",
    "1080",
    "p.Arg1162X",
    "0.00511591333263858"
  ],
  "1132C>T": [
    "1132C>T",
    "No",
    "977",
    "CF-causing",
    "0.004628006783322123",
    "p.Arg334Trp",
    "c.1000C>T",
    "R334W"
  ],
  "977": [
    "1132C>T",
    "No",
    "977",
    "CF-causing",
    "0.004628006783322123",
    "p.Arg334Trp",
    "c.1000C>T",
    "R334W"
  ],
  "0.004628006783322123": [
    "1132C>T",
    "No",
    "977",
    "CF-causing",
    "0.004628006783322123",
    "p.Arg334Trp",
    "c.1000C>T",
    "R334W"
  ],
  "p.Arg334Trp": [
    "1132C>T",
    "No",
    "977",
    "CF-causing",
    "0.004628006783322123",
    "p.Arg334Trp",
    "c.1000C>T",
    "R334W"
  ],
  "c.1000C>T": [
    "1132C>T",
    "No",
    "977",
    "CF-causing",
    "0.004628006783322123",
    "p.Arg334Trp",
    "c.1000C>T",
    "R334W"
  ],
  "R334W": [
    "1132C>T",
    "No",
    "977",
    "CF-causing",
    "0.004628006783322123",
    "p.Arg334Trp",
    "c.1000C>T",
    "R334W"
  ],
  "c.3140-26A>G": [
    "p.?",
    "No",
    "c.3140-26A>G",
    "0.004613795912953682",
    "CF-causing",
    "974",
    "3272-26A->G"
  ],
  "0.004613795912953682": [
    "p.?",
    "No",
    "c.3140-26A>G",
    "0.004613795912953682",
    "CF-causing",
    "974",
    "3272-26A->G"
  ],
  "974": [
    "p.?",
    "No",
    "c.3140-26A>G",
    "0.004613795912953682",
    "CF-causing",
    "974",
    "3272-26A->G"
  ],
  "3272-26A->G": [
    "p.?",
    "No",
    "c.3140-26A>G",
    "0.004613795912953682",
    "CF-causing",
    "974",
    "3272-26A->G"
  ],
  "3120+1G->A": [
    "p.?",
    "No",
    "3120+1G->A",
    "0.004509582863585118",
    "CF-causing",
    "c.2988+1G>A",
    "952"
  ],
  "0.004509582863585118": [
    "p.?",
    "No",
    "3120+1G->A",
    "0.004509582863585118",
    "CF-causing",
    "c.2988+1G>A",
    "952"
  ],
  "c.2988+1G>A": [
    "p.?",
    "No",
    "3120+1G->A",
    "0.004509582863585118",
    "CF-causing",
    "c.2988+1G>A",
    "952"
  ],
  "952": [
    "p.?",
    "No",
    "3120+1G->A",
    "0.004509582863585118",
    "CF-causing",
    "c.2988+1G>A",
    "952"
  ],
  "2183delAA->G": [
    "2183delAA->G",
    "0.004452739382111356",
    "940",
    "No",
    "2183AA->G",
    "c.2051_2052delinsG",
    "p.Lys684SerfsX38",
    "CF-causing"
  ],
  "0.004452739382111356": [
    "2183delAA->G",
    "0.004452739382111356",
    "940",
    "No",
    "2183AA->G",
    "c.2051_2052delinsG",
    "p.Lys684SerfsX38",
    "CF-causing"
  ],
  "940": [
    "2183delAA->G",
    "0.004452739382111356",
    "940",
    "No",
    "2183AA->G",
    "c.2051_2052delinsG",
    "p.Lys684SerfsX38",
    "CF-causing"
  ],
  "2183AA->G": [
    "2183delAA->G",
    "0.004452739382111356",
    "940",
    "No",
    "2183AA->G",
    "c.2051_2052delinsG",
    "p.Lys684SerfsX38",
    "CF-causing"
  ],
  "c.2051_2052delinsG": [
    "2183delAA->G",
    "0.004452739382111356",
    "940",
    "No",
    "2183AA->G",
    "c.2051_2052delinsG",
    "p.Lys684SerfsX38",
    "CF-causing"
  ],
  "p.Lys684SerfsX38": [
    "2183delAA->G",
    "0.004452739382111356",
    "940",
    "No",
    "2183AA->G",
    "c.2051_2052delinsG",
    "p.Lys684SerfsX38",
    "CF-causing"
  ],
  "c.1519_1521del|c.1516_1518delATC|I506del|p.Ile506del|1651delATC": [
    "c.1519_1521del|c.1516_1518delATC|I506del|p.Ile506del|1651delATC",
    "p.Ile507del",
    "875",
    "No",
    "c.1519_1521del",
    "CF-causing",
    "I507del",
    "0.0041448371907951455"
  ],
  "p.Ile507del": [
    "c.1519_1521del|c.1516_1518delATC|I506del|p.Ile506del|1651delATC",
    "p.Ile507del",
    "875",
    "No",
    "c.1519_1521del",
    "CF-causing",
    "I507del",
    "0.0041448371907951455"
  ],
  "875": [
    "c.1519_1521del|c.1516_1518delATC|I506del|p.Ile506del|1651delATC",
    "p.Ile507del",
    "875",
    "No",
    "c.1519_1521del",
    "CF-causing",
    "I507del",
    "0.0041448371907951455"
  ],
  "c.1519_1521del": [
    "c.1519_1521del|c.1516_1518delATC|I506del|p.Ile506del|1651delATC",
    "p.Ile507del",
    "875",
    "No",
    "c.1519_1521del",
    "CF-causing",
    "I507del",
    "0.0041448371907951455"
  ],
  "I507del": [
    "c.1519_1521del|c.1516_1518delATC|I506del|p.Ile506del|1651delATC",
    "p.Ile507del",
    "875",
    "No",
    "c.1519_1521del",
    "CF-causing",
    "I507del",
    "0.0041448371907951455"
  ],
  "0.0041448371907951455": [
    "c.1519_1521del|c.1516_1518delATC|I506del|p.Ile506del|1651delATC",
    "p.Ile507del",
    "875",
    "No",
    "c.1519_1521del",
    "CF-causing",
    "I507del",
    "0.0041448371907951455"
  ],
  "p.Arg347Pro": [
    "p.Arg347Pro",
    "No",
    "1172G>C",
    "c.1040G>C",
    "CF-causing",
    "867",
    "0.004106941536479304",
    "R347P"
  ],
  "1172G>C": [
    "p.Arg347Pro",
    "No",
    "1172G>C",
    "c.1040G>C",
    "CF-causing",
    "867",
    "0.004106941536479304",
    "R347P"
  ],
  "c.1040G>C": [
    "p.Arg347Pro",
    "No",
    "1172G>C",
    "c.1040G>C",
    "CF-causing",
    "867",
    "0.004106941536479304",
    "R347P"
  ],
  "867": [
    "p.Arg347Pro",
    "No",
    "1172G>C",
    "c.1040G>C",
    "CF-causing",
    "867",
    "0.004106941536479304",
    "R347P"
  ],
  "0.004106941536479304": [
    "p.Arg347Pro",
    "No",
    "1172G>C",
    "c.1040G>C",
    "CF-causing",
    "867",
    "0.004106941536479304",
    "R347P"
  ],
  "R347P": [
    "p.Arg347Pro",
    "No",
    "1172G>C",
    "c.1040G>C",
    "CF-causing",
    "867",
    "0.004106941536479304",
    "R347P"
  ],
  "848": [
    "No",
    "848",
    "CF-causing",
    "c.2052_2053insA|2185insA",
    "0.004016939357479181",
    "2184insA",
    "c.2052dup",
    "p.Gln685ThrfsX4"
  ],
  "c.2052_2053insA|2185insA": [
    "No",
    "848",
    "CF-causing",
    "c.2052_2053insA|2185insA",
    "0.004016939357479181",
    "2184insA",
    "c.2052dup",
    "p.Gln685ThrfsX4"
  ],
  "0.004016939357479181": [
    "No",
    "848",
    "CF-causing",
    "c.2052_2053insA|2185insA",
    "0.004016939357479181",
    "2184insA",
    "c.2052dup",
    "p.Gln685ThrfsX4"
  ],
  "2184insA": [
    "No",
    "848",
    "CF-causing",
    "c.2052_2053insA|2185insA",
    "0.004016939357479181",
    "2184insA",
    "c.2052dup",
    "p.Gln685ThrfsX4"
  ],
  "c.2052dup": [
    "No",
    "848",
    "CF-causing",
    "c.2052_2053insA|2185insA",
    "0.004016939357479181",
    "2184insA",
    "c.2052dup",
    "p.Gln685ThrfsX4"
  ],
  "p.Gln685ThrfsX4": [
    "No",
    "13",
    "CF-causing",
    "2176insC",
    "6.158043826324216e-05",
    "c.2045dup",
    "p.Gln685ThrfsX4"
  ],
  "p.Lys1177SerfsX15": [
    "p.Lys1177SerfsX15",
    "No",
    "3662delA",
    "4",
    "CF-causing",
    "c.3530del",
    "1.8947827157920666e-05"
  ],
  "0.003510084981004803": [
    "p.Lys1177SerfsX15",
    "0.003510084981004803",
    "No",
    "CF-causing",
    "741",
    "3659delC",
    "c.3528del"
  ],
  "741": [
    "p.Lys1177SerfsX15",
    "0.003510084981004803",
    "No",
    "CF-causing",
    "741",
    "3659delC",
    "c.3528del"
  ],
  "3659delC": [
    "p.Lys1177SerfsX15",
    "0.003510084981004803",
    "No",
    "CF-causing",
    "741",
    "3659delC",
    "c.3528del"
  ],
  "c.3528del": [
    "p.Lys1177SerfsX15",
    "0.003510084981004803",
    "No",
    "CF-causing",
    "741",
    "3659delC",
    "c.3528del"
  ],
  "c.617T>G": [
    "c.617T>G",
    "p.Leu206Trp",
    "0.003386924104478319",
    "No",
    "CF-causing",
    "715",
    "749T>G",
    "L206W"
  ],
  "p.Leu206Trp": [
    "c.617T>G",
    "p.Leu206Trp",
    "0.003386924104478319",
    "No",
    "CF-causing",
    "715",
    "749T>G",
    "L206W"
  ],
  "0.003386924104478319": [
    "c.617T>G",
    "p.Leu206Trp",
    "0.003386924104478319",
    "No",
    "CF-causing",
    "715",
    "749T>G",
    "L206W"
  ],
  "715": [
    "c.617T>G",
    "p.Leu206Trp",
    "0.003386924104478319",
    "No",
    "CF-causing",
    "715",
    "749T>G",
    "L206W"
  ],
  "749T>G": [
    "c.617T>G",
    "p.Leu206Trp",
    "0.003386924104478319",
    "No",
    "CF-causing",
    "715",
    "749T>G",
    "L206W"
  ],
  "L206W": [
    "c.617T>G",
    "p.Leu206Trp",
    "0.003386924104478319",
    "No",
    "CF-causing",
    "715",
    "749T>G",
    "L206W"
  ],
  "5T": [
    "5T",
    "p.?",
    "No",
    "c.1210-12T[5]",
    "Varying clinical consequence",
    "710",
    "0.0033632393205309183"
  ],
  "c.1210-12T[5]": [
    "5T",
    "p.?",
    "No",
    "c.1210-12T[5]",
    "Varying clinical consequence",
    "710",
    "0.0033632393205309183"
  ],
  "710": [
    "5T",
    "p.?",
    "No",
    "c.1210-12T[5]",
    "Varying clinical consequence",
    "710",
    "0.0033632393205309183"
  ],
  "0.0033632393205309183": [
    "5T",
    "p.?",
    "No",
    "c.1210-12T[5]",
    "Varying clinical consequence",
    "710",
    "0.0033632393205309183"
  ],
  "0.003334817579794037": [
    "No",
    "0.003334817579794037",
    "c.1364C>A",
    "CF-causing",
    "1496C>A",
    "p.Ala455Glu",
    "704",
    "A455E"
  ],
  "c.1364C>A": [
    "No",
    "0.003334817579794037",
    "c.1364C>A",
    "CF-causing",
    "1496C>A",
    "p.Ala455Glu",
    "704",
    "A455E"
  ],
  "1496C>A": [
    "No",
    "0.003334817579794037",
    "c.1364C>A",
    "CF-causing",
    "1496C>A",
    "p.Ala455Glu",
    "704",
    "A455E"
  ],
  "p.Ala455Glu": [
    "No",
    "0.003334817579794037",
    "c.1364C>A",
    "CF-causing",
    "1496C>A",
    "p.Ala455Glu",
    "704",
    "A455E"
  ],
  "704": [
    "No",
    "0.003334817579794037",
    "c.1364C>A",
    "CF-causing",
    "1496C>A",
    "p.Ala455Glu",
    "704",
    "A455E"
  ],
  "A455E": [
    "No",
    "0.003334817579794037",
    "c.1364C>A",
    "CF-causing",
    "1496C>A",
    "p.Ala455Glu",
    "704",
    "A455E"
  ],
  "5T;TG12": [
    "5T;TG12",
    "p.?",
    "c.1210-11T>G",
    "0.002927439295898743",
    "No",
    "618",
    "Varying clinical consequence",
    "c.1210-33_1210-6GT[12]T[4]"
  ],
  "c.1210-11T>G": [
    "5T;TG12",
    "p.?",
    "c.1210-11T>G",
    "0.002927439295898743",
    "No",
    "618",
    "Varying clinical consequence",
    "c.1210-33_1210-6GT[12]T[4]"
  ],
  "0.002927439295898743": [
    "5T;TG12",
    "p.?",
    "c.1210-11T>G",
    "0.002927439295898743",
    "No",
    "618",
    "Varying clinical consequence",
    "c.1210-33_1210-6GT[12]T[4]"
  ],
  "618": [
    "5T;TG12",
    "p.?",
    "c.1210-11T>G",
    "0.002927439295898743",
    "No",
    "618",
    "Varying clinical consequence",
    "c.1210-33_1210-6GT[12]T[4]"
  ],
  "c.1210-33_1210-6GT[12]T[4]": [
    "5T;TG12",
    "p.?",
    "c.1210-11T>G",
    "0.002927439295898743",
    "No",
    "618",
    "Varying clinical consequence",
    "c.1210-33_1210-6GT[12]T[4]"
  ],
  "603": [
    "603",
    "p.?",
    "c.1766+1G>A",
    "No",
    "1898+1G->A",
    "CF-causing",
    "0.0028563849440565404"
  ],
  "c.1766+1G>A": [
    "603",
    "p.?",
    "c.1766+1G>A",
    "No",
    "1898+1G->A",
    "CF-causing",
    "0.0028563849440565404"
  ],
  "1898+1G->A": [
    "603",
    "p.?",
    "c.1766+1G>A",
    "No",
    "1898+1G->A",
    "CF-causing",
    "0.0028563849440565404"
  ],
  "0.0028563849440565404": [
    "603",
    "p.?",
    "c.1766+1G>A",
    "No",
    "1898+1G->A",
    "CF-causing",
    "0.0028563849440565404"
  ],
  "0.0025200610120034487": [
    "No",
    "0.0025200610120034487",
    "R1066C",
    "CF-causing",
    "3328C>T",
    "c.3196C>T",
    "p.Arg1066Cys",
    "532"
  ],
  "R1066C": [
    "No",
    "0.0025200610120034487",
    "R1066C",
    "CF-causing",
    "3328C>T",
    "c.3196C>T",
    "p.Arg1066Cys",
    "532"
  ],
  "3328C>T": [
    "No",
    "0.0025200610120034487",
    "R1066C",
    "CF-causing",
    "3328C>T",
    "c.3196C>T",
    "p.Arg1066Cys",
    "532"
  ],
  "c.3196C>T": [
    "No",
    "0.0025200610120034487",
    "R1066C",
    "CF-causing",
    "3328C>T",
    "c.3196C>T",
    "p.Arg1066Cys",
    "532"
  ],
  "p.Arg1066Cys": [
    "No",
    "0.0025200610120034487",
    "R1066C",
    "CF-causing",
    "3328C>T",
    "c.3196C>T",
    "p.Arg1066Cys",
    "532"
  ],
  "532": [
    "No",
    "0.0025200610120034487",
    "R1066C",
    "CF-causing",
    "3328C>T",
    "c.3196C>T",
    "p.Arg1066Cys",
    "532"
  ],
  "517": [
    "517",
    "No",
    "0.002449006660161246",
    "CF-causing",
    "p.Tyr515X",
    "1677delTA",
    "c.1545_1546del"
  ],
  "0.002449006660161246": [
    "517",
    "No",
    "0.002449006660161246",
    "CF-causing",
    "p.Tyr515X",
    "1677delTA",
    "c.1545_1546del"
  ],
  "p.Tyr515X": [
    "517",
    "No",
    "0.002449006660161246",
    "CF-causing",
    "p.Tyr515X",
    "1677delTA",
    "c.1545_1546del"
  ],
  "1677delTA": [
    "517",
    "No",
    "0.002449006660161246",
    "CF-causing",
    "p.Tyr515X",
    "1677delTA",
    "c.1545_1546del"
  ],
  "c.1545_1546del": [
    "517",
    "No",
    "0.002449006660161246",
    "CF-causing",
    "p.Tyr515X",
    "1677delTA",
    "c.1545_1546del"
  ],
  "[482G>A with 1342-12T[7]]|R117H with 7T": [
    "No",
    "[482G>A with 1342-12T[7]]|R117H with 7T",
    "477",
    "Varying clinical consequence",
    "0.002259528388582039",
    "c.[350G>A;1210-12T[7]]",
    "R117H;7T"
  ],
  "477": [
    "394delTT",
    "No",
    "477",
    "p.Leu88IlefsX22",
    "CF-causing",
    "0.002259528388582039",
    "c.262_263del"
  ],
  "0.002259528388582039": [
    "394delTT",
    "No",
    "477",
    "p.Leu88IlefsX22",
    "CF-causing",
    "0.002259528388582039",
    "c.262_263del"
  ],
  "c.[350G>A;1210-12T[7]]": [
    "No",
    "[482G>A with 1342-12T[7]]|R117H with 7T",
    "477",
    "Varying clinical consequence",
    "0.002259528388582039",
    "c.[350G>A;1210-12T[7]]",
    "R117H;7T"
  ],
  "R117H;7T": [
    "No",
    "[482G>A with 1342-12T[7]]|R117H with 7T",
    "477",
    "Varying clinical consequence",
    "0.002259528388582039",
    "c.[350G>A;1210-12T[7]]",
    "R117H;7T"
  ],
  "394delTT": [
    "394delTT",
    "No",
    "477",
    "p.Leu88IlefsX22",
    "CF-causing",
    "0.002259528388582039",
    "c.262_263del"
  ],
  "p.Leu88IlefsX22": [
    "394delTT",
    "No",
    "477",
    "p.Leu88IlefsX22",
    "CF-causing",
    "0.002259528388582039",
    "c.262_263del"
  ],
  "c.262_263del": [
    "394delTT",
    "No",
    "477",
    "p.Leu88IlefsX22",
    "CF-causing",
    "0.002259528388582039",
    "c.262_263del"
  ],
  "0.0021268935984765946": [
    "0.0021268935984765946",
    "p.?",
    "No",
    "c.579+1G>T",
    "CF-causing",
    "449",
    "711+1G->T"
  ],
  "c.579+1G>T": [
    "0.0021268935984765946",
    "p.?",
    "No",
    "c.579+1G>T",
    "CF-causing",
    "449",
    "711+1G->T"
  ],
  "449": [
    "0.0021268935984765946",
    "p.?",
    "No",
    "c.579+1G>T",
    "CF-causing",
    "449",
    "711+1G->T"
  ],
  "711+1G->T": [
    "0.0021268935984765946",
    "p.?",
    "No",
    "c.579+1G>T",
    "CF-causing",
    "449",
    "711+1G->T"
  ],
  "R560T": [
    "R560T",
    "No",
    "c.1679G>C",
    "CF-causing",
    "p.Arg560Thr",
    "0.002051102289844912",
    "1811G>C",
    "433"
  ],
  "c.1679G>C": [
    "R560T",
    "No",
    "c.1679G>C",
    "CF-causing",
    "p.Arg560Thr",
    "0.002051102289844912",
    "1811G>C",
    "433"
  ],
  "p.Arg560Thr": [
    "R560T",
    "No",
    "c.1679G>C",
    "CF-causing",
    "p.Arg560Thr",
    "0.002051102289844912",
    "1811G>C",
    "433"
  ],
  "0.002051102289844912": [
    "R560T",
    "No",
    "c.1679G>C",
    "CF-causing",
    "p.Arg560Thr",
    "0.002051102289844912",
    "1811G>C",
    "433"
  ],
  "1811G>C": [
    "R560T",
    "No",
    "c.1679G>C",
    "CF-causing",
    "p.Arg560Thr",
    "0.002051102289844912",
    "1811G>C",
    "433"
  ],
  "433": [
    "R560T",
    "No",
    "c.1679G>C",
    "CF-causing",
    "p.Arg560Thr",
    "0.002051102289844912",
    "1811G>C",
    "433"
  ],
  "Q493X": [
    "Q493X",
    "No",
    "c.1477C>T",
    "0.002013206635529071",
    "CF-causing",
    "p.Gln493X",
    "425",
    "1609C>T"
  ],
  "c.1477C>T": [
    "Q493X",
    "No",
    "c.1477C>T",
    "0.002013206635529071",
    "CF-causing",
    "p.Gln493X",
    "425",
    "1609C>T"
  ],
  "0.002013206635529071": [
    "Q493X",
    "No",
    "c.1477C>T",
    "0.002013206635529071",
    "CF-causing",
    "p.Gln493X",
    "425",
    "1609C>T"
  ],
  "p.Gln493X": [
    "Q493X",
    "No",
    "c.1477C>T",
    "0.002013206635529071",
    "CF-causing",
    "p.Gln493X",
    "425",
    "1609C>T"
  ],
  "425": [
    "Q493X",
    "No",
    "c.1477C>T",
    "0.002013206635529071",
    "CF-causing",
    "p.Gln493X",
    "425",
    "1609C>T"
  ],
  "1609C>T": [
    "Q493X",
    "No",
    "c.1477C>T",
    "0.002013206635529071",
    "CF-causing",
    "p.Gln493X",
    "425",
    "1609C>T"
  ],
  "422": [
    "No",
    "CF-causing",
    "422",
    "2184delA",
    "0.00199899576516063",
    "c.2052del",
    "p.Lys684AsnfsX38"
  ],
  "2184delA": [
    "No",
    "CF-causing",
    "422",
    "2184delA",
    "0.00199899576516063",
    "c.2052del",
    "p.Lys684AsnfsX38"
  ],
  "0.00199899576516063": [
    "No",
    "CF-causing",
    "422",
    "2184delA",
    "0.00199899576516063",
    "c.2052del",
    "p.Lys684AsnfsX38"
  ],
  "c.2052del": [
    "No",
    "CF-causing",
    "422",
    "2184delA",
    "0.00199899576516063",
    "c.2052del",
    "p.Lys684AsnfsX38"
  ],
  "p.Lys684AsnfsX38": [
    "No",
    "CF-causing",
    "422",
    "2184delA",
    "0.00199899576516063",
    "c.2052del",
    "p.Lys684AsnfsX38"
  ],
  "1540A>G": [
    "1540A>G",
    "No",
    "M470V",
    "p.Met470Val",
    "0.001961100110844789",
    "Non CF-causing",
    "c.1408A>G",
    "414"
  ],
  "M470V": [
    "1540A>G",
    "No",
    "M470V",
    "p.Met470Val",
    "0.001961100110844789",
    "Non CF-causing",
    "c.1408A>G",
    "414"
  ],
  "p.Met470Val": [
    "1540A>G",
    "No",
    "M470V",
    "p.Met470Val",
    "0.001961100110844789",
    "Non CF-causing",
    "c.1408A>G",
    "414"
  ],
  "0.001961100110844789": [
    "1540A>G",
    "No",
    "M470V",
    "p.Met470Val",
    "0.001961100110844789",
    "Non CF-causing",
    "c.1408A>G",
    "414"
  ],
  "Non CF-causing": [
    "No",
    "c.958T>G",
    "9",
    "Non CF-causing",
    "p.Leu320Val",
    "L320V",
    "4.26326111053215e-05",
    "1090T>G"
  ],
  "c.1408A>G": [
    "1540A>G",
    "No",
    "M470V",
    "p.Met470Val",
    "0.001961100110844789",
    "Non CF-causing",
    "c.1408A>G",
    "414"
  ],
  "414": [
    "1540A>G",
    "No",
    "M470V",
    "p.Met470Val",
    "0.001961100110844789",
    "Non CF-causing",
    "c.1408A>G",
    "414"
  ],
  "411": [
    "411",
    "E60X",
    "No",
    "c.178G>T",
    "p.Glu60X",
    "CF-causing",
    "310G>T",
    "0.0019468892404763483"
  ],
  "E60X": [
    "411",
    "E60X",
    "No",
    "c.178G>T",
    "p.Glu60X",
    "CF-causing",
    "310G>T",
    "0.0019468892404763483"
  ],
  "c.178G>T": [
    "411",
    "E60X",
    "No",
    "c.178G>T",
    "p.Glu60X",
    "CF-causing",
    "310G>T",
    "0.0019468892404763483"
  ],
  "p.Glu60X": [
    "411",
    "E60X",
    "No",
    "c.178G>T",
    "p.Glu60X",
    "CF-causing",
    "310G>T",
    "0.0019468892404763483"
  ],
  "310G>T": [
    "411",
    "E60X",
    "No",
    "c.178G>T",
    "p.Glu60X",
    "CF-causing",
    "310G>T",
    "0.0019468892404763483"
  ],
  "0.0019468892404763483": [
    "411",
    "E60X",
    "No",
    "c.178G>T",
    "p.Glu60X",
    "CF-causing",
    "310G>T",
    "0.0019468892404763483"
  ],
  "p.Pro67Leu": [
    "p.Pro67Leu",
    "No",
    "332C>T",
    "P67L",
    "c.200C>T",
    "CF-causing",
    "404",
    "0.0019137305429499873"
  ],
  "332C>T": [
    "p.Pro67Leu",
    "No",
    "332C>T",
    "P67L",
    "c.200C>T",
    "CF-causing",
    "404",
    "0.0019137305429499873"
  ],
  "P67L": [
    "p.Pro67Leu",
    "No",
    "332C>T",
    "P67L",
    "c.200C>T",
    "CF-causing",
    "404",
    "0.0019137305429499873"
  ],
  "c.200C>T": [
    "p.Pro67Leu",
    "No",
    "332C>T",
    "P67L",
    "c.200C>T",
    "CF-causing",
    "404",
    "0.0019137305429499873"
  ],
  "404": [
    "p.Pro67Leu",
    "No",
    "332C>T",
    "P67L",
    "c.200C>T",
    "CF-causing",
    "404",
    "0.0019137305429499873"
  ],
  "0.0019137305429499873": [
    "p.Pro67Leu",
    "No",
    "332C>T",
    "P67L",
    "c.200C>T",
    "CF-causing",
    "404",
    "0.0019137305429499873"
  ],
  "p.Phe342HisfsX28": [
    "No",
    "p.Phe342HisfsX28",
    "CF-causing",
    "c.1022_1023insTC",
    "c.1021_1022dup",
    "0.001733726184949741",
    "366",
    "1154insTC"
  ],
  "c.1022_1023insTC": [
    "No",
    "p.Phe342HisfsX28",
    "CF-causing",
    "c.1022_1023insTC",
    "c.1021_1022dup",
    "0.001733726184949741",
    "366",
    "1154insTC"
  ],
  "c.1021_1022dup": [
    "No",
    "p.Phe342HisfsX28",
    "CF-causing",
    "c.1022_1023insTC",
    "c.1021_1022dup",
    "0.001733726184949741",
    "366",
    "1154insTC"
  ],
  "0.001733726184949741": [
    "No",
    "p.Phe342HisfsX28",
    "CF-causing",
    "c.1022_1023insTC",
    "c.1021_1022dup",
    "0.001733726184949741",
    "366",
    "1154insTC"
  ],
  "366": [
    "No",
    "p.Phe342HisfsX28",
    "CF-causing",
    "c.1022_1023insTC",
    "c.1021_1022dup",
    "0.001733726184949741",
    "366",
    "1154insTC"
  ],
  "1154insTC": [
    "No",
    "p.Phe342HisfsX28",
    "CF-causing",
    "c.1022_1023insTC",
    "c.1021_1022dup",
    "0.001733726184949741",
    "366",
    "1154insTC"
  ],
  "p.Arg117Cys": [
    "p.Arg117Cys",
    "No",
    "365",
    "0.0017289892281602607",
    "CF-causing",
    "481C>T",
    "R117C",
    "c.349C>T"
  ],
  "365": [
    "p.Arg117Cys",
    "No",
    "365",
    "0.0017289892281602607",
    "CF-causing",
    "481C>T",
    "R117C",
    "c.349C>T"
  ],
  "0.0017289892281602607": [
    "p.Arg117Cys",
    "No",
    "365",
    "0.0017289892281602607",
    "CF-causing",
    "481C>T",
    "R117C",
    "c.349C>T"
  ],
  "481C>T": [
    "p.Arg117Cys",
    "No",
    "365",
    "0.0017289892281602607",
    "CF-causing",
    "481C>T",
    "R117C",
    "c.349C>T"
  ],
  "R117C": [
    "p.Arg117Cys",
    "No",
    "365",
    "0.0017289892281602607",
    "CF-causing",
    "481C>T",
    "R117C",
    "c.349C>T"
  ],
  "c.349C>T": [
    "p.Arg117Cys",
    "No",
    "365",
    "0.0017289892281602607",
    "CF-causing",
    "481C>T",
    "R117C",
    "c.349C>T"
  ],
  "R347H": [
    "No",
    "R347H",
    "p.Arg347His",
    "CF-causing",
    "0.00171004140100234",
    "1172G>A",
    "c.1040G>A",
    "361"
  ],
  "p.Arg347His": [
    "No",
    "R347H",
    "p.Arg347His",
    "CF-causing",
    "0.00171004140100234",
    "1172G>A",
    "c.1040G>A",
    "361"
  ],
  "0.00171004140100234": [
    "No",
    "R347H",
    "p.Arg347His",
    "CF-causing",
    "0.00171004140100234",
    "1172G>A",
    "c.1040G>A",
    "361"
  ],
  "1172G>A": [
    "No",
    "R347H",
    "p.Arg347His",
    "CF-causing",
    "0.00171004140100234",
    "1172G>A",
    "c.1040G>A",
    "361"
  ],
  "c.1040G>A": [
    "No",
    "R347H",
    "p.Arg347His",
    "CF-causing",
    "0.00171004140100234",
    "1172G>A",
    "c.1040G>A",
    "361"
  ],
  "361": [
    "No",
    "R347H",
    "p.Arg347His",
    "CF-causing",
    "0.00171004140100234",
    "1172G>A",
    "c.1040G>A",
    "361"
  ],
  "Y1092X(C->A)|Y1092X(C->G)|3408C>A|3408C>G": [
    "Y1092X(C->A)|Y1092X(C->G)|3408C>A|3408C>G",
    "Y1092X",
    "No",
    "c.3276C>A|c.3276C>G",
    "CF-causing",
    "357",
    "0.0016910935738444193",
    "p.Tyr1092X"
  ],
  "Y1092X": [
    "Y1092X(C->A)|Y1092X(C->G)|3408C>A|3408C>G",
    "Y1092X",
    "No",
    "c.3276C>A|c.3276C>G",
    "CF-causing",
    "357",
    "0.0016910935738444193",
    "p.Tyr1092X"
  ],
  "c.3276C>A|c.3276C>G": [
    "Y1092X(C->A)|Y1092X(C->G)|3408C>A|3408C>G",
    "Y1092X",
    "No",
    "c.3276C>A|c.3276C>G",
    "CF-causing",
    "357",
    "0.0016910935738444193",
    "p.Tyr1092X"
  ],
  "357": [
    "Y1092X(C->A)|Y1092X(C->G)|3408C>A|3408C>G",
    "Y1092X",
    "No",
    "c.3276C>A|c.3276C>G",
    "CF-causing",
    "357",
    "0.0016910935738444193",
    "p.Tyr1092X"
  ],
  "0.0016910935738444193": [
    "Y1092X(C->A)|Y1092X(C->G)|3408C>A|3408C>G",
    "Y1092X",
    "No",
    "c.3276C>A|c.3276C>G",
    "CF-causing",
    "357",
    "0.0016910935738444193",
    "p.Tyr1092X"
  ],
  "p.Tyr1092X": [
    "Y1092X(C->A)|Y1092X(C->G)|3408C>A|3408C>G",
    "Y1092X",
    "No",
    "c.3276C>A|c.3276C>G",
    "CF-causing",
    "357",
    "0.0016910935738444193",
    "p.Tyr1092X"
  ],
  "R1158X": [
    "No",
    "R1158X",
    "p.Arg1158X",
    "c.3472C>T",
    "354",
    "CF-causing",
    "0.0016768827034759788",
    "3604C>T"
  ],
  "p.Arg1158X": [
    "No",
    "R1158X",
    "p.Arg1158X",
    "c.3472C>T",
    "354",
    "CF-causing",
    "0.0016768827034759788",
    "3604C>T"
  ],
  "c.3472C>T": [
    "No",
    "R1158X",
    "p.Arg1158X",
    "c.3472C>T",
    "354",
    "CF-causing",
    "0.0016768827034759788",
    "3604C>T"
  ],
  "354": [
    "No",
    "R1158X",
    "p.Arg1158X",
    "c.3472C>T",
    "354",
    "CF-causing",
    "0.0016768827034759788",
    "3604C>T"
  ],
  "0.0016768827034759788": [
    "No",
    "R1158X",
    "p.Arg1158X",
    "c.3472C>T",
    "354",
    "CF-causing",
    "0.0016768827034759788",
    "3604C>T"
  ],
  "3604C>T": [
    "No",
    "R1158X",
    "p.Arg1158X",
    "c.3472C>T",
    "354",
    "CF-causing",
    "0.0016768827034759788",
    "3604C>T"
  ],
  "0.0016626718331075384": [
    "0.0016626718331075384",
    "c.274G>A",
    "No",
    "CF-causing",
    "351",
    "p.Glu92Lys",
    "E92K",
    "406G>A"
  ],
  "p.Met1101Lys": [
    "0.0016626718331075384",
    "No",
    "CF-causing",
    "p.Met1101Lys",
    "3434T>A",
    "c.3302T>A",
    "351",
    "M1101K"
  ],
  "3434T>A": [
    "0.0016626718331075384",
    "No",
    "CF-causing",
    "p.Met1101Lys",
    "3434T>A",
    "c.3302T>A",
    "351",
    "M1101K"
  ],
  "c.3302T>A": [
    "0.0016626718331075384",
    "No",
    "CF-causing",
    "p.Met1101Lys",
    "3434T>A",
    "c.3302T>A",
    "351",
    "M1101K"
  ],
  "351": [
    "0.0016626718331075384",
    "c.274G>A",
    "No",
    "CF-causing",
    "351",
    "p.Glu92Lys",
    "E92K",
    "406G>A"
  ],
  "M1101K": [
    "0.0016626718331075384",
    "No",
    "CF-causing",
    "p.Met1101Lys",
    "3434T>A",
    "c.3302T>A",
    "351",
    "M1101K"
  ],
  "c.274G>A": [
    "0.0016626718331075384",
    "c.274G>A",
    "No",
    "CF-causing",
    "351",
    "p.Glu92Lys",
    "E92K",
    "406G>A"
  ],
  "p.Glu92Lys": [
    "0.0016626718331075384",
    "c.274G>A",
    "No",
    "CF-causing",
    "351",
    "p.Glu92Lys",
    "E92K",
    "406G>A"
  ],
  "E92K": [
    "0.0016626718331075384",
    "c.274G>A",
    "No",
    "CF-causing",
    "351",
    "p.Glu92Lys",
    "E92K",
    "406G>A"
  ],
  "406G>A": [
    "0.0016626718331075384",
    "c.274G>A",
    "No",
    "CF-causing",
    "351",
    "p.Glu92Lys",
    "E92K",
    "406G>A"
  ],
  "c.3773dup": [
    "No",
    "c.3773dup",
    "330",
    "3905insT",
    "CF-causing",
    "p.Leu1258PhefsX7",
    "0.0015631957405284548",
    "c.3773_3774insT"
  ],
  "330": [
    "No",
    "c.3773dup",
    "330",
    "3905insT",
    "CF-causing",
    "p.Leu1258PhefsX7",
    "0.0015631957405284548",
    "c.3773_3774insT"
  ],
  "3905insT": [
    "No",
    "c.3773dup",
    "330",
    "3905insT",
    "CF-causing",
    "p.Leu1258PhefsX7",
    "0.0015631957405284548",
    "c.3773_3774insT"
  ],
  "p.Leu1258PhefsX7": [
    "4.7369567894801664e-06",
    "3898insC",
    "No",
    "CF-causing",
    "1",
    "p.Leu1258PhefsX7",
    "c.3767dup"
  ],
  "0.0015631957405284548": [
    "No",
    "c.3773dup",
    "330",
    "3905insT",
    "CF-causing",
    "p.Leu1258PhefsX7",
    "0.0015631957405284548",
    "c.3773_3774insT"
  ],
  "c.3773_3774insT": [
    "No",
    "c.3773dup",
    "330",
    "3905insT",
    "CF-causing",
    "p.Leu1258PhefsX7",
    "0.0015631957405284548",
    "c.3773_3774insT"
  ],
  "p.Leu671X": [
    "p.Leu671X",
    "2144delT",
    "0.0015537218269494947",
    "No",
    "CF-causing",
    "2143delT",
    "c.2012del",
    "328"
  ],
  "2144delT": [
    "p.Leu671X",
    "2144delT",
    "0.0015537218269494947",
    "No",
    "CF-causing",
    "2143delT",
    "c.2012del",
    "328"
  ],
  "0.0015537218269494947": [
    "p.Leu671X",
    "2144delT",
    "0.0015537218269494947",
    "No",
    "CF-causing",
    "2143delT",
    "c.2012del",
    "328"
  ],
  "2143delT": [
    "p.Leu671X",
    "2144delT",
    "0.0015537218269494947",
    "No",
    "CF-causing",
    "2143delT",
    "c.2012del",
    "328"
  ],
  "c.2012del": [
    "p.Leu671X",
    "2144delT",
    "0.0015537218269494947",
    "No",
    "CF-causing",
    "2143delT",
    "c.2012del",
    "328"
  ],
  "328": [
    "p.Leu671X",
    "2144delT",
    "0.0015537218269494947",
    "No",
    "CF-causing",
    "2143delT",
    "c.2012del",
    "328"
  ],
  "0.001506352259054693": [
    "0.001506352259054693",
    "No",
    "1778G>A",
    "c.1646G>A",
    "CF-causing",
    "S549N",
    "p.Ser549Asn",
    "318"
  ],
  "1778G>A": [
    "0.001506352259054693",
    "No",
    "1778G>A",
    "c.1646G>A",
    "CF-causing",
    "S549N",
    "p.Ser549Asn",
    "318"
  ],
  "c.1646G>A": [
    "0.001506352259054693",
    "No",
    "1778G>A",
    "c.1646G>A",
    "CF-causing",
    "S549N",
    "p.Ser549Asn",
    "318"
  ],
  "S549N": [
    "0.001506352259054693",
    "No",
    "1778G>A",
    "c.1646G>A",
    "CF-causing",
    "S549N",
    "p.Ser549Asn",
    "318"
  ],
  "p.Ser549Asn": [
    "0.001506352259054693",
    "No",
    "1778G>A",
    "c.1646G>A",
    "CF-causing",
    "S549N",
    "p.Ser549Asn",
    "318"
  ],
  "318": [
    "0.001506352259054693",
    "No",
    "1778G>A",
    "c.1646G>A",
    "CF-causing",
    "S549N",
    "p.Ser549Asn",
    "318"
  ],
  "304": [
    "304",
    "R117H;5T",
    "No",
    "CF-causing",
    "0.00144003486400197",
    "c.[350G>A;1210-11T>G]",
    "[482G>A with 1342-12T[5]]|R117H with 5T"
  ],
  "R117H;5T": [
    "304",
    "R117H;5T",
    "No",
    "CF-causing",
    "0.00144003486400197",
    "c.[350G>A;1210-11T>G]",
    "[482G>A with 1342-12T[5]]|R117H with 5T"
  ],
  "0.00144003486400197": [
    "304",
    "R117H;5T",
    "No",
    "CF-causing",
    "0.00144003486400197",
    "c.[350G>A;1210-11T>G]",
    "[482G>A with 1342-12T[5]]|R117H with 5T"
  ],
  "c.[350G>A;1210-11T>G]": [
    "304",
    "R117H;5T",
    "No",
    "CF-causing",
    "0.00144003486400197",
    "c.[350G>A;1210-11T>G]",
    "[482G>A with 1342-12T[5]]|R117H with 5T"
  ],
  "[482G>A with 1342-12T[5]]|R117H with 5T": [
    "304",
    "R117H;5T",
    "No",
    "CF-causing",
    "0.00144003486400197",
    "c.[350G>A;1210-11T>G]",
    "[482G>A with 1342-12T[5]]|R117H with 5T"
  ],
  "S945L": [
    "S945L",
    "c.2834C>T",
    "0.0014021392096861293",
    "No",
    "p.Ser945Leu",
    "2966C>T",
    "CF-causing",
    "296"
  ],
  "c.2834C>T": [
    "S945L",
    "c.2834C>T",
    "0.0014021392096861293",
    "No",
    "p.Ser945Leu",
    "2966C>T",
    "CF-causing",
    "296"
  ],
  "0.0014021392096861293": [
    "S945L",
    "c.2834C>T",
    "0.0014021392096861293",
    "No",
    "p.Ser945Leu",
    "2966C>T",
    "CF-causing",
    "296"
  ],
  "p.Ser945Leu": [
    "S945L",
    "c.2834C>T",
    "0.0014021392096861293",
    "No",
    "p.Ser945Leu",
    "2966C>T",
    "CF-causing",
    "296"
  ],
  "2966C>T": [
    "S945L",
    "c.2834C>T",
    "0.0014021392096861293",
    "No",
    "p.Ser945Leu",
    "2966C>T",
    "CF-causing",
    "296"
  ],
  "296": [
    "S945L",
    "c.2834C>T",
    "0.0014021392096861293",
    "No",
    "p.Ser945Leu",
    "2966C>T",
    "CF-causing",
    "296"
  ],
  "253": [
    "253",
    "No",
    "1078delT",
    "p.Phe316LeufsX12",
    "0.0011984500677384821",
    "CF-causing",
    "c.948del",
    "1080delT"
  ],
  "1078delT": [
    "253",
    "No",
    "1078delT",
    "p.Phe316LeufsX12",
    "0.0011984500677384821",
    "CF-causing",
    "c.948del",
    "1080delT"
  ],
  "p.Phe316LeufsX12": [
    "253",
    "No",
    "1078delT",
    "p.Phe316LeufsX12",
    "0.0011984500677384821",
    "CF-causing",
    "c.948del",
    "1080delT"
  ],
  "0.0011984500677384821": [
    "253",
    "No",
    "1078delT",
    "p.Phe316LeufsX12",
    "0.0011984500677384821",
    "CF-causing",
    "c.948del",
    "1080delT"
  ],
  "c.948del": [
    "253",
    "No",
    "1078delT",
    "p.Phe316LeufsX12",
    "0.0011984500677384821",
    "CF-causing",
    "c.948del",
    "1080delT"
  ],
  "1080delT": [
    "253",
    "No",
    "1078delT",
    "p.Phe316LeufsX12",
    "0.0011984500677384821",
    "CF-causing",
    "c.948del",
    "1080delT"
  ],
  "0.001027919623317196": [
    "No",
    "0.001027919623317196",
    "CF-causing",
    "c.1645A>C|c.1647T>A|c.1647T>G",
    "S549R(A->C)|S549R(T->G)|1777A>C|1779T>G|1779T>A",
    "217",
    "S549R",
    "p.Ser549Arg"
  ],
  "c.1645A>C|c.1647T>A|c.1647T>G": [
    "No",
    "0.001027919623317196",
    "CF-causing",
    "c.1645A>C|c.1647T>A|c.1647T>G",
    "S549R(A->C)|S549R(T->G)|1777A>C|1779T>G|1779T>A",
    "217",
    "S549R",
    "p.Ser549Arg"
  ],
  "S549R(A->C)|S549R(T->G)|1777A>C|1779T>G|1779T>A": [
    "No",
    "0.001027919623317196",
    "CF-causing",
    "c.1645A>C|c.1647T>A|c.1647T>G",
    "S549R(A->C)|S549R(T->G)|1777A>C|1779T>G|1779T>A",
    "217",
    "S549R",
    "p.Ser549Arg"
  ],
  "217": [
    "No",
    "0.001027919623317196",
    "CF-causing",
    "c.1645A>C|c.1647T>A|c.1647T>G",
    "S549R(A->C)|S549R(T->G)|1777A>C|1779T>G|1779T>A",
    "217",
    "S549R",
    "p.Ser549Arg"
  ],
  "S549R": [
    "No",
    "0.001027919623317196",
    "CF-causing",
    "c.1645A>C|c.1647T>A|c.1647T>G",
    "S549R(A->C)|S549R(T->G)|1777A>C|1779T>G|1779T>A",
    "217",
    "S549R",
    "p.Ser549Arg"
  ],
  "p.Ser549Arg": [
    "No",
    "0.001027919623317196",
    "CF-causing",
    "c.1645A>C|c.1647T>A|c.1647T>G",
    "S549R(A->C)|S549R(T->G)|1777A>C|1779T>G|1779T>A",
    "217",
    "S549R",
    "p.Ser549Arg"
  ],
  "c.2657+2_2657+3insA": [
    "c.2657+2_2657+3insA",
    "p.?",
    "Varying clinical consequence",
    "2789+2insA",
    "216",
    "Yes",
    "Unknown significance",
    "0.001023182666527716"
  ],
  "2789+2insA": [
    "c.2657+2_2657+3insA",
    "p.?",
    "Varying clinical consequence",
    "2789+2insA",
    "216",
    "Yes",
    "Unknown significance",
    "0.001023182666527716"
  ],
  "216": [
    "c.2657+2_2657+3insA",
    "p.?",
    "Varying clinical consequence",
    "2789+2insA",
    "216",
    "Yes",
    "Unknown significance",
    "0.001023182666527716"
  ],
  "Yes": [
    "c.2770G>A",
    "2902G>A",
    "4",
    "Varying clinical consequence",
    "Yes",
    "D924N",
    "p.Asp924Asn",
    "Unknown significance",
    "1.8947827157920666e-05"
  ],
  "Unknown significance": [
    "c.2770G>A",
    "2902G>A",
    "4",
    "Varying clinical consequence",
    "Yes",
    "D924N",
    "p.Asp924Asn",
    "Unknown significance",
    "1.8947827157920666e-05"
  ],
  "0.001023182666527716": [
    "c.2657+2_2657+3insA",
    "p.?",
    "Varying clinical consequence",
    "2789+2insA",
    "216",
    "Yes",
    "Unknown significance",
    "0.001023182666527716"
  ],
  "p.Glu585X": [
    "No",
    "p.Glu585X",
    "1885G>T",
    "CF-causing",
    "209",
    "E585X",
    "c.1753G>T",
    "0.0009900239690013547"
  ],
  "1885G>T": [
    "No",
    "p.Glu585X",
    "1885G>T",
    "CF-causing",
    "209",
    "E585X",
    "c.1753G>T",
    "0.0009900239690013547"
  ],
  "209": [
    "No",
    "p.Glu585X",
    "1885G>T",
    "CF-causing",
    "209",
    "E585X",
    "c.1753G>T",
    "0.0009900239690013547"
  ],
  "E585X": [
    "No",
    "p.Glu585X",
    "1885G>T",
    "CF-causing",
    "209",
    "E585X",
    "c.1753G>T",
    "0.0009900239690013547"
  ],
  "c.1753G>T": [
    "No",
    "p.Glu585X",
    "1885G>T",
    "CF-causing",
    "209",
    "E585X",
    "c.1753G>T",
    "0.0009900239690013547"
  ],
  "0.0009900239690013547": [
    "No",
    "p.Glu585X",
    "1885G>T",
    "CF-causing",
    "209",
    "E585X",
    "c.1753G>T",
    "0.0009900239690013547"
  ],
  "L1077P": [
    "No",
    "L1077P",
    "0.0009473913578960332",
    "CF-causing",
    "200",
    "3362T>C",
    "p.Leu1077Pro",
    "c.3230T>C"
  ],
  "0.0009473913578960332": [
    "No",
    "L1077P",
    "0.0009473913578960332",
    "CF-causing",
    "200",
    "3362T>C",
    "p.Leu1077Pro",
    "c.3230T>C"
  ],
  "200": [
    "No",
    "L1077P",
    "0.0009473913578960332",
    "CF-causing",
    "200",
    "3362T>C",
    "p.Leu1077Pro",
    "c.3230T>C"
  ],
  "3362T>C": [
    "No",
    "L1077P",
    "0.0009473913578960332",
    "CF-causing",
    "200",
    "3362T>C",
    "p.Leu1077Pro",
    "c.3230T>C"
  ],
  "p.Leu1077Pro": [
    "No",
    "L1077P",
    "0.0009473913578960332",
    "CF-causing",
    "200",
    "3362T>C",
    "p.Leu1077Pro",
    "c.3230T>C"
  ],
  "c.3230T>C": [
    "No",
    "L1077P",
    "0.0009473913578960332",
    "CF-causing",
    "200",
    "3362T>C",
    "p.Leu1077Pro",
    "c.3230T>C"
  ],
  "V520F": [
    "No",
    "V520F",
    "CF-causing",
    "1690G>T",
    "p.Val520Phe",
    "199",
    "c.1558G>T",
    "0.0009426544011065532"
  ],
  "1690G>T": [
    "No",
    "V520F",
    "CF-causing",
    "1690G>T",
    "p.Val520Phe",
    "199",
    "c.1558G>T",
    "0.0009426544011065532"
  ],
  "p.Val520Phe": [
    "No",
    "V520F",
    "CF-causing",
    "1690G>T",
    "p.Val520Phe",
    "199",
    "c.1558G>T",
    "0.0009426544011065532"
  ],
  "199": [
    "No",
    "V520F",
    "CF-causing",
    "1690G>T",
    "p.Val520Phe",
    "199",
    "c.1558G>T",
    "0.0009426544011065532"
  ],
  "c.1558G>T": [
    "No",
    "V520F",
    "CF-causing",
    "1690G>T",
    "p.Val520Phe",
    "199",
    "c.1558G>T",
    "0.0009426544011065532"
  ],
  "0.0009426544011065532": [
    "No",
    "V520F",
    "CF-causing",
    "1690G>T",
    "p.Val520Phe",
    "199",
    "c.1558G>T",
    "0.0009426544011065532"
  ],
  "196": [
    "196",
    "p.Arg1066His",
    "No",
    "3329G>A",
    "CF-causing",
    "R1066H",
    "c.3197G>A",
    "0.0009284435307381126"
  ],
  "p.Leu997Phe": [
    "196",
    "p.Leu997Phe",
    "No",
    "3123G>C",
    "L997F",
    "Non CF-causing",
    "c.2991G>C",
    "0.0009284435307381126"
  ],
  "3123G>C": [
    "196",
    "p.Leu997Phe",
    "No",
    "3123G>C",
    "L997F",
    "Non CF-causing",
    "c.2991G>C",
    "0.0009284435307381126"
  ],
  "L997F": [
    "196",
    "p.Leu997Phe",
    "No",
    "3123G>C",
    "L997F",
    "Non CF-causing",
    "c.2991G>C",
    "0.0009284435307381126"
  ],
  "c.2991G>C": [
    "196",
    "p.Leu997Phe",
    "No",
    "3123G>C",
    "L997F",
    "Non CF-causing",
    "c.2991G>C",
    "0.0009284435307381126"
  ],
  "0.0009284435307381126": [
    "196",
    "p.Arg1066His",
    "No",
    "3329G>A",
    "CF-causing",
    "R1066H",
    "c.3197G>A",
    "0.0009284435307381126"
  ],
  "p.Arg1066His": [
    "196",
    "p.Arg1066His",
    "No",
    "3329G>A",
    "CF-causing",
    "R1066H",
    "c.3197G>A",
    "0.0009284435307381126"
  ],
  "3329G>A": [
    "196",
    "p.Arg1066His",
    "No",
    "3329G>A",
    "CF-causing",
    "R1066H",
    "c.3197G>A",
    "0.0009284435307381126"
  ],
  "R1066H": [
    "196",
    "p.Arg1066His",
    "No",
    "3329G>A",
    "CF-causing",
    "R1066H",
    "c.3197G>A",
    "0.0009284435307381126"
  ],
  "c.3197G>A": [
    "196",
    "p.Arg1066His",
    "No",
    "3329G>A",
    "CF-causing",
    "R1066H",
    "c.3197G>A",
    "0.0009284435307381126"
  ],
  "192": [
    "192",
    "No",
    "CF-causing",
    "p.Arg352Gln",
    "1187G>A",
    "0.0009094957035801919",
    "R352Q",
    "c.1055G>A"
  ],
  "p.Arg352Gln": [
    "192",
    "No",
    "CF-causing",
    "p.Arg352Gln",
    "1187G>A",
    "0.0009094957035801919",
    "R352Q",
    "c.1055G>A"
  ],
  "1187G>A": [
    "192",
    "No",
    "CF-causing",
    "p.Arg352Gln",
    "1187G>A",
    "0.0009094957035801919",
    "R352Q",
    "c.1055G>A"
  ],
  "0.0009094957035801919": [
    "192",
    "No",
    "CF-causing",
    "p.Arg352Gln",
    "1187G>A",
    "0.0009094957035801919",
    "R352Q",
    "c.1055G>A"
  ],
  "R352Q": [
    "192",
    "No",
    "CF-causing",
    "p.Arg352Gln",
    "1187G>A",
    "0.0009094957035801919",
    "R352Q",
    "c.1055G>A"
  ],
  "c.1055G>A": [
    "192",
    "No",
    "CF-causing",
    "p.Arg352Gln",
    "1187G>A",
    "0.0009094957035801919",
    "R352Q",
    "c.1055G>A"
  ],
  "G1244E": [
    "No",
    "G1244E",
    "c.3731G>A",
    "0.0009047587467907118",
    "191",
    "CF-causing",
    "3863G>A",
    "p.Gly1244Glu"
  ],
  "c.3731G>A": [
    "No",
    "G1244E",
    "c.3731G>A",
    "0.0009047587467907118",
    "191",
    "CF-causing",
    "3863G>A",
    "p.Gly1244Glu"
  ],
  "0.0009047587467907118": [
    "No",
    "G1244E",
    "c.3731G>A",
    "0.0009047587467907118",
    "191",
    "CF-causing",
    "3863G>A",
    "p.Gly1244Glu"
  ],
  "191": [
    "No",
    "G1244E",
    "c.3731G>A",
    "0.0009047587467907118",
    "191",
    "CF-causing",
    "3863G>A",
    "p.Gly1244Glu"
  ],
  "3863G>A": [
    "No",
    "G1244E",
    "c.3731G>A",
    "0.0009047587467907118",
    "191",
    "CF-causing",
    "3863G>A",
    "p.Gly1244Glu"
  ],
  "p.Gly1244Glu": [
    "No",
    "G1244E",
    "c.3731G>A",
    "0.0009047587467907118",
    "191",
    "CF-causing",
    "3863G>A",
    "p.Gly1244Glu"
  ],
  "D110H": [
    "D110H",
    "No",
    "460G>C",
    "c.328G>C",
    "CF-causing",
    "p.Asp110His",
    "0.0008858109196327911",
    "187"
  ],
  "460G>C": [
    "D110H",
    "No",
    "460G>C",
    "c.328G>C",
    "CF-causing",
    "p.Asp110His",
    "0.0008858109196327911",
    "187"
  ],
  "c.328G>C": [
    "D110H",
    "No",
    "460G>C",
    "c.328G>C",
    "CF-causing",
    "p.Asp110His",
    "0.0008858109196327911",
    "187"
  ],
  "p.Asp110His": [
    "D110H",
    "No",
    "460G>C",
    "c.328G>C",
    "CF-causing",
    "p.Asp110His",
    "0.0008858109196327911",
    "187"
  ],
  "0.0008858109196327911": [
    "D110H",
    "No",
    "460G>C",
    "c.328G>C",
    "CF-causing",
    "p.Asp110His",
    "0.0008858109196327911",
    "187"
  ],
  "187": [
    "D110H",
    "No",
    "460G>C",
    "c.328G>C",
    "CF-causing",
    "p.Asp110His",
    "0.0008858109196327911",
    "187"
  ],
  "183": [
    "183",
    "p.?",
    "No",
    "1811+1634A->G",
    "0.0008668630924748705",
    "CF-causing",
    "c.1679+1634A>G|1812-886A>G|1811+1.6kbA->G",
    "c.1680-886A>G"
  ],
  "1811+1634A->G": [
    "183",
    "p.?",
    "No",
    "1811+1634A->G",
    "0.0008668630924748705",
    "CF-causing",
    "c.1679+1634A>G|1812-886A>G|1811+1.6kbA->G",
    "c.1680-886A>G"
  ],
  "0.0008668630924748705": [
    "183",
    "p.?",
    "No",
    "1811+1634A->G",
    "0.0008668630924748705",
    "CF-causing",
    "c.1679+1634A>G|1812-886A>G|1811+1.6kbA->G",
    "c.1680-886A>G"
  ],
  "c.1679+1634A>G|1812-886A>G|1811+1.6kbA->G": [
    "183",
    "p.?",
    "No",
    "1811+1634A->G",
    "0.0008668630924748705",
    "CF-causing",
    "c.1679+1634A>G|1812-886A>G|1811+1.6kbA->G",
    "c.1680-886A>G"
  ],
  "c.1680-886A>G": [
    "183",
    "p.?",
    "No",
    "1811+1634A->G",
    "0.0008668630924748705",
    "CF-causing",
    "c.1679+1634A>G|1812-886A>G|1811+1.6kbA->G",
    "c.1680-886A>G"
  ],
  "179": [
    "179",
    "p.?",
    "No",
    "deletion of exon 2 (legacy and current numbering)",
    "CFTRdele2",
    "CF-causing",
    "0.0008479152653169498",
    "c.(53+1_54-1)_(164+1_165-1)del"
  ],
  "deletion of exon 2 (legacy and current numbering)": [
    "179",
    "p.?",
    "No",
    "deletion of exon 2 (legacy and current numbering)",
    "CFTRdele2",
    "CF-causing",
    "0.0008479152653169498",
    "c.(53+1_54-1)_(164+1_165-1)del"
  ],
  "CFTRdele2": [
    "179",
    "p.?",
    "No",
    "deletion of exon 2 (legacy and current numbering)",
    "CFTRdele2",
    "CF-causing",
    "0.0008479152653169498",
    "c.(53+1_54-1)_(164+1_165-1)del"
  ],
  "0.0008479152653169498": [
    "179",
    "p.?",
    "No",
    "deletion of exon 2 (legacy and current numbering)",
    "CFTRdele2",
    "CF-causing",
    "0.0008479152653169498",
    "c.(53+1_54-1)_(164+1_165-1)del"
  ],
  "c.(53+1_54-1)_(164+1_165-1)del": [
    "179",
    "p.?",
    "No",
    "deletion of exon 2 (legacy and current numbering)",
    "CFTRdele2",
    "CF-causing",
    "0.0008479152653169498",
    "c.(53+1_54-1)_(164+1_165-1)del"
  ],
  "664G>A": [
    "664G>A",
    "p.Gly178Arg",
    "No",
    "G178R",
    "c.532G>A",
    "CF-causing",
    "0.0008194935245800688",
    "173"
  ],
  "p.Gly178Arg": [
    "664G>A",
    "p.Gly178Arg",
    "No",
    "G178R",
    "c.532G>A",
    "CF-causing",
    "0.0008194935245800688",
    "173"
  ],
  "G178R": [
    "664G>A",
    "p.Gly178Arg",
    "No",
    "G178R",
    "c.532G>A",
    "CF-causing",
    "0.0008194935245800688",
    "173"
  ],
  "c.532G>A": [
    "664G>A",
    "p.Gly178Arg",
    "No",
    "G178R",
    "c.532G>A",
    "CF-causing",
    "0.0008194935245800688",
    "173"
  ],
  "0.0008194935245800688": [
    "664G>A",
    "p.Gly178Arg",
    "No",
    "G178R",
    "c.532G>A",
    "CF-causing",
    "0.0008194935245800688",
    "173"
  ],
  "173": [
    "664G>A",
    "p.Gly178Arg",
    "No",
    "G178R",
    "c.532G>A",
    "CF-causing",
    "0.0008194935245800688",
    "173"
  ],
  "172": [
    "No",
    "172",
    "p.Lys1250ArgfsX9",
    "CF-causing",
    "c.3744del",
    "3876delA",
    "0.0008147565677905887"
  ],
  "p.Lys1250ArgfsX9": [
    "9.473913578960333e-05",
    "No",
    "20",
    "c.3747del",
    "p.Lys1250ArgfsX9",
    "CF-causing",
    "3878delG"
  ],
  "c.3744del": [
    "No",
    "172",
    "p.Lys1250ArgfsX9",
    "CF-causing",
    "c.3744del",
    "3876delA",
    "0.0008147565677905887"
  ],
  "3876delA": [
    "No",
    "172",
    "p.Lys1250ArgfsX9",
    "CF-causing",
    "c.3744del",
    "3876delA",
    "0.0008147565677905887"
  ],
  "0.0008147565677905887": [
    "No",
    "172",
    "p.Lys1250ArgfsX9",
    "CF-causing",
    "c.3744del",
    "3876delA",
    "0.0008147565677905887"
  ],
  "0.0007910717838431878": [
    "0.0007910717838431878",
    "2622+1G->A",
    "p.?",
    "No",
    "c.2490+1G>A",
    "CF-causing",
    "167"
  ],
  "2622+1G->A": [
    "0.0007910717838431878",
    "2622+1G->A",
    "p.?",
    "No",
    "c.2490+1G>A",
    "CF-causing",
    "167"
  ],
  "c.2490+1G>A": [
    "0.0007910717838431878",
    "2622+1G->A",
    "p.?",
    "No",
    "c.2490+1G>A",
    "CF-causing",
    "167"
  ],
  "167": [
    "0.0007910717838431878",
    "2622+1G->A",
    "p.?",
    "No",
    "c.2490+1G>A",
    "CF-causing",
    "167"
  ],
  "c.579+3A>G": [
    "p.?",
    "No",
    "c.579+3A>G",
    "711+3A->G",
    "CF-causing",
    "165",
    "0.0007815978702642274"
  ],
  "711+3A->G": [
    "p.?",
    "No",
    "c.579+3A>G",
    "711+3A->G",
    "CF-causing",
    "165",
    "0.0007815978702642274"
  ],
  "165": [
    "p.?",
    "No",
    "c.579+3A>G",
    "711+3A->G",
    "CF-causing",
    "165",
    "0.0007815978702642274"
  ],
  "0.0007815978702642274": [
    "p.?",
    "No",
    "c.579+3A>G",
    "711+3A->G",
    "CF-causing",
    "165",
    "0.0007815978702642274"
  ],
  "I148T": [
    "I148T",
    "p.Ile148Thr",
    "No",
    "c.443T>C",
    "0.0007673869998957869",
    "575T>C",
    "162",
    "Non CF-causing"
  ],
  "p.Ile148Thr": [
    "I148T",
    "p.Ile148Thr",
    "No",
    "c.443T>C",
    "0.0007673869998957869",
    "575T>C",
    "162",
    "Non CF-causing"
  ],
  "c.443T>C": [
    "I148T",
    "p.Ile148Thr",
    "No",
    "c.443T>C",
    "0.0007673869998957869",
    "575T>C",
    "162",
    "Non CF-causing"
  ],
  "0.0007673869998957869": [
    "I148T",
    "p.Ile148Thr",
    "No",
    "c.443T>C",
    "0.0007673869998957869",
    "575T>C",
    "162",
    "Non CF-causing"
  ],
  "575T>C": [
    "I148T",
    "p.Ile148Thr",
    "No",
    "c.443T>C",
    "0.0007673869998957869",
    "575T>C",
    "162",
    "Non CF-causing"
  ],
  "162": [
    "I148T",
    "p.Ile148Thr",
    "No",
    "c.443T>C",
    "0.0007673869998957869",
    "575T>C",
    "162",
    "Non CF-causing"
  ],
  "3884G>A": [
    "3884G>A",
    "No",
    "160",
    "0.0007579130863168267",
    "S1251N",
    "c.3752G>A",
    "CF-causing",
    "p.Ser1251Asn"
  ],
  "160": [
    "3884G>A",
    "No",
    "160",
    "0.0007579130863168267",
    "S1251N",
    "c.3752G>A",
    "CF-causing",
    "p.Ser1251Asn"
  ],
  "0.0007579130863168267": [
    "3884G>A",
    "No",
    "160",
    "0.0007579130863168267",
    "S1251N",
    "c.3752G>A",
    "CF-causing",
    "p.Ser1251Asn"
  ],
  "S1251N": [
    "3884G>A",
    "No",
    "160",
    "0.0007579130863168267",
    "S1251N",
    "c.3752G>A",
    "CF-causing",
    "p.Ser1251Asn"
  ],
  "c.3752G>A": [
    "3884G>A",
    "No",
    "160",
    "0.0007579130863168267",
    "S1251N",
    "c.3752G>A",
    "CF-causing",
    "p.Ser1251Asn"
  ],
  "p.Ser1251Asn": [
    "3884G>A",
    "No",
    "160",
    "0.0007579130863168267",
    "S1251N",
    "c.3752G>A",
    "CF-causing",
    "p.Ser1251Asn"
  ],
  "0.000738965259158906": [
    "0.000738965259158906",
    "No",
    "4016insT",
    "p.Ser1297PhefsX5",
    "c.3889dup",
    "CF-causing",
    "156",
    "c.3884_3885insT|4021dupT"
  ],
  "4016insT": [
    "0.000738965259158906",
    "No",
    "4016insT",
    "p.Ser1297PhefsX5",
    "c.3889dup",
    "CF-causing",
    "156",
    "c.3884_3885insT|4021dupT"
  ],
  "p.Ser1297PhefsX5": [
    "0.000738965259158906",
    "No",
    "4016insT",
    "p.Ser1297PhefsX5",
    "c.3889dup",
    "CF-causing",
    "156",
    "c.3884_3885insT|4021dupT"
  ],
  "c.3889dup": [
    "0.000738965259158906",
    "No",
    "4016insT",
    "p.Ser1297PhefsX5",
    "c.3889dup",
    "CF-causing",
    "156",
    "c.3884_3885insT|4021dupT"
  ],
  "156": [
    "0.000738965259158906",
    "No",
    "4016insT",
    "p.Ser1297PhefsX5",
    "c.3889dup",
    "CF-causing",
    "156",
    "c.3884_3885insT|4021dupT"
  ],
  "c.3884_3885insT|4021dupT": [
    "0.000738965259158906",
    "No",
    "4016insT",
    "p.Ser1297PhefsX5",
    "c.3889dup",
    "CF-causing",
    "156",
    "c.3884_3885insT|4021dupT"
  ],
  "A559T": [
    "A559T",
    "c.1675G>A",
    "No",
    "p.Ala559Thr",
    "CF-causing",
    "1807G>A",
    "0.0007342283023694258",
    "155"
  ],
  "c.1675G>A": [
    "A559T",
    "c.1675G>A",
    "No",
    "p.Ala559Thr",
    "CF-causing",
    "1807G>A",
    "0.0007342283023694258",
    "155"
  ],
  "p.Ala559Thr": [
    "A559T",
    "c.1675G>A",
    "No",
    "p.Ala559Thr",
    "CF-causing",
    "1807G>A",
    "0.0007342283023694258",
    "155"
  ],
  "1807G>A": [
    "A559T",
    "c.1675G>A",
    "No",
    "p.Ala559Thr",
    "CF-causing",
    "1807G>A",
    "0.0007342283023694258",
    "155"
  ],
  "0.0007342283023694258": [
    "A559T",
    "c.1675G>A",
    "No",
    "p.Ala559Thr",
    "CF-causing",
    "1807G>A",
    "0.0007342283023694258",
    "155"
  ],
  "155": [
    "A559T",
    "c.1675G>A",
    "No",
    "p.Ala559Thr",
    "CF-causing",
    "1807G>A",
    "0.0007342283023694258",
    "155"
  ],
  "c.1393-1G>A": [
    "p.?",
    "No",
    "c.1393-1G>A",
    "CF-causing",
    "151",
    "1525-1G->A",
    "0.0007152804752115051"
  ],
  "151": [
    "p.?",
    "No",
    "c.1393-1G>A",
    "CF-causing",
    "151",
    "1525-1G->A",
    "0.0007152804752115051"
  ],
  "1525-1G->A": [
    "p.?",
    "No",
    "c.1393-1G>A",
    "CF-causing",
    "151",
    "1525-1G->A",
    "0.0007152804752115051"
  ],
  "0.0007152804752115051": [
    "p.?",
    "No",
    "c.1393-1G>A",
    "CF-causing",
    "151",
    "1525-1G->A",
    "0.0007152804752115051"
  ],
  "c.223C>T": [
    "c.223C>T",
    "355C>T",
    "0.0007105435184220249",
    "No",
    "R75X",
    "CF-causing",
    "150",
    "p.Arg75X"
  ],
  "355C>T": [
    "c.223C>T",
    "355C>T",
    "0.0007105435184220249",
    "No",
    "R75X",
    "CF-causing",
    "150",
    "p.Arg75X"
  ],
  "0.0007105435184220249": [
    "c.223C>T",
    "355C>T",
    "0.0007105435184220249",
    "No",
    "R75X",
    "CF-causing",
    "150",
    "p.Arg75X"
  ],
  "R75X": [
    "c.223C>T",
    "355C>T",
    "0.0007105435184220249",
    "No",
    "R75X",
    "CF-causing",
    "150",
    "p.Arg75X"
  ],
  "150": [
    "c.223C>T",
    "355C>T",
    "0.0007105435184220249",
    "No",
    "R75X",
    "CF-causing",
    "150",
    "p.Arg75X"
  ],
  "p.Arg75X": [
    "c.223C>T",
    "355C>T",
    "0.0007105435184220249",
    "No",
    "R75X",
    "CF-causing",
    "150",
    "p.Arg75X"
  ],
  "790C>T": [
    "790C>T",
    "No",
    "149",
    "c.658C>T",
    "CF-causing",
    "0.0007058065616325447",
    "Q220X",
    "p.Gln220X"
  ],
  "149": [
    "790C>T",
    "No",
    "149",
    "c.658C>T",
    "CF-causing",
    "0.0007058065616325447",
    "Q220X",
    "p.Gln220X"
  ],
  "c.658C>T": [
    "790C>T",
    "No",
    "149",
    "c.658C>T",
    "CF-causing",
    "0.0007058065616325447",
    "Q220X",
    "p.Gln220X"
  ],
  "0.0007058065616325447": [
    "790C>T",
    "No",
    "149",
    "c.658C>T",
    "CF-causing",
    "0.0007058065616325447",
    "Q220X",
    "p.Gln220X"
  ],
  "Q220X": [
    "790C>T",
    "No",
    "149",
    "c.658C>T",
    "CF-causing",
    "0.0007058065616325447",
    "Q220X",
    "p.Gln220X"
  ],
  "p.Gln220X": [
    "790C>T",
    "No",
    "149",
    "c.658C>T",
    "CF-causing",
    "0.0007058065616325447",
    "Q220X",
    "p.Gln220X"
  ],
  "Q996Q|p.Gln996Gln": [
    "No",
    "Q996Q|p.Gln996Gln",
    "c.2988G>A",
    "CF-causing",
    "p.Gln996=",
    "0.0007010696048430647",
    "148",
    "3120G->A"
  ],
  "c.2988G>A": [
    "No",
    "Q996Q|p.Gln996Gln",
    "c.2988G>A",
    "CF-causing",
    "p.Gln996=",
    "0.0007010696048430647",
    "148",
    "3120G->A"
  ],
  "p.Gln996=": [
    "No",
    "Q996Q|p.Gln996Gln",
    "c.2988G>A",
    "CF-causing",
    "p.Gln996=",
    "0.0007010696048430647",
    "148",
    "3120G->A"
  ],
  "0.0007010696048430647": [
    "No",
    "Q996Q|p.Gln996Gln",
    "c.2988G>A",
    "CF-causing",
    "p.Gln996=",
    "0.0007010696048430647",
    "148",
    "3120G->A"
  ],
  "148": [
    "No",
    "Q996Q|p.Gln996Gln",
    "c.2988G>A",
    "CF-causing",
    "p.Gln996=",
    "0.0007010696048430647",
    "148",
    "3120G->A"
  ],
  "3120G->A": [
    "No",
    "Q996Q|p.Gln996Gln",
    "c.2988G>A",
    "CF-causing",
    "p.Gln996=",
    "0.0007010696048430647",
    "148",
    "3120G->A"
  ],
  "p.Glu1418ArgfsX14": [
    "p.Glu1418ArgfsX14",
    "4382delA",
    "No",
    "0.0006347522097903423",
    "CF-causing",
    "c.4251del",
    "134"
  ],
  "4382delA": [
    "p.Glu1418ArgfsX14",
    "4382delA",
    "No",
    "0.0006347522097903423",
    "CF-causing",
    "c.4251del",
    "134"
  ],
  "0.0006347522097903423": [
    "p.Glu1418ArgfsX14",
    "4382delA",
    "No",
    "0.0006347522097903423",
    "CF-causing",
    "c.4251del",
    "134"
  ],
  "c.4251del": [
    "p.Glu1418ArgfsX14",
    "4382delA",
    "No",
    "0.0006347522097903423",
    "CF-causing",
    "c.4251del",
    "134"
  ],
  "134": [
    "p.Glu1418ArgfsX14",
    "4382delA",
    "No",
    "0.0006347522097903423",
    "CF-causing",
    "c.4251del",
    "134"
  ],
  "0.0006300152530008622": [
    "No",
    "0.0006300152530008622",
    "p.Ser1235Arg",
    "c.3705T>G",
    "3837T>G",
    "S1235R",
    "Non CF-causing",
    "133"
  ],
  "p.Ser1235Arg": [
    "No",
    "0.0006300152530008622",
    "p.Ser1235Arg",
    "c.3705T>G",
    "3837T>G",
    "S1235R",
    "Non CF-causing",
    "133"
  ],
  "c.3705T>G": [
    "No",
    "0.0006300152530008622",
    "p.Ser1235Arg",
    "c.3705T>G",
    "3837T>G",
    "S1235R",
    "Non CF-causing",
    "133"
  ],
  "3837T>G": [
    "No",
    "0.0006300152530008622",
    "p.Ser1235Arg",
    "c.3705T>G",
    "3837T>G",
    "S1235R",
    "Non CF-causing",
    "133"
  ],
  "S1235R": [
    "No",
    "0.0006300152530008622",
    "p.Ser1235Arg",
    "c.3705T>G",
    "3837T>G",
    "S1235R",
    "Non CF-causing",
    "133"
  ],
  "133": [
    "No",
    "0.0006300152530008622",
    "p.Ser1235Arg",
    "c.3705T>G",
    "3837T>G",
    "S1235R",
    "Non CF-causing",
    "133"
  ],
  "p.Pro205Ser": [
    "No",
    "p.Pro205Ser",
    "P205S",
    "0.000625278296211382",
    "CF-causing",
    "c.613C>T",
    "132",
    "745C>T"
  ],
  "P205S": [
    "No",
    "p.Pro205Ser",
    "P205S",
    "0.000625278296211382",
    "CF-causing",
    "c.613C>T",
    "132",
    "745C>T"
  ],
  "0.000625278296211382": [
    "No",
    "p.Pro205Ser",
    "P205S",
    "0.000625278296211382",
    "CF-causing",
    "c.613C>T",
    "132",
    "745C>T"
  ],
  "c.613C>T": [
    "No",
    "p.Pro205Ser",
    "P205S",
    "0.000625278296211382",
    "CF-causing",
    "c.613C>T",
    "132",
    "745C>T"
  ],
  "132": [
    "No",
    "p.Pro205Ser",
    "P205S",
    "0.000625278296211382",
    "CF-causing",
    "c.613C>T",
    "132",
    "745C>T"
  ],
  "745C>T": [
    "No",
    "p.Pro205Ser",
    "P205S",
    "0.000625278296211382",
    "CF-causing",
    "c.613C>T",
    "132",
    "745C>T"
  ],
  "p.Arg709X": [
    "No",
    "p.Arg709X",
    "R709X",
    "c.2125C>T",
    "0.0006205413394219018",
    "CF-causing",
    "131",
    "2257C>T"
  ],
  "R709X": [
    "No",
    "p.Arg709X",
    "R709X",
    "c.2125C>T",
    "0.0006205413394219018",
    "CF-causing",
    "131",
    "2257C>T"
  ],
  "c.2125C>T": [
    "No",
    "p.Arg709X",
    "R709X",
    "c.2125C>T",
    "0.0006205413394219018",
    "CF-causing",
    "131",
    "2257C>T"
  ],
  "0.0006205413394219018": [
    "No",
    "p.Arg709X",
    "R709X",
    "c.2125C>T",
    "0.0006205413394219018",
    "CF-causing",
    "131",
    "2257C>T"
  ],
  "131": [
    "No",
    "p.Arg709X",
    "R709X",
    "c.2125C>T",
    "0.0006205413394219018",
    "CF-causing",
    "131",
    "2257C>T"
  ],
  "2257C>T": [
    "No",
    "p.Arg709X",
    "R709X",
    "c.2125C>T",
    "0.0006205413394219018",
    "CF-causing",
    "131",
    "2257C>T"
  ],
  "p.Pro5Leu": [
    "p.Pro5Leu",
    "128",
    "No",
    "0.0006063304690534613",
    "c.14C>T",
    "Varying clinical consequence",
    "P5L",
    "146C>T"
  ],
  "128": [
    "3199delATAGTG",
    "128",
    "No",
    "0.0006063304690534613",
    "CF-causing",
    "3199del6",
    "c.3067_3072del",
    "p.Ile1023_Val1024del"
  ],
  "0.0006063304690534613": [
    "3199delATAGTG",
    "128",
    "No",
    "0.0006063304690534613",
    "CF-causing",
    "3199del6",
    "c.3067_3072del",
    "p.Ile1023_Val1024del"
  ],
  "c.14C>T": [
    "p.Pro5Leu",
    "128",
    "No",
    "0.0006063304690534613",
    "c.14C>T",
    "Varying clinical consequence",
    "P5L",
    "146C>T"
  ],
  "P5L": [
    "p.Pro5Leu",
    "128",
    "No",
    "0.0006063304690534613",
    "c.14C>T",
    "Varying clinical consequence",
    "P5L",
    "146C>T"
  ],
  "146C>T": [
    "p.Pro5Leu",
    "128",
    "No",
    "0.0006063304690534613",
    "c.14C>T",
    "Varying clinical consequence",
    "P5L",
    "146C>T"
  ],
  "3199delATAGTG": [
    "3199delATAGTG",
    "128",
    "No",
    "0.0006063304690534613",
    "CF-causing",
    "3199del6",
    "c.3067_3072del",
    "p.Ile1023_Val1024del"
  ],
  "3199del6": [
    "3199delATAGTG",
    "128",
    "No",
    "0.0006063304690534613",
    "CF-causing",
    "3199del6",
    "c.3067_3072del",
    "p.Ile1023_Val1024del"
  ],
  "c.3067_3072del": [
    "3199delATAGTG",
    "128",
    "No",
    "0.0006063304690534613",
    "CF-causing",
    "3199del6",
    "c.3067_3072del",
    "p.Ile1023_Val1024del"
  ],
  "p.Ile1023_Val1024del": [
    "3199delATAGTG",
    "128",
    "No",
    "0.0006063304690534613",
    "CF-causing",
    "3199del6",
    "c.3067_3072del",
    "p.Ile1023_Val1024del"
  ],
  "127": [
    "No",
    "127",
    "c.1397C>A|c.1397C>G",
    "S466X",
    "CF-causing",
    "0.0006015935122639811",
    "S466X(TGA)|S466X(TAA)|1529C>A|1529C>G",
    "p.Ser466X"
  ],
  "c.1397C>A|c.1397C>G": [
    "No",
    "127",
    "c.1397C>A|c.1397C>G",
    "S466X",
    "CF-causing",
    "0.0006015935122639811",
    "S466X(TGA)|S466X(TAA)|1529C>A|1529C>G",
    "p.Ser466X"
  ],
  "S466X": [
    "No",
    "127",
    "c.1397C>A|c.1397C>G",
    "S466X",
    "CF-causing",
    "0.0006015935122639811",
    "S466X(TGA)|S466X(TAA)|1529C>A|1529C>G",
    "p.Ser466X"
  ],
  "0.0006015935122639811": [
    "No",
    "127",
    "c.1397C>A|c.1397C>G",
    "S466X",
    "CF-causing",
    "0.0006015935122639811",
    "S466X(TGA)|S466X(TAA)|1529C>A|1529C>G",
    "p.Ser466X"
  ],
  "S466X(TGA)|S466X(TAA)|1529C>A|1529C>G": [
    "No",
    "127",
    "c.1397C>A|c.1397C>G",
    "S466X",
    "CF-causing",
    "0.0006015935122639811",
    "S466X(TGA)|S466X(TAA)|1529C>A|1529C>G",
    "p.Ser466X"
  ],
  "p.Ser466X": [
    "No",
    "127",
    "c.1397C>A|c.1397C>G",
    "S466X",
    "CF-causing",
    "0.0006015935122639811",
    "S466X(TGA)|S466X(TAA)|1529C>A|1529C>G",
    "p.Ser466X"
  ],
  "c.579+5G>A": [
    "p.?",
    "c.579+5G>A",
    "0.0005968565554745009",
    "No",
    "CF-causing",
    "711+5G->A",
    "126"
  ],
  "0.0005968565554745009": [
    "p.?",
    "c.579+5G>A",
    "0.0005968565554745009",
    "No",
    "CF-causing",
    "711+5G->A",
    "126"
  ],
  "711+5G->A": [
    "p.?",
    "c.579+5G>A",
    "0.0005968565554745009",
    "No",
    "CF-causing",
    "711+5G->A",
    "126"
  ],
  "126": [
    "p.?",
    "c.579+5G>A",
    "0.0005968565554745009",
    "No",
    "CF-causing",
    "711+5G->A",
    "126"
  ],
  "c.1210-33_1210-6GT[11]T[4]": [
    "p.?",
    "No",
    "c.1210-33_1210-6GT[11]T[4]",
    "124",
    "c.1210-7_1210-6del",
    "Non CF-causing",
    "5T;TG11",
    "0.0005873826418955406"
  ],
  "124": [
    "p.?",
    "No",
    "c.1210-33_1210-6GT[11]T[4]",
    "124",
    "c.1210-7_1210-6del",
    "Non CF-causing",
    "5T;TG11",
    "0.0005873826418955406"
  ],
  "c.1210-7_1210-6del": [
    "p.?",
    "No",
    "c.1210-33_1210-6GT[11]T[4]",
    "124",
    "c.1210-7_1210-6del",
    "Non CF-causing",
    "5T;TG11",
    "0.0005873826418955406"
  ],
  "5T;TG11": [
    "p.?",
    "No",
    "c.1210-33_1210-6GT[11]T[4]",
    "124",
    "c.1210-7_1210-6del",
    "Non CF-causing",
    "5T;TG11",
    "0.0005873826418955406"
  ],
  "0.0005873826418955406": [
    "p.?",
    "No",
    "c.1210-33_1210-6GT[11]T[4]",
    "124",
    "c.1210-7_1210-6del",
    "Non CF-causing",
    "5T;TG11",
    "0.0005873826418955406"
  ],
  "c.1210-33_1210-6GT[13]T[4]": [
    "p.?",
    "c.1210-33_1210-6GT[13]T[4]",
    "No",
    "c.1210-11delinsGTG",
    "Varying clinical consequence",
    "123",
    "5T;TG13",
    "0.0005826456851060604"
  ],
  "c.1210-11delinsGTG": [
    "p.?",
    "c.1210-33_1210-6GT[13]T[4]",
    "No",
    "c.1210-11delinsGTG",
    "Varying clinical consequence",
    "123",
    "5T;TG13",
    "0.0005826456851060604"
  ],
  "123": [
    "p.?",
    "c.1210-33_1210-6GT[13]T[4]",
    "No",
    "c.1210-11delinsGTG",
    "Varying clinical consequence",
    "123",
    "5T;TG13",
    "0.0005826456851060604"
  ],
  "5T;TG13": [
    "p.?",
    "c.1210-33_1210-6GT[13]T[4]",
    "No",
    "c.1210-11delinsGTG",
    "Varying clinical consequence",
    "123",
    "5T;TG13",
    "0.0005826456851060604"
  ],
  "0.0005826456851060604": [
    "p.?",
    "c.1210-33_1210-6GT[13]T[4]",
    "No",
    "c.1210-11delinsGTG",
    "Varying clinical consequence",
    "123",
    "5T;TG13",
    "0.0005826456851060604"
  ],
  "827T>A": [
    "827T>A",
    "No",
    "CF-causing",
    "p.Val232Asp",
    "0.00056843481473762",
    "c.695T>A",
    "V232D",
    "120"
  ],
  "p.Val232Asp": [
    "827T>A",
    "No",
    "CF-causing",
    "p.Val232Asp",
    "0.00056843481473762",
    "c.695T>A",
    "V232D",
    "120"
  ],
  "0.00056843481473762": [
    "827T>A",
    "No",
    "CF-causing",
    "p.Val232Asp",
    "0.00056843481473762",
    "c.695T>A",
    "V232D",
    "120"
  ],
  "c.695T>A": [
    "827T>A",
    "No",
    "CF-causing",
    "p.Val232Asp",
    "0.00056843481473762",
    "c.695T>A",
    "V232D",
    "120"
  ],
  "V232D": [
    "827T>A",
    "No",
    "CF-causing",
    "p.Val232Asp",
    "0.00056843481473762",
    "c.695T>A",
    "V232D",
    "120"
  ],
  "120": [
    "827T>A",
    "No",
    "CF-causing",
    "p.Val232Asp",
    "0.00056843481473762",
    "c.695T>A",
    "V232D",
    "120"
  ],
  "L138ins": [
    "No",
    "L138ins",
    "CF-causing",
    "p.Leu138dup",
    "546insCTA|545dupTAC",
    "0.0005589609011586596",
    "118",
    "c.413_415dup"
  ],
  "p.Leu138dup": [
    "No",
    "L138ins",
    "CF-causing",
    "p.Leu138dup",
    "546insCTA|545dupTAC",
    "0.0005589609011586596",
    "118",
    "c.413_415dup"
  ],
  "546insCTA|545dupTAC": [
    "No",
    "L138ins",
    "CF-causing",
    "p.Leu138dup",
    "546insCTA|545dupTAC",
    "0.0005589609011586596",
    "118",
    "c.413_415dup"
  ],
  "0.0005589609011586596": [
    "No",
    "L138ins",
    "CF-causing",
    "p.Leu138dup",
    "546insCTA|545dupTAC",
    "0.0005589609011586596",
    "118",
    "c.413_415dup"
  ],
  "118": [
    "No",
    "L138ins",
    "CF-causing",
    "p.Leu138dup",
    "546insCTA|545dupTAC",
    "0.0005589609011586596",
    "118",
    "c.413_415dup"
  ],
  "c.413_415dup": [
    "No",
    "L138ins",
    "CF-causing",
    "p.Leu138dup",
    "546insCTA|545dupTAC",
    "0.0005589609011586596",
    "118",
    "c.413_415dup"
  ],
  "116": [
    "116",
    "No",
    "356G>A",
    "p.Arg75Gln",
    "Non CF-causing",
    "0.0005494869875796993",
    "c.224G>A",
    "R75Q"
  ],
  "I336K": [
    "116",
    "No",
    "I336K",
    "CF-causing",
    "0.0005494869875796993",
    "c.1007T>A",
    "p.Ile336Lys",
    "1139T>A"
  ],
  "0.0005494869875796993": [
    "116",
    "No",
    "356G>A",
    "p.Arg75Gln",
    "Non CF-causing",
    "0.0005494869875796993",
    "c.224G>A",
    "R75Q"
  ],
  "c.1007T>A": [
    "116",
    "No",
    "I336K",
    "CF-causing",
    "0.0005494869875796993",
    "c.1007T>A",
    "p.Ile336Lys",
    "1139T>A"
  ],
  "p.Ile336Lys": [
    "116",
    "No",
    "I336K",
    "CF-causing",
    "0.0005494869875796993",
    "c.1007T>A",
    "p.Ile336Lys",
    "1139T>A"
  ],
  "1139T>A": [
    "116",
    "No",
    "I336K",
    "CF-causing",
    "0.0005494869875796993",
    "c.1007T>A",
    "p.Ile336Lys",
    "1139T>A"
  ],
  "356G>A": [
    "116",
    "No",
    "356G>A",
    "p.Arg75Gln",
    "Non CF-causing",
    "0.0005494869875796993",
    "c.224G>A",
    "R75Q"
  ],
  "p.Arg75Gln": [
    "116",
    "No",
    "356G>A",
    "p.Arg75Gln",
    "Non CF-causing",
    "0.0005494869875796993",
    "c.224G>A",
    "R75Q"
  ],
  "c.224G>A": [
    "116",
    "No",
    "356G>A",
    "p.Arg75Gln",
    "Non CF-causing",
    "0.0005494869875796993",
    "c.224G>A",
    "R75Q"
  ],
  "R75Q": [
    "116",
    "No",
    "356G>A",
    "p.Arg75Gln",
    "Non CF-causing",
    "0.0005494869875796993",
    "c.224G>A",
    "R75Q"
  ],
  "c.2491G>T": [
    "c.2491G>T",
    "E831X",
    "No",
    "2623G>T",
    "0.0005447500307902191",
    "CF-causing",
    "115",
    "p.Glu831X"
  ],
  "E831X": [
    "c.2491G>T",
    "E831X",
    "No",
    "2623G>T",
    "0.0005447500307902191",
    "CF-causing",
    "115",
    "p.Glu831X"
  ],
  "2623G>T": [
    "c.2491G>T",
    "E831X",
    "No",
    "2623G>T",
    "0.0005447500307902191",
    "CF-causing",
    "115",
    "p.Glu831X"
  ],
  "0.0005447500307902191": [
    "p.?",
    "No",
    "0.0005447500307902191",
    "CF-causing",
    "c.(2988+1_2989-1)_(3468+1_3469-1)del",
    "115",
    "3120+1kbdel8.6kb|deletion of exons 17a, 17b, and 18 (legacy numbering)|deletion of exons 19, 20, and 21 (current numbering)",
    "CFTRdele17a-18"
  ],
  "115": [
    "p.?",
    "No",
    "0.0005447500307902191",
    "CF-causing",
    "c.(2988+1_2989-1)_(3468+1_3469-1)del",
    "115",
    "3120+1kbdel8.6kb|deletion of exons 17a, 17b, and 18 (legacy numbering)|deletion of exons 19, 20, and 21 (current numbering)",
    "CFTRdele17a-18"
  ],
  "p.Glu831X": [
    "c.2491G>T",
    "E831X",
    "No",
    "2623G>T",
    "0.0005447500307902191",
    "CF-causing",
    "115",
    "p.Glu831X"
  ],
  "c.(2988+1_2989-1)_(3468+1_3469-1)del": [
    "p.?",
    "No",
    "0.0005447500307902191",
    "CF-causing",
    "c.(2988+1_2989-1)_(3468+1_3469-1)del",
    "115",
    "3120+1kbdel8.6kb|deletion of exons 17a, 17b, and 18 (legacy numbering)|deletion of exons 19, 20, and 21 (current numbering)",
    "CFTRdele17a-18"
  ],
  "3120+1kbdel8.6kb|deletion of exons 17a, 17b, and 18 (legacy numbering)|deletion of exons 19, 20, and 21 (current numbering)": [
    "p.?",
    "No",
    "0.0005447500307902191",
    "CF-causing",
    "c.(2988+1_2989-1)_(3468+1_3469-1)del",
    "115",
    "3120+1kbdel8.6kb|deletion of exons 17a, 17b, and 18 (legacy numbering)|deletion of exons 19, 20, and 21 (current numbering)",
    "CFTRdele17a-18"
  ],
  "CFTRdele17a-18": [
    "p.?",
    "No",
    "0.0005447500307902191",
    "CF-causing",
    "c.(2988+1_2989-1)_(3468+1_3469-1)del",
    "115",
    "3120+1kbdel8.6kb|deletion of exons 17a, 17b, and 18 (legacy numbering)|deletion of exons 19, 20, and 21 (current numbering)",
    "CFTRdele17a-18"
  ],
  "3212T>C": [
    "3212T>C",
    "114",
    "No",
    "I1027T",
    "0.000540013074000739",
    "Non CF-causing",
    "c.3080T>C",
    "p.Ile1027Thr"
  ],
  "114": [
    "3212T>C",
    "114",
    "No",
    "I1027T",
    "0.000540013074000739",
    "Non CF-causing",
    "c.3080T>C",
    "p.Ile1027Thr"
  ],
  "I1027T": [
    "3212T>C",
    "114",
    "No",
    "I1027T",
    "0.000540013074000739",
    "Non CF-causing",
    "c.3080T>C",
    "p.Ile1027Thr"
  ],
  "0.000540013074000739": [
    "3212T>C",
    "114",
    "No",
    "I1027T",
    "0.000540013074000739",
    "Non CF-causing",
    "c.3080T>C",
    "p.Ile1027Thr"
  ],
  "c.3080T>C": [
    "3212T>C",
    "114",
    "No",
    "I1027T",
    "0.000540013074000739",
    "Non CF-causing",
    "c.3080T>C",
    "p.Ile1027Thr"
  ],
  "p.Ile1027Thr": [
    "3212T>C",
    "114",
    "No",
    "I1027T",
    "0.000540013074000739",
    "Non CF-causing",
    "c.3080T>C",
    "p.Ile1027Thr"
  ],
  "0.0005352761172112588": [
    "F508del in cis with I1027T|[1653delCTT with 3212T>C]",
    "c.[1521_1523del;3080T>C]",
    "0.0005352761172112588",
    "No",
    "p.[Phe508del;Ile1027Thr]",
    "F508del;I1027T",
    "CF-causing",
    "113"
  ],
  "c.11C>A": [
    "0.0005352761172112588",
    "No",
    "c.11C>A",
    "143C>A",
    "p.Ser4X",
    "S4X",
    "CF-causing",
    "113"
  ],
  "143C>A": [
    "0.0005352761172112588",
    "No",
    "c.11C>A",
    "143C>A",
    "p.Ser4X",
    "S4X",
    "CF-causing",
    "113"
  ],
  "p.Ser4X": [
    "0.0005352761172112588",
    "No",
    "c.11C>A",
    "143C>A",
    "p.Ser4X",
    "S4X",
    "CF-causing",
    "113"
  ],
  "S4X": [
    "0.0005352761172112588",
    "No",
    "c.11C>A",
    "143C>A",
    "p.Ser4X",
    "S4X",
    "CF-causing",
    "113"
  ],
  "113": [
    "F508del in cis with I1027T|[1653delCTT with 3212T>C]",
    "c.[1521_1523del;3080T>C]",
    "0.0005352761172112588",
    "No",
    "p.[Phe508del;Ile1027Thr]",
    "F508del;I1027T",
    "CF-causing",
    "113"
  ],
  "3398G>A": [
    "3398G>A",
    "0.0005352761172112588",
    "No",
    "p.Trp1089X",
    "CF-causing",
    "c.3266G>A",
    "113",
    "W1089X"
  ],
  "p.Trp1089X": [
    "3398G>A",
    "0.0005352761172112588",
    "No",
    "p.Trp1089X",
    "CF-causing",
    "c.3266G>A",
    "113",
    "W1089X"
  ],
  "c.3266G>A": [
    "3398G>A",
    "0.0005352761172112588",
    "No",
    "p.Trp1089X",
    "CF-causing",
    "c.3266G>A",
    "113",
    "W1089X"
  ],
  "W1089X": [
    "3398G>A",
    "0.0005352761172112588",
    "No",
    "p.Trp1089X",
    "CF-causing",
    "c.3266G>A",
    "113",
    "W1089X"
  ],
  "F508del in cis with I1027T|[1653delCTT with 3212T>C]": [
    "F508del in cis with I1027T|[1653delCTT with 3212T>C]",
    "c.[1521_1523del;3080T>C]",
    "0.0005352761172112588",
    "No",
    "p.[Phe508del;Ile1027Thr]",
    "F508del;I1027T",
    "CF-causing",
    "113"
  ],
  "c.[1521_1523del;3080T>C]": [
    "F508del in cis with I1027T|[1653delCTT with 3212T>C]",
    "c.[1521_1523del;3080T>C]",
    "0.0005352761172112588",
    "No",
    "p.[Phe508del;Ile1027Thr]",
    "F508del;I1027T",
    "CF-causing",
    "113"
  ],
  "p.[Phe508del;Ile1027Thr]": [
    "F508del in cis with I1027T|[1653delCTT with 3212T>C]",
    "c.[1521_1523del;3080T>C]",
    "0.0005352761172112588",
    "No",
    "p.[Phe508del;Ile1027Thr]",
    "F508del;I1027T",
    "CF-causing",
    "113"
  ],
  "F508del;I1027T": [
    "F508del in cis with I1027T|[1653delCTT with 3212T>C]",
    "c.[1521_1523del;3080T>C]",
    "0.0005352761172112588",
    "No",
    "p.[Phe508del;Ile1027Thr]",
    "F508del;I1027T",
    "CF-causing",
    "113"
  ],
  "c.(3963+1_3964-1)_(4242+1_4243-1)del": [
    "c.(3963+1_3964-1)_(4242+1_4243-1)del",
    "p.?",
    "deletion of exons 22 and 23 (legacy numbering)|deletion of exons 25 and 26 (current numbering)",
    "No",
    "CFTRdele22,23",
    "112",
    "CF-causing",
    "0.0005305391604217786"
  ],
  "deletion of exons 22 and 23 (legacy numbering)|deletion of exons 25 and 26 (current numbering)": [
    "c.(3963+1_3964-1)_(4242+1_4243-1)del",
    "p.?",
    "deletion of exons 22 and 23 (legacy numbering)|deletion of exons 25 and 26 (current numbering)",
    "No",
    "CFTRdele22,23",
    "112",
    "CF-causing",
    "0.0005305391604217786"
  ],
  "CFTRdele22,23": [
    "c.(3963+1_3964-1)_(4242+1_4243-1)del",
    "p.?",
    "deletion of exons 22 and 23 (legacy numbering)|deletion of exons 25 and 26 (current numbering)",
    "No",
    "CFTRdele22,23",
    "112",
    "CF-causing",
    "0.0005305391604217786"
  ],
  "112": [
    "c.(3963+1_3964-1)_(4242+1_4243-1)del",
    "p.?",
    "deletion of exons 22 and 23 (legacy numbering)|deletion of exons 25 and 26 (current numbering)",
    "No",
    "CFTRdele22,23",
    "112",
    "CF-causing",
    "0.0005305391604217786"
  ],
  "0.0005305391604217786": [
    "c.(3963+1_3964-1)_(4242+1_4243-1)del",
    "p.?",
    "deletion of exons 22 and 23 (legacy numbering)|deletion of exons 25 and 26 (current numbering)",
    "No",
    "CFTRdele22,23",
    "112",
    "CF-causing",
    "0.0005305391604217786"
  ],
  "T338I": [
    "T338I",
    "p.Thr338Ile",
    "No",
    "0.00048790654931645715",
    "CF-causing",
    "103",
    "c.1013C>T",
    "1145C>T"
  ],
  "p.Thr338Ile": [
    "T338I",
    "p.Thr338Ile",
    "No",
    "0.00048790654931645715",
    "CF-causing",
    "103",
    "c.1013C>T",
    "1145C>T"
  ],
  "0.00048790654931645715": [
    "p.?",
    "No",
    "712-1G->T",
    "0.00048790654931645715",
    "CF-causing",
    "103",
    "c.580-1G>T"
  ],
  "103": [
    "p.?",
    "No",
    "712-1G->T",
    "0.00048790654931645715",
    "CF-causing",
    "103",
    "c.580-1G>T"
  ],
  "c.1013C>T": [
    "T338I",
    "p.Thr338Ile",
    "No",
    "0.00048790654931645715",
    "CF-causing",
    "103",
    "c.1013C>T",
    "1145C>T"
  ],
  "1145C>T": [
    "T338I",
    "p.Thr338Ile",
    "No",
    "0.00048790654931645715",
    "CF-causing",
    "103",
    "c.1013C>T",
    "1145C>T"
  ],
  "712-1G->T": [
    "p.?",
    "No",
    "712-1G->T",
    "0.00048790654931645715",
    "CF-causing",
    "103",
    "c.580-1G>T"
  ],
  "c.580-1G>T": [
    "p.?",
    "No",
    "712-1G->T",
    "0.00048790654931645715",
    "CF-causing",
    "103",
    "c.580-1G>T"
  ],
  "99": [
    "99",
    "p.Phe1052Val",
    "F1052V",
    "c.3154T>G",
    "No",
    "3286T>G",
    "0.0004689587221585365",
    "Varying clinical consequence"
  ],
  "p.Phe1052Val": [
    "99",
    "p.Phe1052Val",
    "F1052V",
    "c.3154T>G",
    "No",
    "3286T>G",
    "0.0004689587221585365",
    "Varying clinical consequence"
  ],
  "F1052V": [
    "99",
    "p.Phe1052Val",
    "F1052V",
    "c.3154T>G",
    "No",
    "3286T>G",
    "0.0004689587221585365",
    "Varying clinical consequence"
  ],
  "c.3154T>G": [
    "99",
    "p.Phe1052Val",
    "F1052V",
    "c.3154T>G",
    "No",
    "3286T>G",
    "0.0004689587221585365",
    "Varying clinical consequence"
  ],
  "3286T>G": [
    "99",
    "p.Phe1052Val",
    "F1052V",
    "c.3154T>G",
    "No",
    "3286T>G",
    "0.0004689587221585365",
    "Varying clinical consequence"
  ],
  "0.0004689587221585365": [
    "99",
    "p.Phe1052Val",
    "F1052V",
    "c.3154T>G",
    "No",
    "3286T>G",
    "0.0004689587221585365",
    "Varying clinical consequence"
  ],
  "0.0004642217653690563": [
    "0.0004642217653690563",
    "No",
    "98",
    "D579G",
    "Varying clinical consequence",
    "1868A>G",
    "c.1736A>G",
    "p.Asp579Gly"
  ],
  "98": [
    "0.0004642217653690563",
    "No",
    "98",
    "D579G",
    "Varying clinical consequence",
    "1868A>G",
    "c.1736A>G",
    "p.Asp579Gly"
  ],
  "D579G": [
    "0.0004642217653690563",
    "No",
    "98",
    "D579G",
    "Varying clinical consequence",
    "1868A>G",
    "c.1736A>G",
    "p.Asp579Gly"
  ],
  "1868A>G": [
    "0.0004642217653690563",
    "No",
    "98",
    "D579G",
    "Varying clinical consequence",
    "1868A>G",
    "c.1736A>G",
    "p.Asp579Gly"
  ],
  "c.1736A>G": [
    "0.0004642217653690563",
    "No",
    "98",
    "D579G",
    "Varying clinical consequence",
    "1868A>G",
    "c.1736A>G",
    "p.Asp579Gly"
  ],
  "p.Asp579Gly": [
    "0.0004642217653690563",
    "No",
    "98",
    "D579G",
    "Varying clinical consequence",
    "1868A>G",
    "c.1736A>G",
    "p.Asp579Gly"
  ],
  "0.0004405369814216555": [
    "0.0004405369814216555",
    "No",
    "CF-causing",
    "p.Lys710X",
    "2260A>T",
    "c.2128A>T",
    "93",
    "K710X"
  ],
  "p.Lys710X": [
    "0.0004405369814216555",
    "No",
    "CF-causing",
    "p.Lys710X",
    "2260A>T",
    "c.2128A>T",
    "93",
    "K710X"
  ],
  "2260A>T": [
    "0.0004405369814216555",
    "No",
    "CF-causing",
    "p.Lys710X",
    "2260A>T",
    "c.2128A>T",
    "93",
    "K710X"
  ],
  "c.2128A>T": [
    "0.0004405369814216555",
    "No",
    "CF-causing",
    "p.Lys710X",
    "2260A>T",
    "c.2128A>T",
    "93",
    "K710X"
  ],
  "93": [
    "0.0004405369814216555",
    "No",
    "CF-causing",
    "p.Lys710X",
    "2260A>T",
    "c.2128A>T",
    "93",
    "K710X"
  ],
  "K710X": [
    "0.0004405369814216555",
    "No",
    "CF-causing",
    "p.Lys710X",
    "2260A>T",
    "c.2128A>T",
    "93",
    "K710X"
  ],
  "0.0004358000246321753": [
    "0.0004358000246321753",
    "No",
    "2307insA",
    "c.2175dup",
    "c.2175_2176insA",
    "CF-causing",
    "92",
    "p.Glu726ArgfsX4"
  ],
  "2307insA": [
    "0.0004358000246321753",
    "No",
    "2307insA",
    "c.2175dup",
    "c.2175_2176insA",
    "CF-causing",
    "92",
    "p.Glu726ArgfsX4"
  ],
  "c.2175dup": [
    "0.0004358000246321753",
    "No",
    "2307insA",
    "c.2175dup",
    "c.2175_2176insA",
    "CF-causing",
    "92",
    "p.Glu726ArgfsX4"
  ],
  "c.2175_2176insA": [
    "0.0004358000246321753",
    "No",
    "2307insA",
    "c.2175dup",
    "c.2175_2176insA",
    "CF-causing",
    "92",
    "p.Glu726ArgfsX4"
  ],
  "92": [
    "0.0004358000246321753",
    "No",
    "2307insA",
    "c.2175dup",
    "c.2175_2176insA",
    "CF-causing",
    "92",
    "p.Glu726ArgfsX4"
  ],
  "p.Glu726ArgfsX4": [
    "0.0004358000246321753",
    "No",
    "2307insA",
    "c.2175dup",
    "c.2175_2176insA",
    "CF-causing",
    "92",
    "p.Glu726ArgfsX4"
  ],
  "S489X": [
    "No",
    "S489X",
    "c.1466C>A|c.1466C>G",
    "89",
    "CF-causing",
    "1598C>A",
    "0.0004215891542637348",
    "p.Ser489X"
  ],
  "c.1466C>A|c.1466C>G": [
    "No",
    "S489X",
    "c.1466C>A|c.1466C>G",
    "89",
    "CF-causing",
    "1598C>A",
    "0.0004215891542637348",
    "p.Ser489X"
  ],
  "89": [
    "c.1327_1330dup",
    "No",
    "89",
    "CF-causing",
    "c.1326_1329dupAGAT|c.1329_1330insAGAT",
    "0.0004215891542637348",
    "1461ins4",
    "p.Ile444ArgfsX3"
  ],
  "1598C>A": [
    "No",
    "S489X",
    "c.1466C>A|c.1466C>G",
    "89",
    "CF-causing",
    "1598C>A",
    "0.0004215891542637348",
    "p.Ser489X"
  ],
  "0.0004215891542637348": [
    "c.1327_1330dup",
    "No",
    "89",
    "CF-causing",
    "c.1326_1329dupAGAT|c.1329_1330insAGAT",
    "0.0004215891542637348",
    "1461ins4",
    "p.Ile444ArgfsX3"
  ],
  "p.Ser489X": [
    "No",
    "S489X",
    "c.1466C>A|c.1466C>G",
    "89",
    "CF-causing",
    "1598C>A",
    "0.0004215891542637348",
    "p.Ser489X"
  ],
  "c.1327_1330dup": [
    "c.1327_1330dup",
    "No",
    "89",
    "CF-causing",
    "c.1326_1329dupAGAT|c.1329_1330insAGAT",
    "0.0004215891542637348",
    "1461ins4",
    "p.Ile444ArgfsX3"
  ],
  "c.1326_1329dupAGAT|c.1329_1330insAGAT": [
    "c.1327_1330dup",
    "No",
    "89",
    "CF-causing",
    "c.1326_1329dupAGAT|c.1329_1330insAGAT",
    "0.0004215891542637348",
    "1461ins4",
    "p.Ile444ArgfsX3"
  ],
  "1461ins4": [
    "c.1327_1330dup",
    "No",
    "89",
    "CF-causing",
    "c.1326_1329dupAGAT|c.1329_1330insAGAT",
    "0.0004215891542637348",
    "1461ins4",
    "p.Ile444ArgfsX3"
  ],
  "p.Ile444ArgfsX3": [
    "c.1327_1330dup",
    "No",
    "89",
    "CF-causing",
    "c.1326_1329dupAGAT|c.1329_1330insAGAT",
    "0.0004215891542637348",
    "1461ins4",
    "p.Ile444ArgfsX3"
  ],
  "1812-1G->A": [
    "1812-1G->A",
    "p.?",
    "0.0004168521974742546",
    "No",
    "CF-causing",
    "88",
    "c.1680-1G>A"
  ],
  "0.0004168521974742546": [
    "1812-1G->A",
    "p.?",
    "0.0004168521974742546",
    "No",
    "CF-causing",
    "88",
    "c.1680-1G>A"
  ],
  "88": [
    "1812-1G->A",
    "p.?",
    "0.0004168521974742546",
    "No",
    "CF-causing",
    "88",
    "c.1680-1G>A"
  ],
  "c.1680-1G>A": [
    "1812-1G->A",
    "p.?",
    "0.0004168521974742546",
    "No",
    "CF-causing",
    "88",
    "c.1680-1G>A"
  ],
  "87": [
    "87",
    "Y122X",
    "No",
    "p.Tyr122X",
    "0.00041211524068477447",
    "CF-causing",
    "c.366T>A",
    "498T>A"
  ],
  "Y122X": [
    "87",
    "Y122X",
    "No",
    "p.Tyr122X",
    "0.00041211524068477447",
    "CF-causing",
    "c.366T>A",
    "498T>A"
  ],
  "p.Tyr122X": [
    "87",
    "Y122X",
    "No",
    "p.Tyr122X",
    "0.00041211524068477447",
    "CF-causing",
    "c.366T>A",
    "498T>A"
  ],
  "0.00041211524068477447": [
    "87",
    "Y122X",
    "No",
    "p.Tyr122X",
    "0.00041211524068477447",
    "CF-causing",
    "c.366T>A",
    "498T>A"
  ],
  "c.366T>A": [
    "87",
    "Y122X",
    "No",
    "p.Tyr122X",
    "0.00041211524068477447",
    "CF-causing",
    "c.366T>A",
    "498T>A"
  ],
  "498T>A": [
    "87",
    "Y122X",
    "No",
    "p.Tyr122X",
    "0.00041211524068477447",
    "CF-causing",
    "c.366T>A",
    "498T>A"
  ],
  "0.00040737828389529433": [
    "0.00040737828389529433",
    "No",
    "c.1682C>A",
    "1814C>A",
    "CF-causing",
    "86",
    "A561E",
    "p.Ala561Glu"
  ],
  "c.1682C>A": [
    "0.00040737828389529433",
    "No",
    "c.1682C>A",
    "1814C>A",
    "CF-causing",
    "86",
    "A561E",
    "p.Ala561Glu"
  ],
  "1814C>A": [
    "0.00040737828389529433",
    "No",
    "c.1682C>A",
    "1814C>A",
    "CF-causing",
    "86",
    "A561E",
    "p.Ala561Glu"
  ],
  "86": [
    "0.00040737828389529433",
    "No",
    "c.1682C>A",
    "1814C>A",
    "CF-causing",
    "86",
    "A561E",
    "p.Ala561Glu"
  ],
  "A561E": [
    "0.00040737828389529433",
    "No",
    "c.1682C>A",
    "1814C>A",
    "CF-causing",
    "86",
    "A561E",
    "p.Ala561Glu"
  ],
  "p.Ala561Glu": [
    "0.00040737828389529433",
    "No",
    "c.1682C>A",
    "1814C>A",
    "CF-causing",
    "86",
    "A561E",
    "p.Ala561Glu"
  ],
  "L732X": [
    "No",
    "L732X",
    "0.00040264132710581414",
    "CF-causing",
    "c.2195T>G",
    "85",
    "p.Leu732X",
    "2327T>G"
  ],
  "0.00040264132710581414": [
    "No",
    "L732X",
    "0.00040264132710581414",
    "CF-causing",
    "c.2195T>G",
    "85",
    "p.Leu732X",
    "2327T>G"
  ],
  "c.2195T>G": [
    "No",
    "L732X",
    "0.00040264132710581414",
    "CF-causing",
    "c.2195T>G",
    "85",
    "p.Leu732X",
    "2327T>G"
  ],
  "85": [
    "No",
    "L732X",
    "0.00040264132710581414",
    "CF-causing",
    "c.2195T>G",
    "85",
    "p.Leu732X",
    "2327T>G"
  ],
  "p.Leu732X": [
    "No",
    "L732X",
    "0.00040264132710581414",
    "CF-causing",
    "c.2195T>G",
    "85",
    "p.Leu732X",
    "2327T>G"
  ],
  "2327T>G": [
    "No",
    "L732X",
    "0.00040264132710581414",
    "CF-causing",
    "c.2195T>G",
    "85",
    "p.Leu732X",
    "2327T>G"
  ],
  "84": [
    "No",
    "84",
    "p.Ile1234Val",
    "CF-causing",
    "c.3700A>G",
    "I1234V",
    "0.000397904370316334",
    "3832A>G"
  ],
  "p.Ile1234Val": [
    "No",
    "84",
    "p.Ile1234Val",
    "CF-causing",
    "c.3700A>G",
    "I1234V",
    "0.000397904370316334",
    "3832A>G"
  ],
  "c.3700A>G": [
    "No",
    "84",
    "p.Ile1234Val",
    "CF-causing",
    "c.3700A>G",
    "I1234V",
    "0.000397904370316334",
    "3832A>G"
  ],
  "I1234V": [
    "No",
    "84",
    "p.Ile1234Val",
    "CF-causing",
    "c.3700A>G",
    "I1234V",
    "0.000397904370316334",
    "3832A>G"
  ],
  "0.000397904370316334": [
    "No",
    "84",
    "p.Ile1234Val",
    "CF-causing",
    "c.3700A>G",
    "I1234V",
    "0.000397904370316334",
    "3832A>G"
  ],
  "3832A>G": [
    "No",
    "84",
    "p.Ile1234Val",
    "CF-causing",
    "c.3700A>G",
    "I1234V",
    "0.000397904370316334",
    "3832A>G"
  ],
  "83": [
    "No",
    "83",
    "p.Arg785X",
    "0.0003931674135268538",
    "CF-causing",
    "R785X",
    "c.2353C>T",
    "2485C>T"
  ],
  "p.Arg785X": [
    "No",
    "83",
    "p.Arg785X",
    "0.0003931674135268538",
    "CF-causing",
    "R785X",
    "c.2353C>T",
    "2485C>T"
  ],
  "0.0003931674135268538": [
    "No",
    "83",
    "p.Arg785X",
    "0.0003931674135268538",
    "CF-causing",
    "R785X",
    "c.2353C>T",
    "2485C>T"
  ],
  "R785X": [
    "No",
    "83",
    "p.Arg785X",
    "0.0003931674135268538",
    "CF-causing",
    "R785X",
    "c.2353C>T",
    "2485C>T"
  ],
  "c.2353C>T": [
    "No",
    "83",
    "p.Arg785X",
    "0.0003931674135268538",
    "CF-causing",
    "R785X",
    "c.2353C>T",
    "2485C>T"
  ],
  "2485C>T": [
    "No",
    "83",
    "p.Arg785X",
    "0.0003931674135268538",
    "CF-causing",
    "R785X",
    "c.2353C>T",
    "2485C>T"
  ],
  "c.1400T>C": [
    "c.1400T>C",
    "No",
    "0.00038843045673737366",
    "1532T>C",
    "82",
    "CF-causing",
    "p.Leu467Pro",
    "L467P"
  ],
  "0.00038843045673737366": [
    "No",
    "p.Gln890X",
    "c.2668C>T",
    "0.00038843045673737366",
    "82",
    "CF-causing",
    "Q890X",
    "2800C>T"
  ],
  "1532T>C": [
    "c.1400T>C",
    "No",
    "0.00038843045673737366",
    "1532T>C",
    "82",
    "CF-causing",
    "p.Leu467Pro",
    "L467P"
  ],
  "82": [
    "No",
    "p.Gln890X",
    "c.2668C>T",
    "0.00038843045673737366",
    "82",
    "CF-causing",
    "Q890X",
    "2800C>T"
  ],
  "p.Leu467Pro": [
    "c.1400T>C",
    "No",
    "0.00038843045673737366",
    "1532T>C",
    "82",
    "CF-causing",
    "p.Leu467Pro",
    "L467P"
  ],
  "L467P": [
    "c.1400T>C",
    "No",
    "0.00038843045673737366",
    "1532T>C",
    "82",
    "CF-causing",
    "p.Leu467Pro",
    "L467P"
  ],
  "p.Gln890X": [
    "No",
    "p.Gln890X",
    "c.2668C>T",
    "0.00038843045673737366",
    "82",
    "CF-causing",
    "Q890X",
    "2800C>T"
  ],
  "c.2668C>T": [
    "No",
    "p.Gln890X",
    "c.2668C>T",
    "0.00038843045673737366",
    "82",
    "CF-causing",
    "Q890X",
    "2800C>T"
  ],
  "Q890X": [
    "No",
    "p.Gln890X",
    "c.2668C>T",
    "0.00038843045673737366",
    "82",
    "CF-causing",
    "Q890X",
    "2800C>T"
  ],
  "2800C>T": [
    "No",
    "p.Gln890X",
    "c.2668C>T",
    "0.00038843045673737366",
    "82",
    "CF-causing",
    "Q890X",
    "2800C>T"
  ],
  "247C>T": [
    "247C>T",
    "No",
    "c.115C>T",
    "81",
    "Q39X",
    "p.Gln39X",
    "CF-causing",
    "0.00038369349994789347"
  ],
  "c.115C>T": [
    "247C>T",
    "No",
    "c.115C>T",
    "81",
    "Q39X",
    "p.Gln39X",
    "CF-causing",
    "0.00038369349994789347"
  ],
  "81": [
    "247C>T",
    "No",
    "c.115C>T",
    "81",
    "Q39X",
    "p.Gln39X",
    "CF-causing",
    "0.00038369349994789347"
  ],
  "Q39X": [
    "247C>T",
    "No",
    "c.115C>T",
    "81",
    "Q39X",
    "p.Gln39X",
    "CF-causing",
    "0.00038369349994789347"
  ],
  "p.Gln39X": [
    "247C>T",
    "No",
    "c.115C>T",
    "81",
    "Q39X",
    "p.Gln39X",
    "CF-causing",
    "0.00038369349994789347"
  ],
  "0.00038369349994789347": [
    "247C>T",
    "No",
    "c.115C>T",
    "81",
    "Q39X",
    "p.Gln39X",
    "CF-causing",
    "0.00038369349994789347"
  ],
  "78": [
    "p.?",
    "No",
    "78",
    "c.1116+1G>A",
    "CF-causing",
    "1248+1G->A",
    "0.000369482629579453"
  ],
  "c.1116+1G>A": [
    "p.?",
    "No",
    "78",
    "c.1116+1G>A",
    "CF-causing",
    "1248+1G->A",
    "0.000369482629579453"
  ],
  "1248+1G->A": [
    "p.?",
    "No",
    "78",
    "c.1116+1G>A",
    "CF-causing",
    "1248+1G->A",
    "0.000369482629579453"
  ],
  "0.000369482629579453": [
    "p.?",
    "No",
    "78",
    "c.1116+1G>A",
    "CF-causing",
    "1248+1G->A",
    "0.000369482629579453"
  ],
  "E92X": [
    "E92X",
    "406G>T",
    "No",
    "0.0003647456727899728",
    "c.274G>T",
    "CF-causing",
    "77",
    "p.Glu92X"
  ],
  "406G>T": [
    "E92X",
    "406G>T",
    "No",
    "0.0003647456727899728",
    "c.274G>T",
    "CF-causing",
    "77",
    "p.Glu92X"
  ],
  "0.0003647456727899728": [
    "E92X",
    "406G>T",
    "No",
    "0.0003647456727899728",
    "c.274G>T",
    "CF-causing",
    "77",
    "p.Glu92X"
  ],
  "c.274G>T": [
    "E92X",
    "406G>T",
    "No",
    "0.0003647456727899728",
    "c.274G>T",
    "CF-causing",
    "77",
    "p.Glu92X"
  ],
  "77": [
    "E92X",
    "406G>T",
    "No",
    "0.0003647456727899728",
    "c.274G>T",
    "CF-causing",
    "77",
    "p.Glu92X"
  ],
  "p.Glu92X": [
    "E92X",
    "406G>T",
    "No",
    "0.0003647456727899728",
    "c.274G>T",
    "CF-causing",
    "77",
    "p.Glu92X"
  ],
  "c.2537G>A|c.2538G>A": [
    "c.2537G>A|c.2538G>A",
    "No",
    "2669G>A|2670G>A",
    "p.Trp846X",
    "CF-causing",
    "W846X",
    "0.00035527175921101247",
    "75"
  ],
  "2669G>A|2670G>A": [
    "c.2537G>A|c.2538G>A",
    "No",
    "2669G>A|2670G>A",
    "p.Trp846X",
    "CF-causing",
    "W846X",
    "0.00035527175921101247",
    "75"
  ],
  "p.Trp846X": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.2538delG",
    "p.Trp846X",
    "CF-causing",
    "1",
    "c.2538del"
  ],
  "W846X": [
    "c.2537G>A|c.2538G>A",
    "No",
    "2669G>A|2670G>A",
    "p.Trp846X",
    "CF-causing",
    "W846X",
    "0.00035527175921101247",
    "75"
  ],
  "0.00035527175921101247": [
    "No",
    "CF-causing",
    "0.00035527175921101247",
    "c.2215del",
    "75",
    "p.Val739TyrfsX16",
    "2347delG"
  ],
  "75": [
    "No",
    "CF-causing",
    "0.00035527175921101247",
    "c.2215del",
    "75",
    "p.Val739TyrfsX16",
    "2347delG"
  ],
  "c.2215del": [
    "No",
    "CF-causing",
    "0.00035527175921101247",
    "c.2215del",
    "75",
    "p.Val739TyrfsX16",
    "2347delG"
  ],
  "p.Val739TyrfsX16": [
    "No",
    "CF-causing",
    "0.00035527175921101247",
    "c.2215del",
    "75",
    "p.Val739TyrfsX16",
    "2347delG"
  ],
  "2347delG": [
    "No",
    "CF-causing",
    "0.00035527175921101247",
    "c.2215del",
    "75",
    "p.Val739TyrfsX16",
    "2347delG"
  ],
  "G576A": [
    "G576A",
    "No",
    "c.1727G>C",
    "p.Gly576Ala",
    "1859G>C",
    "0.000341060888842572",
    "Non CF-causing",
    "72"
  ],
  "c.1727G>C": [
    "G576A",
    "No",
    "c.1727G>C",
    "p.Gly576Ala",
    "1859G>C",
    "0.000341060888842572",
    "Non CF-causing",
    "72"
  ],
  "p.Gly576Ala": [
    "G576A",
    "No",
    "c.1727G>C",
    "p.Gly576Ala",
    "1859G>C",
    "0.000341060888842572",
    "Non CF-causing",
    "72"
  ],
  "1859G>C": [
    "G576A",
    "No",
    "c.1727G>C",
    "p.Gly576Ala",
    "1859G>C",
    "0.000341060888842572",
    "Non CF-causing",
    "72"
  ],
  "0.000341060888842572": [
    "1898+3A->G",
    "p.?",
    "No",
    "CF-causing",
    "0.000341060888842572",
    "72",
    "c.1766+3A>G"
  ],
  "72": [
    "1898+3A->G",
    "p.?",
    "No",
    "CF-causing",
    "0.000341060888842572",
    "72",
    "c.1766+3A>G"
  ],
  "1898+3A->G": [
    "1898+3A->G",
    "p.?",
    "No",
    "CF-causing",
    "0.000341060888842572",
    "72",
    "c.1766+3A>G"
  ],
  "c.1766+3A>G": [
    "1898+3A->G",
    "p.?",
    "No",
    "CF-causing",
    "0.000341060888842572",
    "72",
    "c.1766+3A>G"
  ],
  "0.0003363239320530918": [
    "p.?",
    "No",
    "0.0003363239320530918",
    "CF-causing",
    "71",
    "c.(3963+1_3964-1)_(*1_?)del",
    "deletion of exons 22, 23, and 24 (legacy numbering)|deletion of exons 25, 26, and 27 (current numbering)",
    "CFTRdele22-24"
  ],
  "71": [
    "p.?",
    "No",
    "0.0003363239320530918",
    "CF-causing",
    "71",
    "c.(3963+1_3964-1)_(*1_?)del",
    "deletion of exons 22, 23, and 24 (legacy numbering)|deletion of exons 25, 26, and 27 (current numbering)",
    "CFTRdele22-24"
  ],
  "c.(3963+1_3964-1)_(*1_?)del": [
    "p.?",
    "No",
    "0.0003363239320530918",
    "CF-causing",
    "71",
    "c.(3963+1_3964-1)_(*1_?)del",
    "deletion of exons 22, 23, and 24 (legacy numbering)|deletion of exons 25, 26, and 27 (current numbering)",
    "CFTRdele22-24"
  ],
  "deletion of exons 22, 23, and 24 (legacy numbering)|deletion of exons 25, 26, and 27 (current numbering)": [
    "p.?",
    "No",
    "0.0003363239320530918",
    "CF-causing",
    "71",
    "c.(3963+1_3964-1)_(*1_?)del",
    "deletion of exons 22, 23, and 24 (legacy numbering)|deletion of exons 25, 26, and 27 (current numbering)",
    "CFTRdele22-24"
  ],
  "CFTRdele22-24": [
    "p.?",
    "No",
    "0.0003363239320530918",
    "CF-causing",
    "71",
    "c.(3963+1_3964-1)_(*1_?)del",
    "deletion of exons 22, 23, and 24 (legacy numbering)|deletion of exons 25, 26, and 27 (current numbering)",
    "CFTRdele22-24"
  ],
  "406-1G->A": [
    "406-1G->A",
    "p.?",
    "No",
    "0.00033158697526361166",
    "c.274-1G>A",
    "CF-causing",
    "70"
  ],
  "0.00033158697526361166": [
    "406-1G->A",
    "p.?",
    "No",
    "0.00033158697526361166",
    "c.274-1G>A",
    "CF-causing",
    "70"
  ],
  "c.274-1G>A": [
    "406-1G->A",
    "p.?",
    "No",
    "0.00033158697526361166",
    "c.274-1G>A",
    "CF-causing",
    "70"
  ],
  "70": [
    "406-1G->A",
    "p.?",
    "No",
    "0.00033158697526361166",
    "c.274-1G>A",
    "CF-causing",
    "70"
  ],
  "c.1705T>G": [
    "c.1705T>G",
    "p.Tyr569Asp",
    "No",
    "0.00032685001847413146",
    "Y569D",
    "1837T>G",
    "CF-causing",
    "69"
  ],
  "p.Tyr569Asp": [
    "c.1705T>G",
    "p.Tyr569Asp",
    "No",
    "0.00032685001847413146",
    "Y569D",
    "1837T>G",
    "CF-causing",
    "69"
  ],
  "0.00032685001847413146": [
    "c.1705T>G",
    "p.Tyr569Asp",
    "No",
    "0.00032685001847413146",
    "Y569D",
    "1837T>G",
    "CF-causing",
    "69"
  ],
  "Y569D": [
    "c.1705T>G",
    "p.Tyr569Asp",
    "No",
    "0.00032685001847413146",
    "Y569D",
    "1837T>G",
    "CF-causing",
    "69"
  ],
  "1837T>G": [
    "c.1705T>G",
    "p.Tyr569Asp",
    "No",
    "0.00032685001847413146",
    "Y569D",
    "1837T>G",
    "CF-causing",
    "69"
  ],
  "69": [
    "c.1705T>G",
    "p.Tyr569Asp",
    "No",
    "0.00032685001847413146",
    "Y569D",
    "1837T>G",
    "CF-causing",
    "69"
  ],
  "0.0003221130616846513": [
    "0.0003221130616846513",
    "No",
    "Varying clinical consequence",
    "p.Arg1070Trp",
    "68",
    "3340C>T",
    "R1070W",
    "c.3208C>T"
  ],
  "p.Arg1070Trp": [
    "0.0003221130616846513",
    "No",
    "Varying clinical consequence",
    "p.Arg1070Trp",
    "68",
    "3340C>T",
    "R1070W",
    "c.3208C>T"
  ],
  "68": [
    "0.0003221130616846513",
    "No",
    "Varying clinical consequence",
    "p.Arg1070Trp",
    "68",
    "3340C>T",
    "R1070W",
    "c.3208C>T"
  ],
  "3340C>T": [
    "0.0003221130616846513",
    "No",
    "Varying clinical consequence",
    "p.Arg1070Trp",
    "68",
    "3340C>T",
    "R1070W",
    "c.3208C>T"
  ],
  "R1070W": [
    "0.0003221130616846513",
    "No",
    "Varying clinical consequence",
    "p.Arg1070Trp",
    "68",
    "3340C>T",
    "R1070W",
    "c.3208C>T"
  ],
  "c.3208C>T": [
    "0.0003221130616846513",
    "No",
    "Varying clinical consequence",
    "p.Arg1070Trp",
    "68",
    "3340C>T",
    "R1070W",
    "c.3208C>T"
  ],
  "c.2290C>T": [
    "c.2290C>T",
    "R764X",
    "No",
    "2422C>T",
    "CF-causing",
    "65",
    "0.0003079021913162108",
    "p.Arg764X"
  ],
  "R764X": [
    "c.2290C>T",
    "R764X",
    "No",
    "2422C>T",
    "CF-causing",
    "65",
    "0.0003079021913162108",
    "p.Arg764X"
  ],
  "2422C>T": [
    "c.2290C>T",
    "R764X",
    "No",
    "2422C>T",
    "CF-causing",
    "65",
    "0.0003079021913162108",
    "p.Arg764X"
  ],
  "65": [
    "c.2290C>T",
    "R764X",
    "No",
    "2422C>T",
    "CF-causing",
    "65",
    "0.0003079021913162108",
    "p.Arg764X"
  ],
  "0.0003079021913162108": [
    "c.2290C>T",
    "R764X",
    "No",
    "2422C>T",
    "CF-causing",
    "65",
    "0.0003079021913162108",
    "p.Arg764X"
  ],
  "p.Arg764X": [
    "c.2290C>T",
    "R764X",
    "No",
    "2422C>T",
    "CF-causing",
    "65",
    "0.0003079021913162108",
    "p.Arg764X"
  ],
  "64": [
    "64",
    "No",
    "0.00030316523452673065",
    "CF-causing",
    "2596G>T",
    "c.2464G>T",
    "E822X",
    "p.Glu822X"
  ],
  "0.00030316523452673065": [
    "64",
    "No",
    "0.00030316523452673065",
    "CF-causing",
    "2596G>T",
    "c.2464G>T",
    "E822X",
    "p.Glu822X"
  ],
  "2596G>T": [
    "64",
    "No",
    "0.00030316523452673065",
    "CF-causing",
    "2596G>T",
    "c.2464G>T",
    "E822X",
    "p.Glu822X"
  ],
  "c.2464G>T": [
    "64",
    "No",
    "0.00030316523452673065",
    "CF-causing",
    "2596G>T",
    "c.2464G>T",
    "E822X",
    "p.Glu822X"
  ],
  "E822X": [
    "64",
    "No",
    "0.00030316523452673065",
    "CF-causing",
    "2596G>T",
    "c.2464G>T",
    "E822X",
    "p.Glu822X"
  ],
  "p.Glu822X": [
    "64",
    "No",
    "0.00030316523452673065",
    "CF-causing",
    "2596G>T",
    "c.2464G>T",
    "E822X",
    "p.Glu822X"
  ],
  "3281T>C": [
    "No",
    "3281T>C",
    "L1065P",
    "c.3194T>C",
    "p.Leu1065Pro",
    "0.00029842827773725046",
    "CF-causing",
    "63"
  ],
  "L1065P": [
    "No",
    "3281T>C",
    "L1065P",
    "c.3194T>C",
    "p.Leu1065Pro",
    "0.00029842827773725046",
    "CF-causing",
    "63"
  ],
  "c.3194T>C": [
    "No",
    "3281T>C",
    "L1065P",
    "c.3194T>C",
    "p.Leu1065Pro",
    "0.00029842827773725046",
    "CF-causing",
    "63"
  ],
  "p.Leu1065Pro": [
    "No",
    "3281T>C",
    "L1065P",
    "c.3194T>C",
    "p.Leu1065Pro",
    "0.00029842827773725046",
    "CF-causing",
    "63"
  ],
  "0.00029842827773725046": [
    "No",
    "3281T>C",
    "L1065P",
    "c.3194T>C",
    "p.Leu1065Pro",
    "0.00029842827773725046",
    "CF-causing",
    "63"
  ],
  "63": [
    "No",
    "3281T>C",
    "L1065P",
    "c.3194T>C",
    "p.Leu1065Pro",
    "0.00029842827773725046",
    "CF-causing",
    "63"
  ],
  "p.Gln552X": [
    "No",
    "p.Gln552X",
    "1786C>T",
    "CF-causing",
    "Q552X",
    "c.1654C>T",
    "62",
    "0.0002936913209477703"
  ],
  "1786C>T": [
    "No",
    "p.Gln552X",
    "1786C>T",
    "CF-causing",
    "Q552X",
    "c.1654C>T",
    "62",
    "0.0002936913209477703"
  ],
  "Q552X": [
    "No",
    "p.Gln552X",
    "1786C>T",
    "CF-causing",
    "Q552X",
    "c.1654C>T",
    "62",
    "0.0002936913209477703"
  ],
  "c.1654C>T": [
    "No",
    "p.Gln552X",
    "1786C>T",
    "CF-causing",
    "Q552X",
    "c.1654C>T",
    "62",
    "0.0002936913209477703"
  ],
  "62": [
    "3341G>A",
    "p.Arg1070Gln",
    "c.3209G>A",
    "No",
    "Varying clinical consequence",
    "62",
    "R1070Q",
    "0.0002936913209477703"
  ],
  "0.0002936913209477703": [
    "3341G>A",
    "p.Arg1070Gln",
    "c.3209G>A",
    "No",
    "Varying clinical consequence",
    "62",
    "R1070Q",
    "0.0002936913209477703"
  ],
  "3341G>A": [
    "3341G>A",
    "p.Arg1070Gln",
    "c.3209G>A",
    "No",
    "Varying clinical consequence",
    "62",
    "R1070Q",
    "0.0002936913209477703"
  ],
  "p.Arg1070Gln": [
    "3341G>A",
    "p.Arg1070Gln",
    "c.3209G>A",
    "No",
    "Varying clinical consequence",
    "62",
    "R1070Q",
    "0.0002936913209477703"
  ],
  "c.3209G>A": [
    "3341G>A",
    "p.Arg1070Gln",
    "c.3209G>A",
    "No",
    "Varying clinical consequence",
    "62",
    "R1070Q",
    "0.0002936913209477703"
  ],
  "R1070Q": [
    "3341G>A",
    "p.Arg1070Gln",
    "c.3209G>A",
    "No",
    "Varying clinical consequence",
    "62",
    "R1070Q",
    "0.0002936913209477703"
  ],
  "E528E": [
    "E528E",
    "p.Glu528=",
    "No",
    "c.1584G>A",
    "61",
    "1716G/A",
    "Non CF-causing",
    "0.0002889543641582901"
  ],
  "p.Glu528=": [
    "E528E",
    "p.Glu528=",
    "No",
    "c.1584G>A",
    "61",
    "1716G/A",
    "Non CF-causing",
    "0.0002889543641582901"
  ],
  "c.1584G>A": [
    "E528E",
    "p.Glu528=",
    "No",
    "c.1584G>A",
    "61",
    "1716G/A",
    "Non CF-causing",
    "0.0002889543641582901"
  ],
  "61": [
    "E528E",
    "p.Glu528=",
    "No",
    "c.1584G>A",
    "61",
    "1716G/A",
    "Non CF-causing",
    "0.0002889543641582901"
  ],
  "1716G/A": [
    "E528E",
    "p.Glu528=",
    "No",
    "c.1584G>A",
    "61",
    "1716G/A",
    "Non CF-causing",
    "0.0002889543641582901"
  ],
  "0.0002889543641582901": [
    "E528E",
    "p.Glu528=",
    "No",
    "c.1584G>A",
    "61",
    "1716G/A",
    "Non CF-causing",
    "0.0002889543641582901"
  ],
  "60": [
    "No",
    "60",
    "R851X",
    "p.Arg851X",
    "CF-causing",
    "2683C>T",
    "0.00028421740736881",
    "c.2551C>T"
  ],
  "R851X": [
    "No",
    "60",
    "R851X",
    "p.Arg851X",
    "CF-causing",
    "2683C>T",
    "0.00028421740736881",
    "c.2551C>T"
  ],
  "p.Arg851X": [
    "No",
    "60",
    "R851X",
    "p.Arg851X",
    "CF-causing",
    "2683C>T",
    "0.00028421740736881",
    "c.2551C>T"
  ],
  "2683C>T": [
    "No",
    "60",
    "R851X",
    "p.Arg851X",
    "CF-causing",
    "2683C>T",
    "0.00028421740736881",
    "c.2551C>T"
  ],
  "0.00028421740736881": [
    "No",
    "60",
    "R851X",
    "p.Arg851X",
    "CF-causing",
    "2683C>T",
    "0.00028421740736881",
    "c.2551C>T"
  ],
  "c.2551C>T": [
    "No",
    "60",
    "R851X",
    "p.Arg851X",
    "CF-causing",
    "2683C>T",
    "0.00028421740736881",
    "c.2551C>T"
  ],
  "c.1475C>T": [
    "No",
    "c.1475C>T",
    "59",
    "p.Ser492Phe",
    "CF-causing",
    "1607C>T",
    "S492F",
    "0.0002794804505793298"
  ],
  "59": [
    "R668C",
    "c.2002C>T",
    "No",
    "59",
    "p.Arg668Cys",
    "2134C>T",
    "Non CF-causing",
    "0.0002794804505793298"
  ],
  "p.Ser492Phe": [
    "No",
    "c.1475C>T",
    "59",
    "p.Ser492Phe",
    "CF-causing",
    "1607C>T",
    "S492F",
    "0.0002794804505793298"
  ],
  "1607C>T": [
    "No",
    "c.1475C>T",
    "59",
    "p.Ser492Phe",
    "CF-causing",
    "1607C>T",
    "S492F",
    "0.0002794804505793298"
  ],
  "S492F": [
    "No",
    "c.1475C>T",
    "59",
    "p.Ser492Phe",
    "CF-causing",
    "1607C>T",
    "S492F",
    "0.0002794804505793298"
  ],
  "0.0002794804505793298": [
    "R668C",
    "c.2002C>T",
    "No",
    "59",
    "p.Arg668Cys",
    "2134C>T",
    "Non CF-causing",
    "0.0002794804505793298"
  ],
  "R668C": [
    "R668C",
    "c.2002C>T",
    "No",
    "59",
    "p.Arg668Cys",
    "2134C>T",
    "Non CF-causing",
    "0.0002794804505793298"
  ],
  "c.2002C>T": [
    "R668C",
    "c.2002C>T",
    "No",
    "59",
    "p.Arg668Cys",
    "2134C>T",
    "Non CF-causing",
    "0.0002794804505793298"
  ],
  "p.Arg668Cys": [
    "R668C",
    "c.2002C>T",
    "No",
    "59",
    "p.Arg668Cys",
    "2134C>T",
    "Non CF-causing",
    "0.0002794804505793298"
  ],
  "2134C>T": [
    "R668C",
    "c.2002C>T",
    "No",
    "59",
    "p.Arg668Cys",
    "2134C>T",
    "Non CF-causing",
    "0.0002794804505793298"
  ],
  "c.1367T>C": [
    "c.1367T>C",
    "No",
    "1499T>C",
    "p.Val456Ala",
    "CF-causing",
    "V456A",
    "58",
    "0.00027474349378984965"
  ],
  "1499T>C": [
    "c.1367T>C",
    "No",
    "1499T>C",
    "p.Val456Ala",
    "CF-causing",
    "V456A",
    "58",
    "0.00027474349378984965"
  ],
  "p.Val456Ala": [
    "c.1367T>C",
    "No",
    "1499T>C",
    "p.Val456Ala",
    "CF-causing",
    "V456A",
    "58",
    "0.00027474349378984965"
  ],
  "V456A": [
    "c.1367T>C",
    "No",
    "1499T>C",
    "p.Val456Ala",
    "CF-causing",
    "V456A",
    "58",
    "0.00027474349378984965"
  ],
  "58": [
    "No",
    "CF-causing",
    "S466X in cis with R1070Q|[1529C>G with 3341G>A]",
    "58",
    "0.00027474349378984965",
    "c.[1397C>A;3209G>A]|c.[1397C>G;3209G>A]",
    "S466X;R1070Q"
  ],
  "0.00027474349378984965": [
    "No",
    "CF-causing",
    "S466X in cis with R1070Q|[1529C>G with 3341G>A]",
    "58",
    "0.00027474349378984965",
    "c.[1397C>A;3209G>A]|c.[1397C>G;3209G>A]",
    "S466X;R1070Q"
  ],
  "S466X in cis with R1070Q|[1529C>G with 3341G>A]": [
    "No",
    "CF-causing",
    "S466X in cis with R1070Q|[1529C>G with 3341G>A]",
    "58",
    "0.00027474349378984965",
    "c.[1397C>A;3209G>A]|c.[1397C>G;3209G>A]",
    "S466X;R1070Q"
  ],
  "c.[1397C>A;3209G>A]|c.[1397C>G;3209G>A]": [
    "No",
    "CF-causing",
    "S466X in cis with R1070Q|[1529C>G with 3341G>A]",
    "58",
    "0.00027474349378984965",
    "c.[1397C>A;3209G>A]|c.[1397C>G;3209G>A]",
    "S466X;R1070Q"
  ],
  "S466X;R1070Q": [
    "No",
    "CF-causing",
    "S466X in cis with R1070Q|[1529C>G with 3341G>A]",
    "58",
    "0.00027474349378984965",
    "c.[1397C>A;3209G>A]|c.[1397C>G;3209G>A]",
    "S466X;R1070Q"
  ],
  "0.0002700065370003695": [
    "c.1680-877G>T",
    "p.?",
    "No",
    "0.0002700065370003695",
    "CF-causing",
    "c.1679+1643G>T",
    "57",
    "1811+1643G->T"
  ],
  "S1196X": [
    "No",
    "0.0002700065370003695",
    "CF-causing",
    "S1196X",
    "3719C>G",
    "57",
    "p.Ser1196X",
    "c.3587C>A|c.3587C>G"
  ],
  "3719C>G": [
    "No",
    "0.0002700065370003695",
    "CF-causing",
    "S1196X",
    "3719C>G",
    "57",
    "p.Ser1196X",
    "c.3587C>A|c.3587C>G"
  ],
  "57": [
    "c.1680-877G>T",
    "p.?",
    "No",
    "0.0002700065370003695",
    "CF-causing",
    "c.1679+1643G>T",
    "57",
    "1811+1643G->T"
  ],
  "p.Ser1196X": [
    "No",
    "0.0002700065370003695",
    "CF-causing",
    "S1196X",
    "3719C>G",
    "57",
    "p.Ser1196X",
    "c.3587C>A|c.3587C>G"
  ],
  "c.3587C>A|c.3587C>G": [
    "No",
    "0.0002700065370003695",
    "CF-causing",
    "S1196X",
    "3719C>G",
    "57",
    "p.Ser1196X",
    "c.3587C>A|c.3587C>G"
  ],
  "c.1680-877G>T": [
    "c.1680-877G>T",
    "p.?",
    "No",
    "0.0002700065370003695",
    "CF-causing",
    "c.1679+1643G>T",
    "57",
    "1811+1643G->T"
  ],
  "c.1679+1643G>T": [
    "c.1680-877G>T",
    "p.?",
    "No",
    "0.0002700065370003695",
    "CF-causing",
    "c.1679+1643G>T",
    "57",
    "1811+1643G->T"
  ],
  "1811+1643G->T": [
    "c.1680-877G>T",
    "p.?",
    "No",
    "0.0002700065370003695",
    "CF-causing",
    "c.1679+1643G>T",
    "57",
    "1811+1643G->T"
  ],
  "p.Thr854=": [
    "p.Thr854=",
    "c.2562T>A|c.2562T>C|c.2562T>G",
    "56",
    "No",
    "T854T",
    "2694T/G|2694T/C|2694T>C|2694T>G|2694T>A",
    "Non CF-causing",
    "0.0002652695802108893"
  ],
  "c.2562T>A|c.2562T>C|c.2562T>G": [
    "p.Thr854=",
    "c.2562T>A|c.2562T>C|c.2562T>G",
    "56",
    "No",
    "T854T",
    "2694T/G|2694T/C|2694T>C|2694T>G|2694T>A",
    "Non CF-causing",
    "0.0002652695802108893"
  ],
  "56": [
    "56",
    "wild-type/reference",
    "p.?",
    "No",
    "7T",
    "Non CF-causing",
    "0.0002652695802108893"
  ],
  "T854T": [
    "p.Thr854=",
    "c.2562T>A|c.2562T>C|c.2562T>G",
    "56",
    "No",
    "T854T",
    "2694T/G|2694T/C|2694T>C|2694T>G|2694T>A",
    "Non CF-causing",
    "0.0002652695802108893"
  ],
  "2694T/G|2694T/C|2694T>C|2694T>G|2694T>A": [
    "p.Thr854=",
    "c.2562T>A|c.2562T>C|c.2562T>G",
    "56",
    "No",
    "T854T",
    "2694T/G|2694T/C|2694T>C|2694T>G|2694T>A",
    "Non CF-causing",
    "0.0002652695802108893"
  ],
  "0.0002652695802108893": [
    "56",
    "wild-type/reference",
    "p.?",
    "No",
    "7T",
    "Non CF-causing",
    "0.0002652695802108893"
  ],
  "405+1G->A": [
    "56",
    "p.?",
    "No",
    "CF-causing",
    "0.0002652695802108893",
    "405+1G->A",
    "c.273+1G>A"
  ],
  "c.273+1G>A": [
    "56",
    "p.?",
    "No",
    "CF-causing",
    "0.0002652695802108893",
    "405+1G->A",
    "c.273+1G>A"
  ],
  "c.2583del": [
    "56",
    "No",
    "c.2583del",
    "CF-causing",
    "0.0002652695802108893",
    "2711delT",
    "p.Phe861LeufsX3"
  ],
  "2711delT": [
    "56",
    "No",
    "c.2583del",
    "CF-causing",
    "0.0002652695802108893",
    "2711delT",
    "p.Phe861LeufsX3"
  ],
  "p.Phe861LeufsX3": [
    "56",
    "No",
    "c.2583del",
    "CF-causing",
    "0.0002652695802108893",
    "2711delT",
    "p.Phe861LeufsX3"
  ],
  "p.Tyr109GlyfsX4": [
    "56",
    "No",
    "p.Tyr109GlyfsX4",
    "CF-causing",
    "0.0002652695802108893",
    "c.325_327delinsG",
    "457TAT->G"
  ],
  "c.325_327delinsG": [
    "56",
    "No",
    "p.Tyr109GlyfsX4",
    "CF-causing",
    "0.0002652695802108893",
    "c.325_327delinsG",
    "457TAT->G"
  ],
  "457TAT->G": [
    "56",
    "No",
    "p.Tyr109GlyfsX4",
    "CF-causing",
    "0.0002652695802108893",
    "c.325_327delinsG",
    "457TAT->G"
  ],
  "wild-type/reference": [
    "56",
    "wild-type/reference",
    "p.?",
    "No",
    "7T",
    "Non CF-causing",
    "0.0002652695802108893"
  ],
  "7T": [
    "56",
    "wild-type/reference",
    "p.?",
    "No",
    "7T",
    "Non CF-causing",
    "0.0002652695802108893"
  ],
  "0.0002605326234214092": [
    "No",
    "0.0002605326234214092",
    "CF-causing",
    "c.2875del",
    "p.Ala959HisfsX9",
    "3007delG",
    "55"
  ],
  "4005+2T->C": [
    "p.?",
    "No",
    "0.0002605326234214092",
    "CF-causing",
    "4005+2T->C",
    "55",
    "c.3873+2T>C"
  ],
  "55": [
    "No",
    "0.0002605326234214092",
    "CF-causing",
    "c.2875del",
    "p.Ala959HisfsX9",
    "3007delG",
    "55"
  ],
  "c.3873+2T>C": [
    "p.?",
    "No",
    "0.0002605326234214092",
    "CF-causing",
    "4005+2T->C",
    "55",
    "c.3873+2T>C"
  ],
  "c.2875del": [
    "No",
    "0.0002605326234214092",
    "CF-causing",
    "c.2875del",
    "p.Ala959HisfsX9",
    "3007delG",
    "55"
  ],
  "p.Ala959HisfsX9": [
    "No",
    "0.0002605326234214092",
    "CF-causing",
    "c.2875del",
    "p.Ala959HisfsX9",
    "3007delG",
    "55"
  ],
  "3007delG": [
    "No",
    "0.0002605326234214092",
    "CF-causing",
    "c.2875del",
    "p.Ala959HisfsX9",
    "3007delG",
    "55"
  ],
  "0.000255795666631929": [
    "0.000255795666631929",
    "No",
    "c.4046G>A",
    "54",
    "CF-causing",
    "4178G>A",
    "G1349D",
    "p.Gly1349Asp"
  ],
  "c.4046G>A": [
    "0.000255795666631929",
    "No",
    "c.4046G>A",
    "54",
    "CF-causing",
    "4178G>A",
    "G1349D",
    "p.Gly1349Asp"
  ],
  "54": [
    "0.000255795666631929",
    "No",
    "c.4046G>A",
    "54",
    "CF-causing",
    "4178G>A",
    "G1349D",
    "p.Gly1349Asp"
  ],
  "4178G>A": [
    "0.000255795666631929",
    "No",
    "c.4046G>A",
    "54",
    "CF-causing",
    "4178G>A",
    "G1349D",
    "p.Gly1349Asp"
  ],
  "G1349D": [
    "0.000255795666631929",
    "No",
    "c.4046G>A",
    "54",
    "CF-causing",
    "4178G>A",
    "G1349D",
    "p.Gly1349Asp"
  ],
  "p.Gly1349Asp": [
    "0.000255795666631929",
    "No",
    "c.4046G>A",
    "54",
    "CF-causing",
    "4178G>A",
    "G1349D",
    "p.Gly1349Asp"
  ],
  "L558S": [
    "No",
    "L558S",
    "52",
    "0.00024632175305296864",
    "CF-causing",
    "p.Leu558Ser",
    "1805T>C",
    "c.1673T>C"
  ],
  "52": [
    "No",
    "52",
    "0.00024632175305296864",
    "p.Ile148LeufsX5",
    "CF-causing",
    "574delA",
    "c.442del"
  ],
  "0.00024632175305296864": [
    "No",
    "52",
    "0.00024632175305296864",
    "p.Ile148LeufsX5",
    "CF-causing",
    "574delA",
    "c.442del"
  ],
  "p.Leu558Ser": [
    "No",
    "L558S",
    "52",
    "0.00024632175305296864",
    "CF-causing",
    "p.Leu558Ser",
    "1805T>C",
    "c.1673T>C"
  ],
  "1805T>C": [
    "No",
    "L558S",
    "52",
    "0.00024632175305296864",
    "CF-causing",
    "p.Leu558Ser",
    "1805T>C",
    "c.1673T>C"
  ],
  "c.1673T>C": [
    "No",
    "L558S",
    "52",
    "0.00024632175305296864",
    "CF-causing",
    "p.Leu558Ser",
    "1805T>C",
    "c.1673T>C"
  ],
  "4496C>G": [
    "4496C>G",
    "No",
    "S1455X",
    "52",
    "0.00024632175305296864",
    "Varying clinical consequence",
    "p.Ser1455X",
    "c.4364C>G"
  ],
  "S1455X": [
    "4496C>G",
    "No",
    "S1455X",
    "52",
    "0.00024632175305296864",
    "Varying clinical consequence",
    "p.Ser1455X",
    "c.4364C>G"
  ],
  "p.Ser1455X": [
    "4496C>G",
    "No",
    "S1455X",
    "52",
    "0.00024632175305296864",
    "Varying clinical consequence",
    "p.Ser1455X",
    "c.4364C>G"
  ],
  "c.4364C>G": [
    "4496C>G",
    "No",
    "S1455X",
    "52",
    "0.00024632175305296864",
    "Varying clinical consequence",
    "p.Ser1455X",
    "c.4364C>G"
  ],
  "p.Ile148LeufsX5": [
    "No",
    "52",
    "0.00024632175305296864",
    "p.Ile148LeufsX5",
    "CF-causing",
    "574delA",
    "c.442del"
  ],
  "574delA": [
    "No",
    "52",
    "0.00024632175305296864",
    "p.Ile148LeufsX5",
    "CF-causing",
    "574delA",
    "c.442del"
  ],
  "c.442del": [
    "No",
    "52",
    "0.00024632175305296864",
    "p.Ile148LeufsX5",
    "CF-causing",
    "574delA",
    "c.442del"
  ],
  "1259insA": [
    "1259insA",
    "0.00024158479626348848",
    "No",
    "1262insA|c.1127_1128insA",
    "CF-causing",
    "c.1130dup",
    "51",
    "p.Gln378AlafsX4"
  ],
  "0.00024158479626348848": [
    "c.4004T>C",
    "0.00024158479626348848",
    "L1335P",
    "No",
    "p.Leu1335Pro",
    "4136T>C",
    "CF-causing",
    "51"
  ],
  "1262insA|c.1127_1128insA": [
    "1259insA",
    "0.00024158479626348848",
    "No",
    "1262insA|c.1127_1128insA",
    "CF-causing",
    "c.1130dup",
    "51",
    "p.Gln378AlafsX4"
  ],
  "c.1130dup": [
    "1259insA",
    "0.00024158479626348848",
    "No",
    "1262insA|c.1127_1128insA",
    "CF-causing",
    "c.1130dup",
    "51",
    "p.Gln378AlafsX4"
  ],
  "51": [
    "c.4004T>C",
    "0.00024158479626348848",
    "L1335P",
    "No",
    "p.Leu1335Pro",
    "4136T>C",
    "CF-causing",
    "51"
  ],
  "p.Gln378AlafsX4": [
    "1259insA",
    "0.00024158479626348848",
    "No",
    "1262insA|c.1127_1128insA",
    "CF-causing",
    "c.1130dup",
    "51",
    "p.Gln378AlafsX4"
  ],
  "p.His609Arg": [
    "p.His609Arg",
    "0.00024158479626348848",
    "No",
    "CF-causing",
    "H609R",
    "c.1826A>G",
    "51",
    "1958A>G"
  ],
  "H609R": [
    "p.His609Arg",
    "0.00024158479626348848",
    "No",
    "CF-causing",
    "H609R",
    "c.1826A>G",
    "51",
    "1958A>G"
  ],
  "c.1826A>G": [
    "p.His609Arg",
    "0.00024158479626348848",
    "No",
    "CF-causing",
    "H609R",
    "c.1826A>G",
    "51",
    "1958A>G"
  ],
  "1958A>G": [
    "p.His609Arg",
    "0.00024158479626348848",
    "No",
    "CF-causing",
    "H609R",
    "c.1826A>G",
    "51",
    "1958A>G"
  ],
  "L927P": [
    "0.00024158479626348848",
    "No",
    "L927P",
    "p.Leu927Pro",
    "CF-causing",
    "2912T>C",
    "c.2780T>C",
    "51"
  ],
  "p.Leu927Pro": [
    "0.00024158479626348848",
    "No",
    "L927P",
    "p.Leu927Pro",
    "CF-causing",
    "2912T>C",
    "c.2780T>C",
    "51"
  ],
  "2912T>C": [
    "0.00024158479626348848",
    "No",
    "L927P",
    "p.Leu927Pro",
    "CF-causing",
    "2912T>C",
    "c.2780T>C",
    "51"
  ],
  "c.2780T>C": [
    "0.00024158479626348848",
    "No",
    "L927P",
    "p.Leu927Pro",
    "CF-causing",
    "2912T>C",
    "c.2780T>C",
    "51"
  ],
  "c.4004T>C": [
    "c.4004T>C",
    "0.00024158479626348848",
    "L1335P",
    "No",
    "p.Leu1335Pro",
    "4136T>C",
    "CF-causing",
    "51"
  ],
  "L1335P": [
    "c.4004T>C",
    "0.00024158479626348848",
    "L1335P",
    "No",
    "p.Leu1335Pro",
    "4136T>C",
    "CF-causing",
    "51"
  ],
  "p.Leu1335Pro": [
    "c.4004T>C",
    "0.00024158479626348848",
    "L1335P",
    "No",
    "p.Leu1335Pro",
    "4136T>C",
    "CF-causing",
    "51"
  ],
  "4136T>C": [
    "c.4004T>C",
    "0.00024158479626348848",
    "L1335P",
    "No",
    "p.Leu1335Pro",
    "4136T>C",
    "CF-causing",
    "51"
  ],
  "50": [
    "50",
    "No",
    "1609delCA",
    "c.1477_1478del",
    "0.0002368478394740083",
    "CF-causing",
    "p.Gln493ValfsX10"
  ],
  "p.Ser341Pro": [
    "50",
    "No",
    "p.Ser341Pro",
    "S341P",
    "c.1021T>C",
    "0.0002368478394740083",
    "CF-causing",
    "1153T>C"
  ],
  "S341P": [
    "50",
    "No",
    "p.Ser341Pro",
    "S341P",
    "c.1021T>C",
    "0.0002368478394740083",
    "CF-causing",
    "1153T>C"
  ],
  "c.1021T>C": [
    "50",
    "No",
    "p.Ser341Pro",
    "S341P",
    "c.1021T>C",
    "0.0002368478394740083",
    "CF-causing",
    "1153T>C"
  ],
  "0.0002368478394740083": [
    "50",
    "No",
    "1609delCA",
    "c.1477_1478del",
    "0.0002368478394740083",
    "CF-causing",
    "p.Gln493ValfsX10"
  ],
  "1153T>C": [
    "50",
    "No",
    "p.Ser341Pro",
    "S341P",
    "c.1021T>C",
    "0.0002368478394740083",
    "CF-causing",
    "1153T>C"
  ],
  "c.3937C>T": [
    "50",
    "No",
    "c.3937C>T",
    "4069C>T",
    "0.0002368478394740083",
    "CF-causing",
    "p.Gln1313X",
    "Q1313X"
  ],
  "4069C>T": [
    "50",
    "No",
    "c.3937C>T",
    "4069C>T",
    "0.0002368478394740083",
    "CF-causing",
    "p.Gln1313X",
    "Q1313X"
  ],
  "p.Gln1313X": [
    "50",
    "No",
    "c.3937C>T",
    "4069C>T",
    "0.0002368478394740083",
    "CF-causing",
    "p.Gln1313X",
    "Q1313X"
  ],
  "Q1313X": [
    "50",
    "No",
    "c.3937C>T",
    "4069C>T",
    "0.0002368478394740083",
    "CF-causing",
    "p.Gln1313X",
    "Q1313X"
  ],
  "1609delCA": [
    "50",
    "No",
    "1609delCA",
    "c.1477_1478del",
    "0.0002368478394740083",
    "CF-causing",
    "p.Gln493ValfsX10"
  ],
  "c.1477_1478del": [
    "50",
    "No",
    "1609delCA",
    "c.1477_1478del",
    "0.0002368478394740083",
    "CF-causing",
    "p.Gln493ValfsX10"
  ],
  "p.Gln493ValfsX10": [
    "50",
    "No",
    "1609delCA",
    "c.1477_1478del",
    "0.0002368478394740083",
    "CF-causing",
    "p.Gln493ValfsX10"
  ],
  "0.00023211088268452814": [
    "No",
    "0.00023211088268452814",
    "CF-causing",
    "4209TGTT->AA",
    "c.4077_4080delinsAA",
    "p.Val1360ThrfsX3",
    "49"
  ],
  "3313G>C": [
    "No",
    "0.00023211088268452814",
    "3313G>C",
    "c.3181G>A|c.3181G>C",
    "CF-causing",
    "G1061R",
    "49",
    "p.Gly1061Arg"
  ],
  "c.3181G>A|c.3181G>C": [
    "No",
    "0.00023211088268452814",
    "3313G>C",
    "c.3181G>A|c.3181G>C",
    "CF-causing",
    "G1061R",
    "49",
    "p.Gly1061Arg"
  ],
  "G1061R": [
    "No",
    "0.00023211088268452814",
    "3313G>C",
    "c.3181G>A|c.3181G>C",
    "CF-causing",
    "G1061R",
    "49",
    "p.Gly1061Arg"
  ],
  "49": [
    "No",
    "0.00023211088268452814",
    "CF-causing",
    "4209TGTT->AA",
    "c.4077_4080delinsAA",
    "p.Val1360ThrfsX3",
    "49"
  ],
  "p.Gly1061Arg": [
    "No",
    "0.00023211088268452814",
    "3313G>C",
    "c.3181G>A|c.3181G>C",
    "CF-causing",
    "G1061R",
    "49",
    "p.Gly1061Arg"
  ],
  "c.3873G>C": [
    "No",
    "Varying clinical consequence",
    "0.00023211088268452814",
    "c.3873G>C",
    "4005G>C",
    "p.Gln1291His",
    "49",
    "Q1291H"
  ],
  "4005G>C": [
    "No",
    "Varying clinical consequence",
    "0.00023211088268452814",
    "c.3873G>C",
    "4005G>C",
    "p.Gln1291His",
    "49",
    "Q1291H"
  ],
  "p.Gln1291His": [
    "No",
    "Varying clinical consequence",
    "0.00023211088268452814",
    "c.3873G>C",
    "4005G>C",
    "p.Gln1291His",
    "49",
    "Q1291H"
  ],
  "Q1291H": [
    "No",
    "Varying clinical consequence",
    "0.00023211088268452814",
    "c.3873G>C",
    "4005G>C",
    "p.Gln1291His",
    "49",
    "Q1291H"
  ],
  "2105-2117del13insAGAAA": [
    "2105-2117del13insAGAAA",
    "No",
    "c.1973_1985delGAAATTCAATCCTinsAGAAA",
    "0.00023211088268452814",
    "CF-causing",
    "p.Arg658LysfsX4",
    "49",
    "c.1973_1985delinsAGAAA"
  ],
  "c.1973_1985delGAAATTCAATCCTinsAGAAA": [
    "2105-2117del13insAGAAA",
    "No",
    "c.1973_1985delGAAATTCAATCCTinsAGAAA",
    "0.00023211088268452814",
    "CF-causing",
    "p.Arg658LysfsX4",
    "49",
    "c.1973_1985delinsAGAAA"
  ],
  "p.Arg658LysfsX4": [
    "2105-2117del13insAGAAA",
    "No",
    "c.1973_1985delGAAATTCAATCCTinsAGAAA",
    "0.00023211088268452814",
    "CF-causing",
    "p.Arg658LysfsX4",
    "49",
    "c.1973_1985delinsAGAAA"
  ],
  "c.1973_1985delinsAGAAA": [
    "2105-2117del13insAGAAA",
    "No",
    "c.1973_1985delGAAATTCAATCCTinsAGAAA",
    "0.00023211088268452814",
    "CF-causing",
    "p.Arg658LysfsX4",
    "49",
    "c.1973_1985delinsAGAAA"
  ],
  "duplication of exons 6b, 7, 8, 9, and 10 (legacy numbering)|duplication of exons 7, 8, 9, 10, and 11 (current numbering)": [
    "duplication of exons 6b, 7, 8, 9, and 10 (legacy numbering)|duplication of exons 7, 8, 9, 10, and 11 (current numbering)",
    "p.?",
    "No",
    "c.(743+1_744-1)_(1584+1_1585-1)dup",
    "0.00023211088268452814",
    "CF-causing",
    "CFTRdup6b-10",
    "49"
  ],
  "c.(743+1_744-1)_(1584+1_1585-1)dup": [
    "duplication of exons 6b, 7, 8, 9, and 10 (legacy numbering)|duplication of exons 7, 8, 9, 10, and 11 (current numbering)",
    "p.?",
    "No",
    "c.(743+1_744-1)_(1584+1_1585-1)dup",
    "0.00023211088268452814",
    "CF-causing",
    "CFTRdup6b-10",
    "49"
  ],
  "CFTRdup6b-10": [
    "duplication of exons 6b, 7, 8, 9, and 10 (legacy numbering)|duplication of exons 7, 8, 9, 10, and 11 (current numbering)",
    "p.?",
    "No",
    "c.(743+1_744-1)_(1584+1_1585-1)dup",
    "0.00023211088268452814",
    "CF-causing",
    "CFTRdup6b-10",
    "49"
  ],
  "c.1A>G": [
    "p.?",
    "No",
    "0.00023211088268452814",
    "CF-causing",
    "c.1A>G",
    "M1V",
    "p.Met1Val|133A>G",
    "49"
  ],
  "M1V": [
    "p.?",
    "No",
    "0.00023211088268452814",
    "CF-causing",
    "c.1A>G",
    "M1V",
    "p.Met1Val|133A>G",
    "49"
  ],
  "p.Met1Val|133A>G": [
    "p.?",
    "No",
    "0.00023211088268452814",
    "CF-causing",
    "c.1A>G",
    "M1V",
    "p.Met1Val|133A>G",
    "49"
  ],
  "4209TGTT->AA": [
    "No",
    "0.00023211088268452814",
    "CF-causing",
    "4209TGTT->AA",
    "c.4077_4080delinsAA",
    "p.Val1360ThrfsX3",
    "49"
  ],
  "c.4077_4080delinsAA": [
    "No",
    "0.00023211088268452814",
    "CF-causing",
    "4209TGTT->AA",
    "c.4077_4080delinsAA",
    "p.Val1360ThrfsX3",
    "49"
  ],
  "p.Val1360ThrfsX3": [
    "No",
    "0.00023211088268452814",
    "CF-causing",
    "4209TGTT->AA",
    "c.4077_4080delinsAA",
    "p.Val1360ThrfsX3",
    "49"
  ],
  "D1270N": [
    "D1270N",
    "No",
    "3940G>A",
    "48",
    "Varying clinical consequence",
    "p.Asp1270Asn",
    "c.3808G>A",
    "0.00022737392589504798"
  ],
  "3940G>A": [
    "D1270N",
    "No",
    "3940G>A",
    "48",
    "Varying clinical consequence",
    "p.Asp1270Asn",
    "c.3808G>A",
    "0.00022737392589504798"
  ],
  "48": [
    "p.?",
    "No",
    "48",
    "c.1585-8G>A",
    "CF-causing",
    "0.00022737392589504798",
    "1717-8G->A"
  ],
  "p.Asp1270Asn": [
    "D1270N",
    "No",
    "3940G>A",
    "48",
    "Varying clinical consequence",
    "p.Asp1270Asn",
    "c.3808G>A",
    "0.00022737392589504798"
  ],
  "c.3808G>A": [
    "D1270N",
    "No",
    "3940G>A",
    "48",
    "Varying clinical consequence",
    "p.Asp1270Asn",
    "c.3808G>A",
    "0.00022737392589504798"
  ],
  "0.00022737392589504798": [
    "p.?",
    "No",
    "48",
    "c.1585-8G>A",
    "CF-causing",
    "0.00022737392589504798",
    "1717-8G->A"
  ],
  "L218X": [
    "L218X",
    "No",
    "785T>A",
    "c.653T>A",
    "48",
    "CF-causing",
    "0.00022737392589504798",
    "p.Leu218X"
  ],
  "785T>A": [
    "L218X",
    "No",
    "785T>A",
    "c.653T>A",
    "48",
    "CF-causing",
    "0.00022737392589504798",
    "p.Leu218X"
  ],
  "c.653T>A": [
    "L218X",
    "No",
    "785T>A",
    "c.653T>A",
    "48",
    "CF-causing",
    "0.00022737392589504798",
    "p.Leu218X"
  ],
  "p.Leu218X": [
    "L218X",
    "No",
    "785T>A",
    "c.653T>A",
    "48",
    "CF-causing",
    "0.00022737392589504798",
    "p.Leu218X"
  ],
  "c.(2988+1_2989-1)_(3367+1_3368-1)del": [
    "c.(2988+1_2989-1)_(3367+1_3368-1)del",
    "p.?",
    "No",
    "0.00022737392589504798",
    "CFTRdele17a,17b",
    "48",
    "CF-causing",
    "deletion of exons 17a and 17b (legacy numbering)|deletion of exons 19 and 20 (current numbering)|3121-977_3499+248del2515"
  ],
  "CFTRdele17a,17b": [
    "c.(2988+1_2989-1)_(3367+1_3368-1)del",
    "p.?",
    "No",
    "0.00022737392589504798",
    "CFTRdele17a,17b",
    "48",
    "CF-causing",
    "deletion of exons 17a and 17b (legacy numbering)|deletion of exons 19 and 20 (current numbering)|3121-977_3499+248del2515"
  ],
  "deletion of exons 17a and 17b (legacy numbering)|deletion of exons 19 and 20 (current numbering)|3121-977_3499+248del2515": [
    "c.(2988+1_2989-1)_(3367+1_3368-1)del",
    "p.?",
    "No",
    "0.00022737392589504798",
    "CFTRdele17a,17b",
    "48",
    "CF-causing",
    "deletion of exons 17a and 17b (legacy numbering)|deletion of exons 19 and 20 (current numbering)|3121-977_3499+248del2515"
  ],
  "c.1585-8G>A": [
    "p.?",
    "No",
    "48",
    "c.1585-8G>A",
    "CF-causing",
    "0.00022737392589504798",
    "1717-8G->A"
  ],
  "1717-8G->A": [
    "p.?",
    "No",
    "48",
    "c.1585-8G>A",
    "CF-causing",
    "0.00022737392589504798",
    "1717-8G->A"
  ],
  "0.0002226369691055678": [
    "0.0002226369691055678",
    "1949del84",
    "47",
    "No",
    "c.1820_1903del",
    "CF-causing",
    "p.Met607_Gln634del"
  ],
  "47": [
    "0.0002226369691055678",
    "1949del84",
    "47",
    "No",
    "c.1820_1903del",
    "CF-causing",
    "p.Met607_Gln634del"
  ],
  "c.1923_1931delinsA": [
    "0.0002226369691055678",
    "No",
    "47",
    "c.1923_1931delinsA",
    "c.1923_1931delCTCAAAACTinsA",
    "CF-causing",
    "2055del9->A",
    "p.Ser641ArgfsX5"
  ],
  "c.1923_1931delCTCAAAACTinsA": [
    "0.0002226369691055678",
    "No",
    "47",
    "c.1923_1931delinsA",
    "c.1923_1931delCTCAAAACTinsA",
    "CF-causing",
    "2055del9->A",
    "p.Ser641ArgfsX5"
  ],
  "2055del9->A": [
    "0.0002226369691055678",
    "No",
    "47",
    "c.1923_1931delinsA",
    "c.1923_1931delCTCAAAACTinsA",
    "CF-causing",
    "2055del9->A",
    "p.Ser641ArgfsX5"
  ],
  "p.Ser641ArgfsX5": [
    "0.0002226369691055678",
    "No",
    "47",
    "c.1923_1931delinsA",
    "c.1923_1931delCTCAAAACTinsA",
    "CF-causing",
    "2055del9->A",
    "p.Ser641ArgfsX5"
  ],
  "1949del84": [
    "0.0002226369691055678",
    "1949del84",
    "47",
    "No",
    "c.1820_1903del",
    "CF-causing",
    "p.Met607_Gln634del"
  ],
  "c.1820_1903del": [
    "0.0002226369691055678",
    "1949del84",
    "47",
    "No",
    "c.1820_1903del",
    "CF-causing",
    "p.Met607_Gln634del"
  ],
  "p.Met607_Gln634del": [
    "0.0002226369691055678",
    "1949del84",
    "47",
    "No",
    "c.1820_1903del",
    "CF-causing",
    "p.Met607_Gln634del"
  ],
  "0.00021790001231608764": [
    "No",
    "Varying clinical consequence",
    "0.00021790001231608764",
    "D614G",
    "p.Asp614Gly",
    "46",
    "c.1841A>G",
    "1973A>G"
  ],
  "D614G": [
    "No",
    "Varying clinical consequence",
    "0.00021790001231608764",
    "D614G",
    "p.Asp614Gly",
    "46",
    "c.1841A>G",
    "1973A>G"
  ],
  "p.Asp614Gly": [
    "No",
    "Varying clinical consequence",
    "0.00021790001231608764",
    "D614G",
    "p.Asp614Gly",
    "46",
    "c.1841A>G",
    "1973A>G"
  ],
  "46": [
    "No",
    "Varying clinical consequence",
    "0.00021790001231608764",
    "D614G",
    "p.Asp614Gly",
    "46",
    "c.1841A>G",
    "1973A>G"
  ],
  "c.1841A>G": [
    "No",
    "Varying clinical consequence",
    "0.00021790001231608764",
    "D614G",
    "p.Asp614Gly",
    "46",
    "c.1841A>G",
    "1973A>G"
  ],
  "1973A>G": [
    "No",
    "Varying clinical consequence",
    "0.00021790001231608764",
    "D614G",
    "p.Asp614Gly",
    "46",
    "c.1841A>G",
    "1973A>G"
  ],
  "45": [
    "45",
    "No",
    "c.3611G>A|c.3612G>A",
    "p.Trp1204X",
    "3743G>A|3644G>A",
    "CF-causing",
    "0.00021316305552660747",
    "W1204X"
  ],
  "c.3611G>A|c.3612G>A": [
    "45",
    "No",
    "c.3611G>A|c.3612G>A",
    "p.Trp1204X",
    "3743G>A|3644G>A",
    "CF-causing",
    "0.00021316305552660747",
    "W1204X"
  ],
  "p.Trp1204X": [
    "45",
    "No",
    "c.3611G>A|c.3612G>A",
    "p.Trp1204X",
    "3743G>A|3644G>A",
    "CF-causing",
    "0.00021316305552660747",
    "W1204X"
  ],
  "3743G>A|3644G>A": [
    "45",
    "No",
    "c.3611G>A|c.3612G>A",
    "p.Trp1204X",
    "3743G>A|3644G>A",
    "CF-causing",
    "0.00021316305552660747",
    "W1204X"
  ],
  "0.00021316305552660747": [
    "45",
    "No",
    "c.3611G>A|c.3612G>A",
    "p.Trp1204X",
    "3743G>A|3644G>A",
    "CF-causing",
    "0.00021316305552660747",
    "W1204X"
  ],
  "W1204X": [
    "45",
    "No",
    "c.3611G>A|c.3612G>A",
    "p.Trp1204X",
    "3743G>A|3644G>A",
    "CF-causing",
    "0.00021316305552660747",
    "W1204X"
  ],
  "c.1687T>A": [
    "No",
    "c.1687T>A",
    "1819T>A",
    "44",
    "0.0002084260987371273",
    "Y563N",
    "CF-causing",
    "p.Tyr563Asn"
  ],
  "1819T>A": [
    "No",
    "c.1687T>A",
    "1819T>A",
    "44",
    "0.0002084260987371273",
    "Y563N",
    "CF-causing",
    "p.Tyr563Asn"
  ],
  "44": [
    "p.Gly1069Arg",
    "c.3205G>A",
    "No",
    "44",
    "0.0002084260987371273",
    "Varying clinical consequence",
    "G1069R",
    "3337G>A"
  ],
  "0.0002084260987371273": [
    "p.Gly1069Arg",
    "c.3205G>A",
    "No",
    "44",
    "0.0002084260987371273",
    "Varying clinical consequence",
    "G1069R",
    "3337G>A"
  ],
  "Y563N": [
    "No",
    "c.1687T>A",
    "1819T>A",
    "44",
    "0.0002084260987371273",
    "Y563N",
    "CF-causing",
    "p.Tyr563Asn"
  ],
  "p.Tyr563Asn": [
    "No",
    "c.1687T>A",
    "1819T>A",
    "44",
    "0.0002084260987371273",
    "Y563N",
    "CF-causing",
    "p.Tyr563Asn"
  ],
  "p.Gly1069Arg": [
    "p.Gly1069Arg",
    "c.3205G>A",
    "No",
    "44",
    "0.0002084260987371273",
    "Varying clinical consequence",
    "G1069R",
    "3337G>A"
  ],
  "c.3205G>A": [
    "p.Gly1069Arg",
    "c.3205G>A",
    "No",
    "44",
    "0.0002084260987371273",
    "Varying clinical consequence",
    "G1069R",
    "3337G>A"
  ],
  "G1069R": [
    "p.Gly1069Arg",
    "c.3205G>A",
    "No",
    "44",
    "0.0002084260987371273",
    "Varying clinical consequence",
    "G1069R",
    "3337G>A"
  ],
  "3337G>A": [
    "p.Gly1069Arg",
    "c.3205G>A",
    "No",
    "44",
    "0.0002084260987371273",
    "Varying clinical consequence",
    "G1069R",
    "3337G>A"
  ],
  "3032T>C": [
    "3032T>C",
    "p.Leu967Ser",
    "L967S",
    "0.00020368914194764717",
    "Varying clinical consequence",
    "43",
    "Non CF-causing",
    "Yes",
    "c.2900T>C"
  ],
  "p.Leu967Ser": [
    "3032T>C",
    "p.Leu967Ser",
    "L967S",
    "0.00020368914194764717",
    "Varying clinical consequence",
    "43",
    "Non CF-causing",
    "Yes",
    "c.2900T>C"
  ],
  "L967S": [
    "3032T>C",
    "p.Leu967Ser",
    "L967S",
    "0.00020368914194764717",
    "Varying clinical consequence",
    "43",
    "Non CF-causing",
    "Yes",
    "c.2900T>C"
  ],
  "0.00020368914194764717": [
    "No",
    "0.00020368914194764717",
    "CF-causing",
    "43",
    "c.595C>T",
    "727C>T",
    "H199Y",
    "p.His199Tyr"
  ],
  "43": [
    "No",
    "0.00020368914194764717",
    "CF-causing",
    "43",
    "c.595C>T",
    "727C>T",
    "H199Y",
    "p.His199Tyr"
  ],
  "c.2900T>C": [
    "3032T>C",
    "p.Leu967Ser",
    "L967S",
    "0.00020368914194764717",
    "Varying clinical consequence",
    "43",
    "Non CF-causing",
    "Yes",
    "c.2900T>C"
  ],
  "3149C>A": [
    "3149C>A",
    "c.3017C>A",
    "No",
    "0.00020368914194764717",
    "CF-causing",
    "43",
    "p.Ala1006Glu",
    "A1006E"
  ],
  "c.3017C>A": [
    "3149C>A",
    "c.3017C>A",
    "No",
    "0.00020368914194764717",
    "CF-causing",
    "43",
    "p.Ala1006Glu",
    "A1006E"
  ],
  "p.Ala1006Glu": [
    "3149C>A",
    "c.3017C>A",
    "No",
    "0.00020368914194764717",
    "CF-causing",
    "43",
    "p.Ala1006Glu",
    "A1006E"
  ],
  "A1006E": [
    "3149C>A",
    "c.3017C>A",
    "No",
    "0.00020368914194764717",
    "CF-causing",
    "43",
    "p.Ala1006Glu",
    "A1006E"
  ],
  "3869C>T": [
    "3869C>T",
    "No",
    "p.Thr1246Ile",
    "c.3737C>T",
    "0.00020368914194764717",
    "Varying clinical consequence",
    "43",
    "T1246I"
  ],
  "p.Thr1246Ile": [
    "3869C>T",
    "No",
    "p.Thr1246Ile",
    "c.3737C>T",
    "0.00020368914194764717",
    "Varying clinical consequence",
    "43",
    "T1246I"
  ],
  "c.3737C>T": [
    "3869C>T",
    "No",
    "p.Thr1246Ile",
    "c.3737C>T",
    "0.00020368914194764717",
    "Varying clinical consequence",
    "43",
    "T1246I"
  ],
  "T1246I": [
    "3869C>T",
    "No",
    "p.Thr1246Ile",
    "c.3737C>T",
    "0.00020368914194764717",
    "Varying clinical consequence",
    "43",
    "T1246I"
  ],
  "c.595C>T": [
    "No",
    "0.00020368914194764717",
    "CF-causing",
    "43",
    "c.595C>T",
    "727C>T",
    "H199Y",
    "p.His199Tyr"
  ],
  "727C>T": [
    "No",
    "0.00020368914194764717",
    "CF-causing",
    "43",
    "c.595C>T",
    "727C>T",
    "H199Y",
    "p.His199Tyr"
  ],
  "H199Y": [
    "No",
    "0.00020368914194764717",
    "CF-causing",
    "43",
    "c.595C>T",
    "727C>T",
    "H199Y",
    "p.His199Tyr"
  ],
  "p.His199Tyr": [
    "No",
    "0.00020368914194764717",
    "CF-causing",
    "43",
    "c.595C>T",
    "727C>T",
    "H199Y",
    "p.His199Tyr"
  ],
  "42": [
    "No",
    "42",
    "F312del",
    "1067delTCT|[delta]F311",
    "Varying clinical consequence",
    "p.Phe312del",
    "0.000198952185158167",
    "c.935_937del"
  ],
  "F312del": [
    "No",
    "42",
    "F312del",
    "1067delTCT|[delta]F311",
    "Varying clinical consequence",
    "p.Phe312del",
    "0.000198952185158167",
    "c.935_937del"
  ],
  "1067delTCT|[delta]F311": [
    "No",
    "42",
    "F312del",
    "1067delTCT|[delta]F311",
    "Varying clinical consequence",
    "p.Phe312del",
    "0.000198952185158167",
    "c.935_937del"
  ],
  "p.Phe312del": [
    "No",
    "42",
    "F312del",
    "1067delTCT|[delta]F311",
    "Varying clinical consequence",
    "p.Phe312del",
    "0.000198952185158167",
    "c.935_937del"
  ],
  "0.000198952185158167": [
    "No",
    "42",
    "F312del",
    "1067delTCT|[delta]F311",
    "Varying clinical consequence",
    "p.Phe312del",
    "0.000198952185158167",
    "c.935_937del"
  ],
  "c.935_937del": [
    "No",
    "42",
    "F312del",
    "1067delTCT|[delta]F311",
    "Varying clinical consequence",
    "p.Phe312del",
    "0.000198952185158167",
    "c.935_937del"
  ],
  "G551S": [
    "G551S",
    "No",
    "c.1651G>A",
    "CF-causing",
    "p.Gly551Ser",
    "41",
    "0.00019421522836868683",
    "1783G>A"
  ],
  "c.1651G>A": [
    "G551S",
    "No",
    "c.1651G>A",
    "CF-causing",
    "p.Gly551Ser",
    "41",
    "0.00019421522836868683",
    "1783G>A"
  ],
  "p.Gly551Ser": [
    "G551S",
    "No",
    "c.1651G>A",
    "CF-causing",
    "p.Gly551Ser",
    "41",
    "0.00019421522836868683",
    "1783G>A"
  ],
  "41": [
    "No",
    "p.Gln98X",
    "424C>T",
    "CF-causing",
    "c.292C>T",
    "Q98X",
    "41",
    "0.00019421522836868683"
  ],
  "0.00019421522836868683": [
    "No",
    "p.Gln98X",
    "424C>T",
    "CF-causing",
    "c.292C>T",
    "Q98X",
    "41",
    "0.00019421522836868683"
  ],
  "1783G>A": [
    "G551S",
    "No",
    "c.1651G>A",
    "CF-causing",
    "p.Gly551Ser",
    "41",
    "0.00019421522836868683",
    "1783G>A"
  ],
  "p.Gln98X": [
    "No",
    "p.Gln98X",
    "424C>T",
    "CF-causing",
    "c.292C>T",
    "Q98X",
    "41",
    "0.00019421522836868683"
  ],
  "424C>T": [
    "No",
    "p.Gln98X",
    "424C>T",
    "CF-causing",
    "c.292C>T",
    "Q98X",
    "41",
    "0.00019421522836868683"
  ],
  "c.292C>T": [
    "No",
    "p.Gln98X",
    "424C>T",
    "CF-causing",
    "c.292C>T",
    "Q98X",
    "41",
    "0.00019421522836868683"
  ],
  "Q98X": [
    "No",
    "p.Gln98X",
    "424C>T",
    "CF-causing",
    "c.292C>T",
    "Q98X",
    "41",
    "0.00019421522836868683"
  ],
  "Y1032C": [
    "Y1032C",
    "No",
    "40",
    "Varying clinical consequence",
    "p.Tyr1032Cys",
    "c.3095A>G",
    "0.00018947827157920666",
    "3227A>G"
  ],
  "40": [
    "No",
    "p.Asn268IlefsX17",
    "c.803del",
    "40",
    "CF-causing",
    "935delA",
    "0.00018947827157920666"
  ],
  "p.Tyr1032Cys": [
    "Y1032C",
    "No",
    "40",
    "Varying clinical consequence",
    "p.Tyr1032Cys",
    "c.3095A>G",
    "0.00018947827157920666",
    "3227A>G"
  ],
  "c.3095A>G": [
    "Y1032C",
    "No",
    "40",
    "Varying clinical consequence",
    "p.Tyr1032Cys",
    "c.3095A>G",
    "0.00018947827157920666",
    "3227A>G"
  ],
  "0.00018947827157920666": [
    "No",
    "p.Asn268IlefsX17",
    "c.803del",
    "40",
    "CF-causing",
    "935delA",
    "0.00018947827157920666"
  ],
  "3227A>G": [
    "Y1032C",
    "No",
    "40",
    "Varying clinical consequence",
    "p.Tyr1032Cys",
    "c.3095A>G",
    "0.00018947827157920666",
    "3227A>G"
  ],
  "p.Glu1104X": [
    "p.Glu1104X",
    "No",
    "3442G>T",
    "c.3310G>T",
    "40",
    "CF-causing",
    "E1104X",
    "0.00018947827157920666"
  ],
  "3442G>T": [
    "p.Glu1104X",
    "No",
    "3442G>T",
    "c.3310G>T",
    "40",
    "CF-causing",
    "E1104X",
    "0.00018947827157920666"
  ],
  "c.3310G>T": [
    "p.Glu1104X",
    "No",
    "3442G>T",
    "c.3310G>T",
    "40",
    "CF-causing",
    "E1104X",
    "0.00018947827157920666"
  ],
  "E1104X": [
    "p.Glu1104X",
    "No",
    "3442G>T",
    "c.3310G>T",
    "40",
    "CF-causing",
    "E1104X",
    "0.00018947827157920666"
  ],
  "c.3764C>A": [
    "No",
    "c.3764C>A",
    "40",
    "CF-causing",
    "p.Ser1255X",
    "0.00018947827157920666",
    "3896C>A",
    "S1255X"
  ],
  "p.Ser1255X": [
    "No",
    "c.3764C>A",
    "40",
    "CF-causing",
    "p.Ser1255X",
    "0.00018947827157920666",
    "3896C>A",
    "S1255X"
  ],
  "3896C>A": [
    "No",
    "c.3764C>A",
    "40",
    "CF-causing",
    "p.Ser1255X",
    "0.00018947827157920666",
    "3896C>A",
    "S1255X"
  ],
  "S1255X": [
    "No",
    "c.3764C>A",
    "40",
    "CF-causing",
    "p.Ser1255X",
    "0.00018947827157920666",
    "3896C>A",
    "S1255X"
  ],
  "3600G->A": [
    "3600G->A",
    "No",
    "p.Leu1156Leu|L1156L",
    "40",
    "CF-causing",
    "c.3468G>A",
    "0.00018947827157920666",
    "p.Leu1156="
  ],
  "p.Leu1156Leu|L1156L": [
    "3600G->A",
    "No",
    "p.Leu1156Leu|L1156L",
    "40",
    "CF-causing",
    "c.3468G>A",
    "0.00018947827157920666",
    "p.Leu1156="
  ],
  "c.3468G>A": [
    "3600G->A",
    "No",
    "p.Leu1156Leu|L1156L",
    "40",
    "CF-causing",
    "c.3468G>A",
    "0.00018947827157920666",
    "p.Leu1156="
  ],
  "p.Leu1156=": [
    "3600G->A",
    "No",
    "p.Leu1156Leu|L1156L",
    "40",
    "CF-causing",
    "c.3468G>A",
    "0.00018947827157920666",
    "p.Leu1156="
  ],
  "3121-1G->A": [
    "p.?",
    "No",
    "40",
    "CF-causing",
    "3121-1G->A",
    "c.2989-1G>A",
    "0.00018947827157920666"
  ],
  "c.2989-1G>A": [
    "p.?",
    "No",
    "40",
    "CF-causing",
    "3121-1G->A",
    "c.2989-1G>A",
    "0.00018947827157920666"
  ],
  "p.Ile177MetfsX12": [
    "p.Ile177MetfsX12",
    "663delT",
    "No",
    "40",
    "CF-causing",
    "c.531del",
    "0.00018947827157920666"
  ],
  "663delT": [
    "p.Ile177MetfsX12",
    "663delT",
    "No",
    "40",
    "CF-causing",
    "c.531del",
    "0.00018947827157920666"
  ],
  "c.531del": [
    "p.Ile177MetfsX12",
    "663delT",
    "No",
    "40",
    "CF-causing",
    "c.531del",
    "0.00018947827157920666"
  ],
  "p.Ser1231ProfsX4": [
    "No",
    "40",
    "CF-causing",
    "p.Ser1231ProfsX4",
    "3821delT",
    "0.00018947827157920666",
    "c.3691del"
  ],
  "3821delT": [
    "No",
    "40",
    "CF-causing",
    "p.Ser1231ProfsX4",
    "3821delT",
    "0.00018947827157920666",
    "c.3691del"
  ],
  "c.3691del": [
    "No",
    "40",
    "CF-causing",
    "p.Ser1231ProfsX4",
    "3821delT",
    "0.00018947827157920666",
    "c.3691del"
  ],
  "p.Asn268IlefsX17": [
    "No",
    "p.Asn268IlefsX17",
    "c.803del",
    "40",
    "CF-causing",
    "935delA",
    "0.00018947827157920666"
  ],
  "c.803del": [
    "No",
    "p.Asn268IlefsX17",
    "c.803del",
    "40",
    "CF-causing",
    "935delA",
    "0.00018947827157920666"
  ],
  "935delA": [
    "No",
    "p.Asn268IlefsX17",
    "c.803del",
    "40",
    "CF-causing",
    "935delA",
    "0.00018947827157920666"
  ],
  "p.Gln98Arg": [
    "p.Gln98Arg",
    "No",
    "0.0001847413147897265",
    "c.293A>G",
    "425A>G",
    "39",
    "CF-causing",
    "Q98R"
  ],
  "0.0001847413147897265": [
    "1471delA",
    "No",
    "0.0001847413147897265",
    "39",
    "CF-causing",
    "p.Lys447ArgfsX2",
    "c.1340del"
  ],
  "c.293A>G": [
    "p.Gln98Arg",
    "No",
    "0.0001847413147897265",
    "c.293A>G",
    "425A>G",
    "39",
    "CF-causing",
    "Q98R"
  ],
  "425A>G": [
    "p.Gln98Arg",
    "No",
    "0.0001847413147897265",
    "c.293A>G",
    "425A>G",
    "39",
    "CF-causing",
    "Q98R"
  ],
  "39": [
    "1471delA",
    "No",
    "0.0001847413147897265",
    "39",
    "CF-causing",
    "p.Lys447ArgfsX2",
    "c.1340del"
  ],
  "Q98R": [
    "p.Gln98Arg",
    "No",
    "0.0001847413147897265",
    "c.293A>G",
    "425A>G",
    "39",
    "CF-causing",
    "Q98R"
  ],
  "I336fs": [
    "I336fs",
    "No",
    "1138insG",
    "0.0001847413147897265",
    "39",
    "p.Ile336SerfsX28",
    "CF-causing",
    "c.1006_1007insG"
  ],
  "1138insG": [
    "I336fs",
    "No",
    "1138insG",
    "0.0001847413147897265",
    "39",
    "p.Ile336SerfsX28",
    "CF-causing",
    "c.1006_1007insG"
  ],
  "p.Ile336SerfsX28": [
    "I336fs",
    "No",
    "1138insG",
    "0.0001847413147897265",
    "39",
    "p.Ile336SerfsX28",
    "CF-causing",
    "c.1006_1007insG"
  ],
  "c.1006_1007insG": [
    "I336fs",
    "No",
    "1138insG",
    "0.0001847413147897265",
    "39",
    "p.Ile336SerfsX28",
    "CF-causing",
    "c.1006_1007insG"
  ],
  "1471delA": [
    "1471delA",
    "No",
    "0.0001847413147897265",
    "39",
    "CF-causing",
    "p.Lys447ArgfsX2",
    "c.1340del"
  ],
  "p.Lys447ArgfsX2": [
    "1471delA",
    "No",
    "0.0001847413147897265",
    "39",
    "CF-causing",
    "p.Lys447ArgfsX2",
    "c.1340del"
  ],
  "c.1340del": [
    "1471delA",
    "No",
    "0.0001847413147897265",
    "39",
    "CF-causing",
    "p.Lys447ArgfsX2",
    "c.1340del"
  ],
  "38": [
    "c.1155_1156dup",
    "38",
    "No",
    "p.Asn386IlefsX3",
    "c.1152_1153dupAT",
    "0.00018000435800024633",
    "CF-causing",
    "1288insTA"
  ],
  "352C>T": [
    "38",
    "No",
    "352C>T",
    "p.Arg74Trp",
    "0.00018000435800024633",
    "Varying clinical consequence",
    "R74W",
    "c.220C>T"
  ],
  "p.Arg74Trp": [
    "38",
    "No",
    "352C>T",
    "p.Arg74Trp",
    "0.00018000435800024633",
    "Varying clinical consequence",
    "R74W",
    "c.220C>T"
  ],
  "0.00018000435800024633": [
    "c.1155_1156dup",
    "38",
    "No",
    "p.Asn386IlefsX3",
    "c.1152_1153dupAT",
    "0.00018000435800024633",
    "CF-causing",
    "1288insTA"
  ],
  "R74W": [
    "38",
    "No",
    "352C>T",
    "p.Arg74Trp",
    "0.00018000435800024633",
    "Varying clinical consequence",
    "R74W",
    "c.220C>T"
  ],
  "c.220C>T": [
    "38",
    "No",
    "352C>T",
    "p.Arg74Trp",
    "0.00018000435800024633",
    "Varying clinical consequence",
    "R74W",
    "c.220C>T"
  ],
  "c.377G>A": [
    "38",
    "c.377G>A",
    "No",
    "p.Gly126Asp",
    "509G>A",
    "0.00018000435800024633",
    "G126D",
    "CF-causing"
  ],
  "p.Gly126Asp": [
    "38",
    "c.377G>A",
    "No",
    "p.Gly126Asp",
    "509G>A",
    "0.00018000435800024633",
    "G126D",
    "CF-causing"
  ],
  "509G>A": [
    "38",
    "c.377G>A",
    "No",
    "p.Gly126Asp",
    "509G>A",
    "0.00018000435800024633",
    "G126D",
    "CF-causing"
  ],
  "G126D": [
    "38",
    "c.377G>A",
    "No",
    "p.Gly126Asp",
    "509G>A",
    "0.00018000435800024633",
    "G126D",
    "CF-causing"
  ],
  "c.1155_1156dup": [
    "c.1155_1156dup",
    "38",
    "No",
    "p.Asn386IlefsX3",
    "c.1152_1153dupAT",
    "0.00018000435800024633",
    "CF-causing",
    "1288insTA"
  ],
  "p.Asn386IlefsX3": [
    "c.1155_1156dup",
    "38",
    "No",
    "p.Asn386IlefsX3",
    "c.1152_1153dupAT",
    "0.00018000435800024633",
    "CF-causing",
    "1288insTA"
  ],
  "c.1152_1153dupAT": [
    "c.1155_1156dup",
    "38",
    "No",
    "p.Asn386IlefsX3",
    "c.1152_1153dupAT",
    "0.00018000435800024633",
    "CF-causing",
    "1288insTA"
  ],
  "1288insTA": [
    "c.1155_1156dup",
    "38",
    "No",
    "p.Asn386IlefsX3",
    "c.1152_1153dupAT",
    "0.00018000435800024633",
    "CF-causing",
    "1288insTA"
  ],
  "1548delG": [
    "1548delG",
    "No",
    "36",
    "0.000170530444421286",
    "CF-causing",
    "p.Gly473GlufsX54",
    "1550delG",
    "c.1418del"
  ],
  "36": [
    "c.3883del",
    "4015delA",
    "p.Ile1295PhefsX33",
    "No",
    "36",
    "0.000170530444421286",
    "CF-causing"
  ],
  "0.000170530444421286": [
    "c.3883del",
    "4015delA",
    "p.Ile1295PhefsX33",
    "No",
    "36",
    "0.000170530444421286",
    "CF-causing"
  ],
  "p.Gly473GlufsX54": [
    "1548delG",
    "No",
    "36",
    "0.000170530444421286",
    "CF-causing",
    "p.Gly473GlufsX54",
    "1550delG",
    "c.1418del"
  ],
  "1550delG": [
    "1548delG",
    "No",
    "36",
    "0.000170530444421286",
    "CF-causing",
    "p.Gly473GlufsX54",
    "1550delG",
    "c.1418del"
  ],
  "c.1418del": [
    "1548delG",
    "No",
    "36",
    "0.000170530444421286",
    "CF-causing",
    "p.Gly473GlufsX54",
    "1550delG",
    "c.1418del"
  ],
  "p.Leu227Arg": [
    "p.Leu227Arg",
    "812T>G",
    "36",
    "No",
    "c.680T>G",
    "0.000170530444421286",
    "CF-causing",
    "L227R"
  ],
  "812T>G": [
    "p.Leu227Arg",
    "812T>G",
    "36",
    "No",
    "c.680T>G",
    "0.000170530444421286",
    "CF-causing",
    "L227R"
  ],
  "c.680T>G": [
    "p.Leu227Arg",
    "812T>G",
    "36",
    "No",
    "c.680T>G",
    "0.000170530444421286",
    "CF-causing",
    "L227R"
  ],
  "L227R": [
    "p.Leu227Arg",
    "812T>G",
    "36",
    "No",
    "c.680T>G",
    "0.000170530444421286",
    "CF-causing",
    "L227R"
  ],
  "c.3883del": [
    "c.3883del",
    "4015delA",
    "p.Ile1295PhefsX33",
    "No",
    "36",
    "0.000170530444421286",
    "CF-causing"
  ],
  "4015delA": [
    "c.3883del",
    "4015delA",
    "p.Ile1295PhefsX33",
    "No",
    "36",
    "0.000170530444421286",
    "CF-causing"
  ],
  "p.Ile1295PhefsX33": [
    "c.3883del",
    "4015delA",
    "p.Ile1295PhefsX33",
    "No",
    "36",
    "0.000170530444421286",
    "CF-causing"
  ],
  "223C>T": [
    "No",
    "223C>T",
    "35",
    "c.91C>T",
    "Non CF-causing",
    "0.00016579348763180583",
    "R31C",
    "p.Arg31Cys"
  ],
  "35": [
    "No",
    "35",
    "CF-causing",
    "2585delT",
    "0.00016579348763180583",
    "c.2453del",
    "p.Leu818TrpfsX3"
  ],
  "c.91C>T": [
    "No",
    "223C>T",
    "35",
    "c.91C>T",
    "Non CF-causing",
    "0.00016579348763180583",
    "R31C",
    "p.Arg31Cys"
  ],
  "0.00016579348763180583": [
    "No",
    "35",
    "CF-causing",
    "2585delT",
    "0.00016579348763180583",
    "c.2453del",
    "p.Leu818TrpfsX3"
  ],
  "R31C": [
    "No",
    "223C>T",
    "35",
    "c.91C>T",
    "Non CF-causing",
    "0.00016579348763180583",
    "R31C",
    "p.Arg31Cys"
  ],
  "p.Arg31Cys": [
    "No",
    "223C>T",
    "35",
    "c.91C>T",
    "Non CF-causing",
    "0.00016579348763180583",
    "R31C",
    "p.Arg31Cys"
  ],
  "c.2374C>T": [
    "c.2374C>T",
    "No",
    "p.Arg792X",
    "35",
    "CF-causing",
    "R792X",
    "2506C>T",
    "0.00016579348763180583"
  ],
  "p.Arg792X": [
    "c.2374C>T",
    "No",
    "p.Arg792X",
    "35",
    "CF-causing",
    "R792X",
    "2506C>T",
    "0.00016579348763180583"
  ],
  "R792X": [
    "c.2374C>T",
    "No",
    "p.Arg792X",
    "35",
    "CF-causing",
    "R792X",
    "2506C>T",
    "0.00016579348763180583"
  ],
  "2506C>T": [
    "c.2374C>T",
    "No",
    "p.Arg792X",
    "35",
    "CF-causing",
    "R792X",
    "2506C>T",
    "0.00016579348763180583"
  ],
  "3893T>G": [
    "3893T>G",
    "No",
    "35",
    "CF-causing",
    "c.3761T>A|c.3761T>G",
    "L1254X",
    "0.00016579348763180583",
    "p.Leu1254X"
  ],
  "c.3761T>A|c.3761T>G": [
    "3893T>G",
    "No",
    "35",
    "CF-causing",
    "c.3761T>A|c.3761T>G",
    "L1254X",
    "0.00016579348763180583",
    "p.Leu1254X"
  ],
  "L1254X": [
    "3893T>G",
    "No",
    "35",
    "CF-causing",
    "c.3761T>A|c.3761T>G",
    "L1254X",
    "0.00016579348763180583",
    "p.Leu1254X"
  ],
  "p.Leu1254X": [
    "3893T>G",
    "No",
    "35",
    "CF-causing",
    "c.3761T>A|c.3761T>G",
    "L1254X",
    "0.00016579348763180583",
    "p.Leu1254X"
  ],
  "c.3659del": [
    "No",
    "c.3659del",
    "35",
    "CF-causing",
    "3791delC",
    "p.Thr1220LysfsX8",
    "0.00016579348763180583"
  ],
  "3791delC": [
    "No",
    "c.3659del",
    "35",
    "CF-causing",
    "3791delC",
    "p.Thr1220LysfsX8",
    "0.00016579348763180583"
  ],
  "p.Thr1220LysfsX8": [
    "No",
    "c.3659del",
    "35",
    "CF-causing",
    "3791delC",
    "p.Thr1220LysfsX8",
    "0.00016579348763180583"
  ],
  "2585delT": [
    "No",
    "35",
    "CF-causing",
    "2585delT",
    "0.00016579348763180583",
    "c.2453del",
    "p.Leu818TrpfsX3"
  ],
  "c.2453del": [
    "No",
    "35",
    "CF-causing",
    "2585delT",
    "0.00016579348763180583",
    "c.2453del",
    "p.Leu818TrpfsX3"
  ],
  "p.Leu818TrpfsX3": [
    "No",
    "35",
    "CF-causing",
    "2585delT",
    "0.00016579348763180583",
    "c.2453del",
    "p.Leu818TrpfsX3"
  ],
  "0.00016105653084232566": [
    "0.00016105653084232566",
    "No",
    "34",
    "c.2737_2738insG",
    "CF-causing",
    "p.Tyr913X",
    "2869insG"
  ],
  "V754M": [
    "0.00016105653084232566",
    "V754M",
    "No",
    "34",
    "2392G>A",
    "c.2260G>A",
    "p.Val754Met",
    "Non CF-causing"
  ],
  "34": [
    "0.00016105653084232566",
    "No",
    "34",
    "c.2737_2738insG",
    "CF-causing",
    "p.Tyr913X",
    "2869insG"
  ],
  "2392G>A": [
    "0.00016105653084232566",
    "V754M",
    "No",
    "34",
    "2392G>A",
    "c.2260G>A",
    "p.Val754Met",
    "Non CF-causing"
  ],
  "c.2260G>A": [
    "0.00016105653084232566",
    "V754M",
    "No",
    "34",
    "2392G>A",
    "c.2260G>A",
    "p.Val754Met",
    "Non CF-causing"
  ],
  "p.Val754Met": [
    "0.00016105653084232566",
    "V754M",
    "No",
    "34",
    "2392G>A",
    "c.2260G>A",
    "p.Val754Met",
    "Non CF-causing"
  ],
  "4558C>T": [
    "0.00016105653084232566",
    "No",
    "34",
    "Varying clinical consequence",
    "4558C>T",
    "Q1476X",
    "p.Gln1476X",
    "c.4426C>T"
  ],
  "Q1476X": [
    "0.00016105653084232566",
    "No",
    "34",
    "Varying clinical consequence",
    "4558C>T",
    "Q1476X",
    "p.Gln1476X",
    "c.4426C>T"
  ],
  "p.Gln1476X": [
    "0.00016105653084232566",
    "No",
    "34",
    "Varying clinical consequence",
    "4558C>T",
    "Q1476X",
    "p.Gln1476X",
    "c.4426C>T"
  ],
  "c.4426C>T": [
    "0.00016105653084232566",
    "No",
    "34",
    "Varying clinical consequence",
    "4558C>T",
    "Q1476X",
    "p.Gln1476X",
    "c.4426C>T"
  ],
  "c.3468+2_3468+3insT": [
    "0.00016105653084232566",
    "p.?",
    "No",
    "c.3468+2_3468+3insT",
    "34",
    "CF-causing",
    "c.3468+2dup",
    "3600+2insT"
  ],
  "c.3468+2dup": [
    "0.00016105653084232566",
    "p.?",
    "No",
    "c.3468+2_3468+3insT",
    "34",
    "CF-causing",
    "c.3468+2dup",
    "3600+2insT"
  ],
  "3600+2insT": [
    "0.00016105653084232566",
    "p.?",
    "No",
    "c.3468+2_3468+3insT",
    "34",
    "CF-causing",
    "c.3468+2dup",
    "3600+2insT"
  ],
  "c.1679+1G>C": [
    "c.1679+1G>C",
    "p.?",
    "0.00016105653084232566",
    "No",
    "1811+1G->C",
    "34",
    "CF-causing"
  ],
  "1811+1G->C": [
    "c.1679+1G>C",
    "p.?",
    "0.00016105653084232566",
    "No",
    "1811+1G->C",
    "34",
    "CF-causing"
  ],
  "4374+1G->T": [
    "0.00016105653084232566",
    "p.?",
    "No",
    "4374+1G->T",
    "34",
    "CF-causing",
    "c.4242+1G>T"
  ],
  "c.4242+1G>T": [
    "0.00016105653084232566",
    "p.?",
    "No",
    "4374+1G->T",
    "34",
    "CF-causing",
    "c.4242+1G>T"
  ],
  "c.2737_2738insG": [
    "0.00016105653084232566",
    "No",
    "34",
    "c.2737_2738insG",
    "CF-causing",
    "p.Tyr913X",
    "2869insG"
  ],
  "p.Tyr913X": [
    "No",
    "Y913X",
    "CF-causing",
    "p.Tyr913X",
    "26",
    "2871T>A",
    "c.2739T>A",
    "0.00012316087652648432"
  ],
  "2869insG": [
    "0.00016105653084232566",
    "No",
    "34",
    "c.2737_2738insG",
    "CF-causing",
    "p.Tyr913X",
    "2869insG"
  ],
  "p.Pro574His": [
    "p.Pro574His",
    "1853C>A",
    "No",
    "0.0001563195740528455",
    "CF-causing",
    "P574H",
    "33",
    "c.1721C>A"
  ],
  "1853C>A": [
    "p.Pro574His",
    "1853C>A",
    "No",
    "0.0001563195740528455",
    "CF-causing",
    "P574H",
    "33",
    "c.1721C>A"
  ],
  "0.0001563195740528455": [
    "c.1075_1079delCAAACinsAAAAA|p.Gln359_Thr360delinsLysLys|[1207C>A or1211C>A]",
    "No",
    "c.[1075C>A;1079C>A]",
    "0.0001563195740528455",
    "CF-causing",
    "33",
    "p.Gln359_Thr360delinsLysLys",
    "Q359K/T360K"
  ],
  "P574H": [
    "p.Pro574His",
    "1853C>A",
    "No",
    "0.0001563195740528455",
    "CF-causing",
    "P574H",
    "33",
    "c.1721C>A"
  ],
  "33": [
    "c.1075_1079delCAAACinsAAAAA|p.Gln359_Thr360delinsLysLys|[1207C>A or1211C>A]",
    "No",
    "c.[1075C>A;1079C>A]",
    "0.0001563195740528455",
    "CF-causing",
    "33",
    "p.Gln359_Thr360delinsLysLys",
    "Q359K/T360K"
  ],
  "c.1721C>A": [
    "p.Pro574His",
    "1853C>A",
    "No",
    "0.0001563195740528455",
    "CF-causing",
    "P574H",
    "33",
    "c.1721C>A"
  ],
  "p.Thr663ArgfsX8": [
    "No",
    "p.Thr663ArgfsX8",
    "0.0001563195740528455",
    "CF-causing",
    "33",
    "2116delCTAA",
    "2118del4",
    "c.1986_1989del"
  ],
  "2116delCTAA": [
    "No",
    "p.Thr663ArgfsX8",
    "0.0001563195740528455",
    "CF-causing",
    "33",
    "2116delCTAA",
    "2118del4",
    "c.1986_1989del"
  ],
  "2118del4": [
    "No",
    "p.Thr663ArgfsX8",
    "0.0001563195740528455",
    "CF-causing",
    "33",
    "2116delCTAA",
    "2118del4",
    "c.1986_1989del"
  ],
  "c.1986_1989del": [
    "No",
    "p.Thr663ArgfsX8",
    "0.0001563195740528455",
    "CF-causing",
    "33",
    "2116delCTAA",
    "2118del4",
    "c.1986_1989del"
  ],
  "p.Ser1159Phe": [
    "No",
    "p.Ser1159Phe",
    "0.0001563195740528455",
    "CF-causing",
    "S1159F",
    "33",
    "c.3476C>T",
    "3608C>T"
  ],
  "S1159F": [
    "No",
    "p.Ser1159Phe",
    "0.0001563195740528455",
    "CF-causing",
    "S1159F",
    "33",
    "c.3476C>T",
    "3608C>T"
  ],
  "c.3476C>T": [
    "No",
    "p.Ser1159Phe",
    "0.0001563195740528455",
    "CF-causing",
    "S1159F",
    "33",
    "c.3476C>T",
    "3608C>T"
  ],
  "3608C>T": [
    "No",
    "p.Ser1159Phe",
    "0.0001563195740528455",
    "CF-causing",
    "S1159F",
    "33",
    "c.3476C>T",
    "3608C>T"
  ],
  "709G>T": [
    "No",
    "709G>T",
    "c.577G>T",
    "0.0001563195740528455",
    "E193X",
    "CF-causing",
    "33",
    "p.Glu193X"
  ],
  "c.577G>T": [
    "No",
    "709G>T",
    "c.577G>T",
    "0.0001563195740528455",
    "E193X",
    "CF-causing",
    "33",
    "p.Glu193X"
  ],
  "E193X": [
    "No",
    "709G>T",
    "c.577G>T",
    "0.0001563195740528455",
    "E193X",
    "CF-causing",
    "33",
    "p.Glu193X"
  ],
  "p.Glu193X": [
    "No",
    "709G>T",
    "c.577G>T",
    "0.0001563195740528455",
    "E193X",
    "CF-causing",
    "33",
    "p.Glu193X"
  ],
  "c.1075_1079delCAAACinsAAAAA|p.Gln359_Thr360delinsLysLys|[1207C>A or1211C>A]": [
    "c.1075_1079delCAAACinsAAAAA|p.Gln359_Thr360delinsLysLys|[1207C>A or1211C>A]",
    "No",
    "c.[1075C>A;1079C>A]",
    "0.0001563195740528455",
    "CF-causing",
    "33",
    "p.Gln359_Thr360delinsLysLys",
    "Q359K/T360K"
  ],
  "c.[1075C>A;1079C>A]": [
    "c.1075_1079delCAAACinsAAAAA|p.Gln359_Thr360delinsLysLys|[1207C>A or1211C>A]",
    "No",
    "c.[1075C>A;1079C>A]",
    "0.0001563195740528455",
    "CF-causing",
    "33",
    "p.Gln359_Thr360delinsLysLys",
    "Q359K/T360K"
  ],
  "p.Gln359_Thr360delinsLysLys": [
    "c.1075_1079delCAAACinsAAAAA|p.Gln359_Thr360delinsLysLys|[1207C>A or1211C>A]",
    "No",
    "c.[1075C>A;1079C>A]",
    "0.0001563195740528455",
    "CF-causing",
    "33",
    "p.Gln359_Thr360delinsLysLys",
    "Q359K/T360K"
  ],
  "Q359K/T360K": [
    "c.1075_1079delCAAACinsAAAAA|p.Gln359_Thr360delinsLysLys|[1207C>A or1211C>A]",
    "No",
    "c.[1075C>A;1079C>A]",
    "0.0001563195740528455",
    "CF-causing",
    "33",
    "p.Gln359_Thr360delinsLysLys",
    "Q359K/T360K"
  ],
  "1133G>T": [
    "1133G>T",
    "No",
    "R334L",
    "c.1001G>T",
    "32",
    "p.Arg334Leu",
    "0.00015158261726336533",
    "CF-causing"
  ],
  "R334L": [
    "1133G>T",
    "No",
    "R334L",
    "c.1001G>T",
    "32",
    "p.Arg334Leu",
    "0.00015158261726336533",
    "CF-causing"
  ],
  "c.1001G>T": [
    "1133G>T",
    "No",
    "R334L",
    "c.1001G>T",
    "32",
    "p.Arg334Leu",
    "0.00015158261726336533",
    "CF-causing"
  ],
  "32": [
    "p.?",
    "No",
    "c.3873+1G>A",
    "0.00015158261726336533",
    "32",
    "CF-causing",
    "4005+1G->A"
  ],
  "p.Arg334Leu": [
    "1133G>T",
    "No",
    "R334L",
    "c.1001G>T",
    "32",
    "p.Arg334Leu",
    "0.00015158261726336533",
    "CF-causing"
  ],
  "0.00015158261726336533": [
    "p.?",
    "No",
    "c.3873+1G>A",
    "0.00015158261726336533",
    "32",
    "CF-causing",
    "4005+1G->A"
  ],
  "c.4197_4198del": [
    "No",
    "c.4197_4198del",
    "4326delTC",
    "32",
    "0.00015158261726336533",
    "CF-causing",
    "p.Cys1400X",
    "4329delCT|c.4196_4197delTC"
  ],
  "4326delTC": [
    "No",
    "c.4197_4198del",
    "4326delTC",
    "32",
    "0.00015158261726336533",
    "CF-causing",
    "p.Cys1400X",
    "4329delCT|c.4196_4197delTC"
  ],
  "p.Cys1400X": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "4332T>A",
    "CF-causing",
    "c.4200T>A",
    "p.Cys1400X",
    "1",
    "C1400X"
  ],
  "4329delCT|c.4196_4197delTC": [
    "No",
    "c.4197_4198del",
    "4326delTC",
    "32",
    "0.00015158261726336533",
    "CF-causing",
    "p.Cys1400X",
    "4329delCT|c.4196_4197delTC"
  ],
  "deletion of exons 4 through 10 (legacy numbering)|deletion of exons 4 through 11 (current numbering)": [
    "deletion of exons 4 through 10 (legacy numbering)|deletion of exons 4 through 11 (current numbering)",
    "p.?",
    "No",
    "CFTRdele4-10",
    "32",
    "0.00015158261726336533",
    "CF-causing",
    "c.(273+1_274-1)_(1584+1_1585-1)del"
  ],
  "CFTRdele4-10": [
    "deletion of exons 4 through 10 (legacy numbering)|deletion of exons 4 through 11 (current numbering)",
    "p.?",
    "No",
    "CFTRdele4-10",
    "32",
    "0.00015158261726336533",
    "CF-causing",
    "c.(273+1_274-1)_(1584+1_1585-1)del"
  ],
  "c.(273+1_274-1)_(1584+1_1585-1)del": [
    "deletion of exons 4 through 10 (legacy numbering)|deletion of exons 4 through 11 (current numbering)",
    "p.?",
    "No",
    "CFTRdele4-10",
    "32",
    "0.00015158261726336533",
    "CF-causing",
    "c.(273+1_274-1)_(1584+1_1585-1)del"
  ],
  "c.3873+1G>A": [
    "p.?",
    "No",
    "c.3873+1G>A",
    "0.00015158261726336533",
    "32",
    "CF-causing",
    "4005+1G->A"
  ],
  "4005+1G->A": [
    "p.?",
    "No",
    "c.3873+1G>A",
    "0.00015158261726336533",
    "32",
    "CF-causing",
    "4005+1G->A"
  ],
  "31": [
    "31",
    "0.00014684566047388516",
    "No",
    "CF-causing",
    "p.Asn415X",
    "1367del5",
    "c.1243_1247del"
  ],
  "4040delA": [
    "31",
    "4040delA",
    "0.00014684566047388516",
    "No",
    "p.Asn1303ThrfsX25",
    "CF-causing",
    "c.3908del",
    "4035delA"
  ],
  "0.00014684566047388516": [
    "31",
    "0.00014684566047388516",
    "No",
    "CF-causing",
    "p.Asn415X",
    "1367del5",
    "c.1243_1247del"
  ],
  "p.Asn1303ThrfsX25": [
    "31",
    "4040delA",
    "0.00014684566047388516",
    "No",
    "p.Asn1303ThrfsX25",
    "CF-causing",
    "c.3908del",
    "4035delA"
  ],
  "c.3908del": [
    "31",
    "4040delA",
    "0.00014684566047388516",
    "No",
    "p.Asn1303ThrfsX25",
    "CF-causing",
    "c.3908del",
    "4035delA"
  ],
  "4035delA": [
    "31",
    "4040delA",
    "0.00014684566047388516",
    "No",
    "p.Asn1303ThrfsX25",
    "CF-causing",
    "c.3908del",
    "4035delA"
  ],
  "1341+1G->A": [
    "31",
    "0.00014684566047388516",
    "p.?",
    "No",
    "CF-causing",
    "1341+1G->A",
    "c.1209+1G>A"
  ],
  "c.1209+1G>A": [
    "31",
    "0.00014684566047388516",
    "p.?",
    "No",
    "CF-causing",
    "1341+1G->A",
    "c.1209+1G>A"
  ],
  "p.Cys343X": [
    "31",
    "0.00014684566047388516",
    "No",
    "p.Cys343X",
    "1161delC",
    "c.1029del",
    "CF-causing"
  ],
  "1161delC": [
    "31",
    "0.00014684566047388516",
    "No",
    "p.Cys343X",
    "1161delC",
    "c.1029del",
    "CF-causing"
  ],
  "c.1029del": [
    "31",
    "0.00014684566047388516",
    "No",
    "p.Cys343X",
    "1161delC",
    "c.1029del",
    "CF-causing"
  ],
  "p.Asn415X": [
    "31",
    "0.00014684566047388516",
    "No",
    "CF-causing",
    "p.Asn415X",
    "1367del5",
    "c.1243_1247del"
  ],
  "1367del5": [
    "31",
    "0.00014684566047388516",
    "No",
    "CF-causing",
    "p.Asn415X",
    "1367del5",
    "c.1243_1247del"
  ],
  "c.1243_1247del": [
    "31",
    "0.00014684566047388516",
    "No",
    "CF-causing",
    "p.Asn415X",
    "1367del5",
    "c.1243_1247del"
  ],
  "c.2735C>A": [
    "c.2735C>A",
    "0.000142108703684405",
    "No",
    "p.Ser912X",
    "2867C>A",
    "30",
    "CF-causing",
    "S912X"
  ],
  "0.000142108703684405": [
    "3849G->A",
    "0.000142108703684405",
    "No",
    "R1239R",
    "p.Arg1239=",
    "30",
    "CF-causing",
    "c.3717G>A"
  ],
  "p.Ser912X": [
    "c.2735C>A",
    "0.000142108703684405",
    "No",
    "p.Ser912X",
    "2867C>A",
    "30",
    "CF-causing",
    "S912X"
  ],
  "2867C>A": [
    "c.2735C>A",
    "0.000142108703684405",
    "No",
    "p.Ser912X",
    "2867C>A",
    "30",
    "CF-causing",
    "S912X"
  ],
  "30": [
    "3849G->A",
    "0.000142108703684405",
    "No",
    "R1239R",
    "p.Arg1239=",
    "30",
    "CF-causing",
    "c.3717G>A"
  ],
  "S912X": [
    "c.2735C>A",
    "0.000142108703684405",
    "No",
    "p.Ser912X",
    "2867C>A",
    "30",
    "CF-causing",
    "S912X"
  ],
  "p.Gly970Asp": [
    "0.000142108703684405",
    "No",
    "p.Gly970Asp",
    "30",
    "CF-causing",
    "3041G>A",
    "G970D",
    "c.2909G>A"
  ],
  "3041G>A": [
    "0.000142108703684405",
    "No",
    "p.Gly970Asp",
    "30",
    "CF-causing",
    "3041G>A",
    "G970D",
    "c.2909G>A"
  ],
  "G970D": [
    "0.000142108703684405",
    "No",
    "p.Gly970Asp",
    "30",
    "CF-causing",
    "3041G>A",
    "G970D",
    "c.2909G>A"
  ],
  "c.2909G>A": [
    "0.000142108703684405",
    "No",
    "p.Gly970Asp",
    "30",
    "CF-causing",
    "3041G>A",
    "G970D",
    "c.2909G>A"
  ],
  "c.3929G>A|c.3930G>A": [
    "c.3929G>A|c.3930G>A",
    "0.000142108703684405",
    "No",
    "30",
    "CF-causing",
    "p.Trp1310X",
    "4061G>A",
    "W1310X"
  ],
  "p.Trp1310X": [
    "c.3929G>A|c.3930G>A",
    "0.000142108703684405",
    "No",
    "30",
    "CF-causing",
    "p.Trp1310X",
    "4061G>A",
    "W1310X"
  ],
  "4061G>A": [
    "c.3929G>A|c.3930G>A",
    "0.000142108703684405",
    "No",
    "30",
    "CF-causing",
    "p.Trp1310X",
    "4061G>A",
    "W1310X"
  ],
  "W1310X": [
    "c.3929G>A|c.3930G>A",
    "0.000142108703684405",
    "No",
    "30",
    "CF-causing",
    "p.Trp1310X",
    "4061G>A",
    "W1310X"
  ],
  "p.Leu165Ser": [
    "0.000142108703684405",
    "No",
    "p.Leu165Ser",
    "L165S",
    "626T>C",
    "30",
    "CF-causing",
    "c.494T>C"
  ],
  "L165S": [
    "0.000142108703684405",
    "No",
    "p.Leu165Ser",
    "L165S",
    "626T>C",
    "30",
    "CF-causing",
    "c.494T>C"
  ],
  "626T>C": [
    "0.000142108703684405",
    "No",
    "p.Leu165Ser",
    "L165S",
    "626T>C",
    "30",
    "CF-causing",
    "c.494T>C"
  ],
  "c.494T>C": [
    "0.000142108703684405",
    "No",
    "p.Leu165Ser",
    "L165S",
    "626T>C",
    "30",
    "CF-causing",
    "c.494T>C"
  ],
  "960C>A": [
    "0.000142108703684405",
    "No",
    "960C>A",
    "30",
    "p.Cys276X",
    "c.828C>A",
    "CF-causing",
    "C276X"
  ],
  "p.Cys276X": [
    "0.000142108703684405",
    "No",
    "960C>A",
    "30",
    "p.Cys276X",
    "c.828C>A",
    "CF-causing",
    "C276X"
  ],
  "c.828C>A": [
    "0.000142108703684405",
    "No",
    "960C>A",
    "30",
    "p.Cys276X",
    "c.828C>A",
    "CF-causing",
    "C276X"
  ],
  "C276X": [
    "0.000142108703684405",
    "No",
    "960C>A",
    "30",
    "p.Cys276X",
    "c.828C>A",
    "CF-causing",
    "C276X"
  ],
  "c.(2619+1_2620-1)_(3367+1_3368-1)del": [
    "p.?",
    "0.000142108703684405",
    "No",
    "c.(2619+1_2620-1)_(3367+1_3368-1)del",
    "CFTRdele14b-17b",
    "30",
    "CF-causing",
    "deletion of exons 14b, 15, 16, 17a, and 17b (legacy numbering)|deletion of exons 16, 17, 18, 19, and 20 (current numbering)"
  ],
  "CFTRdele14b-17b": [
    "p.?",
    "0.000142108703684405",
    "No",
    "c.(2619+1_2620-1)_(3367+1_3368-1)del",
    "CFTRdele14b-17b",
    "30",
    "CF-causing",
    "deletion of exons 14b, 15, 16, 17a, and 17b (legacy numbering)|deletion of exons 16, 17, 18, 19, and 20 (current numbering)"
  ],
  "deletion of exons 14b, 15, 16, 17a, and 17b (legacy numbering)|deletion of exons 16, 17, 18, 19, and 20 (current numbering)": [
    "p.?",
    "0.000142108703684405",
    "No",
    "c.(2619+1_2620-1)_(3367+1_3368-1)del",
    "CFTRdele14b-17b",
    "30",
    "CF-causing",
    "deletion of exons 14b, 15, 16, 17a, and 17b (legacy numbering)|deletion of exons 16, 17, 18, 19, and 20 (current numbering)"
  ],
  "3849G->A": [
    "3849G->A",
    "0.000142108703684405",
    "No",
    "R1239R",
    "p.Arg1239=",
    "30",
    "CF-causing",
    "c.3717G>A"
  ],
  "R1239R": [
    "3849G->A",
    "0.000142108703684405",
    "No",
    "R1239R",
    "p.Arg1239=",
    "30",
    "CF-causing",
    "c.3717G>A"
  ],
  "p.Arg1239=": [
    "3849G->A",
    "0.000142108703684405",
    "No",
    "R1239R",
    "p.Arg1239=",
    "30",
    "CF-causing",
    "c.3717G>A"
  ],
  "c.3717G>A": [
    "3849G->A",
    "0.000142108703684405",
    "No",
    "R1239R",
    "p.Arg1239=",
    "30",
    "CF-causing",
    "c.3717G>A"
  ],
  "0.00013737174689492482": [
    "c.2998del",
    "No",
    "0.00013737174689492482",
    "CF-causing",
    "29",
    "3130delA",
    "p.Ile1000LeufsX2"
  ],
  "W57G": [
    "No",
    "0.00013737174689492482",
    "W57G",
    "CF-causing",
    "301T>G",
    "29",
    "c.169T>G",
    "p.Trp57Gly"
  ],
  "301T>G": [
    "No",
    "0.00013737174689492482",
    "W57G",
    "CF-causing",
    "301T>G",
    "29",
    "c.169T>G",
    "p.Trp57Gly"
  ],
  "29": [
    "c.2998del",
    "No",
    "0.00013737174689492482",
    "CF-causing",
    "29",
    "3130delA",
    "p.Ile1000LeufsX2"
  ],
  "c.169T>G": [
    "No",
    "0.00013737174689492482",
    "W57G",
    "CF-causing",
    "301T>G",
    "29",
    "c.169T>G",
    "p.Trp57Gly"
  ],
  "p.Trp57Gly": [
    "No",
    "0.00013737174689492482",
    "W57G",
    "CF-causing",
    "301T>G",
    "29",
    "c.169T>G",
    "p.Trp57Gly"
  ],
  "993delCTTAA|c.859_863delAACTT": [
    "993delCTTAA|c.859_863delAACTT",
    "No",
    "0.00013737174689492482",
    "c.861_865del",
    "CF-causing",
    "29",
    "p.Asn287LysfsX19",
    "991del5"
  ],
  "c.861_865del": [
    "993delCTTAA|c.859_863delAACTT",
    "No",
    "0.00013737174689492482",
    "c.861_865del",
    "CF-causing",
    "29",
    "p.Asn287LysfsX19",
    "991del5"
  ],
  "p.Asn287LysfsX19": [
    "993delCTTAA|c.859_863delAACTT",
    "No",
    "0.00013737174689492482",
    "c.861_865del",
    "CF-causing",
    "29",
    "p.Asn287LysfsX19",
    "991del5"
  ],
  "991del5": [
    "993delCTTAA|c.859_863delAACTT",
    "No",
    "0.00013737174689492482",
    "c.861_865del",
    "CF-causing",
    "29",
    "p.Asn287LysfsX19",
    "991del5"
  ],
  "182delT": [
    "No",
    "0.00013737174689492482",
    "182delT",
    "CF-causing",
    "c.50del",
    "29",
    "p.Phe17SerfsX8"
  ],
  "c.50del": [
    "No",
    "0.00013737174689492482",
    "182delT",
    "CF-causing",
    "c.50del",
    "29",
    "p.Phe17SerfsX8"
  ],
  "p.Phe17SerfsX8": [
    "No",
    "0.00013737174689492482",
    "182delT",
    "CF-causing",
    "c.50del",
    "29",
    "p.Phe17SerfsX8"
  ],
  "c.2998del": [
    "c.2998del",
    "No",
    "0.00013737174689492482",
    "CF-causing",
    "29",
    "3130delA",
    "p.Ile1000LeufsX2"
  ],
  "3130delA": [
    "c.2998del",
    "No",
    "0.00013737174689492482",
    "CF-causing",
    "29",
    "3130delA",
    "p.Ile1000LeufsX2"
  ],
  "p.Ile1000LeufsX2": [
    "c.2998del",
    "No",
    "0.00013737174689492482",
    "CF-causing",
    "29",
    "3130delA",
    "p.Ile1000LeufsX2"
  ],
  "c.988G>T": [
    "c.988G>T",
    "No",
    "1120G>T",
    "G330X",
    "0.00013263479010544466",
    "CF-causing",
    "p.Gly330X",
    "28"
  ],
  "1120G>T": [
    "c.988G>T",
    "No",
    "1120G>T",
    "G330X",
    "0.00013263479010544466",
    "CF-causing",
    "p.Gly330X",
    "28"
  ],
  "G330X": [
    "c.988G>T",
    "No",
    "1120G>T",
    "G330X",
    "0.00013263479010544466",
    "CF-causing",
    "p.Gly330X",
    "28"
  ],
  "0.00013263479010544466": [
    "No",
    "p.Gln637HisfsX26",
    "0.00013263479010544466",
    "CF-causing",
    "c.1911del",
    "28",
    "2043delG"
  ],
  "p.Gly330X": [
    "c.988G>T",
    "No",
    "1120G>T",
    "G330X",
    "0.00013263479010544466",
    "CF-causing",
    "p.Gly330X",
    "28"
  ],
  "28": [
    "No",
    "p.Gln637HisfsX26",
    "0.00013263479010544466",
    "CF-causing",
    "c.1911del",
    "28",
    "2043delG"
  ],
  "p.Val562Ile": [
    "p.Val562Ile",
    "No",
    "c.1684G>A",
    "V562I",
    "0.00013263479010544466",
    "Non CF-causing",
    "1816G>A",
    "28"
  ],
  "c.1684G>A": [
    "p.Val562Ile",
    "No",
    "c.1684G>A",
    "V562I",
    "0.00013263479010544466",
    "Non CF-causing",
    "1816G>A",
    "28"
  ],
  "V562I": [
    "p.Val562Ile",
    "No",
    "c.1684G>A",
    "V562I",
    "0.00013263479010544466",
    "Non CF-causing",
    "1816G>A",
    "28"
  ],
  "1816G>A": [
    "p.Val562Ile",
    "No",
    "c.1684G>A",
    "V562I",
    "0.00013263479010544466",
    "Non CF-causing",
    "1816G>A",
    "28"
  ],
  "3062C>T": [
    "3062C>T",
    "No",
    "S977F",
    "Varying clinical consequence",
    "0.00013263479010544466",
    "p.Ser977Phe",
    "28",
    "c.2930C>T"
  ],
  "S977F": [
    "3062C>T",
    "No",
    "S977F",
    "Varying clinical consequence",
    "0.00013263479010544466",
    "p.Ser977Phe",
    "28",
    "c.2930C>T"
  ],
  "p.Ser977Phe": [
    "3062C>T",
    "No",
    "S977F",
    "Varying clinical consequence",
    "0.00013263479010544466",
    "p.Ser977Phe",
    "28",
    "c.2930C>T"
  ],
  "c.2930C>T": [
    "3062C>T",
    "No",
    "S977F",
    "Varying clinical consequence",
    "0.00013263479010544466",
    "p.Ser977Phe",
    "28",
    "c.2930C>T"
  ],
  "3292C>G": [
    "No",
    "0.00013263479010544466",
    "CF-causing",
    "3292C>G",
    "H1054D",
    "c.3160C>G",
    "p.His1054Asp",
    "28"
  ],
  "H1054D": [
    "No",
    "0.00013263479010544466",
    "CF-causing",
    "3292C>G",
    "H1054D",
    "c.3160C>G",
    "p.His1054Asp",
    "28"
  ],
  "c.3160C>G": [
    "No",
    "0.00013263479010544466",
    "CF-causing",
    "3292C>G",
    "H1054D",
    "c.3160C>G",
    "p.His1054Asp",
    "28"
  ],
  "p.His1054Asp": [
    "No",
    "0.00013263479010544466",
    "CF-causing",
    "3292C>G",
    "H1054D",
    "c.3160C>G",
    "p.His1054Asp",
    "28"
  ],
  "c.4111G>T": [
    "c.4111G>T",
    "No",
    "E1371X",
    "0.00013263479010544466",
    "CF-causing",
    "4243G>T",
    "28",
    "p.Glu1371X"
  ],
  "E1371X": [
    "c.4111G>T",
    "No",
    "E1371X",
    "0.00013263479010544466",
    "CF-causing",
    "4243G>T",
    "28",
    "p.Glu1371X"
  ],
  "4243G>T": [
    "c.4111G>T",
    "No",
    "E1371X",
    "0.00013263479010544466",
    "CF-causing",
    "4243G>T",
    "28",
    "p.Glu1371X"
  ],
  "p.Glu1371X": [
    "c.4111G>T",
    "No",
    "E1371X",
    "0.00013263479010544466",
    "CF-causing",
    "4243G>T",
    "28",
    "p.Glu1371X"
  ],
  "852del22": [
    "p.?",
    "No",
    "852del22",
    "0.00013263479010544466",
    "CF-causing",
    "28",
    "c.720_741delAGGGAGAATGATGATGAAGTAC",
    "c.723_743+1del"
  ],
  "c.720_741delAGGGAGAATGATGATGAAGTAC": [
    "p.?",
    "No",
    "852del22",
    "0.00013263479010544466",
    "CF-causing",
    "28",
    "c.720_741delAGGGAGAATGATGATGAAGTAC",
    "c.723_743+1del"
  ],
  "c.723_743+1del": [
    "p.?",
    "No",
    "852del22",
    "0.00013263479010544466",
    "CF-causing",
    "28",
    "c.720_741delAGGGAGAATGATGATGAAGTAC",
    "c.723_743+1del"
  ],
  "p.Gln637HisfsX26": [
    "No",
    "p.Gln637HisfsX26",
    "0.00013263479010544466",
    "CF-causing",
    "c.1911del",
    "28",
    "2043delG"
  ],
  "c.1911del": [
    "No",
    "p.Gln637HisfsX26",
    "0.00013263479010544466",
    "CF-causing",
    "c.1911del",
    "28",
    "2043delG"
  ],
  "2043delG": [
    "No",
    "p.Gln637HisfsX26",
    "0.00013263479010544466",
    "CF-causing",
    "c.1911del",
    "28",
    "2043delG"
  ],
  "0.0001278978333159645": [
    "0.0001278978333159645",
    "p.?",
    "27",
    "No",
    "CF-causing",
    "1898+1G->C",
    "c.1766+1G>C"
  ],
  "27": [
    "0.0001278978333159645",
    "p.?",
    "27",
    "No",
    "CF-causing",
    "1898+1G->C",
    "c.1766+1G>C"
  ],
  "W401X": [
    "0.0001278978333159645",
    "27",
    "No",
    "W401X",
    "p.Trp401X",
    "CF-causing",
    "c.1202G>A|c.1203G>A",
    "W401X(TAG)|W401X(TGA)|1334G>A|1335G>A"
  ],
  "p.Trp401X": [
    "0.0001278978333159645",
    "27",
    "No",
    "W401X",
    "p.Trp401X",
    "CF-causing",
    "c.1202G>A|c.1203G>A",
    "W401X(TAG)|W401X(TGA)|1334G>A|1335G>A"
  ],
  "c.1202G>A|c.1203G>A": [
    "0.0001278978333159645",
    "27",
    "No",
    "W401X",
    "p.Trp401X",
    "CF-causing",
    "c.1202G>A|c.1203G>A",
    "W401X(TAG)|W401X(TGA)|1334G>A|1335G>A"
  ],
  "W401X(TAG)|W401X(TGA)|1334G>A|1335G>A": [
    "0.0001278978333159645",
    "27",
    "No",
    "W401X",
    "p.Trp401X",
    "CF-causing",
    "c.1202G>A|c.1203G>A",
    "W401X(TAG)|W401X(TGA)|1334G>A|1335G>A"
  ],
  "1898+1G->C": [
    "0.0001278978333159645",
    "p.?",
    "27",
    "No",
    "CF-causing",
    "1898+1G->C",
    "c.1766+1G>C"
  ],
  "c.1766+1G>C": [
    "0.0001278978333159645",
    "p.?",
    "27",
    "No",
    "CF-causing",
    "1898+1G->C",
    "c.1766+1G>C"
  ],
  "S434X": [
    "S434X",
    "No",
    "c.1301C>A|c.1301C>G",
    "CF-causing",
    "26",
    "p.Ser434X",
    "0.00012316087652648432",
    "1433C>G|1433C>A"
  ],
  "c.1301C>A|c.1301C>G": [
    "S434X",
    "No",
    "c.1301C>A|c.1301C>G",
    "CF-causing",
    "26",
    "p.Ser434X",
    "0.00012316087652648432",
    "1433C>G|1433C>A"
  ],
  "26": [
    "No",
    "CF-causing",
    "26",
    "3944delGT",
    "c.3816_3817del",
    "p.Ser1273LeufsX28",
    "0.00012316087652648432"
  ],
  "p.Ser434X": [
    "S434X",
    "No",
    "c.1301C>A|c.1301C>G",
    "CF-causing",
    "26",
    "p.Ser434X",
    "0.00012316087652648432",
    "1433C>G|1433C>A"
  ],
  "0.00012316087652648432": [
    "No",
    "CF-causing",
    "26",
    "3944delGT",
    "c.3816_3817del",
    "p.Ser1273LeufsX28",
    "0.00012316087652648432"
  ],
  "1433C>G|1433C>A": [
    "S434X",
    "No",
    "c.1301C>A|c.1301C>G",
    "CF-causing",
    "26",
    "p.Ser434X",
    "0.00012316087652648432",
    "1433C>G|1433C>A"
  ],
  "Y913X": [
    "No",
    "Y913X",
    "CF-causing",
    "p.Tyr913X",
    "26",
    "2871T>A",
    "c.2739T>A",
    "0.00012316087652648432"
  ],
  "2871T>A": [
    "No",
    "Y913X",
    "CF-causing",
    "p.Tyr913X",
    "26",
    "2871T>A",
    "c.2739T>A",
    "0.00012316087652648432"
  ],
  "c.2739T>A": [
    "No",
    "Y913X",
    "CF-causing",
    "p.Tyr913X",
    "26",
    "2871T>A",
    "c.2739T>A",
    "0.00012316087652648432"
  ],
  "p.Arg59LysfsX10": [
    "p.Arg59LysfsX10",
    "306insA",
    "No",
    "CF-causing",
    "26",
    "c.175dup",
    "307insA|c.174_175insA",
    "0.00012316087652648432"
  ],
  "306insA": [
    "p.Arg59LysfsX10",
    "306insA",
    "No",
    "CF-causing",
    "26",
    "c.175dup",
    "307insA|c.174_175insA",
    "0.00012316087652648432"
  ],
  "c.175dup": [
    "p.Arg59LysfsX10",
    "306insA",
    "No",
    "CF-causing",
    "26",
    "c.175dup",
    "307insA|c.174_175insA",
    "0.00012316087652648432"
  ],
  "307insA|c.174_175insA": [
    "p.Arg59LysfsX10",
    "306insA",
    "No",
    "CF-causing",
    "26",
    "c.175dup",
    "307insA|c.174_175insA",
    "0.00012316087652648432"
  ],
  "c.330C>A": [
    "c.330C>A",
    "462C>A",
    "No",
    "Varying clinical consequence",
    "26",
    "0.00012316087652648432",
    "p.Asp110Glu",
    "D110E"
  ],
  "462C>A": [
    "c.330C>A",
    "462C>A",
    "No",
    "Varying clinical consequence",
    "26",
    "0.00012316087652648432",
    "p.Asp110Glu",
    "D110E"
  ],
  "p.Asp110Glu": [
    "c.330C>A",
    "462C>A",
    "No",
    "Varying clinical consequence",
    "26",
    "0.00012316087652648432",
    "p.Asp110Glu",
    "D110E"
  ],
  "D110E": [
    "c.330C>A",
    "462C>A",
    "No",
    "Varying clinical consequence",
    "26",
    "0.00012316087652648432",
    "p.Asp110Glu",
    "D110E"
  ],
  "3500-2A->G": [
    "p.?",
    "No",
    "3500-2A->G",
    "CF-causing",
    "26",
    "c.3368-2A>G",
    "0.00012316087652648432"
  ],
  "c.3368-2A>G": [
    "p.?",
    "No",
    "3500-2A->G",
    "CF-causing",
    "26",
    "c.3368-2A>G",
    "0.00012316087652648432"
  ],
  "3944delGT": [
    "No",
    "CF-causing",
    "26",
    "3944delGT",
    "c.3816_3817del",
    "p.Ser1273LeufsX28",
    "0.00012316087652648432"
  ],
  "c.3816_3817del": [
    "No",
    "CF-causing",
    "26",
    "3944delGT",
    "c.3816_3817del",
    "p.Ser1273LeufsX28",
    "0.00012316087652648432"
  ],
  "p.Ser1273LeufsX28": [
    "No",
    "CF-causing",
    "26",
    "3944delGT",
    "c.3816_3817del",
    "p.Ser1273LeufsX28",
    "0.00012316087652648432"
  ],
  "I502T": [
    "I502T",
    "No",
    "1637T>C",
    "c.1505T>C",
    "p.Ile502Thr",
    "0.00011842391973700416",
    "CF-causing",
    "25"
  ],
  "1637T>C": [
    "I502T",
    "No",
    "1637T>C",
    "c.1505T>C",
    "p.Ile502Thr",
    "0.00011842391973700416",
    "CF-causing",
    "25"
  ],
  "c.1505T>C": [
    "I502T",
    "No",
    "1637T>C",
    "c.1505T>C",
    "p.Ile502Thr",
    "0.00011842391973700416",
    "CF-causing",
    "25"
  ],
  "p.Ile502Thr": [
    "I502T",
    "No",
    "1637T>C",
    "c.1505T>C",
    "p.Ile502Thr",
    "0.00011842391973700416",
    "CF-causing",
    "25"
  ],
  "0.00011842391973700416": [
    "No",
    "0.00011842391973700416",
    "CF-causing",
    "p.Gly673X",
    "2149G>T",
    "25",
    "c.2017G>T",
    "G673X"
  ],
  "25": [
    "No",
    "0.00011842391973700416",
    "CF-causing",
    "p.Gly673X",
    "2149G>T",
    "25",
    "c.2017G>T",
    "G673X"
  ],
  "p.Gly673X": [
    "No",
    "0.00011842391973700416",
    "CF-causing",
    "p.Gly673X",
    "2149G>T",
    "25",
    "c.2017G>T",
    "G673X"
  ],
  "2149G>T": [
    "No",
    "0.00011842391973700416",
    "CF-causing",
    "p.Gly673X",
    "2149G>T",
    "25",
    "c.2017G>T",
    "G673X"
  ],
  "c.2017G>T": [
    "No",
    "0.00011842391973700416",
    "CF-causing",
    "p.Gly673X",
    "2149G>T",
    "25",
    "c.2017G>T",
    "G673X"
  ],
  "G673X": [
    "No",
    "0.00011842391973700416",
    "CF-causing",
    "p.Gly673X",
    "2149G>T",
    "25",
    "c.2017G>T",
    "G673X"
  ],
  "A613T": [
    "A613T",
    "No",
    "p.Ala613Thr",
    "24",
    "0.00011368696294752399",
    "CF-causing",
    "1969G>A",
    "c.1837G>A"
  ],
  "p.Ala613Thr": [
    "A613T",
    "No",
    "p.Ala613Thr",
    "24",
    "0.00011368696294752399",
    "CF-causing",
    "1969G>A",
    "c.1837G>A"
  ],
  "24": [
    "p.?",
    "No",
    "24",
    "0.00011368696294752399",
    "CF-causing",
    "c.743+1G>A",
    "875+1G->A"
  ],
  "0.00011368696294752399": [
    "p.?",
    "No",
    "24",
    "0.00011368696294752399",
    "CF-causing",
    "c.743+1G>A",
    "875+1G->A"
  ],
  "1969G>A": [
    "A613T",
    "No",
    "p.Ala613Thr",
    "24",
    "0.00011368696294752399",
    "CF-causing",
    "1969G>A",
    "c.1837G>A"
  ],
  "c.1837G>A": [
    "A613T",
    "No",
    "p.Ala613Thr",
    "24",
    "0.00011368696294752399",
    "CF-causing",
    "1969G>A",
    "c.1837G>A"
  ],
  "c.3107C>A": [
    "No",
    "24",
    "c.3107C>A",
    "0.00011368696294752399",
    "CF-causing",
    "3239C>A",
    "p.Thr1036Asn",
    "T1036N"
  ],
  "3239C>A": [
    "No",
    "24",
    "c.3107C>A",
    "0.00011368696294752399",
    "CF-causing",
    "3239C>A",
    "p.Thr1036Asn",
    "T1036N"
  ],
  "p.Thr1036Asn": [
    "No",
    "24",
    "c.3107C>A",
    "0.00011368696294752399",
    "CF-causing",
    "3239C>A",
    "p.Thr1036Asn",
    "T1036N"
  ],
  "T1036N": [
    "No",
    "24",
    "c.3107C>A",
    "0.00011368696294752399",
    "CF-causing",
    "3239C>A",
    "p.Thr1036Asn",
    "T1036N"
  ],
  "deletion of exons 19, 20, and 21 (legacy numbering)|deletion of exons 22, 23, and 24 (current numbering)": [
    "p.?",
    "No",
    "24",
    "deletion of exons 19, 20, and 21 (legacy numbering)|deletion of exons 22, 23, and 24 (current numbering)",
    "0.00011368696294752399",
    "CF-causing",
    "CFTRdele19-21",
    "c.(3468+1_3469-1)_(3963+1_3964-1)del"
  ],
  "CFTRdele19-21": [
    "p.?",
    "No",
    "24",
    "deletion of exons 19, 20, and 21 (legacy numbering)|deletion of exons 22, 23, and 24 (current numbering)",
    "0.00011368696294752399",
    "CF-causing",
    "CFTRdele19-21",
    "c.(3468+1_3469-1)_(3963+1_3964-1)del"
  ],
  "c.(3468+1_3469-1)_(3963+1_3964-1)del": [
    "p.?",
    "No",
    "24",
    "deletion of exons 19, 20, and 21 (legacy numbering)|deletion of exons 22, 23, and 24 (current numbering)",
    "0.00011368696294752399",
    "CF-causing",
    "CFTRdele19-21",
    "c.(3468+1_3469-1)_(3963+1_3964-1)del"
  ],
  "c.1393-2A>G": [
    "c.1393-2A>G",
    "p.?",
    "No",
    "24",
    "0.00011368696294752399",
    "CF-causing",
    "1525-2A->G"
  ],
  "1525-2A->G": [
    "c.1393-2A>G",
    "p.?",
    "No",
    "24",
    "0.00011368696294752399",
    "CF-causing",
    "1525-2A->G"
  ],
  "c.743+1G>A": [
    "p.?",
    "No",
    "24",
    "0.00011368696294752399",
    "CF-causing",
    "c.743+1G>A",
    "875+1G->A"
  ],
  "875+1G->A": [
    "p.?",
    "No",
    "24",
    "0.00011368696294752399",
    "CF-causing",
    "c.743+1G>A",
    "875+1G->A"
  ],
  "deletion of exons 4 through 11 (legacy numbering)|deletion of exons 4 through 12 (current numbering)": [
    "p.?",
    "No",
    "deletion of exons 4 through 11 (legacy numbering)|deletion of exons 4 through 12 (current numbering)",
    "c.(273+1_274-1)_(1679+1_1680-1)del",
    "CFTRdele4-11",
    "23",
    "CF-causing",
    "0.00010895000615804382"
  ],
  "c.(273+1_274-1)_(1679+1_1680-1)del": [
    "p.?",
    "No",
    "deletion of exons 4 through 11 (legacy numbering)|deletion of exons 4 through 12 (current numbering)",
    "c.(273+1_274-1)_(1679+1_1680-1)del",
    "CFTRdele4-11",
    "23",
    "CF-causing",
    "0.00010895000615804382"
  ],
  "CFTRdele4-11": [
    "p.?",
    "No",
    "deletion of exons 4 through 11 (legacy numbering)|deletion of exons 4 through 12 (current numbering)",
    "c.(273+1_274-1)_(1679+1_1680-1)del",
    "CFTRdele4-11",
    "23",
    "CF-causing",
    "0.00010895000615804382"
  ],
  "23": [
    "c.489+3A>G",
    "p.?",
    "No",
    "Varying clinical consequence",
    "23",
    "621+3A->G",
    "0.00010895000615804382"
  ],
  "0.00010895000615804382": [
    "c.489+3A>G",
    "p.?",
    "No",
    "Varying clinical consequence",
    "23",
    "621+3A->G",
    "0.00010895000615804382"
  ],
  "c.1081del": [
    "No",
    "c.1081del",
    "23",
    "CF-causing",
    "1213delT",
    "0.00010895000615804382",
    "p.Trp361GlyfsX8"
  ],
  "1213delT": [
    "No",
    "c.1081del",
    "23",
    "CF-causing",
    "1213delT",
    "0.00010895000615804382",
    "p.Trp361GlyfsX8"
  ],
  "p.Trp361GlyfsX8": [
    "4.7369567894801664e-06",
    "1212delA",
    "Yes, new variant added",
    "c.1080del",
    "CF-causing",
    "1",
    "p.Trp361GlyfsX8"
  ],
  "Yes, new variant added": [
    "c.273+7982del18652",
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "405+7982del18652"
  ],
  "M1T": [
    "p.?",
    "Yes, new variant added",
    "M1T",
    "23",
    "CF-causing",
    "c.2T>C",
    "0.00010895000615804382"
  ],
  "c.2T>C": [
    "p.?",
    "Yes, new variant added",
    "M1T",
    "23",
    "CF-causing",
    "c.2T>C",
    "0.00010895000615804382"
  ],
  "c.489+3A>G": [
    "c.489+3A>G",
    "p.?",
    "No",
    "Varying clinical consequence",
    "23",
    "621+3A->G",
    "0.00010895000615804382"
  ],
  "621+3A->G": [
    "c.489+3A>G",
    "p.?",
    "No",
    "Varying clinical consequence",
    "23",
    "621+3A->G",
    "0.00010895000615804382"
  ],
  "1985T>C": [
    "1985T>C",
    "21",
    "p.Ile618Thr",
    "Varying clinical consequence",
    "CF-causing",
    "Yes",
    "c.1853T>C",
    "I618T",
    "9.94760925790835e-05"
  ],
  "21": [
    "No",
    "21",
    "c.2051_2052del",
    "CF-causing",
    "2183delAA",
    "p.Lys684ThrfsX4",
    "9.94760925790835e-05"
  ],
  "p.Ile618Thr": [
    "1985T>C",
    "21",
    "p.Ile618Thr",
    "Varying clinical consequence",
    "CF-causing",
    "Yes",
    "c.1853T>C",
    "I618T",
    "9.94760925790835e-05"
  ],
  "c.1853T>C": [
    "1985T>C",
    "21",
    "p.Ile618Thr",
    "Varying clinical consequence",
    "CF-causing",
    "Yes",
    "c.1853T>C",
    "I618T",
    "9.94760925790835e-05"
  ],
  "I618T": [
    "1985T>C",
    "21",
    "p.Ile618Thr",
    "Varying clinical consequence",
    "CF-causing",
    "Yes",
    "c.1853T>C",
    "I618T",
    "9.94760925790835e-05"
  ],
  "9.94760925790835e-05": [
    "No",
    "21",
    "c.2051_2052del",
    "CF-causing",
    "2183delAA",
    "p.Lys684ThrfsX4",
    "9.94760925790835e-05"
  ],
  "c.2421A>G": [
    "No",
    "21",
    "c.2421A>G",
    "Non CF-causing",
    "p.Ile807Met",
    "2553A>G",
    "I807M",
    "9.94760925790835e-05"
  ],
  "p.Ile807Met": [
    "No",
    "21",
    "c.2421A>G",
    "Non CF-causing",
    "p.Ile807Met",
    "2553A>G",
    "I807M",
    "9.94760925790835e-05"
  ],
  "2553A>G": [
    "No",
    "21",
    "c.2421A>G",
    "Non CF-causing",
    "p.Ile807Met",
    "2553A>G",
    "I807M",
    "9.94760925790835e-05"
  ],
  "I807M": [
    "No",
    "21",
    "c.2421A>G",
    "Non CF-causing",
    "p.Ile807Met",
    "2553A>G",
    "I807M",
    "9.94760925790835e-05"
  ],
  "p.Tyr849X": [
    "p.Tyr849X",
    "No",
    "21",
    "c.2547C>A",
    "CF-causing",
    "2679C>A",
    "Y849X",
    "9.94760925790835e-05"
  ],
  "c.2547C>A": [
    "p.Tyr849X",
    "No",
    "21",
    "c.2547C>A",
    "CF-causing",
    "2679C>A",
    "Y849X",
    "9.94760925790835e-05"
  ],
  "2679C>A": [
    "p.Tyr849X",
    "No",
    "21",
    "c.2547C>A",
    "CF-causing",
    "2679C>A",
    "Y849X",
    "9.94760925790835e-05"
  ],
  "Y849X": [
    "p.Tyr849X",
    "No",
    "21",
    "c.2547C>A",
    "CF-causing",
    "2679C>A",
    "Y849X",
    "9.94760925790835e-05"
  ],
  "3354T>A|3352T>C|3354T>G": [
    "No",
    "21",
    "3354T>A|3352T>C|3354T>G",
    "p.Phe1074Leu",
    "c.3220T>C|c.3222T>G|c.3222T>A",
    "9.94760925790835e-05",
    "Varying clinical consequence",
    "F1074L"
  ],
  "p.Phe1074Leu": [
    "No",
    "21",
    "3354T>A|3352T>C|3354T>G",
    "p.Phe1074Leu",
    "c.3220T>C|c.3222T>G|c.3222T>A",
    "9.94760925790835e-05",
    "Varying clinical consequence",
    "F1074L"
  ],
  "c.3220T>C|c.3222T>G|c.3222T>A": [
    "No",
    "21",
    "3354T>A|3352T>C|3354T>G",
    "p.Phe1074Leu",
    "c.3220T>C|c.3222T>G|c.3222T>A",
    "9.94760925790835e-05",
    "Varying clinical consequence",
    "F1074L"
  ],
  "F1074L": [
    "No",
    "21",
    "3354T>A|3352T>C|3354T>G",
    "p.Phe1074Leu",
    "c.3220T>C|c.3222T>G|c.3222T>A",
    "9.94760925790835e-05",
    "Varying clinical consequence",
    "F1074L"
  ],
  "957C>G": [
    "957C>G",
    "No",
    "21",
    "Y275X",
    "CF-causing",
    "c.825C>G",
    "p.Tyr275X",
    "9.94760925790835e-05"
  ],
  "Y275X": [
    "957C>G",
    "No",
    "21",
    "Y275X",
    "CF-causing",
    "c.825C>G",
    "p.Tyr275X",
    "9.94760925790835e-05"
  ],
  "c.825C>G": [
    "957C>G",
    "No",
    "21",
    "Y275X",
    "CF-causing",
    "c.825C>G",
    "p.Tyr275X",
    "9.94760925790835e-05"
  ],
  "p.Tyr275X": [
    "957C>G",
    "No",
    "21",
    "Y275X",
    "CF-causing",
    "c.825C>G",
    "p.Tyr275X",
    "9.94760925790835e-05"
  ],
  "p.Thr1179IlefsX17": [
    "No",
    "21",
    "p.Thr1179IlefsX17",
    "CF-causing",
    "c.3535_3536insTCAA",
    "c.3532_3535dup",
    "3667ins4",
    "9.94760925790835e-05"
  ],
  "c.3535_3536insTCAA": [
    "No",
    "21",
    "p.Thr1179IlefsX17",
    "CF-causing",
    "c.3535_3536insTCAA",
    "c.3532_3535dup",
    "3667ins4",
    "9.94760925790835e-05"
  ],
  "c.3532_3535dup": [
    "No",
    "21",
    "p.Thr1179IlefsX17",
    "CF-causing",
    "c.3535_3536insTCAA",
    "c.3532_3535dup",
    "3667ins4",
    "9.94760925790835e-05"
  ],
  "3667ins4": [
    "No",
    "21",
    "p.Thr1179IlefsX17",
    "CF-causing",
    "c.3535_3536insTCAA",
    "c.3532_3535dup",
    "3667ins4",
    "9.94760925790835e-05"
  ],
  "p.Ile105SerfsX2": [
    "p.Ile105SerfsX2",
    "No",
    "21",
    "CF-causing",
    "c.313del",
    "444delA",
    "9.94760925790835e-05"
  ],
  "c.313del": [
    "p.Ile105SerfsX2",
    "No",
    "21",
    "CF-causing",
    "c.313del",
    "444delA",
    "9.94760925790835e-05"
  ],
  "444delA": [
    "p.Ile105SerfsX2",
    "No",
    "21",
    "CF-causing",
    "c.313del",
    "444delA",
    "9.94760925790835e-05"
  ],
  "c.2051_2052del": [
    "No",
    "21",
    "c.2051_2052del",
    "CF-causing",
    "2183delAA",
    "p.Lys684ThrfsX4",
    "9.94760925790835e-05"
  ],
  "2183delAA": [
    "No",
    "21",
    "c.2051_2052del",
    "CF-causing",
    "2183delAA",
    "p.Lys684ThrfsX4",
    "9.94760925790835e-05"
  ],
  "p.Lys684ThrfsX4": [
    "No",
    "21",
    "c.2051_2052del",
    "CF-causing",
    "2183delAA",
    "p.Lys684ThrfsX4",
    "9.94760925790835e-05"
  ],
  "9.473913578960333e-05": [
    "9.473913578960333e-05",
    "p.?",
    "No",
    "20",
    "CF-causing",
    "3849+4A->G",
    "c.3717+4A>G"
  ],
  "20": [
    "9.473913578960333e-05",
    "p.?",
    "No",
    "20",
    "CF-causing",
    "3849+4A->G",
    "c.3717+4A>G"
  ],
  "c.1135G>T": [
    "9.473913578960333e-05",
    "No",
    "20",
    "c.1135G>T",
    "CF-causing",
    "1267G>T",
    "E379X",
    "p.Glu379X"
  ],
  "1267G>T": [
    "9.473913578960333e-05",
    "No",
    "20",
    "c.1135G>T",
    "CF-causing",
    "1267G>T",
    "E379X",
    "p.Glu379X"
  ],
  "E379X": [
    "9.473913578960333e-05",
    "No",
    "20",
    "c.1135G>T",
    "CF-causing",
    "1267G>T",
    "E379X",
    "p.Glu379X"
  ],
  "p.Glu379X": [
    "9.473913578960333e-05",
    "No",
    "20",
    "c.1135G>T",
    "CF-causing",
    "1267G>T",
    "E379X",
    "p.Glu379X"
  ],
  "C524X": [
    "9.473913578960333e-05",
    "No",
    "C524X",
    "20",
    "CF-causing",
    "1704C>A",
    "p.Cys524X",
    "c.1572C>A"
  ],
  "1704C>A": [
    "9.473913578960333e-05",
    "No",
    "C524X",
    "20",
    "CF-causing",
    "1704C>A",
    "p.Cys524X",
    "c.1572C>A"
  ],
  "p.Cys524X": [
    "9.473913578960333e-05",
    "No",
    "C524X",
    "20",
    "CF-causing",
    "1704C>A",
    "p.Cys524X",
    "c.1572C>A"
  ],
  "c.1572C>A": [
    "9.473913578960333e-05",
    "No",
    "C524X",
    "20",
    "CF-causing",
    "1704C>A",
    "p.Cys524X",
    "c.1572C>A"
  ],
  "1811G>A": [
    "9.473913578960333e-05",
    "No",
    "20",
    "1811G>A",
    "R560K",
    "CF-causing",
    "p.Arg560Lys",
    "c.1679G>A"
  ],
  "R560K": [
    "9.473913578960333e-05",
    "No",
    "20",
    "1811G>A",
    "R560K",
    "CF-causing",
    "p.Arg560Lys",
    "c.1679G>A"
  ],
  "p.Arg560Lys": [
    "9.473913578960333e-05",
    "No",
    "20",
    "1811G>A",
    "R560K",
    "CF-causing",
    "p.Arg560Lys",
    "c.1679G>A"
  ],
  "c.1679G>A": [
    "9.473913578960333e-05",
    "No",
    "20",
    "1811G>A",
    "R560K",
    "CF-causing",
    "p.Arg560Lys",
    "c.1679G>A"
  ],
  "p.Ser1159Pro": [
    "9.473913578960333e-05",
    "p.Ser1159Pro",
    "No",
    "20",
    "CF-causing",
    "c.3475T>C",
    "S1159P",
    "3607T>C"
  ],
  "c.3475T>C": [
    "9.473913578960333e-05",
    "p.Ser1159Pro",
    "No",
    "20",
    "CF-causing",
    "c.3475T>C",
    "S1159P",
    "3607T>C"
  ],
  "S1159P": [
    "9.473913578960333e-05",
    "p.Ser1159Pro",
    "No",
    "20",
    "CF-causing",
    "c.3475T>C",
    "S1159P",
    "3607T>C"
  ],
  "3607T>C": [
    "9.473913578960333e-05",
    "p.Ser1159Pro",
    "No",
    "20",
    "CF-causing",
    "c.3475T>C",
    "S1159P",
    "3607T>C"
  ],
  "R1162L": [
    "9.473913578960333e-05",
    "No",
    "20",
    "R1162L",
    "p.Arg1162Leu",
    "Non CF-causing",
    "c.3485G>T",
    "3671G/T|3617G>T"
  ],
  "p.Arg1162Leu": [
    "9.473913578960333e-05",
    "No",
    "20",
    "R1162L",
    "p.Arg1162Leu",
    "Non CF-causing",
    "c.3485G>T",
    "3671G/T|3617G>T"
  ],
  "c.3485G>T": [
    "9.473913578960333e-05",
    "No",
    "20",
    "R1162L",
    "p.Arg1162Leu",
    "Non CF-causing",
    "c.3485G>T",
    "3671G/T|3617G>T"
  ],
  "3671G/T|3617G>T": [
    "9.473913578960333e-05",
    "No",
    "20",
    "R1162L",
    "p.Arg1162Leu",
    "Non CF-causing",
    "c.3485G>T",
    "3671G/T|3617G>T"
  ],
  "3938T>A": [
    "9.473913578960333e-05",
    "No",
    "20",
    "3938T>A",
    "p.Ile1269Asn",
    "CF-causing",
    "c.3806T>A",
    "I1269N"
  ],
  "p.Ile1269Asn": [
    "9.473913578960333e-05",
    "No",
    "20",
    "3938T>A",
    "p.Ile1269Asn",
    "CF-causing",
    "c.3806T>A",
    "I1269N"
  ],
  "c.3806T>A": [
    "9.473913578960333e-05",
    "No",
    "20",
    "3938T>A",
    "p.Ile1269Asn",
    "CF-causing",
    "c.3806T>A",
    "I1269N"
  ],
  "I1269N": [
    "9.473913578960333e-05",
    "No",
    "20",
    "3938T>A",
    "p.Ile1269Asn",
    "CF-causing",
    "c.3806T>A",
    "I1269N"
  ],
  "641G>A": [
    "9.473913578960333e-05",
    "No",
    "20",
    "641G>A",
    "p.Arg170His",
    "c.509G>A",
    "Non CF-causing",
    "R170H"
  ],
  "p.Arg170His": [
    "9.473913578960333e-05",
    "No",
    "20",
    "641G>A",
    "p.Arg170His",
    "c.509G>A",
    "Non CF-causing",
    "R170H"
  ],
  "c.509G>A": [
    "9.473913578960333e-05",
    "No",
    "20",
    "641G>A",
    "p.Arg170His",
    "c.509G>A",
    "Non CF-causing",
    "R170H"
  ],
  "R170H": [
    "9.473913578960333e-05",
    "No",
    "20",
    "641G>A",
    "p.Arg170His",
    "c.509G>A",
    "Non CF-causing",
    "R170H"
  ],
  "c.53+1G>T": [
    "9.473913578960333e-05",
    "p.?",
    "No",
    "20",
    "c.53+1G>T",
    "185+1G->T",
    "CF-causing"
  ],
  "185+1G->T": [
    "9.473913578960333e-05",
    "p.?",
    "No",
    "20",
    "c.53+1G>T",
    "185+1G->T",
    "CF-causing"
  ],
  "c.3874-1G>A": [
    "9.473913578960333e-05",
    "c.3874-1G>A",
    "p.?",
    "No",
    "4006-1G->A",
    "20",
    "CF-causing"
  ],
  "4006-1G->A": [
    "9.473913578960333e-05",
    "c.3874-1G>A",
    "p.?",
    "No",
    "4006-1G->A",
    "20",
    "CF-causing"
  ],
  "c.3747del": [
    "9.473913578960333e-05",
    "No",
    "20",
    "c.3747del",
    "p.Lys1250ArgfsX9",
    "CF-causing",
    "3878delG"
  ],
  "3878delG": [
    "9.473913578960333e-05",
    "No",
    "20",
    "c.3747del",
    "p.Lys1250ArgfsX9",
    "CF-causing",
    "3878delG"
  ],
  "3849+4A->G": [
    "9.473913578960333e-05",
    "p.?",
    "No",
    "20",
    "CF-causing",
    "3849+4A->G",
    "c.3717+4A>G"
  ],
  "c.3717+4A>G": [
    "9.473913578960333e-05",
    "p.?",
    "No",
    "20",
    "CF-causing",
    "3849+4A->G",
    "c.3717+4A>G"
  ],
  "p.Gln525X": [
    "p.Gln525X",
    "1705C>T",
    "No",
    "9.000217900012316e-05",
    "Q525X",
    "c.1573C>T",
    "CF-causing",
    "19"
  ],
  "1705C>T": [
    "p.Gln525X",
    "1705C>T",
    "No",
    "9.000217900012316e-05",
    "Q525X",
    "c.1573C>T",
    "CF-causing",
    "19"
  ],
  "9.000217900012316e-05": [
    "No",
    "9.000217900012316e-05",
    "CF-causing",
    "19",
    "c.3002_3003del",
    "p.Val1001AspfsX45",
    "3132delTG"
  ],
  "Q525X": [
    "p.Gln525X",
    "1705C>T",
    "No",
    "9.000217900012316e-05",
    "Q525X",
    "c.1573C>T",
    "CF-causing",
    "19"
  ],
  "c.1573C>T": [
    "p.Gln525X",
    "1705C>T",
    "No",
    "9.000217900012316e-05",
    "Q525X",
    "c.1573C>T",
    "CF-causing",
    "19"
  ],
  "19": [
    "No",
    "9.000217900012316e-05",
    "CF-causing",
    "19",
    "c.3002_3003del",
    "p.Val1001AspfsX45",
    "3132delTG"
  ],
  "Q1291R": [
    "Q1291R",
    "No",
    "9.000217900012316e-05",
    "c.3872A>G",
    "Varying clinical consequence",
    "4004A>G",
    "19",
    "p.Gln1291Arg"
  ],
  "c.3872A>G": [
    "Q1291R",
    "No",
    "9.000217900012316e-05",
    "c.3872A>G",
    "Varying clinical consequence",
    "4004A>G",
    "19",
    "p.Gln1291Arg"
  ],
  "4004A>G": [
    "Q1291R",
    "No",
    "9.000217900012316e-05",
    "c.3872A>G",
    "Varying clinical consequence",
    "4004A>G",
    "19",
    "p.Gln1291Arg"
  ],
  "p.Gln1291Arg": [
    "Q1291R",
    "No",
    "9.000217900012316e-05",
    "c.3872A>G",
    "Varying clinical consequence",
    "4004A>G",
    "19",
    "p.Gln1291Arg"
  ],
  "deletion of exons 2, 3, and 4 (legacy and current numbering)|IVSI-5842_IVS4+401del|c.54-5842_489+401del": [
    "p.?",
    "deletion of exons 2, 3, and 4 (legacy and current numbering)|IVSI-5842_IVS4+401del|c.54-5842_489+401del",
    "9.000217900012316e-05",
    "No",
    "CF-causing",
    "19",
    "c.(53+1_54-1)_(489+1_490-1)del",
    "CFTRdele2-4"
  ],
  "c.(53+1_54-1)_(489+1_490-1)del": [
    "p.?",
    "deletion of exons 2, 3, and 4 (legacy and current numbering)|IVSI-5842_IVS4+401del|c.54-5842_489+401del",
    "9.000217900012316e-05",
    "No",
    "CF-causing",
    "19",
    "c.(53+1_54-1)_(489+1_490-1)del",
    "CFTRdele2-4"
  ],
  "CFTRdele2-4": [
    "p.?",
    "deletion of exons 2, 3, and 4 (legacy and current numbering)|IVSI-5842_IVS4+401del|c.54-5842_489+401del",
    "9.000217900012316e-05",
    "No",
    "CF-causing",
    "19",
    "c.(53+1_54-1)_(489+1_490-1)del",
    "CFTRdele2-4"
  ],
  "c.3002_3003del": [
    "No",
    "9.000217900012316e-05",
    "CF-causing",
    "19",
    "c.3002_3003del",
    "p.Val1001AspfsX45",
    "3132delTG"
  ],
  "p.Val1001AspfsX45": [
    "No",
    "9.000217900012316e-05",
    "CF-causing",
    "19",
    "c.3002_3003del",
    "p.Val1001AspfsX45",
    "3132delTG"
  ],
  "3132delTG": [
    "No",
    "9.000217900012316e-05",
    "CF-causing",
    "19",
    "c.3002_3003del",
    "p.Val1001AspfsX45",
    "3132delTG"
  ],
  "Q414X": [
    "No",
    "Q414X",
    "18",
    "p.Gln414X",
    "CF-causing",
    "1372C>T",
    "c.1240C>T",
    "8.5265222210643e-05"
  ],
  "18": [
    "p.?",
    "No",
    "c.2989-2A>G",
    "18",
    "CF-causing",
    "3121-2A->G",
    "8.5265222210643e-05"
  ],
  "p.Gln414X": [
    "No",
    "Q414X",
    "18",
    "p.Gln414X",
    "CF-causing",
    "1372C>T",
    "c.1240C>T",
    "8.5265222210643e-05"
  ],
  "1372C>T": [
    "No",
    "Q414X",
    "18",
    "p.Gln414X",
    "CF-causing",
    "1372C>T",
    "c.1240C>T",
    "8.5265222210643e-05"
  ],
  "c.1240C>T": [
    "No",
    "Q414X",
    "18",
    "p.Gln414X",
    "CF-causing",
    "1372C>T",
    "c.1240C>T",
    "8.5265222210643e-05"
  ],
  "8.5265222210643e-05": [
    "p.?",
    "No",
    "c.2989-2A>G",
    "18",
    "CF-causing",
    "3121-2A->G",
    "8.5265222210643e-05"
  ],
  "c.1882G>A|c.1882G>C": [
    "c.1882G>A|c.1882G>C",
    "No",
    "2014G>C|2014G>A",
    "18",
    "CF-causing",
    "p.Gly628Arg",
    "8.5265222210643e-05",
    "G628R"
  ],
  "2014G>C|2014G>A": [
    "c.1882G>A|c.1882G>C",
    "No",
    "2014G>C|2014G>A",
    "18",
    "CF-causing",
    "p.Gly628Arg",
    "8.5265222210643e-05",
    "G628R"
  ],
  "p.Gly628Arg": [
    "c.1882G>A|c.1882G>C",
    "No",
    "2014G>C|2014G>A",
    "18",
    "CF-causing",
    "p.Gly628Arg",
    "8.5265222210643e-05",
    "G628R"
  ],
  "G628R": [
    "c.1882G>A|c.1882G>C",
    "No",
    "2014G>C|2014G>A",
    "18",
    "CF-causing",
    "p.Gly628Arg",
    "8.5265222210643e-05",
    "G628R"
  ],
  "p.Gly970Arg": [
    "p.Gly970Arg",
    "3040G>C",
    "No",
    "18",
    "CF-causing",
    "G970R",
    "c.2908G>C",
    "8.5265222210643e-05"
  ],
  "3040G>C": [
    "p.Gly970Arg",
    "3040G>C",
    "No",
    "18",
    "CF-causing",
    "G970R",
    "c.2908G>C",
    "8.5265222210643e-05"
  ],
  "G970R": [
    "p.Gly970Arg",
    "3040G>C",
    "No",
    "18",
    "CF-causing",
    "G970R",
    "c.2908G>C",
    "8.5265222210643e-05"
  ],
  "c.2908G>C": [
    "p.Gly970Arg",
    "3040G>C",
    "No",
    "18",
    "CF-causing",
    "G970R",
    "c.2908G>C",
    "8.5265222210643e-05"
  ],
  "4015del4|c.3882_3885delTATT": [
    "4015del4|c.3882_3885delTATT",
    "No",
    "c.3883_3886del",
    "18",
    "p.Ile1295PhefsX32",
    "CF-causing",
    "4010del4",
    "8.5265222210643e-05"
  ],
  "c.3883_3886del": [
    "4015del4|c.3882_3885delTATT",
    "No",
    "c.3883_3886del",
    "18",
    "p.Ile1295PhefsX32",
    "CF-causing",
    "4010del4",
    "8.5265222210643e-05"
  ],
  "p.Ile1295PhefsX32": [
    "4015del4|c.3882_3885delTATT",
    "No",
    "c.3883_3886del",
    "18",
    "p.Ile1295PhefsX32",
    "CF-causing",
    "4010del4",
    "8.5265222210643e-05"
  ],
  "4010del4": [
    "4015del4|c.3882_3885delTATT",
    "No",
    "c.3883_3886del",
    "18",
    "p.Ile1295PhefsX32",
    "CF-causing",
    "4010del4",
    "8.5265222210643e-05"
  ],
  "c.4231C>T": [
    "c.4231C>T",
    "No",
    "18",
    "4363C>T",
    "CF-causing",
    "p.Gln1411X",
    "Q1411X",
    "8.5265222210643e-05"
  ],
  "4363C>T": [
    "c.4231C>T",
    "No",
    "18",
    "4363C>T",
    "CF-causing",
    "p.Gln1411X",
    "Q1411X",
    "8.5265222210643e-05"
  ],
  "p.Gln1411X": [
    "c.4231C>T",
    "No",
    "18",
    "4363C>T",
    "CF-causing",
    "p.Gln1411X",
    "Q1411X",
    "8.5265222210643e-05"
  ],
  "Q1411X": [
    "c.4231C>T",
    "No",
    "18",
    "4363C>T",
    "CF-causing",
    "p.Gln1411X",
    "Q1411X",
    "8.5265222210643e-05"
  ],
  "c.2989-2A>G": [
    "p.?",
    "No",
    "c.2989-2A>G",
    "18",
    "CF-causing",
    "3121-2A->G",
    "8.5265222210643e-05"
  ],
  "3121-2A->G": [
    "p.?",
    "No",
    "c.2989-2A>G",
    "18",
    "CF-causing",
    "3121-2A->G",
    "8.5265222210643e-05"
  ],
  "3895T>C": [
    "3895T>C",
    "8.052826542116283e-05",
    "S1255P",
    "No",
    "CF-causing",
    "p.Ser1255Pro",
    "17",
    "c.3763T>C"
  ],
  "8.052826542116283e-05": [
    "8.052826542116283e-05",
    "p.?",
    "No",
    "c.1766+5G>T",
    "CF-causing",
    "17",
    "1898+5G->T"
  ],
  "S1255P": [
    "3895T>C",
    "8.052826542116283e-05",
    "S1255P",
    "No",
    "CF-causing",
    "p.Ser1255Pro",
    "17",
    "c.3763T>C"
  ],
  "p.Ser1255Pro": [
    "3895T>C",
    "8.052826542116283e-05",
    "S1255P",
    "No",
    "CF-causing",
    "p.Ser1255Pro",
    "17",
    "c.3763T>C"
  ],
  "17": [
    "8.052826542116283e-05",
    "p.?",
    "No",
    "c.1766+5G>T",
    "CF-causing",
    "17",
    "1898+5G->T"
  ],
  "c.3763T>C": [
    "3895T>C",
    "8.052826542116283e-05",
    "S1255P",
    "No",
    "CF-causing",
    "p.Ser1255Pro",
    "17",
    "c.3763T>C"
  ],
  "R117L": [
    "R117L",
    "8.052826542116283e-05",
    "No",
    "c.350G>T",
    "Varying clinical consequence",
    "p.Arg117Leu",
    "17",
    "482G>T"
  ],
  "c.350G>T": [
    "R117L",
    "8.052826542116283e-05",
    "No",
    "c.350G>T",
    "Varying clinical consequence",
    "p.Arg117Leu",
    "17",
    "482G>T"
  ],
  "p.Arg117Leu": [
    "R117L",
    "8.052826542116283e-05",
    "No",
    "c.350G>T",
    "Varying clinical consequence",
    "p.Arg117Leu",
    "17",
    "482G>T"
  ],
  "482G>T": [
    "R117L",
    "8.052826542116283e-05",
    "No",
    "c.350G>T",
    "Varying clinical consequence",
    "p.Arg117Leu",
    "17",
    "482G>T"
  ],
  "c.233_234insT|359insT|360-365insT": [
    "8.052826542116283e-05",
    "No",
    "c.233_234insT|359insT|360-365insT",
    "CF-causing",
    "17",
    "p.Trp79LeufsX32",
    "365-366insT",
    "c.233dup"
  ],
  "p.Trp79LeufsX32": [
    "Yes, new variant added",
    "c.234dup",
    "2.8421740736880997e-05",
    "366insC",
    "CF-causing",
    "6",
    "p.Trp79LeufsX32"
  ],
  "365-366insT": [
    "8.052826542116283e-05",
    "No",
    "c.233_234insT|359insT|360-365insT",
    "CF-causing",
    "17",
    "p.Trp79LeufsX32",
    "365-366insT",
    "c.233dup"
  ],
  "c.233dup": [
    "8.052826542116283e-05",
    "No",
    "c.233_234insT|359insT|360-365insT",
    "CF-causing",
    "17",
    "p.Trp79LeufsX32",
    "365-366insT",
    "c.233dup"
  ],
  "c.2810dup": [
    "c.2810dup",
    "8.052826542116283e-05",
    "No",
    "2942insT",
    "CF-causing",
    "c.2810_2811insT",
    "17",
    "p.Val938GlyfsX37"
  ],
  "2942insT": [
    "c.2810dup",
    "8.052826542116283e-05",
    "No",
    "2942insT",
    "CF-causing",
    "c.2810_2811insT",
    "17",
    "p.Val938GlyfsX37"
  ],
  "c.2810_2811insT": [
    "c.2810dup",
    "8.052826542116283e-05",
    "No",
    "2942insT",
    "CF-causing",
    "c.2810_2811insT",
    "17",
    "p.Val938GlyfsX37"
  ],
  "p.Val938GlyfsX37": [
    "c.2810dup",
    "8.052826542116283e-05",
    "No",
    "2942insT",
    "CF-causing",
    "c.2810_2811insT",
    "17",
    "p.Val938GlyfsX37"
  ],
  "CFTRdele16-17b": [
    "8.052826542116283e-05",
    "p.?",
    "No",
    "CFTRdele16-17b",
    "c.(2908+1_2909-1)_(3367+1_3368-1)del",
    "CF-causing",
    "17",
    "deletion of exons 16, 17a, and 17b (legacy numbering)|deletion of exons 18, 19, and 20 (current numbering)"
  ],
  "c.(2908+1_2909-1)_(3367+1_3368-1)del": [
    "8.052826542116283e-05",
    "p.?",
    "No",
    "CFTRdele16-17b",
    "c.(2908+1_2909-1)_(3367+1_3368-1)del",
    "CF-causing",
    "17",
    "deletion of exons 16, 17a, and 17b (legacy numbering)|deletion of exons 18, 19, and 20 (current numbering)"
  ],
  "deletion of exons 16, 17a, and 17b (legacy numbering)|deletion of exons 18, 19, and 20 (current numbering)": [
    "8.052826542116283e-05",
    "p.?",
    "No",
    "CFTRdele16-17b",
    "c.(2908+1_2909-1)_(3367+1_3368-1)del",
    "CF-causing",
    "17",
    "deletion of exons 16, 17a, and 17b (legacy numbering)|deletion of exons 18, 19, and 20 (current numbering)"
  ],
  "1342-2A->C": [
    "8.052826542116283e-05",
    "p.?",
    "No",
    "1342-2A->C",
    "CF-causing",
    "17",
    "c.1210-2A>C"
  ],
  "c.1210-2A>C": [
    "8.052826542116283e-05",
    "p.?",
    "No",
    "1342-2A->C",
    "CF-causing",
    "17",
    "c.1210-2A>C"
  ],
  "1497delGG": [
    "8.052826542116283e-05",
    "No",
    "1497delGG",
    "CF-causing",
    "c.1365_1366del",
    "17",
    "p.Val456CysfsX25"
  ],
  "c.1365_1366del": [
    "8.052826542116283e-05",
    "No",
    "1497delGG",
    "CF-causing",
    "c.1365_1366del",
    "17",
    "p.Val456CysfsX25"
  ],
  "p.Val456CysfsX25": [
    "8.052826542116283e-05",
    "No",
    "1497delGG",
    "CF-causing",
    "c.1365_1366del",
    "17",
    "p.Val456CysfsX25"
  ],
  "p.Asp58GlufsX32": [
    "p.Asp58GlufsX32",
    "8.052826542116283e-05",
    "No",
    "c.174_177del",
    "CF-causing",
    "306delTAGA",
    "17"
  ],
  "c.174_177del": [
    "p.Asp58GlufsX32",
    "8.052826542116283e-05",
    "No",
    "c.174_177del",
    "CF-causing",
    "306delTAGA",
    "17"
  ],
  "306delTAGA": [
    "p.Asp58GlufsX32",
    "8.052826542116283e-05",
    "No",
    "c.174_177del",
    "CF-causing",
    "306delTAGA",
    "17"
  ],
  "c.1766+5G>T": [
    "8.052826542116283e-05",
    "p.?",
    "No",
    "c.1766+5G>T",
    "CF-causing",
    "17",
    "1898+5G->T"
  ],
  "1898+5G->T": [
    "8.052826542116283e-05",
    "p.?",
    "No",
    "c.1766+5G>T",
    "CF-causing",
    "17",
    "1898+5G->T"
  ],
  "2381C>T": [
    "2381C>T",
    "No",
    "c.2249C>T",
    "P750L",
    "Varying clinical consequence",
    "p.Pro750Leu",
    "7.579130863168266e-05",
    "16"
  ],
  "c.2249C>T": [
    "2381C>T",
    "No",
    "c.2249C>T",
    "P750L",
    "Varying clinical consequence",
    "p.Pro750Leu",
    "7.579130863168266e-05",
    "16"
  ],
  "P750L": [
    "2381C>T",
    "No",
    "c.2249C>T",
    "P750L",
    "Varying clinical consequence",
    "p.Pro750Leu",
    "7.579130863168266e-05",
    "16"
  ],
  "p.Pro750Leu": [
    "2381C>T",
    "No",
    "c.2249C>T",
    "P750L",
    "Varying clinical consequence",
    "p.Pro750Leu",
    "7.579130863168266e-05",
    "16"
  ],
  "7.579130863168266e-05": [
    "p.?",
    "No",
    "124del23bp",
    "CF-causing",
    "7.579130863168266e-05",
    "16",
    "c.-9_14del"
  ],
  "16": [
    "p.?",
    "No",
    "124del23bp",
    "CF-causing",
    "7.579130863168266e-05",
    "16",
    "c.-9_14del"
  ],
  "c.3292T>C": [
    "No",
    "CF-causing",
    "c.3292T>C",
    "W1098R",
    "p.Trp1098Arg",
    "7.579130863168266e-05",
    "16",
    "3424T>C"
  ],
  "W1098R": [
    "No",
    "CF-causing",
    "c.3292T>C",
    "W1098R",
    "p.Trp1098Arg",
    "7.579130863168266e-05",
    "16",
    "3424T>C"
  ],
  "p.Trp1098Arg": [
    "No",
    "CF-causing",
    "c.3292T>C",
    "W1098R",
    "p.Trp1098Arg",
    "7.579130863168266e-05",
    "16",
    "3424T>C"
  ],
  "3424T>C": [
    "No",
    "CF-causing",
    "c.3292T>C",
    "W1098R",
    "p.Trp1098Arg",
    "7.579130863168266e-05",
    "16",
    "3424T>C"
  ],
  "3850-1G->A": [
    "3850-1G->A",
    "p.?",
    "No",
    "CF-causing",
    "c.3718-1G>A",
    "7.579130863168266e-05",
    "16"
  ],
  "c.3718-1G>A": [
    "3850-1G->A",
    "p.?",
    "No",
    "CF-causing",
    "c.3718-1G>A",
    "7.579130863168266e-05",
    "16"
  ],
  "1716+1G->A": [
    "p.?",
    "No",
    "CF-causing",
    "1716+1G->A",
    "c.1584+1G>A",
    "7.579130863168266e-05",
    "16"
  ],
  "c.1584+1G>A": [
    "p.?",
    "No",
    "CF-causing",
    "1716+1G->A",
    "c.1584+1G>A",
    "7.579130863168266e-05",
    "16"
  ],
  "c.2589_2599del": [
    "c.2589_2599del",
    "No",
    "2721del11",
    "CF-causing",
    "p.Ile864SerfsX28",
    "7.579130863168266e-05",
    "16"
  ],
  "2721del11": [
    "c.2589_2599del",
    "No",
    "2721del11",
    "CF-causing",
    "p.Ile864SerfsX28",
    "7.579130863168266e-05",
    "16"
  ],
  "p.Ile864SerfsX28": [
    "c.2589_2599del",
    "No",
    "2721del11",
    "CF-causing",
    "p.Ile864SerfsX28",
    "7.579130863168266e-05",
    "16"
  ],
  "c.3718-3T>G": [
    "c.3718-3T>G",
    "p.?",
    "No",
    "3850-3T->G",
    "CF-causing",
    "7.579130863168266e-05",
    "16"
  ],
  "3850-3T->G": [
    "c.3718-3T>G",
    "p.?",
    "No",
    "3850-3T->G",
    "CF-causing",
    "7.579130863168266e-05",
    "16"
  ],
  "124del23bp": [
    "p.?",
    "No",
    "124del23bp",
    "CF-causing",
    "7.579130863168266e-05",
    "16",
    "c.-9_14del"
  ],
  "c.-9_14del": [
    "p.?",
    "No",
    "124del23bp",
    "CF-causing",
    "7.579130863168266e-05",
    "16",
    "c.-9_14del"
  ],
  "c.933C>A|c.933C>G": [
    "No",
    "c.933C>A|c.933C>G",
    "7.10543518422025e-05",
    "1065C>G",
    "CF-causing",
    "F311L",
    "p.Phe311Leu",
    "15"
  ],
  "7.10543518422025e-05": [
    "p.?",
    "No",
    "7.10543518422025e-05",
    "CF-causing",
    "3849+5G->A",
    "15",
    "c.3717+5G>A"
  ],
  "1065C>G": [
    "No",
    "c.933C>A|c.933C>G",
    "7.10543518422025e-05",
    "1065C>G",
    "CF-causing",
    "F311L",
    "p.Phe311Leu",
    "15"
  ],
  "F311L": [
    "No",
    "c.933C>A|c.933C>G",
    "7.10543518422025e-05",
    "1065C>G",
    "CF-causing",
    "F311L",
    "p.Phe311Leu",
    "15"
  ],
  "p.Phe311Leu": [
    "No",
    "c.933C>A|c.933C>G",
    "7.10543518422025e-05",
    "1065C>G",
    "CF-causing",
    "F311L",
    "p.Phe311Leu",
    "15"
  ],
  "15": [
    "p.?",
    "No",
    "7.10543518422025e-05",
    "CF-causing",
    "3849+5G->A",
    "15",
    "c.3717+5G>A"
  ],
  "1133G>A": [
    "1133G>A",
    "p.Arg334Gln",
    "R334Q",
    "No",
    "7.10543518422025e-05",
    "Varying clinical consequence",
    "15",
    "c.1001G>A"
  ],
  "p.Arg334Gln": [
    "1133G>A",
    "p.Arg334Gln",
    "R334Q",
    "No",
    "7.10543518422025e-05",
    "Varying clinical consequence",
    "15",
    "c.1001G>A"
  ],
  "R334Q": [
    "1133G>A",
    "p.Arg334Gln",
    "R334Q",
    "No",
    "7.10543518422025e-05",
    "Varying clinical consequence",
    "15",
    "c.1001G>A"
  ],
  "c.1001G>A": [
    "1133G>A",
    "p.Arg334Gln",
    "R334Q",
    "No",
    "7.10543518422025e-05",
    "Varying clinical consequence",
    "15",
    "c.1001G>A"
  ],
  "c.2506G>T": [
    "No",
    "c.2506G>T",
    "D836Y",
    "7.10543518422025e-05",
    "2638G>T",
    "15",
    "Non CF-causing",
    "p.Asp836Tyr"
  ],
  "D836Y": [
    "No",
    "c.2506G>T",
    "D836Y",
    "7.10543518422025e-05",
    "2638G>T",
    "15",
    "Non CF-causing",
    "p.Asp836Tyr"
  ],
  "2638G>T": [
    "No",
    "c.2506G>T",
    "D836Y",
    "7.10543518422025e-05",
    "2638G>T",
    "15",
    "Non CF-causing",
    "p.Asp836Tyr"
  ],
  "p.Asp836Tyr": [
    "No",
    "c.2506G>T",
    "D836Y",
    "7.10543518422025e-05",
    "2638G>T",
    "15",
    "Non CF-causing",
    "p.Asp836Tyr"
  ],
  "c.137C>A": [
    "c.137C>A",
    "269C>A",
    "No",
    "7.10543518422025e-05",
    "CF-causing",
    "15",
    "A46D",
    "p.Ala46Asp"
  ],
  "269C>A": [
    "c.137C>A",
    "269C>A",
    "No",
    "7.10543518422025e-05",
    "CF-causing",
    "15",
    "A46D",
    "p.Ala46Asp"
  ],
  "A46D": [
    "c.137C>A",
    "269C>A",
    "No",
    "7.10543518422025e-05",
    "CF-causing",
    "15",
    "A46D",
    "p.Ala46Asp"
  ],
  "p.Ala46Asp": [
    "c.137C>A",
    "269C>A",
    "No",
    "7.10543518422025e-05",
    "CF-causing",
    "15",
    "A46D",
    "p.Ala46Asp"
  ],
  "3173A>G": [
    "3173A>G",
    "c.3041A>G",
    "7.10543518422025e-05",
    "p.Tyr1014Cys",
    "Varying clinical consequence",
    "15",
    "Yes",
    "Unknown significance",
    "Y1014C"
  ],
  "c.3041A>G": [
    "3173A>G",
    "c.3041A>G",
    "7.10543518422025e-05",
    "p.Tyr1014Cys",
    "Varying clinical consequence",
    "15",
    "Yes",
    "Unknown significance",
    "Y1014C"
  ],
  "p.Tyr1014Cys": [
    "3173A>G",
    "c.3041A>G",
    "7.10543518422025e-05",
    "p.Tyr1014Cys",
    "Varying clinical consequence",
    "15",
    "Yes",
    "Unknown significance",
    "Y1014C"
  ],
  "Y1014C": [
    "3173A>G",
    "c.3041A>G",
    "7.10543518422025e-05",
    "p.Tyr1014Cys",
    "Varying clinical consequence",
    "15",
    "Yes",
    "Unknown significance",
    "Y1014C"
  ],
  "S1118F": [
    "S1118F",
    "3485C>T",
    "No",
    "p.Ser1118Phe",
    "7.10543518422025e-05",
    "c.3353C>T",
    "CF-causing",
    "15"
  ],
  "3485C>T": [
    "S1118F",
    "3485C>T",
    "No",
    "p.Ser1118Phe",
    "7.10543518422025e-05",
    "c.3353C>T",
    "CF-causing",
    "15"
  ],
  "p.Ser1118Phe": [
    "S1118F",
    "3485C>T",
    "No",
    "p.Ser1118Phe",
    "7.10543518422025e-05",
    "c.3353C>T",
    "CF-causing",
    "15"
  ],
  "c.3353C>T": [
    "S1118F",
    "3485C>T",
    "No",
    "p.Ser1118Phe",
    "7.10543518422025e-05",
    "c.3353C>T",
    "CF-causing",
    "15"
  ],
  "4256A>C": [
    "No",
    "7.10543518422025e-05",
    "4256A>C",
    "CF-causing",
    "15",
    "c.4124A>C",
    "H1375P",
    "p.His1375Pro"
  ],
  "c.4124A>C": [
    "No",
    "7.10543518422025e-05",
    "4256A>C",
    "CF-causing",
    "15",
    "c.4124A>C",
    "H1375P",
    "p.His1375Pro"
  ],
  "H1375P": [
    "No",
    "7.10543518422025e-05",
    "4256A>C",
    "CF-causing",
    "15",
    "c.4124A>C",
    "H1375P",
    "p.His1375Pro"
  ],
  "p.His1375Pro": [
    "No",
    "7.10543518422025e-05",
    "4256A>C",
    "CF-causing",
    "15",
    "c.4124A>C",
    "H1375P",
    "p.His1375Pro"
  ],
  "c.2859_2890del": [
    "c.2859_2890del",
    "No",
    "7.10543518422025e-05",
    "CF-causing",
    "15",
    "2991del32",
    "p.Leu953PhefsX11",
    "c.2859_2890del32"
  ],
  "2991del32": [
    "c.2859_2890del",
    "No",
    "7.10543518422025e-05",
    "CF-causing",
    "15",
    "2991del32",
    "p.Leu953PhefsX11",
    "c.2859_2890del32"
  ],
  "p.Leu953PhefsX11": [
    "c.2859_2890del",
    "No",
    "7.10543518422025e-05",
    "CF-causing",
    "15",
    "2991del32",
    "p.Leu953PhefsX11",
    "c.2859_2890del32"
  ],
  "c.2859_2890del32": [
    "c.2859_2890del",
    "No",
    "7.10543518422025e-05",
    "CF-causing",
    "15",
    "2991del32",
    "p.Leu953PhefsX11",
    "c.2859_2890del32"
  ],
  "W57X(TAG)|W57X(TGA)|302G>A|303G>A": [
    "No",
    "7.10543518422025e-05",
    "W57X(TAG)|W57X(TGA)|302G>A|303G>A",
    "CF-causing",
    "c.170G>A|c.171G>A",
    "W57X",
    "p.Trp57X",
    "15"
  ],
  "c.170G>A|c.171G>A": [
    "No",
    "7.10543518422025e-05",
    "W57X(TAG)|W57X(TGA)|302G>A|303G>A",
    "CF-causing",
    "c.170G>A|c.171G>A",
    "W57X",
    "p.Trp57X",
    "15"
  ],
  "W57X": [
    "No",
    "7.10543518422025e-05",
    "W57X(TAG)|W57X(TGA)|302G>A|303G>A",
    "CF-causing",
    "c.170G>A|c.171G>A",
    "W57X",
    "p.Trp57X",
    "15"
  ],
  "p.Trp57X": [
    "No",
    "7.10543518422025e-05",
    "W57X(TAG)|W57X(TGA)|302G>A|303G>A",
    "CF-causing",
    "c.170G>A|c.171G>A",
    "W57X",
    "p.Trp57X",
    "15"
  ],
  "c.2658-1G>C": [
    "p.?",
    "c.2658-1G>C",
    "No",
    "7.10543518422025e-05",
    "2790-1G->C",
    "CF-causing",
    "15"
  ],
  "2790-1G->C": [
    "p.?",
    "c.2658-1G>C",
    "No",
    "7.10543518422025e-05",
    "2790-1G->C",
    "CF-causing",
    "15"
  ],
  "c.164+1G>T": [
    "p.?",
    "No",
    "7.10543518422025e-05",
    "CF-causing",
    "15",
    "c.164+1G>T",
    "296+1G->T"
  ],
  "296+1G->T": [
    "p.?",
    "No",
    "7.10543518422025e-05",
    "CF-causing",
    "15",
    "c.164+1G>T",
    "296+1G->T"
  ],
  "c.3717+40A>G": [
    "p.?",
    "No",
    "7.10543518422025e-05",
    "c.3717+40A>G",
    "CF-causing",
    "15",
    "3849+40A->G"
  ],
  "3849+40A->G": [
    "p.?",
    "No",
    "7.10543518422025e-05",
    "c.3717+40A>G",
    "CF-causing",
    "15",
    "3849+40A->G"
  ],
  "405+3A->C": [
    "405+3A->C",
    "p.?",
    "c.273+3A>C",
    "No",
    "7.10543518422025e-05",
    "CF-causing",
    "15"
  ],
  "c.273+3A>C": [
    "405+3A->C",
    "p.?",
    "c.273+3A>C",
    "No",
    "7.10543518422025e-05",
    "CF-causing",
    "15"
  ],
  "3849+5G->A": [
    "p.?",
    "No",
    "7.10543518422025e-05",
    "CF-causing",
    "3849+5G->A",
    "15",
    "c.3717+5G>A"
  ],
  "c.3717+5G>A": [
    "p.?",
    "No",
    "7.10543518422025e-05",
    "CF-causing",
    "3849+5G->A",
    "15",
    "c.3717+5G>A"
  ],
  "c.1523T>G": [
    "c.1523T>G",
    "No",
    "1655T>G",
    "Non CF-causing",
    "6.631739505272233e-05",
    "p.Phe508Cys",
    "F508C",
    "14"
  ],
  "1655T>G": [
    "c.1523T>G",
    "No",
    "1655T>G",
    "Non CF-causing",
    "6.631739505272233e-05",
    "p.Phe508Cys",
    "F508C",
    "14"
  ],
  "6.631739505272233e-05": [
    "p.?",
    "No",
    "1249-1G->A",
    "CF-causing",
    "6.631739505272233e-05",
    "c.1117-1G>A",
    "14"
  ],
  "p.Phe508Cys": [
    "c.1523T>G",
    "No",
    "1655T>G",
    "Non CF-causing",
    "6.631739505272233e-05",
    "p.Phe508Cys",
    "F508C",
    "14"
  ],
  "F508C": [
    "c.1523T>G",
    "No",
    "1655T>G",
    "Non CF-causing",
    "6.631739505272233e-05",
    "p.Phe508Cys",
    "F508C",
    "14"
  ],
  "14": [
    "p.?",
    "No",
    "1249-1G->A",
    "CF-causing",
    "6.631739505272233e-05",
    "c.1117-1G>A",
    "14"
  ],
  "G622D": [
    "No",
    "G622D",
    "1997G>A",
    "Varying clinical consequence",
    "6.631739505272233e-05",
    "p.Gly622Asp",
    "c.1865G>A",
    "14"
  ],
  "1997G>A": [
    "No",
    "G622D",
    "1997G>A",
    "Varying clinical consequence",
    "6.631739505272233e-05",
    "p.Gly622Asp",
    "c.1865G>A",
    "14"
  ],
  "p.Gly622Asp": [
    "No",
    "G622D",
    "1997G>A",
    "Varying clinical consequence",
    "6.631739505272233e-05",
    "p.Gly622Asp",
    "c.1865G>A",
    "14"
  ],
  "c.1865G>A": [
    "No",
    "G622D",
    "1997G>A",
    "Varying clinical consequence",
    "6.631739505272233e-05",
    "p.Gly622Asp",
    "c.1865G>A",
    "14"
  ],
  "3235C>T": [
    "No",
    "3235C>T",
    "CF-causing",
    "p.Gln1035X",
    "Q1035X",
    "c.3103C>T",
    "6.631739505272233e-05",
    "14"
  ],
  "p.Gln1035X": [
    "No",
    "3235C>T",
    "CF-causing",
    "p.Gln1035X",
    "Q1035X",
    "c.3103C>T",
    "6.631739505272233e-05",
    "14"
  ],
  "Q1035X": [
    "No",
    "3235C>T",
    "CF-causing",
    "p.Gln1035X",
    "Q1035X",
    "c.3103C>T",
    "6.631739505272233e-05",
    "14"
  ],
  "c.3103C>T": [
    "No",
    "3235C>T",
    "CF-causing",
    "p.Gln1035X",
    "Q1035X",
    "c.3103C>T",
    "6.631739505272233e-05",
    "14"
  ],
  "c.(3468+1_3469-1)_(3717+1_3718-1)del": [
    "c.(3468+1_3469-1)_(3717+1_3718-1)del",
    "p.?",
    "No",
    "CF-causing",
    "deletion of exon 19 (legacy numbering)|deletion of exon 22 (current numbering)",
    "6.631739505272233e-05",
    "CFTRdele19",
    "14"
  ],
  "deletion of exon 19 (legacy numbering)|deletion of exon 22 (current numbering)": [
    "c.(3468+1_3469-1)_(3717+1_3718-1)del",
    "p.?",
    "No",
    "CF-causing",
    "deletion of exon 19 (legacy numbering)|deletion of exon 22 (current numbering)",
    "6.631739505272233e-05",
    "CFTRdele19",
    "14"
  ],
  "CFTRdele19": [
    "c.(3468+1_3469-1)_(3717+1_3718-1)del",
    "p.?",
    "No",
    "CF-causing",
    "deletion of exon 19 (legacy numbering)|deletion of exon 22 (current numbering)",
    "6.631739505272233e-05",
    "CFTRdele19",
    "14"
  ],
  "4374+1G->A": [
    "p.?",
    "No",
    "4374+1G->A",
    "CF-causing",
    "c.4242+1G>A",
    "6.631739505272233e-05",
    "14"
  ],
  "c.4242+1G>A": [
    "p.?",
    "No",
    "4374+1G->A",
    "CF-causing",
    "c.4242+1G>A",
    "6.631739505272233e-05",
    "14"
  ],
  "1249-1G->A": [
    "p.?",
    "No",
    "1249-1G->A",
    "CF-causing",
    "6.631739505272233e-05",
    "c.1117-1G>A",
    "14"
  ],
  "c.1117-1G>A": [
    "p.?",
    "No",
    "1249-1G->A",
    "CF-causing",
    "6.631739505272233e-05",
    "c.1117-1G>A",
    "14"
  ],
  "V470M": [
    "V470M",
    "No",
    "1540G>A",
    "13",
    "6.158043826324216e-05",
    "Non CF-causing",
    "p.Val470Met",
    "c.1408G>A"
  ],
  "1540G>A": [
    "V470M",
    "No",
    "1540G>A",
    "13",
    "6.158043826324216e-05",
    "Non CF-causing",
    "p.Val470Met",
    "c.1408G>A"
  ],
  "13": [
    "p.?",
    "No",
    "13",
    "6.158043826324216e-05",
    "Non CF-causing",
    "125G/C",
    "c.-8G>C"
  ],
  "6.158043826324216e-05": [
    "p.?",
    "No",
    "13",
    "6.158043826324216e-05",
    "Non CF-causing",
    "125G/C",
    "c.-8G>C"
  ],
  "p.Val470Met": [
    "V470M",
    "No",
    "1540G>A",
    "13",
    "6.158043826324216e-05",
    "Non CF-causing",
    "p.Val470Met",
    "c.1408G>A"
  ],
  "c.1408G>A": [
    "V470M",
    "No",
    "1540G>A",
    "13",
    "6.158043826324216e-05",
    "Non CF-causing",
    "p.Val470Met",
    "c.1408G>A"
  ],
  "c.79G>T": [
    "c.79G>T",
    "No",
    "13",
    "211G>T",
    "p.Gly27X",
    "CF-causing",
    "6.158043826324216e-05",
    "G27X"
  ],
  "211G>T": [
    "c.79G>T",
    "No",
    "13",
    "211G>T",
    "p.Gly27X",
    "CF-causing",
    "6.158043826324216e-05",
    "G27X"
  ],
  "p.Gly27X": [
    "c.79G>T",
    "No",
    "13",
    "211G>T",
    "p.Gly27X",
    "CF-causing",
    "6.158043826324216e-05",
    "G27X"
  ],
  "G27X": [
    "c.79G>T",
    "No",
    "13",
    "211G>T",
    "p.Gly27X",
    "CF-causing",
    "6.158043826324216e-05",
    "G27X"
  ],
  "p.Met1101Arg": [
    "p.Met1101Arg",
    "M1101R",
    "No",
    "13",
    "3434T>G",
    "CF-causing",
    "6.158043826324216e-05",
    "c.3302T>G"
  ],
  "M1101R": [
    "p.Met1101Arg",
    "M1101R",
    "No",
    "13",
    "3434T>G",
    "CF-causing",
    "6.158043826324216e-05",
    "c.3302T>G"
  ],
  "3434T>G": [
    "p.Met1101Arg",
    "M1101R",
    "No",
    "13",
    "3434T>G",
    "CF-causing",
    "6.158043826324216e-05",
    "c.3302T>G"
  ],
  "c.3302T>G": [
    "p.Met1101Arg",
    "M1101R",
    "No",
    "13",
    "3434T>G",
    "CF-causing",
    "6.158043826324216e-05",
    "c.3302T>G"
  ],
  "R1102X": [
    "R1102X",
    "No",
    "p.Arg1102X",
    "13",
    "3436A>T",
    "c.3304A>T",
    "CF-causing",
    "6.158043826324216e-05"
  ],
  "p.Arg1102X": [
    "R1102X",
    "No",
    "p.Arg1102X",
    "13",
    "3436A>T",
    "c.3304A>T",
    "CF-causing",
    "6.158043826324216e-05"
  ],
  "3436A>T": [
    "R1102X",
    "No",
    "p.Arg1102X",
    "13",
    "3436A>T",
    "c.3304A>T",
    "CF-causing",
    "6.158043826324216e-05"
  ],
  "c.3304A>T": [
    "R1102X",
    "No",
    "p.Arg1102X",
    "13",
    "3436A>T",
    "c.3304A>T",
    "CF-causing",
    "6.158043826324216e-05"
  ],
  "V201M": [
    "V201M",
    "13",
    "Varying clinical consequence",
    "c.601G>A",
    "6.158043826324216e-05",
    "Yes",
    "p.Val201Met",
    "733G>A",
    "Unknown significance"
  ],
  "c.601G>A": [
    "V201M",
    "13",
    "Varying clinical consequence",
    "c.601G>A",
    "6.158043826324216e-05",
    "Yes",
    "p.Val201Met",
    "733G>A",
    "Unknown significance"
  ],
  "p.Val201Met": [
    "V201M",
    "13",
    "Varying clinical consequence",
    "c.601G>A",
    "6.158043826324216e-05",
    "Yes",
    "p.Val201Met",
    "733G>A",
    "Unknown significance"
  ],
  "733G>A": [
    "V201M",
    "13",
    "Varying clinical consequence",
    "c.601G>A",
    "6.158043826324216e-05",
    "Yes",
    "p.Val201Met",
    "733G>A",
    "Unknown significance"
  ],
  "c.4296_4297insGA": [
    "c.4296_4297insGA",
    "No",
    "13",
    "p.Ser1435GlyfsX14",
    "CF-causing",
    "c.4300_4301dup",
    "6.158043826324216e-05",
    "4428insGA"
  ],
  "p.Ser1435GlyfsX14": [
    "c.4296_4297insGA",
    "No",
    "13",
    "p.Ser1435GlyfsX14",
    "CF-causing",
    "c.4300_4301dup",
    "6.158043826324216e-05",
    "4428insGA"
  ],
  "c.4300_4301dup": [
    "c.4296_4297insGA",
    "No",
    "13",
    "p.Ser1435GlyfsX14",
    "CF-causing",
    "c.4300_4301dup",
    "6.158043826324216e-05",
    "4428insGA"
  ],
  "4428insGA": [
    "c.4296_4297insGA",
    "No",
    "13",
    "p.Ser1435GlyfsX14",
    "CF-causing",
    "c.4300_4301dup",
    "6.158043826324216e-05",
    "4428insGA"
  ],
  "c.(?_1)_(53+1_54-1)del": [
    "p.?",
    "No",
    "c.(?_1)_(53+1_54-1)del",
    "13",
    "deletion of exon 1 (legacy and current numbering)|CFTRdelePr-1|deletion of part of the promoter and exon 1 (legacy and current numbering)",
    "CF-causing",
    "6.158043826324216e-05",
    "CFTRdele1"
  ],
  "deletion of exon 1 (legacy and current numbering)|CFTRdelePr-1|deletion of part of the promoter and exon 1 (legacy and current numbering)": [
    "p.?",
    "No",
    "c.(?_1)_(53+1_54-1)del",
    "13",
    "deletion of exon 1 (legacy and current numbering)|CFTRdelePr-1|deletion of part of the promoter and exon 1 (legacy and current numbering)",
    "CF-causing",
    "6.158043826324216e-05",
    "CFTRdele1"
  ],
  "CFTRdele1": [
    "p.?",
    "No",
    "c.(?_1)_(53+1_54-1)del",
    "13",
    "deletion of exon 1 (legacy and current numbering)|CFTRdelePr-1|deletion of part of the promoter and exon 1 (legacy and current numbering)",
    "CF-causing",
    "6.158043826324216e-05",
    "CFTRdele1"
  ],
  "deletion of exons 19 and 20 (legacy numbering)|deletion of exons 22 and 23 (current numbering)": [
    "p.?",
    "deletion of exons 19 and 20 (legacy numbering)|deletion of exons 22 and 23 (current numbering)",
    "Yes, new variant added",
    "13",
    "CF-causing",
    "6.158043826324216e-05",
    "CFTRdele19,20",
    "c.(3468+1_3469-1)_(3873+1_3874-1)del"
  ],
  "CFTRdele19,20": [
    "p.?",
    "deletion of exons 19 and 20 (legacy numbering)|deletion of exons 22 and 23 (current numbering)",
    "Yes, new variant added",
    "13",
    "CF-causing",
    "6.158043826324216e-05",
    "CFTRdele19,20",
    "c.(3468+1_3469-1)_(3873+1_3874-1)del"
  ],
  "c.(3468+1_3469-1)_(3873+1_3874-1)del": [
    "p.?",
    "deletion of exons 19 and 20 (legacy numbering)|deletion of exons 22 and 23 (current numbering)",
    "Yes, new variant added",
    "13",
    "CF-causing",
    "6.158043826324216e-05",
    "CFTRdele19,20",
    "c.(3468+1_3469-1)_(3873+1_3874-1)del"
  ],
  "875+1G->C": [
    "p.?",
    "No",
    "875+1G->C",
    "c.743+1G>C",
    "13",
    "CF-causing",
    "6.158043826324216e-05"
  ],
  "c.743+1G>C": [
    "p.?",
    "No",
    "875+1G->C",
    "c.743+1G>C",
    "13",
    "CF-causing",
    "6.158043826324216e-05"
  ],
  "1717-2A->G": [
    "p.?",
    "No",
    "1717-2A->G",
    "13",
    "CF-causing",
    "6.158043826324216e-05",
    "c.1585-2A>G"
  ],
  "c.1585-2A>G": [
    "p.?",
    "No",
    "1717-2A->G",
    "13",
    "CF-causing",
    "6.158043826324216e-05",
    "c.1585-2A>G"
  ],
  "c.1766+1G>T": [
    "p.?",
    "No",
    "c.1766+1G>T",
    "1898+1G->T",
    "13",
    "CF-causing",
    "6.158043826324216e-05"
  ],
  "1898+1G->T": [
    "p.?",
    "No",
    "c.1766+1G>T",
    "1898+1G->T",
    "13",
    "CF-causing",
    "6.158043826324216e-05"
  ],
  "557delT": [
    "No",
    "13",
    "557delT",
    "CF-causing",
    "c.429del",
    "6.158043826324216e-05",
    "p.Phe143LeufsX10"
  ],
  "c.429del": [
    "No",
    "13",
    "557delT",
    "CF-causing",
    "c.429del",
    "6.158043826324216e-05",
    "p.Phe143LeufsX10"
  ],
  "p.Phe143LeufsX10": [
    "No",
    "13",
    "557delT",
    "CF-causing",
    "c.429del",
    "6.158043826324216e-05",
    "p.Phe143LeufsX10"
  ],
  "2176insC": [
    "No",
    "13",
    "CF-causing",
    "2176insC",
    "6.158043826324216e-05",
    "c.2045dup",
    "p.Gln685ThrfsX4"
  ],
  "c.2045dup": [
    "No",
    "13",
    "CF-causing",
    "2176insC",
    "6.158043826324216e-05",
    "c.2045dup",
    "p.Gln685ThrfsX4"
  ],
  "c.2825del": [
    "No",
    "13",
    "c.2825del",
    "CF-causing",
    "6.158043826324216e-05",
    "2957delT",
    "p.Ile942ThrfsX26"
  ],
  "2957delT": [
    "No",
    "13",
    "c.2825del",
    "CF-causing",
    "6.158043826324216e-05",
    "2957delT",
    "p.Ile942ThrfsX26"
  ],
  "p.Ile942ThrfsX26": [
    "No",
    "13",
    "c.2825del",
    "CF-causing",
    "6.158043826324216e-05",
    "2957delT",
    "p.Ile942ThrfsX26"
  ],
  "125G/C": [
    "p.?",
    "No",
    "13",
    "6.158043826324216e-05",
    "Non CF-causing",
    "125G/C",
    "c.-8G>C"
  ],
  "c.-8G>C": [
    "p.?",
    "No",
    "13",
    "6.158043826324216e-05",
    "Non CF-causing",
    "125G/C",
    "c.-8G>C"
  ],
  "1459G>T": [
    "1459G>T",
    "c.1327G>T",
    "No",
    "Varying clinical consequence",
    "5.6843481473761994e-05",
    "p.Asp443Tyr",
    "D443Y",
    "12"
  ],
  "c.1327G>T": [
    "1459G>T",
    "c.1327G>T",
    "No",
    "Varying clinical consequence",
    "5.6843481473761994e-05",
    "p.Asp443Tyr",
    "D443Y",
    "12"
  ],
  "5.6843481473761994e-05": [
    "p.?",
    "Yes, new variant added",
    "622-1G->A",
    "5.6843481473761994e-05",
    "c.490-1G>A",
    "CF-causing",
    "12"
  ],
  "p.Asp443Tyr": [
    "1459G>T",
    "c.1327G>T",
    "No",
    "Varying clinical consequence",
    "5.6843481473761994e-05",
    "p.Asp443Tyr",
    "D443Y",
    "12"
  ],
  "D443Y": [
    "1459G>T",
    "c.1327G>T",
    "No",
    "Varying clinical consequence",
    "5.6843481473761994e-05",
    "p.Asp443Tyr",
    "D443Y",
    "12"
  ],
  "12": [
    "p.?",
    "Yes, new variant added",
    "622-1G->A",
    "5.6843481473761994e-05",
    "c.490-1G>A",
    "CF-causing",
    "12"
  ],
  "c.1487G>A": [
    "c.1487G>A",
    "No",
    "1619G>A",
    "5.6843481473761994e-05",
    "W496X",
    "p.Trp496X",
    "CF-causing",
    "12"
  ],
  "1619G>A": [
    "c.1487G>A",
    "No",
    "1619G>A",
    "5.6843481473761994e-05",
    "W496X",
    "p.Trp496X",
    "CF-causing",
    "12"
  ],
  "W496X": [
    "c.1487G>A",
    "No",
    "1619G>A",
    "5.6843481473761994e-05",
    "W496X",
    "p.Trp496X",
    "CF-causing",
    "12"
  ],
  "p.Trp496X": [
    "c.1487G>A",
    "No",
    "1619G>A",
    "5.6843481473761994e-05",
    "W496X",
    "p.Trp496X",
    "CF-causing",
    "12"
  ],
  "1812A>C": [
    "No",
    "1812A>C",
    "5.6843481473761994e-05",
    "R560S",
    "CF-causing",
    "c.1680A>C|c.1680A>T",
    "12",
    "p.Arg560Ser"
  ],
  "R560S": [
    "No",
    "1812A>C",
    "5.6843481473761994e-05",
    "R560S",
    "CF-causing",
    "c.1680A>C|c.1680A>T",
    "12",
    "p.Arg560Ser"
  ],
  "c.1680A>C|c.1680A>T": [
    "No",
    "1812A>C",
    "5.6843481473761994e-05",
    "R560S",
    "CF-causing",
    "c.1680A>C|c.1680A>T",
    "12",
    "p.Arg560Ser"
  ],
  "p.Arg560Ser": [
    "No",
    "1812A>C",
    "5.6843481473761994e-05",
    "R560S",
    "CF-causing",
    "c.1680A>C|c.1680A>T",
    "12",
    "p.Arg560Ser"
  ],
  "2987T>C": [
    "12",
    "2987T>C",
    "c.2855T>C",
    "Varying clinical consequence",
    "5.6843481473761994e-05",
    "Yes",
    "p.Met952Thr",
    "M952T",
    "Unknown significance"
  ],
  "c.2855T>C": [
    "12",
    "2987T>C",
    "c.2855T>C",
    "Varying clinical consequence",
    "5.6843481473761994e-05",
    "Yes",
    "p.Met952Thr",
    "M952T",
    "Unknown significance"
  ],
  "p.Met952Thr": [
    "12",
    "2987T>C",
    "c.2855T>C",
    "Varying clinical consequence",
    "5.6843481473761994e-05",
    "Yes",
    "p.Met952Thr",
    "M952T",
    "Unknown significance"
  ],
  "M952T": [
    "12",
    "2987T>C",
    "c.2855T>C",
    "Varying clinical consequence",
    "5.6843481473761994e-05",
    "Yes",
    "p.Met952Thr",
    "M952T",
    "Unknown significance"
  ],
  "p.Ala1004_Ala1006del": [
    "No",
    "p.Ala1004_Ala1006del",
    "c.3011_3019del",
    "5.6843481473761994e-05",
    "CF-causing",
    "3141del9",
    "12",
    "3143del9"
  ],
  "c.3011_3019del": [
    "No",
    "p.Ala1004_Ala1006del",
    "c.3011_3019del",
    "5.6843481473761994e-05",
    "CF-causing",
    "3141del9",
    "12",
    "3143del9"
  ],
  "3141del9": [
    "No",
    "p.Ala1004_Ala1006del",
    "c.3011_3019del",
    "5.6843481473761994e-05",
    "CF-causing",
    "3141del9",
    "12",
    "3143del9"
  ],
  "3143del9": [
    "No",
    "p.Ala1004_Ala1006del",
    "c.3011_3019del",
    "5.6843481473761994e-05",
    "CF-causing",
    "3141del9",
    "12",
    "3143del9"
  ],
  "p.Thr1053Ile": [
    "No",
    "p.Thr1053Ile",
    "c.3158C>T",
    "5.6843481473761994e-05",
    "Non CF-causing",
    "3290C>T",
    "12",
    "T1053I"
  ],
  "c.3158C>T": [
    "No",
    "p.Thr1053Ile",
    "c.3158C>T",
    "5.6843481473761994e-05",
    "Non CF-causing",
    "3290C>T",
    "12",
    "T1053I"
  ],
  "3290C>T": [
    "No",
    "p.Thr1053Ile",
    "c.3158C>T",
    "5.6843481473761994e-05",
    "Non CF-causing",
    "3290C>T",
    "12",
    "T1053I"
  ],
  "T1053I": [
    "No",
    "p.Thr1053Ile",
    "c.3158C>T",
    "5.6843481473761994e-05",
    "Non CF-causing",
    "3290C>T",
    "12",
    "T1053I"
  ],
  "c.3407_3422del": [
    "c.3407_3422del",
    "No",
    "p.Ala1136ValfsX7",
    "3539del16",
    "5.6843481473761994e-05",
    "CF-causing",
    "3407_3422del16",
    "CF-causing - previously called c.3407_3422del16 or 3407_3422del16",
    "12"
  ],
  "p.Ala1136ValfsX7": [
    "c.3407_3422del",
    "No",
    "p.Ala1136ValfsX7",
    "3539del16",
    "5.6843481473761994e-05",
    "CF-causing",
    "3407_3422del16",
    "CF-causing - previously called c.3407_3422del16 or 3407_3422del16",
    "12"
  ],
  "3539del16": [
    "c.3407_3422del",
    "No",
    "p.Ala1136ValfsX7",
    "3539del16",
    "5.6843481473761994e-05",
    "CF-causing",
    "3407_3422del16",
    "CF-causing - previously called c.3407_3422del16 or 3407_3422del16",
    "12"
  ],
  "3407_3422del16": [
    "CF-causing (now renamed 3539del16)",
    "(CF-causing under new name)",
    "3407_3422del16",
    "No, but renamed"
  ],
  "CF-causing - previously called c.3407_3422del16 or 3407_3422del16": [
    "c.3407_3422del",
    "No",
    "p.Ala1136ValfsX7",
    "3539del16",
    "5.6843481473761994e-05",
    "CF-causing",
    "3407_3422del16",
    "CF-causing - previously called c.3407_3422del16 or 3407_3422del16",
    "12"
  ],
  "c.3293G>A|c.3294G>A": [
    "c.3293G>A|c.3294G>A",
    "No",
    "3425G>A|3426G>A",
    "5.6843481473761994e-05",
    "CF-causing",
    "W1098X",
    "12",
    "p.Trp1098X"
  ],
  "3425G>A|3426G>A": [
    "c.3293G>A|c.3294G>A",
    "No",
    "3425G>A|3426G>A",
    "5.6843481473761994e-05",
    "CF-causing",
    "W1098X",
    "12",
    "p.Trp1098X"
  ],
  "W1098X": [
    "c.3293G>A|c.3294G>A",
    "No",
    "3425G>A|3426G>A",
    "5.6843481473761994e-05",
    "CF-causing",
    "W1098X",
    "12",
    "p.Trp1098X"
  ],
  "p.Trp1098X": [
    "c.3293G>A|c.3294G>A",
    "No",
    "3425G>A|3426G>A",
    "5.6843481473761994e-05",
    "CF-causing",
    "W1098X",
    "12",
    "p.Trp1098X"
  ],
  "p.Phe1099Leu": [
    "p.Phe1099Leu",
    "No",
    "F1099L",
    "3429C>A",
    "5.6843481473761994e-05",
    "Varying clinical consequence",
    "c.3297C>A",
    "12"
  ],
  "F1099L": [
    "p.Phe1099Leu",
    "No",
    "F1099L",
    "3429C>A",
    "5.6843481473761994e-05",
    "Varying clinical consequence",
    "c.3297C>A",
    "12"
  ],
  "3429C>A": [
    "p.Phe1099Leu",
    "No",
    "F1099L",
    "3429C>A",
    "5.6843481473761994e-05",
    "Varying clinical consequence",
    "c.3297C>A",
    "12"
  ],
  "c.3297C>A": [
    "p.Phe1099Leu",
    "No",
    "F1099L",
    "3429C>A",
    "5.6843481473761994e-05",
    "Varying clinical consequence",
    "c.3297C>A",
    "12"
  ],
  "Q1382X": [
    "Q1382X",
    "No",
    "5.6843481473761994e-05",
    "CF-causing",
    "p.Gln1382X",
    "4276C>T",
    "c.4144C>T",
    "12"
  ],
  "p.Gln1382X": [
    "Q1382X",
    "No",
    "5.6843481473761994e-05",
    "CF-causing",
    "p.Gln1382X",
    "4276C>T",
    "c.4144C>T",
    "12"
  ],
  "4276C>T": [
    "Q1382X",
    "No",
    "5.6843481473761994e-05",
    "CF-causing",
    "p.Gln1382X",
    "4276C>T",
    "c.4144C>T",
    "12"
  ],
  "c.4144C>T": [
    "Q1382X",
    "No",
    "5.6843481473761994e-05",
    "CF-causing",
    "p.Gln1382X",
    "4276C>T",
    "c.4144C>T",
    "12"
  ],
  "c.4234C>T": [
    "No",
    "c.4234C>T",
    "5.6843481473761994e-05",
    "CF-causing",
    "p.Gln1412X",
    "Q1412X",
    "12",
    "4366C>T"
  ],
  "p.Gln1412X": [
    "No",
    "c.4234C>T",
    "5.6843481473761994e-05",
    "CF-causing",
    "p.Gln1412X",
    "Q1412X",
    "12",
    "4366C>T"
  ],
  "Q1412X": [
    "No",
    "c.4234C>T",
    "5.6843481473761994e-05",
    "CF-causing",
    "p.Gln1412X",
    "Q1412X",
    "12",
    "4366C>T"
  ],
  "4366C>T": [
    "No",
    "c.4234C>T",
    "5.6843481473761994e-05",
    "CF-causing",
    "p.Gln1412X",
    "Q1412X",
    "12",
    "4366C>T"
  ],
  "p.Met284AsnfsX3": [
    "p.Met284AsnfsX3",
    "No",
    "982dupA",
    "c.850dup",
    "5.6843481473761994e-05",
    "CF-causing",
    "977insA",
    "12"
  ],
  "982dupA": [
    "p.Met284AsnfsX3",
    "No",
    "982dupA",
    "c.850dup",
    "5.6843481473761994e-05",
    "CF-causing",
    "977insA",
    "12"
  ],
  "c.850dup": [
    "p.Met284AsnfsX3",
    "No",
    "982dupA",
    "c.850dup",
    "5.6843481473761994e-05",
    "CF-causing",
    "977insA",
    "12"
  ],
  "977insA": [
    "p.Met284AsnfsX3",
    "No",
    "982dupA",
    "c.850dup",
    "5.6843481473761994e-05",
    "CF-causing",
    "977insA",
    "12"
  ],
  "L88X(T->G)|L88X(T->A)|395T>A|395T>G": [
    "L88X(T->G)|L88X(T->A)|395T>A|395T>G",
    "c.263T>A|c.263T>G",
    "No",
    "L88X",
    "p.Leu88X",
    "5.6843481473761994e-05",
    "CF-causing",
    "12"
  ],
  "c.263T>A|c.263T>G": [
    "L88X(T->G)|L88X(T->A)|395T>A|395T>G",
    "c.263T>A|c.263T>G",
    "No",
    "L88X",
    "p.Leu88X",
    "5.6843481473761994e-05",
    "CF-causing",
    "12"
  ],
  "L88X": [
    "L88X(T->G)|L88X(T->A)|395T>A|395T>G",
    "c.263T>A|c.263T>G",
    "No",
    "L88X",
    "p.Leu88X",
    "5.6843481473761994e-05",
    "CF-causing",
    "12"
  ],
  "p.Leu88X": [
    "L88X(T->G)|L88X(T->A)|395T>A|395T>G",
    "c.263T>A|c.263T>G",
    "No",
    "L88X",
    "p.Leu88X",
    "5.6843481473761994e-05",
    "CF-causing",
    "12"
  ],
  "1898+2T->C": [
    "p.?",
    "No",
    "1898+2T->C",
    "5.6843481473761994e-05",
    "CF-causing",
    "c.1766+2T>C",
    "12"
  ],
  "c.1766+2T>C": [
    "p.?",
    "No",
    "1898+2T->C",
    "5.6843481473761994e-05",
    "CF-causing",
    "c.1766+2T>C",
    "12"
  ],
  "c.168del": [
    "No",
    "c.168del",
    "300delA",
    "5.6843481473761994e-05",
    "CF-causing",
    "12",
    "p.Glu56AspfsX35"
  ],
  "300delA": [
    "No",
    "c.168del",
    "300delA",
    "5.6843481473761994e-05",
    "CF-causing",
    "12",
    "p.Glu56AspfsX35"
  ],
  "p.Glu56AspfsX35": [
    "No",
    "c.168del",
    "300delA",
    "5.6843481473761994e-05",
    "CF-causing",
    "12",
    "p.Glu56AspfsX35"
  ],
  "541delC": [
    "No",
    "541delC",
    "5.6843481473761994e-05",
    "c.409del",
    "CF-causing",
    "p.Leu137SerfsX16",
    "12"
  ],
  "c.409del": [
    "No",
    "541delC",
    "5.6843481473761994e-05",
    "c.409del",
    "CF-causing",
    "p.Leu137SerfsX16",
    "12"
  ],
  "p.Leu137SerfsX16": [
    "No",
    "541delC",
    "5.6843481473761994e-05",
    "c.409del",
    "CF-causing",
    "p.Leu137SerfsX16",
    "12"
  ],
  "622-1G->A": [
    "p.?",
    "Yes, new variant added",
    "622-1G->A",
    "5.6843481473761994e-05",
    "c.490-1G>A",
    "CF-causing",
    "12"
  ],
  "c.490-1G>A": [
    "p.?",
    "Yes, new variant added",
    "622-1G->A",
    "5.6843481473761994e-05",
    "c.490-1G>A",
    "CF-causing",
    "12"
  ],
  "p.Arg352Trp": [
    "p.Arg352Trp",
    "5.2106524684281827e-05",
    "No",
    "1186C>T",
    "Varying clinical consequence",
    "11",
    "R352W",
    "c.1054C>T"
  ],
  "5.2106524684281827e-05": [
    "p.?",
    "5.2106524684281827e-05",
    "2752-26A->G",
    "Non CF-causing",
    "Yes",
    "c.2620-26A>G",
    "11",
    "Unknown significance"
  ],
  "1186C>T": [
    "p.Arg352Trp",
    "5.2106524684281827e-05",
    "No",
    "1186C>T",
    "Varying clinical consequence",
    "11",
    "R352W",
    "c.1054C>T"
  ],
  "11": [
    "p.?",
    "5.2106524684281827e-05",
    "2752-26A->G",
    "Non CF-causing",
    "Yes",
    "c.2620-26A>G",
    "11",
    "Unknown significance"
  ],
  "R352W": [
    "p.Arg352Trp",
    "5.2106524684281827e-05",
    "No",
    "1186C>T",
    "Varying clinical consequence",
    "11",
    "R352W",
    "c.1054C>T"
  ],
  "c.1054C>T": [
    "p.Arg352Trp",
    "5.2106524684281827e-05",
    "No",
    "1186C>T",
    "Varying clinical consequence",
    "11",
    "R352W",
    "c.1054C>T"
  ],
  "G550X": [
    "5.2106524684281827e-05",
    "No",
    "CF-causing",
    "G550X",
    "c.1648G>T",
    "p.Gly550X",
    "11",
    "1780G>T"
  ],
  "c.1648G>T": [
    "5.2106524684281827e-05",
    "No",
    "CF-causing",
    "G550X",
    "c.1648G>T",
    "p.Gly550X",
    "11",
    "1780G>T"
  ],
  "p.Gly550X": [
    "5.2106524684281827e-05",
    "No",
    "CF-causing",
    "G550X",
    "c.1648G>T",
    "p.Gly550X",
    "11",
    "1780G>T"
  ],
  "1780G>T": [
    "5.2106524684281827e-05",
    "No",
    "CF-causing",
    "G550X",
    "c.1648G>T",
    "p.Gly550X",
    "11",
    "1780G>T"
  ],
  "E56K": [
    "5.2106524684281827e-05",
    "No",
    "11",
    "CF-causing",
    "E56K",
    "p.Glu56Lys",
    "c.166G>A",
    "298G>A"
  ],
  "p.Glu56Lys": [
    "5.2106524684281827e-05",
    "No",
    "11",
    "CF-causing",
    "E56K",
    "p.Glu56Lys",
    "c.166G>A",
    "298G>A"
  ],
  "c.166G>A": [
    "5.2106524684281827e-05",
    "No",
    "11",
    "CF-causing",
    "E56K",
    "p.Glu56Lys",
    "c.166G>A",
    "298G>A"
  ],
  "298G>A": [
    "5.2106524684281827e-05",
    "No",
    "11",
    "CF-causing",
    "E56K",
    "p.Glu56Lys",
    "c.166G>A",
    "298G>A"
  ],
  "p.Glu116Lys": [
    "5.2106524684281827e-05",
    "No",
    "p.Glu116Lys",
    "c.346G>A",
    "CF-causing",
    "478G>A",
    "11",
    "E116K"
  ],
  "c.346G>A": [
    "5.2106524684281827e-05",
    "No",
    "p.Glu116Lys",
    "c.346G>A",
    "CF-causing",
    "478G>A",
    "11",
    "E116K"
  ],
  "478G>A": [
    "5.2106524684281827e-05",
    "No",
    "p.Glu116Lys",
    "c.346G>A",
    "CF-causing",
    "478G>A",
    "11",
    "E116K"
  ],
  "E116K": [
    "5.2106524684281827e-05",
    "No",
    "p.Glu116Lys",
    "c.346G>A",
    "CF-causing",
    "478G>A",
    "11",
    "E116K"
  ],
  "481C>G": [
    "481C>G",
    "5.2106524684281827e-05",
    "No",
    "c.349C>G",
    "p.Arg117Gly",
    "Varying clinical consequence",
    "R117G",
    "11"
  ],
  "c.349C>G": [
    "481C>G",
    "5.2106524684281827e-05",
    "No",
    "c.349C>G",
    "p.Arg117Gly",
    "Varying clinical consequence",
    "R117G",
    "11"
  ],
  "p.Arg117Gly": [
    "481C>G",
    "5.2106524684281827e-05",
    "No",
    "c.349C>G",
    "p.Arg117Gly",
    "Varying clinical consequence",
    "R117G",
    "11"
  ],
  "R117G": [
    "481C>G",
    "5.2106524684281827e-05",
    "No",
    "c.349C>G",
    "p.Arg117Gly",
    "Varying clinical consequence",
    "R117G",
    "11"
  ],
  "c.416A>G": [
    "5.2106524684281827e-05",
    "No",
    "c.416A>G",
    "H139R",
    "CF-causing",
    "p.His139Arg",
    "548A>G",
    "11"
  ],
  "H139R": [
    "5.2106524684281827e-05",
    "No",
    "c.416A>G",
    "H139R",
    "CF-causing",
    "p.His139Arg",
    "548A>G",
    "11"
  ],
  "p.His139Arg": [
    "5.2106524684281827e-05",
    "No",
    "c.416A>G",
    "H139R",
    "CF-causing",
    "p.His139Arg",
    "548A>G",
    "11"
  ],
  "548A>G": [
    "5.2106524684281827e-05",
    "No",
    "c.416A>G",
    "H139R",
    "CF-causing",
    "p.His139Arg",
    "548A>G",
    "11"
  ],
  "709G>A": [
    "709G>A",
    "5.2106524684281827e-05",
    "c.577G>A",
    "No",
    "CF-causing",
    "p.Glu193Lys",
    "E193K",
    "11"
  ],
  "c.577G>A": [
    "709G>A",
    "5.2106524684281827e-05",
    "c.577G>A",
    "No",
    "CF-causing",
    "p.Glu193Lys",
    "E193K",
    "11"
  ],
  "p.Glu193Lys": [
    "709G>A",
    "5.2106524684281827e-05",
    "c.577G>A",
    "No",
    "CF-causing",
    "p.Glu193Lys",
    "E193K",
    "11"
  ],
  "E193K": [
    "709G>A",
    "5.2106524684281827e-05",
    "c.577G>A",
    "No",
    "CF-causing",
    "p.Glu193Lys",
    "E193K",
    "11"
  ],
  "c.581G>T": [
    "5.2106524684281827e-05",
    "No",
    "c.581G>T",
    "Varying clinical consequence",
    "G194V",
    "11",
    "p.Gly194Val",
    "713G>T"
  ],
  "G194V": [
    "5.2106524684281827e-05",
    "No",
    "c.581G>T",
    "Varying clinical consequence",
    "G194V",
    "11",
    "p.Gly194Val",
    "713G>T"
  ],
  "p.Gly194Val": [
    "5.2106524684281827e-05",
    "No",
    "c.581G>T",
    "Varying clinical consequence",
    "G194V",
    "11",
    "p.Gly194Val",
    "713G>T"
  ],
  "713G>T": [
    "5.2106524684281827e-05",
    "No",
    "c.581G>T",
    "Varying clinical consequence",
    "G194V",
    "11",
    "p.Gly194Val",
    "713G>T"
  ],
  "2594delGT": [
    "2594delGT",
    "5.2106524684281827e-05",
    "No",
    "c.2462_2463delGT",
    "c.2463_2464del",
    "CF-causing",
    "p.Ser821ArgfsX4",
    "11"
  ],
  "c.2462_2463delGT": [
    "2594delGT",
    "5.2106524684281827e-05",
    "No",
    "c.2462_2463delGT",
    "c.2463_2464del",
    "CF-causing",
    "p.Ser821ArgfsX4",
    "11"
  ],
  "c.2463_2464del": [
    "2594delGT",
    "5.2106524684281827e-05",
    "No",
    "c.2462_2463delGT",
    "c.2463_2464del",
    "CF-causing",
    "p.Ser821ArgfsX4",
    "11"
  ],
  "p.Ser821ArgfsX4": [
    "2594delGT",
    "5.2106524684281827e-05",
    "No",
    "c.2462_2463delGT",
    "c.2463_2464del",
    "CF-causing",
    "p.Ser821ArgfsX4",
    "11"
  ],
  "c.2763_2764dup": [
    "c.2763_2764dup",
    "2896insAG",
    "c.2764_2765insAGA",
    "5.2106524684281827e-05",
    "No",
    "CF-causing",
    "p.Val922GlufsX2",
    "11"
  ],
  "2896insAG": [
    "c.2763_2764dup",
    "2896insAG",
    "c.2764_2765insAGA",
    "5.2106524684281827e-05",
    "No",
    "CF-causing",
    "p.Val922GlufsX2",
    "11"
  ],
  "c.2764_2765insAGA": [
    "c.2763_2764dup",
    "2896insAG",
    "c.2764_2765insAGA",
    "5.2106524684281827e-05",
    "No",
    "CF-causing",
    "p.Val922GlufsX2",
    "11"
  ],
  "p.Val922GlufsX2": [
    "c.2763_2764dup",
    "2896insAG",
    "c.2764_2765insAGA",
    "5.2106524684281827e-05",
    "No",
    "CF-causing",
    "p.Val922GlufsX2",
    "11"
  ],
  "c.3891dup": [
    "c.3891dup",
    "5.2106524684281827e-05",
    "No",
    "CF-causing",
    "4022insT",
    "c.3890_3891insT",
    "11",
    "p.Gly1298TrpfsX4"
  ],
  "4022insT": [
    "c.3891dup",
    "5.2106524684281827e-05",
    "No",
    "CF-causing",
    "4022insT",
    "c.3890_3891insT",
    "11",
    "p.Gly1298TrpfsX4"
  ],
  "c.3890_3891insT": [
    "c.3891dup",
    "5.2106524684281827e-05",
    "No",
    "CF-causing",
    "4022insT",
    "c.3890_3891insT",
    "11",
    "p.Gly1298TrpfsX4"
  ],
  "p.Gly1298TrpfsX4": [
    "c.3891dup",
    "5.2106524684281827e-05",
    "No",
    "CF-causing",
    "4022insT",
    "c.3890_3891insT",
    "11",
    "p.Gly1298TrpfsX4"
  ],
  "175insT": [
    "175insT",
    "5.2106524684281827e-05",
    "No",
    "CF-causing",
    "c.50dup",
    "11",
    "p.Ser18GlnfsX27"
  ],
  "c.50dup": [
    "175insT",
    "5.2106524684281827e-05",
    "No",
    "CF-causing",
    "c.50dup",
    "11",
    "p.Ser18GlnfsX27"
  ],
  "p.Ser18GlnfsX27": [
    "175insT",
    "5.2106524684281827e-05",
    "No",
    "CF-causing",
    "c.50dup",
    "11",
    "p.Ser18GlnfsX27"
  ],
  "c.531dup": [
    "c.531dup",
    "5.2106524684281827e-05",
    "No",
    "p.Gly178TrpfsX5",
    "CF-causing",
    "663insT",
    "11"
  ],
  "p.Gly178TrpfsX5": [
    "c.531dup",
    "5.2106524684281827e-05",
    "No",
    "p.Gly178TrpfsX5",
    "CF-causing",
    "663insT",
    "11"
  ],
  "663insT": [
    "c.531dup",
    "5.2106524684281827e-05",
    "No",
    "p.Gly178TrpfsX5",
    "CF-causing",
    "663insT",
    "11"
  ],
  "2752-26A->G": [
    "p.?",
    "5.2106524684281827e-05",
    "2752-26A->G",
    "Non CF-causing",
    "Yes",
    "c.2620-26A>G",
    "11",
    "Unknown significance"
  ],
  "c.2620-26A>G": [
    "p.?",
    "5.2106524684281827e-05",
    "2752-26A->G",
    "Non CF-causing",
    "Yes",
    "c.2620-26A>G",
    "11",
    "Unknown significance"
  ],
  "Q353X": [
    "No",
    "Q353X",
    "10",
    "c.1057C>T",
    "p.Gln353X",
    "CF-causing",
    "1189C>T",
    "4.7369567894801666e-05"
  ],
  "10": [
    "p.?",
    "No",
    "10",
    "Non CF-causing",
    "9T",
    "c.1210-7_1210-6dup",
    "4.7369567894801666e-05"
  ],
  "c.1057C>T": [
    "No",
    "Q353X",
    "10",
    "c.1057C>T",
    "p.Gln353X",
    "CF-causing",
    "1189C>T",
    "4.7369567894801666e-05"
  ],
  "p.Gln353X": [
    "No",
    "Q353X",
    "10",
    "c.1057C>T",
    "p.Gln353X",
    "CF-causing",
    "1189C>T",
    "4.7369567894801666e-05"
  ],
  "1189C>T": [
    "No",
    "Q353X",
    "10",
    "c.1057C>T",
    "p.Gln353X",
    "CF-causing",
    "1189C>T",
    "4.7369567894801666e-05"
  ],
  "4.7369567894801666e-05": [
    "p.?",
    "No",
    "10",
    "Non CF-causing",
    "9T",
    "c.1210-7_1210-6dup",
    "4.7369567894801666e-05"
  ],
  "p.Gly404AspfsX38": [
    "p.Gly404AspfsX38",
    "c.1211del",
    "1342delG|c.1210delG",
    "No",
    "1343delG",
    "10",
    "CF-causing",
    "4.7369567894801666e-05"
  ],
  "c.1211del": [
    "p.Gly404AspfsX38",
    "c.1211del",
    "1342delG|c.1210delG",
    "No",
    "1343delG",
    "10",
    "CF-causing",
    "4.7369567894801666e-05"
  ],
  "1342delG|c.1210delG": [
    "p.Gly404AspfsX38",
    "c.1211del",
    "1342delG|c.1210delG",
    "No",
    "1343delG",
    "10",
    "CF-causing",
    "4.7369567894801666e-05"
  ],
  "1343delG": [
    "p.Gly404AspfsX38",
    "c.1211del",
    "1342delG|c.1210delG",
    "No",
    "1343delG",
    "10",
    "CF-causing",
    "4.7369567894801666e-05"
  ],
  "p.Asp513Gly": [
    "No",
    "p.Asp513Gly",
    "10",
    "c.1538A>G",
    "1670A>G",
    "CF-causing",
    "D513G",
    "4.7369567894801666e-05"
  ],
  "c.1538A>G": [
    "No",
    "p.Asp513Gly",
    "10",
    "c.1538A>G",
    "1670A>G",
    "CF-causing",
    "D513G",
    "4.7369567894801666e-05"
  ],
  "1670A>G": [
    "No",
    "p.Asp513Gly",
    "10",
    "c.1538A>G",
    "1670A>G",
    "CF-causing",
    "D513G",
    "4.7369567894801666e-05"
  ],
  "D513G": [
    "No",
    "p.Asp513Gly",
    "10",
    "c.1538A>G",
    "1670A>G",
    "CF-causing",
    "D513G",
    "4.7369567894801666e-05"
  ],
  "c.38C>T": [
    "No",
    "10",
    "CF-causing",
    "c.38C>T",
    "4.7369567894801666e-05",
    "170C>T",
    "S13F",
    "p.Ser13Phe"
  ],
  "170C>T": [
    "No",
    "10",
    "CF-causing",
    "c.38C>T",
    "4.7369567894801666e-05",
    "170C>T",
    "S13F",
    "p.Ser13Phe"
  ],
  "S13F": [
    "No",
    "10",
    "CF-causing",
    "c.38C>T",
    "4.7369567894801666e-05",
    "170C>T",
    "S13F",
    "p.Ser13Phe"
  ],
  "p.Ser13Phe": [
    "No",
    "10",
    "CF-causing",
    "c.38C>T",
    "4.7369567894801666e-05",
    "170C>T",
    "S13F",
    "p.Ser13Phe"
  ],
  "c.2601dup": [
    "No",
    "c.2601dup",
    "2732insA",
    "10",
    "CF-causing",
    "2733insA|c.2600_2601insA",
    "p.Val868SerfsX28",
    "4.7369567894801666e-05"
  ],
  "2732insA": [
    "No",
    "c.2601dup",
    "2732insA",
    "10",
    "CF-causing",
    "2733insA|c.2600_2601insA",
    "p.Val868SerfsX28",
    "4.7369567894801666e-05"
  ],
  "2733insA|c.2600_2601insA": [
    "No",
    "c.2601dup",
    "2732insA",
    "10",
    "CF-causing",
    "2733insA|c.2600_2601insA",
    "p.Val868SerfsX28",
    "4.7369567894801666e-05"
  ],
  "p.Val868SerfsX28": [
    "No",
    "c.2601dup",
    "2732insA",
    "10",
    "CF-causing",
    "2733insA|c.2600_2601insA",
    "p.Val868SerfsX28",
    "4.7369567894801666e-05"
  ],
  "c.3745G>A|c.3745G>C": [
    "No",
    "c.3745G>A|c.3745G>C",
    "G1249R",
    "10",
    "CF-causing",
    "3877G>A",
    "4.7369567894801666e-05",
    "p.Gly1249Arg"
  ],
  "G1249R": [
    "No",
    "c.3745G>A|c.3745G>C",
    "G1249R",
    "10",
    "CF-causing",
    "3877G>A",
    "4.7369567894801666e-05",
    "p.Gly1249Arg"
  ],
  "3877G>A": [
    "No",
    "c.3745G>A|c.3745G>C",
    "G1249R",
    "10",
    "CF-causing",
    "3877G>A",
    "4.7369567894801666e-05",
    "p.Gly1249Arg"
  ],
  "p.Gly1249Arg": [
    "No",
    "c.3745G>A|c.3745G>C",
    "G1249R",
    "10",
    "CF-causing",
    "3877G>A",
    "4.7369567894801666e-05",
    "p.Gly1249Arg"
  ],
  "4120C>T": [
    "4120C>T",
    "No",
    "10",
    "p.Gln1330X",
    "c.3988C>T",
    "CF-causing",
    "Q1330X",
    "4.7369567894801666e-05"
  ],
  "p.Gln1330X": [
    "4120C>T",
    "No",
    "10",
    "p.Gln1330X",
    "c.3988C>T",
    "CF-causing",
    "Q1330X",
    "4.7369567894801666e-05"
  ],
  "c.3988C>T": [
    "4120C>T",
    "No",
    "10",
    "p.Gln1330X",
    "c.3988C>T",
    "CF-causing",
    "Q1330X",
    "4.7369567894801666e-05"
  ],
  "Q1330X": [
    "4120C>T",
    "No",
    "10",
    "p.Gln1330X",
    "c.3988C>T",
    "CF-causing",
    "Q1330X",
    "4.7369567894801666e-05"
  ],
  "c.4097T>A": [
    "No",
    "c.4097T>A",
    "10",
    "p.Ile1366Asn",
    "CF-causing",
    "I1366N",
    "4229T>A",
    "4.7369567894801666e-05"
  ],
  "p.Ile1366Asn": [
    "No",
    "c.4097T>A",
    "10",
    "p.Ile1366Asn",
    "CF-causing",
    "I1366N",
    "4229T>A",
    "4.7369567894801666e-05"
  ],
  "I1366N": [
    "No",
    "c.4097T>A",
    "10",
    "p.Ile1366Asn",
    "CF-causing",
    "I1366N",
    "4229T>A",
    "4.7369567894801666e-05"
  ],
  "4229T>A": [
    "No",
    "c.4097T>A",
    "10",
    "p.Ile1366Asn",
    "CF-causing",
    "I1366N",
    "4229T>A",
    "4.7369567894801666e-05"
  ],
  "c.571T>G": [
    "c.571T>G",
    "F191V",
    "p.Phe191Val",
    "No",
    "10",
    "CF-causing",
    "703T>G",
    "4.7369567894801666e-05"
  ],
  "F191V": [
    "c.571T>G",
    "F191V",
    "p.Phe191Val",
    "No",
    "10",
    "CF-causing",
    "703T>G",
    "4.7369567894801666e-05"
  ],
  "p.Phe191Val": [
    "c.571T>G",
    "F191V",
    "p.Phe191Val",
    "No",
    "10",
    "CF-causing",
    "703T>G",
    "4.7369567894801666e-05"
  ],
  "703T>G": [
    "c.571T>G",
    "F191V",
    "p.Phe191Val",
    "No",
    "10",
    "CF-causing",
    "703T>G",
    "4.7369567894801666e-05"
  ],
  "D192G": [
    "D192G",
    "No",
    "10",
    "CF-causing",
    "p.Asp192Gly",
    "707A>G",
    "c.575A>G",
    "4.7369567894801666e-05"
  ],
  "p.Asp192Gly": [
    "D192G",
    "No",
    "10",
    "CF-causing",
    "p.Asp192Gly",
    "707A>G",
    "c.575A>G",
    "4.7369567894801666e-05"
  ],
  "707A>G": [
    "D192G",
    "No",
    "10",
    "CF-causing",
    "p.Asp192Gly",
    "707A>G",
    "c.575A>G",
    "4.7369567894801666e-05"
  ],
  "c.575A>G": [
    "D192G",
    "No",
    "10",
    "CF-causing",
    "p.Asp192Gly",
    "707A>G",
    "c.575A>G",
    "4.7369567894801666e-05"
  ],
  "2185insC": [
    "No",
    "2185insC",
    "10",
    "CF-causing",
    "c.2053_2054insC",
    "p.Gln685ProfsX4",
    "4.7369567894801666e-05",
    "c.2053dup"
  ],
  "c.2053_2054insC": [
    "No",
    "2185insC",
    "10",
    "CF-causing",
    "c.2053_2054insC",
    "p.Gln685ProfsX4",
    "4.7369567894801666e-05",
    "c.2053dup"
  ],
  "p.Gln685ProfsX4": [
    "No",
    "2185insC",
    "10",
    "CF-causing",
    "c.2053_2054insC",
    "p.Gln685ProfsX4",
    "4.7369567894801666e-05",
    "c.2053dup"
  ],
  "c.2053dup": [
    "No",
    "2185insC",
    "10",
    "CF-causing",
    "c.2053_2054insC",
    "p.Gln685ProfsX4",
    "4.7369567894801666e-05",
    "c.2053dup"
  ],
  "c.3039dup": [
    "No",
    "c.3039dup",
    "10",
    "3171insC",
    "CF-causing",
    "c.3039_3040insC",
    "p.Tyr1014LeufsX33",
    "4.7369567894801666e-05"
  ],
  "3171insC": [
    "No",
    "c.3039dup",
    "10",
    "3171insC",
    "CF-causing",
    "c.3039_3040insC",
    "p.Tyr1014LeufsX33",
    "4.7369567894801666e-05"
  ],
  "c.3039_3040insC": [
    "No",
    "c.3039dup",
    "10",
    "3171insC",
    "CF-causing",
    "c.3039_3040insC",
    "p.Tyr1014LeufsX33",
    "4.7369567894801666e-05"
  ],
  "p.Tyr1014LeufsX33": [
    "No",
    "c.3039dup",
    "10",
    "3171insC",
    "CF-causing",
    "c.3039_3040insC",
    "p.Tyr1014LeufsX33",
    "4.7369567894801666e-05"
  ],
  "deletion of exon 11 (legacy numbering)|deletion of exon 12 (current numbering)": [
    "deletion of exon 11 (legacy numbering)|deletion of exon 12 (current numbering)",
    "p.?",
    "c.(1584+1_1585-1)_(1679+1_1680-1)del",
    "No",
    "10",
    "CF-causing",
    "CFTRdele11",
    "4.7369567894801666e-05"
  ],
  "c.(1584+1_1585-1)_(1679+1_1680-1)del": [
    "deletion of exon 11 (legacy numbering)|deletion of exon 12 (current numbering)",
    "p.?",
    "c.(1584+1_1585-1)_(1679+1_1680-1)del",
    "No",
    "10",
    "CF-causing",
    "CFTRdele11",
    "4.7369567894801666e-05"
  ],
  "CFTRdele11": [
    "deletion of exon 11 (legacy numbering)|deletion of exon 12 (current numbering)",
    "p.?",
    "c.(1584+1_1585-1)_(1679+1_1680-1)del",
    "No",
    "10",
    "CF-causing",
    "CFTRdele11",
    "4.7369567894801666e-05"
  ],
  "CFTRdele9": [
    "p.?",
    "CFTRdele9",
    "Yes, new variant added",
    "10",
    "c.(1209+1_1210-1)_(1392+1_1393-1)del",
    "CF-causing",
    "deletion of exon 9 (legacy numbering)|deletion of exon 10 (current numbering)",
    "4.7369567894801666e-05"
  ],
  "c.(1209+1_1210-1)_(1392+1_1393-1)del": [
    "p.?",
    "CFTRdele9",
    "Yes, new variant added",
    "10",
    "c.(1209+1_1210-1)_(1392+1_1393-1)del",
    "CF-causing",
    "deletion of exon 9 (legacy numbering)|deletion of exon 10 (current numbering)",
    "4.7369567894801666e-05"
  ],
  "deletion of exon 9 (legacy numbering)|deletion of exon 10 (current numbering)": [
    "p.?",
    "CFTRdele9",
    "Yes, new variant added",
    "10",
    "c.(1209+1_1210-1)_(1392+1_1393-1)del",
    "CF-causing",
    "deletion of exon 9 (legacy numbering)|deletion of exon 10 (current numbering)",
    "4.7369567894801666e-05"
  ],
  "deletion of exons 4, 5, 6a, 6b, and 7 (legacy numbering)|deletion of exons 4, 5, 6, 7, and 8 (current numbering)": [
    "p.?",
    "No",
    "10",
    "CF-causing",
    "deletion of exons 4, 5, 6a, 6b, and 7 (legacy numbering)|deletion of exons 4, 5, 6, 7, and 8 (current numbering)",
    "CFTRdele4-7",
    "c.(273+1_274-1)_(1116+1_1117-1)del",
    "4.7369567894801666e-05"
  ],
  "CFTRdele4-7": [
    "p.?",
    "No",
    "10",
    "CF-causing",
    "deletion of exons 4, 5, 6a, 6b, and 7 (legacy numbering)|deletion of exons 4, 5, 6, 7, and 8 (current numbering)",
    "CFTRdele4-7",
    "c.(273+1_274-1)_(1116+1_1117-1)del",
    "4.7369567894801666e-05"
  ],
  "c.(273+1_274-1)_(1116+1_1117-1)del": [
    "p.?",
    "No",
    "10",
    "CF-causing",
    "deletion of exons 4, 5, 6a, 6b, and 7 (legacy numbering)|deletion of exons 4, 5, 6, 7, and 8 (current numbering)",
    "CFTRdele4-7",
    "c.(273+1_274-1)_(1116+1_1117-1)del",
    "4.7369567894801666e-05"
  ],
  "c.(3963+1_3964-1)_(4136+1_4137-1)dup": [
    "p.?",
    "Yes, new variant added",
    "10",
    "c.(3963+1_3964-1)_(4136+1_4137-1)dup",
    "CF-causing",
    "4.7369567894801666e-05",
    "duplication of exon 22 (legacy numbering)|duplication of exon 25 (current numbering)",
    "CFTRdup22"
  ],
  "duplication of exon 22 (legacy numbering)|duplication of exon 25 (current numbering)": [
    "p.?",
    "Yes, new variant added",
    "10",
    "c.(3963+1_3964-1)_(4136+1_4137-1)dup",
    "CF-causing",
    "4.7369567894801666e-05",
    "duplication of exon 22 (legacy numbering)|duplication of exon 25 (current numbering)",
    "CFTRdup22"
  ],
  "CFTRdup22": [
    "p.?",
    "Yes, new variant added",
    "10",
    "c.(3963+1_3964-1)_(4136+1_4137-1)dup",
    "CF-causing",
    "4.7369567894801666e-05",
    "duplication of exon 22 (legacy numbering)|duplication of exon 25 (current numbering)",
    "CFTRdup22"
  ],
  "1811+1G->A": [
    "p.?",
    "No",
    "1811+1G->A",
    "10",
    "CF-causing",
    "4.7369567894801666e-05",
    "c.1679+1G>A"
  ],
  "c.1679+1G>A": [
    "p.?",
    "No",
    "1811+1G->A",
    "10",
    "CF-causing",
    "4.7369567894801666e-05",
    "c.1679+1G>A"
  ],
  "297-1G->A": [
    "p.?",
    "No",
    "297-1G->A",
    "10",
    "c.165-1G>A",
    "CF-causing",
    "4.7369567894801666e-05"
  ],
  "c.165-1G>A": [
    "p.?",
    "No",
    "297-1G->A",
    "10",
    "c.165-1G>A",
    "CF-causing",
    "4.7369567894801666e-05"
  ],
  "p.Leu941GlnfsX27": [
    "No",
    "p.Leu941GlnfsX27",
    "10",
    "CF-causing",
    "2954delT",
    "c.2822del",
    "4.7369567894801666e-05"
  ],
  "2954delT": [
    "No",
    "p.Leu941GlnfsX27",
    "10",
    "CF-causing",
    "2954delT",
    "c.2822del",
    "4.7369567894801666e-05"
  ],
  "c.2822del": [
    "No",
    "p.Leu941GlnfsX27",
    "10",
    "CF-causing",
    "2954delT",
    "c.2822del",
    "4.7369567894801666e-05"
  ],
  "c.409_412del": [
    "c.409_412del",
    "No",
    "10",
    "CF-causing",
    "p.Leu137TyrfsX15",
    "541del4",
    "4.7369567894801666e-05"
  ],
  "p.Leu137TyrfsX15": [
    "c.409_412del",
    "No",
    "10",
    "CF-causing",
    "p.Leu137TyrfsX15",
    "541del4",
    "4.7369567894801666e-05"
  ],
  "541del4": [
    "c.409_412del",
    "No",
    "10",
    "CF-causing",
    "p.Leu137TyrfsX15",
    "541del4",
    "4.7369567894801666e-05"
  ],
  "3028delA": [
    "3028delA",
    "No",
    "10",
    "CF-causing",
    "c.2896del",
    "p.Thr966ArgfsX2",
    "4.7369567894801666e-05"
  ],
  "c.2896del": [
    "3028delA",
    "No",
    "10",
    "CF-causing",
    "c.2896del",
    "p.Thr966ArgfsX2",
    "4.7369567894801666e-05"
  ],
  "p.Thr966ArgfsX2": [
    "3028delA",
    "No",
    "10",
    "CF-causing",
    "c.2896del",
    "p.Thr966ArgfsX2",
    "4.7369567894801666e-05"
  ],
  "c.1703del": [
    "c.1703del",
    "No",
    "10",
    "p.Leu568CysfsX4",
    "CF-causing",
    "1833delT",
    "4.7369567894801666e-05"
  ],
  "p.Leu568CysfsX4": [
    "c.1703del",
    "No",
    "10",
    "p.Leu568CysfsX4",
    "CF-causing",
    "1833delT",
    "4.7369567894801666e-05"
  ],
  "1833delT": [
    "c.1703del",
    "No",
    "10",
    "p.Leu568CysfsX4",
    "CF-causing",
    "1833delT",
    "4.7369567894801666e-05"
  ],
  "c.3229_3230del": [
    "No",
    "10",
    "CF-causing",
    "c.3229_3230del",
    "p.Leu1077ValfsX78",
    "3359delCT",
    "4.7369567894801666e-05"
  ],
  "p.Leu1077ValfsX78": [
    "No",
    "10",
    "CF-causing",
    "c.3229_3230del",
    "p.Leu1077ValfsX78",
    "3359delCT",
    "4.7369567894801666e-05"
  ],
  "3359delCT": [
    "No",
    "10",
    "CF-causing",
    "c.3229_3230del",
    "p.Leu1077ValfsX78",
    "3359delCT",
    "4.7369567894801666e-05"
  ],
  "1002-2A->G": [
    "p.?",
    "Yes, new variant added",
    "10",
    "1002-2A->G",
    "CF-causing",
    "c.870-2A>G",
    "4.7369567894801666e-05"
  ],
  "c.870-2A>G": [
    "p.?",
    "Yes, new variant added",
    "10",
    "1002-2A->G",
    "CF-causing",
    "c.870-2A>G",
    "4.7369567894801666e-05"
  ],
  "9T": [
    "p.?",
    "No",
    "10",
    "Non CF-causing",
    "9T",
    "c.1210-7_1210-6dup",
    "4.7369567894801666e-05"
  ],
  "c.1210-7_1210-6dup": [
    "p.?",
    "No",
    "10",
    "Non CF-causing",
    "9T",
    "c.1210-7_1210-6dup",
    "4.7369567894801666e-05"
  ],
  "p.Gly314Glu": [
    "No",
    "p.Gly314Glu",
    "9",
    "Varying clinical consequence",
    "c.941G>A",
    "1073G>A",
    "G314E",
    "4.26326111053215e-05"
  ],
  "9": [
    "c.164+28A>G",
    "p.?",
    "296+28A->G",
    "9",
    "Varying clinical consequence",
    "Yes",
    "4.26326111053215e-05",
    "Unknown significance"
  ],
  "c.941G>A": [
    "No",
    "p.Gly314Glu",
    "9",
    "Varying clinical consequence",
    "c.941G>A",
    "1073G>A",
    "G314E",
    "4.26326111053215e-05"
  ],
  "1073G>A": [
    "No",
    "p.Gly314Glu",
    "9",
    "Varying clinical consequence",
    "c.941G>A",
    "1073G>A",
    "G314E",
    "4.26326111053215e-05"
  ],
  "G314E": [
    "No",
    "p.Gly314Glu",
    "9",
    "Varying clinical consequence",
    "c.941G>A",
    "1073G>A",
    "G314E",
    "4.26326111053215e-05"
  ],
  "4.26326111053215e-05": [
    "c.164+28A>G",
    "p.?",
    "296+28A->G",
    "9",
    "Varying clinical consequence",
    "Yes",
    "4.26326111053215e-05",
    "Unknown significance"
  ],
  "c.958T>G": [
    "No",
    "c.958T>G",
    "9",
    "Non CF-causing",
    "p.Leu320Val",
    "L320V",
    "4.26326111053215e-05",
    "1090T>G"
  ],
  "p.Leu320Val": [
    "No",
    "c.958T>G",
    "9",
    "Non CF-causing",
    "p.Leu320Val",
    "L320V",
    "4.26326111053215e-05",
    "1090T>G"
  ],
  "L320V": [
    "No",
    "c.958T>G",
    "9",
    "Non CF-causing",
    "p.Leu320Val",
    "L320V",
    "4.26326111053215e-05",
    "1090T>G"
  ],
  "1090T>G": [
    "No",
    "c.958T>G",
    "9",
    "Non CF-causing",
    "p.Leu320Val",
    "L320V",
    "4.26326111053215e-05",
    "1090T>G"
  ],
  "p.Gln359Arg": [
    "p.Gln359Arg",
    "c.1076A>G",
    "9",
    "Varying clinical consequence",
    "CF-causing",
    "1208A>G",
    "Yes",
    "4.26326111053215e-05",
    "Q359R"
  ],
  "c.1076A>G": [
    "p.Gln359Arg",
    "c.1076A>G",
    "9",
    "Varying clinical consequence",
    "CF-causing",
    "1208A>G",
    "Yes",
    "4.26326111053215e-05",
    "Q359R"
  ],
  "1208A>G": [
    "p.Gln359Arg",
    "c.1076A>G",
    "9",
    "Varying clinical consequence",
    "CF-causing",
    "1208A>G",
    "Yes",
    "4.26326111053215e-05",
    "Q359R"
  ],
  "Q359R": [
    "p.Gln359Arg",
    "c.1076A>G",
    "9",
    "Varying clinical consequence",
    "CF-causing",
    "1208A>G",
    "Yes",
    "4.26326111053215e-05",
    "Q359R"
  ],
  "R516G": [
    "No",
    "9",
    "R516G",
    "1678A>G",
    "CF-causing",
    "c.1546A>G",
    "p.Arg516Gly",
    "4.26326111053215e-05"
  ],
  "1678A>G": [
    "No",
    "9",
    "R516G",
    "1678A>G",
    "CF-causing",
    "c.1546A>G",
    "p.Arg516Gly",
    "4.26326111053215e-05"
  ],
  "c.1546A>G": [
    "No",
    "9",
    "R516G",
    "1678A>G",
    "CF-causing",
    "c.1546A>G",
    "p.Arg516Gly",
    "4.26326111053215e-05"
  ],
  "p.Arg516Gly": [
    "No",
    "9",
    "R516G",
    "1678A>G",
    "CF-causing",
    "c.1546A>G",
    "p.Arg516Gly",
    "4.26326111053215e-05"
  ],
  "2068G>T": [
    "2068G>T",
    "No",
    "p.Gly646X",
    "9",
    "CF-causing",
    "4.26326111053215e-05",
    "c.1936G>T",
    "G646X"
  ],
  "p.Gly646X": [
    "2068G>T",
    "No",
    "p.Gly646X",
    "9",
    "CF-causing",
    "4.26326111053215e-05",
    "c.1936G>T",
    "G646X"
  ],
  "c.1936G>T": [
    "2068G>T",
    "No",
    "p.Gly646X",
    "9",
    "CF-causing",
    "4.26326111053215e-05",
    "c.1936G>T",
    "G646X"
  ],
  "G646X": [
    "2068G>T",
    "No",
    "p.Gly646X",
    "9",
    "CF-causing",
    "4.26326111053215e-05",
    "c.1936G>T",
    "G646X"
  ],
  "R933G": [
    "R933G",
    "No",
    "2929A>G",
    "p.Arg933Gly",
    "9",
    "Varying clinical consequence",
    "c.2797A>G",
    "4.26326111053215e-05"
  ],
  "2929A>G": [
    "R933G",
    "No",
    "2929A>G",
    "p.Arg933Gly",
    "9",
    "Varying clinical consequence",
    "c.2797A>G",
    "4.26326111053215e-05"
  ],
  "p.Arg933Gly": [
    "R933G",
    "No",
    "2929A>G",
    "p.Arg933Gly",
    "9",
    "Varying clinical consequence",
    "c.2797A>G",
    "4.26326111053215e-05"
  ],
  "c.2797A>G": [
    "R933G",
    "No",
    "2929A>G",
    "p.Arg933Gly",
    "9",
    "Varying clinical consequence",
    "c.2797A>G",
    "4.26326111053215e-05"
  ],
  "p.Gln1042X": [
    "p.Gln1042X",
    "No",
    "9",
    "CF-causing",
    "Q1042X",
    "4.26326111053215e-05",
    "c.3124C>T",
    "3256C>T"
  ],
  "Q1042X": [
    "p.Gln1042X",
    "No",
    "9",
    "CF-causing",
    "Q1042X",
    "4.26326111053215e-05",
    "c.3124C>T",
    "3256C>T"
  ],
  "c.3124C>T": [
    "p.Gln1042X",
    "No",
    "9",
    "CF-causing",
    "Q1042X",
    "4.26326111053215e-05",
    "c.3124C>T",
    "3256C>T"
  ],
  "3256C>T": [
    "p.Gln1042X",
    "No",
    "9",
    "CF-causing",
    "Q1042X",
    "4.26326111053215e-05",
    "c.3124C>T",
    "3256C>T"
  ],
  "c.310del": [
    "c.310del",
    "No",
    "9",
    "CF-causing",
    "p.Arg104GlufsX3",
    "442delA",
    "441delA",
    "4.26326111053215e-05"
  ],
  "p.Arg104GlufsX3": [
    "c.310del",
    "No",
    "9",
    "CF-causing",
    "p.Arg104GlufsX3",
    "442delA",
    "441delA",
    "4.26326111053215e-05"
  ],
  "442delA": [
    "c.310del",
    "No",
    "9",
    "CF-causing",
    "p.Arg104GlufsX3",
    "442delA",
    "441delA",
    "4.26326111053215e-05"
  ],
  "441delA": [
    "c.310del",
    "No",
    "9",
    "CF-causing",
    "p.Arg104GlufsX3",
    "442delA",
    "441delA",
    "4.26326111053215e-05"
  ],
  "904A>G": [
    "904A>G",
    "c.772A>G",
    "No",
    "9",
    "Varying clinical consequence",
    "p.Arg258Gly",
    "4.26326111053215e-05",
    "R258G"
  ],
  "c.772A>G": [
    "904A>G",
    "c.772A>G",
    "No",
    "9",
    "Varying clinical consequence",
    "p.Arg258Gly",
    "4.26326111053215e-05",
    "R258G"
  ],
  "p.Arg258Gly": [
    "904A>G",
    "c.772A>G",
    "No",
    "9",
    "Varying clinical consequence",
    "p.Arg258Gly",
    "4.26326111053215e-05",
    "R258G"
  ],
  "R258G": [
    "904A>G",
    "c.772A>G",
    "No",
    "9",
    "Varying clinical consequence",
    "p.Arg258Gly",
    "4.26326111053215e-05",
    "R258G"
  ],
  "p.Lys1363X": [
    "No",
    "p.Lys1363X",
    "c.4086_4087insT",
    "9",
    "CF-causing",
    "4.26326111053215e-05",
    "c.4086dup",
    "4218insT"
  ],
  "c.4086_4087insT": [
    "No",
    "p.Lys1363X",
    "c.4086_4087insT",
    "9",
    "CF-causing",
    "4.26326111053215e-05",
    "c.4086dup",
    "4218insT"
  ],
  "c.4086dup": [
    "No",
    "p.Lys1363X",
    "c.4086_4087insT",
    "9",
    "CF-causing",
    "4.26326111053215e-05",
    "c.4086dup",
    "4218insT"
  ],
  "4218insT": [
    "No",
    "p.Lys1363X",
    "c.4086_4087insT",
    "9",
    "CF-causing",
    "4.26326111053215e-05",
    "c.4086dup",
    "4218insT"
  ],
  "c.[(164+1_165-1)_(1584+1_1585-1)del;(2619+1_2620-1)_(2988+1_2989-1)del]": [
    "c.[(164+1_165-1)_(1584+1_1585-1)del;(2619+1_2620-1)_(2988+1_2989-1)del]",
    "p.?",
    "No",
    "9",
    "CF-causing",
    "complex deletion of exons 3 through 10 and 14b through 16 (legacy numbering)|complex deletion of exons 3 through 11 and 16 through 18 (current numbering)",
    "4.26326111053215e-05",
    "CFTRdele3-10,14b-16"
  ],
  "complex deletion of exons 3 through 10 and 14b through 16 (legacy numbering)|complex deletion of exons 3 through 11 and 16 through 18 (current numbering)": [
    "c.[(164+1_165-1)_(1584+1_1585-1)del;(2619+1_2620-1)_(2988+1_2989-1)del]",
    "p.?",
    "No",
    "9",
    "CF-causing",
    "complex deletion of exons 3 through 10 and 14b through 16 (legacy numbering)|complex deletion of exons 3 through 11 and 16 through 18 (current numbering)",
    "4.26326111053215e-05",
    "CFTRdele3-10,14b-16"
  ],
  "CFTRdele3-10,14b-16": [
    "c.[(164+1_165-1)_(1584+1_1585-1)del;(2619+1_2620-1)_(2988+1_2989-1)del]",
    "p.?",
    "No",
    "9",
    "CF-causing",
    "complex deletion of exons 3 through 10 and 14b through 16 (legacy numbering)|complex deletion of exons 3 through 11 and 16 through 18 (current numbering)",
    "4.26326111053215e-05",
    "CFTRdele3-10,14b-16"
  ],
  "CFTR50kbdel": [
    "CFTR50kbdel",
    "complex deletion of exons 4 through 7 and 11 through 18 (legacy numbering)|complex deletion of exons 4 through 8 and 12 through 21 (current numbering)",
    "p.?",
    "No",
    "9",
    "CF-causing",
    "4.26326111053215e-05",
    "c.[(273+1_274-1)_(1116+1_1117-1)del;(1584+1_1585-1)_(3468+1_3469-1)del]"
  ],
  "complex deletion of exons 4 through 7 and 11 through 18 (legacy numbering)|complex deletion of exons 4 through 8 and 12 through 21 (current numbering)": [
    "CFTR50kbdel",
    "complex deletion of exons 4 through 7 and 11 through 18 (legacy numbering)|complex deletion of exons 4 through 8 and 12 through 21 (current numbering)",
    "p.?",
    "No",
    "9",
    "CF-causing",
    "4.26326111053215e-05",
    "c.[(273+1_274-1)_(1116+1_1117-1)del;(1584+1_1585-1)_(3468+1_3469-1)del]"
  ],
  "c.[(273+1_274-1)_(1116+1_1117-1)del;(1584+1_1585-1)_(3468+1_3469-1)del]": [
    "CFTR50kbdel",
    "complex deletion of exons 4 through 7 and 11 through 18 (legacy numbering)|complex deletion of exons 4 through 8 and 12 through 21 (current numbering)",
    "p.?",
    "No",
    "9",
    "CF-causing",
    "4.26326111053215e-05",
    "c.[(273+1_274-1)_(1116+1_1117-1)del;(1584+1_1585-1)_(3468+1_3469-1)del]"
  ],
  "CFTRdele18": [
    "p.?",
    "No",
    "9",
    "CF-causing",
    "CFTRdele18",
    "4.26326111053215e-05",
    "c.(3367+1_3368-1)_(3468+1_3469-1)del",
    "deletion of exon 18 (legacy numbering)|deletion of exon 21 (current numbering)"
  ],
  "c.(3367+1_3368-1)_(3468+1_3469-1)del": [
    "p.?",
    "No",
    "9",
    "CF-causing",
    "CFTRdele18",
    "4.26326111053215e-05",
    "c.(3367+1_3368-1)_(3468+1_3469-1)del",
    "deletion of exon 18 (legacy numbering)|deletion of exon 21 (current numbering)"
  ],
  "deletion of exon 18 (legacy numbering)|deletion of exon 21 (current numbering)": [
    "p.?",
    "No",
    "9",
    "CF-causing",
    "CFTRdele18",
    "4.26326111053215e-05",
    "c.(3367+1_3368-1)_(3468+1_3469-1)del",
    "deletion of exon 18 (legacy numbering)|deletion of exon 21 (current numbering)"
  ],
  "deletion of exons 17b and 18 (legacy numbering)|deletion of exons 20 and 21 (current numbering)": [
    "p.?",
    "deletion of exons 17b and 18 (legacy numbering)|deletion of exons 20 and 21 (current numbering)",
    "Yes, new variant added",
    "c.(3139+1_3140-1)_(3468+1_3469-1)del",
    "9",
    "CF-causing",
    "CFTRdele17b,18",
    "4.26326111053215e-05"
  ],
  "c.(3139+1_3140-1)_(3468+1_3469-1)del": [
    "p.?",
    "deletion of exons 17b and 18 (legacy numbering)|deletion of exons 20 and 21 (current numbering)",
    "Yes, new variant added",
    "c.(3139+1_3140-1)_(3468+1_3469-1)del",
    "9",
    "CF-causing",
    "CFTRdele17b,18",
    "4.26326111053215e-05"
  ],
  "CFTRdele17b,18": [
    "p.?",
    "deletion of exons 17b and 18 (legacy numbering)|deletion of exons 20 and 21 (current numbering)",
    "Yes, new variant added",
    "c.(3139+1_3140-1)_(3468+1_3469-1)del",
    "9",
    "CF-causing",
    "CFTRdele17b,18",
    "4.26326111053215e-05"
  ],
  "c.164+1G>A": [
    "p.?",
    "No",
    "9",
    "c.164+1G>A",
    "CF-causing",
    "296+1G->A",
    "4.26326111053215e-05"
  ],
  "296+1G->A": [
    "p.?",
    "No",
    "9",
    "c.164+1G>A",
    "CF-causing",
    "296+1G->A",
    "4.26326111053215e-05"
  ],
  "3601-2A->G": [
    "p.?",
    "No",
    "9",
    "CF-causing",
    "3601-2A->G",
    "4.26326111053215e-05",
    "c.3469-2A>G"
  ],
  "c.3469-2A>G": [
    "p.?",
    "No",
    "9",
    "CF-causing",
    "3601-2A->G",
    "4.26326111053215e-05",
    "c.3469-2A>G"
  ],
  "1524+1G->A": [
    "1524+1G->A",
    "p.?",
    "No",
    "9",
    "CF-causing",
    "c.1392+1G>A",
    "4.26326111053215e-05"
  ],
  "c.1392+1G>A": [
    "1524+1G->A",
    "p.?",
    "No",
    "9",
    "CF-causing",
    "c.1392+1G>A",
    "4.26326111053215e-05"
  ],
  "p.Tyr1014ThrfsX9": [
    "No",
    "9",
    "CF-causing",
    "p.Tyr1014ThrfsX9",
    "c.3039del",
    "3171delC",
    "4.26326111053215e-05"
  ],
  "c.3039del": [
    "No",
    "9",
    "CF-causing",
    "p.Tyr1014ThrfsX9",
    "c.3039del",
    "3171delC",
    "4.26326111053215e-05"
  ],
  "3171delC": [
    "No",
    "9",
    "CF-causing",
    "p.Tyr1014ThrfsX9",
    "c.3039del",
    "3171delC",
    "4.26326111053215e-05"
  ],
  "c.1792_1798del": [
    "c.1792_1798del",
    "No",
    "1924del7",
    "9",
    "CF-causing",
    "4.26326111053215e-05",
    "p.Lys598GlyfsX11"
  ],
  "1924del7": [
    "c.1792_1798del",
    "No",
    "1924del7",
    "9",
    "CF-causing",
    "4.26326111053215e-05",
    "p.Lys598GlyfsX11"
  ],
  "p.Lys598GlyfsX11": [
    "c.1792_1798del",
    "No",
    "1924del7",
    "9",
    "CF-causing",
    "4.26326111053215e-05",
    "p.Lys598GlyfsX11"
  ],
  "c.2997_3000del": [
    "c.2997_3000del",
    "No",
    "9",
    "CF-causing",
    "p.Ile1000X",
    "4.26326111053215e-05",
    "3129del4"
  ],
  "p.Ile1000X": [
    "c.2997_3000del",
    "No",
    "9",
    "CF-causing",
    "p.Ile1000X",
    "4.26326111053215e-05",
    "3129del4"
  ],
  "3129del4": [
    "c.2997_3000del",
    "No",
    "9",
    "CF-causing",
    "p.Ile1000X",
    "4.26326111053215e-05",
    "3129del4"
  ],
  "3849+1G->A": [
    "p.?",
    "Yes, new variant added",
    "3849+1G->A",
    "9",
    "CF-causing",
    "c.3717+1G>A",
    "4.26326111053215e-05"
  ],
  "c.3717+1G>A": [
    "p.?",
    "Yes, new variant added",
    "3849+1G->A",
    "9",
    "CF-causing",
    "c.3717+1G>A",
    "4.26326111053215e-05"
  ],
  "175delC": [
    "Yes, new variant added",
    "9",
    "CF-causing",
    "175delC",
    "p.Leu15PhefsX10",
    "4.26326111053215e-05",
    "c.43del"
  ],
  "p.Leu15PhefsX10": [
    "Yes, new variant added",
    "9",
    "CF-causing",
    "175delC",
    "p.Leu15PhefsX10",
    "4.26326111053215e-05",
    "c.43del"
  ],
  "c.43del": [
    "Yes, new variant added",
    "9",
    "CF-causing",
    "175delC",
    "p.Leu15PhefsX10",
    "4.26326111053215e-05",
    "c.43del"
  ],
  "c.488delA": [
    "Yes, new variant added",
    "c.488delA",
    "9",
    "CF-causing",
    "4.26326111053215e-05",
    "p.Lys163ArgfsX3",
    "c.488del"
  ],
  "p.Lys163ArgfsX3": [
    "Yes, new variant added",
    "c.488delA",
    "9",
    "CF-causing",
    "4.26326111053215e-05",
    "p.Lys163ArgfsX3",
    "c.488del"
  ],
  "c.488del": [
    "Yes, new variant added",
    "c.488delA",
    "9",
    "CF-causing",
    "4.26326111053215e-05",
    "p.Lys163ArgfsX3",
    "c.488del"
  ],
  "c.164+28A>G": [
    "c.164+28A>G",
    "p.?",
    "296+28A->G",
    "9",
    "Varying clinical consequence",
    "Yes",
    "4.26326111053215e-05",
    "Unknown significance"
  ],
  "296+28A->G": [
    "c.164+28A>G",
    "p.?",
    "296+28A->G",
    "9",
    "Varying clinical consequence",
    "Yes",
    "4.26326111053215e-05",
    "Unknown significance"
  ],
  "L346P": [
    "L346P",
    "No",
    "8",
    "3.789565431584133e-05",
    "1169T>G",
    "CF-causing",
    "p.Leu346Pro",
    "c.1037T>C"
  ],
  "8": [
    "No",
    "3.789565431584133e-05",
    "8",
    "p.Gly551ValfsX8",
    "CF-causing",
    "c.1650del",
    "1782delA"
  ],
  "3.789565431584133e-05": [
    "No",
    "3.789565431584133e-05",
    "8",
    "p.Gly551ValfsX8",
    "CF-causing",
    "c.1650del",
    "1782delA"
  ],
  "1169T>G": [
    "L346P",
    "No",
    "8",
    "3.789565431584133e-05",
    "1169T>G",
    "CF-causing",
    "p.Leu346Pro",
    "c.1037T>C"
  ],
  "p.Leu346Pro": [
    "L346P",
    "No",
    "8",
    "3.789565431584133e-05",
    "1169T>G",
    "CF-causing",
    "p.Leu346Pro",
    "c.1037T>C"
  ],
  "c.1037T>C": [
    "L346P",
    "No",
    "8",
    "3.789565431584133e-05",
    "1169T>G",
    "CF-causing",
    "p.Leu346Pro",
    "c.1037T>C"
  ],
  "A349V": [
    "A349V",
    "c.1046C>T",
    "8",
    "3.789565431584133e-05",
    "Varying clinical consequence",
    "p.Ala349Val",
    "Yes",
    "1178C>T",
    "Unknown significance"
  ],
  "c.1046C>T": [
    "A349V",
    "c.1046C>T",
    "8",
    "3.789565431584133e-05",
    "Varying clinical consequence",
    "p.Ala349Val",
    "Yes",
    "1178C>T",
    "Unknown significance"
  ],
  "p.Ala349Val": [
    "A349V",
    "c.1046C>T",
    "8",
    "3.789565431584133e-05",
    "Varying clinical consequence",
    "p.Ala349Val",
    "Yes",
    "1178C>T",
    "Unknown significance"
  ],
  "1178C>T": [
    "A349V",
    "c.1046C>T",
    "8",
    "3.789565431584133e-05",
    "Varying clinical consequence",
    "p.Ala349Val",
    "Yes",
    "1178C>T",
    "Unknown significance"
  ],
  "Q2X": [
    "Q2X",
    "No",
    "8",
    "3.789565431584133e-05",
    "CF-causing",
    "136C>T",
    "c.4C>T",
    "p.Gln2X"
  ],
  "136C>T": [
    "Q2X",
    "No",
    "8",
    "3.789565431584133e-05",
    "CF-causing",
    "136C>T",
    "c.4C>T",
    "p.Gln2X"
  ],
  "c.4C>T": [
    "Q2X",
    "No",
    "8",
    "3.789565431584133e-05",
    "CF-causing",
    "136C>T",
    "c.4C>T",
    "p.Gln2X"
  ],
  "p.Gln2X": [
    "Q2X",
    "No",
    "8",
    "3.789565431584133e-05",
    "CF-causing",
    "136C>T",
    "c.4C>T",
    "p.Gln2X"
  ],
  "c.1724T>A": [
    "No",
    "8",
    "3.789565431584133e-05",
    "c.1724T>A",
    "Varying clinical consequence",
    "p.Phe575Tyr",
    "1856T>A",
    "F575Y"
  ],
  "p.Phe575Tyr": [
    "No",
    "8",
    "3.789565431584133e-05",
    "c.1724T>A",
    "Varying clinical consequence",
    "p.Phe575Tyr",
    "1856T>A",
    "F575Y"
  ],
  "1856T>A": [
    "No",
    "8",
    "3.789565431584133e-05",
    "c.1724T>A",
    "Varying clinical consequence",
    "p.Phe575Tyr",
    "1856T>A",
    "F575Y"
  ],
  "F575Y": [
    "No",
    "8",
    "3.789565431584133e-05",
    "c.1724T>A",
    "Varying clinical consequence",
    "p.Phe575Tyr",
    "1856T>A",
    "F575Y"
  ],
  "c.1763A>T": [
    "No",
    "8",
    "c.1763A>T",
    "1895A>T",
    "3.789565431584133e-05",
    "Varying clinical consequence",
    "p.Glu588Val",
    "E588V"
  ],
  "1895A>T": [
    "No",
    "8",
    "c.1763A>T",
    "1895A>T",
    "3.789565431584133e-05",
    "Varying clinical consequence",
    "p.Glu588Val",
    "E588V"
  ],
  "p.Glu588Val": [
    "No",
    "8",
    "c.1763A>T",
    "1895A>T",
    "3.789565431584133e-05",
    "Varying clinical consequence",
    "p.Glu588Val",
    "E588V"
  ],
  "E588V": [
    "No",
    "8",
    "c.1763A>T",
    "1895A>T",
    "3.789565431584133e-05",
    "Varying clinical consequence",
    "p.Glu588Val",
    "E588V"
  ],
  "c.2735C>T": [
    "c.2735C>T",
    "2867C>T",
    "8",
    "3.789565431584133e-05",
    "p.Ser912Leu",
    "Varying clinical consequence",
    "Yes",
    "S912L",
    "Unknown significance"
  ],
  "2867C>T": [
    "c.2735C>T",
    "2867C>T",
    "8",
    "3.789565431584133e-05",
    "p.Ser912Leu",
    "Varying clinical consequence",
    "Yes",
    "S912L",
    "Unknown significance"
  ],
  "p.Ser912Leu": [
    "c.2735C>T",
    "2867C>T",
    "8",
    "3.789565431584133e-05",
    "p.Ser912Leu",
    "Varying clinical consequence",
    "Yes",
    "S912L",
    "Unknown significance"
  ],
  "S912L": [
    "c.2735C>T",
    "2867C>T",
    "8",
    "3.789565431584133e-05",
    "p.Ser912Leu",
    "Varying clinical consequence",
    "Yes",
    "S912L",
    "Unknown significance"
  ],
  "3851T>G": [
    "No",
    "3851T>G",
    "8",
    "3.789565431584133e-05",
    "V1240G",
    "CF-causing",
    "p.Val1240Gly",
    "c.3719T>G"
  ],
  "V1240G": [
    "No",
    "3851T>G",
    "8",
    "3.789565431584133e-05",
    "V1240G",
    "CF-causing",
    "p.Val1240Gly",
    "c.3719T>G"
  ],
  "p.Val1240Gly": [
    "No",
    "3851T>G",
    "8",
    "3.789565431584133e-05",
    "V1240G",
    "CF-causing",
    "p.Val1240Gly",
    "c.3719T>G"
  ],
  "c.3719T>G": [
    "No",
    "3851T>G",
    "8",
    "3.789565431584133e-05",
    "V1240G",
    "CF-causing",
    "p.Val1240Gly",
    "c.3719T>G"
  ],
  "p.Trp1274X": [
    "p.Trp1274X",
    "No",
    "8",
    "W1274X",
    "3.789565431584133e-05",
    "3954G>A",
    "CF-causing",
    "c.3822G>A"
  ],
  "W1274X": [
    "p.Trp1274X",
    "No",
    "8",
    "W1274X",
    "3.789565431584133e-05",
    "3954G>A",
    "CF-causing",
    "c.3822G>A"
  ],
  "3954G>A": [
    "p.Trp1274X",
    "No",
    "8",
    "W1274X",
    "3.789565431584133e-05",
    "3954G>A",
    "CF-causing",
    "c.3822G>A"
  ],
  "c.3822G>A": [
    "p.Trp1274X",
    "No",
    "8",
    "W1274X",
    "3.789565431584133e-05",
    "3954G>A",
    "CF-causing",
    "c.3822G>A"
  ],
  "p.Leu1480Pro": [
    "p.Leu1480Pro",
    "No",
    "8",
    "3.789565431584133e-05",
    "4571T>C",
    "L1480P",
    "Varying clinical consequence",
    "c.4439T>C"
  ],
  "4571T>C": [
    "p.Leu1480Pro",
    "No",
    "8",
    "3.789565431584133e-05",
    "4571T>C",
    "L1480P",
    "Varying clinical consequence",
    "c.4439T>C"
  ],
  "L1480P": [
    "p.Leu1480Pro",
    "No",
    "8",
    "3.789565431584133e-05",
    "4571T>C",
    "L1480P",
    "Varying clinical consequence",
    "c.4439T>C"
  ],
  "c.4439T>C": [
    "p.Leu1480Pro",
    "No",
    "8",
    "3.789565431584133e-05",
    "4571T>C",
    "L1480P",
    "Varying clinical consequence",
    "c.4439T>C"
  ],
  "c.358G>A": [
    "No",
    "c.358G>A",
    "8",
    "3.789565431584133e-05",
    "Varying clinical consequence",
    "490G>A",
    "A120T",
    "p.Ala120Thr"
  ],
  "490G>A": [
    "No",
    "c.358G>A",
    "8",
    "3.789565431584133e-05",
    "Varying clinical consequence",
    "490G>A",
    "A120T",
    "p.Ala120Thr"
  ],
  "A120T": [
    "No",
    "c.358G>A",
    "8",
    "3.789565431584133e-05",
    "Varying clinical consequence",
    "490G>A",
    "A120T",
    "p.Ala120Thr"
  ],
  "p.Ala120Thr": [
    "No",
    "c.358G>A",
    "8",
    "3.789565431584133e-05",
    "Varying clinical consequence",
    "490G>A",
    "A120T",
    "p.Ala120Thr"
  ],
  "c.445G>A": [
    "No",
    "c.445G>A",
    "8",
    "p.Gly149Arg",
    "3.789565431584133e-05",
    "CF-causing",
    "G149R",
    "577G>A"
  ],
  "p.Gly149Arg": [
    "No",
    "c.445G>A",
    "8",
    "p.Gly149Arg",
    "3.789565431584133e-05",
    "CF-causing",
    "G149R",
    "577G>A"
  ],
  "G149R": [
    "No",
    "c.445G>A",
    "8",
    "p.Gly149Arg",
    "3.789565431584133e-05",
    "CF-causing",
    "G149R",
    "577G>A"
  ],
  "577G>A": [
    "No",
    "c.445G>A",
    "8",
    "p.Gly149Arg",
    "3.789565431584133e-05",
    "CF-causing",
    "G149R",
    "577G>A"
  ],
  "712G>A": [
    "No",
    "8",
    "3.789565431584133e-05",
    "CF-causing",
    "712G>A",
    "c.580G>A|c.580G>C",
    "p.Gly194Arg",
    "G194R"
  ],
  "c.580G>A|c.580G>C": [
    "No",
    "8",
    "3.789565431584133e-05",
    "CF-causing",
    "712G>A",
    "c.580G>A|c.580G>C",
    "p.Gly194Arg",
    "G194R"
  ],
  "p.Gly194Arg": [
    "No",
    "8",
    "3.789565431584133e-05",
    "CF-causing",
    "712G>A",
    "c.580G>A|c.580G>C",
    "p.Gly194Arg",
    "G194R"
  ],
  "G194R": [
    "No",
    "8",
    "3.789565431584133e-05",
    "CF-causing",
    "712G>A",
    "c.580G>A|c.580G>C",
    "p.Gly194Arg",
    "G194R"
  ],
  "p.Met265Arg": [
    "No",
    "8",
    "3.789565431584133e-05",
    "p.Met265Arg",
    "Varying clinical consequence",
    "M265R",
    "c.794T>G",
    "926T>G"
  ],
  "M265R": [
    "No",
    "8",
    "3.789565431584133e-05",
    "p.Met265Arg",
    "Varying clinical consequence",
    "M265R",
    "c.794T>G",
    "926T>G"
  ],
  "c.794T>G": [
    "No",
    "8",
    "3.789565431584133e-05",
    "p.Met265Arg",
    "Varying clinical consequence",
    "M265R",
    "c.794T>G",
    "926T>G"
  ],
  "926T>G": [
    "No",
    "8",
    "3.789565431584133e-05",
    "p.Met265Arg",
    "Varying clinical consequence",
    "M265R",
    "c.794T>G",
    "926T>G"
  ],
  "c.(1392+1_1393-1)_(1584+1_1585-1)del": [
    "p.?",
    "No",
    "8",
    "c.(1392+1_1393-1)_(1584+1_1585-1)del",
    "CFTRdele10",
    "3.789565431584133e-05",
    "CF-causing",
    "deletion of exon 10 (legacy numbering)|deletion of exon 11 (current numbering)"
  ],
  "CFTRdele10": [
    "p.?",
    "No",
    "8",
    "c.(1392+1_1393-1)_(1584+1_1585-1)del",
    "CFTRdele10",
    "3.789565431584133e-05",
    "CF-causing",
    "deletion of exon 10 (legacy numbering)|deletion of exon 11 (current numbering)"
  ],
  "deletion of exon 10 (legacy numbering)|deletion of exon 11 (current numbering)": [
    "p.?",
    "No",
    "8",
    "c.(1392+1_1393-1)_(1584+1_1585-1)del",
    "CFTRdele10",
    "3.789565431584133e-05",
    "CF-causing",
    "deletion of exon 10 (legacy numbering)|deletion of exon 11 (current numbering)"
  ],
  "deletion of exons 13 and 14a (legacy numbering)|deletion of exons 14 and 15 (current numbering)": [
    "p.?",
    "No",
    "8",
    "deletion of exons 13 and 14a (legacy numbering)|deletion of exons 14 and 15 (current numbering)",
    "3.789565431584133e-05",
    "CF-causing",
    "c.(1766+1_1767-1)_(2619+1_2620-1)del",
    "CFTRdele13,14a"
  ],
  "c.(1766+1_1767-1)_(2619+1_2620-1)del": [
    "p.?",
    "No",
    "8",
    "deletion of exons 13 and 14a (legacy numbering)|deletion of exons 14 and 15 (current numbering)",
    "3.789565431584133e-05",
    "CF-causing",
    "c.(1766+1_1767-1)_(2619+1_2620-1)del",
    "CFTRdele13,14a"
  ],
  "CFTRdele13,14a": [
    "p.?",
    "No",
    "8",
    "deletion of exons 13 and 14a (legacy numbering)|deletion of exons 14 and 15 (current numbering)",
    "3.789565431584133e-05",
    "CF-causing",
    "c.(1766+1_1767-1)_(2619+1_2620-1)del",
    "CFTRdele13,14a"
  ],
  "deletion of exons 18 through 20 (legacy numbering)|deletion of exons 21 through 23 (current numbering)": [
    "p.?",
    "Yes, new variant added",
    "8",
    "deletion of exons 18 through 20 (legacy numbering)|deletion of exons 21 through 23 (current numbering)",
    "3.789565431584133e-05",
    "c.(3367+1_3368-1)_(3873+1_3874-1)del",
    "CFTRdele18-20",
    "CF-causing"
  ],
  "c.(3367+1_3368-1)_(3873+1_3874-1)del": [
    "p.?",
    "Yes, new variant added",
    "8",
    "deletion of exons 18 through 20 (legacy numbering)|deletion of exons 21 through 23 (current numbering)",
    "3.789565431584133e-05",
    "c.(3367+1_3368-1)_(3873+1_3874-1)del",
    "CFTRdele18-20",
    "CF-causing"
  ],
  "CFTRdele18-20": [
    "p.?",
    "Yes, new variant added",
    "8",
    "deletion of exons 18 through 20 (legacy numbering)|deletion of exons 21 through 23 (current numbering)",
    "3.789565431584133e-05",
    "c.(3367+1_3368-1)_(3873+1_3874-1)del",
    "CFTRdele18-20",
    "CF-causing"
  ],
  "deletion of exons 4 through 8 (legacy numbering)|deletion of exons 4 through 9 (current numbering)": [
    "p.?",
    "deletion of exons 4 through 8 (legacy numbering)|deletion of exons 4 through 9 (current numbering)",
    "CFTRdele4-8",
    "Yes, new variant added",
    "8",
    "3.789565431584133e-05",
    "c.(273+1_274-1)_(1209+1_1210-1)del",
    "CF-causing"
  ],
  "CFTRdele4-8": [
    "p.?",
    "deletion of exons 4 through 8 (legacy numbering)|deletion of exons 4 through 9 (current numbering)",
    "CFTRdele4-8",
    "Yes, new variant added",
    "8",
    "3.789565431584133e-05",
    "c.(273+1_274-1)_(1209+1_1210-1)del",
    "CF-causing"
  ],
  "c.(273+1_274-1)_(1209+1_1210-1)del": [
    "p.?",
    "deletion of exons 4 through 8 (legacy numbering)|deletion of exons 4 through 9 (current numbering)",
    "CFTRdele4-8",
    "Yes, new variant added",
    "8",
    "3.789565431584133e-05",
    "c.(273+1_274-1)_(1209+1_1210-1)del",
    "CF-causing"
  ],
  "406-2A->G": [
    "406-2A->G",
    "p.?",
    "No",
    "3.789565431584133e-05",
    "8",
    "c.274-2A>G",
    "CF-causing"
  ],
  "c.274-2A>G": [
    "406-2A->G",
    "p.?",
    "No",
    "3.789565431584133e-05",
    "8",
    "c.274-2A>G",
    "CF-causing"
  ],
  "p.Lys254ArgfsX7": [
    "No",
    "3.789565431584133e-05",
    "8",
    "CF-causing",
    "p.Lys254ArgfsX7",
    "892delA",
    "c.761del"
  ],
  "892delA": [
    "No",
    "3.789565431584133e-05",
    "8",
    "CF-causing",
    "p.Lys254ArgfsX7",
    "892delA",
    "c.761del"
  ],
  "c.761del": [
    "No",
    "3.789565431584133e-05",
    "8",
    "CF-causing",
    "p.Lys254ArgfsX7",
    "892delA",
    "c.761del"
  ],
  "1215delG": [
    "No",
    "8",
    "3.789565431584133e-05",
    "1215delG",
    "CF-causing",
    "p.Trp361CysfsX8",
    "c.1083del"
  ],
  "p.Trp361CysfsX8": [
    "No",
    "8",
    "3.789565431584133e-05",
    "1215delG",
    "CF-causing",
    "p.Trp361CysfsX8",
    "c.1083del"
  ],
  "c.1083del": [
    "No",
    "8",
    "3.789565431584133e-05",
    "1215delG",
    "CF-causing",
    "p.Trp361CysfsX8",
    "c.1083del"
  ],
  "p.Gly551ValfsX8": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.1652del",
    "p.Gly551ValfsX8",
    "CF-causing",
    "1",
    "1784delG"
  ],
  "c.1650del": [
    "No",
    "3.789565431584133e-05",
    "8",
    "p.Gly551ValfsX8",
    "CF-causing",
    "c.1650del",
    "1782delA"
  ],
  "1782delA": [
    "No",
    "3.789565431584133e-05",
    "8",
    "p.Gly551ValfsX8",
    "CF-causing",
    "c.1650del",
    "1782delA"
  ],
  "p.Gln781X": [
    "p.Gln781X",
    "No",
    "3.3158697526361164e-05",
    "2473C>T",
    "7",
    "CF-causing",
    "c.2341C>T",
    "Q781X"
  ],
  "3.3158697526361164e-05": [
    "3.3158697526361164e-05",
    "Yes, new variant added",
    "7",
    "CF-causing",
    "c.1084_1088dup",
    "p.Ser364MetfsX7"
  ],
  "2473C>T": [
    "p.Gln781X",
    "No",
    "3.3158697526361164e-05",
    "2473C>T",
    "7",
    "CF-causing",
    "c.2341C>T",
    "Q781X"
  ],
  "7": [
    "3.3158697526361164e-05",
    "Yes, new variant added",
    "7",
    "CF-causing",
    "c.1084_1088dup",
    "p.Ser364MetfsX7"
  ],
  "c.2341C>T": [
    "p.Gln781X",
    "No",
    "3.3158697526361164e-05",
    "2473C>T",
    "7",
    "CF-causing",
    "c.2341C>T",
    "Q781X"
  ],
  "Q781X": [
    "p.Gln781X",
    "No",
    "3.3158697526361164e-05",
    "2473C>T",
    "7",
    "CF-causing",
    "c.2341C>T",
    "Q781X"
  ],
  "310G>A": [
    "310G>A",
    "p.Glu60Lys",
    "No",
    "3.3158697526361164e-05",
    "7",
    "CF-causing",
    "c.178G>A",
    "E60K"
  ],
  "p.Glu60Lys": [
    "310G>A",
    "p.Glu60Lys",
    "No",
    "3.3158697526361164e-05",
    "7",
    "CF-causing",
    "c.178G>A",
    "E60K"
  ],
  "c.178G>A": [
    "310G>A",
    "p.Glu60Lys",
    "No",
    "3.3158697526361164e-05",
    "7",
    "CF-causing",
    "c.178G>A",
    "E60K"
  ],
  "E60K": [
    "310G>A",
    "p.Glu60Lys",
    "No",
    "3.3158697526361164e-05",
    "7",
    "CF-causing",
    "c.178G>A",
    "E60K"
  ],
  "c.3294G>C|c.3294G>T": [
    "c.3294G>C|c.3294G>T",
    "3426G>C|3426G>T",
    "No",
    "3.3158697526361164e-05",
    "7",
    "CF-causing",
    "W1098C",
    "p.Trp1098Cys"
  ],
  "3426G>C|3426G>T": [
    "c.3294G>C|c.3294G>T",
    "3426G>C|3426G>T",
    "No",
    "3.3158697526361164e-05",
    "7",
    "CF-causing",
    "W1098C",
    "p.Trp1098Cys"
  ],
  "W1098C": [
    "c.3294G>C|c.3294G>T",
    "3426G>C|3426G>T",
    "No",
    "3.3158697526361164e-05",
    "7",
    "CF-causing",
    "W1098C",
    "p.Trp1098Cys"
  ],
  "p.Trp1098Cys": [
    "c.3294G>C|c.3294G>T",
    "3426G>C|3426G>T",
    "No",
    "3.3158697526361164e-05",
    "7",
    "CF-causing",
    "W1098C",
    "p.Trp1098Cys"
  ],
  "p.Trp1145X": [
    "No",
    "3.3158697526361164e-05",
    "p.Trp1145X",
    "7",
    "c.3434G>A|c.3435G>A",
    "CF-causing",
    "W1145X",
    "3567G>A"
  ],
  "c.3434G>A|c.3435G>A": [
    "No",
    "3.3158697526361164e-05",
    "p.Trp1145X",
    "7",
    "c.3434G>A|c.3435G>A",
    "CF-causing",
    "W1145X",
    "3567G>A"
  ],
  "W1145X": [
    "No",
    "3.3158697526361164e-05",
    "p.Trp1145X",
    "7",
    "c.3434G>A|c.3435G>A",
    "CF-causing",
    "W1145X",
    "3567G>A"
  ],
  "3567G>A": [
    "No",
    "3.3158697526361164e-05",
    "p.Trp1145X",
    "7",
    "c.3434G>A|c.3435G>A",
    "CF-causing",
    "W1145X",
    "3567G>A"
  ],
  "c.3458T>A": [
    "No",
    "3.3158697526361164e-05",
    "c.3458T>A",
    "7",
    "Varying clinical consequence",
    "V1153E",
    "p.Val1153Glu",
    "3590T>A"
  ],
  "V1153E": [
    "No",
    "3.3158697526361164e-05",
    "c.3458T>A",
    "7",
    "Varying clinical consequence",
    "V1153E",
    "p.Val1153Glu",
    "3590T>A"
  ],
  "p.Val1153Glu": [
    "No",
    "3.3158697526361164e-05",
    "c.3458T>A",
    "7",
    "Varying clinical consequence",
    "V1153E",
    "p.Val1153Glu",
    "3590T>A"
  ],
  "3590T>A": [
    "No",
    "3.3158697526361164e-05",
    "c.3458T>A",
    "7",
    "Varying clinical consequence",
    "V1153E",
    "p.Val1153Glu",
    "3590T>A"
  ],
  "p.Ser1206X": [
    "p.Ser1206X",
    "No",
    "3.3158697526361164e-05",
    "7",
    "CF-causing",
    "c.3617C>G",
    "3749C>G",
    "S1206X"
  ],
  "c.3617C>G": [
    "p.Ser1206X",
    "No",
    "3.3158697526361164e-05",
    "7",
    "CF-causing",
    "c.3617C>G",
    "3749C>G",
    "S1206X"
  ],
  "3749C>G": [
    "p.Ser1206X",
    "No",
    "3.3158697526361164e-05",
    "7",
    "CF-causing",
    "c.3617C>G",
    "3749C>G",
    "S1206X"
  ],
  "S1206X": [
    "p.Ser1206X",
    "No",
    "3.3158697526361164e-05",
    "7",
    "CF-causing",
    "c.3617C>G",
    "3749C>G",
    "S1206X"
  ],
  "3980G>T": [
    "No",
    "3.3158697526361164e-05",
    "3980G>T",
    "7",
    "c.3848G>T",
    "p.Arg1283Met",
    "CF-causing",
    "R1283M"
  ],
  "c.3848G>T": [
    "No",
    "3.3158697526361164e-05",
    "3980G>T",
    "7",
    "c.3848G>T",
    "p.Arg1283Met",
    "CF-causing",
    "R1283M"
  ],
  "p.Arg1283Met": [
    "No",
    "3.3158697526361164e-05",
    "3980G>T",
    "7",
    "c.3848G>T",
    "p.Arg1283Met",
    "CF-causing",
    "R1283M"
  ],
  "R1283M": [
    "No",
    "3.3158697526361164e-05",
    "3980G>T",
    "7",
    "c.3848G>T",
    "p.Arg1283Met",
    "CF-causing",
    "R1283M"
  ],
  "428C>T": [
    "No",
    "3.3158697526361164e-05",
    "7",
    "CF-causing",
    "428C>T",
    "p.Pro99Leu",
    "c.296C>T",
    "P99L"
  ],
  "p.Pro99Leu": [
    "No",
    "3.3158697526361164e-05",
    "7",
    "CF-causing",
    "428C>T",
    "p.Pro99Leu",
    "c.296C>T",
    "P99L"
  ],
  "c.296C>T": [
    "No",
    "3.3158697526361164e-05",
    "7",
    "CF-causing",
    "428C>T",
    "p.Pro99Leu",
    "c.296C>T",
    "P99L"
  ],
  "P99L": [
    "No",
    "3.3158697526361164e-05",
    "7",
    "CF-causing",
    "428C>T",
    "p.Pro99Leu",
    "c.296C>T",
    "P99L"
  ],
  "p.Phe157X": [
    "No",
    "3.3158697526361164e-05",
    "7",
    "p.Phe157X",
    "c.470_483del14|c.469_482del14",
    "c.470_483del",
    "CF-causing",
    "602del14"
  ],
  "c.470_483del14|c.469_482del14": [
    "No",
    "3.3158697526361164e-05",
    "7",
    "p.Phe157X",
    "c.470_483del14|c.469_482del14",
    "c.470_483del",
    "CF-causing",
    "602del14"
  ],
  "c.470_483del": [
    "No",
    "3.3158697526361164e-05",
    "7",
    "p.Phe157X",
    "c.470_483del14|c.469_482del14",
    "c.470_483del",
    "CF-causing",
    "602del14"
  ],
  "602del14": [
    "No",
    "3.3158697526361164e-05",
    "7",
    "p.Phe157X",
    "c.470_483del14|c.469_482del14",
    "c.470_483del",
    "CF-causing",
    "602del14"
  ],
  "deletion of exon 15 (legacy numbering)|deletion of exon 17 (current numbering)": [
    "p.?",
    "3.3158697526361164e-05",
    "Yes, new variant added",
    "7",
    "deletion of exon 15 (legacy numbering)|deletion of exon 17 (current numbering)",
    "c.(2657+1_2658-1)_(2908+1_2909-1)del",
    "CF-causing",
    "CFTRdele15"
  ],
  "c.(2657+1_2658-1)_(2908+1_2909-1)del": [
    "p.?",
    "3.3158697526361164e-05",
    "Yes, new variant added",
    "7",
    "deletion of exon 15 (legacy numbering)|deletion of exon 17 (current numbering)",
    "c.(2657+1_2658-1)_(2908+1_2909-1)del",
    "CF-causing",
    "CFTRdele15"
  ],
  "CFTRdele15": [
    "p.?",
    "3.3158697526361164e-05",
    "Yes, new variant added",
    "7",
    "deletion of exon 15 (legacy numbering)|deletion of exon 17 (current numbering)",
    "c.(2657+1_2658-1)_(2908+1_2909-1)del",
    "CF-causing",
    "CFTRdele15"
  ],
  "c.(3717+1_3718-1)_(3873+1_3874-1)del": [
    "c.(3717+1_3718-1)_(3873+1_3874-1)del",
    "p.?",
    "3.3158697526361164e-05",
    "Yes, new variant added",
    "7",
    "CF-causing",
    "CFTRdele20",
    "deletion of exon 20 (legacy numbering)|deletion of exon 23 (current numbering)"
  ],
  "CFTRdele20": [
    "c.(3717+1_3718-1)_(3873+1_3874-1)del",
    "p.?",
    "3.3158697526361164e-05",
    "Yes, new variant added",
    "7",
    "CF-causing",
    "CFTRdele20",
    "deletion of exon 20 (legacy numbering)|deletion of exon 23 (current numbering)"
  ],
  "deletion of exon 20 (legacy numbering)|deletion of exon 23 (current numbering)": [
    "c.(3717+1_3718-1)_(3873+1_3874-1)del",
    "p.?",
    "3.3158697526361164e-05",
    "Yes, new variant added",
    "7",
    "CF-causing",
    "CFTRdele20",
    "deletion of exon 20 (legacy numbering)|deletion of exon 23 (current numbering)"
  ],
  "deletion of exon 21 (legacy numbering)|deletion of exon 24 (current numbering)": [
    "p.?",
    "deletion of exon 21 (legacy numbering)|deletion of exon 24 (current numbering)",
    "c.(3873+1_3874-1)_(3963+1_3964-1)del",
    "3.3158697526361164e-05",
    "No",
    "7",
    "CFTRdele21",
    "CF-causing"
  ],
  "c.(3873+1_3874-1)_(3963+1_3964-1)del": [
    "p.?",
    "deletion of exon 21 (legacy numbering)|deletion of exon 24 (current numbering)",
    "c.(3873+1_3874-1)_(3963+1_3964-1)del",
    "3.3158697526361164e-05",
    "No",
    "7",
    "CFTRdele21",
    "CF-causing"
  ],
  "CFTRdele21": [
    "p.?",
    "deletion of exon 21 (legacy numbering)|deletion of exon 24 (current numbering)",
    "c.(3873+1_3874-1)_(3963+1_3964-1)del",
    "3.3158697526361164e-05",
    "No",
    "7",
    "CFTRdele21",
    "CF-causing"
  ],
  "c.(3468+1_3469-1)_(3717+1_3718-1)dup": [
    "p.?",
    "c.(3468+1_3469-1)_(3717+1_3718-1)dup",
    "duplication of exon 19 (legacy numbering)|duplication of exon 22 (current numbering)",
    "3.3158697526361164e-05",
    "Yes, new variant added",
    "7",
    "CF-causing",
    "CFTRdup19"
  ],
  "duplication of exon 19 (legacy numbering)|duplication of exon 22 (current numbering)": [
    "p.?",
    "c.(3468+1_3469-1)_(3717+1_3718-1)dup",
    "duplication of exon 19 (legacy numbering)|duplication of exon 22 (current numbering)",
    "3.3158697526361164e-05",
    "Yes, new variant added",
    "7",
    "CF-causing",
    "CFTRdup19"
  ],
  "CFTRdup19": [
    "p.?",
    "c.(3468+1_3469-1)_(3717+1_3718-1)dup",
    "duplication of exon 19 (legacy numbering)|duplication of exon 22 (current numbering)",
    "3.3158697526361164e-05",
    "Yes, new variant added",
    "7",
    "CF-causing",
    "CFTRdup19"
  ],
  "c.(1392+1_1393-1)_(1766+1_1767-1)dup": [
    "c.(1392+1_1393-1)_(1766+1_1767-1)dup",
    "p.?",
    "duplication of exons 10 through 12 (legacy numbering)|duplication of exons 11 through 13 (current numbering)",
    "3.3158697526361164e-05",
    "Yes, new variant added",
    "7",
    "CF-causing",
    "CFTRdup10-12"
  ],
  "duplication of exons 10 through 12 (legacy numbering)|duplication of exons 11 through 13 (current numbering)": [
    "c.(1392+1_1393-1)_(1766+1_1767-1)dup",
    "p.?",
    "duplication of exons 10 through 12 (legacy numbering)|duplication of exons 11 through 13 (current numbering)",
    "3.3158697526361164e-05",
    "Yes, new variant added",
    "7",
    "CF-causing",
    "CFTRdup10-12"
  ],
  "CFTRdup10-12": [
    "c.(1392+1_1393-1)_(1766+1_1767-1)dup",
    "p.?",
    "duplication of exons 10 through 12 (legacy numbering)|duplication of exons 11 through 13 (current numbering)",
    "3.3158697526361164e-05",
    "Yes, new variant added",
    "7",
    "CF-causing",
    "CFTRdup10-12"
  ],
  "c.(1116+1_1117-1)_(1584+1_1585-1)dup": [
    "c.(1116+1_1117-1)_(1584+1_1585-1)dup",
    "p.?",
    "3.3158697526361164e-05",
    "Yes, new variant added",
    "duplication of exons 8 through 10 (legacy numbering)|duplication of exons 9 through 11 (current numbering)",
    "7",
    "CF-causing",
    "CFTRdup8-10"
  ],
  "duplication of exons 8 through 10 (legacy numbering)|duplication of exons 9 through 11 (current numbering)": [
    "c.(1116+1_1117-1)_(1584+1_1585-1)dup",
    "p.?",
    "3.3158697526361164e-05",
    "Yes, new variant added",
    "duplication of exons 8 through 10 (legacy numbering)|duplication of exons 9 through 11 (current numbering)",
    "7",
    "CF-causing",
    "CFTRdup8-10"
  ],
  "CFTRdup8-10": [
    "c.(1116+1_1117-1)_(1584+1_1585-1)dup",
    "p.?",
    "3.3158697526361164e-05",
    "Yes, new variant added",
    "duplication of exons 8 through 10 (legacy numbering)|duplication of exons 9 through 11 (current numbering)",
    "7",
    "CF-causing",
    "CFTRdup8-10"
  ],
  "c.[4C>T;7A>T]": [
    "No",
    "3.3158697526361164e-05",
    "c.[4C>T;7A>T]",
    "7",
    "CF-causing",
    "Q2X in cis with R3W|[136C>T with 139A>T]",
    "Q2X;R3W"
  ],
  "Q2X in cis with R3W|[136C>T with 139A>T]": [
    "No",
    "3.3158697526361164e-05",
    "c.[4C>T;7A>T]",
    "7",
    "CF-causing",
    "Q2X in cis with R3W|[136C>T with 139A>T]",
    "Q2X;R3W"
  ],
  "Q2X;R3W": [
    "No",
    "3.3158697526361164e-05",
    "c.[4C>T;7A>T]",
    "7",
    "CF-causing",
    "Q2X in cis with R3W|[136C>T with 139A>T]",
    "Q2X;R3W"
  ],
  "W1282X;R1283M": [
    "No",
    "3.3158697526361164e-05",
    "7",
    "W1282X;R1283M",
    "c.[3846G>A;3848G>T]",
    "CF-causing",
    "W1282X in cis with R1283M|[3978G>A or3980G>T]"
  ],
  "c.[3846G>A;3848G>T]": [
    "No",
    "3.3158697526361164e-05",
    "7",
    "W1282X;R1283M",
    "c.[3846G>A;3848G>T]",
    "CF-causing",
    "W1282X in cis with R1283M|[3978G>A or3980G>T]"
  ],
  "W1282X in cis with R1283M|[3978G>A or3980G>T]": [
    "No",
    "3.3158697526361164e-05",
    "7",
    "W1282X;R1283M",
    "c.[3846G>A;3848G>T]",
    "CF-causing",
    "W1282X in cis with R1283M|[3978G>A or3980G>T]"
  ],
  "c.3139_3139+1del": [
    "p.?",
    "No",
    "3.3158697526361164e-05",
    "7",
    "CF-causing",
    "c.3139_3139+1del",
    "3271delGG"
  ],
  "3271delGG": [
    "p.?",
    "No",
    "3.3158697526361164e-05",
    "7",
    "CF-causing",
    "c.3139_3139+1del",
    "3271delGG"
  ],
  "1824delA": [
    "No",
    "3.3158697526361164e-05",
    "1824delA",
    "7",
    "CF-causing",
    "p.Asp565MetfsX7",
    "c.1692del"
  ],
  "p.Asp565MetfsX7": [
    "No",
    "3.3158697526361164e-05",
    "1824delA",
    "7",
    "CF-causing",
    "p.Asp565MetfsX7",
    "c.1692del"
  ],
  "c.1692del": [
    "No",
    "3.3158697526361164e-05",
    "1824delA",
    "7",
    "CF-causing",
    "p.Asp565MetfsX7",
    "c.1692del"
  ],
  "p.Gln799SerfsX6": [
    "No",
    "3.3158697526361164e-05",
    "p.Gln799SerfsX6",
    "7",
    "CF-causing",
    "c.2393dup",
    "2522insC"
  ],
  "c.2393dup": [
    "No",
    "3.3158697526361164e-05",
    "p.Gln799SerfsX6",
    "7",
    "CF-causing",
    "c.2393dup",
    "2522insC"
  ],
  "2522insC": [
    "No",
    "3.3158697526361164e-05",
    "p.Gln799SerfsX6",
    "7",
    "CF-causing",
    "c.2393dup",
    "2522insC"
  ],
  "p.S1347PfsX13": [
    "No",
    "3.3158697526361164e-05",
    "7",
    "CF-causing",
    "p.S1347PfsX13",
    "p.Ser1347ProfsX13",
    "c.4035_4038dup"
  ],
  "p.Ser1347ProfsX13": [
    "No",
    "3.3158697526361164e-05",
    "7",
    "CF-causing",
    "p.S1347PfsX13",
    "p.Ser1347ProfsX13",
    "c.4035_4038dup"
  ],
  "c.4035_4038dup": [
    "No",
    "3.3158697526361164e-05",
    "7",
    "CF-causing",
    "p.S1347PfsX13",
    "p.Ser1347ProfsX13",
    "c.4035_4038dup"
  ],
  "c.1742dup": [
    "No",
    "3.3158697526361164e-05",
    "7",
    "c.1742dup",
    "CF-causing",
    "p.Leu581PhefsX8",
    "1874insT"
  ],
  "p.Leu581PhefsX8": [
    "No",
    "3.3158697526361164e-05",
    "7",
    "c.1742dup",
    "CF-causing",
    "p.Leu581PhefsX8",
    "1874insT"
  ],
  "1874insT": [
    "No",
    "3.3158697526361164e-05",
    "7",
    "c.1742dup",
    "CF-causing",
    "p.Leu581PhefsX8",
    "1874insT"
  ],
  "p.Val1008SerfsX15": [
    "4.7369567894801664e-06",
    "p.Val1008SerfsX15",
    "Yes, new variant added",
    "3152delT",
    "CF-causing",
    "1",
    "c.3021del"
  ],
  "c.3022del": [
    "p.Val1008SerfsX15",
    "No",
    "3.3158697526361164e-05",
    "7",
    "c.3022del",
    "CF-causing",
    "3154delG"
  ],
  "3154delG": [
    "p.Val1008SerfsX15",
    "No",
    "3.3158697526361164e-05",
    "7",
    "c.3022del",
    "CF-causing",
    "3154delG"
  ],
  "297-3C->T": [
    "p.?",
    "3.3158697526361164e-05",
    "7",
    "CF-causing",
    "297-3C->T",
    "Yes",
    "c.165-3C>T",
    "Unknown significance"
  ],
  "c.165-3C>T": [
    "p.?",
    "3.3158697526361164e-05",
    "7",
    "CF-causing",
    "297-3C->T",
    "Yes",
    "c.165-3C>T",
    "Unknown significance"
  ],
  "c.2472del": [
    "3.3158697526361164e-05",
    "Yes, new variant added",
    "7",
    "c.2472del",
    "p.Asn825ThrfsX5",
    "CF-causing",
    "2603delT"
  ],
  "p.Asn825ThrfsX5": [
    "3.3158697526361164e-05",
    "Yes, new variant added",
    "7",
    "c.2472del",
    "p.Asn825ThrfsX5",
    "CF-causing",
    "2603delT"
  ],
  "2603delT": [
    "3.3158697526361164e-05",
    "Yes, new variant added",
    "7",
    "c.2472del",
    "p.Asn825ThrfsX5",
    "CF-causing",
    "2603delT"
  ],
  "c.1084_1088dup": [
    "3.3158697526361164e-05",
    "Yes, new variant added",
    "7",
    "CF-causing",
    "c.1084_1088dup",
    "p.Ser364MetfsX7"
  ],
  "p.Ser364MetfsX7": [
    "3.3158697526361164e-05",
    "Yes, new variant added",
    "7",
    "CF-causing",
    "c.1084_1088dup",
    "p.Ser364MetfsX7"
  ],
  "c.868C>T": [
    "No",
    "c.868C>T",
    "2.8421740736880997e-05",
    "1000C>T",
    "CF-causing",
    "6",
    "p.Gln290X",
    "Q290X"
  ],
  "2.8421740736880997e-05": [
    "p.Phe17LeufsX8",
    "Yes, new variant added",
    "183delC",
    "c.51del",
    "2.8421740736880997e-05",
    "CF-causing",
    "6"
  ],
  "1000C>T": [
    "No",
    "c.868C>T",
    "2.8421740736880997e-05",
    "1000C>T",
    "CF-causing",
    "6",
    "p.Gln290X",
    "Q290X"
  ],
  "6": [
    "p.Phe17LeufsX8",
    "Yes, new variant added",
    "183delC",
    "c.51del",
    "2.8421740736880997e-05",
    "CF-causing",
    "6"
  ],
  "p.Gln290X": [
    "No",
    "c.868C>T",
    "2.8421740736880997e-05",
    "1000C>T",
    "CF-causing",
    "6",
    "p.Gln290X",
    "Q290X"
  ],
  "Q290X": [
    "No",
    "c.868C>T",
    "2.8421740736880997e-05",
    "1000C>T",
    "CF-causing",
    "6",
    "p.Gln290X",
    "Q290X"
  ],
  "c.1086T>A|c.1086T>G": [
    "c.1086T>A|c.1086T>G",
    "p.Tyr362X",
    "No",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "Y362X",
    "1218T>A|1218T>G"
  ],
  "p.Tyr362X": [
    "c.1086T>A|c.1086T>G",
    "p.Tyr362X",
    "No",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "Y362X",
    "1218T>A|1218T>G"
  ],
  "Y362X": [
    "c.1086T>A|c.1086T>G",
    "p.Tyr362X",
    "No",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "Y362X",
    "1218T>A|1218T>G"
  ],
  "1218T>A|1218T>G": [
    "c.1086T>A|c.1086T>G",
    "p.Tyr362X",
    "No",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "Y362X",
    "1218T>A|1218T>G"
  ],
  "E407X": [
    "Yes, new variant added",
    "E407X",
    "2.8421740736880997e-05",
    "CF-causing",
    "c.1219G>T",
    "6",
    "p.Glu407X",
    "1351G->T"
  ],
  "c.1219G>T": [
    "Yes, new variant added",
    "E407X",
    "2.8421740736880997e-05",
    "CF-causing",
    "c.1219G>T",
    "6",
    "p.Glu407X",
    "1351G->T"
  ],
  "p.Glu407X": [
    "Yes, new variant added",
    "E407X",
    "2.8421740736880997e-05",
    "CF-causing",
    "c.1219G>T",
    "6",
    "p.Glu407X",
    "1351G->T"
  ],
  "1351G->T": [
    "Yes, new variant added",
    "E407X",
    "2.8421740736880997e-05",
    "CF-causing",
    "c.1219G>T",
    "6",
    "p.Glu407X",
    "1351G->T"
  ],
  "c.1366G>T": [
    "c.1366G>T",
    "p.Val456Phe",
    "No",
    "2.8421740736880997e-05",
    "CF-causing",
    "V456F",
    "6",
    "1498G>T"
  ],
  "p.Val456Phe": [
    "c.1366G>T",
    "p.Val456Phe",
    "No",
    "2.8421740736880997e-05",
    "CF-causing",
    "V456F",
    "6",
    "1498G>T"
  ],
  "V456F": [
    "c.1366G>T",
    "p.Val456Phe",
    "No",
    "2.8421740736880997e-05",
    "CF-causing",
    "V456F",
    "6",
    "1498G>T"
  ],
  "1498G>T": [
    "c.1366G>T",
    "p.Val456Phe",
    "No",
    "2.8421740736880997e-05",
    "CF-causing",
    "V456F",
    "6",
    "1498G>T"
  ],
  "L15P": [
    "L15P",
    "No",
    "2.8421740736880997e-05",
    "CF-causing",
    "176T>C",
    "6",
    "c.44T>C",
    "p.Leu15Pro"
  ],
  "176T>C": [
    "L15P",
    "No",
    "2.8421740736880997e-05",
    "CF-causing",
    "176T>C",
    "6",
    "c.44T>C",
    "p.Leu15Pro"
  ],
  "c.44T>C": [
    "L15P",
    "No",
    "2.8421740736880997e-05",
    "CF-causing",
    "176T>C",
    "6",
    "c.44T>C",
    "p.Leu15Pro"
  ],
  "p.Leu15Pro": [
    "L15P",
    "No",
    "2.8421740736880997e-05",
    "CF-causing",
    "176T>C",
    "6",
    "c.44T>C",
    "p.Leu15Pro"
  ],
  "c.1687T>G": [
    "c.1687T>G",
    "No",
    "2.8421740736880997e-05",
    "Y563D",
    "CF-causing",
    "6",
    "1819T>G",
    "p.Tyr563Asp"
  ],
  "Y563D": [
    "c.1687T>G",
    "No",
    "2.8421740736880997e-05",
    "Y563D",
    "CF-causing",
    "6",
    "1819T>G",
    "p.Tyr563Asp"
  ],
  "1819T>G": [
    "c.1687T>G",
    "No",
    "2.8421740736880997e-05",
    "Y563D",
    "CF-causing",
    "6",
    "1819T>G",
    "p.Tyr563Asp"
  ],
  "p.Tyr563Asp": [
    "c.1687T>G",
    "No",
    "2.8421740736880997e-05",
    "Y563D",
    "CF-causing",
    "6",
    "1819T>G",
    "p.Tyr563Asp"
  ],
  "c.1801A>T": [
    "No",
    "c.1801A>T",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "p.Ile601Phe",
    "I601F",
    "1933A>T"
  ],
  "p.Ile601Phe": [
    "No",
    "c.1801A>T",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "p.Ile601Phe",
    "I601F",
    "1933A>T"
  ],
  "I601F": [
    "No",
    "c.1801A>T",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "p.Ile601Phe",
    "I601F",
    "1933A>T"
  ],
  "1933A>T": [
    "No",
    "c.1801A>T",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "p.Ile601Phe",
    "I601F",
    "1933A>T"
  ],
  "c.79G>A": [
    "No",
    "2.8421740736880997e-05",
    "c.79G>A",
    "G27R",
    "CF-causing",
    "6",
    "p.Gly27Arg",
    "211G>A"
  ],
  "G27R": [
    "No",
    "2.8421740736880997e-05",
    "c.79G>A",
    "G27R",
    "CF-causing",
    "6",
    "p.Gly27Arg",
    "211G>A"
  ],
  "p.Gly27Arg": [
    "No",
    "2.8421740736880997e-05",
    "c.79G>A",
    "G27R",
    "CF-causing",
    "6",
    "p.Gly27Arg",
    "211G>A"
  ],
  "211G>A": [
    "No",
    "2.8421740736880997e-05",
    "c.79G>A",
    "G27R",
    "CF-causing",
    "6",
    "p.Gly27Arg",
    "211G>A"
  ],
  "2122G>T": [
    "No",
    "2122G>T",
    "p.Glu664X",
    "2.8421740736880997e-05",
    "CF-causing",
    "E664X",
    "6",
    "c.1990G>T"
  ],
  "p.Glu664X": [
    "No",
    "2122G>T",
    "p.Glu664X",
    "2.8421740736880997e-05",
    "CF-causing",
    "E664X",
    "6",
    "c.1990G>T"
  ],
  "E664X": [
    "No",
    "2122G>T",
    "p.Glu664X",
    "2.8421740736880997e-05",
    "CF-causing",
    "E664X",
    "6",
    "c.1990G>T"
  ],
  "c.1990G>T": [
    "No",
    "2122G>T",
    "p.Glu664X",
    "2.8421740736880997e-05",
    "CF-causing",
    "E664X",
    "6",
    "c.1990G>T"
  ],
  "c.92G>T": [
    "c.92G>T",
    "224G>T",
    "R31L",
    "2.8421740736880997e-05",
    "Varying clinical consequence",
    "6",
    "Yes",
    "p.Arg31Leu",
    "Unknown significance"
  ],
  "224G>T": [
    "c.92G>T",
    "224G>T",
    "R31L",
    "2.8421740736880997e-05",
    "Varying clinical consequence",
    "6",
    "Yes",
    "p.Arg31Leu",
    "Unknown significance"
  ],
  "R31L": [
    "c.92G>T",
    "224G>T",
    "R31L",
    "2.8421740736880997e-05",
    "Varying clinical consequence",
    "6",
    "Yes",
    "p.Arg31Leu",
    "Unknown significance"
  ],
  "p.Arg31Leu": [
    "c.92G>T",
    "224G>T",
    "R31L",
    "2.8421740736880997e-05",
    "Varying clinical consequence",
    "6",
    "Yes",
    "p.Arg31Leu",
    "Unknown significance"
  ],
  "p.Gln720X": [
    "p.Gln720X",
    "2290C>T",
    "Q720X",
    "No",
    "c.2158C>T",
    "2.8421740736880997e-05",
    "CF-causing",
    "6"
  ],
  "2290C>T": [
    "p.Gln720X",
    "2290C>T",
    "Q720X",
    "No",
    "c.2158C>T",
    "2.8421740736880997e-05",
    "CF-causing",
    "6"
  ],
  "Q720X": [
    "p.Gln720X",
    "2290C>T",
    "Q720X",
    "No",
    "c.2158C>T",
    "2.8421740736880997e-05",
    "CF-causing",
    "6"
  ],
  "c.2158C>T": [
    "p.Gln720X",
    "2290C>T",
    "Q720X",
    "No",
    "c.2158C>T",
    "2.8421740736880997e-05",
    "CF-causing",
    "6"
  ],
  "p.Ile748SerfsX28": [
    "p.Ile748SerfsX28",
    "No",
    "2.8421740736880997e-05",
    "CF-causing",
    "2372del8",
    "6",
    "c.2241_2248del",
    "2373del8|c.2240_2247delCGATACTG"
  ],
  "2372del8": [
    "p.Ile748SerfsX28",
    "No",
    "2.8421740736880997e-05",
    "CF-causing",
    "2372del8",
    "6",
    "c.2241_2248del",
    "2373del8|c.2240_2247delCGATACTG"
  ],
  "c.2241_2248del": [
    "p.Ile748SerfsX28",
    "No",
    "2.8421740736880997e-05",
    "CF-causing",
    "2372del8",
    "6",
    "c.2241_2248del",
    "2373del8|c.2240_2247delCGATACTG"
  ],
  "2373del8|c.2240_2247delCGATACTG": [
    "p.Ile748SerfsX28",
    "No",
    "2.8421740736880997e-05",
    "CF-causing",
    "2372del8",
    "6",
    "c.2241_2248del",
    "2373del8|c.2240_2247delCGATACTG"
  ],
  "2777G>A": [
    "2777G>A",
    "No",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "c.2645G>A|c.2646G>A",
    "p.Trp882X",
    "W882X"
  ],
  "c.2645G>A|c.2646G>A": [
    "2777G>A",
    "No",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "c.2645G>A|c.2646G>A",
    "p.Trp882X",
    "W882X"
  ],
  "p.Trp882X": [
    "2777G>A",
    "No",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "c.2645G>A|c.2646G>A",
    "p.Trp882X",
    "W882X"
  ],
  "W882X": [
    "2777G>A",
    "No",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "c.2645G>A|c.2646G>A",
    "p.Trp882X",
    "W882X"
  ],
  "c.236G>A": [
    "No",
    "c.236G>A",
    "368G>A",
    "p.Trp79X",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "W79X"
  ],
  "368G>A": [
    "No",
    "c.236G>A",
    "368G>A",
    "p.Trp79X",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "W79X"
  ],
  "p.Trp79X": [
    "No",
    "c.236G>A",
    "368G>A",
    "p.Trp79X",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "W79X"
  ],
  "W79X": [
    "No",
    "c.236G>A",
    "368G>A",
    "p.Trp79X",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "W79X"
  ],
  "c.3841C>T": [
    "c.3841C>T",
    "No",
    "3973C>T",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "Q1281X",
    "p.Gln1281X"
  ],
  "3973C>T": [
    "c.3841C>T",
    "No",
    "3973C>T",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "Q1281X",
    "p.Gln1281X"
  ],
  "Q1281X": [
    "c.3841C>T",
    "No",
    "3973C>T",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "Q1281X",
    "p.Gln1281X"
  ],
  "p.Gln1281X": [
    "c.3841C>T",
    "No",
    "3973C>T",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "Q1281X",
    "p.Gln1281X"
  ],
  "403G>A": [
    "403G>A",
    "No",
    "c.271G>A",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "p.Gly91Arg",
    "G91R"
  ],
  "c.271G>A": [
    "403G>A",
    "No",
    "c.271G>A",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "p.Gly91Arg",
    "G91R"
  ],
  "p.Gly91Arg": [
    "403G>A",
    "No",
    "c.271G>A",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "p.Gly91Arg",
    "G91R"
  ],
  "G91R": [
    "403G>A",
    "No",
    "c.271G>A",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "p.Gly91Arg",
    "G91R"
  ],
  "4103T>C": [
    "4103T>C",
    "No",
    "p.Leu1324Pro",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "c.3971T>C",
    "L1324P"
  ],
  "p.Leu1324Pro": [
    "4103T>C",
    "No",
    "p.Leu1324Pro",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "c.3971T>C",
    "L1324P"
  ],
  "c.3971T>C": [
    "4103T>C",
    "No",
    "p.Leu1324Pro",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "c.3971T>C",
    "L1324P"
  ],
  "L1324P": [
    "4103T>C",
    "No",
    "p.Leu1324Pro",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "c.3971T>C",
    "L1324P"
  ],
  "p.Leu101X": [
    "p.Leu101X",
    "434T>G",
    "Yes, new variant added",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "c.302T>G",
    "L101X"
  ],
  "434T>G": [
    "p.Leu101X",
    "434T>G",
    "Yes, new variant added",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "c.302T>G",
    "L101X"
  ],
  "c.302T>G": [
    "p.Leu101X",
    "434T>G",
    "Yes, new variant added",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "c.302T>G",
    "L101X"
  ],
  "L101X": [
    "p.Leu101X",
    "434T>G",
    "Yes, new variant added",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "c.302T>G",
    "L101X"
  ],
  "c.307G>T": [
    "No",
    "c.307G>T",
    "G103X",
    "2.8421740736880997e-05",
    "CF-causing",
    "439G>T",
    "6",
    "p.Gly103X"
  ],
  "G103X": [
    "No",
    "c.307G>T",
    "G103X",
    "2.8421740736880997e-05",
    "CF-causing",
    "439G>T",
    "6",
    "p.Gly103X"
  ],
  "439G>T": [
    "No",
    "c.307G>T",
    "G103X",
    "2.8421740736880997e-05",
    "CF-causing",
    "439G>T",
    "6",
    "p.Gly103X"
  ],
  "p.Gly103X": [
    "No",
    "c.307G>T",
    "G103X",
    "2.8421740736880997e-05",
    "CF-causing",
    "439G>T",
    "6",
    "p.Gly103X"
  ],
  "c.481T>G": [
    "No",
    "c.481T>G",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "p.Tyr161Asp",
    "Y161D",
    "613T>G"
  ],
  "p.Tyr161Asp": [
    "No",
    "c.481T>G",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "p.Tyr161Asp",
    "Y161D",
    "613T>G"
  ],
  "Y161D": [
    "No",
    "c.481T>G",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "p.Tyr161Asp",
    "Y161D",
    "613T>G"
  ],
  "613T>G": [
    "No",
    "c.481T>G",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "p.Tyr161Asp",
    "Y161D",
    "613T>G"
  ],
  "G194X": [
    "No",
    "G194X",
    "712G>T",
    "p.Gly194X",
    "2.8421740736880997e-05",
    "CF-causing",
    "c.580G>T",
    "6"
  ],
  "712G>T": [
    "No",
    "G194X",
    "712G>T",
    "p.Gly194X",
    "2.8421740736880997e-05",
    "CF-causing",
    "c.580G>T",
    "6"
  ],
  "p.Gly194X": [
    "No",
    "G194X",
    "712G>T",
    "p.Gly194X",
    "2.8421740736880997e-05",
    "CF-causing",
    "c.580G>T",
    "6"
  ],
  "c.580G>T": [
    "No",
    "G194X",
    "712G>T",
    "p.Gly194X",
    "2.8421740736880997e-05",
    "CF-causing",
    "c.580G>T",
    "6"
  ],
  "807T>A": [
    "807T>A",
    "No",
    "2.8421740736880997e-05",
    "CF-causing",
    "p.Cys225X",
    "6",
    "c.675T>A",
    "C225X"
  ],
  "p.Cys225X": [
    "807T>A",
    "No",
    "2.8421740736880997e-05",
    "CF-causing",
    "p.Cys225X",
    "6",
    "c.675T>A",
    "C225X"
  ],
  "c.675T>A": [
    "807T>A",
    "No",
    "2.8421740736880997e-05",
    "CF-causing",
    "p.Cys225X",
    "6",
    "c.675T>A",
    "C225X"
  ],
  "C225X": [
    "807T>A",
    "No",
    "2.8421740736880997e-05",
    "CF-causing",
    "p.Cys225X",
    "6",
    "c.675T>A",
    "C225X"
  ],
  "c.709C>G": [
    "No",
    "c.709C>G",
    "Varying clinical consequence",
    "841C>G",
    "2.8421740736880997e-05",
    "Q237E",
    "6",
    "p.Gln237Glu"
  ],
  "841C>G": [
    "No",
    "c.709C>G",
    "Varying clinical consequence",
    "841C>G",
    "2.8421740736880997e-05",
    "Q237E",
    "6",
    "p.Gln237Glu"
  ],
  "Q237E": [
    "No",
    "c.709C>G",
    "Varying clinical consequence",
    "841C>G",
    "2.8421740736880997e-05",
    "Q237E",
    "6",
    "p.Gln237Glu"
  ],
  "p.Gln237Glu": [
    "No",
    "c.709C>G",
    "Varying clinical consequence",
    "841C>G",
    "2.8421740736880997e-05",
    "Q237E",
    "6",
    "p.Gln237Glu"
  ],
  "W277X": [
    "No",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "W277X",
    "962G>A",
    "p.Trp277X",
    "c.830G>A|c.831G>A"
  ],
  "962G>A": [
    "No",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "W277X",
    "962G>A",
    "p.Trp277X",
    "c.830G>A|c.831G>A"
  ],
  "p.Trp277X": [
    "No",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "W277X",
    "962G>A",
    "p.Trp277X",
    "c.830G>A|c.831G>A"
  ],
  "c.830G>A|c.831G>A": [
    "No",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "W277X",
    "962G>A",
    "p.Trp277X",
    "c.830G>A|c.831G>A"
  ],
  "p.Ser809IlefsX13": [
    "No",
    "p.Ser809IlefsX13",
    "c.2423_2424dup",
    "2.8421740736880997e-05",
    "CF-causing",
    "2556insAT",
    "6",
    "c.2421_2422dupAT|c.2422_2423insAT"
  ],
  "c.2423_2424dup": [
    "No",
    "p.Ser809IlefsX13",
    "c.2423_2424dup",
    "2.8421740736880997e-05",
    "CF-causing",
    "2556insAT",
    "6",
    "c.2421_2422dupAT|c.2422_2423insAT"
  ],
  "2556insAT": [
    "No",
    "p.Ser809IlefsX13",
    "c.2423_2424dup",
    "2.8421740736880997e-05",
    "CF-causing",
    "2556insAT",
    "6",
    "c.2421_2422dupAT|c.2422_2423insAT"
  ],
  "c.2421_2422dupAT|c.2422_2423insAT": [
    "No",
    "p.Ser809IlefsX13",
    "c.2423_2424dup",
    "2.8421740736880997e-05",
    "CF-causing",
    "2556insAT",
    "6",
    "c.2421_2422dupAT|c.2422_2423insAT"
  ],
  "4279insA": [
    "No",
    "4279insA",
    "c.4147_4148insA",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "p.Ile1383AsnfsX3",
    "c.4147dup"
  ],
  "c.4147_4148insA": [
    "No",
    "4279insA",
    "c.4147_4148insA",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "p.Ile1383AsnfsX3",
    "c.4147dup"
  ],
  "p.Ile1383AsnfsX3": [
    "No",
    "4279insA",
    "c.4147_4148insA",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "p.Ile1383AsnfsX3",
    "c.4147dup"
  ],
  "c.4147dup": [
    "No",
    "4279insA",
    "c.4147_4148insA",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "p.Ile1383AsnfsX3",
    "c.4147dup"
  ],
  "CFTRdele14a": [
    "p.?",
    "Yes, new variant added",
    "CFTRdele14a",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "c.(2490+1_2491-1)_(2619+1_2620-1)del",
    "deletion of exon 14a (legacy numbering)|deletion of exon 15 (current numbering)|c.2490+827_2620-3551del"
  ],
  "c.(2490+1_2491-1)_(2619+1_2620-1)del": [
    "p.?",
    "Yes, new variant added",
    "CFTRdele14a",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "c.(2490+1_2491-1)_(2619+1_2620-1)del",
    "deletion of exon 14a (legacy numbering)|deletion of exon 15 (current numbering)|c.2490+827_2620-3551del"
  ],
  "deletion of exon 14a (legacy numbering)|deletion of exon 15 (current numbering)|c.2490+827_2620-3551del": [
    "p.?",
    "Yes, new variant added",
    "CFTRdele14a",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "c.(2490+1_2491-1)_(2619+1_2620-1)del",
    "deletion of exon 14a (legacy numbering)|deletion of exon 15 (current numbering)|c.2490+827_2620-3551del"
  ],
  "CFTRdele14b,15": [
    "CFTRdele14b,15",
    "p.?",
    "Yes, new variant added",
    "c.(2619+1_2620-1)_(2908+1_2909-1)del",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "deletion of exons 14b and 15 (legacy numbering)|deletion of exons 16 and 17 (current numbering)"
  ],
  "c.(2619+1_2620-1)_(2908+1_2909-1)del": [
    "CFTRdele14b,15",
    "p.?",
    "Yes, new variant added",
    "c.(2619+1_2620-1)_(2908+1_2909-1)del",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "deletion of exons 14b and 15 (legacy numbering)|deletion of exons 16 and 17 (current numbering)"
  ],
  "deletion of exons 14b and 15 (legacy numbering)|deletion of exons 16 and 17 (current numbering)": [
    "CFTRdele14b,15",
    "p.?",
    "Yes, new variant added",
    "c.(2619+1_2620-1)_(2908+1_2909-1)del",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "deletion of exons 14b and 15 (legacy numbering)|deletion of exons 16 and 17 (current numbering)"
  ],
  "c.987del": [
    "No",
    "c.987del",
    "1119delA",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "p.Gly330GlufsX39"
  ],
  "1119delA": [
    "No",
    "c.987del",
    "1119delA",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "p.Gly330GlufsX39"
  ],
  "p.Gly330GlufsX39": [
    "No",
    "c.987del",
    "1119delA",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "p.Gly330GlufsX39"
  ],
  "p.Leu548GlufsX19": [
    "No",
    "p.Leu548GlufsX19",
    "c.1642_1643del",
    "2.8421740736880997e-05",
    "CF-causing",
    "1774delCT",
    "6"
  ],
  "c.1642_1643del": [
    "No",
    "p.Leu548GlufsX19",
    "c.1642_1643del",
    "2.8421740736880997e-05",
    "CF-causing",
    "1774delCT",
    "6"
  ],
  "1774delCT": [
    "No",
    "p.Leu548GlufsX19",
    "c.1642_1643del",
    "2.8421740736880997e-05",
    "CF-causing",
    "1774delCT",
    "6"
  ],
  "c.3605del": [
    "c.3605del",
    "p.Asp1202AlafsX9",
    "No",
    "3737delA",
    "2.8421740736880997e-05",
    "CF-causing",
    "6"
  ],
  "p.Asp1202AlafsX9": [
    "c.3605del",
    "p.Asp1202AlafsX9",
    "No",
    "3737delA",
    "2.8421740736880997e-05",
    "CF-causing",
    "6"
  ],
  "3737delA": [
    "c.3605del",
    "p.Asp1202AlafsX9",
    "No",
    "3737delA",
    "2.8421740736880997e-05",
    "CF-causing",
    "6"
  ],
  "c.2502dup": [
    "No",
    "c.2502dup",
    "p.Asp835X",
    "2.8421740736880997e-05",
    "CF-causing",
    "2634insT",
    "6"
  ],
  "p.Asp835X": [
    "No",
    "c.2502dup",
    "p.Asp835X",
    "2.8421740736880997e-05",
    "CF-causing",
    "2634insT",
    "6"
  ],
  "2634insT": [
    "No",
    "c.2502dup",
    "p.Asp835X",
    "2.8421740736880997e-05",
    "CF-causing",
    "2634insT",
    "6"
  ],
  "3056delGA": [
    "No",
    "3056delGA",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "c.2924_2925del",
    "p.Arg975IlefsX10"
  ],
  "c.2924_2925del": [
    "No",
    "3056delGA",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "c.2924_2925del",
    "p.Arg975IlefsX10"
  ],
  "p.Arg975IlefsX10": [
    "No",
    "3056delGA",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "c.2924_2925del",
    "p.Arg975IlefsX10"
  ],
  "c.234dup": [
    "Yes, new variant added",
    "c.234dup",
    "2.8421740736880997e-05",
    "366insC",
    "CF-causing",
    "6",
    "p.Trp79LeufsX32"
  ],
  "366insC": [
    "Yes, new variant added",
    "c.234dup",
    "2.8421740736880997e-05",
    "366insC",
    "CF-causing",
    "6",
    "p.Trp79LeufsX32"
  ],
  "c.1469del": [
    "c.1469del",
    "p.Phe490SerfsX37",
    "1601delT",
    "Yes, new variant added",
    "2.8421740736880997e-05",
    "CF-causing",
    "6"
  ],
  "p.Phe490SerfsX37": [
    "c.1469del",
    "p.Phe490SerfsX37",
    "1601delT",
    "Yes, new variant added",
    "2.8421740736880997e-05",
    "CF-causing",
    "6"
  ],
  "1601delT": [
    "c.1469del",
    "p.Phe490SerfsX37",
    "1601delT",
    "Yes, new variant added",
    "2.8421740736880997e-05",
    "CF-causing",
    "6"
  ],
  "c.2556dupT": [
    "c.2556dupT",
    "c.2556dup",
    "Yes, new variant added",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "p.Ile853TyrfsX43"
  ],
  "c.2556dup": [
    "c.2556dupT",
    "c.2556dup",
    "Yes, new variant added",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "p.Ile853TyrfsX43"
  ],
  "p.Ile853TyrfsX43": [
    "c.2556dupT",
    "c.2556dup",
    "Yes, new variant added",
    "2.8421740736880997e-05",
    "CF-causing",
    "6",
    "p.Ile853TyrfsX43"
  ],
  "p.Phe17LeufsX8": [
    "p.Phe17LeufsX8",
    "Yes, new variant added",
    "183delC",
    "c.51del",
    "2.8421740736880997e-05",
    "CF-causing",
    "6"
  ],
  "183delC": [
    "p.Phe17LeufsX8",
    "Yes, new variant added",
    "183delC",
    "c.51del",
    "2.8421740736880997e-05",
    "CF-causing",
    "6"
  ],
  "c.51del": [
    "p.Phe17LeufsX8",
    "Yes, new variant added",
    "183delC",
    "c.51del",
    "2.8421740736880997e-05",
    "CF-causing",
    "6"
  ],
  "1490T>C": [
    "1490T>C",
    "2.3684783947400833e-05",
    "No",
    "L453S",
    "CF-causing",
    "c.1358T>C",
    "p.Leu453Ser",
    "5"
  ],
  "2.3684783947400833e-05": [
    "2.3684783947400833e-05",
    "Yes, new variant added",
    "CF-causing",
    "c.708del",
    "p.Gln237ArgfsX4",
    "840delT",
    "5"
  ],
  "L453S": [
    "1490T>C",
    "2.3684783947400833e-05",
    "No",
    "L453S",
    "CF-causing",
    "c.1358T>C",
    "p.Leu453Ser",
    "5"
  ],
  "c.1358T>C": [
    "1490T>C",
    "2.3684783947400833e-05",
    "No",
    "L453S",
    "CF-causing",
    "c.1358T>C",
    "p.Leu453Ser",
    "5"
  ],
  "p.Leu453Ser": [
    "1490T>C",
    "2.3684783947400833e-05",
    "No",
    "L453S",
    "CF-causing",
    "c.1358T>C",
    "p.Leu453Ser",
    "5"
  ],
  "5": [
    "2.3684783947400833e-05",
    "Yes, new variant added",
    "CF-causing",
    "c.708del",
    "p.Gln237ArgfsX4",
    "840delT",
    "5"
  ],
  "p.Trp19X": [
    "p.Trp19X",
    "2.3684783947400833e-05",
    "c.56G>A|c.57G>A",
    "No",
    "W19X",
    "CF-causing",
    "179G>A",
    "5"
  ],
  "c.56G>A|c.57G>A": [
    "p.Trp19X",
    "2.3684783947400833e-05",
    "c.56G>A|c.57G>A",
    "No",
    "W19X",
    "CF-causing",
    "179G>A",
    "5"
  ],
  "W19X": [
    "p.Trp19X",
    "2.3684783947400833e-05",
    "c.56G>A|c.57G>A",
    "No",
    "W19X",
    "CF-causing",
    "179G>A",
    "5"
  ],
  "179G>A": [
    "p.Trp19X",
    "2.3684783947400833e-05",
    "c.56G>A|c.57G>A",
    "No",
    "W19X",
    "CF-causing",
    "179G>A",
    "5"
  ],
  "G745X": [
    "2.3684783947400833e-05",
    "G745X",
    "c.2233G>T",
    "No",
    "CF-causing",
    "2365G>T",
    "p.Gly745X",
    "5"
  ],
  "c.2233G>T": [
    "2.3684783947400833e-05",
    "G745X",
    "c.2233G>T",
    "No",
    "CF-causing",
    "2365G>T",
    "p.Gly745X",
    "5"
  ],
  "2365G>T": [
    "2.3684783947400833e-05",
    "G745X",
    "c.2233G>T",
    "No",
    "CF-causing",
    "2365G>T",
    "p.Gly745X",
    "5"
  ],
  "p.Gly745X": [
    "2.3684783947400833e-05",
    "G745X",
    "c.2233G>T",
    "No",
    "CF-causing",
    "2365G>T",
    "p.Gly745X",
    "5"
  ],
  "3179T>C": [
    "2.3684783947400833e-05",
    "No",
    "3179T>C",
    "p.Phe1016Ser",
    "Varying clinical consequence",
    "F1016S",
    "c.3047T>C",
    "5"
  ],
  "p.Phe1016Ser": [
    "2.3684783947400833e-05",
    "No",
    "3179T>C",
    "p.Phe1016Ser",
    "Varying clinical consequence",
    "F1016S",
    "c.3047T>C",
    "5"
  ],
  "F1016S": [
    "2.3684783947400833e-05",
    "No",
    "3179T>C",
    "p.Phe1016Ser",
    "Varying clinical consequence",
    "F1016S",
    "c.3047T>C",
    "5"
  ],
  "c.3047T>C": [
    "2.3684783947400833e-05",
    "No",
    "3179T>C",
    "p.Phe1016Ser",
    "Varying clinical consequence",
    "F1016S",
    "c.3047T>C",
    "5"
  ],
  "H1085P": [
    "H1085P",
    "2.3684783947400833e-05",
    "No",
    "CF-causing",
    "c.3254A>C",
    "3386A>C",
    "p.His1085Pro",
    "5"
  ],
  "c.3254A>C": [
    "H1085P",
    "2.3684783947400833e-05",
    "No",
    "CF-causing",
    "c.3254A>C",
    "3386A>C",
    "p.His1085Pro",
    "5"
  ],
  "3386A>C": [
    "H1085P",
    "2.3684783947400833e-05",
    "No",
    "CF-causing",
    "c.3254A>C",
    "3386A>C",
    "p.His1085Pro",
    "5"
  ],
  "p.His1085Pro": [
    "H1085P",
    "2.3684783947400833e-05",
    "No",
    "CF-causing",
    "c.3254A>C",
    "3386A>C",
    "p.His1085Pro",
    "5"
  ],
  "p.Tyr84X": [
    "2.3684783947400833e-05",
    "p.Tyr84X",
    "Yes, new variant added",
    "CF-causing",
    "Y84X",
    "384T>A",
    "c.252T>A",
    "5"
  ],
  "Y84X": [
    "2.3684783947400833e-05",
    "p.Tyr84X",
    "Yes, new variant added",
    "CF-causing",
    "Y84X",
    "384T>A",
    "c.252T>A",
    "5"
  ],
  "384T>A": [
    "2.3684783947400833e-05",
    "p.Tyr84X",
    "Yes, new variant added",
    "CF-causing",
    "Y84X",
    "384T>A",
    "c.252T>A",
    "5"
  ],
  "c.252T>A": [
    "2.3684783947400833e-05",
    "p.Tyr84X",
    "Yes, new variant added",
    "CF-causing",
    "Y84X",
    "384T>A",
    "c.252T>A",
    "5"
  ],
  "c.3743C>A|c.3743C>G": [
    "c.3743C>A|c.3743C>G",
    "2.3684783947400833e-05",
    "No",
    "3875C>A|3875C>G",
    "S1248X",
    "CF-causing",
    "p.Ser1248X",
    "5"
  ],
  "3875C>A|3875C>G": [
    "c.3743C>A|c.3743C>G",
    "2.3684783947400833e-05",
    "No",
    "3875C>A|3875C>G",
    "S1248X",
    "CF-causing",
    "p.Ser1248X",
    "5"
  ],
  "S1248X": [
    "c.3743C>A|c.3743C>G",
    "2.3684783947400833e-05",
    "No",
    "3875C>A|3875C>G",
    "S1248X",
    "CF-causing",
    "p.Ser1248X",
    "5"
  ],
  "p.Ser1248X": [
    "c.3743C>A|c.3743C>G",
    "2.3684783947400833e-05",
    "No",
    "3875C>A|3875C>G",
    "S1248X",
    "CF-causing",
    "p.Ser1248X",
    "5"
  ],
  "c.3871C>T": [
    "2.3684783947400833e-05",
    "Yes, new variant added",
    "c.3871C>T",
    "4003C>T",
    "CF-causing",
    "Q1291X",
    "p.Gln1291X",
    "5"
  ],
  "4003C>T": [
    "2.3684783947400833e-05",
    "Yes, new variant added",
    "c.3871C>T",
    "4003C>T",
    "CF-causing",
    "Q1291X",
    "p.Gln1291X",
    "5"
  ],
  "Q1291X": [
    "2.3684783947400833e-05",
    "Yes, new variant added",
    "c.3871C>T",
    "4003C>T",
    "CF-causing",
    "Q1291X",
    "p.Gln1291X",
    "5"
  ],
  "p.Gln1291X": [
    "2.3684783947400833e-05",
    "Yes, new variant added",
    "c.3871C>T",
    "4003C>T",
    "CF-causing",
    "Q1291X",
    "p.Gln1291X",
    "5"
  ],
  "c.305T>G": [
    "2.3684783947400833e-05",
    "c.305T>G",
    "No",
    "L102R",
    "CF-causing",
    "437T>G",
    "5",
    "p.Leu102Arg"
  ],
  "L102R": [
    "2.3684783947400833e-05",
    "c.305T>G",
    "No",
    "L102R",
    "CF-causing",
    "437T>G",
    "5",
    "p.Leu102Arg"
  ],
  "437T>G": [
    "2.3684783947400833e-05",
    "c.305T>G",
    "No",
    "L102R",
    "CF-causing",
    "437T>G",
    "5",
    "p.Leu102Arg"
  ],
  "p.Leu102Arg": [
    "2.3684783947400833e-05",
    "c.305T>G",
    "No",
    "L102R",
    "CF-causing",
    "437T>G",
    "5",
    "p.Leu102Arg"
  ],
  "459T>A": [
    "2.3684783947400833e-05",
    "No",
    "459T>A",
    "Y109X",
    "CF-causing",
    "p.Tyr109X",
    "c.327T>A",
    "5"
  ],
  "Y109X": [
    "2.3684783947400833e-05",
    "No",
    "459T>A",
    "Y109X",
    "CF-causing",
    "p.Tyr109X",
    "c.327T>A",
    "5"
  ],
  "p.Tyr109X": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "p.Tyr109X",
    "1",
    "458delAT",
    "c.326_327del"
  ],
  "c.327T>A": [
    "2.3684783947400833e-05",
    "No",
    "459T>A",
    "Y109X",
    "CF-causing",
    "p.Tyr109X",
    "c.327T>A",
    "5"
  ],
  "R117P": [
    "2.3684783947400833e-05",
    "R117P",
    "No",
    "p.Arg117Pro",
    "CF-causing",
    "482G>C",
    "c.350G>C",
    "5"
  ],
  "p.Arg117Pro": [
    "2.3684783947400833e-05",
    "R117P",
    "No",
    "p.Arg117Pro",
    "CF-causing",
    "482G>C",
    "c.350G>C",
    "5"
  ],
  "482G>C": [
    "2.3684783947400833e-05",
    "R117P",
    "No",
    "p.Arg117Pro",
    "CF-causing",
    "482G>C",
    "c.350G>C",
    "5"
  ],
  "c.350G>C": [
    "2.3684783947400833e-05",
    "R117P",
    "No",
    "p.Arg117Pro",
    "CF-causing",
    "482G>C",
    "c.350G>C",
    "5"
  ],
  "W202X": [
    "2.3684783947400833e-05",
    "No",
    "W202X",
    "CF-causing",
    "p.Trp202X",
    "738G>A",
    "c.606G>A",
    "5"
  ],
  "p.Trp202X": [
    "2.3684783947400833e-05",
    "No",
    "W202X",
    "CF-causing",
    "p.Trp202X",
    "738G>A",
    "c.606G>A",
    "5"
  ],
  "738G>A": [
    "2.3684783947400833e-05",
    "No",
    "W202X",
    "CF-causing",
    "p.Trp202X",
    "738G>A",
    "c.606G>A",
    "5"
  ],
  "c.606G>A": [
    "2.3684783947400833e-05",
    "No",
    "W202X",
    "CF-causing",
    "p.Trp202X",
    "738G>A",
    "c.606G>A",
    "5"
  ],
  "CFTRdele17a": [
    "2.3684783947400833e-05",
    "CFTRdele17a",
    "p.?",
    "deletion of exon 17a (legacy numbering)|deletion of exon 19 (current numbering)",
    "Yes, new variant added",
    "CF-causing",
    "c.(2988+1_2989-1)_(3139+1_3140-1)del",
    "5"
  ],
  "deletion of exon 17a (legacy numbering)|deletion of exon 19 (current numbering)": [
    "2.3684783947400833e-05",
    "CFTRdele17a",
    "p.?",
    "deletion of exon 17a (legacy numbering)|deletion of exon 19 (current numbering)",
    "Yes, new variant added",
    "CF-causing",
    "c.(2988+1_2989-1)_(3139+1_3140-1)del",
    "5"
  ],
  "c.(2988+1_2989-1)_(3139+1_3140-1)del": [
    "2.3684783947400833e-05",
    "CFTRdele17a",
    "p.?",
    "deletion of exon 17a (legacy numbering)|deletion of exon 19 (current numbering)",
    "Yes, new variant added",
    "CF-causing",
    "c.(2988+1_2989-1)_(3139+1_3140-1)del",
    "5"
  ],
  "CFTRdele22": [
    "CFTRdele22",
    "p.?",
    "2.3684783947400833e-05",
    "Yes, new variant added",
    "CF-causing",
    "c.(3963+1_3964-1)_(4136+1_4137-1)del",
    "deletion of exon 22 (legacy numbering)|deletion of exon 25 (current numbering)",
    "5"
  ],
  "c.(3963+1_3964-1)_(4136+1_4137-1)del": [
    "CFTRdele22",
    "p.?",
    "2.3684783947400833e-05",
    "Yes, new variant added",
    "CF-causing",
    "c.(3963+1_3964-1)_(4136+1_4137-1)del",
    "deletion of exon 22 (legacy numbering)|deletion of exon 25 (current numbering)",
    "5"
  ],
  "deletion of exon 22 (legacy numbering)|deletion of exon 25 (current numbering)": [
    "CFTRdele22",
    "p.?",
    "2.3684783947400833e-05",
    "Yes, new variant added",
    "CF-causing",
    "c.(3963+1_3964-1)_(4136+1_4137-1)del",
    "deletion of exon 22 (legacy numbering)|deletion of exon 25 (current numbering)",
    "5"
  ],
  "c.1392+12_2657+403delins35": [
    "c.1392+12_2657+403delins35",
    "p.?",
    "2.3684783947400833e-05",
    "Yes, new variant added",
    "deletion of exons 10 through 14b (legacy numbering)|deletion of exons 11 through 16 (current numbering)",
    "CFTRdele10-14b",
    "CF-causing",
    "5"
  ],
  "deletion of exons 10 through 14b (legacy numbering)|deletion of exons 11 through 16 (current numbering)": [
    "c.1392+12_2657+403delins35",
    "p.?",
    "2.3684783947400833e-05",
    "Yes, new variant added",
    "deletion of exons 10 through 14b (legacy numbering)|deletion of exons 11 through 16 (current numbering)",
    "CFTRdele10-14b",
    "CF-causing",
    "5"
  ],
  "CFTRdele10-14b": [
    "c.1392+12_2657+403delins35",
    "p.?",
    "2.3684783947400833e-05",
    "Yes, new variant added",
    "deletion of exons 10 through 14b (legacy numbering)|deletion of exons 11 through 16 (current numbering)",
    "CFTRdele10-14b",
    "CF-causing",
    "5"
  ],
  "c.(2490+1_2491-1)_(2908+1_2909-1)del": [
    "2.3684783947400833e-05",
    "p.?",
    "c.(2490+1_2491-1)_(2908+1_2909-1)del",
    "Yes, new variant added",
    "CFTRdele14a-15",
    "deletion of exons 14a through 15 (legacy numbering)|deletion of exons 15 through 17 (current numbering)",
    "CF-causing",
    "5"
  ],
  "CFTRdele14a-15": [
    "2.3684783947400833e-05",
    "p.?",
    "c.(2490+1_2491-1)_(2908+1_2909-1)del",
    "Yes, new variant added",
    "CFTRdele14a-15",
    "deletion of exons 14a through 15 (legacy numbering)|deletion of exons 15 through 17 (current numbering)",
    "CF-causing",
    "5"
  ],
  "deletion of exons 14a through 15 (legacy numbering)|deletion of exons 15 through 17 (current numbering)": [
    "2.3684783947400833e-05",
    "p.?",
    "c.(2490+1_2491-1)_(2908+1_2909-1)del",
    "Yes, new variant added",
    "CFTRdele14a-15",
    "deletion of exons 14a through 15 (legacy numbering)|deletion of exons 15 through 17 (current numbering)",
    "CF-causing",
    "5"
  ],
  "c.164+1G>C": [
    "2.3684783947400833e-05",
    "p.?",
    "No",
    "c.164+1G>C",
    "CF-causing",
    "296+1G->C",
    "5"
  ],
  "296+1G->C": [
    "2.3684783947400833e-05",
    "p.?",
    "No",
    "c.164+1G>C",
    "CF-causing",
    "296+1G->C",
    "5"
  ],
  "c.1679+2T>C": [
    "2.3684783947400833e-05",
    "p.?",
    "c.1679+2T>C",
    "No",
    "1811+2T->C",
    "CF-causing",
    "5"
  ],
  "1811+2T->C": [
    "2.3684783947400833e-05",
    "p.?",
    "c.1679+2T>C",
    "No",
    "1811+2T->C",
    "CF-causing",
    "5"
  ],
  "1898+2T->A": [
    "2.3684783947400833e-05",
    "p.?",
    "No",
    "CF-causing",
    "1898+2T->A",
    "c.1766+2T>A",
    "5"
  ],
  "c.1766+2T>A": [
    "2.3684783947400833e-05",
    "p.?",
    "No",
    "CF-causing",
    "1898+2T->A",
    "c.1766+2T>A",
    "5"
  ],
  "3040+1G->A": [
    "3040+1G->A",
    "2.3684783947400833e-05",
    "p.?",
    "No",
    "CF-causing",
    "c.2908+1G>A",
    "5"
  ],
  "c.2908+1G>A": [
    "3040+1G->A",
    "2.3684783947400833e-05",
    "p.?",
    "No",
    "CF-causing",
    "c.2908+1G>A",
    "5"
  ],
  "621+2T->C": [
    "2.3684783947400833e-05",
    "p.?",
    "No",
    "CF-causing",
    "621+2T->C",
    "c.489+2T>C",
    "5"
  ],
  "c.489+2T>C": [
    "2.3684783947400833e-05",
    "p.?",
    "No",
    "CF-causing",
    "621+2T->C",
    "c.489+2T>C",
    "5"
  ],
  "c.2658-2A>G": [
    "2.3684783947400833e-05",
    "p.?",
    "c.2658-2A>G",
    "No",
    "CF-causing",
    "2790-2A->G",
    "5"
  ],
  "2790-2A->G": [
    "2.3684783947400833e-05",
    "p.?",
    "c.2658-2A>G",
    "No",
    "CF-causing",
    "2790-2A->G",
    "5"
  ],
  "1716+2T->C": [
    "2.3684783947400833e-05",
    "p.?",
    "No",
    "CF-causing",
    "1716+2T->C",
    "5",
    "c.1584+2T>C"
  ],
  "c.1584+2T>C": [
    "2.3684783947400833e-05",
    "p.?",
    "No",
    "CF-causing",
    "1716+2T->C",
    "5",
    "c.1584+2T>C"
  ],
  "c.580-2A>G": [
    "2.3684783947400833e-05",
    "p.?",
    "No",
    "c.580-2A>G",
    "712-2A->G",
    "CF-causing",
    "5"
  ],
  "712-2A->G": [
    "2.3684783947400833e-05",
    "p.?",
    "No",
    "c.580-2A>G",
    "712-2A->G",
    "CF-causing",
    "5"
  ],
  "297-2A->G": [
    "2.3684783947400833e-05",
    "p.?",
    "No",
    "CF-causing",
    "297-2A->G",
    "c.165-2A>G",
    "5"
  ],
  "c.165-2A>G": [
    "2.3684783947400833e-05",
    "p.?",
    "No",
    "CF-causing",
    "297-2A->G",
    "c.165-2A>G",
    "5"
  ],
  "c.1976del": [
    "2.3684783947400833e-05",
    "c.1976del",
    "No",
    "CF-causing",
    "p.Asn659IlefsX4",
    "2108delA",
    "5"
  ],
  "p.Asn659IlefsX4": [
    "2.3684783947400833e-05",
    "c.1976del",
    "No",
    "CF-causing",
    "p.Asn659IlefsX4",
    "2108delA",
    "5"
  ],
  "2108delA": [
    "2.3684783947400833e-05",
    "c.1976del",
    "No",
    "CF-causing",
    "p.Asn659IlefsX4",
    "2108delA",
    "5"
  ],
  "1434delA": [
    "2.3684783947400833e-05",
    "1434delA",
    "No",
    "CF-causing",
    "c.1302del",
    "p.Leu435PhefsX7",
    "5"
  ],
  "c.1302del": [
    "2.3684783947400833e-05",
    "1434delA",
    "No",
    "CF-causing",
    "c.1302del",
    "p.Leu435PhefsX7",
    "5"
  ],
  "p.Leu435PhefsX7": [
    "2.3684783947400833e-05",
    "1434delA",
    "No",
    "CF-causing",
    "c.1302del",
    "p.Leu435PhefsX7",
    "5"
  ],
  "p.Ala412GlnfsX30": [
    "2.3684783947400833e-05",
    "No",
    "p.Ala412GlnfsX30",
    "1366delG",
    "CF-causing",
    "c.1234del",
    "5"
  ],
  "1366delG": [
    "2.3684783947400833e-05",
    "No",
    "p.Ala412GlnfsX30",
    "1366delG",
    "CF-causing",
    "c.1234del",
    "5"
  ],
  "c.1234del": [
    "2.3684783947400833e-05",
    "No",
    "p.Ala412GlnfsX30",
    "1366delG",
    "CF-causing",
    "c.1234del",
    "5"
  ],
  "p.Gly458AspfsX11": [
    "2.3684783947400833e-05",
    "p.Gly458AspfsX11",
    "No",
    "CF-causing",
    "1504delG",
    "c.1373del",
    "5"
  ],
  "1504delG": [
    "2.3684783947400833e-05",
    "p.Gly458AspfsX11",
    "No",
    "CF-causing",
    "1504delG",
    "c.1373del",
    "5"
  ],
  "c.1373del": [
    "2.3684783947400833e-05",
    "p.Gly458AspfsX11",
    "No",
    "CF-causing",
    "1504delG",
    "c.1373del",
    "5"
  ],
  "2723delTT": [
    "2.3684783947400833e-05",
    "No",
    "CF-causing",
    "2723delTT",
    "c.2592_2593del",
    "5",
    "p.Ile864MetfsX31"
  ],
  "c.2592_2593del": [
    "2.3684783947400833e-05",
    "No",
    "CF-causing",
    "2723delTT",
    "c.2592_2593del",
    "5",
    "p.Ile864MetfsX31"
  ],
  "p.Ile864MetfsX31": [
    "2.3684783947400833e-05",
    "No",
    "CF-causing",
    "2723delTT",
    "c.2592_2593del",
    "5",
    "p.Ile864MetfsX31"
  ],
  "c.3600del": [
    "2.3684783947400833e-05",
    "c.3600del",
    "3732delA",
    "No",
    "CF-causing",
    "p.Asp1201MetfsX10",
    "5"
  ],
  "3732delA": [
    "2.3684783947400833e-05",
    "c.3600del",
    "3732delA",
    "No",
    "CF-causing",
    "p.Asp1201MetfsX10",
    "5"
  ],
  "p.Asp1201MetfsX10": [
    "2.3684783947400833e-05",
    "c.3600del",
    "3732delA",
    "No",
    "CF-causing",
    "p.Asp1201MetfsX10",
    "5"
  ],
  "4259del5": [
    "2.3684783947400833e-05",
    "No",
    "4259del5",
    "c.4127_4131del",
    "CF-causing",
    "p.Leu1376SerfsX8",
    "5"
  ],
  "c.4127_4131del": [
    "2.3684783947400833e-05",
    "No",
    "4259del5",
    "c.4127_4131del",
    "CF-causing",
    "p.Leu1376SerfsX8",
    "5"
  ],
  "p.Leu1376SerfsX8": [
    "2.3684783947400833e-05",
    "No",
    "4259del5",
    "c.4127_4131del",
    "CF-causing",
    "p.Leu1376SerfsX8",
    "5"
  ],
  "p.Leu183PhefsX5": [
    "2.3684783947400833e-05",
    "No",
    "CF-causing",
    "p.Leu183PhefsX5",
    "c.543_546del",
    "675del4",
    "5"
  ],
  "c.543_546del": [
    "2.3684783947400833e-05",
    "No",
    "CF-causing",
    "p.Leu183PhefsX5",
    "c.543_546del",
    "675del4",
    "5"
  ],
  "675del4": [
    "2.3684783947400833e-05",
    "No",
    "CF-causing",
    "p.Leu183PhefsX5",
    "c.543_546del",
    "675del4",
    "5"
  ],
  "c.777del": [
    "2.3684783947400833e-05",
    "No",
    "CF-causing",
    "c.777del",
    "909delT",
    "p.Val260X",
    "5"
  ],
  "909delT": [
    "2.3684783947400833e-05",
    "No",
    "CF-causing",
    "c.777del",
    "909delT",
    "p.Val260X",
    "5"
  ],
  "p.Val260X": [
    "2.3684783947400833e-05",
    "No",
    "CF-causing",
    "c.777del",
    "909delT",
    "p.Val260X",
    "5"
  ],
  "712-2A->C": [
    "2.3684783947400833e-05",
    "p.?",
    "712-2A->C",
    "Yes, new variant added",
    "CF-causing",
    "c.580-2A>C",
    "5"
  ],
  "c.580-2A>C": [
    "2.3684783947400833e-05",
    "p.?",
    "712-2A->C",
    "Yes, new variant added",
    "CF-causing",
    "c.580-2A>C",
    "5"
  ],
  "c.2554dup": [
    "2.3684783947400833e-05",
    "c.2554dup",
    "Yes, new variant added",
    "2686dupT",
    "CF-causing",
    "p.Tyr852LeufsX44",
    "5"
  ],
  "2686dupT": [
    "2.3684783947400833e-05",
    "c.2554dup",
    "Yes, new variant added",
    "2686dupT",
    "CF-causing",
    "p.Tyr852LeufsX44",
    "5"
  ],
  "p.Tyr852LeufsX44": [
    "2.3684783947400833e-05",
    "c.2554dup",
    "Yes, new variant added",
    "2686dupT",
    "CF-causing",
    "p.Tyr852LeufsX44",
    "5"
  ],
  "604insA": [
    "2.3684783947400833e-05",
    "604insA",
    "p.Ser158LysfsX5",
    "Yes, new variant added",
    "c.472dup",
    "CF-causing",
    "5"
  ],
  "p.Ser158LysfsX5": [
    "2.3684783947400833e-05",
    "604insA",
    "p.Ser158LysfsX5",
    "Yes, new variant added",
    "c.472dup",
    "CF-causing",
    "5"
  ],
  "c.472dup": [
    "2.3684783947400833e-05",
    "604insA",
    "p.Ser158LysfsX5",
    "Yes, new variant added",
    "c.472dup",
    "CF-causing",
    "5"
  ],
  "c.708del": [
    "2.3684783947400833e-05",
    "Yes, new variant added",
    "CF-causing",
    "c.708del",
    "p.Gln237ArgfsX4",
    "840delT",
    "5"
  ],
  "p.Gln237ArgfsX4": [
    "2.3684783947400833e-05",
    "Yes, new variant added",
    "CF-causing",
    "c.708del",
    "p.Gln237ArgfsX4",
    "840delT",
    "5"
  ],
  "840delT": [
    "2.3684783947400833e-05",
    "Yes, new variant added",
    "CF-causing",
    "c.708del",
    "p.Gln237ArgfsX4",
    "840delT",
    "5"
  ],
  "E292X": [
    "E292X",
    "1.8947827157920666e-05",
    "Yes, new variant added",
    "c.874G>T",
    "4",
    "CF-causing",
    "p.Glu292X",
    "1006G>T"
  ],
  "1.8947827157920666e-05": [
    "Yes, new variant added",
    "4",
    "CF-causing",
    "c.1329_1350del",
    "D443fs",
    "1.8947827157920666e-05",
    "p.Asp443GlufsX19"
  ],
  "c.874G>T": [
    "E292X",
    "1.8947827157920666e-05",
    "Yes, new variant added",
    "c.874G>T",
    "4",
    "CF-causing",
    "p.Glu292X",
    "1006G>T"
  ],
  "4": [
    "Yes, new variant added",
    "4",
    "CF-causing",
    "c.1329_1350del",
    "D443fs",
    "1.8947827157920666e-05",
    "p.Asp443GlufsX19"
  ],
  "p.Glu292X": [
    "E292X",
    "1.8947827157920666e-05",
    "Yes, new variant added",
    "c.874G>T",
    "4",
    "CF-causing",
    "p.Glu292X",
    "1006G>T"
  ],
  "1006G>T": [
    "E292X",
    "1.8947827157920666e-05",
    "Yes, new variant added",
    "c.874G>T",
    "4",
    "CF-causing",
    "p.Glu292X",
    "1006G>T"
  ],
  "p.Ser434LeufsX6": [
    "1.8947827157920666e-05",
    "No",
    "p.Ser434LeufsX6",
    "c.1301_1307del",
    "1429del7",
    "4",
    "CF-causing",
    "1433delCACTTCT"
  ],
  "c.1301_1307del": [
    "1.8947827157920666e-05",
    "No",
    "p.Ser434LeufsX6",
    "c.1301_1307del",
    "1429del7",
    "4",
    "CF-causing",
    "1433delCACTTCT"
  ],
  "1429del7": [
    "1.8947827157920666e-05",
    "No",
    "p.Ser434LeufsX6",
    "c.1301_1307del",
    "1429del7",
    "4",
    "CF-causing",
    "1433delCACTTCT"
  ],
  "1433delCACTTCT": [
    "1.8947827157920666e-05",
    "No",
    "p.Ser434LeufsX6",
    "c.1301_1307del",
    "1429del7",
    "4",
    "CF-causing",
    "1433delCACTTCT"
  ],
  "1552G>A": [
    "No",
    "1552G>A",
    "4",
    "CF-causing",
    "c.1420G>A",
    "p.Glu474Lys",
    "E474K",
    "1.8947827157920666e-05"
  ],
  "c.1420G>A": [
    "No",
    "1552G>A",
    "4",
    "CF-causing",
    "c.1420G>A",
    "p.Glu474Lys",
    "E474K",
    "1.8947827157920666e-05"
  ],
  "p.Glu474Lys": [
    "No",
    "1552G>A",
    "4",
    "CF-causing",
    "c.1420G>A",
    "p.Glu474Lys",
    "E474K",
    "1.8947827157920666e-05"
  ],
  "E474K": [
    "No",
    "1552G>A",
    "4",
    "CF-causing",
    "c.1420G>A",
    "p.Glu474Lys",
    "E474K",
    "1.8947827157920666e-05"
  ],
  "p.Glu514X": [
    "p.Glu514X",
    "E514X",
    "No",
    "1672G>T",
    "4",
    "CF-causing",
    "1.8947827157920666e-05",
    "c.1540G>T"
  ],
  "E514X": [
    "p.Glu514X",
    "E514X",
    "No",
    "1672G>T",
    "4",
    "CF-causing",
    "1.8947827157920666e-05",
    "c.1540G>T"
  ],
  "1672G>T": [
    "p.Glu514X",
    "E514X",
    "No",
    "1672G>T",
    "4",
    "CF-causing",
    "1.8947827157920666e-05",
    "c.1540G>T"
  ],
  "c.1540G>T": [
    "p.Glu514X",
    "E514X",
    "No",
    "1672G>T",
    "4",
    "CF-causing",
    "1.8947827157920666e-05",
    "c.1540G>T"
  ],
  "Y563X": [
    "Y563X",
    "p.Tyr563X",
    "1821C>A",
    "No",
    "4",
    "CF-causing",
    "c.1689C>A",
    "1.8947827157920666e-05"
  ],
  "p.Tyr563X": [
    "Y563X",
    "p.Tyr563X",
    "1821C>A",
    "No",
    "4",
    "CF-causing",
    "c.1689C>A",
    "1.8947827157920666e-05"
  ],
  "1821C>A": [
    "Y563X",
    "p.Tyr563X",
    "1821C>A",
    "No",
    "4",
    "CF-causing",
    "c.1689C>A",
    "1.8947827157920666e-05"
  ],
  "c.1689C>A": [
    "Y563X",
    "p.Tyr563X",
    "1821C>A",
    "No",
    "4",
    "CF-causing",
    "c.1689C>A",
    "1.8947827157920666e-05"
  ],
  "p.Gln652X": [
    "1.8947827157920666e-05",
    "No",
    "p.Gln652X",
    "Q652X",
    "4",
    "CF-causing",
    "c.1954C>T",
    "2086C>T"
  ],
  "Q652X": [
    "1.8947827157920666e-05",
    "No",
    "p.Gln652X",
    "Q652X",
    "4",
    "CF-causing",
    "c.1954C>T",
    "2086C>T"
  ],
  "c.1954C>T": [
    "1.8947827157920666e-05",
    "No",
    "p.Gln652X",
    "Q652X",
    "4",
    "CF-causing",
    "c.1954C>T",
    "2086C>T"
  ],
  "2086C>T": [
    "1.8947827157920666e-05",
    "No",
    "p.Gln652X",
    "Q652X",
    "4",
    "CF-causing",
    "c.1954C>T",
    "2086C>T"
  ],
  "c.2053C>T": [
    "c.2053C>T",
    "No",
    "p.Gln685X",
    "2185C>T",
    "4",
    "CF-causing",
    "Q685X",
    "1.8947827157920666e-05"
  ],
  "p.Gln685X": [
    "c.2053C>T",
    "No",
    "p.Gln685X",
    "2185C>T",
    "4",
    "CF-causing",
    "Q685X",
    "1.8947827157920666e-05"
  ],
  "2185C>T": [
    "c.2053C>T",
    "No",
    "p.Gln685X",
    "2185C>T",
    "4",
    "CF-causing",
    "Q685X",
    "1.8947827157920666e-05"
  ],
  "Q685X": [
    "c.2053C>T",
    "No",
    "p.Gln685X",
    "2185C>T",
    "4",
    "CF-causing",
    "Q685X",
    "1.8947827157920666e-05"
  ],
  "c.2143C>T": [
    "c.2143C>T",
    "No",
    "2275C>T",
    "4",
    "CF-causing",
    "Q715X",
    "p.Gln715X",
    "1.8947827157920666e-05"
  ],
  "2275C>T": [
    "c.2143C>T",
    "No",
    "2275C>T",
    "4",
    "CF-causing",
    "Q715X",
    "p.Gln715X",
    "1.8947827157920666e-05"
  ],
  "Q715X": [
    "c.2143C>T",
    "No",
    "2275C>T",
    "4",
    "CF-causing",
    "Q715X",
    "p.Gln715X",
    "1.8947827157920666e-05"
  ],
  "p.Gln715X": [
    "c.2143C>T",
    "No",
    "2275C>T",
    "4",
    "CF-causing",
    "Q715X",
    "p.Gln715X",
    "1.8947827157920666e-05"
  ],
  "c.2770G>A": [
    "c.2770G>A",
    "2902G>A",
    "4",
    "Varying clinical consequence",
    "Yes",
    "D924N",
    "p.Asp924Asn",
    "Unknown significance",
    "1.8947827157920666e-05"
  ],
  "2902G>A": [
    "c.2770G>A",
    "2902G>A",
    "4",
    "Varying clinical consequence",
    "Yes",
    "D924N",
    "p.Asp924Asn",
    "Unknown significance",
    "1.8947827157920666e-05"
  ],
  "D924N": [
    "c.2770G>A",
    "2902G>A",
    "4",
    "Varying clinical consequence",
    "Yes",
    "D924N",
    "p.Asp924Asn",
    "Unknown significance",
    "1.8947827157920666e-05"
  ],
  "p.Asp924Asn": [
    "c.2770G>A",
    "2902G>A",
    "4",
    "Varying clinical consequence",
    "Yes",
    "D924N",
    "p.Asp924Asn",
    "Unknown significance",
    "1.8947827157920666e-05"
  ],
  "p.Lys978X": [
    "No",
    "p.Lys978X",
    "4",
    "K978X",
    "CF-causing",
    "3064A>T",
    "c.2932A>T",
    "1.8947827157920666e-05"
  ],
  "K978X": [
    "No",
    "p.Lys978X",
    "4",
    "K978X",
    "CF-causing",
    "3064A>T",
    "c.2932A>T",
    "1.8947827157920666e-05"
  ],
  "3064A>T": [
    "No",
    "p.Lys978X",
    "4",
    "K978X",
    "CF-causing",
    "3064A>T",
    "c.2932A>T",
    "1.8947827157920666e-05"
  ],
  "c.2932A>T": [
    "No",
    "p.Lys978X",
    "4",
    "K978X",
    "CF-causing",
    "3064A>T",
    "c.2932A>T",
    "1.8947827157920666e-05"
  ],
  "c.3189G>A": [
    "c.3189G>A",
    "W1063X",
    "No",
    "3321G>A",
    "p.Trp1063X",
    "4",
    "CF-causing",
    "1.8947827157920666e-05"
  ],
  "W1063X": [
    "c.3189G>A",
    "W1063X",
    "No",
    "3321G>A",
    "p.Trp1063X",
    "4",
    "CF-causing",
    "1.8947827157920666e-05"
  ],
  "3321G>A": [
    "c.3189G>A",
    "W1063X",
    "No",
    "3321G>A",
    "p.Trp1063X",
    "4",
    "CF-causing",
    "1.8947827157920666e-05"
  ],
  "p.Trp1063X": [
    "c.3189G>A",
    "W1063X",
    "No",
    "3321G>A",
    "p.Trp1063X",
    "4",
    "CF-causing",
    "1.8947827157920666e-05"
  ],
  "c.202A>T": [
    "No",
    "c.202A>T",
    "4",
    "CF-causing",
    "p.Lys68X",
    "334A>T",
    "K68X",
    "1.8947827157920666e-05"
  ],
  "p.Lys68X": [
    "No",
    "c.202A>T",
    "4",
    "CF-causing",
    "p.Lys68X",
    "334A>T",
    "K68X",
    "1.8947827157920666e-05"
  ],
  "334A>T": [
    "No",
    "c.202A>T",
    "4",
    "CF-causing",
    "p.Lys68X",
    "334A>T",
    "K68X",
    "1.8947827157920666e-05"
  ],
  "K68X": [
    "No",
    "c.202A>T",
    "4",
    "CF-causing",
    "p.Lys68X",
    "334A>T",
    "K68X",
    "1.8947827157920666e-05"
  ],
  "c.3904A>T": [
    "No",
    "c.3904A>T",
    "4",
    "CF-causing",
    "p.Lys1302X",
    "4036A>T",
    "K1302X",
    "1.8947827157920666e-05"
  ],
  "p.Lys1302X": [
    "No",
    "c.3904A>T",
    "4",
    "CF-causing",
    "p.Lys1302X",
    "4036A>T",
    "K1302X",
    "1.8947827157920666e-05"
  ],
  "4036A>T": [
    "No",
    "c.3904A>T",
    "4",
    "CF-causing",
    "p.Lys1302X",
    "4036A>T",
    "K1302X",
    "1.8947827157920666e-05"
  ],
  "K1302X": [
    "No",
    "c.3904A>T",
    "4",
    "CF-causing",
    "p.Lys1302X",
    "4036A>T",
    "K1302X",
    "1.8947827157920666e-05"
  ],
  "E1308X": [
    "E1308X",
    "Yes, new variant added",
    "p.Glu1308X",
    "4",
    "CF-causing",
    "c.3922G>T",
    "4054G>T",
    "1.8947827157920666e-05"
  ],
  "p.Glu1308X": [
    "E1308X",
    "Yes, new variant added",
    "p.Glu1308X",
    "4",
    "CF-causing",
    "c.3922G>T",
    "4054G>T",
    "1.8947827157920666e-05"
  ],
  "c.3922G>T": [
    "E1308X",
    "Yes, new variant added",
    "p.Glu1308X",
    "4",
    "CF-causing",
    "c.3922G>T",
    "4054G>T",
    "1.8947827157920666e-05"
  ],
  "4054G>T": [
    "E1308X",
    "Yes, new variant added",
    "p.Glu1308X",
    "4",
    "CF-causing",
    "c.3922G>T",
    "4054G>T",
    "1.8947827157920666e-05"
  ],
  "p.Gln1309X": [
    "p.Gln1309X",
    "c.3925C>T",
    "No",
    "4",
    "CF-causing",
    "Q1309X",
    "4057C>T",
    "1.8947827157920666e-05"
  ],
  "c.3925C>T": [
    "p.Gln1309X",
    "c.3925C>T",
    "No",
    "4",
    "CF-causing",
    "Q1309X",
    "4057C>T",
    "1.8947827157920666e-05"
  ],
  "Q1309X": [
    "p.Gln1309X",
    "c.3925C>T",
    "No",
    "4",
    "CF-causing",
    "Q1309X",
    "4057C>T",
    "1.8947827157920666e-05"
  ],
  "4057C>T": [
    "p.Gln1309X",
    "c.3925C>T",
    "No",
    "4",
    "CF-causing",
    "Q1309X",
    "4057C>T",
    "1.8947827157920666e-05"
  ],
  "c.619C>T": [
    "c.619C>T",
    "No",
    "Q207X",
    "4",
    "CF-causing",
    "p.Gln207X",
    "751C>T",
    "1.8947827157920666e-05"
  ],
  "Q207X": [
    "c.619C>T",
    "No",
    "Q207X",
    "4",
    "CF-causing",
    "p.Gln207X",
    "751C>T",
    "1.8947827157920666e-05"
  ],
  "p.Gln207X": [
    "c.619C>T",
    "No",
    "Q207X",
    "4",
    "CF-causing",
    "p.Gln207X",
    "751C>T",
    "1.8947827157920666e-05"
  ],
  "751C>T": [
    "c.619C>T",
    "No",
    "Q207X",
    "4",
    "CF-causing",
    "p.Gln207X",
    "751C>T",
    "1.8947827157920666e-05"
  ],
  "W216X": [
    "No",
    "W216X",
    "4",
    "p.Trp216X",
    "CF-causing",
    "c.647G>A|c.648G>A",
    "1.8947827157920666e-05",
    "779G>A"
  ],
  "p.Trp216X": [
    "No",
    "W216X",
    "4",
    "p.Trp216X",
    "CF-causing",
    "c.647G>A|c.648G>A",
    "1.8947827157920666e-05",
    "779G>A"
  ],
  "c.647G>A|c.648G>A": [
    "No",
    "W216X",
    "4",
    "p.Trp216X",
    "CF-causing",
    "c.647G>A|c.648G>A",
    "1.8947827157920666e-05",
    "779G>A"
  ],
  "779G>A": [
    "No",
    "W216X",
    "4",
    "p.Trp216X",
    "CF-causing",
    "c.647G>A|c.648G>A",
    "1.8947827157920666e-05",
    "779G>A"
  ],
  "3349insT": [
    "3349insT",
    "c.3217dup",
    "p.Tyr1073LeufsX3",
    "No",
    "c.3217_3218insT",
    "4",
    "CF-causing",
    "1.8947827157920666e-05"
  ],
  "c.3217dup": [
    "3349insT",
    "c.3217dup",
    "p.Tyr1073LeufsX3",
    "No",
    "c.3217_3218insT",
    "4",
    "CF-causing",
    "1.8947827157920666e-05"
  ],
  "p.Tyr1073LeufsX3": [
    "3349insT",
    "c.3217dup",
    "p.Tyr1073LeufsX3",
    "No",
    "c.3217_3218insT",
    "4",
    "CF-causing",
    "1.8947827157920666e-05"
  ],
  "c.3217_3218insT": [
    "3349insT",
    "c.3217dup",
    "p.Tyr1073LeufsX3",
    "No",
    "c.3217_3218insT",
    "4",
    "CF-causing",
    "1.8947827157920666e-05"
  ],
  "c.(3139+1_3140-1)_(3367+1_3368-1)del": [
    "c.(3139+1_3140-1)_(3367+1_3368-1)del",
    "deletion of exon 17b (legacy numbering)|deletion of exon 20 (current numbering)",
    "p.?",
    "No",
    "CFTRdele17b",
    "4",
    "CF-causing",
    "1.8947827157920666e-05"
  ],
  "deletion of exon 17b (legacy numbering)|deletion of exon 20 (current numbering)": [
    "c.(3139+1_3140-1)_(3367+1_3368-1)del",
    "deletion of exon 17b (legacy numbering)|deletion of exon 20 (current numbering)",
    "p.?",
    "No",
    "CFTRdele17b",
    "4",
    "CF-causing",
    "1.8947827157920666e-05"
  ],
  "CFTRdele17b": [
    "c.(3139+1_3140-1)_(3367+1_3368-1)del",
    "deletion of exon 17b (legacy numbering)|deletion of exon 20 (current numbering)",
    "p.?",
    "No",
    "CFTRdele17b",
    "4",
    "CF-causing",
    "1.8947827157920666e-05"
  ],
  "duplication of exons 1 through 3 (legacy and current numbering)": [
    "duplication of exons 1 through 3 (legacy and current numbering)",
    "p.?",
    "Yes, new variant added",
    "c.(?_1)_(273+1_274-1)dup",
    "4",
    "CF-causing",
    "CFTRdup1-3",
    "1.8947827157920666e-05"
  ],
  "c.(?_1)_(273+1_274-1)dup": [
    "duplication of exons 1 through 3 (legacy and current numbering)",
    "p.?",
    "Yes, new variant added",
    "c.(?_1)_(273+1_274-1)dup",
    "4",
    "CF-causing",
    "CFTRdup1-3",
    "1.8947827157920666e-05"
  ],
  "CFTRdup1-3": [
    "duplication of exons 1 through 3 (legacy and current numbering)",
    "p.?",
    "Yes, new variant added",
    "c.(?_1)_(273+1_274-1)dup",
    "4",
    "CF-causing",
    "CFTRdup1-3",
    "1.8947827157920666e-05"
  ],
  "F508C in cis with S1251N|[1655T>G with 3884G>A]": [
    "No",
    "F508C in cis with S1251N|[1655T>G with 3884G>A]",
    "4",
    "CF-causing",
    "c.[1523T>G;3752G>A]",
    "F508C;S1251N",
    "1.8947827157920666e-05"
  ],
  "c.[1523T>G;3752G>A]": [
    "No",
    "F508C in cis with S1251N|[1655T>G with 3884G>A]",
    "4",
    "CF-causing",
    "c.[1523T>G;3752G>A]",
    "F508C;S1251N",
    "1.8947827157920666e-05"
  ],
  "F508C;S1251N": [
    "No",
    "F508C in cis with S1251N|[1655T>G with 3884G>A]",
    "4",
    "CF-causing",
    "c.[1523T>G;3752G>A]",
    "F508C;S1251N",
    "1.8947827157920666e-05"
  ],
  "c.274-1G>C": [
    "p.?",
    "No",
    "c.274-1G>C",
    "4",
    "CF-causing",
    "406-1G->C",
    "1.8947827157920666e-05"
  ],
  "406-1G->C": [
    "p.?",
    "No",
    "c.274-1G>C",
    "4",
    "CF-causing",
    "406-1G->C",
    "1.8947827157920666e-05"
  ],
  "c.2620-2A>G": [
    "p.?",
    "No",
    "4",
    "CF-causing",
    "c.2620-2A>G",
    "1.8947827157920666e-05",
    "2752-2A->G"
  ],
  "2752-2A->G": [
    "p.?",
    "No",
    "4",
    "CF-causing",
    "c.2620-2A>G",
    "1.8947827157920666e-05",
    "2752-2A->G"
  ],
  "876-2A->G": [
    "p.?",
    "No",
    "4",
    "CF-causing",
    "876-2A->G",
    "c.744-2A>G",
    "1.8947827157920666e-05"
  ],
  "c.744-2A>G": [
    "p.?",
    "No",
    "4",
    "CF-causing",
    "876-2A->G",
    "c.744-2A>G",
    "1.8947827157920666e-05"
  ],
  "3940delG": [
    "No",
    "4",
    "CF-causing",
    "3940delG",
    "c.3808del",
    "p.Asp1270MetfsX8",
    "1.8947827157920666e-05"
  ],
  "c.3808del": [
    "No",
    "4",
    "CF-causing",
    "3940delG",
    "c.3808del",
    "p.Asp1270MetfsX8",
    "1.8947827157920666e-05"
  ],
  "p.Asp1270MetfsX8": [
    "No",
    "4",
    "CF-causing",
    "3940delG",
    "c.3808del",
    "p.Asp1270MetfsX8",
    "1.8947827157920666e-05"
  ],
  "p.Lys166AsnfsX7": [
    "p.Lys166AsnfsX7",
    "No",
    "c.498del",
    "4",
    "CF-causing",
    "630delG",
    "1.8947827157920666e-05"
  ],
  "c.498del": [
    "p.Lys166AsnfsX7",
    "No",
    "c.498del",
    "4",
    "CF-causing",
    "630delG",
    "1.8947827157920666e-05"
  ],
  "630delG": [
    "p.Lys166AsnfsX7",
    "No",
    "c.498del",
    "4",
    "CF-causing",
    "630delG",
    "1.8947827157920666e-05"
  ],
  "c.874_875del": [
    "c.874_875del",
    "No",
    "p.Glu292ThrfsX15",
    "1006_1007delGA",
    "4",
    "CF-causing",
    "1.8947827157920666e-05"
  ],
  "p.Glu292ThrfsX15": [
    "c.874_875del",
    "No",
    "p.Glu292ThrfsX15",
    "1006_1007delGA",
    "4",
    "CF-causing",
    "1.8947827157920666e-05"
  ],
  "1006_1007delGA": [
    "c.874_875del",
    "No",
    "p.Glu292ThrfsX15",
    "1006_1007delGA",
    "4",
    "CF-causing",
    "1.8947827157920666e-05"
  ],
  "c.461dup": [
    "No",
    "c.461dup",
    "4",
    "CF-causing",
    "593insT",
    "p.Ala155SerfsX4",
    "1.8947827157920666e-05"
  ],
  "593insT": [
    "No",
    "c.461dup",
    "4",
    "CF-causing",
    "593insT",
    "p.Ala155SerfsX4",
    "1.8947827157920666e-05"
  ],
  "p.Ala155SerfsX4": [
    "No",
    "c.461dup",
    "4",
    "CF-causing",
    "593insT",
    "p.Ala155SerfsX4",
    "1.8947827157920666e-05"
  ],
  "p.Ile255ThrfsX6": [
    "No",
    "p.Ile255ThrfsX6",
    "4",
    "896delT",
    "CF-causing",
    "c.764del",
    "1.8947827157920666e-05"
  ],
  "896delT": [
    "No",
    "p.Ile255ThrfsX6",
    "4",
    "896delT",
    "CF-causing",
    "c.764del",
    "1.8947827157920666e-05"
  ],
  "c.764del": [
    "No",
    "p.Ile255ThrfsX6",
    "4",
    "896delT",
    "CF-causing",
    "c.764del",
    "1.8947827157920666e-05"
  ],
  "p.Asp648ValfsX15": [
    "No",
    "p.Asp648ValfsX15",
    "2075delA",
    "4",
    "CF-causing",
    "c.1943del",
    "1.8947827157920666e-05"
  ],
  "2075delA": [
    "No",
    "p.Asp648ValfsX15",
    "2075delA",
    "4",
    "CF-causing",
    "c.1943del",
    "1.8947827157920666e-05"
  ],
  "c.1943del": [
    "No",
    "p.Asp648ValfsX15",
    "2075delA",
    "4",
    "CF-causing",
    "c.1943del",
    "1.8947827157920666e-05"
  ],
  "c.550del": [
    "No",
    "c.550del",
    "4",
    "681delC",
    "CF-causing",
    "p.Leu184PhefsX5",
    "1.8947827157920666e-05"
  ],
  "681delC": [
    "No",
    "c.550del",
    "4",
    "681delC",
    "CF-causing",
    "p.Leu184PhefsX5",
    "1.8947827157920666e-05"
  ],
  "p.Leu184PhefsX5": [
    "No",
    "c.550del",
    "4",
    "681delC",
    "CF-causing",
    "p.Leu184PhefsX5",
    "1.8947827157920666e-05"
  ],
  "1199delG": [
    "No",
    "4",
    "CF-causing",
    "1199delG",
    "c.1069del",
    "p.Ala357LeufsX12",
    "1.8947827157920666e-05"
  ],
  "c.1069del": [
    "No",
    "4",
    "CF-causing",
    "1199delG",
    "c.1069del",
    "p.Ala357LeufsX12",
    "1.8947827157920666e-05"
  ],
  "p.Ala357LeufsX12": [
    "No",
    "4",
    "CF-causing",
    "1199delG",
    "c.1069del",
    "p.Ala357LeufsX12",
    "1.8947827157920666e-05"
  ],
  "p.Phe834LeufsX10": [
    "p.Phe834LeufsX10",
    "No",
    "2634delT",
    "4",
    "CF-causing",
    "1.8947827157920666e-05",
    "c.2502del"
  ],
  "2634delT": [
    "p.Phe834LeufsX10",
    "No",
    "2634delT",
    "4",
    "CF-causing",
    "1.8947827157920666e-05",
    "c.2502del"
  ],
  "c.2502del": [
    "p.Phe834LeufsX10",
    "No",
    "2634delT",
    "4",
    "CF-causing",
    "1.8947827157920666e-05",
    "c.2502del"
  ],
  "c.3397del": [
    "c.3397del",
    "No",
    "4",
    "p.Leu1133X",
    "CF-causing",
    "3528delC",
    "1.8947827157920666e-05"
  ],
  "p.Leu1133X": [
    "c.3397del",
    "No",
    "4",
    "p.Leu1133X",
    "CF-causing",
    "3528delC",
    "1.8947827157920666e-05"
  ],
  "3528delC": [
    "c.3397del",
    "No",
    "4",
    "p.Leu1133X",
    "CF-causing",
    "3528delC",
    "1.8947827157920666e-05"
  ],
  "3662delA": [
    "p.Lys1177SerfsX15",
    "No",
    "3662delA",
    "4",
    "CF-causing",
    "c.3530del",
    "1.8947827157920666e-05"
  ],
  "c.3530del": [
    "p.Lys1177SerfsX15",
    "No",
    "3662delA",
    "4",
    "CF-causing",
    "c.3530del",
    "1.8947827157920666e-05"
  ],
  "c.980del": [
    "No",
    "c.980del",
    "1112delT",
    "4",
    "CF-causing",
    "p.Leu327GlnfsX42",
    "1.8947827157920666e-05"
  ],
  "1112delT": [
    "No",
    "c.980del",
    "1112delT",
    "4",
    "CF-causing",
    "p.Leu327GlnfsX42",
    "1.8947827157920666e-05"
  ],
  "p.Leu327GlnfsX42": [
    "No",
    "c.980del",
    "1112delT",
    "4",
    "CF-causing",
    "p.Leu327GlnfsX42",
    "1.8947827157920666e-05"
  ],
  "p.Ser557PhefsX2": [
    "No",
    "p.Ser557PhefsX2",
    "4",
    "c.1670del",
    "CF-causing",
    "1802delC",
    "1.8947827157920666e-05"
  ],
  "c.1670del": [
    "No",
    "p.Ser557PhefsX2",
    "4",
    "c.1670del",
    "CF-causing",
    "1802delC",
    "1.8947827157920666e-05"
  ],
  "1802delC": [
    "No",
    "p.Ser557PhefsX2",
    "4",
    "c.1670del",
    "CF-causing",
    "1802delC",
    "1.8947827157920666e-05"
  ],
  "c.49_50dup": [
    "c.49_50dup",
    "No",
    "4",
    "CF-causing",
    "181_182dup",
    "1.8947827157920666e-05",
    "p.Trp19AlafsX7"
  ],
  "181_182dup": [
    "c.49_50dup",
    "No",
    "4",
    "CF-causing",
    "181_182dup",
    "1.8947827157920666e-05",
    "p.Trp19AlafsX7"
  ],
  "p.Trp19AlafsX7": [
    "c.49_50dup",
    "No",
    "4",
    "CF-causing",
    "181_182dup",
    "1.8947827157920666e-05",
    "p.Trp19AlafsX7"
  ],
  "4271delC": [
    "4271delC",
    "No",
    "4",
    "p.Thr1380AsnfsX4",
    "CF-causing",
    "c.4139del",
    "1.8947827157920666e-05"
  ],
  "p.Thr1380AsnfsX4": [
    "4271delC",
    "No",
    "4",
    "p.Thr1380AsnfsX4",
    "CF-causing",
    "c.4139del",
    "1.8947827157920666e-05"
  ],
  "c.4139del": [
    "4271delC",
    "No",
    "4",
    "p.Thr1380AsnfsX4",
    "CF-causing",
    "c.4139del",
    "1.8947827157920666e-05"
  ],
  "p.Gly1208ProfsX56": [
    "p.Gly1208ProfsX56",
    "3750delAG",
    "No",
    "4",
    "CF-causing",
    "c.3618_3619del",
    "1.8947827157920666e-05"
  ],
  "3750delAG": [
    "p.Gly1208ProfsX56",
    "3750delAG",
    "No",
    "4",
    "CF-causing",
    "c.3618_3619del",
    "1.8947827157920666e-05"
  ],
  "c.3618_3619del": [
    "p.Gly1208ProfsX56",
    "3750delAG",
    "No",
    "4",
    "CF-causing",
    "c.3618_3619del",
    "1.8947827157920666e-05"
  ],
  "c.164+4dup": [
    "c.164+4dup",
    "p.?",
    "No",
    "4",
    "296+3insT",
    "CF-causing",
    "1.8947827157920666e-05"
  ],
  "296+3insT": [
    "c.164+4dup",
    "p.?",
    "No",
    "4",
    "296+3insT",
    "CF-causing",
    "1.8947827157920666e-05"
  ],
  "c.578_579+5del": [
    "p.?",
    "c.578_579+5del",
    "No",
    "4",
    "CF-causing",
    "710_711+5del7",
    "1.8947827157920666e-05"
  ],
  "710_711+5del7": [
    "p.?",
    "c.578_579+5del",
    "No",
    "4",
    "CF-causing",
    "710_711+5del7",
    "1.8947827157920666e-05"
  ],
  "3271+1delG": [
    "p.?",
    "Yes, new variant added",
    "4",
    "CF-causing",
    "3271+1delG",
    "1.8947827157920666e-05",
    "c.3139+1del"
  ],
  "c.3139+1del": [
    "p.?",
    "Yes, new variant added",
    "4",
    "CF-causing",
    "3271+1delG",
    "1.8947827157920666e-05",
    "c.3139+1del"
  ],
  "c.3883_3884insG": [
    "c.3883_3884insG",
    "Yes, new variant added",
    "CF-causing",
    "4",
    "p.Ile1295SerfsX7",
    "1.8947827157920666e-05"
  ],
  "p.Ile1295SerfsX7": [
    "c.3883_3884insG",
    "Yes, new variant added",
    "CF-causing",
    "4",
    "p.Ile1295SerfsX7",
    "1.8947827157920666e-05"
  ],
  "p.Ser686AsnfsX37": [
    "Yes, new variant added",
    "p.Ser686AsnfsX37",
    "4",
    "CF-causing",
    "c.2053_2054insAA",
    "1.8947827157920666e-05"
  ],
  "c.2053_2054insAA": [
    "Yes, new variant added",
    "p.Ser686AsnfsX37",
    "4",
    "CF-causing",
    "c.2053_2054insAA",
    "1.8947827157920666e-05"
  ],
  "c.1656del": [
    "c.1656del",
    "Yes, new variant added",
    "4",
    "CF-causing",
    "p.Gln552HisfsX7",
    "1787delA",
    "1.8947827157920666e-05"
  ],
  "p.Gln552HisfsX7": [
    "c.1656del",
    "Yes, new variant added",
    "4",
    "CF-causing",
    "p.Gln552HisfsX7",
    "1787delA",
    "1.8947827157920666e-05"
  ],
  "1787delA": [
    "c.1656del",
    "Yes, new variant added",
    "4",
    "CF-causing",
    "p.Gln552HisfsX7",
    "1787delA",
    "1.8947827157920666e-05"
  ],
  "c.1329_1350del": [
    "Yes, new variant added",
    "4",
    "CF-causing",
    "c.1329_1350del",
    "D443fs",
    "1.8947827157920666e-05",
    "p.Asp443GlufsX19"
  ],
  "D443fs": [
    "Yes, new variant added",
    "4",
    "CF-causing",
    "c.1329_1350del",
    "D443fs",
    "1.8947827157920666e-05",
    "p.Asp443GlufsX19"
  ],
  "p.Asp443GlufsX19": [
    "Yes, new variant added",
    "4",
    "CF-causing",
    "c.1329_1350del",
    "D443fs",
    "1.8947827157920666e-05",
    "p.Asp443GlufsX19"
  ],
  "3": [
    "c.3477del",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CF-causing",
    "p.Val1160X",
    "c.3477delT"
  ],
  "1.4210870368440498e-05": [
    "c.3477del",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CF-causing",
    "p.Val1160X",
    "c.3477delT"
  ],
  "1200G>A": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "1200G>A",
    "W356X",
    "p.Trp356X",
    "CF-causing",
    "c.1068G>A"
  ],
  "W356X": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "1200G>A",
    "W356X",
    "p.Trp356X",
    "CF-causing",
    "c.1068G>A"
  ],
  "p.Trp356X": [
    "4.7369567894801664e-06",
    "1200_1219del20",
    "Yes, new variant added",
    "p.Trp356X",
    "c.1068_1087del",
    "CF-causing",
    "1"
  ],
  "c.1068G>A": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "1200G>A",
    "W356X",
    "p.Trp356X",
    "CF-causing",
    "c.1068G>A"
  ],
  "p.Trp361X": [
    "p.Trp361X",
    "3",
    "1.4210870368440498e-05",
    "No",
    "1214G>A|1215G>A",
    "W361X",
    "CF-causing",
    "c.1082G>A|c.1083G>A"
  ],
  "1214G>A|1215G>A": [
    "p.Trp361X",
    "3",
    "1.4210870368440498e-05",
    "No",
    "1214G>A|1215G>A",
    "W361X",
    "CF-causing",
    "c.1082G>A|c.1083G>A"
  ],
  "W361X": [
    "p.Trp361X",
    "3",
    "1.4210870368440498e-05",
    "No",
    "1214G>A|1215G>A",
    "W361X",
    "CF-causing",
    "c.1082G>A|c.1083G>A"
  ],
  "c.1082G>A|c.1083G>A": [
    "p.Trp361X",
    "3",
    "1.4210870368440498e-05",
    "No",
    "1214G>A|1215G>A",
    "W361X",
    "CF-causing",
    "c.1082G>A|c.1083G>A"
  ],
  "p.Lys381X": [
    "3",
    "1.4210870368440498e-05",
    "p.Lys381X",
    "Yes, new variant added",
    "c.1141A>T",
    "CF-causing",
    "K381X",
    "1273A>T"
  ],
  "c.1141A>T": [
    "3",
    "1.4210870368440498e-05",
    "p.Lys381X",
    "Yes, new variant added",
    "c.1141A>T",
    "CF-causing",
    "K381X",
    "1273A>T"
  ],
  "K381X": [
    "3",
    "1.4210870368440498e-05",
    "p.Lys381X",
    "Yes, new variant added",
    "c.1141A>T",
    "CF-causing",
    "K381X",
    "1273A>T"
  ],
  "1273A>T": [
    "3",
    "1.4210870368440498e-05",
    "p.Lys381X",
    "Yes, new variant added",
    "c.1141A>T",
    "CF-causing",
    "K381X",
    "1273A>T"
  ],
  "p.Tyr577X": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "p.Tyr577X",
    "1863C>A",
    "Y577X",
    "c.1731C>A"
  ],
  "1863C>A": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "p.Tyr577X",
    "1863C>A",
    "Y577X",
    "c.1731C>A"
  ],
  "Y577X": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "p.Tyr577X",
    "1863C>A",
    "Y577X",
    "c.1731C>A"
  ],
  "c.1731C>A": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "p.Tyr577X",
    "1863C>A",
    "Y577X",
    "c.1731C>A"
  ],
  "K598X": [
    "K598X",
    "3",
    "1.4210870368440498e-05",
    "No",
    "c.1792A>T",
    "CF-causing",
    "p.Lys598X",
    "1924A>T"
  ],
  "c.1792A>T": [
    "K598X",
    "3",
    "1.4210870368440498e-05",
    "No",
    "c.1792A>T",
    "CF-causing",
    "p.Lys598X",
    "1924A>T"
  ],
  "p.Lys598X": [
    "K598X",
    "3",
    "1.4210870368440498e-05",
    "No",
    "c.1792A>T",
    "CF-causing",
    "p.Lys598X",
    "1924A>T"
  ],
  "1924A>T": [
    "K598X",
    "3",
    "1.4210870368440498e-05",
    "No",
    "c.1792A>T",
    "CF-causing",
    "p.Lys598X",
    "1924A>T"
  ],
  "E656X": [
    "3",
    "E656X",
    "1.4210870368440498e-05",
    "No",
    "c.1966G>T",
    "CF-causing",
    "p.Glu656X",
    "2098G>T"
  ],
  "c.1966G>T": [
    "3",
    "E656X",
    "1.4210870368440498e-05",
    "No",
    "c.1966G>T",
    "CF-causing",
    "p.Glu656X",
    "2098G>T"
  ],
  "p.Glu656X": [
    "3",
    "E656X",
    "1.4210870368440498e-05",
    "No",
    "c.1966G>T",
    "CF-causing",
    "p.Glu656X",
    "2098G>T"
  ],
  "2098G>T": [
    "3",
    "E656X",
    "1.4210870368440498e-05",
    "No",
    "c.1966G>T",
    "CF-causing",
    "p.Glu656X",
    "2098G>T"
  ],
  "2168G>A": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "2168G>A",
    "CF-causing",
    "W679X",
    "c.2036G>A|c.2037G>A",
    "p.Trp679X"
  ],
  "W679X": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "2168G>A",
    "CF-causing",
    "W679X",
    "c.2036G>A|c.2037G>A",
    "p.Trp679X"
  ],
  "c.2036G>A|c.2037G>A": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "2168G>A",
    "CF-causing",
    "W679X",
    "c.2036G>A|c.2037G>A",
    "p.Trp679X"
  ],
  "p.Trp679X": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "2168G>A",
    "CF-causing",
    "W679X",
    "c.2036G>A|c.2037G>A",
    "p.Trp679X"
  ],
  "p.Glu33X": [
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "p.Glu33X",
    "c.97G>T",
    "CF-causing",
    "229G>T",
    "E33X"
  ],
  "c.97G>T": [
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "p.Glu33X",
    "c.97G>T",
    "CF-causing",
    "229G>T",
    "E33X"
  ],
  "229G>T": [
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "p.Glu33X",
    "c.97G>T",
    "CF-causing",
    "229G>T",
    "E33X"
  ],
  "E33X": [
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "p.Glu33X",
    "c.97G>T",
    "CF-causing",
    "229G>T",
    "E33X"
  ],
  "S962X": [
    "S962X",
    "c.2885C>A|c.2885C>G",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "p.Ser962X",
    "3017C>A|3017C>G"
  ],
  "c.2885C>A|c.2885C>G": [
    "S962X",
    "c.2885C>A|c.2885C>G",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "p.Ser962X",
    "3017C>A|3017C>G"
  ],
  "p.Ser962X": [
    "S962X",
    "c.2885C>A|c.2885C>G",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "p.Ser962X",
    "3017C>A|3017C>G"
  ],
  "3017C>A|3017C>G": [
    "S962X",
    "c.2885C>A|c.2885C>G",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "p.Ser962X",
    "3017C>A|3017C>G"
  ],
  "D979V": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "D979V",
    "p.Asp979Val",
    "CF-causing",
    "3068A>T",
    "c.2936A>T"
  ],
  "p.Asp979Val": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "D979V",
    "p.Asp979Val",
    "CF-causing",
    "3068A>T",
    "c.2936A>T"
  ],
  "3068A>T": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "D979V",
    "p.Asp979Val",
    "CF-causing",
    "3068A>T",
    "c.2936A>T"
  ],
  "c.2936A>T": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "D979V",
    "p.Asp979Val",
    "CF-causing",
    "3068A>T",
    "c.2936A>T"
  ],
  "R1128X": [
    "R1128X",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "3514A>T",
    "p.Arg1128X",
    "c.3382A>T"
  ],
  "3514A>T": [
    "R1128X",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "3514A>T",
    "p.Arg1128X",
    "c.3382A>T"
  ],
  "p.Arg1128X": [
    "R1128X",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "3514A>T",
    "p.Arg1128X",
    "c.3382A>T"
  ],
  "c.3382A>T": [
    "R1128X",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "3514A>T",
    "p.Arg1128X",
    "c.3382A>T"
  ],
  "c.3430C>T": [
    "c.3430C>T",
    "3",
    "1.4210870368440498e-05",
    "No",
    "Q1144X",
    "p.Gln1144X",
    "CF-causing",
    "3562C>T"
  ],
  "Q1144X": [
    "c.3430C>T",
    "3",
    "1.4210870368440498e-05",
    "No",
    "Q1144X",
    "p.Gln1144X",
    "CF-causing",
    "3562C>T"
  ],
  "p.Gln1144X": [
    "c.3430C>T",
    "3",
    "1.4210870368440498e-05",
    "No",
    "Q1144X",
    "p.Gln1144X",
    "CF-causing",
    "3562C>T"
  ],
  "3562C>T": [
    "c.3430C>T",
    "3",
    "1.4210870368440498e-05",
    "No",
    "Q1144X",
    "p.Gln1144X",
    "CF-causing",
    "3562C>T"
  ],
  "c.3796G>T": [
    "c.3796G>T",
    "3",
    "1.4210870368440498e-05",
    "3928G>T",
    "No",
    "CF-causing",
    "p.Glu1266X",
    "E1266X"
  ],
  "3928G>T": [
    "c.3796G>T",
    "3",
    "1.4210870368440498e-05",
    "3928G>T",
    "No",
    "CF-causing",
    "p.Glu1266X",
    "E1266X"
  ],
  "p.Glu1266X": [
    "c.3796G>T",
    "3",
    "1.4210870368440498e-05",
    "3928G>T",
    "No",
    "CF-causing",
    "p.Glu1266X",
    "E1266X"
  ],
  "E1266X": [
    "c.3796G>T",
    "3",
    "1.4210870368440498e-05",
    "3928G>T",
    "No",
    "CF-causing",
    "p.Glu1266X",
    "E1266X"
  ],
  "c.3838C>T": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "c.3838C>T",
    "3970C>T",
    "CF-causing",
    "p.Gln1280X",
    "Q1280X"
  ],
  "3970C>T": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "c.3838C>T",
    "3970C>T",
    "CF-causing",
    "p.Gln1280X",
    "Q1280X"
  ],
  "p.Gln1280X": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "c.3838C>T",
    "3970C>T",
    "CF-causing",
    "p.Gln1280X",
    "Q1280X"
  ],
  "Q1280X": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "c.3838C>T",
    "3970C>T",
    "CF-causing",
    "p.Gln1280X",
    "Q1280X"
  ],
  "4300C>T": [
    "4300C>T",
    "3",
    "1.4210870368440498e-05",
    "No",
    "Q1390X",
    "p.Gln1390X",
    "CF-causing",
    "c.4168C>T"
  ],
  "Q1390X": [
    "4300C>T",
    "3",
    "1.4210870368440498e-05",
    "No",
    "Q1390X",
    "p.Gln1390X",
    "CF-causing",
    "c.4168C>T"
  ],
  "p.Gln1390X": [
    "4300C>T",
    "3",
    "1.4210870368440498e-05",
    "No",
    "Q1390X",
    "p.Gln1390X",
    "CF-causing",
    "c.4168C>T"
  ],
  "c.4168C>T": [
    "4300C>T",
    "3",
    "1.4210870368440498e-05",
    "No",
    "Q1390X",
    "p.Gln1390X",
    "CF-causing",
    "c.4168C>T"
  ],
  "p.Gln179X": [
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "p.Gln179X",
    "CF-causing",
    "667C>T",
    "c.535C>T",
    "Q179X"
  ],
  "667C>T": [
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "p.Gln179X",
    "CF-causing",
    "667C>T",
    "c.535C>T",
    "Q179X"
  ],
  "c.535C>T": [
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "p.Gln179X",
    "CF-causing",
    "667C>T",
    "c.535C>T",
    "Q179X"
  ],
  "Q179X": [
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "p.Gln179X",
    "CF-causing",
    "667C>T",
    "c.535C>T",
    "Q179X"
  ],
  "p.Leu1346MetfsX6": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "p.Leu1346MetfsX6",
    "c.4036_4042del",
    "CF-causing",
    "4168delCTAAGCC"
  ],
  "c.4036_4042del": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "p.Leu1346MetfsX6",
    "c.4036_4042del",
    "CF-causing",
    "4168delCTAAGCC"
  ],
  "4168delCTAAGCC": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "p.Leu1346MetfsX6",
    "c.4036_4042del",
    "CF-causing",
    "4168delCTAAGCC"
  ],
  "deletion of exon 3 (legacy and current numbering)": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "deletion of exon 3 (legacy and current numbering)",
    "Yes, new variant added",
    "CF-causing",
    "CFTRdele3",
    "c.(164+1_165-1)_(273+1_274-1)del"
  ],
  "CFTRdele3": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "deletion of exon 3 (legacy and current numbering)",
    "Yes, new variant added",
    "CF-causing",
    "CFTRdele3",
    "c.(164+1_165-1)_(273+1_274-1)del"
  ],
  "c.(164+1_165-1)_(273+1_274-1)del": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "deletion of exon 3 (legacy and current numbering)",
    "Yes, new variant added",
    "CF-causing",
    "CFTRdele3",
    "c.(164+1_165-1)_(273+1_274-1)del"
  ],
  "CFTRdele4": [
    "p.?",
    "3",
    "CFTRdele4",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "c.(273+1_274-1)_(489+1_490-1)del",
    "CF-causing",
    "deletion of exon 4 (legacy and current numbering)"
  ],
  "c.(273+1_274-1)_(489+1_490-1)del": [
    "p.?",
    "3",
    "CFTRdele4",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "c.(273+1_274-1)_(489+1_490-1)del",
    "CF-causing",
    "deletion of exon 4 (legacy and current numbering)"
  ],
  "deletion of exon 4 (legacy and current numbering)": [
    "p.?",
    "3",
    "CFTRdele4",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "c.(273+1_274-1)_(489+1_490-1)del",
    "CF-causing",
    "deletion of exon 4 (legacy and current numbering)"
  ],
  "deletion of exon 8 (legacy numbering)|deletion of exon 9 (current numbering)": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CF-causing",
    "deletion of exon 8 (legacy numbering)|deletion of exon 9 (current numbering)",
    "CFTRdele8",
    "c.(1116+1_1117-1)_(1209+1_1210-1)del"
  ],
  "CFTRdele8": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CF-causing",
    "deletion of exon 8 (legacy numbering)|deletion of exon 9 (current numbering)",
    "CFTRdele8",
    "c.(1116+1_1117-1)_(1209+1_1210-1)del"
  ],
  "c.(1116+1_1117-1)_(1209+1_1210-1)del": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CF-causing",
    "deletion of exon 8 (legacy numbering)|deletion of exon 9 (current numbering)",
    "CFTRdele8",
    "c.(1116+1_1117-1)_(1209+1_1210-1)del"
  ],
  "CFTRdele1-10": [
    "CFTRdele1-10",
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CF-causing",
    "deletion of exons 1 through 10 (legacy numbering)|deletion of exons 1 through 11 (current numbering)",
    "c.(?_-1)_(1584+1_1585-1)del"
  ],
  "deletion of exons 1 through 10 (legacy numbering)|deletion of exons 1 through 11 (current numbering)": [
    "CFTRdele1-10",
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CF-causing",
    "deletion of exons 1 through 10 (legacy numbering)|deletion of exons 1 through 11 (current numbering)",
    "c.(?_-1)_(1584+1_1585-1)del"
  ],
  "c.(?_-1)_(1584+1_1585-1)del": [
    "CFTRdele1-10",
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CF-causing",
    "deletion of exons 1 through 10 (legacy numbering)|deletion of exons 1 through 11 (current numbering)",
    "c.(?_-1)_(1584+1_1585-1)del"
  ],
  "deletion of exons 1 through 9 (legacy numbering)|deletion of exons 1 through 10 (current numbering)": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "deletion of exons 1 through 9 (legacy numbering)|deletion of exons 1 through 10 (current numbering)",
    "CF-causing",
    "c.(?_1)_(1392+1_1393-1)del",
    "CFTRdele1-9"
  ],
  "c.(?_1)_(1392+1_1393-1)del": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "deletion of part of the promoter through exon 9 (legacy numbering)|deletion of part of the promoter through exon 10 (current numbering)",
    "CF-causing",
    "c.(?_1)_(1392+1_1393-1)del",
    "1",
    "CFTRdelePr-9"
  ],
  "CFTRdele1-9": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "deletion of exons 1 through 9 (legacy numbering)|deletion of exons 1 through 10 (current numbering)",
    "CF-causing",
    "c.(?_1)_(1392+1_1393-1)del",
    "CFTRdele1-9"
  ],
  "CFTRdele16-20": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CF-causing",
    "CFTRdele16-20",
    "c.(2908+1_2909-1)_(3873+1_3874-1)del",
    "deletion of exons 16 through 20 (legacy numbering)|deletion of exons 16 through 23 (current numbering)"
  ],
  "c.(2908+1_2909-1)_(3873+1_3874-1)del": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CF-causing",
    "CFTRdele16-20",
    "c.(2908+1_2909-1)_(3873+1_3874-1)del",
    "deletion of exons 16 through 20 (legacy numbering)|deletion of exons 16 through 23 (current numbering)"
  ],
  "deletion of exons 16 through 20 (legacy numbering)|deletion of exons 16 through 23 (current numbering)": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CF-causing",
    "CFTRdele16-20",
    "c.(2908+1_2909-1)_(3873+1_3874-1)del",
    "deletion of exons 16 through 20 (legacy numbering)|deletion of exons 16 through 23 (current numbering)"
  ],
  "CFTRdele2-10": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CFTRdele2-10",
    "deletion of exons 2 through 10 (legacy numbering)|deletion of exons 2 through 11 (current numbering)",
    "c.(53+1_54-1)_(1584+1_1585-1)del",
    "CF-causing"
  ],
  "deletion of exons 2 through 10 (legacy numbering)|deletion of exons 2 through 11 (current numbering)": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CFTRdele2-10",
    "deletion of exons 2 through 10 (legacy numbering)|deletion of exons 2 through 11 (current numbering)",
    "c.(53+1_54-1)_(1584+1_1585-1)del",
    "CF-causing"
  ],
  "c.(53+1_54-1)_(1584+1_1585-1)del": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CFTRdele2-10",
    "deletion of exons 2 through 10 (legacy numbering)|deletion of exons 2 through 11 (current numbering)",
    "c.(53+1_54-1)_(1584+1_1585-1)del",
    "CF-causing"
  ],
  "CFTRdele4-6ains6": [
    "p.?",
    "3",
    "CFTRdele4-6ains6",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CF-causing",
    "deletion of exons 4 through 6a and insertion of 6 nucleotides (legacy numbering)|deletion of exons 4 through 7 and insertion of 6 nucleotides (current numbering)",
    "c.273+7983_743+362delinsACCTCG"
  ],
  "deletion of exons 4 through 6a and insertion of 6 nucleotides (legacy numbering)|deletion of exons 4 through 7 and insertion of 6 nucleotides (current numbering)": [
    "p.?",
    "3",
    "CFTRdele4-6ains6",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CF-causing",
    "deletion of exons 4 through 6a and insertion of 6 nucleotides (legacy numbering)|deletion of exons 4 through 7 and insertion of 6 nucleotides (current numbering)",
    "c.273+7983_743+362delinsACCTCG"
  ],
  "c.273+7983_743+362delinsACCTCG": [
    "p.?",
    "3",
    "CFTRdele4-6ains6",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CF-causing",
    "deletion of exons 4 through 6a and insertion of 6 nucleotides (legacy numbering)|deletion of exons 4 through 7 and insertion of 6 nucleotides (current numbering)",
    "c.273+7983_743+362delinsACCTCG"
  ],
  "deletion of exons 4 through 8 and 12 through 21 (legacy numbering)|deletion of exons 4 through 9 and 13 through 24 (current numbering)": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "deletion of exons 4 through 8 and 12 through 21 (legacy numbering)|deletion of exons 4 through 9 and 13 through 24 (current numbering)",
    "CF-causing",
    "CFTRdele4-8,12-21",
    "c.[(273+1_274-1)_(1209+1_1210-1)del;(1679+1_1680-1)_(3963+1_3964-1)del]"
  ],
  "CFTRdele4-8,12-21": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "deletion of exons 4 through 8 and 12 through 21 (legacy numbering)|deletion of exons 4 through 9 and 13 through 24 (current numbering)",
    "CF-causing",
    "CFTRdele4-8,12-21",
    "c.[(273+1_274-1)_(1209+1_1210-1)del;(1679+1_1680-1)_(3963+1_3964-1)del]"
  ],
  "c.[(273+1_274-1)_(1209+1_1210-1)del;(1679+1_1680-1)_(3963+1_3964-1)del]": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "deletion of exons 4 through 8 and 12 through 21 (legacy numbering)|deletion of exons 4 through 9 and 13 through 24 (current numbering)",
    "CF-causing",
    "CFTRdele4-8,12-21",
    "c.[(273+1_274-1)_(1209+1_1210-1)del;(1679+1_1680-1)_(3963+1_3964-1)del]"
  ],
  "CFTRdele8,9": [
    "CFTRdele8,9",
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CF-causing",
    "deletion of exons 8 and 9 (legacy numbering)|deletion of exons 9 and 10 (current numbering)",
    "c.(1116+1_1117-1)_(1392+1_1393-1)del"
  ],
  "deletion of exons 8 and 9 (legacy numbering)|deletion of exons 9 and 10 (current numbering)": [
    "CFTRdele8,9",
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CF-causing",
    "deletion of exons 8 and 9 (legacy numbering)|deletion of exons 9 and 10 (current numbering)",
    "c.(1116+1_1117-1)_(1392+1_1393-1)del"
  ],
  "c.(1116+1_1117-1)_(1392+1_1393-1)del": [
    "CFTRdele8,9",
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CF-causing",
    "deletion of exons 8 and 9 (legacy numbering)|deletion of exons 9 and 10 (current numbering)",
    "c.(1116+1_1117-1)_(1392+1_1393-1)del"
  ],
  "CFTRdelePr-3": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CFTRdelePr-3",
    "CF-causing",
    "deletion of part of the promoter through exon 3 (legacy and current numbering)",
    "c.(?_1)_(273+1_274-1)del"
  ],
  "deletion of part of the promoter through exon 3 (legacy and current numbering)": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CFTRdelePr-3",
    "CF-causing",
    "deletion of part of the promoter through exon 3 (legacy and current numbering)",
    "c.(?_1)_(273+1_274-1)del"
  ],
  "c.(?_1)_(273+1_274-1)del": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CFTRdelePr-3",
    "CF-causing",
    "deletion of part of the promoter through exon 3 (legacy and current numbering)",
    "c.(?_1)_(273+1_274-1)del"
  ],
  "CFTRdup2": [
    "CFTRdup2",
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CF-causing",
    "duplication of exon 2 (legacy and current numbering)",
    "c.54-4235_164+377dup"
  ],
  "duplication of exon 2 (legacy and current numbering)": [
    "CFTRdup2",
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CF-causing",
    "duplication of exon 2 (legacy and current numbering)",
    "c.54-4235_164+377dup"
  ],
  "c.54-4235_164+377dup": [
    "CFTRdup2",
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CF-causing",
    "duplication of exon 2 (legacy and current numbering)",
    "c.54-4235_164+377dup"
  ],
  "c.(273+1_274-1)_(1584+1_1585-1)dup": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "c.(273+1_274-1)_(1584+1_1585-1)dup",
    "CF-causing",
    "CFTRdup4-10",
    "duplication of exons 4 through 9 (legacy numbering)|duplication of exons 4 through 10 (current numbering)"
  ],
  "CFTRdup4-10": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "c.(273+1_274-1)_(1584+1_1585-1)dup",
    "CF-causing",
    "CFTRdup4-10",
    "duplication of exons 4 through 9 (legacy numbering)|duplication of exons 4 through 10 (current numbering)"
  ],
  "duplication of exons 4 through 9 (legacy numbering)|duplication of exons 4 through 10 (current numbering)": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "c.(273+1_274-1)_(1584+1_1585-1)dup",
    "CF-causing",
    "CFTRdup4-10",
    "duplication of exons 4 through 9 (legacy numbering)|duplication of exons 4 through 10 (current numbering)"
  ],
  "duplication of exons 6b and 7 (legacy numbering)|duplication of exons 7 and 8 (current numbering)": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "duplication of exons 6b and 7 (legacy numbering)|duplication of exons 7 and 8 (current numbering)",
    "CF-causing",
    "CFTRdup6b,7",
    "c.(743+1_744-1)_(1116+1_1117-1)dup"
  ],
  "CFTRdup6b,7": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "duplication of exons 6b and 7 (legacy numbering)|duplication of exons 7 and 8 (current numbering)",
    "CF-causing",
    "CFTRdup6b,7",
    "c.(743+1_744-1)_(1116+1_1117-1)dup"
  ],
  "c.(743+1_744-1)_(1116+1_1117-1)dup": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "duplication of exons 6b and 7 (legacy numbering)|duplication of exons 7 and 8 (current numbering)",
    "CF-causing",
    "CFTRdup6b,7",
    "c.(743+1_744-1)_(1116+1_1117-1)dup"
  ],
  "3600+1G->T": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "No",
    "3600+1G->T",
    "CF-causing",
    "c.3468+1G>T"
  ],
  "c.3468+1G>T": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "No",
    "3600+1G->T",
    "CF-causing",
    "c.3468+1G>T"
  ],
  "296+2T->G": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "No",
    "296+2T->G",
    "CF-causing",
    "c.164+2T>G"
  ],
  "c.164+2T>G": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "No",
    "296+2T->G",
    "CF-causing",
    "c.164+2T>G"
  ],
  "621+1G->A": [
    "621+1G->A",
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "c.489+1G>A"
  ],
  "c.489+1G>A": [
    "621+1G->A",
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "c.489+1G>A"
  ],
  "c.1585-1G>T": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "c.1585-1G>T",
    "1717-1G->T"
  ],
  "1717-1G->T": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "c.1585-1G>T",
    "1717-1G->T"
  ],
  "2751+2T->C": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "2751+2T->C",
    "c.2619+2T>C"
  ],
  "c.2619+2T>C": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "2751+2T->C",
    "c.2619+2T>C"
  ],
  "1001+1G->C": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "No",
    "1001+1G->C",
    "c.869+1G>C",
    "CF-causing"
  ],
  "c.869+1G>C": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "No",
    "1001+1G->C",
    "c.869+1G>C",
    "CF-causing"
  ],
  "c.164+2T>C": [
    "p.?",
    "3",
    "c.164+2T>C",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "296+2T->C"
  ],
  "296+2T->C": [
    "p.?",
    "3",
    "c.164+2T>C",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "296+2T->C"
  ],
  "c.54-1G>A": [
    "c.54-1G>A",
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "186-1G->A"
  ],
  "186-1G->A": [
    "c.54-1G>A",
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "186-1G->A"
  ],
  "875+2T->C": [
    "875+2T->C",
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "c.743+2T>C"
  ],
  "c.743+2T>C": [
    "875+2T->C",
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "c.743+2T>C"
  ],
  "p.Thr1122LysfsX12": [
    "3",
    "p.Thr1122LysfsX12",
    "1.4210870368440498e-05",
    "No",
    "c.3365del",
    "CF-causing",
    "3497delC"
  ],
  "c.3365del": [
    "3",
    "p.Thr1122LysfsX12",
    "1.4210870368440498e-05",
    "No",
    "c.3365del",
    "CF-causing",
    "3497delC"
  ],
  "3497delC": [
    "3",
    "p.Thr1122LysfsX12",
    "1.4210870368440498e-05",
    "No",
    "c.3365del",
    "CF-causing",
    "3497delC"
  ],
  "1540del10": [
    "1540del10",
    "3",
    "1.4210870368440498e-05",
    "No",
    "p.Val470GlufsX54",
    "c.1409_1418del",
    "CF-causing"
  ],
  "p.Val470GlufsX54": [
    "1540del10",
    "3",
    "1.4210870368440498e-05",
    "No",
    "p.Val470GlufsX54",
    "c.1409_1418del",
    "CF-causing"
  ],
  "c.1409_1418del": [
    "1540del10",
    "3",
    "1.4210870368440498e-05",
    "No",
    "p.Val470GlufsX54",
    "c.1409_1418del",
    "CF-causing"
  ],
  "c.1920_1921dup": [
    "c.1920_1921dup",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "p.Ser641IlefsX23",
    "2053insTA"
  ],
  "p.Ser641IlefsX23": [
    "c.1920_1921dup",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "p.Ser641IlefsX23",
    "2053insTA"
  ],
  "2053insTA": [
    "c.1920_1921dup",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "p.Ser641IlefsX23",
    "2053insTA"
  ],
  "1353delA": [
    "1353delA",
    "3",
    "1.4210870368440498e-05",
    "No",
    "c.1221del",
    "p.Glu407AspfsX35",
    "CF-causing"
  ],
  "c.1221del": [
    "1353delA",
    "3",
    "1.4210870368440498e-05",
    "No",
    "c.1221del",
    "p.Glu407AspfsX35",
    "CF-causing"
  ],
  "p.Glu407AspfsX35": [
    "1353delA",
    "3",
    "1.4210870368440498e-05",
    "No",
    "c.1221del",
    "p.Glu407AspfsX35",
    "CF-causing"
  ],
  "c.142_145del": [
    "c.142_145del",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "c.142_145delAATC",
    "p.Asn48TyrfsX42"
  ],
  "c.142_145delAATC": [
    "c.142_145del",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "c.142_145delAATC",
    "p.Asn48TyrfsX42"
  ],
  "p.Asn48TyrfsX42": [
    "c.142_145del",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "c.142_145delAATC",
    "p.Asn48TyrfsX42"
  ],
  "2221insA": [
    "2221insA",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "p.Arg697LysfsX33",
    "c.2089dup"
  ],
  "p.Arg697LysfsX33": [
    "2221insA",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "p.Arg697LysfsX33",
    "c.2089dup"
  ],
  "c.2089dup": [
    "2221insA",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "p.Arg697LysfsX33",
    "c.2089dup"
  ],
  "c.2261del": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "c.2261del",
    "CF-causing",
    "p.Val754GlyfsX17",
    "c.2261delT"
  ],
  "p.Val754GlyfsX17": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "c.2261del",
    "CF-causing",
    "p.Val754GlyfsX17",
    "c.2261delT"
  ],
  "c.2261delT": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "c.2261del",
    "CF-causing",
    "p.Val754GlyfsX17",
    "c.2261delT"
  ],
  "c.3536_3539del": [
    "3",
    "c.3536_3539del",
    "1.4210870368440498e-05",
    "No",
    "3667del4",
    "p.Thr1179AsnfsX12",
    "CF-causing"
  ],
  "3667del4": [
    "3",
    "c.3536_3539del",
    "1.4210870368440498e-05",
    "No",
    "3667del4",
    "p.Thr1179AsnfsX12",
    "CF-causing"
  ],
  "p.Thr1179AsnfsX12": [
    "3",
    "c.3536_3539del",
    "1.4210870368440498e-05",
    "No",
    "3667del4",
    "p.Thr1179AsnfsX12",
    "CF-causing"
  ],
  "c.601del": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "c.601del",
    "733delG",
    "CF-causing",
    "p.Val201CysfsX14"
  ],
  "733delG": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "c.601del",
    "733delG",
    "CF-causing",
    "p.Val201CysfsX14"
  ],
  "p.Val201CysfsX14": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "c.601del",
    "733delG",
    "CF-causing",
    "p.Val201CysfsX14"
  ],
  "849delG": [
    "3",
    "849delG",
    "1.4210870368440498e-05",
    "No",
    "c.717del",
    "p.Leu240X",
    "CF-causing"
  ],
  "c.717del": [
    "3",
    "849delG",
    "1.4210870368440498e-05",
    "No",
    "c.717del",
    "p.Leu240X",
    "CF-causing"
  ],
  "p.Leu240X": [
    "Yes, new variant added",
    "9.473913578960333e-06",
    "p.Leu240X",
    "CF-causing",
    "2",
    "L240X",
    "c.714del"
  ],
  "1460delAT": [
    "1460delAT",
    "3",
    "1.4210870368440498e-05",
    "No",
    "c.1330_1331del",
    "CF-causing",
    "p.Ile444X"
  ],
  "c.1330_1331del": [
    "1460delAT",
    "3",
    "1.4210870368440498e-05",
    "No",
    "c.1330_1331del",
    "CF-causing",
    "p.Ile444X"
  ],
  "p.Ile444X": [
    "1460delAT",
    "3",
    "1.4210870368440498e-05",
    "No",
    "c.1330_1331del",
    "CF-causing",
    "p.Ile444X"
  ],
  "c.156_163dup": [
    "c.156_163dup",
    "3",
    "p.Arg55AsnfsX39",
    "1.4210870368440498e-05",
    "No",
    "295ins8",
    "CF-causing"
  ],
  "p.Arg55AsnfsX39": [
    "c.156_163dup",
    "3",
    "p.Arg55AsnfsX39",
    "1.4210870368440498e-05",
    "No",
    "295ins8",
    "CF-causing"
  ],
  "295ins8": [
    "c.156_163dup",
    "3",
    "p.Arg55AsnfsX39",
    "1.4210870368440498e-05",
    "No",
    "295ins8",
    "CF-causing"
  ],
  "2335delA": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "2335delA",
    "CF-causing",
    "p.Arg735GlyfsX4",
    "c.2203del"
  ],
  "p.Arg735GlyfsX4": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "2335delA",
    "CF-causing",
    "p.Arg735GlyfsX4",
    "c.2203del"
  ],
  "c.2203del": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "2335delA",
    "CF-causing",
    "p.Arg735GlyfsX4",
    "c.2203del"
  ],
  "c.2425del": [
    "c.2425del",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "2557delT",
    "p.Ser809GlnfsX12"
  ],
  "2557delT": [
    "c.2425del",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "2557delT",
    "p.Ser809GlnfsX12"
  ],
  "p.Ser809GlnfsX12": [
    "c.2425del",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "2557delT",
    "p.Ser809GlnfsX12"
  ],
  "2937_2942delinsTCAGA": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "2937_2942delinsTCAGA",
    "c.2805_2810del",
    "p.Pro936_Leu937del"
  ],
  "c.2805_2810del": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "2937_2942delinsTCAGA",
    "c.2805_2810del",
    "p.Pro936_Leu937del"
  ],
  "p.Pro936_Leu937del": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "2937_2942delinsTCAGA",
    "c.2805_2810del",
    "p.Pro936_Leu937del"
  ],
  "p.Thr940AsnfsX33": [
    "p.Thr940AsnfsX33",
    "3",
    "c.2819_2823del",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "2949del5"
  ],
  "c.2819_2823del": [
    "p.Thr940AsnfsX33",
    "3",
    "c.2819_2823del",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "2949del5"
  ],
  "2949del5": [
    "p.Thr940AsnfsX33",
    "3",
    "c.2819_2823del",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "2949del5"
  ],
  "c.3011del": [
    "c.3011del",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "3143delC",
    "p.Ala1004ValfsX2"
  ],
  "3143delC": [
    "c.3011del",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "3143delC",
    "p.Ala1004ValfsX2"
  ],
  "p.Ala1004ValfsX2": [
    "c.3011del",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "3143delC",
    "p.Ala1004ValfsX2"
  ],
  "c.303dup": [
    "c.303dup",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "p.Leu102ThrfsX9",
    "435insA"
  ],
  "p.Leu102ThrfsX9": [
    "c.303dup",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "p.Leu102ThrfsX9",
    "435insA"
  ],
  "435insA": [
    "c.303dup",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "p.Leu102ThrfsX9",
    "435insA"
  ],
  "556delA": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "556delA",
    "c.424del",
    "p.Ile142PhefsX11"
  ],
  "c.424del": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "556delA",
    "c.424del",
    "p.Ile142PhefsX11"
  ],
  "p.Ile142PhefsX11": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "556delA",
    "c.424del",
    "p.Ile142PhefsX11"
  ],
  "c.49_50delTT": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "c.49_50delTT",
    "CF-causing",
    "c.49_50del",
    "p.Phe17GlnfsX27"
  ],
  "c.49_50del": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "c.49_50delTT",
    "CF-causing",
    "c.49_50del",
    "p.Phe17GlnfsX27"
  ],
  "p.Phe17GlnfsX27": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "c.49_50delTT",
    "CF-causing",
    "c.49_50del",
    "p.Phe17GlnfsX27"
  ],
  "1601delTC": [
    "1601delTC",
    "p.Phe490LeufsX13",
    "3",
    "1.4210870368440498e-05",
    "No",
    "c.1470_1471del",
    "CF-causing"
  ],
  "p.Phe490LeufsX13": [
    "1601delTC",
    "p.Phe490LeufsX13",
    "3",
    "1.4210870368440498e-05",
    "No",
    "c.1470_1471del",
    "CF-causing"
  ],
  "c.1470_1471del": [
    "1601delTC",
    "p.Phe490LeufsX13",
    "3",
    "1.4210870368440498e-05",
    "No",
    "c.1470_1471del",
    "CF-causing"
  ],
  "p.Pro111ArgfsX13": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "p.Pro111ArgfsX13",
    "c.332del",
    "464delC"
  ],
  "c.332del": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "p.Pro111ArgfsX13",
    "c.332del",
    "464delC"
  ],
  "464delC": [
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "p.Pro111ArgfsX13",
    "c.332del",
    "464delC"
  ],
  "c.3468+5G>A": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "c.3468+5G>A",
    "3600+5G->A"
  ],
  "3600+5G->A": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "No",
    "CF-causing",
    "c.3468+5G>A",
    "3600+5G->A"
  ],
  "c.490-1G>C": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "c.490-1G>C",
    "CF-causing",
    "622-1G->C"
  ],
  "622-1G->C": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "c.490-1G>C",
    "CF-causing",
    "622-1G->C"
  ],
  "3271+1G->A": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "3271+1G->A",
    "Yes, new variant added",
    "CF-causing",
    "c.3139+1G>A"
  ],
  "c.3139+1G>A": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "3271+1G->A",
    "Yes, new variant added",
    "CF-causing",
    "c.3139+1G>A"
  ],
  "c.3367+1G>A": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "c.3367+1G>A",
    "CF-causing",
    "3499+1G->A"
  ],
  "3499+1G->A": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "c.3367+1G>A",
    "CF-causing",
    "3499+1G->A"
  ],
  "c.1116+1G>C": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "c.1116+1G>C",
    "CF-causing",
    "1248+1G->C"
  ],
  "1248+1G->C": [
    "p.?",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "c.1116+1G>C",
    "CF-causing",
    "1248+1G->C"
  ],
  "1342-1delG": [
    "p.?",
    "3",
    "1342-1delG",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "c.1210-1del",
    "CF-causing"
  ],
  "c.1210-1del": [
    "p.?",
    "3",
    "1342-1delG",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "c.1210-1del",
    "CF-causing"
  ],
  "1309delG": [
    "1309delG",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "p.Val393X",
    "CF-causing",
    "c.1177del"
  ],
  "p.Val393X": [
    "1309delG",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "p.Val393X",
    "CF-causing",
    "c.1177del"
  ],
  "c.1177del": [
    "1309delG",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "p.Val393X",
    "CF-causing",
    "c.1177del"
  ],
  "1465_1466insTAAT": [
    "1465_1466insTAAT",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CF-causing",
    "c.1333_1334insTAAT",
    "p.Asn445IlefsX38"
  ],
  "c.1333_1334insTAAT": [
    "1465_1466insTAAT",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CF-causing",
    "c.1333_1334insTAAT",
    "p.Asn445IlefsX38"
  ],
  "p.Asn445IlefsX38": [
    "1465_1466insTAAT",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CF-causing",
    "c.1333_1334insTAAT",
    "p.Asn445IlefsX38"
  ],
  "c.1157_1158insTA": [
    "c.1157_1158insTA",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "1289insTA",
    "CF-causing",
    "p.Leu387ThrfsX2"
  ],
  "1289insTA": [
    "c.1157_1158insTA",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "1289insTA",
    "CF-causing",
    "p.Leu387ThrfsX2"
  ],
  "p.Leu387ThrfsX2": [
    "c.1157_1158insTA",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "1289insTA",
    "CF-causing",
    "p.Leu387ThrfsX2"
  ],
  "c.2089del": [
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "c.2089del",
    "CF-causing",
    "c.2089delA",
    "p.Arg697GlyfsX25"
  ],
  "c.2089delA": [
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "c.2089del",
    "CF-causing",
    "c.2089delA",
    "p.Arg697GlyfsX25"
  ],
  "p.Arg697GlyfsX25": [
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "c.2089del",
    "CF-causing",
    "c.2089delA",
    "p.Arg697GlyfsX25"
  ],
  "c.3486_3487del": [
    "c.3486_3487del",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "p.Val1163LeufsX2",
    "CF-causing",
    "3617delGA"
  ],
  "p.Val1163LeufsX2": [
    "c.3486_3487del",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "p.Val1163LeufsX2",
    "CF-causing",
    "3617delGA"
  ],
  "3617delGA": [
    "c.3486_3487del",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "p.Val1163LeufsX2",
    "CF-causing",
    "3617delGA"
  ],
  "p.Lys14AsnfsX11": [
    "3",
    "1.4210870368440498e-05",
    "p.Lys14AsnfsX11",
    "Yes, new variant added",
    "c.42del",
    "CF-causing",
    "174delA"
  ],
  "c.42del": [
    "3",
    "1.4210870368440498e-05",
    "p.Lys14AsnfsX11",
    "Yes, new variant added",
    "c.42del",
    "CF-causing",
    "174delA"
  ],
  "174delA": [
    "3",
    "1.4210870368440498e-05",
    "p.Lys14AsnfsX11",
    "Yes, new variant added",
    "c.42del",
    "CF-causing",
    "174delA"
  ],
  "c.3477del": [
    "c.3477del",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CF-causing",
    "p.Val1160X",
    "c.3477delT"
  ],
  "p.Val1160X": [
    "c.3477del",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CF-causing",
    "p.Val1160X",
    "c.3477delT"
  ],
  "c.3477delT": [
    "c.3477del",
    "3",
    "1.4210870368440498e-05",
    "Yes, new variant added",
    "CF-causing",
    "p.Val1160X",
    "c.3477delT"
  ],
  "c.912C>G": [
    "c.912C>G",
    "Yes, new variant added",
    "p.Tyr304X",
    "9.473913578960333e-06",
    "CF-causing",
    "Y304X",
    "2",
    "1044C>G"
  ],
  "p.Tyr304X": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.912delinsGG",
    "p.Tyr304X",
    "CF-causing",
    "1",
    "c.912delCinsGG"
  ],
  "9.473913578960333e-06": [
    "p.?",
    "Yes, new variant added",
    "c.3G>A",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "M1I"
  ],
  "Y304X": [
    "c.912C>G",
    "Yes, new variant added",
    "p.Tyr304X",
    "9.473913578960333e-06",
    "CF-causing",
    "Y304X",
    "2",
    "1044C>G"
  ],
  "2": [
    "p.?",
    "Yes, new variant added",
    "c.3G>A",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "M1I"
  ],
  "1044C>G": [
    "c.912C>G",
    "Yes, new variant added",
    "p.Tyr304X",
    "9.473913578960333e-06",
    "CF-causing",
    "Y304X",
    "2",
    "1044C>G"
  ],
  "c.1114C>T": [
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "c.1114C>T",
    "Q372X",
    "2",
    "1246C>T",
    "p.Gln372X"
  ],
  "Q372X": [
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "c.1114C>T",
    "Q372X",
    "2",
    "1246C>T",
    "p.Gln372X"
  ],
  "1246C>T": [
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "c.1114C>T",
    "Q372X",
    "2",
    "1246C>T",
    "p.Gln372X"
  ],
  "p.Gln372X": [
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "c.1114C>T",
    "Q372X",
    "2",
    "1246C>T",
    "p.Gln372X"
  ],
  "p.Gln378X": [
    "No",
    "p.Gln378X",
    "Q378X",
    "1264C>T",
    "9.473913578960333e-06",
    "CF-causing",
    "c.1132C>T",
    "2"
  ],
  "Q378X": [
    "No",
    "p.Gln378X",
    "Q378X",
    "1264C>T",
    "9.473913578960333e-06",
    "CF-causing",
    "c.1132C>T",
    "2"
  ],
  "1264C>T": [
    "No",
    "p.Gln378X",
    "Q378X",
    "1264C>T",
    "9.473913578960333e-06",
    "CF-causing",
    "c.1132C>T",
    "2"
  ],
  "c.1132C>T": [
    "No",
    "p.Gln378X",
    "Q378X",
    "1264C>T",
    "9.473913578960333e-06",
    "CF-causing",
    "c.1132C>T",
    "2"
  ],
  "1336G>T": [
    "1336G>T",
    "E402X",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Glu402X",
    "2",
    "c.1204G>T"
  ],
  "E402X": [
    "1336G>T",
    "E402X",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Glu402X",
    "2",
    "c.1204G>T"
  ],
  "p.Glu402X": [
    "1336G>T",
    "E402X",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Glu402X",
    "2",
    "c.1204G>T"
  ],
  "c.1204G>T": [
    "1336G>T",
    "E402X",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Glu402X",
    "2",
    "c.1204G>T"
  ],
  "1456A>T": [
    "No",
    "1456A>T",
    "c.1324A>T",
    "p.Lys442X",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "K442X"
  ],
  "c.1324A>T": [
    "No",
    "1456A>T",
    "c.1324A>T",
    "p.Lys442X",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "K442X"
  ],
  "p.Lys442X": [
    "No",
    "1456A>T",
    "c.1324A>T",
    "p.Lys442X",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "K442X"
  ],
  "K442X": [
    "No",
    "1456A>T",
    "c.1324A>T",
    "p.Lys442X",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "K442X"
  ],
  "E528X": [
    "No",
    "E528X",
    "c.1582G>T",
    "p.Glu528X",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "1714G>T"
  ],
  "c.1582G>T": [
    "No",
    "E528X",
    "c.1582G>T",
    "p.Glu528X",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "1714G>T"
  ],
  "p.Glu528X": [
    "No",
    "E528X",
    "c.1582G>T",
    "p.Glu528X",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "1714G>T"
  ],
  "1714G>T": [
    "No",
    "E528X",
    "c.1582G>T",
    "p.Glu528X",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "1714G>T"
  ],
  "p.Leu568X": [
    "p.Leu568X",
    "L568X",
    "c.1703T>A",
    "No",
    "1835T>A",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "L568X": [
    "p.Leu568X",
    "L568X",
    "c.1703T>A",
    "No",
    "1835T>A",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "c.1703T>A": [
    "p.Leu568X",
    "L568X",
    "c.1703T>A",
    "No",
    "1835T>A",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "1835T>A": [
    "p.Leu568X",
    "L568X",
    "c.1703T>A",
    "No",
    "1835T>A",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "p.Tyr569X": [
    "p.Tyr569X",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "Y569X",
    "2",
    "c.1707T>A",
    "1839T>A"
  ],
  "Y569X": [
    "p.Tyr569X",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "Y569X",
    "2",
    "c.1707T>A",
    "1839T>A"
  ],
  "c.1707T>A": [
    "p.Tyr569X",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "Y569X",
    "2",
    "c.1707T>A",
    "1839T>A"
  ],
  "1839T>A": [
    "p.Tyr569X",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "Y569X",
    "2",
    "c.1707T>A",
    "1839T>A"
  ],
  "E588X": [
    "E588X",
    "p.Glu588X",
    "Yes, new variant added",
    "1894G>T",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.1762G>T"
  ],
  "p.Glu588X": [
    "E588X",
    "p.Glu588X",
    "Yes, new variant added",
    "1894G>T",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.1762G>T"
  ],
  "1894G>T": [
    "E588X",
    "p.Glu588X",
    "Yes, new variant added",
    "1894G>T",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.1762G>T"
  ],
  "c.1762G>T": [
    "E588X",
    "p.Glu588X",
    "Yes, new variant added",
    "1894G>T",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.1762G>T"
  ],
  "c.1979C>A|c.1979C>G": [
    "Yes, new variant added",
    "c.1979C>A|c.1979C>G",
    "9.473913578960333e-06",
    "CF-causing",
    "S660X",
    "2",
    "p.Ser660X",
    "2111C>A|2111C>G"
  ],
  "S660X": [
    "Yes, new variant added",
    "c.1979C>A|c.1979C>G",
    "9.473913578960333e-06",
    "CF-causing",
    "S660X",
    "2",
    "p.Ser660X",
    "2111C>A|2111C>G"
  ],
  "p.Ser660X": [
    "Yes, new variant added",
    "c.1979C>A|c.1979C>G",
    "9.473913578960333e-06",
    "CF-causing",
    "S660X",
    "2",
    "p.Ser660X",
    "2111C>A|2111C>G"
  ],
  "2111C>A|2111C>G": [
    "Yes, new variant added",
    "c.1979C>A|c.1979C>G",
    "9.473913578960333e-06",
    "CF-causing",
    "S660X",
    "2",
    "p.Ser660X",
    "2111C>A|2111C>G"
  ],
  "c.2062A>T": [
    "c.2062A>T",
    "p.Lys688X",
    "No",
    "2194A>T",
    "K688X",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "p.Lys688X": [
    "c.2062A>T",
    "p.Lys688X",
    "No",
    "2194A>T",
    "K688X",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "2194A>T": [
    "c.2062A>T",
    "p.Lys688X",
    "No",
    "2194A>T",
    "K688X",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "K688X": [
    "c.2062A>T",
    "p.Lys688X",
    "No",
    "2194A>T",
    "K688X",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "c.88C>T": [
    "No",
    "c.88C>T",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Gln30X",
    "2",
    "Q30X",
    "220C>T"
  ],
  "p.Gln30X": [
    "No",
    "c.88C>T",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Gln30X",
    "2",
    "Q30X",
    "220C>T"
  ],
  "Q30X": [
    "No",
    "c.88C>T",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Gln30X",
    "2",
    "Q30X",
    "220C>T"
  ],
  "220C>T": [
    "No",
    "c.88C>T",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Gln30X",
    "2",
    "Q30X",
    "220C>T"
  ],
  "2288T>A": [
    "2288T>A",
    "No",
    "p.Leu719X",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.2156T>A",
    "L719X"
  ],
  "p.Leu719X": [
    "2288T>A",
    "No",
    "p.Leu719X",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.2156T>A",
    "L719X"
  ],
  "c.2156T>A": [
    "2288T>A",
    "No",
    "p.Leu719X",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.2156T>A",
    "L719X"
  ],
  "L719X": [
    "2288T>A",
    "No",
    "p.Leu719X",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.2156T>A",
    "L719X"
  ],
  "c.2188G>T": [
    "No",
    "c.2188G>T",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Glu730X",
    "E730X",
    "2",
    "2320G>T"
  ],
  "p.Glu730X": [
    "No",
    "c.2188G>T",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Glu730X",
    "E730X",
    "2",
    "2320G>T"
  ],
  "E730X": [
    "No",
    "c.2188G>T",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Glu730X",
    "E730X",
    "2",
    "2320G>T"
  ],
  "2320G>T": [
    "No",
    "c.2188G>T",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Glu730X",
    "E730X",
    "2",
    "2320G>T"
  ],
  "Q767X": [
    "Q767X",
    "No",
    "c.2299C>T",
    "9.473913578960333e-06",
    "CF-causing",
    "2431C>T",
    "p.Gln767X",
    "2"
  ],
  "c.2299C>T": [
    "Q767X",
    "No",
    "c.2299C>T",
    "9.473913578960333e-06",
    "CF-causing",
    "2431C>T",
    "p.Gln767X",
    "2"
  ],
  "2431C>T": [
    "Q767X",
    "No",
    "c.2299C>T",
    "9.473913578960333e-06",
    "CF-causing",
    "2431C>T",
    "p.Gln767X",
    "2"
  ],
  "p.Gln767X": [
    "Q767X",
    "No",
    "c.2299C>T",
    "9.473913578960333e-06",
    "CF-causing",
    "2431C>T",
    "p.Gln767X",
    "2"
  ],
  "p.Gln779X": [
    "No",
    "p.Gln779X",
    "9.473913578960333e-06",
    "CF-causing",
    "Q779X",
    "2",
    "2467C>T",
    "c.2335C>T"
  ],
  "Q779X": [
    "No",
    "p.Gln779X",
    "9.473913578960333e-06",
    "CF-causing",
    "Q779X",
    "2",
    "2467C>T",
    "c.2335C>T"
  ],
  "2467C>T": [
    "No",
    "p.Gln779X",
    "9.473913578960333e-06",
    "CF-causing",
    "Q779X",
    "2",
    "2467C>T",
    "c.2335C>T"
  ],
  "c.2335C>T": [
    "No",
    "p.Gln779X",
    "9.473913578960333e-06",
    "CF-causing",
    "Q779X",
    "2",
    "2467C>T",
    "c.2335C>T"
  ],
  "R810X": [
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "R810X",
    "2",
    "c.2428A>T",
    "2560A>T",
    "p.Arg810X"
  ],
  "c.2428A>T": [
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "R810X",
    "2",
    "c.2428A>T",
    "2560A>T",
    "p.Arg810X"
  ],
  "2560A>T": [
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "R810X",
    "2",
    "c.2428A>T",
    "2560A>T",
    "p.Arg810X"
  ],
  "p.Arg810X": [
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "R810X",
    "2",
    "c.2428A>T",
    "2560A>T",
    "p.Arg810X"
  ],
  "p.Gln814X": [
    "No",
    "p.Gln814X",
    "2572C>T",
    "9.473913578960333e-06",
    "CF-causing",
    "Q814X",
    "2",
    "c.2440C>T"
  ],
  "2572C>T": [
    "No",
    "p.Gln814X",
    "2572C>T",
    "9.473913578960333e-06",
    "CF-causing",
    "Q814X",
    "2",
    "c.2440C>T"
  ],
  "Q814X": [
    "No",
    "p.Gln814X",
    "2572C>T",
    "9.473913578960333e-06",
    "CF-causing",
    "Q814X",
    "2",
    "c.2440C>T"
  ],
  "c.2440C>T": [
    "No",
    "p.Gln814X",
    "2572C>T",
    "9.473913578960333e-06",
    "CF-causing",
    "Q814X",
    "2",
    "c.2440C>T"
  ],
  "p.Glu815X": [
    "p.Glu815X",
    "c.2443G>T",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "E815X",
    "2575G>T"
  ],
  "c.2443G>T": [
    "p.Glu815X",
    "c.2443G>T",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "E815X",
    "2575G>T"
  ],
  "E815X": [
    "p.Glu815X",
    "c.2443G>T",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "E815X",
    "2575G>T"
  ],
  "2575G>T": [
    "p.Glu815X",
    "c.2443G>T",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "E815X",
    "2575G>T"
  ],
  "p.Glu826X": [
    "p.Glu826X",
    "E826X",
    "2608G>T",
    "c.2476G>T",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "E826X": [
    "p.Glu826X",
    "E826X",
    "2608G>T",
    "c.2476G>T",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "2608G>T": [
    "p.Glu826X",
    "E826X",
    "2608G>T",
    "c.2476G>T",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "c.2476G>T": [
    "p.Glu826X",
    "E826X",
    "2608G>T",
    "c.2476G>T",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "c.2488A>T": [
    "c.2488A>T",
    "p.Lys830X",
    "No",
    "2620A>T",
    "9.473913578960333e-06",
    "CF-causing",
    "K830X",
    "2"
  ],
  "p.Lys830X": [
    "c.2488A>T",
    "p.Lys830X",
    "No",
    "2620A>T",
    "9.473913578960333e-06",
    "CF-causing",
    "K830X",
    "2"
  ],
  "2620A>T": [
    "c.2488A>T",
    "p.Lys830X",
    "No",
    "2620A>T",
    "9.473913578960333e-06",
    "CF-causing",
    "K830X",
    "2"
  ],
  "K830X": [
    "c.2488A>T",
    "p.Lys830X",
    "No",
    "2620A>T",
    "9.473913578960333e-06",
    "CF-causing",
    "K830X",
    "2"
  ],
  "298G>T": [
    "298G>T",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "E56X",
    "CF-causing",
    "p.Glu56X",
    "c.166G>T",
    "2"
  ],
  "E56X": [
    "298G>T",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "E56X",
    "CF-causing",
    "p.Glu56X",
    "c.166G>T",
    "2"
  ],
  "p.Glu56X": [
    "298G>T",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "E56X",
    "CF-causing",
    "p.Glu56X",
    "c.166G>T",
    "2"
  ],
  "c.166G>T": [
    "298G>T",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "E56X",
    "CF-causing",
    "p.Glu56X",
    "c.166G>T",
    "2"
  ],
  "G1003X": [
    "No",
    "G1003X",
    "p.Gly1003X",
    "3139G>T",
    "9.473913578960333e-06",
    "CF-causing",
    "c.3007G>T",
    "2"
  ],
  "p.Gly1003X": [
    "No",
    "G1003X",
    "p.Gly1003X",
    "3139G>T",
    "9.473913578960333e-06",
    "CF-causing",
    "c.3007G>T",
    "2"
  ],
  "3139G>T": [
    "No",
    "G1003X",
    "p.Gly1003X",
    "3139G>T",
    "9.473913578960333e-06",
    "CF-causing",
    "c.3007G>T",
    "2"
  ],
  "c.3007G>T": [
    "No",
    "G1003X",
    "p.Gly1003X",
    "3139G>T",
    "9.473913578960333e-06",
    "CF-causing",
    "c.3007G>T",
    "2"
  ],
  "p.Leu1011X": [
    "p.Leu1011X",
    "Yes, new variant added",
    "L1011X",
    "c.3032T>G",
    "9.473913578960333e-06",
    "CF-causing",
    "3164T>G",
    "2"
  ],
  "L1011X": [
    "p.Leu1011X",
    "Yes, new variant added",
    "L1011X",
    "c.3032T>G",
    "9.473913578960333e-06",
    "CF-causing",
    "3164T>G",
    "2"
  ],
  "c.3032T>G": [
    "p.Leu1011X",
    "Yes, new variant added",
    "L1011X",
    "c.3032T>G",
    "9.473913578960333e-06",
    "CF-causing",
    "3164T>G",
    "2"
  ],
  "3164T>G": [
    "p.Leu1011X",
    "Yes, new variant added",
    "L1011X",
    "c.3032T>G",
    "9.473913578960333e-06",
    "CF-causing",
    "3164T>G",
    "2"
  ],
  "c.3546C>G": [
    "c.3546C>G",
    "No",
    "Y1182X",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "p.Tyr1182X",
    "3678C>G"
  ],
  "Y1182X": [
    "c.3546C>G",
    "No",
    "Y1182X",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "p.Tyr1182X",
    "3678C>G"
  ],
  "p.Tyr1182X": [
    "c.3546C>G",
    "No",
    "Y1182X",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "p.Tyr1182X",
    "3678C>G"
  ],
  "3678C>G": [
    "c.3546C>G",
    "No",
    "Y1182X",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "p.Tyr1182X",
    "3678C>G"
  ],
  "c.253G>T": [
    "c.253G>T",
    "Yes, new variant added",
    "385G>T",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "p.Gly85X",
    "G85X"
  ],
  "385G>T": [
    "c.253G>T",
    "Yes, new variant added",
    "385G>T",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "p.Gly85X",
    "G85X"
  ],
  "p.Gly85X": [
    "c.253G>T",
    "Yes, new variant added",
    "385G>T",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "p.Gly85X",
    "G85X"
  ],
  "G85X": [
    "c.253G>T",
    "Yes, new variant added",
    "385G>T",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "p.Gly85X",
    "G85X"
  ],
  "G1247X": [
    "G1247X",
    "Yes, new variant added",
    "c.3739G>T",
    "p.Gly1247X",
    "3871G>T",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "c.3739G>T": [
    "G1247X",
    "Yes, new variant added",
    "c.3739G>T",
    "p.Gly1247X",
    "3871G>T",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "p.Gly1247X": [
    "G1247X",
    "Yes, new variant added",
    "c.3739G>T",
    "p.Gly1247X",
    "3871G>T",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "3871G>T": [
    "G1247X",
    "Yes, new variant added",
    "c.3739G>T",
    "p.Gly1247X",
    "3871G>T",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "c.3859G>T": [
    "c.3859G>T",
    "p.Gly1287X",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "G1287X",
    "2",
    "3991G>T"
  ],
  "p.Gly1287X": [
    "c.3859G>T",
    "p.Gly1287X",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "G1287X",
    "2",
    "3991G>T"
  ],
  "G1287X": [
    "c.3859G>T",
    "p.Gly1287X",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "G1287X",
    "2",
    "3991G>T"
  ],
  "3991G>T": [
    "c.3859G>T",
    "p.Gly1287X",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "G1287X",
    "2",
    "3991G>T"
  ],
  "4053T>A": [
    "4053T>A",
    "No",
    "p.Tyr1307X",
    "9.473913578960333e-06",
    "CF-causing",
    "c.3921T>A",
    "2",
    "Y1307X"
  ],
  "p.Tyr1307X": [
    "4053T>A",
    "No",
    "p.Tyr1307X",
    "9.473913578960333e-06",
    "CF-causing",
    "c.3921T>A",
    "2",
    "Y1307X"
  ],
  "c.3921T>A": [
    "4053T>A",
    "No",
    "p.Tyr1307X",
    "9.473913578960333e-06",
    "CF-causing",
    "c.3921T>A",
    "2",
    "Y1307X"
  ],
  "Y1307X": [
    "4053T>A",
    "No",
    "p.Tyr1307X",
    "9.473913578960333e-06",
    "CF-causing",
    "c.3921T>A",
    "2",
    "Y1307X"
  ],
  "p.Trp1316X": [
    "p.Trp1316X",
    "No",
    "W1316X",
    "9.473913578960333e-06",
    "CF-causing",
    "4079G>A",
    "2",
    "c.3947G>A"
  ],
  "W1316X": [
    "p.Trp1316X",
    "No",
    "W1316X",
    "9.473913578960333e-06",
    "CF-causing",
    "4079G>A",
    "2",
    "c.3947G>A"
  ],
  "4079G>A": [
    "p.Trp1316X",
    "No",
    "W1316X",
    "9.473913578960333e-06",
    "CF-causing",
    "4079G>A",
    "2",
    "c.3947G>A"
  ],
  "c.3947G>A": [
    "p.Trp1316X",
    "No",
    "W1316X",
    "9.473913578960333e-06",
    "CF-causing",
    "4079G>A",
    "2",
    "c.3947G>A"
  ],
  "p.Tyr1381X": [
    "p.Tyr1381X",
    "Yes, new variant added",
    "Y1381X",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "4275C>A|4275C>G",
    "c.4143C>A|c.4143C>G"
  ],
  "Y1381X": [
    "p.Tyr1381X",
    "Yes, new variant added",
    "Y1381X",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "4275C>A|4275C>G",
    "c.4143C>A|c.4143C>G"
  ],
  "4275C>A|4275C>G": [
    "p.Tyr1381X",
    "Yes, new variant added",
    "Y1381X",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "4275C>A|4275C>G",
    "c.4143C>A|c.4143C>G"
  ],
  "c.4143C>A|c.4143C>G": [
    "p.Tyr1381X",
    "Yes, new variant added",
    "Y1381X",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "4275C>A|4275C>G",
    "c.4143C>A|c.4143C>G"
  ],
  "p.Glu1401X": [
    "p.Glu1401X",
    "E1401X",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "c.4201G>T",
    "2",
    "4333G>T"
  ],
  "E1401X": [
    "p.Glu1401X",
    "E1401X",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "c.4201G>T",
    "2",
    "4333G>T"
  ],
  "c.4201G>T": [
    "p.Glu1401X",
    "E1401X",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "c.4201G>T",
    "2",
    "4333G>T"
  ],
  "4333G>T": [
    "p.Glu1401X",
    "E1401X",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "c.4201G>T",
    "2",
    "4333G>T"
  ],
  "Q151X": [
    "Q151X",
    "c.451C>T",
    "p.Gln151X",
    "Yes, new variant added",
    "583C>T",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "c.451C>T": [
    "Q151X",
    "c.451C>T",
    "p.Gln151X",
    "Yes, new variant added",
    "583C>T",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "p.Gln151X": [
    "Q151X",
    "c.451C>T",
    "p.Gln151X",
    "Yes, new variant added",
    "583C>T",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "583C>T": [
    "Q151X",
    "c.451C>T",
    "p.Gln151X",
    "Yes, new variant added",
    "583C>T",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "deletion of exon 12 (legacy numbering)|deletion of exon 13 (current numbering)": [
    "p.?",
    "Yes, new variant added",
    "deletion of exon 12 (legacy numbering)|deletion of exon 13 (current numbering)",
    "c.(1679+1_1680-1)_(1766+1_1767-1)del",
    "CFTRdele12",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "c.(1679+1_1680-1)_(1766+1_1767-1)del": [
    "p.?",
    "Yes, new variant added",
    "deletion of exon 12 (legacy numbering)|deletion of exon 13 (current numbering)",
    "c.(1679+1_1680-1)_(1766+1_1767-1)del",
    "CFTRdele12",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "CFTRdele12": [
    "p.?",
    "Yes, new variant added",
    "deletion of exon 12 (legacy numbering)|deletion of exon 13 (current numbering)",
    "c.(1679+1_1680-1)_(1766+1_1767-1)del",
    "CFTRdele12",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "c.(870-1053_870-126)_(1116+186_1117-409)del": [
    "c.(870-1053_870-126)_(1116+186_1117-409)del",
    "p.?",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "CFTRdele7",
    "2",
    "deletion of exon 7 (legacy numbering)|deletion of exon 8 (current numbering)"
  ],
  "CFTRdele7": [
    "c.(870-1053_870-126)_(1116+186_1117-409)del",
    "p.?",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "CFTRdele7",
    "2",
    "deletion of exon 7 (legacy numbering)|deletion of exon 8 (current numbering)"
  ],
  "deletion of exon 7 (legacy numbering)|deletion of exon 8 (current numbering)": [
    "c.(870-1053_870-126)_(1116+186_1117-409)del",
    "p.?",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "CFTRdele7",
    "2",
    "deletion of exon 7 (legacy numbering)|deletion of exon 8 (current numbering)"
  ],
  "deletion of exons 1 through 24 (legacy numbering)|deletion of exons 1 through 27 (current numbering)|deletion of entire CFTR gene": [
    "p.?",
    "Yes, new variant added",
    "deletion of exons 1 through 24 (legacy numbering)|deletion of exons 1 through 27 (current numbering)|deletion of entire CFTR gene",
    "9.473913578960333e-06",
    "CF-causing",
    "CFTRdele1-24",
    "c.(?_-1)_(*1_?)del",
    "2"
  ],
  "CFTRdele1-24": [
    "p.?",
    "Yes, new variant added",
    "deletion of exons 1 through 24 (legacy numbering)|deletion of exons 1 through 27 (current numbering)|deletion of entire CFTR gene",
    "9.473913578960333e-06",
    "CF-causing",
    "CFTRdele1-24",
    "c.(?_-1)_(*1_?)del",
    "2"
  ],
  "c.(?_-1)_(*1_?)del": [
    "p.?",
    "Yes, new variant added",
    "deletion of exons 1 through 24 (legacy numbering)|deletion of exons 1 through 27 (current numbering)|deletion of entire CFTR gene",
    "9.473913578960333e-06",
    "CF-causing",
    "CFTRdele1-24",
    "c.(?_-1)_(*1_?)del",
    "2"
  ],
  "CFTRdele11-18": [
    "CFTRdele11-18",
    "p.?",
    "Yes, new variant added",
    "c.(1584+1_1585-1)_(3468+1_3469-1)del",
    "9.473913578960333e-06",
    "CF-causing",
    "deletion of exons 11 through 18 (legacy numbering)|deletion of exons 12 through 21 (current numbering)",
    "2"
  ],
  "c.(1584+1_1585-1)_(3468+1_3469-1)del": [
    "CFTRdele11-18",
    "p.?",
    "Yes, new variant added",
    "c.(1584+1_1585-1)_(3468+1_3469-1)del",
    "9.473913578960333e-06",
    "CF-causing",
    "deletion of exons 11 through 18 (legacy numbering)|deletion of exons 12 through 21 (current numbering)",
    "2"
  ],
  "deletion of exons 11 through 18 (legacy numbering)|deletion of exons 12 through 21 (current numbering)": [
    "CFTRdele11-18",
    "p.?",
    "Yes, new variant added",
    "c.(1584+1_1585-1)_(3468+1_3469-1)del",
    "9.473913578960333e-06",
    "CF-causing",
    "deletion of exons 11 through 18 (legacy numbering)|deletion of exons 12 through 21 (current numbering)",
    "2"
  ],
  "deletion of exons 14a through 17b (legacy numbering)|deletion of exons 15 through 20 (current numbering)": [
    "p.?",
    "Yes, new variant added",
    "deletion of exons 14a through 17b (legacy numbering)|deletion of exons 15 through 20 (current numbering)",
    "CFTRdele14a-17b",
    "c.(2490+1_2491-1)_(3367+1_3368-1)del",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "CFTRdele14a-17b": [
    "p.?",
    "Yes, new variant added",
    "deletion of exons 14a through 17b (legacy numbering)|deletion of exons 15 through 20 (current numbering)",
    "CFTRdele14a-17b",
    "c.(2490+1_2491-1)_(3367+1_3368-1)del",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "c.(2490+1_2491-1)_(3367+1_3368-1)del": [
    "p.?",
    "Yes, new variant added",
    "deletion of exons 14a through 17b (legacy numbering)|deletion of exons 15 through 20 (current numbering)",
    "CFTRdele14a-17b",
    "c.(2490+1_2491-1)_(3367+1_3368-1)del",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "deletion of exons 16 and 17a (legacy numbering)|deletion of exons 18 and 19 (current numbering)": [
    "deletion of exons 16 and 17a (legacy numbering)|deletion of exons 18 and 19 (current numbering)",
    "p.?",
    "Yes, new variant added",
    "c.(2908+1_2909-1)_(3139+1_3140-1)del",
    "9.473913578960333e-06",
    "CF-causing",
    "CFTRdele16,17a",
    "2"
  ],
  "c.(2908+1_2909-1)_(3139+1_3140-1)del": [
    "deletion of exons 16 and 17a (legacy numbering)|deletion of exons 18 and 19 (current numbering)",
    "p.?",
    "Yes, new variant added",
    "c.(2908+1_2909-1)_(3139+1_3140-1)del",
    "9.473913578960333e-06",
    "CF-causing",
    "CFTRdele16,17a",
    "2"
  ],
  "CFTRdele16,17a": [
    "deletion of exons 16 and 17a (legacy numbering)|deletion of exons 18 and 19 (current numbering)",
    "p.?",
    "Yes, new variant added",
    "c.(2908+1_2909-1)_(3139+1_3140-1)del",
    "9.473913578960333e-06",
    "CF-causing",
    "CFTRdele16,17a",
    "2"
  ],
  "CFTRdele2-6b": [
    "p.?",
    "Yes, new variant added",
    "CFTRdele2-6b",
    "9.473913578960333e-06",
    "c.(53+1_54-1)_(869+1_870-1)del",
    "deletion of exons 2 through 6b (legacy numbering)|deletion of exons 2 through 7 (current numbering)",
    "CF-causing",
    "2"
  ],
  "c.(53+1_54-1)_(869+1_870-1)del": [
    "p.?",
    "Yes, new variant added",
    "CFTRdele2-6b",
    "9.473913578960333e-06",
    "c.(53+1_54-1)_(869+1_870-1)del",
    "deletion of exons 2 through 6b (legacy numbering)|deletion of exons 2 through 7 (current numbering)",
    "CF-causing",
    "2"
  ],
  "deletion of exons 2 through 6b (legacy numbering)|deletion of exons 2 through 7 (current numbering)": [
    "p.?",
    "Yes, new variant added",
    "CFTRdele2-6b",
    "9.473913578960333e-06",
    "c.(53+1_54-1)_(869+1_870-1)del",
    "deletion of exons 2 through 6b (legacy numbering)|deletion of exons 2 through 7 (current numbering)",
    "CF-causing",
    "2"
  ],
  "c.(1209+1_1210-1)_(1584+1_1585-1)del": [
    "p.?",
    "c.(1209+1_1210-1)_(1584+1_1585-1)del",
    "Yes, new variant added",
    "deletion of exons 9 and 10 (legacy numbering)|deletion of exons 10 and 11 (current numbering)",
    "9.473913578960333e-06",
    "CF-causing",
    "CFTRdele9,10",
    "2"
  ],
  "deletion of exons 9 and 10 (legacy numbering)|deletion of exons 10 and 11 (current numbering)": [
    "p.?",
    "c.(1209+1_1210-1)_(1584+1_1585-1)del",
    "Yes, new variant added",
    "deletion of exons 9 and 10 (legacy numbering)|deletion of exons 10 and 11 (current numbering)",
    "9.473913578960333e-06",
    "CF-causing",
    "CFTRdele9,10",
    "2"
  ],
  "CFTRdele9,10": [
    "p.?",
    "c.(1209+1_1210-1)_(1584+1_1585-1)del",
    "Yes, new variant added",
    "deletion of exons 9 and 10 (legacy numbering)|deletion of exons 10 and 11 (current numbering)",
    "9.473913578960333e-06",
    "CF-causing",
    "CFTRdele9,10",
    "2"
  ],
  "duplication of exons 16 and 17a (legacy numbering)|duplication of exons 18 and 19 (current numbering)": [
    "duplication of exons 16 and 17a (legacy numbering)|duplication of exons 18 and 19 (current numbering)",
    "p.?",
    "c.(2908+1_2909-1)_(3139+1_3140-1)dup",
    "CFTRdup16,17a",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "c.(2908+1_2909-1)_(3139+1_3140-1)dup": [
    "duplication of exons 16 and 17a (legacy numbering)|duplication of exons 18 and 19 (current numbering)",
    "p.?",
    "c.(2908+1_2909-1)_(3139+1_3140-1)dup",
    "CFTRdup16,17a",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "CFTRdup16,17a": [
    "duplication of exons 16 and 17a (legacy numbering)|duplication of exons 18 and 19 (current numbering)",
    "p.?",
    "c.(2908+1_2909-1)_(3139+1_3140-1)dup",
    "CFTRdup16,17a",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "duplication of exons 22 through 24 (legacy numbering)|duplication of exons 25 through 27 (current numbering)": [
    "duplication of exons 22 through 24 (legacy numbering)|duplication of exons 25 through 27 (current numbering)",
    "p.?",
    "Yes, new variant added",
    "c.(3963+1_3964-1)_(*1_?)dup",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "CFTRdup22-24"
  ],
  "c.(3963+1_3964-1)_(*1_?)dup": [
    "duplication of exons 22 through 24 (legacy numbering)|duplication of exons 25 through 27 (current numbering)",
    "p.?",
    "Yes, new variant added",
    "c.(3963+1_3964-1)_(*1_?)dup",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "CFTRdup22-24"
  ],
  "CFTRdup22-24": [
    "duplication of exons 22 through 24 (legacy numbering)|duplication of exons 25 through 27 (current numbering)",
    "p.?",
    "Yes, new variant added",
    "c.(3963+1_3964-1)_(*1_?)dup",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "CFTRdup22-24"
  ],
  "CFTRdup6b-16": [
    "CFTRdup6b-16",
    "c.(743+1_744-1)_(2988+1_2989-1)dup",
    "p.?",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "duplication of exons 6b through 16 (legacy numbering)|duplication of exons 6b through 18 (current numbering)",
    "2"
  ],
  "c.(743+1_744-1)_(2988+1_2989-1)dup": [
    "CFTRdup6b-16",
    "c.(743+1_744-1)_(2988+1_2989-1)dup",
    "p.?",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "duplication of exons 6b through 16 (legacy numbering)|duplication of exons 6b through 18 (current numbering)",
    "2"
  ],
  "duplication of exons 6b through 16 (legacy numbering)|duplication of exons 6b through 18 (current numbering)": [
    "CFTRdup6b-16",
    "c.(743+1_744-1)_(2988+1_2989-1)dup",
    "p.?",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "duplication of exons 6b through 16 (legacy numbering)|duplication of exons 6b through 18 (current numbering)",
    "2"
  ],
  "1812-2A->C": [
    "p.?",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "1812-2A->C",
    "2",
    "c.1680-2A>C"
  ],
  "c.1680-2A>C": [
    "p.?",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "1812-2A->C",
    "2",
    "c.1680-2A>C"
  ],
  "c.3140-1G>A": [
    "p.?",
    "No",
    "c.3140-1G>A",
    "9.473913578960333e-06",
    "CF-causing",
    "3272-1G->A",
    "2"
  ],
  "3272-1G->A": [
    "p.?",
    "No",
    "c.3140-1G>A",
    "9.473913578960333e-06",
    "CF-causing",
    "3272-1G->A",
    "2"
  ],
  "c.1210-1G>C": [
    "c.1210-1G>C",
    "p.?",
    "No",
    "1342-1G->C",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "1342-1G->C": [
    "c.1210-1G>C",
    "p.?",
    "No",
    "1342-1G->C",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "c.3139+2T>C": [
    "p.?",
    "No",
    "c.3139+2T>C",
    "9.473913578960333e-06",
    "CF-causing",
    "3271+2T->C",
    "2"
  ],
  "3271+2T->C": [
    "p.?",
    "No",
    "c.3139+2T>C",
    "9.473913578960333e-06",
    "CF-causing",
    "3271+2T->C",
    "2"
  ],
  "c.3468+1G>A": [
    "c.3468+1G>A",
    "p.?",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "3600+1G->A",
    "2"
  ],
  "3600+1G->A": [
    "c.3468+1G>A",
    "p.?",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "3600+1G->A",
    "2"
  ],
  "621+2T->G": [
    "p.?",
    "No",
    "621+2T->G",
    "9.473913578960333e-06",
    "CF-causing",
    "c.489+2T>G",
    "2"
  ],
  "c.489+2T>G": [
    "p.?",
    "No",
    "621+2T->G",
    "9.473913578960333e-06",
    "CF-causing",
    "c.489+2T>G",
    "2"
  ],
  "185+2T->C": [
    "p.?",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "185+2T->C",
    "2",
    "c.53+2T>C"
  ],
  "c.53+2T>C": [
    "p.?",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "185+2T->C",
    "2",
    "c.53+2T>C"
  ],
  "710del4": [
    "p.?",
    "No",
    "710del4",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.579_579+3del"
  ],
  "c.579_579+3del": [
    "p.?",
    "No",
    "710del4",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.579_579+3del"
  ],
  "c.1209+1G>T": [
    "p.?",
    "No",
    "c.1209+1G>T",
    "9.473913578960333e-06",
    "CF-causing",
    "1341+1G->T",
    "2"
  ],
  "1341+1G->T": [
    "p.?",
    "No",
    "c.1209+1G>T",
    "9.473913578960333e-06",
    "CF-causing",
    "1341+1G->T",
    "2"
  ],
  "c.53+2T>G": [
    "p.?",
    "No",
    "c.53+2T>G",
    "9.473913578960333e-06",
    "CF-causing",
    "185+2T->G",
    "2"
  ],
  "185+2T->G": [
    "p.?",
    "No",
    "c.53+2T>G",
    "9.473913578960333e-06",
    "CF-causing",
    "185+2T->G",
    "2"
  ],
  "c.273+2T>G": [
    "p.?",
    "No",
    "c.273+2T>G",
    "9.473913578960333e-06",
    "CF-causing",
    "405+2T->G",
    "2"
  ],
  "405+2T->G": [
    "p.?",
    "No",
    "c.273+2T>G",
    "9.473913578960333e-06",
    "CF-causing",
    "405+2T->G",
    "2"
  ],
  "982delA": [
    "982delA",
    "No",
    "p.Met284X",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.850del"
  ],
  "p.Met284X": [
    "982delA",
    "No",
    "p.Met284X",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.850del"
  ],
  "c.850del": [
    "982delA",
    "No",
    "p.Met284X",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.850del"
  ],
  "1058delC": [
    "No",
    "1058delC",
    "9.473913578960333e-06",
    "p.Phe310SerfsX18",
    "CF-causing",
    "2",
    "c.927del"
  ],
  "p.Phe310SerfsX18": [
    "No",
    "1058delC",
    "9.473913578960333e-06",
    "p.Phe310SerfsX18",
    "CF-causing",
    "2",
    "c.927del"
  ],
  "c.927del": [
    "No",
    "1058delC",
    "9.473913578960333e-06",
    "p.Phe310SerfsX18",
    "CF-causing",
    "2",
    "c.927del"
  ],
  "p.Phe131LeufsX3": [
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Phe131LeufsX3",
    "c.393del",
    "525delT",
    "2"
  ],
  "c.393del": [
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Phe131LeufsX3",
    "c.393del",
    "525delT",
    "2"
  ],
  "525delT": [
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Phe131LeufsX3",
    "c.393del",
    "525delT",
    "2"
  ],
  "c.1375_1385del": [
    "c.1375_1385del",
    "No",
    "p.Ser459ArgfsX19",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "p.Ser459ArgfsX19": [
    "c.1375_1385del",
    "No",
    "p.Ser459ArgfsX19",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "p.Lys52AsnfsX39": [
    "No",
    "9.473913578960333e-06",
    "p.Lys52AsnfsX39",
    "CF-causing",
    "2",
    "284delA",
    "c.156del"
  ],
  "284delA": [
    "No",
    "9.473913578960333e-06",
    "p.Lys52AsnfsX39",
    "CF-causing",
    "2",
    "284delA",
    "c.156del"
  ],
  "c.156del": [
    "No",
    "9.473913578960333e-06",
    "p.Lys52AsnfsX39",
    "CF-causing",
    "2",
    "284delA",
    "c.156del"
  ],
  "c.1981del": [
    "No",
    "c.1981del",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "p.Ile661SerfsX2",
    "2113delA"
  ],
  "p.Ile661SerfsX2": [
    "No",
    "c.1981del",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "p.Ile661SerfsX2",
    "2113delA"
  ],
  "2113delA": [
    "No",
    "c.1981del",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "p.Ile661SerfsX2",
    "2113delA"
  ],
  "c.2909del": [
    "c.2909del",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Gly970ValfsX11",
    "2",
    "3041delG"
  ],
  "p.Gly970ValfsX11": [
    "c.2909del",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Gly970ValfsX11",
    "2",
    "3041delG"
  ],
  "3041delG": [
    "c.2909del",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Gly970ValfsX11",
    "2",
    "3041delG"
  ],
  "p.Trp1089GlyfsX13": [
    "No",
    "p.Trp1089GlyfsX13",
    "c.3264del",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "3396delC"
  ],
  "c.3264del": [
    "No",
    "p.Trp1089GlyfsX13",
    "c.3264del",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "3396delC"
  ],
  "3396delC": [
    "No",
    "p.Trp1089GlyfsX13",
    "c.3264del",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "3396delC"
  ],
  "3521del14": [
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "3521del14",
    "2",
    "c.3389_3402del",
    "p.Gly1130ValfsX21"
  ],
  "c.3389_3402del": [
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "3521del14",
    "2",
    "c.3389_3402del",
    "p.Gly1130ValfsX21"
  ],
  "p.Gly1130ValfsX21": [
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "3521del14",
    "2",
    "c.3389_3402del",
    "p.Gly1130ValfsX21"
  ],
  "p.Lys1165X": [
    "p.Lys1165X",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "c.3493A>T",
    "K1165X",
    "1",
    "3625A>T"
  ],
  "3622insT": [
    "p.Lys1165X",
    "No",
    "3622insT",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.3492dup"
  ],
  "c.3492dup": [
    "p.Lys1165X",
    "No",
    "3622insT",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.3492dup"
  ],
  "489delC": [
    "489delC",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Ile119MetfsX5",
    "2",
    "c.357del"
  ],
  "p.Ile119MetfsX5": [
    "489delC",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Ile119MetfsX5",
    "2",
    "c.357del"
  ],
  "c.357del": [
    "489delC",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Ile119MetfsX5",
    "2",
    "c.357del"
  ],
  "p.Lys1200SerfsX12": [
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Lys1200SerfsX12",
    "3730A->TCT",
    "2",
    "c.3598delinsTCT"
  ],
  "3730A->TCT": [
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Lys1200SerfsX12",
    "3730A->TCT",
    "2",
    "c.3598delinsTCT"
  ],
  "c.3598delinsTCT": [
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Lys1200SerfsX12",
    "3730A->TCT",
    "2",
    "c.3598delinsTCT"
  ],
  "c.548del": [
    "No",
    "c.548del",
    "9.473913578960333e-06",
    "p.Leu183ProfsX6",
    "CF-causing",
    "680delT",
    "2"
  ],
  "p.Leu183ProfsX6": [
    "No",
    "c.548del",
    "9.473913578960333e-06",
    "p.Leu183ProfsX6",
    "CF-causing",
    "680delT",
    "2"
  ],
  "680delT": [
    "No",
    "c.548del",
    "9.473913578960333e-06",
    "p.Leu183ProfsX6",
    "CF-causing",
    "680delT",
    "2"
  ],
  "p.Leu365TrpfsX16": [
    "No",
    "p.Leu365TrpfsX16",
    "1221delCT",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.1093_1094del"
  ],
  "1221delCT": [
    "No",
    "p.Leu365TrpfsX16",
    "1221delCT",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.1093_1094del"
  ],
  "c.1093_1094del": [
    "No",
    "p.Leu365TrpfsX16",
    "1221delCT",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.1093_1094del"
  ],
  "p.Leu387AsnfsX23": [
    "No",
    "p.Leu387AsnfsX23",
    "9.473913578960333e-06",
    "CF-causing",
    "c.1159_1160del",
    "2",
    "1291delTT"
  ],
  "c.1159_1160del": [
    "No",
    "p.Leu387AsnfsX23",
    "9.473913578960333e-06",
    "CF-causing",
    "c.1159_1160del",
    "2",
    "1291delTT"
  ],
  "1291delTT": [
    "No",
    "p.Leu387AsnfsX23",
    "9.473913578960333e-06",
    "CF-causing",
    "c.1159_1160del",
    "2",
    "1291delTT"
  ],
  "p.Leu475ArgfsX52": [
    "p.Leu475ArgfsX52",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "1556delT",
    "c.1424del"
  ],
  "1556delT": [
    "p.Leu475ArgfsX52",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "1556delT",
    "c.1424del"
  ],
  "c.1424del": [
    "p.Leu475ArgfsX52",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "1556delT",
    "c.1424del"
  ],
  "c.1446dup": [
    "c.1446dup",
    "No",
    "p.Lys483X",
    "9.473913578960333e-06",
    "CF-causing",
    "1576insT",
    "2"
  ],
  "p.Lys483X": [
    "c.1446dup",
    "No",
    "p.Lys483X",
    "9.473913578960333e-06",
    "CF-causing",
    "1576insT",
    "2"
  ],
  "1576insT": [
    "c.1446dup",
    "No",
    "p.Lys483X",
    "9.473913578960333e-06",
    "CF-causing",
    "1576insT",
    "2"
  ],
  "c.1682dup": [
    "c.1682dup",
    "No",
    "p.Val562SerfsX6",
    "9.473913578960333e-06",
    "CF-causing",
    "1813insC",
    "2"
  ],
  "p.Val562SerfsX6": [
    "c.1682dup",
    "No",
    "p.Val562SerfsX6",
    "9.473913578960333e-06",
    "CF-causing",
    "1813insC",
    "2"
  ],
  "1813insC": [
    "c.1682dup",
    "No",
    "p.Val562SerfsX6",
    "9.473913578960333e-06",
    "CF-causing",
    "1813insC",
    "2"
  ],
  "c.1786_1787del": [
    "No",
    "c.1786_1787del",
    "9.473913578960333e-06",
    "p.Ala596X",
    "1918delGC",
    "CF-causing",
    "2"
  ],
  "p.Ala596X": [
    "No",
    "c.1786_1787del",
    "9.473913578960333e-06",
    "p.Ala596X",
    "1918delGC",
    "CF-causing",
    "2"
  ],
  "1918delGC": [
    "No",
    "c.1786_1787del",
    "9.473913578960333e-06",
    "p.Ala596X",
    "1918delGC",
    "CF-causing",
    "2"
  ],
  "c.1807delG": [
    "No",
    "c.1807delG",
    "9.473913578960333e-06",
    "CF-causing",
    "c.1807del",
    "2",
    "p.Val603SerfsX8"
  ],
  "c.1807del": [
    "No",
    "c.1807delG",
    "9.473913578960333e-06",
    "CF-causing",
    "c.1807del",
    "2",
    "p.Val603SerfsX8"
  ],
  "p.Val603SerfsX8": [
    "No",
    "c.1807delG",
    "9.473913578960333e-06",
    "CF-causing",
    "c.1807del",
    "2",
    "p.Val603SerfsX8"
  ],
  "1978dupA": [
    "No",
    "9.473913578960333e-06",
    "1978dupA",
    "c.1846dup",
    "CF-causing",
    "p.Ile616AsnfsX6",
    "2"
  ],
  "c.1846dup": [
    "No",
    "9.473913578960333e-06",
    "1978dupA",
    "c.1846dup",
    "CF-causing",
    "p.Ile616AsnfsX6",
    "2"
  ],
  "p.Ile616AsnfsX6": [
    "No",
    "9.473913578960333e-06",
    "1978dupA",
    "c.1846dup",
    "CF-causing",
    "p.Ile616AsnfsX6",
    "2"
  ],
  "2189CT->A": [
    "No",
    "2189CT->A",
    "p.Ser686TyrfsX36",
    "9.473913578960333e-06",
    "CF-causing",
    "c.2057_2058delinsA",
    "2"
  ],
  "p.Ser686TyrfsX36": [
    "No",
    "2189CT->A",
    "p.Ser686TyrfsX36",
    "9.473913578960333e-06",
    "CF-causing",
    "c.2057_2058delinsA",
    "2"
  ],
  "c.2057_2058delinsA": [
    "No",
    "2189CT->A",
    "p.Ser686TyrfsX36",
    "9.473913578960333e-06",
    "CF-causing",
    "c.2057_2058delinsA",
    "2"
  ],
  "c.2148del": [
    "c.2148del",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Thr717LeufsX5",
    "2",
    "c.2148delG"
  ],
  "p.Thr717LeufsX5": [
    "c.2148del",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Thr717LeufsX5",
    "2",
    "c.2148delG"
  ],
  "c.2148delG": [
    "c.2148del",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Thr717LeufsX5",
    "2",
    "c.2148delG"
  ],
  "p.His784SerfsX21": [
    "p.His784SerfsX21",
    "No",
    "c.2349dup",
    "9.473913578960333e-06",
    "2481-2482insT",
    "CF-causing",
    "2"
  ],
  "c.2349dup": [
    "p.His784SerfsX21",
    "No",
    "c.2349dup",
    "9.473913578960333e-06",
    "2481-2482insT",
    "CF-causing",
    "2"
  ],
  "2481-2482insT": [
    "p.His784SerfsX21",
    "No",
    "c.2349dup",
    "9.473913578960333e-06",
    "2481-2482insT",
    "CF-causing",
    "2"
  ],
  "p.Leu859X": [
    "p.Leu859X",
    "c.2576_2588del",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "2708del13"
  ],
  "c.2576_2588del": [
    "p.Leu859X",
    "c.2576_2588del",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "2708del13"
  ],
  "2708del13": [
    "p.Leu859X",
    "c.2576_2588del",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "2708del13"
  ],
  "p.Ala9GlyfsX36": [
    "No",
    "p.Ala9GlyfsX36",
    "9.473913578960333e-06",
    "CF-causing",
    "c.25dup",
    "2",
    "156insG"
  ],
  "c.25dup": [
    "No",
    "p.Ala9GlyfsX36",
    "9.473913578960333e-06",
    "CF-causing",
    "c.25dup",
    "2",
    "156insG"
  ],
  "156insG": [
    "No",
    "p.Ala9GlyfsX36",
    "9.473913578960333e-06",
    "CF-causing",
    "c.25dup",
    "2",
    "156insG"
  ],
  "c.2705del": [
    "No",
    "c.2705del",
    "p.Ser902ThrfsX4",
    "9.473913578960333e-06",
    "CF-causing",
    "2837delG",
    "2"
  ],
  "p.Ser902ThrfsX4": [
    "No",
    "c.2705del",
    "p.Ser902ThrfsX4",
    "9.473913578960333e-06",
    "CF-causing",
    "2837delG",
    "2"
  ],
  "2837delG": [
    "No",
    "c.2705del",
    "p.Ser902ThrfsX4",
    "9.473913578960333e-06",
    "CF-causing",
    "2837delG",
    "2"
  ],
  "2907delTT": [
    "No",
    "2907delTT",
    "c.2776_2777del",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "p.Leu926AlafsX48"
  ],
  "c.2776_2777del": [
    "No",
    "2907delTT",
    "c.2776_2777del",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "p.Leu926AlafsX48"
  ],
  "p.Leu926AlafsX48": [
    "No",
    "2907delTT",
    "c.2776_2777del",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "p.Leu926AlafsX48"
  ],
  "c.2964dup": [
    "c.2964dup",
    "No",
    "p.Leu989SerfsX5",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "3095insT"
  ],
  "p.Leu989SerfsX5": [
    "c.2964dup",
    "No",
    "p.Leu989SerfsX5",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "3095insT"
  ],
  "3095insT": [
    "c.2964dup",
    "No",
    "p.Leu989SerfsX5",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "3095insT"
  ],
  "3293delA": [
    "3293delA",
    "No",
    "c.3161del",
    "p.His1054LeufsX6",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "c.3161del": [
    "3293delA",
    "No",
    "c.3161del",
    "p.His1054LeufsX6",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "p.His1054LeufsX6": [
    "3293delA",
    "No",
    "c.3161del",
    "p.His1054LeufsX6",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "p.Thr1076IlefsX78": [
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Thr1076IlefsX78",
    "c.3227_3231del",
    "3359delCTCTG",
    "2"
  ],
  "c.3227_3231del": [
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Thr1076IlefsX78",
    "c.3227_3231del",
    "3359delCTCTG",
    "2"
  ],
  "3359delCTCTG": [
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Thr1076IlefsX78",
    "c.3227_3231del",
    "3359delCTCTG",
    "2"
  ],
  "3532AC->GTA": [
    "No",
    "3532AC->GTA",
    "9.473913578960333e-06",
    "CF-causing",
    "c.3400_3401delinsGTA",
    "2",
    "p.Thr1134ValfsX22"
  ],
  "c.3400_3401delinsGTA": [
    "No",
    "3532AC->GTA",
    "9.473913578960333e-06",
    "CF-causing",
    "c.3400_3401delinsGTA",
    "2",
    "p.Thr1134ValfsX22"
  ],
  "p.Thr1134ValfsX22": [
    "No",
    "3532AC->GTA",
    "9.473913578960333e-06",
    "CF-causing",
    "c.3400_3401delinsGTA",
    "2",
    "p.Thr1134ValfsX22"
  ],
  "p.Ser1206GlnfsX5": [
    "p.Ser1206GlnfsX5",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "c.3615del",
    "3747delC",
    "2"
  ],
  "c.3615del": [
    "p.Ser1206GlnfsX5",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "c.3615del",
    "3747delC",
    "2"
  ],
  "3747delC": [
    "p.Ser1206GlnfsX5",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "c.3615del",
    "3747delC",
    "2"
  ],
  "p.Ser1311LysfsX12": [
    "No",
    "p.Ser1311LysfsX12",
    "4064-4065delinsAATATG",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.3932_3933delinsAATATG"
  ],
  "4064-4065delinsAATATG": [
    "No",
    "p.Ser1311LysfsX12",
    "4064-4065delinsAATATG",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.3932_3933delinsAATATG"
  ],
  "c.3932_3933delinsAATATG": [
    "No",
    "p.Ser1311LysfsX12",
    "4064-4065delinsAATATG",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.3932_3933delinsAATATG"
  ],
  "c.3976del": [
    "c.3976del",
    "No",
    "4108delT",
    "9.473913578960333e-06",
    "p.Ser1326LeufsX2",
    "CF-causing",
    "2"
  ],
  "4108delT": [
    "c.3976del",
    "No",
    "4108delT",
    "9.473913578960333e-06",
    "p.Ser1326LeufsX2",
    "CF-causing",
    "2"
  ],
  "p.Ser1326LeufsX2": [
    "c.3976del",
    "No",
    "4108delT",
    "9.473913578960333e-06",
    "p.Ser1326LeufsX2",
    "CF-causing",
    "2"
  ],
  "c.4046del": [
    "c.4046del",
    "4177delG",
    "No",
    "p.Gly1349AlafsX5",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "4177delG": [
    "c.4046del",
    "4177delG",
    "No",
    "p.Gly1349AlafsX5",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "p.Gly1349AlafsX5": [
    "c.4046del",
    "4177delG",
    "No",
    "p.Gly1349AlafsX5",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "c.4090del": [
    "No",
    "c.4090del",
    "9.473913578960333e-06",
    "CF-causing",
    "4222delG",
    "p.Ala1364ArgfsX16",
    "2"
  ],
  "4222delG": [
    "No",
    "c.4090del",
    "9.473913578960333e-06",
    "CF-causing",
    "4222delG",
    "p.Ala1364ArgfsX16",
    "2"
  ],
  "p.Ala1364ArgfsX16": [
    "No",
    "c.4090del",
    "9.473913578960333e-06",
    "CF-causing",
    "4222delG",
    "p.Ala1364ArgfsX16",
    "2"
  ],
  "542del7": [
    "542del7",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Leu137ProfsX14",
    "2",
    "c.410_416del"
  ],
  "p.Leu137ProfsX14": [
    "542del7",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Leu137ProfsX14",
    "2",
    "c.410_416del"
  ],
  "c.410_416del": [
    "542del7",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Leu137ProfsX14",
    "2",
    "c.410_416del"
  ],
  "654del5": [
    "654del5",
    "No",
    "c.522_526del",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Ile175TyrfsX6",
    "2"
  ],
  "c.522_526del": [
    "654del5",
    "No",
    "c.522_526del",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Ile175TyrfsX6",
    "2"
  ],
  "p.Ile175TyrfsX6": [
    "654del5",
    "No",
    "c.522_526del",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Ile175TyrfsX6",
    "2"
  ],
  "p.Ser182GlnfsX6": [
    "No",
    "p.Ser182GlnfsX6",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "675del14",
    "c.543_556del"
  ],
  "675del14": [
    "No",
    "p.Ser182GlnfsX6",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "675del14",
    "c.543_556del"
  ],
  "c.543_556del": [
    "No",
    "p.Ser182GlnfsX6",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "675del14",
    "c.543_556del"
  ],
  "c.551_555del": [
    "c.551_555del",
    "No",
    "p.Leu184GlnfsX7",
    "9.473913578960333e-06",
    "CF-causing",
    "c.551_555delTTTCC",
    "2"
  ],
  "p.Leu184GlnfsX7": [
    "c.551_555del",
    "No",
    "p.Leu184GlnfsX7",
    "9.473913578960333e-06",
    "CF-causing",
    "c.551_555delTTTCC",
    "2"
  ],
  "c.551_555delTTTCC": [
    "c.551_555del",
    "No",
    "p.Leu184GlnfsX7",
    "9.473913578960333e-06",
    "CF-causing",
    "c.551_555delTTTCC",
    "2"
  ],
  "c.581_582del": [
    "No",
    "c.581_582del",
    "9.473913578960333e-06",
    "CF-causing",
    "713delGA",
    "2",
    "p.Gly194AlafsX63"
  ],
  "713delGA": [
    "No",
    "c.581_582del",
    "9.473913578960333e-06",
    "CF-causing",
    "713delGA",
    "2",
    "p.Gly194AlafsX63"
  ],
  "p.Gly194AlafsX63": [
    "No",
    "c.581_582del",
    "9.473913578960333e-06",
    "CF-causing",
    "713delGA",
    "2",
    "p.Gly194AlafsX63"
  ],
  "p.Trp202AspfsX55": [
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Trp202AspfsX55",
    "c.604_605delTG",
    "2",
    "c.604_605del"
  ],
  "c.604_605delTG": [
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Trp202AspfsX55",
    "c.604_605delTG",
    "2",
    "c.604_605del"
  ],
  "c.604_605del": [
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Trp202AspfsX55",
    "c.604_605delTG",
    "2",
    "c.604_605del"
  ],
  "840insT": [
    "840insT",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "c.708dup",
    "2",
    "p.Gln237SerfsX21"
  ],
  "c.708dup": [
    "840insT",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "c.708dup",
    "2",
    "p.Gln237SerfsX21"
  ],
  "p.Gln237SerfsX21": [
    "840insT",
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "c.708dup",
    "2",
    "p.Gln237SerfsX21"
  ],
  "p.Ala842SerfsX45": [
    "No",
    "p.Ala842SerfsX45",
    "9.473913578960333e-06",
    "CF-causing",
    "2655del26",
    "c.2523_2548del",
    "2"
  ],
  "2655del26": [
    "No",
    "p.Ala842SerfsX45",
    "9.473913578960333e-06",
    "CF-causing",
    "2655del26",
    "c.2523_2548del",
    "2"
  ],
  "c.2523_2548del": [
    "No",
    "p.Ala842SerfsX45",
    "9.473913578960333e-06",
    "CF-causing",
    "2655del26",
    "c.2523_2548del",
    "2"
  ],
  "c.4028dup": [
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "c.4028dup",
    "p.Cys1344LeufsX15",
    "2",
    "4160insG"
  ],
  "p.Cys1344LeufsX15": [
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "c.4028dup",
    "p.Cys1344LeufsX15",
    "2",
    "4160insG"
  ],
  "4160insG": [
    "No",
    "9.473913578960333e-06",
    "CF-causing",
    "c.4028dup",
    "p.Cys1344LeufsX15",
    "2",
    "4160insG"
  ],
  "c.1A>C": [
    "p.?",
    "No",
    "9.473913578960333e-06",
    "c.1A>C",
    "CF-causing",
    "2",
    "M1L"
  ],
  "M1L": [
    "p.?",
    "No",
    "9.473913578960333e-06",
    "c.1A>C",
    "CF-causing",
    "2",
    "M1L"
  ],
  "1812-1G->C": [
    "p.?",
    "1812-1G->C",
    "No",
    "c.1680-1G>C",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "CF-causing - previously IVS11-1G->C"
  ],
  "c.1680-1G>C": [
    "p.?",
    "1812-1G->C",
    "No",
    "c.1680-1G>C",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "CF-causing - previously IVS11-1G->C"
  ],
  "CF-causing - previously IVS11-1G->C": [
    "p.?",
    "1812-1G->C",
    "No",
    "c.1680-1G>C",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "CF-causing - previously IVS11-1G->C"
  ],
  "1001+2T->A": [
    "p.?",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "1001+2T->A",
    "c.869+2T>A",
    "2"
  ],
  "c.869+2T>A": [
    "p.?",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "1001+2T->A",
    "c.869+2T>A",
    "2"
  ],
  "4095+1G->T": [
    "p.?",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "4095+1G->T",
    "CF-causing",
    "c.3963+1G>T",
    "2"
  ],
  "c.3963+1G>T": [
    "p.?",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "4095+1G->T",
    "CF-causing",
    "c.3963+1G>T",
    "2"
  ],
  "c.3964-1G>A": [
    "p.?",
    "Yes, new variant added",
    "c.3964-1G>A",
    "9.473913578960333e-06",
    "CF-causing",
    "4096-1G->A",
    "2"
  ],
  "4096-1G->A": [
    "p.?",
    "Yes, new variant added",
    "c.3964-1G>A",
    "9.473913578960333e-06",
    "CF-causing",
    "4096-1G->A",
    "2"
  ],
  "3041-1G->C": [
    "p.?",
    "Yes, new variant added",
    "3041-1G->C",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.2909-1G>C"
  ],
  "c.2909-1G>C": [
    "p.?",
    "Yes, new variant added",
    "3041-1G->C",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.2909-1G>C"
  ],
  "c.3469-1G>C": [
    "c.3469-1G>C",
    "p.?",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "3601-1G->C",
    "2"
  ],
  "3601-1G->C": [
    "c.3469-1G>C",
    "p.?",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "3601-1G->C",
    "2"
  ],
  "c.579+2T>C": [
    "p.?",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "c.579+2T>C",
    "2",
    "711+2T->C"
  ],
  "711+2T->C": [
    "p.?",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "c.579+2T>C",
    "2",
    "711+2T->C"
  ],
  "1001+2T->G": [
    "p.?",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "1001+2T->G",
    "2",
    "c.869+2T>G"
  ],
  "c.869+2T>G": [
    "p.?",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "1001+2T->G",
    "2",
    "c.869+2T>G"
  ],
  "1716+2delT": [
    "p.?",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "1716+2delT",
    "2",
    "c.1584+2del"
  ],
  "c.1584+2del": [
    "p.?",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "1716+2delT",
    "2",
    "c.1584+2del"
  ],
  "3499+2T->A": [
    "p.?",
    "Yes, new variant added",
    "3499+2T->A",
    "9.473913578960333e-06",
    "c.3367+2T>A",
    "CF-causing",
    "2"
  ],
  "c.3367+2T>A": [
    "p.?",
    "Yes, new variant added",
    "3499+2T->A",
    "9.473913578960333e-06",
    "c.3367+2T>A",
    "CF-causing",
    "2"
  ],
  "c.2909-1G>A": [
    "p.?",
    "Yes, new variant added",
    "c.2909-1G>A",
    "9.473913578960333e-06",
    "CF-causing",
    "3041-1G->A",
    "2"
  ],
  "3041-1G->A": [
    "p.?",
    "Yes, new variant added",
    "c.2909-1G>A",
    "9.473913578960333e-06",
    "CF-causing",
    "3041-1G->A",
    "2"
  ],
  "4040dupA": [
    "4040dupA",
    "Yes, new variant added",
    "p.Asn1303LysfsX6",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.3908dup"
  ],
  "p.Asn1303LysfsX6": [
    "4040dupA",
    "Yes, new variant added",
    "p.Asn1303LysfsX6",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.3908dup"
  ],
  "c.3908dup": [
    "4040dupA",
    "Yes, new variant added",
    "p.Asn1303LysfsX6",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.3908dup"
  ],
  "c.1543_1555del": [
    "Yes, new variant added",
    "c.1543_1555del",
    "9.473913578960333e-06",
    "CF-causing",
    "1675_1687del13",
    "p.Tyr515AlafsX8",
    "2"
  ],
  "1675_1687del13": [
    "Yes, new variant added",
    "c.1543_1555del",
    "9.473913578960333e-06",
    "CF-causing",
    "1675_1687del13",
    "p.Tyr515AlafsX8",
    "2"
  ],
  "p.Tyr515AlafsX8": [
    "Yes, new variant added",
    "c.1543_1555del",
    "9.473913578960333e-06",
    "CF-causing",
    "1675_1687del13",
    "p.Tyr515AlafsX8",
    "2"
  ],
  "c.3231_3232del": [
    "c.3231_3232del",
    "Yes, new variant added",
    "c.3231_3232delGT",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Phe1078ProfsX77",
    "2"
  ],
  "c.3231_3232delGT": [
    "c.3231_3232del",
    "Yes, new variant added",
    "c.3231_3232delGT",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Phe1078ProfsX77",
    "2"
  ],
  "p.Phe1078ProfsX77": [
    "c.3231_3232del",
    "Yes, new variant added",
    "c.3231_3232delGT",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Phe1078ProfsX77",
    "2"
  ],
  "c.3322del": [
    "Yes, new variant added",
    "c.3322del",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "3454delG",
    "p.Val1108SerfsX13"
  ],
  "3454delG": [
    "Yes, new variant added",
    "c.3322del",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "3454delG",
    "p.Val1108SerfsX13"
  ],
  "p.Val1108SerfsX13": [
    "Yes, new variant added",
    "c.3322del",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "3454delG",
    "p.Val1108SerfsX13"
  ],
  "p.Leu1279AlafsX22": [
    "Yes, new variant added",
    "p.Leu1279AlafsX22",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "3967delTT",
    "c.3835_3836del"
  ],
  "3967delTT": [
    "Yes, new variant added",
    "p.Leu1279AlafsX22",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "3967delTT",
    "c.3835_3836del"
  ],
  "c.3835_3836del": [
    "Yes, new variant added",
    "p.Leu1279AlafsX22",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "3967delTT",
    "c.3835_3836del"
  ],
  "c.40_44delAAACT": [
    "Yes, new variant added",
    "c.40_44delAAACT",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Lys14PhefsX29",
    "c.40_44del",
    "2"
  ],
  "p.Lys14PhefsX29": [
    "Yes, new variant added",
    "c.40_44delAAACT",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Lys14PhefsX29",
    "c.40_44del",
    "2"
  ],
  "c.40_44del": [
    "Yes, new variant added",
    "c.40_44delAAACT",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Lys14PhefsX29",
    "c.40_44del",
    "2"
  ],
  "c.4028del": [
    "c.4028del",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "p.Gly1343AlafsX4",
    "CF-causing",
    "c.4028delG",
    "2"
  ],
  "p.Gly1343AlafsX4": [
    "c.4028del",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "p.Gly1343AlafsX4",
    "CF-causing",
    "c.4028delG",
    "2"
  ],
  "c.4028delG": [
    "c.4028del",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "p.Gly1343AlafsX4",
    "CF-causing",
    "c.4028delG",
    "2"
  ],
  "p.Asp537ThrfsX3": [
    "p.Asp537ThrfsX3",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "c.1608del",
    "c.1608delA",
    "2"
  ],
  "c.1608del": [
    "p.Asp537ThrfsX3",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "c.1608del",
    "c.1608delA",
    "2"
  ],
  "c.1608delA": [
    "p.Asp537ThrfsX3",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "c.1608del",
    "c.1608delA",
    "2"
  ],
  "p.Leu570ArgfsX17": [
    "Yes, new variant added",
    "p.Leu570ArgfsX17",
    "9.473913578960333e-06",
    "CF-causing",
    "c.1708_1712delTTATT",
    "2",
    "c.1708_1712del"
  ],
  "c.1708_1712delTTATT": [
    "Yes, new variant added",
    "p.Leu570ArgfsX17",
    "9.473913578960333e-06",
    "CF-causing",
    "c.1708_1712delTTATT",
    "2",
    "c.1708_1712del"
  ],
  "c.1708_1712del": [
    "Yes, new variant added",
    "p.Leu570ArgfsX17",
    "9.473913578960333e-06",
    "CF-causing",
    "c.1708_1712delTTATT",
    "2",
    "c.1708_1712del"
  ],
  "c.1725del": [
    "Yes, new variant added",
    "c.1725del",
    "1857delT",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Phe575LeufsX4",
    "2"
  ],
  "1857delT": [
    "Yes, new variant added",
    "c.1725del",
    "1857delT",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Phe575LeufsX4",
    "2"
  ],
  "p.Phe575LeufsX4": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.1725_1727delinsAT",
    "CF-causing",
    "p.Phe575LeufsX4",
    "1"
  ],
  "p.Thr787AspfsX18": [
    "p.Thr787AspfsX18",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "c.2357dupA",
    "CF-causing",
    "2",
    "c.2357dup"
  ],
  "c.2357dupA": [
    "p.Thr787AspfsX18",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "c.2357dupA",
    "CF-causing",
    "2",
    "c.2357dup"
  ],
  "c.2357dup": [
    "p.Thr787AspfsX18",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "c.2357dupA",
    "CF-causing",
    "2",
    "c.2357dup"
  ],
  "c.324del": [
    "c.324del",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "c.324delC",
    "CF-causing",
    "p.Tyr109MetfsX15",
    "2"
  ],
  "c.324delC": [
    "c.324del",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "c.324delC",
    "CF-causing",
    "p.Tyr109MetfsX15",
    "2"
  ],
  "p.Tyr109MetfsX15": [
    "c.324del",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "c.324delC",
    "CF-causing",
    "p.Tyr109MetfsX15",
    "2"
  ],
  "c.3495del": [
    "Yes, new variant added",
    "c.3495del",
    "9.473913578960333e-06",
    "c.3495delG",
    "CF-causing",
    "2",
    "p.Lys1165AsnfsX27"
  ],
  "c.3495delG": [
    "Yes, new variant added",
    "c.3495del",
    "9.473913578960333e-06",
    "c.3495delG",
    "CF-causing",
    "2",
    "p.Lys1165AsnfsX27"
  ],
  "p.Lys1165AsnfsX27": [
    "Yes, new variant added",
    "c.3495del",
    "9.473913578960333e-06",
    "c.3495delG",
    "CF-causing",
    "2",
    "p.Lys1165AsnfsX27"
  ],
  "c.405_406dup": [
    "c.405_406dup",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "538insAC",
    "p.Leu136HisfsX18"
  ],
  "538insAC": [
    "c.405_406dup",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "538insAC",
    "p.Leu136HisfsX18"
  ],
  "p.Leu136HisfsX18": [
    "c.405_406dup",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "538insAC",
    "p.Leu136HisfsX18"
  ],
  "c.433del": [
    "c.433del",
    "Yes, new variant added",
    "565delC",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Leu145PhefsX8",
    "2"
  ],
  "565delC": [
    "c.433del",
    "Yes, new variant added",
    "565delC",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Leu145PhefsX8",
    "2"
  ],
  "p.Leu145PhefsX8": [
    "c.433del",
    "Yes, new variant added",
    "565delC",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Leu145PhefsX8",
    "2"
  ],
  "c.494del": [
    "Yes, new variant added",
    "c.494del",
    "624delT",
    "9.473913578960333e-06",
    "p.Leu165X",
    "CF-causing",
    "2"
  ],
  "624delT": [
    "Yes, new variant added",
    "c.494del",
    "624delT",
    "9.473913578960333e-06",
    "p.Leu165X",
    "CF-causing",
    "2"
  ],
  "p.Leu165X": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.494T>A",
    "p.Leu165X",
    "CF-causing",
    "626T>A",
    "1",
    "L165X"
  ],
  "c.1219del": [
    "Yes, new variant added",
    "c.1219del",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Glu407AsnfsX35",
    "2",
    "c.1219delG"
  ],
  "p.Glu407AsnfsX35": [
    "Yes, new variant added",
    "c.1219del",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Glu407AsnfsX35",
    "2",
    "c.1219delG"
  ],
  "c.1219delG": [
    "Yes, new variant added",
    "c.1219del",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Glu407AsnfsX35",
    "2",
    "c.1219delG"
  ],
  "c.1433_1434del": [
    "Yes, new variant added",
    "c.1433_1434del",
    "9.473913578960333e-06",
    "CF-causing",
    "1565delCA",
    "p.Ser478X",
    "2"
  ],
  "1565delCA": [
    "Yes, new variant added",
    "c.1433_1434del",
    "9.473913578960333e-06",
    "CF-causing",
    "1565delCA",
    "p.Ser478X",
    "2"
  ],
  "p.Ser478X": [
    "Yes, new variant added",
    "c.1433_1434del",
    "9.473913578960333e-06",
    "CF-causing",
    "1565delCA",
    "p.Ser478X",
    "2"
  ],
  "p.Val510PhefsX17": [
    "p.Val510PhefsX17",
    "2",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "c.1528del",
    "1660delG"
  ],
  "c.1528del": [
    "p.Val510PhefsX17",
    "2",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "c.1528del",
    "1660delG"
  ],
  "1660delG": [
    "p.Val510PhefsX17",
    "2",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "c.1528del",
    "1660delG"
  ],
  "1845delAG/1846delGA": [
    "1845delAG/1846delGA",
    "Yes, new variant added",
    "p.Asp572LeufsX16",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.1714_1715del"
  ],
  "p.Asp572LeufsX16": [
    "1845delAG/1846delGA",
    "Yes, new variant added",
    "p.Asp572LeufsX16",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.1714_1715del"
  ],
  "c.1714_1715del": [
    "1845delAG/1846delGA",
    "Yes, new variant added",
    "p.Asp572LeufsX16",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.1714_1715del"
  ],
  "c.1853_1863del": [
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.1853_1863del",
    "p.Ile618ArgfsX2"
  ],
  "p.Ile618ArgfsX2": [
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.1853_1863del",
    "p.Ile618ArgfsX2"
  ],
  "p.Thr682LysfsX40": [
    "p.Thr682LysfsX40",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "c.2045del",
    "CF-causing",
    "c.2045delC",
    "2"
  ],
  "c.2045del": [
    "p.Thr682LysfsX40",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "c.2045del",
    "CF-causing",
    "c.2045delC",
    "2"
  ],
  "c.2045delC": [
    "p.Thr682LysfsX40",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "c.2045del",
    "CF-causing",
    "c.2045delC",
    "2"
  ],
  "c.2274_2275delinsT": [
    "c.2274_2275delinsT",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Thr760ArgfsX11",
    "2",
    "2406_2407delinsT"
  ],
  "p.Thr760ArgfsX11": [
    "4.7369567894801664e-06",
    "c.2277del",
    "No",
    "CF-causing",
    "2409delC",
    "1",
    "p.Thr760ArgfsX11"
  ],
  "2406_2407delinsT": [
    "c.2274_2275delinsT",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Thr760ArgfsX11",
    "2",
    "2406_2407delinsT"
  ],
  "c.2335del": [
    "Yes, new variant added",
    "9.473913578960333e-06",
    "c.2335del",
    "CF-causing",
    "p.Gln779LysfsX24",
    "2466delC",
    "2"
  ],
  "p.Gln779LysfsX24": [
    "Yes, new variant added",
    "9.473913578960333e-06",
    "c.2335del",
    "CF-causing",
    "p.Gln779LysfsX24",
    "2466delC",
    "2"
  ],
  "2466delC": [
    "Yes, new variant added",
    "9.473913578960333e-06",
    "c.2335del",
    "CF-causing",
    "p.Gln779LysfsX24",
    "2466delC",
    "2"
  ],
  "c.2340_2346del": [
    "c.2340_2346del",
    "2472_2478del7",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "p.Gln781PhefsX20"
  ],
  "2472_2478del7": [
    "c.2340_2346del",
    "2472_2478del7",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "p.Gln781PhefsX20"
  ],
  "p.Gln781PhefsX20": [
    "c.2340_2346del",
    "2472_2478del7",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "p.Gln781PhefsX20"
  ],
  "c.2879_2882delCTAT": [
    "Yes, new variant added",
    "c.2879_2882delCTAT",
    "9.473913578960333e-06",
    "p.Pro960ArgfsX7",
    "CF-causing",
    "2",
    "c.2879_2882del"
  ],
  "p.Pro960ArgfsX7": [
    "Yes, new variant added",
    "c.2879_2882delCTAT",
    "9.473913578960333e-06",
    "p.Pro960ArgfsX7",
    "CF-causing",
    "2",
    "c.2879_2882del"
  ],
  "c.2879_2882del": [
    "Yes, new variant added",
    "c.2879_2882delCTAT",
    "9.473913578960333e-06",
    "p.Pro960ArgfsX7",
    "CF-causing",
    "2",
    "c.2879_2882del"
  ],
  "c.3180delA": [
    "c.3180delA",
    "c.3180del",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Gly1061AspfsX22",
    "2"
  ],
  "c.3180del": [
    "c.3180delA",
    "c.3180del",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Gly1061AspfsX22",
    "2"
  ],
  "p.Gly1061AspfsX22": [
    "c.3180delA",
    "c.3180del",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Gly1061AspfsX22",
    "2"
  ],
  "c.3325del": [
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "c.3325del",
    "2",
    "c.3325delA",
    "p.Ile1109SerfsX12"
  ],
  "c.3325delA": [
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "c.3325del",
    "2",
    "c.3325delA",
    "p.Ile1109SerfsX12"
  ],
  "p.Ile1109SerfsX12": [
    "4.7369567894801664e-06",
    "No",
    "3456delC",
    "c.3324del",
    "CF-causing",
    "1",
    "p.Ile1109SerfsX12"
  ],
  "p.Leu1143ValfsX14": [
    "p.Leu1143ValfsX14",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "c.3426_3427insGTAA",
    "2"
  ],
  "c.3426_3427insGTAA": [
    "p.Leu1143ValfsX14",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "c.3426_3427insGTAA",
    "2"
  ],
  "c.4200_4201del": [
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "c.4200_4201del",
    "p.Cys1400X",
    "2",
    "4332delTG"
  ],
  "4332delTG": [
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "c.4200_4201del",
    "p.Cys1400X",
    "2",
    "4332delTG"
  ],
  "p.Gln2ArgfsX23": [
    "p.Gln2ArgfsX23",
    "Yes, new variant added",
    "c.4delC",
    "9.473913578960333e-06",
    "c.4del",
    "CF-causing",
    "2"
  ],
  "c.4delC": [
    "p.Gln2ArgfsX23",
    "Yes, new variant added",
    "c.4delC",
    "9.473913578960333e-06",
    "c.4del",
    "CF-causing",
    "2"
  ],
  "c.4del": [
    "p.Gln2ArgfsX23",
    "Yes, new variant added",
    "c.4delC",
    "9.473913578960333e-06",
    "c.4del",
    "CF-causing",
    "2"
  ],
  "954delA": [
    "954delA",
    "Yes, new variant added",
    "p.Tyr275ThrfsX10",
    "9.473913578960333e-06",
    "CF-causing",
    "c.822del",
    "2"
  ],
  "p.Tyr275ThrfsX10": [
    "954delA",
    "Yes, new variant added",
    "p.Tyr275ThrfsX10",
    "9.473913578960333e-06",
    "CF-causing",
    "c.822del",
    "2"
  ],
  "c.822del": [
    "954delA",
    "Yes, new variant added",
    "p.Tyr275ThrfsX10",
    "9.473913578960333e-06",
    "CF-causing",
    "c.822del",
    "2"
  ],
  "c.1312dup": [
    "c.1312dup",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Thr438AsnfsX8",
    "2",
    "c.1312dupA"
  ],
  "p.Thr438AsnfsX8": [
    "c.1312dup",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Thr438AsnfsX8",
    "2",
    "c.1312dupA"
  ],
  "c.1312dupA": [
    "c.1312dup",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Thr438AsnfsX8",
    "2",
    "c.1312dupA"
  ],
  "c.1573del": [
    "Yes, new variant added",
    "c.1573del",
    "9.473913578960333e-06",
    "CF-causing",
    "c.1573delC",
    "2",
    "p.Gln525AsnfsX2"
  ],
  "c.1573delC": [
    "Yes, new variant added",
    "c.1573del",
    "9.473913578960333e-06",
    "CF-causing",
    "c.1573delC",
    "2",
    "p.Gln525AsnfsX2"
  ],
  "p.Gln525AsnfsX2": [
    "Yes, new variant added",
    "c.1573del",
    "9.473913578960333e-06",
    "CF-causing",
    "c.1573delC",
    "2",
    "p.Gln525AsnfsX2"
  ],
  "p.Pro936GlnfsX6": [
    "p.Pro936GlnfsX6",
    "c.2805_2810delinsTCAGA",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "c.2805_2810delinsTCAGA": [
    "p.Pro936GlnfsX6",
    "c.2805_2810delinsTCAGA",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "2"
  ],
  "p.Ser977TyrfsX9": [
    "p.Ser977TyrfsX9",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "c.2929_2930insA",
    "3061insA",
    "2"
  ],
  "c.2929_2930insA": [
    "p.Ser977TyrfsX9",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "c.2929_2930insA",
    "3061insA",
    "2"
  ],
  "3061insA": [
    "p.Ser977TyrfsX9",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "c.2929_2930insA",
    "3061insA",
    "2"
  ],
  "p.Thr1176AsnfsX12": [
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Thr1176AsnfsX12",
    "2",
    "c.3525_3537del"
  ],
  "c.3525_3537del": [
    "Yes, new variant added",
    "9.473913578960333e-06",
    "CF-causing",
    "p.Thr1176AsnfsX12",
    "2",
    "c.3525_3537del"
  ],
  "p.Gly1208AlafsX3": [
    "p.Gly1208AlafsX3",
    "Yes, new variant added",
    "3755delG",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.3623del"
  ],
  "3750delA": [
    "p.Gly1208AlafsX3",
    "3750delA",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "c.3618del",
    "CF-causing",
    "2"
  ],
  "c.3618del": [
    "p.Gly1208AlafsX3",
    "3750delA",
    "Yes, new variant added",
    "9.473913578960333e-06",
    "c.3618del",
    "CF-causing",
    "2"
  ],
  "3755delG": [
    "p.Gly1208AlafsX3",
    "Yes, new variant added",
    "3755delG",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.3623del"
  ],
  "c.3623del": [
    "p.Gly1208AlafsX3",
    "Yes, new variant added",
    "3755delG",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.3623del"
  ],
  "p.Asn186LysfsX3": [
    "p.Asn186LysfsX3",
    "Yes, new variant added",
    "c.558del",
    "9.473913578960333e-06",
    "690delC",
    "CF-causing",
    "2"
  ],
  "c.558del": [
    "p.Asn186LysfsX3",
    "Yes, new variant added",
    "c.558del",
    "9.473913578960333e-06",
    "690delC",
    "CF-causing",
    "2"
  ],
  "690delC": [
    "p.Asn186LysfsX3",
    "Yes, new variant added",
    "c.558del",
    "9.473913578960333e-06",
    "690delC",
    "CF-causing",
    "2"
  ],
  "L240X": [
    "Yes, new variant added",
    "9.473913578960333e-06",
    "p.Leu240X",
    "CF-causing",
    "2",
    "L240X",
    "c.714del"
  ],
  "c.714del": [
    "Yes, new variant added",
    "9.473913578960333e-06",
    "p.Leu240X",
    "CF-causing",
    "2",
    "L240X",
    "c.714del"
  ],
  "p.Leu259AlafsX12": [
    "Yes, new variant added",
    "p.Leu259AlafsX12",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.775delinsGCTGGGAAGAT"
  ],
  "c.775delinsGCTGGGAAGAT": [
    "Yes, new variant added",
    "p.Leu259AlafsX12",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "c.775delinsGCTGGGAAGAT"
  ],
  "c.3G>A": [
    "p.?",
    "Yes, new variant added",
    "c.3G>A",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "M1I"
  ],
  "M1I": [
    "p.?",
    "Yes, new variant added",
    "c.3G>A",
    "9.473913578960333e-06",
    "CF-causing",
    "2",
    "M1I"
  ],
  "4.7369567894801664e-06": [
    "c.273+7982del18652",
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "405+7982del18652"
  ],
  "1091T>A": [
    "4.7369567894801664e-06",
    "No",
    "1091T>A",
    "CF-causing",
    "1",
    "p.Leu320X",
    "L320X",
    "c.959T>A"
  ],
  "1": [
    "c.273+7982del18652",
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "405+7982del18652"
  ],
  "p.Leu320X": [
    "4.7369567894801664e-06",
    "No",
    "1091T>A",
    "CF-causing",
    "1",
    "p.Leu320X",
    "L320X",
    "c.959T>A"
  ],
  "L320X": [
    "4.7369567894801664e-06",
    "No",
    "1091T>A",
    "CF-causing",
    "1",
    "p.Leu320X",
    "L320X",
    "c.959T>A"
  ],
  "c.959T>A": [
    "4.7369567894801664e-06",
    "No",
    "1091T>A",
    "CF-causing",
    "1",
    "p.Leu320X",
    "L320X",
    "c.959T>A"
  ],
  "1117A>T": [
    "4.7369567894801664e-06",
    "1117A>T",
    "Yes, new variant added",
    "K329X",
    "CF-causing",
    "1",
    "c.985A>T",
    "p.Lys329X"
  ],
  "K329X": [
    "4.7369567894801664e-06",
    "1117A>T",
    "Yes, new variant added",
    "K329X",
    "CF-causing",
    "1",
    "c.985A>T",
    "p.Lys329X"
  ],
  "c.985A>T": [
    "4.7369567894801664e-06",
    "1117A>T",
    "Yes, new variant added",
    "K329X",
    "CF-causing",
    "1",
    "c.985A>T",
    "p.Lys329X"
  ],
  "p.Lys329X": [
    "4.7369567894801664e-06",
    "1117A>T",
    "Yes, new variant added",
    "K329X",
    "CF-causing",
    "1",
    "c.985A>T",
    "p.Lys329X"
  ],
  "c.1126C>T": [
    "4.7369567894801664e-06",
    "c.1126C>T",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "Q376X",
    "1258C>T",
    "p.Gln376X"
  ],
  "Q376X": [
    "4.7369567894801664e-06",
    "c.1126C>T",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "Q376X",
    "1258C>T",
    "p.Gln376X"
  ],
  "1258C>T": [
    "4.7369567894801664e-06",
    "c.1126C>T",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "Q376X",
    "1258C>T",
    "p.Gln376X"
  ],
  "p.Gln376X": [
    "4.7369567894801664e-06",
    "c.1126C>T",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "Q376X",
    "1258C>T",
    "p.Gln376X"
  ],
  "1486C>T": [
    "4.7369567894801664e-06",
    "1486C>T",
    "c.1354C>T",
    "Yes, new variant added",
    "Q452X",
    "CF-causing",
    "1",
    "p.Gln452X"
  ],
  "c.1354C>T": [
    "4.7369567894801664e-06",
    "1486C>T",
    "c.1354C>T",
    "Yes, new variant added",
    "Q452X",
    "CF-causing",
    "1",
    "p.Gln452X"
  ],
  "Q452X": [
    "4.7369567894801664e-06",
    "1486C>T",
    "c.1354C>T",
    "Yes, new variant added",
    "Q452X",
    "CF-causing",
    "1",
    "p.Gln452X"
  ],
  "p.Gln452X": [
    "4.7369567894801664e-06",
    "1486C>T",
    "c.1354C>T",
    "Yes, new variant added",
    "Q452X",
    "CF-causing",
    "1",
    "p.Gln452X"
  ],
  "p.Glu479X": [
    "4.7369567894801664e-06",
    "p.Glu479X",
    "c.1435G>T",
    "Yes, new variant added",
    "1567G>T",
    "CF-causing",
    "E479X",
    "1"
  ],
  "c.1435G>T": [
    "4.7369567894801664e-06",
    "p.Glu479X",
    "c.1435G>T",
    "Yes, new variant added",
    "1567G>T",
    "CF-causing",
    "E479X",
    "1"
  ],
  "1567G>T": [
    "4.7369567894801664e-06",
    "p.Glu479X",
    "c.1435G>T",
    "Yes, new variant added",
    "1567G>T",
    "CF-causing",
    "E479X",
    "1"
  ],
  "E479X": [
    "4.7369567894801664e-06",
    "p.Glu479X",
    "c.1435G>T",
    "Yes, new variant added",
    "1567G>T",
    "CF-causing",
    "E479X",
    "1"
  ],
  "1642G>T": [
    "4.7369567894801664e-06",
    "No",
    "1642G>T",
    "p.Glu504X",
    "CF-causing",
    "c.1510G>T",
    "1",
    "E504X"
  ],
  "p.Glu504X": [
    "4.7369567894801664e-06",
    "No",
    "1642G>T",
    "p.Glu504X",
    "CF-causing",
    "c.1510G>T",
    "1",
    "E504X"
  ],
  "c.1510G>T": [
    "4.7369567894801664e-06",
    "No",
    "1642G>T",
    "p.Glu504X",
    "CF-causing",
    "c.1510G>T",
    "1",
    "E504X"
  ],
  "E504X": [
    "4.7369567894801664e-06",
    "No",
    "1642G>T",
    "p.Glu504X",
    "CF-causing",
    "c.1510G>T",
    "1",
    "E504X"
  ],
  "1683C>A|1683C>G": [
    "4.7369567894801664e-06",
    "1683C>A|1683C>G",
    "No",
    "c.1551C>A|c.1551C>G",
    "CF-causing",
    "Y517X",
    "1",
    "p.Tyr517X"
  ],
  "c.1551C>A|c.1551C>G": [
    "4.7369567894801664e-06",
    "1683C>A|1683C>G",
    "No",
    "c.1551C>A|c.1551C>G",
    "CF-causing",
    "Y517X",
    "1",
    "p.Tyr517X"
  ],
  "Y517X": [
    "4.7369567894801664e-06",
    "1683C>A|1683C>G",
    "No",
    "c.1551C>A|c.1551C>G",
    "CF-causing",
    "Y517X",
    "1",
    "p.Tyr517X"
  ],
  "p.Tyr517X": [
    "4.7369567894801664e-06",
    "1683C>A|1683C>G",
    "No",
    "c.1551C>A|c.1551C>G",
    "CF-causing",
    "Y517X",
    "1",
    "p.Tyr517X"
  ],
  "p.Glu527X": [
    "4.7369567894801664e-06",
    "p.Glu527X",
    "Yes, new variant added",
    "E527X",
    "1711G>T",
    "CF-causing",
    "1",
    "c.1579G>T"
  ],
  "E527X": [
    "4.7369567894801664e-06",
    "p.Glu527X",
    "Yes, new variant added",
    "E527X",
    "1711G>T",
    "CF-causing",
    "1",
    "c.1579G>T"
  ],
  "1711G>T": [
    "4.7369567894801664e-06",
    "p.Glu527X",
    "Yes, new variant added",
    "E527X",
    "1711G>T",
    "CF-causing",
    "1",
    "c.1579G>T"
  ],
  "c.1579G>T": [
    "4.7369567894801664e-06",
    "p.Glu527X",
    "Yes, new variant added",
    "E527X",
    "1711G>T",
    "CF-causing",
    "1",
    "c.1579G>T"
  ],
  "K14X": [
    "4.7369567894801664e-06",
    "K14X",
    "Yes, new variant added",
    "c.40A>T",
    "CF-causing",
    "172A>T",
    "1",
    "p.Lys14X"
  ],
  "c.40A>T": [
    "4.7369567894801664e-06",
    "K14X",
    "Yes, new variant added",
    "c.40A>T",
    "CF-causing",
    "172A>T",
    "1",
    "p.Lys14X"
  ],
  "172A>T": [
    "4.7369567894801664e-06",
    "K14X",
    "Yes, new variant added",
    "c.40A>T",
    "CF-causing",
    "172A>T",
    "1",
    "p.Lys14X"
  ],
  "p.Lys14X": [
    "4.7369567894801664e-06",
    "K14X",
    "Yes, new variant added",
    "c.40A>T",
    "CF-causing",
    "172A>T",
    "1",
    "p.Lys14X"
  ],
  "c.1606A>T": [
    "4.7369567894801664e-06",
    "c.1606A>T",
    "Yes, new variant added",
    "1738A>T",
    "K536X",
    "CF-causing",
    "1",
    "p.Lys536X"
  ],
  "1738A>T": [
    "4.7369567894801664e-06",
    "c.1606A>T",
    "Yes, new variant added",
    "1738A>T",
    "K536X",
    "CF-causing",
    "1",
    "p.Lys536X"
  ],
  "K536X": [
    "4.7369567894801664e-06",
    "c.1606A>T",
    "Yes, new variant added",
    "1738A>T",
    "K536X",
    "CF-causing",
    "1",
    "p.Lys536X"
  ],
  "p.Lys536X": [
    "4.7369567894801664e-06",
    "c.1606A>T",
    "Yes, new variant added",
    "1738A>T",
    "K536X",
    "CF-causing",
    "1",
    "p.Lys536X"
  ],
  "R555X": [
    "4.7369567894801664e-06",
    "R555X",
    "p.Arg555X",
    "Yes, new variant added",
    "CF-causing",
    "c.1663A>T",
    "1",
    "1795A>T"
  ],
  "p.Arg555X": [
    "4.7369567894801664e-06",
    "R555X",
    "p.Arg555X",
    "Yes, new variant added",
    "CF-causing",
    "c.1663A>T",
    "1",
    "1795A>T"
  ],
  "c.1663A>T": [
    "4.7369567894801664e-06",
    "R555X",
    "p.Arg555X",
    "Yes, new variant added",
    "CF-causing",
    "c.1663A>T",
    "1",
    "1795A>T"
  ],
  "1795A>T": [
    "4.7369567894801664e-06",
    "R555X",
    "p.Arg555X",
    "Yes, new variant added",
    "CF-causing",
    "c.1663A>T",
    "1",
    "1795A>T"
  ],
  "L570X": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "L570X",
    "p.Leu570X",
    "CF-causing",
    "1",
    "c.1709T>A",
    "1841T>A"
  ],
  "p.Leu570X": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "L570X",
    "p.Leu570X",
    "CF-causing",
    "1",
    "c.1709T>A",
    "1841T>A"
  ],
  "c.1709T>A": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "L570X",
    "p.Leu570X",
    "CF-causing",
    "1",
    "c.1709T>A",
    "1841T>A"
  ],
  "1841T>A": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "L570X",
    "p.Leu570X",
    "CF-causing",
    "1",
    "c.1709T>A",
    "1841T>A"
  ],
  "L581X": [
    "4.7369567894801664e-06",
    "L581X",
    "Yes, new variant added",
    "CF-causing",
    "p.Leu581X",
    "1",
    "c.1742T>A",
    "1874T>A"
  ],
  "p.Leu581X": [
    "4.7369567894801664e-06",
    "L581X",
    "Yes, new variant added",
    "CF-causing",
    "p.Leu581X",
    "1",
    "c.1742T>A",
    "1874T>A"
  ],
  "c.1742T>A": [
    "4.7369567894801664e-06",
    "L581X",
    "Yes, new variant added",
    "CF-causing",
    "p.Leu581X",
    "1",
    "c.1742T>A",
    "1874T>A"
  ],
  "1874T>A": [
    "4.7369567894801664e-06",
    "L581X",
    "Yes, new variant added",
    "CF-causing",
    "p.Leu581X",
    "1",
    "c.1742T>A",
    "1874T>A"
  ],
  "p.Ser631X": [
    "4.7369567894801664e-06",
    "p.Ser631X",
    "Yes, new variant added",
    "c.1892C>G",
    "CF-causing",
    "2024C>G",
    "1",
    "S631X"
  ],
  "c.1892C>G": [
    "4.7369567894801664e-06",
    "p.Ser631X",
    "Yes, new variant added",
    "c.1892C>G",
    "CF-causing",
    "2024C>G",
    "1",
    "S631X"
  ],
  "2024C>G": [
    "4.7369567894801664e-06",
    "p.Ser631X",
    "Yes, new variant added",
    "c.1892C>G",
    "CF-causing",
    "2024C>G",
    "1",
    "S631X"
  ],
  "S631X": [
    "4.7369567894801664e-06",
    "p.Ser631X",
    "Yes, new variant added",
    "c.1892C>G",
    "CF-causing",
    "2024C>G",
    "1",
    "S631X"
  ],
  "2032C>T": [
    "4.7369567894801664e-06",
    "No",
    "2032C>T",
    "c.1900C>T",
    "CF-causing",
    "1",
    "Q634X",
    "p.Gln634X"
  ],
  "c.1900C>T": [
    "4.7369567894801664e-06",
    "No",
    "2032C>T",
    "c.1900C>T",
    "CF-causing",
    "1",
    "Q634X",
    "p.Gln634X"
  ],
  "Q634X": [
    "4.7369567894801664e-06",
    "No",
    "2032C>T",
    "c.1900C>T",
    "CF-causing",
    "1",
    "Q634X",
    "p.Gln634X"
  ],
  "p.Gln634X": [
    "4.7369567894801664e-06",
    "No",
    "2032C>T",
    "c.1900C>T",
    "CF-causing",
    "1",
    "Q634X",
    "p.Gln634X"
  ],
  "c.1969A>T": [
    "4.7369567894801664e-06",
    "c.1969A>T",
    "Yes, new variant added",
    "2101A>T",
    "R657X",
    "CF-causing",
    "p.Arg657X",
    "1"
  ],
  "2101A>T": [
    "4.7369567894801664e-06",
    "c.1969A>T",
    "Yes, new variant added",
    "2101A>T",
    "R657X",
    "CF-causing",
    "p.Arg657X",
    "1"
  ],
  "R657X": [
    "4.7369567894801664e-06",
    "c.1969A>T",
    "Yes, new variant added",
    "2101A>T",
    "R657X",
    "CF-causing",
    "p.Arg657X",
    "1"
  ],
  "p.Arg657X": [
    "4.7369567894801664e-06",
    "c.1969A>T",
    "Yes, new variant added",
    "2101A>T",
    "R657X",
    "CF-causing",
    "p.Arg657X",
    "1"
  ],
  "E692X": [
    "4.7369567894801664e-06",
    "E692X",
    "No",
    "2206G>T",
    "c.2074G>T",
    "CF-causing",
    "1",
    "p.Glu692X"
  ],
  "2206G>T": [
    "4.7369567894801664e-06",
    "E692X",
    "No",
    "2206G>T",
    "c.2074G>T",
    "CF-causing",
    "1",
    "p.Glu692X"
  ],
  "c.2074G>T": [
    "4.7369567894801664e-06",
    "E692X",
    "No",
    "2206G>T",
    "c.2074G>T",
    "CF-causing",
    "1",
    "p.Glu692X"
  ],
  "p.Glu692X": [
    "4.7369567894801664e-06",
    "E692X",
    "No",
    "2206G>T",
    "c.2074G>T",
    "CF-causing",
    "1",
    "p.Glu692X"
  ],
  "246C>G": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "246C>G",
    "CF-causing",
    "c.114C>G",
    "1",
    "p.Tyr38X",
    "Y38X"
  ],
  "c.114C>G": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "246C>G",
    "CF-causing",
    "c.114C>G",
    "1",
    "p.Tyr38X",
    "Y38X"
  ],
  "p.Tyr38X": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "246C>G",
    "CF-causing",
    "c.114C>G",
    "1",
    "p.Tyr38X",
    "Y38X"
  ],
  "Y38X": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "246C>G",
    "CF-causing",
    "c.114C>G",
    "1",
    "p.Tyr38X",
    "Y38X"
  ],
  "2527C>T": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "2527C>T",
    "1",
    "p.Gln799X",
    "Q799X",
    "c.2395C>T"
  ],
  "p.Gln799X": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "2527C>T",
    "1",
    "p.Gln799X",
    "Q799X",
    "c.2395C>T"
  ],
  "Q799X": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "2527C>T",
    "1",
    "p.Gln799X",
    "Q799X",
    "c.2395C>T"
  ],
  "c.2395C>T": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "2527C>T",
    "1",
    "p.Gln799X",
    "Q799X",
    "c.2395C>T"
  ],
  "2567T>A": [
    "4.7369567894801664e-06",
    "2567T>A",
    "L812X",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.2435T>A",
    "p.Leu812X"
  ],
  "L812X": [
    "4.7369567894801664e-06",
    "2567T>A",
    "L812X",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.2435T>A",
    "p.Leu812X"
  ],
  "c.2435T>A": [
    "4.7369567894801664e-06",
    "2567T>A",
    "L812X",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.2435T>A",
    "p.Leu812X"
  ],
  "p.Leu812X": [
    "4.7369567894801664e-06",
    "2567T>A",
    "L812X",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.2435T>A",
    "p.Leu812X"
  ],
  "p.Lys52X": [
    "4.7369567894801664e-06",
    "No",
    "p.Lys52X",
    "286A>T",
    "CF-causing",
    "c.154A>T",
    "1",
    "K52X"
  ],
  "286A>T": [
    "4.7369567894801664e-06",
    "No",
    "p.Lys52X",
    "286A>T",
    "CF-causing",
    "c.154A>T",
    "1",
    "K52X"
  ],
  "c.154A>T": [
    "4.7369567894801664e-06",
    "No",
    "p.Lys52X",
    "286A>T",
    "CF-causing",
    "c.154A>T",
    "1",
    "K52X"
  ],
  "K52X": [
    "4.7369567894801664e-06",
    "No",
    "p.Lys52X",
    "286A>T",
    "CF-causing",
    "c.154A>T",
    "1",
    "K52X"
  ],
  "p.Glu54X": [
    "4.7369567894801664e-06",
    "p.Glu54X",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "292G>T",
    "c.160G>T",
    "E54X"
  ],
  "292G>T": [
    "4.7369567894801664e-06",
    "p.Glu54X",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "292G>T",
    "c.160G>T",
    "E54X"
  ],
  "c.160G>T": [
    "4.7369567894801664e-06",
    "p.Glu54X",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "292G>T",
    "c.160G>T",
    "E54X"
  ],
  "E54X": [
    "4.7369567894801664e-06",
    "p.Glu54X",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "292G>T",
    "c.160G>T",
    "E54X"
  ],
  "p.Lys946X": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "p.Lys946X",
    "1",
    "K946X",
    "c.2836A>T",
    "2968A>T"
  ],
  "K946X": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "p.Lys946X",
    "1",
    "K946X",
    "c.2836A>T",
    "2968A>T"
  ],
  "c.2836A>T": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "p.Lys946X",
    "1",
    "K946X",
    "c.2836A>T",
    "2968A>T"
  ],
  "2968A>T": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "p.Lys946X",
    "1",
    "K946X",
    "c.2836A>T",
    "2968A>T"
  ],
  "p.Lys951X": [
    "p.Lys951X",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.2851A>T",
    "CF-causing",
    "1",
    "K951X",
    "2983A>T"
  ],
  "c.2851A>T": [
    "p.Lys951X",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.2851A>T",
    "CF-causing",
    "1",
    "K951X",
    "2983A>T"
  ],
  "K951X": [
    "p.Lys951X",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.2851A>T",
    "CF-causing",
    "1",
    "K951X",
    "2983A>T"
  ],
  "2983A>T": [
    "p.Lys951X",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.2851A>T",
    "CF-causing",
    "1",
    "K951X",
    "2983A>T"
  ],
  "3118C>T": [
    "3118C>T",
    "p.Gln996X",
    "4.7369567894801664e-06",
    "No",
    "c.2986C>T",
    "Q996X",
    "CF-causing",
    "1"
  ],
  "p.Gln996X": [
    "3118C>T",
    "p.Gln996X",
    "4.7369567894801664e-06",
    "No",
    "c.2986C>T",
    "Q996X",
    "CF-causing",
    "1"
  ],
  "c.2986C>T": [
    "3118C>T",
    "p.Gln996X",
    "4.7369567894801664e-06",
    "No",
    "c.2986C>T",
    "Q996X",
    "CF-causing",
    "1"
  ],
  "Q996X": [
    "3118C>T",
    "p.Gln996X",
    "4.7369567894801664e-06",
    "No",
    "c.2986C>T",
    "Q996X",
    "CF-causing",
    "1"
  ],
  "p.Gln1012X": [
    "4.7369567894801664e-06",
    "p.Gln1012X",
    "Yes, new variant added",
    "CF-causing",
    "3166C>T",
    "1",
    "c.3034C>T",
    "Q1012X"
  ],
  "3166C>T": [
    "4.7369567894801664e-06",
    "p.Gln1012X",
    "Yes, new variant added",
    "CF-causing",
    "3166C>T",
    "1",
    "c.3034C>T",
    "Q1012X"
  ],
  "c.3034C>T": [
    "4.7369567894801664e-06",
    "p.Gln1012X",
    "Yes, new variant added",
    "CF-causing",
    "3166C>T",
    "1",
    "c.3034C>T",
    "Q1012X"
  ],
  "Q1012X": [
    "4.7369567894801664e-06",
    "p.Gln1012X",
    "Yes, new variant added",
    "CF-causing",
    "3166C>T",
    "1",
    "c.3034C>T",
    "Q1012X"
  ],
  "c.3110C>A": [
    "4.7369567894801664e-06",
    "c.3110C>A",
    "Yes, new variant added",
    "3242C>A",
    "CF-causing",
    "S1037X",
    "1",
    "p.Ser1037X"
  ],
  "3242C>A": [
    "4.7369567894801664e-06",
    "c.3110C>A",
    "Yes, new variant added",
    "3242C>A",
    "CF-causing",
    "S1037X",
    "1",
    "p.Ser1037X"
  ],
  "S1037X": [
    "4.7369567894801664e-06",
    "c.3110C>A",
    "Yes, new variant added",
    "3242C>A",
    "CF-causing",
    "S1037X",
    "1",
    "p.Ser1037X"
  ],
  "p.Ser1037X": [
    "4.7369567894801664e-06",
    "c.3110C>A",
    "Yes, new variant added",
    "3242C>A",
    "CF-causing",
    "S1037X",
    "1",
    "p.Ser1037X"
  ],
  "Q1038X": [
    "4.7369567894801664e-06",
    "Q1038X",
    "Yes, new variant added",
    "c.3112C>T",
    "CF-causing",
    "3244C>T",
    "p.Gln1038X",
    "1"
  ],
  "c.3112C>T": [
    "4.7369567894801664e-06",
    "Q1038X",
    "Yes, new variant added",
    "c.3112C>T",
    "CF-causing",
    "3244C>T",
    "p.Gln1038X",
    "1"
  ],
  "3244C>T": [
    "4.7369567894801664e-06",
    "Q1038X",
    "Yes, new variant added",
    "c.3112C>T",
    "CF-causing",
    "3244C>T",
    "p.Gln1038X",
    "1"
  ],
  "p.Gln1038X": [
    "4.7369567894801664e-06",
    "Q1038X",
    "Yes, new variant added",
    "c.3112C>T",
    "CF-causing",
    "3244C>T",
    "p.Gln1038X",
    "1"
  ],
  "E1044X": [
    "4.7369567894801664e-06",
    "E1044X",
    "Yes, new variant added",
    "CF-causing",
    "3262G>T",
    "c.3130G>T",
    "1",
    "p.Glu1044X"
  ],
  "3262G>T": [
    "4.7369567894801664e-06",
    "E1044X",
    "Yes, new variant added",
    "CF-causing",
    "3262G>T",
    "c.3130G>T",
    "1",
    "p.Glu1044X"
  ],
  "c.3130G>T": [
    "4.7369567894801664e-06",
    "E1044X",
    "Yes, new variant added",
    "CF-causing",
    "3262G>T",
    "c.3130G>T",
    "1",
    "p.Glu1044X"
  ],
  "p.Glu1044X": [
    "4.7369567894801664e-06",
    "E1044X",
    "Yes, new variant added",
    "CF-causing",
    "3262G>T",
    "c.3130G>T",
    "1",
    "p.Glu1044X"
  ],
  "E1046X": [
    "4.7369567894801664e-06",
    "E1046X",
    "No",
    "c.3136G>T",
    "CF-causing",
    "1",
    "3268G>T",
    "p.Glu1046X"
  ],
  "c.3136G>T": [
    "4.7369567894801664e-06",
    "E1046X",
    "No",
    "c.3136G>T",
    "CF-causing",
    "1",
    "3268G>T",
    "p.Glu1046X"
  ],
  "3268G>T": [
    "4.7369567894801664e-06",
    "E1046X",
    "No",
    "c.3136G>T",
    "CF-causing",
    "1",
    "3268G>T",
    "p.Glu1046X"
  ],
  "p.Glu1046X": [
    "4.7369567894801664e-06",
    "E1046X",
    "No",
    "c.3136G>T",
    "CF-causing",
    "1",
    "3268G>T",
    "p.Glu1046X"
  ],
  "p.Leu1059X": [
    "4.7369567894801664e-06",
    "No",
    "p.Leu1059X",
    "3308T>G",
    "c.3176T>G",
    "CF-causing",
    "1",
    "L1059X"
  ],
  "3308T>G": [
    "4.7369567894801664e-06",
    "No",
    "p.Leu1059X",
    "3308T>G",
    "c.3176T>G",
    "CF-causing",
    "1",
    "L1059X"
  ],
  "c.3176T>G": [
    "4.7369567894801664e-06",
    "No",
    "p.Leu1059X",
    "3308T>G",
    "c.3176T>G",
    "CF-causing",
    "1",
    "L1059X"
  ],
  "L1059X": [
    "4.7369567894801664e-06",
    "No",
    "p.Leu1059X",
    "3308T>G",
    "c.3176T>G",
    "CF-causing",
    "1",
    "L1059X"
  ],
  "3430C>T": [
    "4.7369567894801664e-06",
    "3430C>T",
    "Yes, new variant added",
    "Q1100X",
    "CF-causing",
    "c.3298C>T",
    "1",
    "p.Gln1100X"
  ],
  "Q1100X": [
    "4.7369567894801664e-06",
    "3430C>T",
    "Yes, new variant added",
    "Q1100X",
    "CF-causing",
    "c.3298C>T",
    "1",
    "p.Gln1100X"
  ],
  "c.3298C>T": [
    "4.7369567894801664e-06",
    "3430C>T",
    "Yes, new variant added",
    "Q1100X",
    "CF-causing",
    "c.3298C>T",
    "1",
    "p.Gln1100X"
  ],
  "p.Gln1100X": [
    "4.7369567894801664e-06",
    "3430C>T",
    "Yes, new variant added",
    "Q1100X",
    "CF-causing",
    "c.3298C>T",
    "1",
    "p.Gln1100X"
  ],
  "c.3493A>T": [
    "p.Lys1165X",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "c.3493A>T",
    "K1165X",
    "1",
    "3625A>T"
  ],
  "K1165X": [
    "p.Lys1165X",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "c.3493A>T",
    "K1165X",
    "1",
    "3625A>T"
  ],
  "3625A>T": [
    "p.Lys1165X",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "c.3493A>T",
    "K1165X",
    "1",
    "3625A>T"
  ],
  "c.3533C>A|c.3533C>G": [
    "4.7369567894801664e-06",
    "No",
    "c.3533C>A|c.3533C>G",
    "CF-causing",
    "3665C>A|3665C>G",
    "1",
    "p.Ser1178X",
    "S1178X"
  ],
  "3665C>A|3665C>G": [
    "4.7369567894801664e-06",
    "No",
    "c.3533C>A|c.3533C>G",
    "CF-causing",
    "3665C>A|3665C>G",
    "1",
    "p.Ser1178X",
    "S1178X"
  ],
  "p.Ser1178X": [
    "4.7369567894801664e-06",
    "No",
    "c.3533C>A|c.3533C>G",
    "CF-causing",
    "3665C>A|3665C>G",
    "1",
    "p.Ser1178X",
    "S1178X"
  ],
  "S1178X": [
    "4.7369567894801664e-06",
    "No",
    "c.3533C>A|c.3533C>G",
    "CF-causing",
    "3665C>A|3665C>G",
    "1",
    "p.Ser1178X",
    "S1178X"
  ],
  "Q1186X": [
    "4.7369567894801664e-06",
    "Q1186X",
    "No",
    "CF-causing",
    "p.Gln1186X",
    "c.3556C>T",
    "1",
    "3688C>T"
  ],
  "p.Gln1186X": [
    "4.7369567894801664e-06",
    "Q1186X",
    "No",
    "CF-causing",
    "p.Gln1186X",
    "c.3556C>T",
    "1",
    "3688C>T"
  ],
  "c.3556C>T": [
    "4.7369567894801664e-06",
    "Q1186X",
    "No",
    "CF-causing",
    "p.Gln1186X",
    "c.3556C>T",
    "1",
    "3688C>T"
  ],
  "3688C>T": [
    "4.7369567894801664e-06",
    "Q1186X",
    "No",
    "CF-causing",
    "p.Gln1186X",
    "c.3556C>T",
    "1",
    "3688C>T"
  ],
  "p.Leu1243X": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "p.Leu1243X",
    "L1243X",
    "3860T>A",
    "1",
    "c.3728T>A"
  ],
  "L1243X": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "p.Leu1243X",
    "L1243X",
    "3860T>A",
    "1",
    "c.3728T>A"
  ],
  "3860T>A": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "p.Leu1243X",
    "L1243X",
    "3860T>A",
    "1",
    "c.3728T>A"
  ],
  "c.3728T>A": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "p.Leu1243X",
    "L1243X",
    "3860T>A",
    "1",
    "c.3728T>A"
  ],
  "c.3773T>A": [
    "4.7369567894801664e-06",
    "c.3773T>A",
    "Yes, new variant added",
    "3905T>A",
    "CF-causing",
    "1",
    "p.Leu1253X",
    "L1253X"
  ],
  "3905T>A": [
    "4.7369567894801664e-06",
    "c.3773T>A",
    "Yes, new variant added",
    "3905T>A",
    "CF-causing",
    "1",
    "p.Leu1253X",
    "L1253X"
  ],
  "p.Leu1253X": [
    "4.7369567894801664e-06",
    "c.3773T>A",
    "Yes, new variant added",
    "3905T>A",
    "CF-causing",
    "1",
    "p.Leu1253X",
    "L1253X"
  ],
  "L1253X": [
    "4.7369567894801664e-06",
    "c.3773T>A",
    "Yes, new variant added",
    "3905T>A",
    "CF-causing",
    "1",
    "p.Leu1253X",
    "L1253X"
  ],
  "K1351X": [
    "K1351X",
    "4.7369567894801664e-06",
    "p.Lys1351X",
    "No",
    "CF-causing",
    "4183A>T",
    "1",
    "c.4051A>T"
  ],
  "p.Lys1351X": [
    "K1351X",
    "4.7369567894801664e-06",
    "p.Lys1351X",
    "No",
    "CF-causing",
    "4183A>T",
    "1",
    "c.4051A>T"
  ],
  "4183A>T": [
    "K1351X",
    "4.7369567894801664e-06",
    "p.Lys1351X",
    "No",
    "CF-causing",
    "4183A>T",
    "1",
    "c.4051A>T"
  ],
  "c.4051A>T": [
    "K1351X",
    "4.7369567894801664e-06",
    "p.Lys1351X",
    "No",
    "CF-causing",
    "4183A>T",
    "1",
    "c.4051A>T"
  ],
  "4332T>A": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "4332T>A",
    "CF-causing",
    "c.4200T>A",
    "p.Cys1400X",
    "1",
    "C1400X"
  ],
  "c.4200T>A": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "4332T>A",
    "CF-causing",
    "c.4200T>A",
    "p.Cys1400X",
    "1",
    "C1400X"
  ],
  "C1400X": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "4332T>A",
    "CF-causing",
    "c.4200T>A",
    "p.Cys1400X",
    "1",
    "C1400X"
  ],
  "c.4225G>T": [
    "4.7369567894801664e-06",
    "c.4225G>T",
    "4357G>T",
    "Yes, new variant added",
    "p.Glu1409X",
    "CF-causing",
    "E1409X",
    "1"
  ],
  "4357G>T": [
    "4.7369567894801664e-06",
    "c.4225G>T",
    "4357G>T",
    "Yes, new variant added",
    "p.Glu1409X",
    "CF-causing",
    "E1409X",
    "1"
  ],
  "p.Glu1409X": [
    "4.7369567894801664e-06",
    "c.4225G>T",
    "4357G>T",
    "Yes, new variant added",
    "p.Glu1409X",
    "CF-causing",
    "E1409X",
    "1"
  ],
  "E1409X": [
    "4.7369567894801664e-06",
    "c.4225G>T",
    "4357G>T",
    "Yes, new variant added",
    "p.Glu1409X",
    "CF-causing",
    "E1409X",
    "1"
  ],
  "c.4230C>A": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.4230C>A",
    "CF-causing",
    "4362C>A",
    "1",
    "p.Cys1410X",
    "C1410X"
  ],
  "4362C>A": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.4230C>A",
    "CF-causing",
    "4362C>A",
    "1",
    "p.Cys1410X",
    "C1410X"
  ],
  "p.Cys1410X": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.4230C>A",
    "CF-causing",
    "4362C>A",
    "1",
    "p.Cys1410X",
    "C1410X"
  ],
  "C1410X": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.4230C>A",
    "CF-causing",
    "4362C>A",
    "1",
    "p.Cys1410X",
    "C1410X"
  ],
  "c.310A>T": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.310A>T",
    "p.Arg104X",
    "CF-causing",
    "442A>T",
    "1",
    "R104X"
  ],
  "p.Arg104X": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.310A>T",
    "p.Arg104X",
    "CF-causing",
    "442A>T",
    "1",
    "R104X"
  ],
  "442A>T": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.310A>T",
    "p.Arg104X",
    "CF-causing",
    "442A>T",
    "1",
    "R104X"
  ],
  "R104X": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.310A>T",
    "p.Arg104X",
    "CF-causing",
    "442A>T",
    "1",
    "R104X"
  ],
  "472A>T": [
    "4.7369567894801664e-06",
    "No",
    "472A>T",
    "c.340A>T",
    "CF-causing",
    "p.Lys114X",
    "1",
    "K114X"
  ],
  "c.340A>T": [
    "4.7369567894801664e-06",
    "No",
    "472A>T",
    "c.340A>T",
    "CF-causing",
    "p.Lys114X",
    "1",
    "K114X"
  ],
  "p.Lys114X": [
    "4.7369567894801664e-06",
    "No",
    "472A>T",
    "c.340A>T",
    "CF-causing",
    "p.Lys114X",
    "1",
    "K114X"
  ],
  "K114X": [
    "4.7369567894801664e-06",
    "No",
    "472A>T",
    "c.340A>T",
    "CF-causing",
    "p.Lys114X",
    "1",
    "K114X"
  ],
  "c.476T>A": [
    "4.7369567894801664e-06",
    "No",
    "c.476T>A",
    "CF-causing",
    "L159X",
    "1",
    "608T>A",
    "p.Leu159X"
  ],
  "L159X": [
    "4.7369567894801664e-06",
    "No",
    "c.476T>A",
    "CF-causing",
    "L159X",
    "1",
    "608T>A",
    "p.Leu159X"
  ],
  "608T>A": [
    "4.7369567894801664e-06",
    "No",
    "c.476T>A",
    "CF-causing",
    "L159X",
    "1",
    "608T>A",
    "p.Leu159X"
  ],
  "p.Leu159X": [
    "4.7369567894801664e-06",
    "No",
    "c.476T>A",
    "CF-causing",
    "L159X",
    "1",
    "608T>A",
    "p.Leu159X"
  ],
  "c.494T>A": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.494T>A",
    "p.Leu165X",
    "CF-causing",
    "626T>A",
    "1",
    "L165X"
  ],
  "626T>A": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.494T>A",
    "p.Leu165X",
    "CF-causing",
    "626T>A",
    "1",
    "L165X"
  ],
  "L165X": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.494T>A",
    "p.Leu165X",
    "CF-causing",
    "626T>A",
    "1",
    "L165X"
  ],
  "Q237X": [
    "4.7369567894801664e-06",
    "Q237X",
    "Yes, new variant added",
    "841C>T",
    "c.709C>T",
    "CF-causing",
    "1",
    "p.Gln237X"
  ],
  "841C>T": [
    "4.7369567894801664e-06",
    "Q237X",
    "Yes, new variant added",
    "841C>T",
    "c.709C>T",
    "CF-causing",
    "1",
    "p.Gln237X"
  ],
  "c.709C>T": [
    "4.7369567894801664e-06",
    "Q237X",
    "Yes, new variant added",
    "841C>T",
    "c.709C>T",
    "CF-causing",
    "1",
    "p.Gln237X"
  ],
  "p.Gln237X": [
    "4.7369567894801664e-06",
    "Q237X",
    "Yes, new variant added",
    "841C>T",
    "c.709C>T",
    "CF-causing",
    "1",
    "p.Gln237X"
  ],
  "p.Tyr247X": [
    "p.Tyr247X",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "873C>G|873C>A",
    "CF-causing",
    "1",
    "c.741C>G|c.741C>A",
    "Y247X"
  ],
  "873C>G|873C>A": [
    "p.Tyr247X",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "873C>G|873C>A",
    "CF-causing",
    "1",
    "c.741C>G|c.741C>A",
    "Y247X"
  ],
  "c.741C>G|c.741C>A": [
    "p.Tyr247X",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "873C>G|873C>A",
    "CF-causing",
    "1",
    "c.741C>G|c.741C>A",
    "Y247X"
  ],
  "Y247X": [
    "p.Tyr247X",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "873C>G|873C>A",
    "CF-causing",
    "1",
    "c.741C>G|c.741C>A",
    "Y247X"
  ],
  "Q250X": [
    "4.7369567894801664e-06",
    "No",
    "Q250X",
    "880C>T",
    "p.Gln250X",
    "CF-causing",
    "1",
    "c.748C>T"
  ],
  "880C>T": [
    "4.7369567894801664e-06",
    "No",
    "Q250X",
    "880C>T",
    "p.Gln250X",
    "CF-causing",
    "1",
    "c.748C>T"
  ],
  "p.Gln250X": [
    "4.7369567894801664e-06",
    "No",
    "Q250X",
    "880C>T",
    "p.Gln250X",
    "CF-causing",
    "1",
    "c.748C>T"
  ],
  "c.748C>T": [
    "4.7369567894801664e-06",
    "No",
    "Q250X",
    "880C>T",
    "p.Gln250X",
    "CF-causing",
    "1",
    "c.748C>T"
  ],
  "p.Gln270X": [
    "4.7369567894801664e-06",
    "p.Gln270X",
    "Yes, new variant added",
    "c.808C>T",
    "CF-causing",
    "940C>T",
    "1",
    "Q270X"
  ],
  "c.808C>T": [
    "4.7369567894801664e-06",
    "p.Gln270X",
    "Yes, new variant added",
    "c.808C>T",
    "CF-causing",
    "940C>T",
    "1",
    "Q270X"
  ],
  "940C>T": [
    "4.7369567894801664e-06",
    "p.Gln270X",
    "Yes, new variant added",
    "c.808C>T",
    "CF-causing",
    "940C>T",
    "1",
    "Q270X"
  ],
  "Q270X": [
    "4.7369567894801664e-06",
    "p.Gln270X",
    "Yes, new variant added",
    "c.808C>T",
    "CF-causing",
    "940C>T",
    "1",
    "Q270X"
  ],
  "967G>T": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "967G>T",
    "p.Glu279X",
    "CF-causing",
    "E279X",
    "c.835G>T",
    "1"
  ],
  "p.Glu279X": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "967G>T",
    "p.Glu279X",
    "CF-causing",
    "E279X",
    "c.835G>T",
    "1"
  ],
  "E279X": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "967G>T",
    "p.Glu279X",
    "CF-causing",
    "E279X",
    "c.835G>T",
    "1"
  ],
  "c.835G>T": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "967G>T",
    "p.Glu279X",
    "CF-causing",
    "E279X",
    "c.835G>T",
    "1"
  ],
  "p.Arg289X": [
    "4.7369567894801664e-06",
    "No",
    "p.Arg289X",
    "CF-causing",
    "R289X",
    "1",
    "c.865A>T",
    "997A>T"
  ],
  "R289X": [
    "4.7369567894801664e-06",
    "No",
    "p.Arg289X",
    "CF-causing",
    "R289X",
    "1",
    "c.865A>T",
    "997A>T"
  ],
  "c.865A>T": [
    "4.7369567894801664e-06",
    "No",
    "p.Arg289X",
    "CF-causing",
    "R289X",
    "1",
    "c.865A>T",
    "997A>T"
  ],
  "997A>T": [
    "4.7369567894801664e-06",
    "No",
    "p.Arg289X",
    "CF-causing",
    "R289X",
    "1",
    "c.865A>T",
    "997A>T"
  ],
  "CFTRdele13": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CFTRdele13",
    "CF-causing",
    "1",
    "deletion of exon 13 (legacy numbering)|deletion of exon 14 (current numbering)",
    "c.(1766+1_1767-1)_(2490+1_2491-1)del"
  ],
  "deletion of exon 13 (legacy numbering)|deletion of exon 14 (current numbering)": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CFTRdele13",
    "CF-causing",
    "1",
    "deletion of exon 13 (legacy numbering)|deletion of exon 14 (current numbering)",
    "c.(1766+1_1767-1)_(2490+1_2491-1)del"
  ],
  "c.(1766+1_1767-1)_(2490+1_2491-1)del": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CFTRdele13",
    "CF-causing",
    "1",
    "deletion of exon 13 (legacy numbering)|deletion of exon 14 (current numbering)",
    "c.(1766+1_1767-1)_(2490+1_2491-1)del"
  ],
  "CFTRdele14b": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CFTRdele14b",
    "deletion of exon 14b (legacy numbering)|deletion of exon 16 (current numbering)",
    "CF-causing",
    "c.(2619+1_2620-1)_(2657+1_2658-1)del",
    "1"
  ],
  "deletion of exon 14b (legacy numbering)|deletion of exon 16 (current numbering)": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CFTRdele14b",
    "deletion of exon 14b (legacy numbering)|deletion of exon 16 (current numbering)",
    "CF-causing",
    "c.(2619+1_2620-1)_(2657+1_2658-1)del",
    "1"
  ],
  "c.(2619+1_2620-1)_(2657+1_2658-1)del": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CFTRdele14b",
    "deletion of exon 14b (legacy numbering)|deletion of exon 16 (current numbering)",
    "CF-causing",
    "c.(2619+1_2620-1)_(2657+1_2658-1)del",
    "1"
  ],
  "deletion of exon 23 (legacy numbering)|deletion of exon 26 (current numbering)": [
    "deletion of exon 23 (legacy numbering)|deletion of exon 26 (current numbering)",
    "4.7369567894801664e-06",
    "p.?",
    "c.(4136+1_4137-1)_(4242+1_4243-1)del",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "CFTRdele23"
  ],
  "c.(4136+1_4137-1)_(4242+1_4243-1)del": [
    "deletion of exon 23 (legacy numbering)|deletion of exon 26 (current numbering)",
    "4.7369567894801664e-06",
    "p.?",
    "c.(4136+1_4137-1)_(4242+1_4243-1)del",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "CFTRdele23"
  ],
  "CFTRdele23": [
    "deletion of exon 23 (legacy numbering)|deletion of exon 26 (current numbering)",
    "4.7369567894801664e-06",
    "p.?",
    "c.(4136+1_4137-1)_(4242+1_4243-1)del",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "CFTRdele23"
  ],
  "deletion of exon 6b (legacy numbering)|deletion of exon 7 (current numbering)": [
    "4.7369567894801664e-06",
    "p.?",
    "deletion of exon 6b (legacy numbering)|deletion of exon 7 (current numbering)",
    "Yes, new variant added",
    "CF-causing",
    "c.(743+1_744-1)_(869+1_870-1)del",
    "1",
    "CFTRdele6b"
  ],
  "c.(743+1_744-1)_(869+1_870-1)del": [
    "4.7369567894801664e-06",
    "p.?",
    "deletion of exon 6b (legacy numbering)|deletion of exon 7 (current numbering)",
    "Yes, new variant added",
    "CF-causing",
    "c.(743+1_744-1)_(869+1_870-1)del",
    "1",
    "CFTRdele6b"
  ],
  "CFTRdele6b": [
    "4.7369567894801664e-06",
    "p.?",
    "deletion of exon 6b (legacy numbering)|deletion of exon 7 (current numbering)",
    "Yes, new variant added",
    "CF-causing",
    "c.(743+1_744-1)_(869+1_870-1)del",
    "1",
    "CFTRdele6b"
  ],
  "c.[(?_1)_(53+1_54-1)del;(1392+1_1393-1)_(1584+1_1585-1)del]": [
    "c.[(?_1)_(53+1_54-1)del;(1392+1_1393-1)_(1584+1_1585-1)del]",
    "deletion of exons 1 and 10 (legacy numbering)|deletion of exons 1 and 11 (current numbering)",
    "p.?",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CFTRdele1,10",
    "CF-causing",
    "1"
  ],
  "deletion of exons 1 and 10 (legacy numbering)|deletion of exons 1 and 11 (current numbering)": [
    "c.[(?_1)_(53+1_54-1)del;(1392+1_1393-1)_(1584+1_1585-1)del]",
    "deletion of exons 1 and 10 (legacy numbering)|deletion of exons 1 and 11 (current numbering)",
    "p.?",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CFTRdele1,10",
    "CF-causing",
    "1"
  ],
  "CFTRdele1,10": [
    "c.[(?_1)_(53+1_54-1)del;(1392+1_1393-1)_(1584+1_1585-1)del]",
    "deletion of exons 1 and 10 (legacy numbering)|deletion of exons 1 and 11 (current numbering)",
    "p.?",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CFTRdele1,10",
    "CF-causing",
    "1"
  ],
  "deletion of exons 1 and 11 through 24 (legacy numbering)|deletion of exons 1 and 12 through 27 (current numbering)": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "deletion of exons 1 and 11 through 24 (legacy numbering)|deletion of exons 1 and 12 through 27 (current numbering)",
    "CFTRdele1,11-24",
    "CF-causing",
    "1",
    "c.[(?_1)_(53+1_54-1)del;(1584+1_1585-1)_(*1_?)del]"
  ],
  "CFTRdele1,11-24": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "deletion of exons 1 and 11 through 24 (legacy numbering)|deletion of exons 1 and 12 through 27 (current numbering)",
    "CFTRdele1,11-24",
    "CF-causing",
    "1",
    "c.[(?_1)_(53+1_54-1)del;(1584+1_1585-1)_(*1_?)del]"
  ],
  "c.[(?_1)_(53+1_54-1)del;(1584+1_1585-1)_(*1_?)del]": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "deletion of exons 1 and 11 through 24 (legacy numbering)|deletion of exons 1 and 12 through 27 (current numbering)",
    "CFTRdele1,11-24",
    "CF-causing",
    "1",
    "c.[(?_1)_(53+1_54-1)del;(1584+1_1585-1)_(*1_?)del]"
  ],
  "CFTRdele11-15,17a,17b": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CFTRdele11-15,17a,17b",
    "CF-causing",
    "1",
    "deletion of exons 11 through 15, 17a, and 17b (legacy numbering)|deletion of exons 12-17, 19, and 20 (current numbering)",
    "c.[(1584+1_1585-1)_(2908+1_2909-1)del;(2988+1_2989-1)_(3367+1_3368-1)del]"
  ],
  "deletion of exons 11 through 15, 17a, and 17b (legacy numbering)|deletion of exons 12-17, 19, and 20 (current numbering)": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CFTRdele11-15,17a,17b",
    "CF-causing",
    "1",
    "deletion of exons 11 through 15, 17a, and 17b (legacy numbering)|deletion of exons 12-17, 19, and 20 (current numbering)",
    "c.[(1584+1_1585-1)_(2908+1_2909-1)del;(2988+1_2989-1)_(3367+1_3368-1)del]"
  ],
  "c.[(1584+1_1585-1)_(2908+1_2909-1)del;(2988+1_2989-1)_(3367+1_3368-1)del]": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CFTRdele11-15,17a,17b",
    "CF-causing",
    "1",
    "deletion of exons 11 through 15, 17a, and 17b (legacy numbering)|deletion of exons 12-17, 19, and 20 (current numbering)",
    "c.[(1584+1_1585-1)_(2908+1_2909-1)del;(2988+1_2989-1)_(3367+1_3368-1)del]"
  ],
  "deletion of exons 12, 13, and 16 (legacy numbering)|deletion of exons 13, 14, and 18 (current numbering)": [
    "4.7369567894801664e-06",
    "p.?",
    "deletion of exons 12, 13, and 16 (legacy numbering)|deletion of exons 13, 14, and 18 (current numbering)",
    "CFTRdele12,13,16",
    "Yes, new variant added",
    "c.[(1679+1_1680-1)_(2490+1_2491-1)del;(2908+1_2909-1)_(2988+1_2909-1)del]",
    "CF-causing",
    "1"
  ],
  "CFTRdele12,13,16": [
    "4.7369567894801664e-06",
    "p.?",
    "deletion of exons 12, 13, and 16 (legacy numbering)|deletion of exons 13, 14, and 18 (current numbering)",
    "CFTRdele12,13,16",
    "Yes, new variant added",
    "c.[(1679+1_1680-1)_(2490+1_2491-1)del;(2908+1_2909-1)_(2988+1_2909-1)del]",
    "CF-causing",
    "1"
  ],
  "c.[(1679+1_1680-1)_(2490+1_2491-1)del;(2908+1_2909-1)_(2988+1_2909-1)del]": [
    "4.7369567894801664e-06",
    "p.?",
    "deletion of exons 12, 13, and 16 (legacy numbering)|deletion of exons 13, 14, and 18 (current numbering)",
    "CFTRdele12,13,16",
    "Yes, new variant added",
    "c.[(1679+1_1680-1)_(2490+1_2491-1)del;(2908+1_2909-1)_(2988+1_2909-1)del]",
    "CF-causing",
    "1"
  ],
  "c.(2619+1_2620-1)_(3873+1_3874-1)del": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "c.(2619+1_2620-1)_(3873+1_3874-1)del",
    "deletion of exons 14b through 20 (legacy numbering)|deletion of exons 16 through 23 (current numbering)",
    "CF-causing",
    "CFTRdele14b-20",
    "1"
  ],
  "deletion of exons 14b through 20 (legacy numbering)|deletion of exons 16 through 23 (current numbering)": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "c.(2619+1_2620-1)_(3873+1_3874-1)del",
    "deletion of exons 14b through 20 (legacy numbering)|deletion of exons 16 through 23 (current numbering)",
    "CF-causing",
    "CFTRdele14b-20",
    "1"
  ],
  "CFTRdele14b-20": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "c.(2619+1_2620-1)_(3873+1_3874-1)del",
    "deletion of exons 14b through 20 (legacy numbering)|deletion of exons 16 through 23 (current numbering)",
    "CF-causing",
    "CFTRdele14b-20",
    "1"
  ],
  "c.2908+1085_3367+260del": [
    "4.7369567894801664e-06",
    "c.2908+1085_3367+260del",
    "p.?",
    "Yes, new variant added",
    "IVS15+1085_IVS17B+260del7201",
    "CF-causing",
    "deletion of exons 16 through 17b (legacy numbering)|deletion of exons 18 through 20 (current numbering)",
    "1"
  ],
  "IVS15+1085_IVS17B+260del7201": [
    "4.7369567894801664e-06",
    "c.2908+1085_3367+260del",
    "p.?",
    "Yes, new variant added",
    "IVS15+1085_IVS17B+260del7201",
    "CF-causing",
    "deletion of exons 16 through 17b (legacy numbering)|deletion of exons 18 through 20 (current numbering)",
    "1"
  ],
  "deletion of exons 16 through 17b (legacy numbering)|deletion of exons 18 through 20 (current numbering)": [
    "4.7369567894801664e-06",
    "c.2908+1085_3367+260del",
    "p.?",
    "Yes, new variant added",
    "IVS15+1085_IVS17B+260del7201",
    "CF-causing",
    "deletion of exons 16 through 17b (legacy numbering)|deletion of exons 18 through 20 (current numbering)",
    "1"
  ],
  "c.(2908+1_2909-15)_(3468+10_3469-1)del": [
    "c.(2908+1_2909-15)_(3468+10_3469-1)del",
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "deletion of exons 16 through 18 (legacy numbering)|deletion of exons 16 through 21 (current numbering)",
    "1",
    "CFTRdele16-18"
  ],
  "deletion of exons 16 through 18 (legacy numbering)|deletion of exons 16 through 21 (current numbering)": [
    "c.(2908+1_2909-15)_(3468+10_3469-1)del",
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "deletion of exons 16 through 18 (legacy numbering)|deletion of exons 16 through 21 (current numbering)",
    "1",
    "CFTRdele16-18"
  ],
  "CFTRdele16-18": [
    "c.(2908+1_2909-15)_(3468+10_3469-1)del",
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "deletion of exons 16 through 18 (legacy numbering)|deletion of exons 16 through 21 (current numbering)",
    "1",
    "CFTRdele16-18"
  ],
  "c.(3367+1_3368-1)_(*1_?)del": [
    "4.7369567894801664e-06",
    "c.(3367+1_3368-1)_(*1_?)del",
    "p.?",
    "Yes, new variant added",
    "CFTRdele18-24",
    "CF-causing",
    "1",
    "deletion of exons 18 through 24 (legacy numbering)|deletion of exons 21 through 27 (current numbering)"
  ],
  "CFTRdele18-24": [
    "4.7369567894801664e-06",
    "c.(3367+1_3368-1)_(*1_?)del",
    "p.?",
    "Yes, new variant added",
    "CFTRdele18-24",
    "CF-causing",
    "1",
    "deletion of exons 18 through 24 (legacy numbering)|deletion of exons 21 through 27 (current numbering)"
  ],
  "deletion of exons 18 through 24 (legacy numbering)|deletion of exons 21 through 27 (current numbering)": [
    "4.7369567894801664e-06",
    "c.(3367+1_3368-1)_(*1_?)del",
    "p.?",
    "Yes, new variant added",
    "CFTRdele18-24",
    "CF-causing",
    "1",
    "deletion of exons 18 through 24 (legacy numbering)|deletion of exons 21 through 27 (current numbering)"
  ],
  "deletion of exons 19 through 24 (legacy numbering)|deletion of exons 22 through 27 (current numbering)": [
    "deletion of exons 19 through 24 (legacy numbering)|deletion of exons 22 through 27 (current numbering)",
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "c.(3468+1_3469-1)_(*1_?)del",
    "CF-causing",
    "1",
    "CFTRdele19-24"
  ],
  "c.(3468+1_3469-1)_(*1_?)del": [
    "deletion of exons 19 through 24 (legacy numbering)|deletion of exons 22 through 27 (current numbering)",
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "c.(3468+1_3469-1)_(*1_?)del",
    "CF-causing",
    "1",
    "CFTRdele19-24"
  ],
  "CFTRdele19-24": [
    "deletion of exons 19 through 24 (legacy numbering)|deletion of exons 22 through 27 (current numbering)",
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "c.(3468+1_3469-1)_(*1_?)del",
    "CF-causing",
    "1",
    "CFTRdele19-24"
  ],
  "CFTRdele2-22": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CFTRdele2-22",
    "CF-causing",
    "1",
    "deletion of exons 2 through 22 (legacy numbering)|deletion of exons 2 through 25 (current numbering)",
    "c.(53+1_54-1)_(4136+1_4137-1)del"
  ],
  "deletion of exons 2 through 22 (legacy numbering)|deletion of exons 2 through 25 (current numbering)": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CFTRdele2-22",
    "CF-causing",
    "1",
    "deletion of exons 2 through 22 (legacy numbering)|deletion of exons 2 through 25 (current numbering)",
    "c.(53+1_54-1)_(4136+1_4137-1)del"
  ],
  "c.(53+1_54-1)_(4136+1_4137-1)del": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CFTRdele2-22",
    "CF-causing",
    "1",
    "deletion of exons 2 through 22 (legacy numbering)|deletion of exons 2 through 25 (current numbering)",
    "c.(53+1_54-1)_(4136+1_4137-1)del"
  ],
  "c.(53+1_54-1)_(1116+1_1117-1)del": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "c.(53+1_54-1)_(1116+1_1117-1)del",
    "CF-causing",
    "deletion of exons 2 through 7 (legacy numbering)|deletion of exons 2 through 8 (current numbering)",
    "1",
    "CFTRdele2-7"
  ],
  "deletion of exons 2 through 7 (legacy numbering)|deletion of exons 2 through 8 (current numbering)": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "c.(53+1_54-1)_(1116+1_1117-1)del",
    "CF-causing",
    "deletion of exons 2 through 7 (legacy numbering)|deletion of exons 2 through 8 (current numbering)",
    "1",
    "CFTRdele2-7"
  ],
  "CFTRdele2-7": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "c.(53+1_54-1)_(1116+1_1117-1)del",
    "CF-causing",
    "deletion of exons 2 through 7 (legacy numbering)|deletion of exons 2 through 8 (current numbering)",
    "1",
    "CFTRdele2-7"
  ],
  "CFTRdele2-8": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CFTRdele2-8",
    "CF-causing",
    "1",
    "deletion of exons 2 through 8 (legacy numbering)|deletion of exons 2 through 9 (current numbering)",
    "c.(53+1_54-1)_(1209+1_1210-1)del"
  ],
  "deletion of exons 2 through 8 (legacy numbering)|deletion of exons 2 through 9 (current numbering)": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CFTRdele2-8",
    "CF-causing",
    "1",
    "deletion of exons 2 through 8 (legacy numbering)|deletion of exons 2 through 9 (current numbering)",
    "c.(53+1_54-1)_(1209+1_1210-1)del"
  ],
  "c.(53+1_54-1)_(1209+1_1210-1)del": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CFTRdele2-8",
    "CF-causing",
    "1",
    "deletion of exons 2 through 8 (legacy numbering)|deletion of exons 2 through 9 (current numbering)",
    "c.(53+1_54-1)_(1209+1_1210-1)del"
  ],
  "CFTRdele2-9": [
    "4.7369567894801664e-06",
    "CFTRdele2-9",
    "p.?",
    "Yes, new variant added",
    "deletion of exons 2 through 9 (legacy numbering)|deletion of exons 2 through 10 (current numbering)",
    "CF-causing",
    "1",
    "c.53+9713_1392+2669del"
  ],
  "deletion of exons 2 through 9 (legacy numbering)|deletion of exons 2 through 10 (current numbering)": [
    "4.7369567894801664e-06",
    "CFTRdele2-9",
    "p.?",
    "Yes, new variant added",
    "deletion of exons 2 through 9 (legacy numbering)|deletion of exons 2 through 10 (current numbering)",
    "CF-causing",
    "1",
    "c.53+9713_1392+2669del"
  ],
  "c.53+9713_1392+2669del": [
    "4.7369567894801664e-06",
    "CFTRdele2-9",
    "p.?",
    "Yes, new variant added",
    "deletion of exons 2 through 9 (legacy numbering)|deletion of exons 2 through 10 (current numbering)",
    "CF-causing",
    "1",
    "c.53+9713_1392+2669del"
  ],
  "deletion of exons 2, 3, and 10 (legacy numbering)|deletion of exons 2, 3, and 11 (current numbering)": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "deletion of exons 2, 3, and 10 (legacy numbering)|deletion of exons 2, 3, and 11 (current numbering)",
    "CF-causing",
    "CFTRdele2,3,10",
    "c.[(53+1_54)_(273_274-1)del;(1392+1_1393-1)_(1584+1_1585-1)del]",
    "1"
  ],
  "CFTRdele2,3,10": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "deletion of exons 2, 3, and 10 (legacy numbering)|deletion of exons 2, 3, and 11 (current numbering)",
    "CF-causing",
    "CFTRdele2,3,10",
    "c.[(53+1_54)_(273_274-1)del;(1392+1_1393-1)_(1584+1_1585-1)del]",
    "1"
  ],
  "c.[(53+1_54)_(273_274-1)del;(1392+1_1393-1)_(1584+1_1585-1)del]": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "deletion of exons 2, 3, and 10 (legacy numbering)|deletion of exons 2, 3, and 11 (current numbering)",
    "CF-causing",
    "CFTRdele2,3,10",
    "c.[(53+1_54)_(273_274-1)del;(1392+1_1393-1)_(1584+1_1585-1)del]",
    "1"
  ],
  "CFTRdele20-23": [
    "4.7369567894801664e-06",
    "p.?",
    "CFTRdele20-23",
    "Yes, new variant added",
    "c.(3717+1_3718-1)_(4242+1_4243-1)del",
    "CF-causing",
    "deletion of exons 20 through 23 (legacy numbering)|deletion of exons 23 through 26 (current numbering)",
    "1"
  ],
  "c.(3717+1_3718-1)_(4242+1_4243-1)del": [
    "4.7369567894801664e-06",
    "p.?",
    "CFTRdele20-23",
    "Yes, new variant added",
    "c.(3717+1_3718-1)_(4242+1_4243-1)del",
    "CF-causing",
    "deletion of exons 20 through 23 (legacy numbering)|deletion of exons 23 through 26 (current numbering)",
    "1"
  ],
  "deletion of exons 20 through 23 (legacy numbering)|deletion of exons 23 through 26 (current numbering)": [
    "4.7369567894801664e-06",
    "p.?",
    "CFTRdele20-23",
    "Yes, new variant added",
    "c.(3717+1_3718-1)_(4242+1_4243-1)del",
    "CF-causing",
    "deletion of exons 20 through 23 (legacy numbering)|deletion of exons 23 through 26 (current numbering)",
    "1"
  ],
  "c.(4136+1_4137-1)_(*1_?)del": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "c.(4136+1_4137-1)_(*1_?)del",
    "1",
    "CFTRdele23,24",
    "deletion of exons 23 and 24 (legacy numbering)|deletion of exons 26 and 27 (current numbering)"
  ],
  "CFTRdele23,24": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "c.(4136+1_4137-1)_(*1_?)del",
    "1",
    "CFTRdele23,24",
    "deletion of exons 23 and 24 (legacy numbering)|deletion of exons 26 and 27 (current numbering)"
  ],
  "deletion of exons 23 and 24 (legacy numbering)|deletion of exons 26 and 27 (current numbering)": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "c.(4136+1_4137-1)_(*1_?)del",
    "1",
    "CFTRdele23,24",
    "deletion of exons 23 and 24 (legacy numbering)|deletion of exons 26 and 27 (current numbering)"
  ],
  "CFTRdele5,6a": [
    "4.7369567894801664e-06",
    "CFTRdele5,6a",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.(489+1_490-1)_(743+1_744-1)del",
    "deletion of exons 5 and 6a (legacy numbering)|deletion of exons 5 and 6 (current numbering)"
  ],
  "c.(489+1_490-1)_(743+1_744-1)del": [
    "4.7369567894801664e-06",
    "CFTRdele5,6a",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.(489+1_490-1)_(743+1_744-1)del",
    "deletion of exons 5 and 6a (legacy numbering)|deletion of exons 5 and 6 (current numbering)"
  ],
  "deletion of exons 5 and 6a (legacy numbering)|deletion of exons 5 and 6 (current numbering)": [
    "4.7369567894801664e-06",
    "CFTRdele5,6a",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.(489+1_490-1)_(743+1_744-1)del",
    "deletion of exons 5 and 6a (legacy numbering)|deletion of exons 5 and 6 (current numbering)"
  ],
  "CFTRdele7,8": [
    "4.7369567894801664e-06",
    "p.?",
    "CFTRdele7,8",
    "Yes, new variant added",
    "CF-causing",
    "deletion of exons 7 and 8 (legacy numbering)|deletion of exons 8 and 9 (current numbering)",
    "c.(870-1053_870-126)_(1209+1_1210-1)del",
    "1"
  ],
  "deletion of exons 7 and 8 (legacy numbering)|deletion of exons 8 and 9 (current numbering)": [
    "4.7369567894801664e-06",
    "p.?",
    "CFTRdele7,8",
    "Yes, new variant added",
    "CF-causing",
    "deletion of exons 7 and 8 (legacy numbering)|deletion of exons 8 and 9 (current numbering)",
    "c.(870-1053_870-126)_(1209+1_1210-1)del",
    "1"
  ],
  "c.(870-1053_870-126)_(1209+1_1210-1)del": [
    "4.7369567894801664e-06",
    "p.?",
    "CFTRdele7,8",
    "Yes, new variant added",
    "CF-causing",
    "deletion of exons 7 and 8 (legacy numbering)|deletion of exons 8 and 9 (current numbering)",
    "c.(870-1053_870-126)_(1209+1_1210-1)del",
    "1"
  ],
  "deletion of part of the promoter through exon 9 (legacy numbering)|deletion of part of the promoter through exon 10 (current numbering)": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "deletion of part of the promoter through exon 9 (legacy numbering)|deletion of part of the promoter through exon 10 (current numbering)",
    "CF-causing",
    "c.(?_1)_(1392+1_1393-1)del",
    "1",
    "CFTRdelePr-9"
  ],
  "CFTRdelePr-9": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "deletion of part of the promoter through exon 9 (legacy numbering)|deletion of part of the promoter through exon 10 (current numbering)",
    "CF-causing",
    "c.(?_1)_(1392+1_1393-1)del",
    "1",
    "CFTRdelePr-9"
  ],
  "CFTRdup1": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "CFTRdup1",
    "duplication of exon 1 (legacy and current numbering)",
    "c.(?_1)_(53+1_54-1)dup"
  ],
  "duplication of exon 1 (legacy and current numbering)": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "CFTRdup1",
    "duplication of exon 1 (legacy and current numbering)",
    "c.(?_1)_(53+1_54-1)dup"
  ],
  "c.(?_1)_(53+1_54-1)dup": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "CFTRdup1",
    "duplication of exon 1 (legacy and current numbering)",
    "c.(?_1)_(53+1_54-1)dup"
  ],
  "duplication of exons 14a through 19 (legacy numbering)|duplication of exons 15 through 22 (current numbering)": [
    "duplication of exons 14a through 19 (legacy numbering)|duplication of exons 15 through 22 (current numbering)",
    "4.7369567894801664e-06",
    "p.?",
    "c.(2490+1_2491-1)_(3717+1_3718-1)dup",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "CFTRdup14a-19"
  ],
  "c.(2490+1_2491-1)_(3717+1_3718-1)dup": [
    "duplication of exons 14a through 19 (legacy numbering)|duplication of exons 15 through 22 (current numbering)",
    "4.7369567894801664e-06",
    "p.?",
    "c.(2490+1_2491-1)_(3717+1_3718-1)dup",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "CFTRdup14a-19"
  ],
  "CFTRdup14a-19": [
    "duplication of exons 14a through 19 (legacy numbering)|duplication of exons 15 through 22 (current numbering)",
    "4.7369567894801664e-06",
    "p.?",
    "c.(2490+1_2491-1)_(3717+1_3718-1)dup",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "CFTRdup14a-19"
  ],
  "CFTRdup14b-17b": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "CFTRdup14b-17b",
    "1",
    "duplication of exons 14b through 17b (legacy numbering)|duplication of exons 16 through 20 (current numbering)",
    "c.(2619+1_2620-1)_(3367+1_3368-1)dup"
  ],
  "duplication of exons 14b through 17b (legacy numbering)|duplication of exons 16 through 20 (current numbering)": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "CFTRdup14b-17b",
    "1",
    "duplication of exons 14b through 17b (legacy numbering)|duplication of exons 16 through 20 (current numbering)",
    "c.(2619+1_2620-1)_(3367+1_3368-1)dup"
  ],
  "c.(2619+1_2620-1)_(3367+1_3368-1)dup": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "CFTRdup14b-17b",
    "1",
    "duplication of exons 14b through 17b (legacy numbering)|duplication of exons 16 through 20 (current numbering)",
    "c.(2619+1_2620-1)_(3367+1_3368-1)dup"
  ],
  "duplication of exons 16 through 18 (legacy numbering)|duplication of exons 18 through 21 (current numbering)": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "duplication of exons 16 through 18 (legacy numbering)|duplication of exons 18 through 21 (current numbering)",
    "CF-causing",
    "c.(2908+1_2909-1)_(3468+1_3469-1)dup",
    "CFTRdup16-18",
    "1"
  ],
  "c.(2908+1_2909-1)_(3468+1_3469-1)dup": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "duplication of exons 16 through 18 (legacy numbering)|duplication of exons 18 through 21 (current numbering)",
    "CF-causing",
    "c.(2908+1_2909-1)_(3468+1_3469-1)dup",
    "CFTRdup16-18",
    "1"
  ],
  "CFTRdup16-18": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "duplication of exons 16 through 18 (legacy numbering)|duplication of exons 18 through 21 (current numbering)",
    "CF-causing",
    "c.(2908+1_2909-1)_(3468+1_3469-1)dup",
    "CFTRdup16-18",
    "1"
  ],
  "duplication of exons 16 through 20 (legacy numbering)|duplication of exons 16 through 23 (current numbering)": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "duplication of exons 16 through 20 (legacy numbering)|duplication of exons 16 through 23 (current numbering)",
    "CFTRdup16-20",
    "CF-causing",
    "1",
    "c.(2908+1_2909-1)_(3873+1_3874-1)dup"
  ],
  "CFTRdup16-20": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "duplication of exons 16 through 20 (legacy numbering)|duplication of exons 16 through 23 (current numbering)",
    "CFTRdup16-20",
    "CF-causing",
    "1",
    "c.(2908+1_2909-1)_(3873+1_3874-1)dup"
  ],
  "c.(2908+1_2909-1)_(3873+1_3874-1)dup": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "duplication of exons 16 through 20 (legacy numbering)|duplication of exons 16 through 23 (current numbering)",
    "CFTRdup16-20",
    "CF-causing",
    "1",
    "c.(2908+1_2909-1)_(3873+1_3874-1)dup"
  ],
  "c.(2908+1_2909-1)_(4136+1_4137-1)del": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "c.(2908+1_2909-1)_(4136+1_4137-1)del",
    "duplication of exons 16 through 22 (legacy numbering)|duplication of exons 16 through 25 (current numbering)",
    "CF-causing",
    "1",
    "CFTRdup16-22"
  ],
  "duplication of exons 16 through 22 (legacy numbering)|duplication of exons 16 through 25 (current numbering)": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "c.(2908+1_2909-1)_(4136+1_4137-1)del",
    "duplication of exons 16 through 22 (legacy numbering)|duplication of exons 16 through 25 (current numbering)",
    "CF-causing",
    "1",
    "CFTRdup16-22"
  ],
  "CFTRdup16-22": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "c.(2908+1_2909-1)_(4136+1_4137-1)del",
    "duplication of exons 16 through 22 (legacy numbering)|duplication of exons 16 through 25 (current numbering)",
    "CF-causing",
    "1",
    "CFTRdup16-22"
  ],
  "c.(53+1_54-1)_(489+1_490-1)dup": [
    "c.(53+1_54-1)_(489+1_490-1)dup",
    "duplication of exons 2 through 4 (legacy numbering and current numbering)",
    "p.?",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CFTRdup2-4",
    "CF-causing",
    "1"
  ],
  "duplication of exons 2 through 4 (legacy numbering and current numbering)": [
    "c.(53+1_54-1)_(489+1_490-1)dup",
    "duplication of exons 2 through 4 (legacy numbering and current numbering)",
    "p.?",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CFTRdup2-4",
    "CF-causing",
    "1"
  ],
  "CFTRdup2-4": [
    "c.(53+1_54-1)_(489+1_490-1)dup",
    "duplication of exons 2 through 4 (legacy numbering and current numbering)",
    "p.?",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CFTRdup2-4",
    "CF-causing",
    "1"
  ],
  "duplication of exons 22 and 23 (legacy numbering)|duplication of exons 25 and 26 (current numbering)": [
    "4.7369567894801664e-06",
    "p.?",
    "duplication of exons 22 and 23 (legacy numbering)|duplication of exons 25 and 26 (current numbering)",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.(3963+1_3964-1)_(4242+1_4243-1)dup",
    "CFTRdup22,23"
  ],
  "c.(3963+1_3964-1)_(4242+1_4243-1)dup": [
    "4.7369567894801664e-06",
    "p.?",
    "duplication of exons 22 and 23 (legacy numbering)|duplication of exons 25 and 26 (current numbering)",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.(3963+1_3964-1)_(4242+1_4243-1)dup",
    "CFTRdup22,23"
  ],
  "CFTRdup22,23": [
    "4.7369567894801664e-06",
    "p.?",
    "duplication of exons 22 and 23 (legacy numbering)|duplication of exons 25 and 26 (current numbering)",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.(3963+1_3964-1)_(4242+1_4243-1)dup",
    "CFTRdup22,23"
  ],
  "c.(273+1_274-1)_(3717+1_3718-1)del": [
    "4.7369567894801664e-06",
    "p.?",
    "c.(273+1_274-1)_(3717+1_3718-1)del",
    "Yes, new variant added",
    "CFTRdup4-19",
    "CF-causing",
    "1",
    "duplication of exons 4 through 19 (legacy numbering)|duplication of exons 4 through 22 (current numbering)"
  ],
  "CFTRdup4-19": [
    "4.7369567894801664e-06",
    "p.?",
    "c.(273+1_274-1)_(3717+1_3718-1)del",
    "Yes, new variant added",
    "CFTRdup4-19",
    "CF-causing",
    "1",
    "duplication of exons 4 through 19 (legacy numbering)|duplication of exons 4 through 22 (current numbering)"
  ],
  "duplication of exons 4 through 19 (legacy numbering)|duplication of exons 4 through 22 (current numbering)": [
    "4.7369567894801664e-06",
    "p.?",
    "c.(273+1_274-1)_(3717+1_3718-1)del",
    "Yes, new variant added",
    "CFTRdup4-19",
    "CF-causing",
    "1",
    "duplication of exons 4 through 19 (legacy numbering)|duplication of exons 4 through 22 (current numbering)"
  ],
  "CFTRdup4-8": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "CFTRdup4-8",
    "c.(273+1_274-1)_(1209+1_1210-1)dup",
    "1",
    "duplication of exons 4 through 8 (legacy numbering)|duplication of exons 4 through 9 (current numbering)"
  ],
  "c.(273+1_274-1)_(1209+1_1210-1)dup": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "CFTRdup4-8",
    "c.(273+1_274-1)_(1209+1_1210-1)dup",
    "1",
    "duplication of exons 4 through 8 (legacy numbering)|duplication of exons 4 through 9 (current numbering)"
  ],
  "duplication of exons 4 through 8 (legacy numbering)|duplication of exons 4 through 9 (current numbering)": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "CFTRdup4-8",
    "c.(273+1_274-1)_(1209+1_1210-1)dup",
    "1",
    "duplication of exons 4 through 8 (legacy numbering)|duplication of exons 4 through 9 (current numbering)"
  ],
  "duplication of exons 6a and 6b (legacy numbering)|duplication of exons 6 and 7 (current numbering)": [
    "duplication of exons 6a and 6b (legacy numbering)|duplication of exons 6 and 7 (current numbering)",
    "CFTRdup6a,6b",
    "p.?",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.(579+1_580-1)_(869+1_870-1)dup"
  ],
  "CFTRdup6a,6b": [
    "duplication of exons 6a and 6b (legacy numbering)|duplication of exons 6 and 7 (current numbering)",
    "CFTRdup6a,6b",
    "p.?",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.(579+1_580-1)_(869+1_870-1)dup"
  ],
  "c.(579+1_580-1)_(869+1_870-1)dup": [
    "duplication of exons 6a and 6b (legacy numbering)|duplication of exons 6 and 7 (current numbering)",
    "CFTRdup6a,6b",
    "p.?",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.(579+1_580-1)_(869+1_870-1)dup"
  ],
  "partial deletion of exon 17b (legacy numbering) with insertion of TGTTAA|partial deletion of exon 20 (current numbering) with insertion of TGTTAA": [
    "4.7369567894801664e-06",
    "p.?",
    "partial deletion of exon 17b (legacy numbering) with insertion of TGTTAA|partial deletion of exon 20 (current numbering) with insertion of TGTTAA",
    "3413_3499+268del355PBins6PB",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.3281_3367+268delinsTGTTAA"
  ],
  "3413_3499+268del355PBins6PB": [
    "4.7369567894801664e-06",
    "p.?",
    "partial deletion of exon 17b (legacy numbering) with insertion of TGTTAA|partial deletion of exon 20 (current numbering) with insertion of TGTTAA",
    "3413_3499+268del355PBins6PB",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.3281_3367+268delinsTGTTAA"
  ],
  "c.3281_3367+268delinsTGTTAA": [
    "4.7369567894801664e-06",
    "p.?",
    "partial deletion of exon 17b (legacy numbering) with insertion of TGTTAA|partial deletion of exon 20 (current numbering) with insertion of TGTTAA",
    "3413_3499+268del355PBins6PB",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.3281_3367+268delinsTGTTAA"
  ],
  "3499+1G->T": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "3499+1G->T",
    "c.3367+1G>T",
    "CF-causing",
    "1"
  ],
  "c.3367+1G>T": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "3499+1G->T",
    "c.3367+1G>T",
    "CF-causing",
    "1"
  ],
  "c.3963+1G>C": [
    "c.3963+1G>C",
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "4095+1G->C",
    "CF-causing",
    "1"
  ],
  "4095+1G->C": [
    "c.3963+1G>C",
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "4095+1G->C",
    "CF-causing",
    "1"
  ],
  "c.1116_1116+1insATCAA": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "CF-causing",
    "c.1116_1116+1insATCAA",
    "1",
    "1248insATCAA"
  ],
  "1248insATCAA": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "CF-causing",
    "c.1116_1116+1insATCAA",
    "1",
    "1248insATCAA"
  ],
  "c.1209+1G>C": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "CF-causing",
    "1",
    "c.1209+1G>C",
    "1341+1G->C"
  ],
  "1341+1G->C": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "CF-causing",
    "1",
    "c.1209+1G>C",
    "1341+1G->C"
  ],
  "1341+2T->G": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "1341+2T->G",
    "CF-causing",
    "c.1209+2T>G",
    "1"
  ],
  "c.1209+2T>G": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "1341+2T->G",
    "CF-causing",
    "c.1209+2T>G",
    "1"
  ],
  "c.1210-1G>T": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "c.1210-1G>T",
    "CF-causing",
    "1342-1G->T",
    "1"
  ],
  "1342-1G->T": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "c.1210-1G>T",
    "CF-causing",
    "1342-1G->T",
    "1"
  ],
  "1524+1delG": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "CF-causing",
    "1",
    "1524+1delG",
    "c.1392+1del"
  ],
  "c.1392+1del": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "CF-causing",
    "1",
    "1524+1delG",
    "c.1392+1del"
  ],
  "c.1766+2del": [
    "4.7369567894801664e-06",
    "c.1766+2del",
    "p.?",
    "No",
    "CF-causing",
    "1",
    "1898+2delT"
  ],
  "1898+2delT": [
    "4.7369567894801664e-06",
    "c.1766+2del",
    "p.?",
    "No",
    "CF-causing",
    "1",
    "1898+2delT"
  ],
  "2751+2T->A": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "CF-causing",
    "2751+2T->A",
    "c.2619+2T>A",
    "1"
  ],
  "c.2619+2T>A": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "CF-causing",
    "2751+2T->A",
    "c.2619+2T>A",
    "1"
  ],
  "c.2620-1G>T": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "c.2620-1G>T",
    "2752-1G->T",
    "CF-causing",
    "1"
  ],
  "2752-1G->T": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "c.2620-1G>T",
    "2752-1G->T",
    "CF-causing",
    "1"
  ],
  "c.274-2A>C": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "c.274-2A>C",
    "CF-causing",
    "1",
    "406-2A->C"
  ],
  "406-2A->C": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "c.274-2A>C",
    "CF-causing",
    "1",
    "406-2A->C"
  ],
  "3121-2A->T": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "3121-2A->T",
    "c.2989-2A>T",
    "CF-causing",
    "1"
  ],
  "c.2989-2A>T": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "3121-2A->T",
    "c.2989-2A>T",
    "CF-causing",
    "1"
  ],
  "3499+2T->C": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "3499+2T->C",
    "CF-causing",
    "1",
    "c.3367+2T>C"
  ],
  "c.3367+2T>C": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "3499+2T->C",
    "CF-causing",
    "1",
    "c.3367+2T>C"
  ],
  "c.3368-1G>A": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "CF-causing",
    "1",
    "c.3368-1G>A",
    "3500-1G->A"
  ],
  "3500-1G->A": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "CF-causing",
    "1",
    "c.3368-1G>A",
    "3500-1G->A"
  ],
  "c.3963+1G>A": [
    "c.3963+1G>A",
    "4.7369567894801664e-06",
    "4095+1G->A",
    "p.?",
    "No",
    "CF-causing",
    "1"
  ],
  "4095+1G->A": [
    "c.3963+1G>A",
    "4.7369567894801664e-06",
    "4095+1G->A",
    "p.?",
    "No",
    "CF-causing",
    "1"
  ],
  "622-2A->C": [
    "622-2A->C",
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "CF-causing",
    "c.490-2A>C",
    "1"
  ],
  "c.490-2A>C": [
    "622-2A->C",
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "CF-causing",
    "c.490-2A>C",
    "1"
  ],
  "186-2A->G": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "186-2A->G",
    "CF-causing",
    "c.54-2A>G",
    "1"
  ],
  "c.54-2A>G": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "186-2A->G",
    "CF-causing",
    "c.54-2A>G",
    "1"
  ],
  "c.2491-2A>G": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "c.2491-2A>G",
    "CF-causing",
    "1",
    "2623-2A->G"
  ],
  "2623-2A->G": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "c.2491-2A>G",
    "CF-causing",
    "1",
    "2623-2A->G"
  ],
  "c.2989-1G>T": [
    "c.2989-1G>T",
    "3121-1G->T",
    "p.?",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "1"
  ],
  "3121-1G->T": [
    "c.2989-1G>T",
    "3121-1G->T",
    "p.?",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "1"
  ],
  "c.2989-2A>C": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "c.2989-2A>C",
    "3121-2A->C",
    "CF-causing",
    "1"
  ],
  "3121-2A->C": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "c.2989-2A>C",
    "3121-2A->C",
    "CF-causing",
    "1"
  ],
  "3601-1G->A": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "CF-causing",
    "3601-1G->A",
    "c.3469-1G>A",
    "1"
  ],
  "c.3469-1G>A": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "CF-causing",
    "3601-1G->A",
    "c.3469-1G>A",
    "1"
  ],
  "c.1972dup": [
    "4.7369567894801664e-06",
    "c.1972dup",
    "No",
    "2104insA",
    "CF-causing",
    "p.Arg658LysfsX7",
    "1"
  ],
  "2104insA": [
    "4.7369567894801664e-06",
    "c.1972dup",
    "No",
    "2104insA",
    "CF-causing",
    "p.Arg658LysfsX7",
    "1"
  ],
  "p.Arg658LysfsX7": [
    "4.7369567894801664e-06",
    "c.1972dup",
    "No",
    "2104insA",
    "CF-causing",
    "p.Arg658LysfsX7",
    "1"
  ],
  "p.Glu695LysfsX27": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "p.Glu695LysfsX27",
    "2215delG",
    "1",
    "c.2083del"
  ],
  "2215delG": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "p.Glu695LysfsX27",
    "2215delG",
    "1",
    "c.2083del"
  ],
  "c.2083del": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "p.Glu695LysfsX27",
    "2215delG",
    "1",
    "c.2083del"
  ],
  "c.2508del": [
    "4.7369567894801664e-06",
    "c.2508del",
    "No",
    "p.Asp836GlufsX8",
    "CF-causing",
    "2640delT",
    "1"
  ],
  "p.Asp836GlufsX8": [
    "4.7369567894801664e-06",
    "c.2508del",
    "No",
    "p.Asp836GlufsX8",
    "CF-causing",
    "2640delT",
    "1"
  ],
  "2640delT": [
    "4.7369567894801664e-06",
    "c.2508del",
    "No",
    "p.Asp836GlufsX8",
    "CF-causing",
    "2640delT",
    "1"
  ],
  "1157insTA": [
    "4.7369567894801664e-06",
    "No",
    "1157insTA",
    "CF-causing",
    "p.Cys343ThrfsX27",
    "1",
    "c.1025_1026insTA"
  ],
  "p.Cys343ThrfsX27": [
    "4.7369567894801664e-06",
    "No",
    "1157insTA",
    "CF-causing",
    "p.Cys343ThrfsX27",
    "1",
    "c.1025_1026insTA"
  ],
  "c.1025_1026insTA": [
    "4.7369567894801664e-06",
    "No",
    "1157insTA",
    "CF-causing",
    "p.Cys343ThrfsX27",
    "1",
    "c.1025_1026insTA"
  ],
  "c.1118dup": [
    "4.7369567894801664e-06",
    "c.1118dup",
    "No",
    "p.Asp373GlufsX9",
    "CF-causing",
    "1",
    "1249insA"
  ],
  "p.Asp373GlufsX9": [
    "4.7369567894801664e-06",
    "c.1118dup",
    "No",
    "p.Asp373GlufsX9",
    "CF-causing",
    "1",
    "1249insA"
  ],
  "1249insA": [
    "4.7369567894801664e-06",
    "c.1118dup",
    "No",
    "p.Asp373GlufsX9",
    "CF-causing",
    "1",
    "1249insA"
  ],
  "241delAT": [
    "4.7369567894801664e-06",
    "No",
    "241delAT",
    "CF-causing",
    "1",
    "c.112_113del",
    "p.Tyr38ProfsX6"
  ],
  "c.112_113del": [
    "4.7369567894801664e-06",
    "No",
    "241delAT",
    "CF-causing",
    "1",
    "c.112_113del",
    "p.Tyr38ProfsX6"
  ],
  "p.Tyr38ProfsX6": [
    "4.7369567894801664e-06",
    "No",
    "241delAT",
    "CF-causing",
    "1",
    "c.112_113del",
    "p.Tyr38ProfsX6"
  ],
  "1262delA": [
    "4.7369567894801664e-06",
    "No",
    "1262delA",
    "p.Lys377SerfsX11",
    "CF-causing",
    "c.1130del",
    "1"
  ],
  "p.Lys377SerfsX11": [
    "4.7369567894801664e-06",
    "No",
    "1262delA",
    "p.Lys377SerfsX11",
    "CF-causing",
    "c.1130del",
    "1"
  ],
  "c.1130del": [
    "4.7369567894801664e-06",
    "No",
    "1262delA",
    "p.Lys377SerfsX11",
    "CF-causing",
    "c.1130del",
    "1"
  ],
  "c.1157dup": [
    "c.1157dup",
    "4.7369567894801664e-06",
    "No",
    "p.Asn386LysfsX25",
    "CF-causing",
    "1",
    "1288insA"
  ],
  "p.Asn386LysfsX25": [
    "c.1157dup",
    "4.7369567894801664e-06",
    "No",
    "p.Asn386LysfsX25",
    "CF-causing",
    "1",
    "1288insA"
  ],
  "1288insA": [
    "c.1157dup",
    "4.7369567894801664e-06",
    "No",
    "p.Asn386LysfsX25",
    "CF-causing",
    "1",
    "1288insA"
  ],
  "c.1162_1168del": [
    "c.1162_1168del",
    "4.7369567894801664e-06",
    "No",
    "1294del7",
    "CF-causing",
    "p.Thr388GlnfsX3",
    "1"
  ],
  "1294del7": [
    "c.1162_1168del",
    "4.7369567894801664e-06",
    "No",
    "1294del7",
    "CF-causing",
    "p.Thr388GlnfsX3",
    "1"
  ],
  "p.Thr388GlnfsX3": [
    "c.1162_1168del",
    "4.7369567894801664e-06",
    "No",
    "1294del7",
    "CF-causing",
    "p.Thr388GlnfsX3",
    "1"
  ],
  "1380insT": [
    "4.7369567894801664e-06",
    "No",
    "1380insT",
    "c.1248dup",
    "CF-causing",
    "p.Asn417X",
    "1"
  ],
  "c.1248dup": [
    "4.7369567894801664e-06",
    "No",
    "1380insT",
    "c.1248dup",
    "CF-causing",
    "p.Asn417X",
    "1"
  ],
  "p.Asn417X": [
    "4.7369567894801664e-06",
    "No",
    "1380insT",
    "c.1248dup",
    "CF-causing",
    "p.Asn417X",
    "1"
  ],
  "1498delG": [
    "1498delG",
    "4.7369567894801664e-06",
    "p.Val456LeufsX13",
    "No",
    "CF-causing",
    "1",
    "c.1366del"
  ],
  "p.Val456LeufsX13": [
    "1498delG",
    "4.7369567894801664e-06",
    "p.Val456LeufsX13",
    "No",
    "CF-causing",
    "1",
    "c.1366del"
  ],
  "c.1366del": [
    "1498delG",
    "4.7369567894801664e-06",
    "p.Val456LeufsX13",
    "No",
    "CF-causing",
    "1",
    "c.1366del"
  ],
  "c.1439del": [
    "c.1439del",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "1571delG",
    "1",
    "p.Gly480ValfsX47"
  ],
  "1571delG": [
    "c.1439del",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "1571delG",
    "1",
    "p.Gly480ValfsX47"
  ],
  "p.Gly480ValfsX47": [
    "c.1439del",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "1571delG",
    "1",
    "p.Gly480ValfsX47"
  ],
  "c.1616_1617dup": [
    "4.7369567894801664e-06",
    "No",
    "c.1616_1617dup",
    "1749insTA",
    "CF-causing",
    "1",
    "p.Val540X"
  ],
  "1749insTA": [
    "4.7369567894801664e-06",
    "No",
    "c.1616_1617dup",
    "1749insTA",
    "CF-causing",
    "1",
    "p.Val540X"
  ],
  "p.Val540X": [
    "4.7369567894801664e-06",
    "No",
    "c.1616_1617dup",
    "1749insTA",
    "CF-causing",
    "1",
    "p.Val540X"
  ],
  "c.1674del": [
    "4.7369567894801664e-06",
    "No",
    "c.1674del",
    "CF-causing",
    "1",
    "p.Ala559GlnfsX13",
    "1806delA"
  ],
  "p.Ala559GlnfsX13": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1807delG",
    "1",
    "c.1675del",
    "p.Ala559GlnfsX13"
  ],
  "1806delA": [
    "4.7369567894801664e-06",
    "No",
    "c.1674del",
    "CF-causing",
    "1",
    "p.Ala559GlnfsX13",
    "1806delA"
  ],
  "c.1741_1742dup": [
    "4.7369567894801664e-06",
    "c.1741_1742dup",
    "No",
    "CF-causing",
    "1874_1875insTT",
    "1",
    "p.Leu581PhefsX2"
  ],
  "1874_1875insTT": [
    "4.7369567894801664e-06",
    "c.1741_1742dup",
    "No",
    "CF-causing",
    "1874_1875insTT",
    "1",
    "p.Leu581PhefsX2"
  ],
  "p.Leu581PhefsX2": [
    "4.7369567894801664e-06",
    "c.1741_1742dup",
    "No",
    "CF-causing",
    "1874_1875insTT",
    "1",
    "p.Leu581PhefsX2"
  ],
  "c.1800del": [
    "4.7369567894801664e-06",
    "No",
    "c.1800del",
    "1932delG",
    "p.Ile601PhefsX10",
    "CF-causing",
    "1"
  ],
  "1932delG": [
    "4.7369567894801664e-06",
    "No",
    "c.1800del",
    "1932delG",
    "p.Ile601PhefsX10",
    "CF-causing",
    "1"
  ],
  "p.Ile601PhefsX10": [
    "4.7369567894801664e-06",
    "No",
    "c.1800del",
    "1932delG",
    "p.Ile601PhefsX10",
    "CF-causing",
    "1"
  ],
  "1942del17": [
    "4.7369567894801664e-06",
    "No",
    "1942del17",
    "CF-causing",
    "p.Thr604PhefsX5",
    "1",
    "c.1810_1826del"
  ],
  "p.Thr604PhefsX5": [
    "4.7369567894801664e-06",
    "No",
    "1942del17",
    "CF-causing",
    "p.Thr604PhefsX5",
    "1",
    "c.1810_1826del"
  ],
  "c.1810_1826del": [
    "4.7369567894801664e-06",
    "No",
    "1942del17",
    "CF-causing",
    "p.Thr604PhefsX5",
    "1",
    "c.1810_1826del"
  ],
  "p.Ile616TyrfsX2": [
    "p.Ile616TyrfsX2",
    "4.7369567894801664e-06",
    "No",
    "1978delA",
    "c.1846del",
    "CF-causing",
    "1"
  ],
  "1978delA": [
    "p.Ile616TyrfsX2",
    "4.7369567894801664e-06",
    "No",
    "1978delA",
    "c.1846del",
    "CF-causing",
    "1"
  ],
  "c.1846del": [
    "p.Ile616TyrfsX2",
    "4.7369567894801664e-06",
    "No",
    "1978delA",
    "c.1846del",
    "CF-causing",
    "1"
  ],
  "317insC": [
    "4.7369567894801664e-06",
    "317insC",
    "No",
    "p.Ser63PhefsX6",
    "CF-causing",
    "1",
    "c.185dup"
  ],
  "p.Ser63PhefsX6": [
    "4.7369567894801664e-06",
    "317insC",
    "No",
    "p.Ser63PhefsX6",
    "CF-causing",
    "1",
    "c.185dup"
  ],
  "c.185dup": [
    "4.7369567894801664e-06",
    "317insC",
    "No",
    "p.Ser63PhefsX6",
    "CF-causing",
    "1",
    "c.185dup"
  ],
  "2005delTA": [
    "4.7369567894801664e-06",
    "No",
    "2005delTA",
    "CF-causing",
    "p.Tyr625PhefsX16",
    "1",
    "c.1874_1875del"
  ],
  "p.Tyr625PhefsX16": [
    "4.7369567894801664e-06",
    "No",
    "2005delTA",
    "CF-causing",
    "p.Tyr625PhefsX16",
    "1",
    "c.1874_1875del"
  ],
  "c.1874_1875del": [
    "4.7369567894801664e-06",
    "No",
    "2005delTA",
    "CF-causing",
    "p.Tyr625PhefsX16",
    "1",
    "c.1874_1875del"
  ],
  "c.1977_1986del": [
    "4.7369567894801664e-06",
    "No",
    "c.1977_1986del",
    "p.Asn659LysfsX10",
    "CF-causing",
    "2109-2118del10",
    "1"
  ],
  "p.Asn659LysfsX10": [
    "4.7369567894801664e-06",
    "No",
    "c.1977_1986del",
    "p.Asn659LysfsX10",
    "CF-causing",
    "2109-2118del10",
    "1"
  ],
  "2109-2118del10": [
    "4.7369567894801664e-06",
    "No",
    "c.1977_1986del",
    "p.Asn659LysfsX10",
    "CF-causing",
    "2109-2118del10",
    "1"
  ],
  "p.Thr663ProfsX21": [
    "p.Thr663ProfsX21",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "2118del14",
    "1",
    "c.1987_2000del"
  ],
  "2118del14": [
    "p.Thr663ProfsX21",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "2118del14",
    "1",
    "c.1987_2000del"
  ],
  "c.1987_2000del": [
    "p.Thr663ProfsX21",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "2118del14",
    "1",
    "c.1987_2000del"
  ],
  "2132delAC": [
    "4.7369567894801664e-06",
    "2132delAC",
    "No",
    "p.His667ProfsX21",
    "CF-causing",
    "1",
    "c.2000_2001del"
  ],
  "p.His667ProfsX21": [
    "4.7369567894801664e-06",
    "2132delAC",
    "No",
    "p.His667ProfsX21",
    "CF-causing",
    "1",
    "c.2000_2001del"
  ],
  "c.2000_2001del": [
    "4.7369567894801664e-06",
    "2132delAC",
    "No",
    "p.His667ProfsX21",
    "CF-causing",
    "1",
    "c.2000_2001del"
  ],
  "c.2044dup": [
    "4.7369567894801664e-06",
    "No",
    "c.2044dup",
    "2175insA",
    "CF-causing",
    "1",
    "p.Thr682AsnfsX7"
  ],
  "2175insA": [
    "4.7369567894801664e-06",
    "No",
    "c.2044dup",
    "2175insA",
    "CF-causing",
    "1",
    "p.Thr682AsnfsX7"
  ],
  "p.Thr682AsnfsX7": [
    "4.7369567894801664e-06",
    "No",
    "c.2044dup",
    "2175insA",
    "CF-causing",
    "1",
    "p.Thr682AsnfsX7"
  ],
  "c.2277del": [
    "4.7369567894801664e-06",
    "c.2277del",
    "No",
    "CF-causing",
    "2409delC",
    "1",
    "p.Thr760ArgfsX11"
  ],
  "2409delC": [
    "4.7369567894801664e-06",
    "c.2277del",
    "No",
    "CF-causing",
    "2409delC",
    "1",
    "p.Thr760ArgfsX11"
  ],
  "2435insC": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "1",
    "2435insC",
    "p.Val769CysfsX10",
    "c.2303dup"
  ],
  "p.Val769CysfsX10": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "1",
    "2435insC",
    "p.Val769CysfsX10",
    "c.2303dup"
  ],
  "c.2303dup": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "1",
    "2435insC",
    "p.Val769CysfsX10",
    "c.2303dup"
  ],
  "2456delAC": [
    "4.7369567894801664e-06",
    "2456delAC",
    "No",
    "c.2324_2325del",
    "CF-causing",
    "1",
    "p.His775LeufsX3"
  ],
  "c.2324_2325del": [
    "4.7369567894801664e-06",
    "2456delAC",
    "No",
    "c.2324_2325del",
    "CF-causing",
    "1",
    "p.His775LeufsX3"
  ],
  "p.His775LeufsX3": [
    "4.7369567894801664e-06",
    "2456delAC",
    "No",
    "c.2324_2325del",
    "CF-causing",
    "1",
    "p.His775LeufsX3"
  ],
  "2512delG": [
    "4.7369567894801664e-06",
    "No",
    "2512delG",
    "CF-causing",
    "1",
    "p.Val794CysfsX9",
    "c.2380del"
  ],
  "p.Val794CysfsX9": [
    "4.7369567894801664e-06",
    "No",
    "2512delG",
    "CF-causing",
    "1",
    "p.Val794CysfsX9",
    "c.2380del"
  ],
  "c.2380del": [
    "4.7369567894801664e-06",
    "No",
    "2512delG",
    "CF-causing",
    "1",
    "p.Val794CysfsX9",
    "c.2380del"
  ],
  "c.2454_2455insT": [
    "c.2454_2455insT",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "2586-2687insT",
    "1",
    "p.Glu819X"
  ],
  "2586-2687insT": [
    "c.2454_2455insT",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "2586-2687insT",
    "1",
    "p.Glu819X"
  ],
  "p.Glu819X": [
    "c.2454_2455insT",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "2586-2687insT",
    "1",
    "p.Glu819X"
  ],
  "2747delC": [
    "4.7369567894801664e-06",
    "No",
    "2747delC",
    "c.2615del",
    "CF-causing",
    "p.Ala872GlufsX34",
    "1"
  ],
  "c.2615del": [
    "4.7369567894801664e-06",
    "No",
    "2747delC",
    "c.2615del",
    "CF-causing",
    "p.Ala872GlufsX34",
    "1"
  ],
  "p.Ala872GlufsX34": [
    "4.7369567894801664e-06",
    "No",
    "2747delC",
    "c.2615del",
    "CF-causing",
    "p.Ala872GlufsX34",
    "1"
  ],
  "p.Ser911ArgfsX64": [
    "4.7369567894801664e-06",
    "No",
    "p.Ser911ArgfsX64",
    "CF-causing",
    "1",
    "c.2732_2733insA"
  ],
  "c.2732_2733insA": [
    "4.7369567894801664e-06",
    "No",
    "p.Ser911ArgfsX64",
    "CF-causing",
    "1",
    "c.2732_2733insA"
  ],
  "p.Ser912IlefsX63": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "p.Ser912IlefsX63",
    "c.2733_2734insA",
    "1",
    "c.2733insA"
  ],
  "c.2733_2734insA": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "p.Ser912IlefsX63",
    "c.2733_2734insA",
    "1",
    "c.2733insA"
  ],
  "c.2733insA": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "p.Ser912IlefsX63",
    "c.2733_2734insA",
    "1",
    "c.2733insA"
  ],
  "c.2803_2813del": [
    "4.7369567894801664e-06",
    "No",
    "c.2803_2813del",
    "CF-causing",
    "2935del11",
    "1",
    "p.Leu935AlafsX36"
  ],
  "2935del11": [
    "4.7369567894801664e-06",
    "No",
    "c.2803_2813del",
    "CF-causing",
    "2935del11",
    "1",
    "p.Leu935AlafsX36"
  ],
  "p.Leu935AlafsX36": [
    "4.7369567894801664e-06",
    "No",
    "c.2803_2813del",
    "CF-causing",
    "2935del11",
    "1",
    "p.Leu935AlafsX36"
  ],
  "p.His939LeufsX3": [
    "4.7369567894801664e-06",
    "p.His939LeufsX3",
    "No",
    "CF-causing",
    "1",
    "2948delA",
    "c.2816del"
  ],
  "2948delA": [
    "4.7369567894801664e-06",
    "p.His939LeufsX3",
    "No",
    "CF-causing",
    "1",
    "2948delA",
    "c.2816del"
  ],
  "c.2816del": [
    "4.7369567894801664e-06",
    "p.His939LeufsX3",
    "No",
    "CF-causing",
    "1",
    "2948delA",
    "c.2816del"
  ],
  "2951insA": [
    "4.7369567894801664e-06",
    "No",
    "2951insA",
    "p.Leu941SerfsX34",
    "c.2819_2820insA",
    "CF-causing",
    "1"
  ],
  "p.Leu941SerfsX34": [
    "4.7369567894801664e-06",
    "No",
    "2951insA",
    "p.Leu941SerfsX34",
    "c.2819_2820insA",
    "CF-causing",
    "1"
  ],
  "c.2819_2820insA": [
    "4.7369567894801664e-06",
    "No",
    "2951insA",
    "p.Leu941SerfsX34",
    "c.2819_2820insA",
    "CF-causing",
    "1"
  ],
  "p.Ala96SerfsX15": [
    "4.7369567894801664e-06",
    "p.Ala96SerfsX15",
    "No",
    "c.285dup",
    "415insA",
    "CF-causing",
    "1"
  ],
  "c.285dup": [
    "4.7369567894801664e-06",
    "p.Ala96SerfsX15",
    "No",
    "c.285dup",
    "415insA",
    "CF-causing",
    "1"
  ],
  "415insA": [
    "4.7369567894801664e-06",
    "p.Ala96SerfsX15",
    "No",
    "c.285dup",
    "415insA",
    "CF-causing",
    "1"
  ],
  "p.Pro960LeufsX8": [
    "4.7369567894801664e-06",
    "No",
    "p.Pro960LeufsX8",
    "CF-causing",
    "c.2879del",
    "1",
    "3011delC"
  ],
  "c.2879del": [
    "4.7369567894801664e-06",
    "No",
    "p.Pro960LeufsX8",
    "CF-causing",
    "c.2879del",
    "1",
    "3011delC"
  ],
  "3011delC": [
    "4.7369567894801664e-06",
    "No",
    "p.Pro960LeufsX8",
    "CF-causing",
    "c.2879del",
    "1",
    "3011delC"
  ],
  "p.Thr963ValfsX13": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "p.Thr963ValfsX13",
    "3015_3018dupGTCA",
    "1",
    "c.2883_2886dup"
  ],
  "3015_3018dupGTCA": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "p.Thr963ValfsX13",
    "3015_3018dupGTCA",
    "1",
    "c.2883_2886dup"
  ],
  "c.2883_2886dup": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "p.Thr963ValfsX13",
    "3015_3018dupGTCA",
    "1",
    "c.2883_2886dup"
  ],
  "3029delC": [
    "4.7369567894801664e-06",
    "3029delC",
    "No",
    "CF-causing",
    "1",
    "c.2897del",
    "p.Thr966SerfsX2"
  ],
  "c.2897del": [
    "4.7369567894801664e-06",
    "3029delC",
    "No",
    "CF-causing",
    "1",
    "c.2897del",
    "p.Thr966SerfsX2"
  ],
  "p.Thr966SerfsX2": [
    "4.7369567894801664e-06",
    "3029delC",
    "No",
    "CF-causing",
    "1",
    "c.2897del",
    "p.Thr966SerfsX2"
  ],
  "3031-3032delinsA": [
    "3031-3032delinsA",
    "4.7369567894801664e-06",
    "No",
    "c.2899_2900delinsA",
    "CF-causing",
    "1",
    "p.Leu967ArgfsX14"
  ],
  "c.2899_2900delinsA": [
    "3031-3032delinsA",
    "4.7369567894801664e-06",
    "No",
    "c.2899_2900delinsA",
    "CF-causing",
    "1",
    "p.Leu967ArgfsX14"
  ],
  "p.Leu967ArgfsX14": [
    "3031-3032delinsA",
    "4.7369567894801664e-06",
    "No",
    "c.2899_2900delinsA",
    "CF-causing",
    "1",
    "p.Leu967ArgfsX14"
  ],
  "c.3081dup": [
    "4.7369567894801664e-06",
    "No",
    "c.3081dup",
    "CF-causing",
    "p.Met1028TyrfsX19",
    "1",
    "3213-3214insT"
  ],
  "p.Met1028TyrfsX19": [
    "4.7369567894801664e-06",
    "No",
    "c.3081dup",
    "CF-causing",
    "p.Met1028TyrfsX19",
    "1",
    "3213-3214insT"
  ],
  "3213-3214insT": [
    "4.7369567894801664e-06",
    "No",
    "c.3081dup",
    "CF-causing",
    "p.Met1028TyrfsX19",
    "1",
    "3213-3214insT"
  ],
  "p.Thr1036ProfsX24": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "p.Thr1036ProfsX24",
    "1",
    "3238delA",
    "c.3106del"
  ],
  "3238delA": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "p.Thr1036ProfsX24",
    "1",
    "3238delA",
    "c.3106del"
  ],
  "c.3106del": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "p.Thr1036ProfsX24",
    "1",
    "3238delA",
    "c.3106del"
  ],
  "p.Arg1097GlnfsX2": [
    "4.7369567894801664e-06",
    "No",
    "p.Arg1097GlnfsX2",
    "CF-causing",
    "3422del16",
    "1",
    "c.3290_3305del"
  ],
  "3422del16": [
    "4.7369567894801664e-06",
    "No",
    "p.Arg1097GlnfsX2",
    "CF-causing",
    "3422del16",
    "1",
    "c.3290_3305del"
  ],
  "c.3290_3305del": [
    "4.7369567894801664e-06",
    "No",
    "p.Arg1097GlnfsX2",
    "CF-causing",
    "3422del16",
    "1",
    "c.3290_3305del"
  ],
  "3425delG": [
    "3425delG",
    "p.Trp1098CysfsX4",
    "4.7369567894801664e-06",
    "c.3294del",
    "No",
    "CF-causing",
    "1"
  ],
  "p.Trp1098CysfsX4": [
    "3425delG",
    "p.Trp1098CysfsX4",
    "4.7369567894801664e-06",
    "c.3294del",
    "No",
    "CF-causing",
    "1"
  ],
  "c.3294del": [
    "3425delG",
    "p.Trp1098CysfsX4",
    "4.7369567894801664e-06",
    "c.3294del",
    "No",
    "CF-causing",
    "1"
  ],
  "c.3315del": [
    "4.7369567894801664e-06",
    "No",
    "c.3315del",
    "CF-causing",
    "p.Met1105IlefsX16",
    "1",
    "3447delG"
  ],
  "p.Met1105IlefsX16": [
    "4.7369567894801664e-06",
    "No",
    "c.3315del",
    "CF-causing",
    "p.Met1105IlefsX16",
    "1",
    "3447delG"
  ],
  "3447delG": [
    "4.7369567894801664e-06",
    "No",
    "c.3315del",
    "CF-causing",
    "p.Met1105IlefsX16",
    "1",
    "3447delG"
  ],
  "p.Val1129TyrfsX25": [
    "4.7369567894801664e-06",
    "No",
    "p.Val1129TyrfsX25",
    "CF-causing",
    "3516del5",
    "c.3384_3388del",
    "1"
  ],
  "3516del5": [
    "4.7369567894801664e-06",
    "No",
    "p.Val1129TyrfsX25",
    "CF-causing",
    "3516del5",
    "c.3384_3388del",
    "1"
  ],
  "c.3384_3388del": [
    "4.7369567894801664e-06",
    "No",
    "p.Val1129TyrfsX25",
    "CF-causing",
    "3516del5",
    "c.3384_3388del",
    "1"
  ],
  "c.3421_3424dup": [
    "4.7369567894801664e-06",
    "No",
    "c.3421_3424dup",
    "CF-causing",
    "1",
    "p.Thr1142LysfsX15",
    "3556insAGTA"
  ],
  "p.Thr1142LysfsX15": [
    "4.7369567894801664e-06",
    "No",
    "c.3421_3424dup",
    "CF-causing",
    "1",
    "p.Thr1142LysfsX15",
    "3556insAGTA"
  ],
  "3556insAGTA": [
    "4.7369567894801664e-06",
    "No",
    "c.3421_3424dup",
    "CF-causing",
    "1",
    "p.Thr1142LysfsX15",
    "3556insAGTA"
  ],
  "c.3539_3554del": [
    "4.7369567894801664e-06",
    "No",
    "c.3539_3554del",
    "CF-causing",
    "1",
    "p.Lys1180ThrfsX7"
  ],
  "p.Lys1180ThrfsX7": [
    "4.7369567894801664e-06",
    "No",
    "c.3539_3554del",
    "CF-causing",
    "1",
    "p.Lys1180ThrfsX7"
  ],
  "3731-3732AA->G": [
    "3731-3732AA->G",
    "4.7369567894801664e-06",
    "No",
    "p.Lys1200ArgfsX11",
    "CF-causing",
    "1",
    "c.3599_3600delinsG"
  ],
  "p.Lys1200ArgfsX11": [
    "3731-3732AA->G",
    "4.7369567894801664e-06",
    "No",
    "p.Lys1200ArgfsX11",
    "CF-causing",
    "1",
    "c.3599_3600delinsG"
  ],
  "c.3599_3600delinsG": [
    "3731-3732AA->G",
    "4.7369567894801664e-06",
    "No",
    "p.Lys1200ArgfsX11",
    "CF-causing",
    "1",
    "c.3599_3600delinsG"
  ],
  "3755dupG": [
    "4.7369567894801664e-06",
    "No",
    "3755dupG",
    "p.Gln1209ProfsX56",
    "CF-causing",
    "c.3623dup",
    "1"
  ],
  "p.Gln1209ProfsX56": [
    "4.7369567894801664e-06",
    "No",
    "3755dupG",
    "p.Gln1209ProfsX56",
    "CF-causing",
    "c.3623dup",
    "1"
  ],
  "c.3623dup": [
    "4.7369567894801664e-06",
    "No",
    "3755dupG",
    "p.Gln1209ProfsX56",
    "CF-causing",
    "c.3623dup",
    "1"
  ],
  "c.3658dup": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "c.3658dup",
    "1",
    "p.Thr1220AsnfsX45",
    "3789insA"
  ],
  "p.Thr1220AsnfsX45": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "c.3658dup",
    "1",
    "p.Thr1220AsnfsX45",
    "3789insA"
  ],
  "3789insA": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "c.3658dup",
    "1",
    "p.Thr1220AsnfsX45",
    "3789insA"
  ],
  "p.Leu123ProfsX36": [
    "4.7369567894801664e-06",
    "p.Leu123ProfsX36",
    "No",
    "c.367dup",
    "CF-causing",
    "1",
    "499dupC"
  ],
  "c.367dup": [
    "4.7369567894801664e-06",
    "p.Leu123ProfsX36",
    "No",
    "c.367dup",
    "CF-causing",
    "1",
    "499dupC"
  ],
  "499dupC": [
    "4.7369567894801664e-06",
    "p.Leu123ProfsX36",
    "No",
    "c.367dup",
    "CF-causing",
    "1",
    "499dupC"
  ],
  "c.3724del": [
    "4.7369567894801664e-06",
    "No",
    "c.3724del",
    "CF-causing",
    "1",
    "3856delC",
    "p.Leu1242SerfsX17"
  ],
  "3856delC": [
    "4.7369567894801664e-06",
    "No",
    "c.3724del",
    "CF-causing",
    "1",
    "3856delC",
    "p.Leu1242SerfsX17"
  ],
  "p.Leu1242SerfsX17": [
    "4.7369567894801664e-06",
    "No",
    "c.3724del",
    "CF-causing",
    "1",
    "3856delC",
    "p.Leu1242SerfsX17"
  ],
  "p.Thr1252AsnfsX13": [
    "4.7369567894801664e-06",
    "No",
    "p.Thr1252AsnfsX13",
    "CF-causing",
    "1",
    "c.3754dup",
    "3886insA"
  ],
  "c.3754dup": [
    "4.7369567894801664e-06",
    "No",
    "p.Thr1252AsnfsX13",
    "CF-causing",
    "1",
    "c.3754dup",
    "3886insA"
  ],
  "3886insA": [
    "4.7369567894801664e-06",
    "No",
    "p.Thr1252AsnfsX13",
    "CF-causing",
    "1",
    "c.3754dup",
    "3886insA"
  ],
  "p.Leu1253PhefsX12": [
    "4.7369567894801664e-06",
    "No",
    "p.Leu1253PhefsX12",
    "3889dupT",
    "CF-causing",
    "c.3758dup",
    "1"
  ],
  "3889dupT": [
    "4.7369567894801664e-06",
    "No",
    "p.Leu1253PhefsX12",
    "3889dupT",
    "CF-causing",
    "c.3758dup",
    "1"
  ],
  "c.3758dup": [
    "4.7369567894801664e-06",
    "No",
    "p.Leu1253PhefsX12",
    "3889dupT",
    "CF-causing",
    "c.3758dup",
    "1"
  ],
  "3898insC": [
    "4.7369567894801664e-06",
    "3898insC",
    "No",
    "CF-causing",
    "1",
    "p.Leu1258PhefsX7",
    "c.3767dup"
  ],
  "c.3767dup": [
    "4.7369567894801664e-06",
    "3898insC",
    "No",
    "CF-causing",
    "1",
    "p.Leu1258PhefsX7",
    "c.3767dup"
  ],
  "c.3773del": [
    "c.3773del",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "1",
    "p.Leu1258X",
    "3905delT"
  ],
  "p.Leu1258X": [
    "c.3773del",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "1",
    "p.Leu1258X",
    "3905delT"
  ],
  "3905delT": [
    "c.3773del",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "1",
    "p.Leu1258X",
    "3905delT"
  ],
  "c.3827del": [
    "c.3827del",
    "4.7369567894801664e-06",
    "No",
    "3959delC",
    "CF-causing",
    "1",
    "p.Ser1276X"
  ],
  "3959delC": [
    "c.3827del",
    "4.7369567894801664e-06",
    "No",
    "3959delC",
    "CF-causing",
    "1",
    "p.Ser1276X"
  ],
  "p.Ser1276X": [
    "c.3827del",
    "4.7369567894801664e-06",
    "No",
    "3959delC",
    "CF-causing",
    "1",
    "p.Ser1276X"
  ],
  "c.3829del": [
    "4.7369567894801664e-06",
    "No",
    "c.3829del",
    "3960-3961delA",
    "CF-causing",
    "1",
    "p.Ile1277X"
  ],
  "3960-3961delA": [
    "4.7369567894801664e-06",
    "No",
    "c.3829del",
    "3960-3961delA",
    "CF-causing",
    "1",
    "p.Ile1277X"
  ],
  "p.Ile1277X": [
    "4.7369567894801664e-06",
    "No",
    "c.3829del",
    "3960-3961delA",
    "CF-causing",
    "1",
    "p.Ile1277X"
  ],
  "p.Asp1320MetfsX8": [
    "4.7369567894801664e-06",
    "No",
    "p.Asp1320MetfsX8",
    "c.3957del",
    "CF-causing",
    "1",
    "4089delA"
  ],
  "c.3957del": [
    "4.7369567894801664e-06",
    "No",
    "p.Asp1320MetfsX8",
    "c.3957del",
    "CF-causing",
    "1",
    "4089delA"
  ],
  "4089delA": [
    "4.7369567894801664e-06",
    "No",
    "p.Asp1320MetfsX8",
    "c.3957del",
    "CF-causing",
    "1",
    "4089delA"
  ],
  "c.4033_4034del": [
    "4.7369567894801664e-06",
    "No",
    "c.4033_4034del",
    "4165delGT",
    "CF-causing",
    "1",
    "p.Val1345ProfsX13"
  ],
  "4165delGT": [
    "4.7369567894801664e-06",
    "No",
    "c.4033_4034del",
    "4165delGT",
    "CF-causing",
    "1",
    "p.Val1345ProfsX13"
  ],
  "p.Val1345ProfsX13": [
    "4.7369567894801664e-06",
    "No",
    "c.4033_4034del",
    "4165delGT",
    "CF-causing",
    "1",
    "p.Val1345ProfsX13"
  ],
  "c.4065_4066del": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "c.4065_4066del",
    "1",
    "p.Leu1356GlyfsX2",
    "4197_4198delCT"
  ],
  "p.Leu1356GlyfsX2": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "c.4065_4066del",
    "1",
    "p.Leu1356GlyfsX2",
    "4197_4198delCT"
  ],
  "4197_4198delCT": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "c.4065_4066del",
    "1",
    "p.Leu1356GlyfsX2",
    "4197_4198delCT"
  ],
  "p.Arg1358AsnfsX22": [
    "4.7369567894801664e-06",
    "No",
    "p.Arg1358AsnfsX22",
    "CF-causing",
    "c.4071_4073delinsAA",
    "1",
    "4203TAG->AA"
  ],
  "c.4071_4073delinsAA": [
    "4.7369567894801664e-06",
    "No",
    "p.Arg1358AsnfsX22",
    "CF-causing",
    "c.4071_4073delinsAA",
    "1",
    "4203TAG->AA"
  ],
  "4203TAG->AA": [
    "4.7369567894801664e-06",
    "No",
    "p.Arg1358AsnfsX22",
    "CF-causing",
    "c.4071_4073delinsAA",
    "1",
    "4203TAG->AA"
  ],
  "c.450dup": [
    "c.450dup",
    "4.7369567894801664e-06",
    "No",
    "p.Gln151AlafsX8",
    "CF-causing",
    "1",
    "582insG"
  ],
  "p.Gln151AlafsX8": [
    "c.450dup",
    "4.7369567894801664e-06",
    "No",
    "p.Gln151AlafsX8",
    "CF-causing",
    "1",
    "582insG"
  ],
  "582insG": [
    "c.450dup",
    "4.7369567894801664e-06",
    "No",
    "p.Gln151AlafsX8",
    "CF-causing",
    "1",
    "582insG"
  ],
  "605insT": [
    "605insT",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "1",
    "p.Leu159PhefsX4",
    "c.476dup"
  ],
  "p.Leu159PhefsX4": [
    "605insT",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "1",
    "p.Leu159PhefsX4",
    "c.476dup"
  ],
  "c.476dup": [
    "605insT",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "1",
    "p.Leu159PhefsX4",
    "c.476dup"
  ],
  "746insC": [
    "746insC",
    "4.7369567894801664e-06",
    "No",
    "c.614dup",
    "CF-causing",
    "p.Leu206PhefsX52",
    "1"
  ],
  "c.614dup": [
    "746insC",
    "4.7369567894801664e-06",
    "No",
    "c.614dup",
    "CF-causing",
    "p.Leu206PhefsX52",
    "1"
  ],
  "p.Leu206PhefsX52": [
    "746insC",
    "4.7369567894801664e-06",
    "No",
    "c.614dup",
    "CF-causing",
    "p.Leu206PhefsX52",
    "1"
  ],
  "c.773del": [
    "4.7369567894801664e-06",
    "No",
    "c.773del",
    "CF-causing",
    "1",
    "p.Arg258AsnfsX3",
    "905delG"
  ],
  "p.Arg258AsnfsX3": [
    "4.7369567894801664e-06",
    "No",
    "c.773del",
    "CF-causing",
    "1",
    "p.Arg258AsnfsX3",
    "905delG"
  ],
  "905delG": [
    "4.7369567894801664e-06",
    "No",
    "c.773del",
    "CF-causing",
    "1",
    "p.Arg258AsnfsX3",
    "905delG"
  ],
  "c.905_906insA": [
    "4.7369567894801664e-06",
    "c.905_906insA",
    "No",
    "CF-causing",
    "p.Arg303GlufsX5",
    "1",
    "1037insA"
  ],
  "p.Arg303GlufsX5": [
    "4.7369567894801664e-06",
    "c.905_906insA",
    "No",
    "CF-causing",
    "p.Arg303GlufsX5",
    "1",
    "1037insA"
  ],
  "1037insA": [
    "4.7369567894801664e-06",
    "c.905_906insA",
    "No",
    "CF-causing",
    "p.Arg303GlufsX5",
    "1",
    "1037insA"
  ],
  "1040del4": [
    "4.7369567894801664e-06",
    "No",
    "1040del4",
    "c.908_911del",
    "CF-causing",
    "p.Arg303ThrfsX24",
    "1"
  ],
  "c.908_911del": [
    "4.7369567894801664e-06",
    "No",
    "1040del4",
    "c.908_911del",
    "CF-causing",
    "p.Arg303ThrfsX24",
    "1"
  ],
  "p.Arg303ThrfsX24": [
    "4.7369567894801664e-06",
    "No",
    "1040del4",
    "c.908_911del",
    "CF-causing",
    "p.Arg303ThrfsX24",
    "1"
  ],
  "c.982delA": [
    "4.7369567894801664e-06",
    "c.982delA",
    "No",
    "c.982del",
    "p.Ile328SerfsX41",
    "CF-causing",
    "1"
  ],
  "c.982del": [
    "4.7369567894801664e-06",
    "c.982delA",
    "No",
    "c.982del",
    "p.Ile328SerfsX41",
    "CF-causing",
    "1"
  ],
  "p.Ile328SerfsX41": [
    "4.7369567894801664e-06",
    "c.982delA",
    "No",
    "c.982del",
    "p.Ile328SerfsX41",
    "CF-causing",
    "1"
  ],
  "c.1053_1054del": [
    "c.1053_1054del",
    "4.7369567894801664e-06",
    "No",
    "1185delTC",
    "p.Arg352AlafsX11",
    "CF-causing",
    "1"
  ],
  "1185delTC": [
    "c.1053_1054del",
    "4.7369567894801664e-06",
    "No",
    "1185delTC",
    "p.Arg352AlafsX11",
    "CF-causing",
    "1"
  ],
  "p.Arg352AlafsX11": [
    "c.1053_1054del",
    "4.7369567894801664e-06",
    "No",
    "1185delTC",
    "p.Arg352AlafsX11",
    "CF-causing",
    "1"
  ],
  "c.177dup": [
    "4.7369567894801664e-06",
    "c.177dup",
    "No",
    "p.Glu60ArgfsX9",
    "CF-causing",
    "308insA",
    "1"
  ],
  "p.Glu60ArgfsX9": [
    "4.7369567894801664e-06",
    "c.177dup",
    "No",
    "p.Glu60ArgfsX9",
    "CF-causing",
    "308insA",
    "1"
  ],
  "308insA": [
    "4.7369567894801664e-06",
    "c.177dup",
    "No",
    "p.Glu60ArgfsX9",
    "CF-causing",
    "308insA",
    "1"
  ],
  "2222delG": [
    "4.7369567894801664e-06",
    "No",
    "2222delG",
    "c.2091del",
    "CF-causing",
    "1",
    "p.Lys698ArgfsX24"
  ],
  "c.2091del": [
    "4.7369567894801664e-06",
    "No",
    "2222delG",
    "c.2091del",
    "CF-causing",
    "1",
    "p.Lys698ArgfsX24"
  ],
  "p.Lys698ArgfsX24": [
    "4.7369567894801664e-06",
    "No",
    "2222delG",
    "c.2091del",
    "CF-causing",
    "1",
    "p.Lys698ArgfsX24"
  ],
  "p.Glu831GlyfsX5": [
    "p.Glu831GlyfsX5",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "c.2489dup",
    "1",
    "c.2489_2490insA"
  ],
  "c.2489dup": [
    "p.Glu831GlyfsX5",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "c.2489dup",
    "1",
    "c.2489_2490insA"
  ],
  "c.2489_2490insA": [
    "p.Glu831GlyfsX5",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "c.2489dup",
    "1",
    "c.2489_2490insA"
  ],
  "2694delT": [
    "2694delT",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "1",
    "c.2562del",
    "p.Val855SerfsX5"
  ],
  "c.2562del": [
    "2694delT",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "1",
    "c.2562del",
    "p.Val855SerfsX5"
  ],
  "p.Val855SerfsX5": [
    "2694delT",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "1",
    "c.2562del",
    "p.Val855SerfsX5"
  ],
  "2777insTG": [
    "4.7369567894801664e-06",
    "No",
    "2777insTG",
    "c.2644_2645dup",
    "CF-causing",
    "1",
    "p.Trp882CysfsX25"
  ],
  "c.2644_2645dup": [
    "4.7369567894801664e-06",
    "No",
    "2777insTG",
    "c.2644_2645dup",
    "CF-causing",
    "1",
    "p.Trp882CysfsX25"
  ],
  "p.Trp882CysfsX25": [
    "4.7369567894801664e-06",
    "No",
    "2777insTG",
    "c.2644_2645dup",
    "CF-causing",
    "1",
    "p.Trp882CysfsX25"
  ],
  "2909delT": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "2909delT",
    "p.Leu926CysfsX16",
    "1",
    "c.2777del"
  ],
  "p.Leu926CysfsX16": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "2909delT",
    "p.Leu926CysfsX16",
    "1",
    "c.2777del"
  ],
  "c.2777del": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "2909delT",
    "p.Leu926CysfsX16",
    "1",
    "c.2777del"
  ],
  "p.Gly1003GlufsX3": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "p.Gly1003GlufsX3",
    "3139delG",
    "1",
    "c.3008del"
  ],
  "3139delG": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "p.Gly1003GlufsX3",
    "3139delG",
    "1",
    "c.3008del"
  ],
  "c.3008del": [
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "p.Gly1003GlufsX3",
    "3139delG",
    "1",
    "c.3008del"
  ],
  "3456delC": [
    "4.7369567894801664e-06",
    "No",
    "3456delC",
    "c.3324del",
    "CF-causing",
    "1",
    "p.Ile1109SerfsX12"
  ],
  "c.3324del": [
    "4.7369567894801664e-06",
    "No",
    "3456delC",
    "c.3324del",
    "CF-causing",
    "1",
    "p.Ile1109SerfsX12"
  ],
  "p.Phe1166SerfsX26": [
    "4.7369567894801664e-06",
    "p.Phe1166SerfsX26",
    "No",
    "c.3497del",
    "CF-causing",
    "1",
    "3629delT"
  ],
  "c.3497del": [
    "4.7369567894801664e-06",
    "p.Phe1166SerfsX26",
    "No",
    "c.3497del",
    "CF-causing",
    "1",
    "3629delT"
  ],
  "3629delT": [
    "4.7369567894801664e-06",
    "p.Phe1166SerfsX26",
    "No",
    "c.3497del",
    "CF-causing",
    "1",
    "3629delT"
  ],
  "c.3592del": [
    "4.7369567894801664e-06",
    "No",
    "c.3592del",
    "3724delG",
    "CF-causing",
    "p.Val1198X",
    "1"
  ],
  "3724delG": [
    "4.7369567894801664e-06",
    "No",
    "c.3592del",
    "3724delG",
    "CF-causing",
    "p.Val1198X",
    "1"
  ],
  "p.Val1198X": [
    "4.7369567894801664e-06",
    "No",
    "c.3592del",
    "3724delG",
    "CF-causing",
    "p.Val1198X",
    "1"
  ],
  "c.3708del": [
    "4.7369567894801664e-06",
    "No",
    "c.3708del",
    "CF-causing",
    "1",
    "3840delT",
    "p.Gly1237AlafsX22"
  ],
  "3840delT": [
    "4.7369567894801664e-06",
    "No",
    "c.3708del",
    "CF-causing",
    "1",
    "3840delT",
    "p.Gly1237AlafsX22"
  ],
  "p.Gly1237AlafsX22": [
    "4.7369567894801664e-06",
    "No",
    "c.3708del",
    "CF-causing",
    "1",
    "3840delT",
    "p.Gly1237AlafsX22"
  ],
  "p.Val1293TyrfsX35": [
    "4.7369567894801664e-06",
    "p.Val1293TyrfsX35",
    "No",
    "4006delA",
    "CF-causing",
    "1",
    "c.3876del"
  ],
  "4006delA": [
    "4.7369567894801664e-06",
    "p.Val1293TyrfsX35",
    "No",
    "4006delA",
    "CF-causing",
    "1",
    "c.3876del"
  ],
  "c.3876del": [
    "4.7369567894801664e-06",
    "p.Val1293TyrfsX35",
    "No",
    "4006delA",
    "CF-causing",
    "1",
    "c.3876del"
  ],
  "p.Leu130SerfsX4": [
    "4.7369567894801664e-06",
    "No",
    "p.Leu130SerfsX4",
    "c.387del",
    "519delT",
    "CF-causing",
    "1"
  ],
  "c.387del": [
    "4.7369567894801664e-06",
    "No",
    "p.Leu130SerfsX4",
    "c.387del",
    "519delT",
    "CF-causing",
    "1"
  ],
  "519delT": [
    "4.7369567894801664e-06",
    "No",
    "p.Leu130SerfsX4",
    "c.387del",
    "519delT",
    "CF-causing",
    "1"
  ],
  "c.4040_4041del": [
    "c.4040_4041del",
    "4.7369567894801664e-06",
    "No",
    "4172delGC",
    "p.Ser1347ThrfsX11",
    "CF-causing",
    "1"
  ],
  "4172delGC": [
    "c.4040_4041del",
    "4.7369567894801664e-06",
    "No",
    "4172delGC",
    "p.Ser1347ThrfsX11",
    "CF-causing",
    "1"
  ],
  "p.Ser1347ThrfsX11": [
    "c.4040_4041del",
    "4.7369567894801664e-06",
    "No",
    "4172delGC",
    "p.Ser1347ThrfsX11",
    "CF-causing",
    "1"
  ],
  "936delTA": [
    "4.7369567894801664e-06",
    "936delTA",
    "No",
    "c.805_806del",
    "p.Ile269ProfsX4",
    "CF-causing",
    "1"
  ],
  "c.805_806del": [
    "4.7369567894801664e-06",
    "936delTA",
    "No",
    "c.805_806del",
    "p.Ile269ProfsX4",
    "CF-causing",
    "1"
  ],
  "p.Ile269ProfsX4": [
    "4.7369567894801664e-06",
    "936delTA",
    "No",
    "c.805_806del",
    "p.Ile269ProfsX4",
    "CF-causing",
    "1"
  ],
  "c.87dup": [
    "4.7369567894801664e-06",
    "No",
    "c.87dup",
    "CF-causing",
    "218insA",
    "1",
    "p.Gln30ThrfsX15"
  ],
  "218insA": [
    "4.7369567894801664e-06",
    "No",
    "c.87dup",
    "CF-causing",
    "218insA",
    "1",
    "p.Gln30ThrfsX15"
  ],
  "p.Gln30ThrfsX15": [
    "4.7369567894801664e-06",
    "No",
    "c.87dup",
    "CF-causing",
    "218insA",
    "1",
    "p.Gln30ThrfsX15"
  ],
  "c.1360_1387del": [
    "4.7369567894801664e-06",
    "No",
    "c.1360_1387del",
    "1491-1500del",
    "CF-causing",
    "1",
    "p.Leu454AlafsX6"
  ],
  "1491-1500del": [
    "4.7369567894801664e-06",
    "No",
    "c.1360_1387del",
    "1491-1500del",
    "CF-causing",
    "1",
    "p.Leu454AlafsX6"
  ],
  "p.Leu454AlafsX6": [
    "4.7369567894801664e-06",
    "No",
    "c.1360_1387del",
    "1491-1500del",
    "CF-causing",
    "1",
    "p.Leu454AlafsX6"
  ],
  "p.Ala1391HisfsX7": [
    "4.7369567894801664e-06",
    "p.Ala1391HisfsX7",
    "No",
    "CF-causing",
    "4301delA",
    "1",
    "c.4170del"
  ],
  "4301delA": [
    "4.7369567894801664e-06",
    "p.Ala1391HisfsX7",
    "No",
    "CF-causing",
    "4301delA",
    "1",
    "c.4170del"
  ],
  "c.4170del": [
    "4.7369567894801664e-06",
    "p.Ala1391HisfsX7",
    "No",
    "CF-causing",
    "4301delA",
    "1",
    "c.4170del"
  ],
  "749delT": [
    "4.7369567894801664e-06",
    "No",
    "749delT",
    "CF-causing",
    "c.617del",
    "p.Leu206CysfsX9",
    "1"
  ],
  "c.617del": [
    "4.7369567894801664e-06",
    "No",
    "749delT",
    "CF-causing",
    "c.617del",
    "p.Leu206CysfsX9",
    "1"
  ],
  "p.Leu206CysfsX9": [
    "4.7369567894801664e-06",
    "No",
    "749delT",
    "CF-causing",
    "c.617del",
    "p.Leu206CysfsX9",
    "1"
  ],
  "c.234delC": [
    "c.234delC",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "1",
    "p.Trp79GlyfsX12",
    "c.234del"
  ],
  "p.Trp79GlyfsX12": [
    "c.234delC",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "1",
    "p.Trp79GlyfsX12",
    "c.234del"
  ],
  "c.234del": [
    "c.234delC",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "1",
    "p.Trp79GlyfsX12",
    "c.234del"
  ],
  "p.Tyr1307ProfsX22": [
    "4.7369567894801664e-06",
    "No",
    "p.Tyr1307ProfsX22",
    "CF-causing",
    "4048insCC",
    "c.3917_3918dup",
    "1"
  ],
  "4048insCC": [
    "4.7369567894801664e-06",
    "No",
    "p.Tyr1307ProfsX22",
    "CF-causing",
    "4048insCC",
    "c.3917_3918dup",
    "1"
  ],
  "c.3917_3918dup": [
    "4.7369567894801664e-06",
    "No",
    "p.Tyr1307ProfsX22",
    "CF-causing",
    "4048insCC",
    "c.3917_3918dup",
    "1"
  ],
  "T388X": [
    "4.7369567894801664e-06",
    "No",
    "T388X",
    "CF-causing",
    "c.1162_1163delinsTA",
    "p.Thr388X",
    "1"
  ],
  "c.1162_1163delinsTA": [
    "4.7369567894801664e-06",
    "No",
    "T388X",
    "CF-causing",
    "c.1162_1163delinsTA",
    "p.Thr388X",
    "1"
  ],
  "p.Thr388X": [
    "4.7369567894801664e-06",
    "No",
    "T388X",
    "CF-causing",
    "c.1162_1163delinsTA",
    "p.Thr388X",
    "1"
  ],
  "p.Lys716X": [
    "p.Lys716X",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "1",
    "c.2145_2146delinsGT|c.2146A>T",
    "K716X"
  ],
  "c.2145_2146delinsGT|c.2146A>T": [
    "p.Lys716X",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "1",
    "c.2145_2146delinsGT|c.2146A>T",
    "K716X"
  ],
  "K716X": [
    "p.Lys716X",
    "4.7369567894801664e-06",
    "No",
    "CF-causing",
    "1",
    "c.2145_2146delinsGT|c.2146A>T",
    "K716X"
  ],
  "c.2655_2657+13del": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "c.2655_2657+13del",
    "CF-causing",
    "2787del16",
    "1"
  ],
  "2787del16": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "c.2655_2657+13del",
    "CF-causing",
    "2787del16",
    "1"
  ],
  "c.2982_2988+2delCATCCAGGT": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "CF-causing",
    "c.2982_2988+2delCATCCAGGT",
    "1",
    "c.2982_2988+2del"
  ],
  "c.2982_2988+2del": [
    "4.7369567894801664e-06",
    "p.?",
    "No",
    "CF-causing",
    "c.2982_2988+2delCATCCAGGT",
    "1",
    "c.2982_2988+2del"
  ],
  "M1K": [
    "4.7369567894801664e-06",
    "M1K",
    "p.?",
    "No",
    "CF-causing",
    "1",
    "c.2T>A"
  ],
  "c.2T>A": [
    "4.7369567894801664e-06",
    "M1K",
    "p.?",
    "No",
    "CF-causing",
    "1",
    "c.2T>A"
  ],
  "CF-causing - previously called c.3033dup": [
    "4.7369567894801664e-06",
    "CF-causing - previously called c.3033dup",
    "No",
    "CF-causing",
    "3165dupA",
    "1",
    "p.Gln1012ThrfsX35",
    "c.3033dup"
  ],
  "3165dupA": [
    "4.7369567894801664e-06",
    "CF-causing - previously called c.3033dup",
    "No",
    "CF-causing",
    "3165dupA",
    "1",
    "p.Gln1012ThrfsX35",
    "c.3033dup"
  ],
  "p.Gln1012ThrfsX35": [
    "4.7369567894801664e-06",
    "CF-causing - previously called c.3033dup",
    "No",
    "CF-causing",
    "3165dupA",
    "1",
    "p.Gln1012ThrfsX35",
    "c.3033dup"
  ],
  "c.3033dup": [
    "CF-causing (now renamed 3165dupA)",
    "c.3033dup",
    "No, but renamed",
    "(CF-causing under new name)"
  ],
  "c.3139+1G>T": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "c.3139+1G>T",
    "CF-causing",
    "3271+1G->T",
    "1"
  ],
  "3271+1G->T": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "c.3139+1G>T",
    "CF-causing",
    "3271+1G->T",
    "1"
  ],
  "1248+1G->T": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "1248+1G->T",
    "c.1116+1G>T"
  ],
  "c.1116+1G>T": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "1248+1G->T",
    "c.1116+1G>T"
  ],
  "1248+2T->C": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "1248+2T->C",
    "c.1116+2T>C"
  ],
  "c.1116+2T>C": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "1248+2T->C",
    "c.1116+2T>C"
  ],
  "3500-2A->T": [
    "4.7369567894801664e-06",
    "p.?",
    "3500-2A->T",
    "Yes, new variant added",
    "CF-causing",
    "c.3368-2A>T",
    "1"
  ],
  "c.3368-2A>T": [
    "4.7369567894801664e-06",
    "p.?",
    "3500-2A->T",
    "Yes, new variant added",
    "CF-causing",
    "c.3368-2A>T",
    "1"
  ],
  "c.2908+1G>T": [
    "c.2908+1G>T",
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "3040+1G->T",
    "1"
  ],
  "3040+1G->T": [
    "c.2908+1G>T",
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "3040+1G->T",
    "1"
  ],
  "1248+2T->A": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "1248+2T->A",
    "CF-causing",
    "1",
    "c.1116+2T>A"
  ],
  "c.1116+2T>A": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "1248+2T->A",
    "CF-causing",
    "1",
    "c.1116+2T>A"
  ],
  "c.1209+2T>A": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "c.1209+2T>A",
    "1",
    "1341+2T->A"
  ],
  "1341+2T->A": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "c.1209+2T>A",
    "1",
    "1341+2T->A"
  ],
  "1342-1G->A": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "1342-1G->A",
    "1",
    "c.1210-1G>A"
  ],
  "c.1210-1G>A": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "1342-1G->A",
    "1",
    "c.1210-1G>A"
  ],
  "c.1393-1G>C": [
    "4.7369567894801664e-06",
    "c.1393-1G>C",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "1525-1G->C",
    "1"
  ],
  "1525-1G->C": [
    "4.7369567894801664e-06",
    "c.1393-1G>C",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "1525-1G->C",
    "1"
  ],
  "1525-1G->T": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "1525-1G->T",
    "c.1393-1G>T",
    "CF-causing",
    "1"
  ],
  "c.1393-1G>T": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "1525-1G->T",
    "c.1393-1G>T",
    "CF-causing",
    "1"
  ],
  "c.1584+1G>T": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.1584+1G>T",
    "1716+1G->T"
  ],
  "1716+1G->T": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.1584+1G>T",
    "1716+1G->T"
  ],
  "296+2T->A": [
    "4.7369567894801664e-06",
    "296+2T->A",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.164+2T>A"
  ],
  "c.164+2T>A": [
    "4.7369567894801664e-06",
    "296+2T->A",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.164+2T>A"
  ],
  "1899-1G->A": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "1899-1G->A",
    "CF-causing",
    "c.1767-1G>A",
    "1"
  ],
  "c.1767-1G>A": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "1899-1G->A",
    "CF-causing",
    "c.1767-1G>A",
    "1"
  ],
  "c.1767-2A>G": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "c.1767-2A>G",
    "1898-2A->G",
    "1"
  ],
  "1898-2A->G": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "c.1767-2A>G",
    "1898-2A->G",
    "1"
  ],
  "2623-1G->C": [
    "4.7369567894801664e-06",
    "p.?",
    "2623-1G->C",
    "c.2491-1G>C",
    "Yes, new variant added",
    "CF-causing",
    "1"
  ],
  "c.2491-1G>C": [
    "4.7369567894801664e-06",
    "p.?",
    "2623-1G->C",
    "c.2491-1G>C",
    "Yes, new variant added",
    "CF-causing",
    "1"
  ],
  "2751+1G->A": [
    "2751+1G->A",
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "c.2619+1G>A",
    "1"
  ],
  "c.2619+1G>A": [
    "2751+1G->A",
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "c.2619+1G>A",
    "1"
  ],
  "c.2658-1G>T": [
    "4.7369567894801664e-06",
    "p.?",
    "c.2658-1G>T",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "2790-1G->T"
  ],
  "2790-1G->T": [
    "4.7369567894801664e-06",
    "p.?",
    "c.2658-1G>T",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "2790-1G->T"
  ],
  "c.2988+1G>C": [
    "4.7369567894801664e-06",
    "c.2988+1G>C",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "3120+1G->C"
  ],
  "3120+1G->C": [
    "4.7369567894801664e-06",
    "c.2988+1G>C",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "3120+1G->C"
  ],
  "c.3139+1G>C": [
    "c.3139+1G>C",
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "3271+1G->C",
    "CF-causing",
    "1"
  ],
  "3271+1G->C": [
    "c.3139+1G>C",
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "3271+1G->C",
    "CF-causing",
    "1"
  ],
  "c.3469-1G>T": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "c.3469-1G>T",
    "1",
    "3601-1G->T"
  ],
  "3601-1G->T": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "c.3469-1G>T",
    "1",
    "3601-1G->T"
  ],
  "c.3469-2A>C": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "c.3469-2A>C",
    "3601-2A->C",
    "CF-causing",
    "1"
  ],
  "3601-2A->C": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "c.3469-2A>C",
    "3601-2A->C",
    "CF-causing",
    "1"
  ],
  "c.3874-2A>G": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "c.3874-2A>G",
    "CF-causing",
    "1",
    "4006-2A->G"
  ],
  "4006-2A->G": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "c.3874-2A>G",
    "CF-causing",
    "1",
    "4006-2A->G"
  ],
  "c.4136+2T>G": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "c.4136+2T>G",
    "CF-causing",
    "1",
    "4268+2T->G"
  ],
  "4268+2T->G": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "c.4136+2T>G",
    "CF-causing",
    "1",
    "4268+2T->G"
  ],
  "c.490-1G>T": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "c.490-1G>T",
    "CF-causing",
    "622-1G->T",
    "1"
  ],
  "622-1G->T": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "c.490-1G>T",
    "CF-causing",
    "622-1G->T",
    "1"
  ],
  "875+2T->A": [
    "4.7369567894801664e-06",
    "p.?",
    "875+2T->A",
    "Yes, new variant added",
    "CF-causing",
    "c.743+2T>A",
    "1"
  ],
  "c.743+2T>A": [
    "4.7369567894801664e-06",
    "p.?",
    "875+2T->A",
    "Yes, new variant added",
    "CF-causing",
    "c.743+2T>A",
    "1"
  ],
  "1002-2A->C": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "1002-2A->C",
    "CF-causing",
    "1",
    "c.870-2A>C"
  ],
  "c.870-2A>C": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "1002-2A->C",
    "CF-causing",
    "1",
    "c.870-2A>C"
  ],
  "c.3873+1G>T": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "c.3873+1G>T",
    "1",
    "4005+1G->T"
  ],
  "4005+1G->T": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "c.3873+1G>T",
    "1",
    "4005+1G->T"
  ],
  "c.1210-2_1210-1del": [
    "c.1210-2_1210-1del",
    "4.7369567894801664e-06",
    "p.?",
    "1342-2delAG",
    "Yes, new variant added",
    "CF-causing",
    "1"
  ],
  "1342-2delAG": [
    "c.1210-2_1210-1del",
    "4.7369567894801664e-06",
    "p.?",
    "1342-2delAG",
    "Yes, new variant added",
    "CF-causing",
    "1"
  ],
  "c.1871_1878del": [
    "4.7369567894801664e-06",
    "c.1871_1878del",
    "Yes, new variant added",
    "2003del8",
    "CF-causing",
    "1",
    "p.Ser624IlefsX15"
  ],
  "2003del8": [
    "4.7369567894801664e-06",
    "c.1871_1878del",
    "Yes, new variant added",
    "2003del8",
    "CF-causing",
    "1",
    "p.Ser624IlefsX15"
  ],
  "p.Ser624IlefsX15": [
    "4.7369567894801664e-06",
    "c.1871_1878del",
    "Yes, new variant added",
    "2003del8",
    "CF-causing",
    "1",
    "p.Ser624IlefsX15"
  ],
  "c.1904del": [
    "4.7369567894801664e-06",
    "c.1904del",
    "Yes, new variant added",
    "p.Asn635IlefsX28",
    "CF-causing",
    "1",
    "2036delA"
  ],
  "p.Asn635IlefsX28": [
    "4.7369567894801664e-06",
    "c.1904del",
    "Yes, new variant added",
    "p.Asn635IlefsX28",
    "CF-causing",
    "1",
    "2036delA"
  ],
  "2036delA": [
    "4.7369567894801664e-06",
    "c.1904del",
    "Yes, new variant added",
    "p.Asn635IlefsX28",
    "CF-causing",
    "1",
    "2036delA"
  ],
  "2967delG": [
    "2967delG",
    "4.7369567894801664e-06",
    "p.Ile947PhefsX21",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.2835del"
  ],
  "p.Ile947PhefsX21": [
    "4.7369567894801664e-06",
    "p.Ile947PhefsX21",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.2839delA",
    "c.2839del"
  ],
  "c.2835del": [
    "2967delG",
    "4.7369567894801664e-06",
    "p.Ile947PhefsX21",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.2835del"
  ],
  "p.Gly1298GlufsX30": [
    "p.Gly1298GlufsX30",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "c.3893delG",
    "1",
    "c.3893del"
  ],
  "c.3893delG": [
    "p.Gly1298GlufsX30",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "c.3893delG",
    "1",
    "c.3893del"
  ],
  "c.3893del": [
    "p.Gly1298GlufsX30",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "c.3893delG",
    "1",
    "c.3893del"
  ],
  "c.3380_3383del": [
    "c.3380_3383del",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "p.Gly1127GlufsX6"
  ],
  "p.Gly1127GlufsX6": [
    "c.3380_3383del",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "p.Gly1127GlufsX6"
  ],
  "1200_1219del20": [
    "4.7369567894801664e-06",
    "1200_1219del20",
    "Yes, new variant added",
    "p.Trp356X",
    "c.1068_1087del",
    "CF-causing",
    "1"
  ],
  "c.1068_1087del": [
    "4.7369567894801664e-06",
    "1200_1219del20",
    "Yes, new variant added",
    "p.Trp356X",
    "c.1068_1087del",
    "CF-causing",
    "1"
  ],
  "1204_1205delGT": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "1204_1205delGT",
    "CF-causing",
    "c.1072_1073del",
    "1"
  ],
  "c.1072_1073del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "1204_1205delGT",
    "CF-causing",
    "c.1072_1073del",
    "1"
  ],
  "1212delA": [
    "4.7369567894801664e-06",
    "1212delA",
    "Yes, new variant added",
    "c.1080del",
    "CF-causing",
    "1",
    "p.Trp361GlyfsX8"
  ],
  "c.1080del": [
    "4.7369567894801664e-06",
    "1212delA",
    "Yes, new variant added",
    "c.1080del",
    "CF-causing",
    "1",
    "p.Trp361GlyfsX8"
  ],
  "c.1115delA": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.1115delA",
    "p.Gln372ArgfsX16",
    "c.1115del",
    "CF-causing",
    "1"
  ],
  "p.Gln372ArgfsX16": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.1115delA",
    "p.Gln372ArgfsX16",
    "c.1115del",
    "CF-causing",
    "1"
  ],
  "c.1115del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.1115delA",
    "p.Gln372ArgfsX16",
    "c.1115del",
    "CF-causing",
    "1"
  ],
  "c.1190dupT": [
    "c.1190dupT",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Thr398AsnfsX13",
    "c.1190dup",
    "CF-causing",
    "1"
  ],
  "p.Thr398AsnfsX13": [
    "c.1190dupT",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Thr398AsnfsX13",
    "c.1190dup",
    "CF-causing",
    "1"
  ],
  "c.1190dup": [
    "c.1190dupT",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Thr398AsnfsX13",
    "c.1190dup",
    "CF-causing",
    "1"
  ],
  "p.Glu403GlyfsX39": [
    "4.7369567894801664e-06",
    "p.Glu403GlyfsX39",
    "Yes, new variant added",
    "1340delA",
    "c.1208del",
    "CF-causing",
    "1"
  ],
  "1340delA": [
    "4.7369567894801664e-06",
    "p.Glu403GlyfsX39",
    "Yes, new variant added",
    "1340delA",
    "c.1208del",
    "CF-causing",
    "1"
  ],
  "c.1208del": [
    "4.7369567894801664e-06",
    "p.Glu403GlyfsX39",
    "Yes, new variant added",
    "1340delA",
    "c.1208del",
    "CF-causing",
    "1"
  ],
  "c.1244delA": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.1244delA",
    "c.1244del",
    "CF-causing",
    "p.Asn415ThrfsX27",
    "1"
  ],
  "c.1244del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.1244delA",
    "c.1244del",
    "CF-causing",
    "p.Asn415ThrfsX27",
    "1"
  ],
  "p.Asn415ThrfsX27": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.1244delA",
    "c.1244del",
    "CF-causing",
    "p.Asn415ThrfsX27",
    "1"
  ],
  "c.1262del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.1262del",
    "CF-causing",
    "p.Thr421IlefsX21",
    "1",
    "c.1262delC"
  ],
  "p.Thr421IlefsX21": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.1262del",
    "CF-causing",
    "p.Thr421IlefsX21",
    "1",
    "c.1262delC"
  ],
  "c.1262delC": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.1262del",
    "CF-causing",
    "p.Thr421IlefsX21",
    "1",
    "c.1262delC"
  ],
  "c.147_150del": [
    "4.7369567894801664e-06",
    "c.147_150del",
    "p.Ser50LysfsX40",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.147_150delATCT"
  ],
  "p.Ser50LysfsX40": [
    "4.7369567894801664e-06",
    "c.147_150del",
    "p.Ser50LysfsX40",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.147_150delATCT"
  ],
  "c.147_150delATCT": [
    "4.7369567894801664e-06",
    "c.147_150del",
    "p.Ser50LysfsX40",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.147_150delATCT"
  ],
  "p.Trp496GlyfsX31": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "p.Trp496GlyfsX31",
    "c.1486del",
    "c.1486delT"
  ],
  "c.1486del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "p.Trp496GlyfsX31",
    "c.1486del",
    "c.1486delT"
  ],
  "c.1486delT": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "p.Trp496GlyfsX31",
    "c.1486del",
    "c.1486delT"
  ],
  "c.1547_1548del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.1547_1548del",
    "CF-causing",
    "1",
    "p.Arg516IlefsX51",
    "c.1547_1548delGA"
  ],
  "p.Arg516IlefsX51": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.1547_1548del",
    "CF-causing",
    "1",
    "p.Arg516IlefsX51",
    "c.1547_1548delGA"
  ],
  "c.1547_1548delGA": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.1547_1548del",
    "CF-causing",
    "1",
    "p.Arg516IlefsX51",
    "c.1547_1548delGA"
  ],
  "p.Glu528ArgfsX40": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "p.Glu528ArgfsX40",
    "c.1581dup",
    "c.1581dupA"
  ],
  "c.1581dup": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "p.Glu528ArgfsX40",
    "c.1581dup",
    "c.1581dupA"
  ],
  "c.1581dupA": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "p.Glu528ArgfsX40",
    "c.1581dup",
    "c.1581dupA"
  ],
  "p.Glu543LysfsX6": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Glu543LysfsX6",
    "c.1627del",
    "CF-causing",
    "1",
    "1759delG"
  ],
  "c.1627del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Glu543LysfsX6",
    "c.1627del",
    "CF-causing",
    "1",
    "1759delG"
  ],
  "1759delG": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Glu543LysfsX6",
    "c.1627del",
    "CF-causing",
    "1",
    "1759delG"
  ],
  "c.1652del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.1652del",
    "p.Gly551ValfsX8",
    "CF-causing",
    "1",
    "1784delG"
  ],
  "1784delG": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.1652del",
    "p.Gly551ValfsX8",
    "CF-causing",
    "1",
    "1784delG"
  ],
  "1807delG": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1807delG",
    "1",
    "c.1675del",
    "p.Ala559GlnfsX13"
  ],
  "c.1675del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1807delG",
    "1",
    "c.1675del",
    "p.Ala559GlnfsX13"
  ],
  "c.1725_1727delinsAT": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.1725_1727delinsAT",
    "CF-causing",
    "p.Phe575LeufsX4",
    "1"
  ],
  "p.Val580PhefsX2": [
    "4.7369567894801664e-06",
    "p.Val580PhefsX2",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.1738del",
    "1870delG"
  ],
  "c.1738del": [
    "4.7369567894801664e-06",
    "p.Val580PhefsX2",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.1738del",
    "1870delG"
  ],
  "1870delG": [
    "4.7369567894801664e-06",
    "p.Val580PhefsX2",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.1738del",
    "1870delG"
  ],
  "305insT": [
    "4.7369567894801664e-06",
    "305insT",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.174dup",
    "p.Arg59X"
  ],
  "c.174dup": [
    "4.7369567894801664e-06",
    "305insT",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.174dup",
    "p.Arg59X"
  ],
  "p.Arg59X": [
    "4.7369567894801664e-06",
    "305insT",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.174dup",
    "p.Arg59X"
  ],
  "c.1753delG": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "c.1753delG",
    "1",
    "p.Glu585LysfsX10",
    "c.1753del"
  ],
  "p.Glu585LysfsX10": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "c.1753delG",
    "1",
    "p.Glu585LysfsX10",
    "c.1753del"
  ],
  "c.1753del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "c.1753delG",
    "1",
    "p.Glu585LysfsX10",
    "c.1753del"
  ],
  "2025dupA": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "2025dupA",
    "p.Glu632ArgfsX10",
    "CF-causing",
    "1",
    "c.1893dup"
  ],
  "p.Glu632ArgfsX10": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "2025dupA",
    "p.Glu632ArgfsX10",
    "CF-causing",
    "1",
    "c.1893dup"
  ],
  "c.1893dup": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "2025dupA",
    "p.Glu632ArgfsX10",
    "CF-causing",
    "1",
    "c.1893dup"
  ],
  "p.Glu632ThrfsX9": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "p.Glu632ThrfsX9",
    "1",
    "c.1894_1895del"
  ],
  "c.1894_1895del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "p.Glu632ThrfsX9",
    "1",
    "c.1894_1895del"
  ],
  "p.Arg657LysfsX6": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "p.Arg657LysfsX6",
    "c.1970delG",
    "1",
    "c.1970del"
  ],
  "c.1970delG": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "p.Arg657LysfsX6",
    "c.1970delG",
    "1",
    "c.1970del"
  ],
  "c.1970del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "p.Arg657LysfsX6",
    "c.1970delG",
    "1",
    "c.1970del"
  ],
  "p.Ser678LeufsX10": [
    "4.7369567894801664e-06",
    "p.Ser678LeufsX10",
    "Yes, new variant added",
    "c.2032_2033del",
    "c.2032_2033delTC",
    "CF-causing",
    "1"
  ],
  "c.2032_2033del": [
    "4.7369567894801664e-06",
    "p.Ser678LeufsX10",
    "Yes, new variant added",
    "c.2032_2033del",
    "c.2032_2033delTC",
    "CF-causing",
    "1"
  ],
  "c.2032_2033delTC": [
    "4.7369567894801664e-06",
    "p.Ser678LeufsX10",
    "Yes, new variant added",
    "c.2032_2033del",
    "c.2032_2033delTC",
    "CF-causing",
    "1"
  ],
  "p.Lys684AsnfsX37": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "p.Lys684AsnfsX37",
    "1",
    "c.2052_2055del",
    "2184del4"
  ],
  "c.2052_2055del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "p.Lys684AsnfsX37",
    "1",
    "c.2052_2055del",
    "2184del4"
  ],
  "2184del4": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "p.Lys684AsnfsX37",
    "1",
    "c.2052_2055del",
    "2184del4"
  ],
  "c.2053delC": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "c.2053delC",
    "c.2053del",
    "1",
    "p.Gln685AsnfsX37"
  ],
  "c.2053del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "c.2053delC",
    "c.2053del",
    "1",
    "p.Gln685AsnfsX37"
  ],
  "p.Gln685AsnfsX37": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "c.2053delC",
    "c.2053del",
    "1",
    "p.Gln685AsnfsX37"
  ],
  "p.Lys688PhefsX2": [
    "4.7369567894801664e-06",
    "p.Lys688PhefsX2",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "2193ins4",
    "c.2058_2061dup"
  ],
  "2193ins4": [
    "4.7369567894801664e-06",
    "p.Lys688PhefsX2",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "2193ins4",
    "c.2058_2061dup"
  ],
  "c.2058_2061dup": [
    "4.7369567894801664e-06",
    "p.Lys688PhefsX2",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "2193ins4",
    "c.2058_2061dup"
  ],
  "p.Gln720LysfsX8": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Gln720LysfsX8",
    "CF-causing",
    "c.2158_2173del",
    "1",
    "2290del16"
  ],
  "c.2158_2173del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Gln720LysfsX8",
    "CF-causing",
    "c.2158_2173del",
    "1",
    "2290del16"
  ],
  "2290del16": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Gln720LysfsX8",
    "CF-causing",
    "c.2158_2173del",
    "1",
    "2290del16"
  ],
  "c.2250delT": [
    "4.7369567894801664e-06",
    "c.2250delT",
    "Yes, new variant added",
    "c.2250del",
    "CF-causing",
    "1",
    "p.Arg751AlafsX4"
  ],
  "c.2250del": [
    "4.7369567894801664e-06",
    "c.2250delT",
    "Yes, new variant added",
    "c.2250del",
    "CF-causing",
    "1",
    "p.Arg751AlafsX4"
  ],
  "p.Arg751AlafsX4": [
    "4.7369567894801664e-06",
    "c.2250delT",
    "Yes, new variant added",
    "c.2250del",
    "CF-causing",
    "1",
    "p.Arg751AlafsX4"
  ],
  "p.Arg766SerfsX5": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Arg766SerfsX5",
    "2429delG",
    "CF-causing",
    "1",
    "c.2298del"
  ],
  "2429delG": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Arg766SerfsX5",
    "2429delG",
    "CF-causing",
    "1",
    "c.2298del"
  ],
  "c.2298del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Arg766SerfsX5",
    "2429delG",
    "CF-causing",
    "1",
    "c.2298del"
  ],
  "p.Lys793SerfsX11": [
    "4.7369567894801664e-06",
    "p.Lys793SerfsX11",
    "Yes, new variant added",
    "2510delAA",
    "c.2378_2379del",
    "CF-causing",
    "1"
  ],
  "2510delAA": [
    "4.7369567894801664e-06",
    "p.Lys793SerfsX11",
    "Yes, new variant added",
    "2510delAA",
    "c.2378_2379del",
    "CF-causing",
    "1"
  ],
  "c.2378_2379del": [
    "4.7369567894801664e-06",
    "p.Lys793SerfsX11",
    "Yes, new variant added",
    "2510delAA",
    "c.2378_2379del",
    "CF-causing",
    "1"
  ],
  "p.Leu812TyrfsX10": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "p.Leu812TyrfsX10",
    "1",
    "c.2433_2437delinsATA"
  ],
  "c.2433_2437delinsATA": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "p.Leu812TyrfsX10",
    "1",
    "c.2433_2437delinsATA"
  ],
  "c.243delT": [
    "4.7369567894801664e-06",
    "c.243delT",
    "Yes, new variant added",
    "p.Phe81LeufsX10",
    "CF-causing",
    "1",
    "c.243del"
  ],
  "p.Phe81LeufsX10": [
    "4.7369567894801664e-06",
    "c.243delT",
    "Yes, new variant added",
    "p.Phe81LeufsX10",
    "CF-causing",
    "1",
    "c.243del"
  ],
  "c.243del": [
    "4.7369567894801664e-06",
    "c.243delT",
    "Yes, new variant added",
    "p.Phe81LeufsX10",
    "CF-causing",
    "1",
    "c.243del"
  ],
  "c.2467_2470delGAAA": [
    "c.2467_2470delGAAA",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Glu823LeufsX6",
    "CF-causing",
    "c.2467_2470del",
    "1"
  ],
  "p.Glu823LeufsX6": [
    "c.2467_2470delGAAA",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Glu823LeufsX6",
    "CF-causing",
    "c.2467_2470del",
    "1"
  ],
  "c.2467_2470del": [
    "c.2467_2470delGAAA",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Glu823LeufsX6",
    "CF-causing",
    "c.2467_2470del",
    "1"
  ],
  "379-381insT": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "379-381insT",
    "CF-causing",
    "c.248dup",
    "p.Tyr84LeufsX27",
    "1"
  ],
  "c.248dup": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "379-381insT",
    "CF-causing",
    "c.248dup",
    "p.Tyr84LeufsX27",
    "1"
  ],
  "p.Tyr84LeufsX27": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "379-381insT",
    "CF-causing",
    "c.248dup",
    "p.Tyr84LeufsX27",
    "1"
  ],
  "c.2493del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.2493del",
    "CF-causing",
    "1",
    "c.2493delG",
    "p.Glu831AspfsX13"
  ],
  "c.2493delG": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.2493del",
    "CF-causing",
    "1",
    "c.2493delG",
    "p.Glu831AspfsX13"
  ],
  "p.Glu831AspfsX13": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.2493del",
    "CF-causing",
    "1",
    "c.2493delG",
    "p.Glu831AspfsX13"
  ],
  "c.2540del": [
    "4.7369567894801664e-06",
    "c.2540del",
    "Yes, new variant added",
    "p.Asn847ThrfsX13",
    "CF-causing",
    "1",
    "2672delA"
  ],
  "p.Asn847ThrfsX13": [
    "4.7369567894801664e-06",
    "c.2540del",
    "Yes, new variant added",
    "p.Asn847ThrfsX13",
    "CF-causing",
    "1",
    "2672delA"
  ],
  "2672delA": [
    "4.7369567894801664e-06",
    "c.2540del",
    "Yes, new variant added",
    "p.Asn847ThrfsX13",
    "CF-causing",
    "1",
    "2672delA"
  ],
  "c.2573del": [
    "c.2573del",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.2573delG",
    "CF-causing",
    "1",
    "p.Ser858ThrfsX2"
  ],
  "c.2573delG": [
    "c.2573del",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.2573delG",
    "CF-causing",
    "1",
    "p.Ser858ThrfsX2"
  ],
  "p.Ser858ThrfsX2": [
    "c.2573del",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.2573delG",
    "CF-causing",
    "1",
    "p.Ser858ThrfsX2"
  ],
  "2737delA": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "2737delA",
    "CF-causing",
    "c.2605del",
    "p.Ile869PhefsX37",
    "1"
  ],
  "c.2605del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "2737delA",
    "CF-causing",
    "c.2605del",
    "p.Ile869PhefsX37",
    "1"
  ],
  "p.Ile869PhefsX37": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "2737delA",
    "CF-causing",
    "c.2605del",
    "p.Ile869PhefsX37",
    "1"
  ],
  "p.Phe916LeufsX58": [
    "4.7369567894801664e-06",
    "p.Phe916LeufsX58",
    "Yes, new variant added",
    "CF-causing",
    "c.2745_2746del",
    "1",
    "c.2745_2746delGT"
  ],
  "c.2745_2746del": [
    "4.7369567894801664e-06",
    "p.Phe916LeufsX58",
    "Yes, new variant added",
    "CF-causing",
    "c.2745_2746del",
    "1",
    "c.2745_2746delGT"
  ],
  "c.2745_2746delGT": [
    "4.7369567894801664e-06",
    "p.Phe916LeufsX58",
    "Yes, new variant added",
    "CF-causing",
    "c.2745_2746del",
    "1",
    "c.2745_2746delGT"
  ],
  "p.Thr940ValfsX30": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Thr940ValfsX30",
    "c.2818_2831del",
    "CF-causing",
    "1"
  ],
  "c.2818_2831del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Thr940ValfsX30",
    "c.2818_2831del",
    "CF-causing",
    "1"
  ],
  "c.2839delA": [
    "4.7369567894801664e-06",
    "p.Ile947PhefsX21",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.2839delA",
    "c.2839del"
  ],
  "c.2839del": [
    "4.7369567894801664e-06",
    "p.Ile947PhefsX21",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.2839delA",
    "c.2839del"
  ],
  "p.Leu948TyrfsX20": [
    "4.7369567894801664e-06",
    "p.Leu948TyrfsX20",
    "Yes, new variant added",
    "CF-causing",
    "2975delT",
    "1",
    "c.2843del"
  ],
  "2975delT": [
    "4.7369567894801664e-06",
    "p.Leu948TyrfsX20",
    "Yes, new variant added",
    "CF-causing",
    "2975delT",
    "1",
    "c.2843del"
  ],
  "c.2843del": [
    "4.7369567894801664e-06",
    "p.Leu948TyrfsX20",
    "Yes, new variant added",
    "CF-causing",
    "2975delT",
    "1",
    "c.2843del"
  ],
  "c.2909_2924dup16": [
    "4.7369567894801664e-06",
    "c.2909_2924dup16",
    "Yes, new variant added",
    "c.2909_2924dup",
    "CF-causing",
    "1",
    "p.Phe976TrpfsX4"
  ],
  "c.2909_2924dup": [
    "4.7369567894801664e-06",
    "c.2909_2924dup16",
    "Yes, new variant added",
    "c.2909_2924dup",
    "CF-causing",
    "1",
    "p.Phe976TrpfsX4"
  ],
  "p.Phe976TrpfsX4": [
    "4.7369567894801664e-06",
    "c.2909_2924dup16",
    "Yes, new variant added",
    "c.2909_2924dup",
    "CF-causing",
    "1",
    "p.Phe976TrpfsX4"
  ],
  "3090del4": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "3090del4",
    "1",
    "p.Pro988LeufsX11",
    "c.2958_2961del"
  ],
  "p.Pro988LeufsX11": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "3090del4",
    "1",
    "p.Pro988LeufsX11",
    "c.2958_2961del"
  ],
  "c.2958_2961del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "3090del4",
    "1",
    "p.Pro988LeufsX11",
    "c.2958_2961del"
  ],
  "c.2994del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.2994del",
    "3126delA",
    "p.Leu998PhefsX2"
  ],
  "3126delA": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.2994del",
    "3126delA",
    "p.Leu998PhefsX2"
  ],
  "p.Leu998PhefsX2": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.2994del",
    "3126delA",
    "p.Leu998PhefsX2"
  ],
  "3152delT": [
    "4.7369567894801664e-06",
    "p.Val1008SerfsX15",
    "Yes, new variant added",
    "3152delT",
    "CF-causing",
    "1",
    "c.3021del"
  ],
  "c.3021del": [
    "4.7369567894801664e-06",
    "p.Val1008SerfsX15",
    "Yes, new variant added",
    "3152delT",
    "CF-causing",
    "1",
    "c.3021del"
  ],
  "p.Gln1042ThrfsX5": [
    "4.7369567894801664e-06",
    "p.Gln1042ThrfsX5",
    "Yes, new variant added",
    "CF-causing",
    "Q1042TfsX5",
    "c.3123dup",
    "1"
  ],
  "Q1042TfsX5": [
    "4.7369567894801664e-06",
    "p.Gln1042ThrfsX5",
    "Yes, new variant added",
    "CF-causing",
    "Q1042TfsX5",
    "c.3123dup",
    "1"
  ],
  "c.3123dup": [
    "4.7369567894801664e-06",
    "p.Gln1042ThrfsX5",
    "Yes, new variant added",
    "CF-causing",
    "Q1042TfsX5",
    "c.3123dup",
    "1"
  ],
  "3359delC": [
    "4.7369567894801664e-06",
    "3359delC",
    "Yes, new variant added",
    "c.3227del",
    "CF-causing",
    "1",
    "p.Thr1076IlefsX7"
  ],
  "c.3227del": [
    "4.7369567894801664e-06",
    "3359delC",
    "Yes, new variant added",
    "c.3227del",
    "CF-causing",
    "1",
    "p.Thr1076IlefsX7"
  ],
  "p.Thr1076IlefsX7": [
    "4.7369567894801664e-06",
    "3359delC",
    "Yes, new variant added",
    "c.3227del",
    "CF-causing",
    "1",
    "p.Thr1076IlefsX7"
  ],
  "458delAT": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "p.Tyr109X",
    "1",
    "458delAT",
    "c.326_327del"
  ],
  "c.326_327del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "p.Tyr109X",
    "1",
    "458delAT",
    "c.326_327del"
  ],
  "3453delT": [
    "4.7369567894801664e-06",
    "3453delT",
    "Yes, new variant added",
    "p.Phe1107LeufsX14",
    "CF-causing",
    "c.3321del",
    "1"
  ],
  "p.Phe1107LeufsX14": [
    "4.7369567894801664e-06",
    "3453delT",
    "Yes, new variant added",
    "p.Phe1107LeufsX14",
    "CF-causing",
    "c.3321del",
    "1"
  ],
  "c.3321del": [
    "4.7369567894801664e-06",
    "3453delT",
    "Yes, new variant added",
    "p.Phe1107LeufsX14",
    "CF-causing",
    "c.3321del",
    "1"
  ],
  "p.Val1108CysfsX48": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Val1108CysfsX48",
    "c.3321dup",
    "CF-causing",
    "1"
  ],
  "c.3321dup": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Val1108CysfsX48",
    "c.3321dup",
    "CF-causing",
    "1"
  ],
  "p.Val1108HisfsX47": [
    "4.7369567894801664e-06",
    "p.Val1108HisfsX47",
    "Yes, new variant added",
    "c.3322_3323delGT",
    "c.3322_3323del",
    "CF-causing",
    "1"
  ],
  "c.3322_3323delGT": [
    "4.7369567894801664e-06",
    "p.Val1108HisfsX47",
    "Yes, new variant added",
    "c.3322_3323delGT",
    "c.3322_3323del",
    "CF-causing",
    "1"
  ],
  "c.3322_3323del": [
    "4.7369567894801664e-06",
    "p.Val1108HisfsX47",
    "Yes, new variant added",
    "c.3322_3323delGT",
    "c.3322_3323del",
    "CF-causing",
    "1"
  ],
  "p.Phe1116LeufsX40": [
    "4.7369567894801664e-06",
    "p.Phe1116LeufsX40",
    "Yes, new variant added",
    "c.3344_3345insA",
    "CF-causing",
    "1"
  ],
  "c.3344_3345insA": [
    "4.7369567894801664e-06",
    "p.Phe1116LeufsX40",
    "Yes, new variant added",
    "c.3344_3345insA",
    "CF-causing",
    "1"
  ],
  "c.3411_3414del": [
    "4.7369567894801664e-06",
    "c.3411_3414del",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.3411_3414delGAAT",
    "p.Met1137IlefsX3"
  ],
  "c.3411_3414delGAAT": [
    "4.7369567894801664e-06",
    "c.3411_3414del",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.3411_3414delGAAT",
    "p.Met1137IlefsX3"
  ],
  "p.Met1137IlefsX3": [
    "4.7369567894801664e-06",
    "c.3411_3414del",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.3411_3414delGAAT",
    "p.Met1137IlefsX3"
  ],
  "p.Ser1161GlyfsX30": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "p.Ser1161GlyfsX30",
    "1",
    "c.3481_3486delinsGG",
    "3613AGCCGA->GG"
  ],
  "c.3481_3486delinsGG": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "p.Ser1161GlyfsX30",
    "1",
    "c.3481_3486delinsGG",
    "3613AGCCGA->GG"
  ],
  "3613AGCCGA->GG": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "p.Ser1161GlyfsX30",
    "1",
    "c.3481_3486delinsGG",
    "3613AGCCGA->GG"
  ],
  "c.3524del": [
    "4.7369567894801664e-06",
    "c.3524del",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.3524delC",
    "p.Pro1175LeufsX17"
  ],
  "c.3524delC": [
    "4.7369567894801664e-06",
    "c.3524del",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.3524delC",
    "p.Pro1175LeufsX17"
  ],
  "p.Pro1175LeufsX17": [
    "4.7369567894801664e-06",
    "c.3524del",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.3524delC",
    "p.Pro1175LeufsX17"
  ],
  "p.Ser118LeufsX6": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "p.Ser118LeufsX6",
    "1",
    "c.353del",
    "c.353delC"
  ],
  "c.353del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "p.Ser118LeufsX6",
    "1",
    "c.353del",
    "c.353delC"
  ],
  "c.353delC": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "p.Ser118LeufsX6",
    "1",
    "c.353del",
    "c.353delC"
  ],
  "c.3563del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.3563del",
    "CF-causing",
    "3695delC",
    "1",
    "p.Ser1188X"
  ],
  "3695delC": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.3563del",
    "CF-causing",
    "3695delC",
    "1",
    "p.Ser1188X"
  ],
  "p.Ser1188X": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.3563del",
    "CF-causing",
    "3695delC",
    "1",
    "p.Ser1188X"
  ],
  "c.3569_3570del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.3569_3570del",
    "c.3569_3570delTT",
    "p.Val1190AspfsX4"
  ],
  "c.3569_3570delTT": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.3569_3570del",
    "c.3569_3570delTT",
    "p.Val1190AspfsX4"
  ],
  "p.Val1190AspfsX4": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.3569_3570del",
    "c.3569_3570delTT",
    "p.Val1190AspfsX4"
  ],
  "p.Arg1239GlyfsX20": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Arg1239GlyfsX20",
    "3847delA",
    "CF-causing",
    "1",
    "c.3715del"
  ],
  "3847delA": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Arg1239GlyfsX20",
    "3847delA",
    "CF-causing",
    "1",
    "c.3715del"
  ],
  "c.3715del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Arg1239GlyfsX20",
    "3847delA",
    "CF-causing",
    "1",
    "c.3715del"
  ],
  "p.Leu1254IlefsX10": [
    "p.Leu1254IlefsX10",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "3892delTT",
    "c.3760_3761del"
  ],
  "3892delTT": [
    "p.Leu1254IlefsX10",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "3892delTT",
    "c.3760_3761del"
  ],
  "c.3760_3761del": [
    "p.Leu1254IlefsX10",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "3892delTT",
    "c.3760_3761del"
  ],
  "c.381_382dup": [
    "4.7369567894801664e-06",
    "c.381_382dup",
    "Yes, new variant added",
    "p.Cys128TyrfsX7",
    "CF-causing",
    "1"
  ],
  "p.Cys128TyrfsX7": [
    "4.7369567894801664e-06",
    "c.381_382dup",
    "Yes, new variant added",
    "p.Cys128TyrfsX7",
    "CF-causing",
    "1"
  ],
  "c.3889delT": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.3889delT",
    "c.3889del",
    "p.Ser1297LeufsX31"
  ],
  "c.3889del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.3889delT",
    "c.3889del",
    "p.Ser1297LeufsX31"
  ],
  "p.Ser1297LeufsX31": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.3889delT",
    "c.3889del",
    "p.Ser1297LeufsX31"
  ],
  "526_527delAT": [
    "526_527delAT",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.394_398del",
    "CF-causing",
    "1",
    "p.Ile132GlufsX25"
  ],
  "c.394_398del": [
    "526_527delAT",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.394_398del",
    "CF-causing",
    "1",
    "p.Ile132GlufsX25"
  ],
  "p.Ile132GlufsX25": [
    "526_527delAT",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.394_398del",
    "CF-causing",
    "1",
    "p.Ile132GlufsX25"
  ],
  "c.3957_3958insAGGG": [
    "c.3957_3958insAGGG",
    "4.7369567894801664e-06",
    "p.Asp1320ArgfsX3",
    "Yes, new variant added",
    "4089ins4",
    "CF-causing",
    "1"
  ],
  "p.Asp1320ArgfsX3": [
    "c.3957_3958insAGGG",
    "4.7369567894801664e-06",
    "p.Asp1320ArgfsX3",
    "Yes, new variant added",
    "4089ins4",
    "CF-causing",
    "1"
  ],
  "4089ins4": [
    "c.3957_3958insAGGG",
    "4.7369567894801664e-06",
    "p.Asp1320ArgfsX3",
    "Yes, new variant added",
    "4089ins4",
    "CF-causing",
    "1"
  ],
  "p.Gln1330ValfsX6": [
    "p.Gln1330ValfsX6",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "4120delCA",
    "CF-causing",
    "1",
    "c.3988_3989del"
  ],
  "4120delCA": [
    "p.Gln1330ValfsX6",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "4120delCA",
    "CF-causing",
    "1",
    "c.3988_3989del"
  ],
  "c.3988_3989del": [
    "p.Gln1330ValfsX6",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "4120delCA",
    "CF-causing",
    "1",
    "c.3988_3989del"
  ],
  "p.Lys1334SerfsX13": [
    "4.7369567894801664e-06",
    "p.Lys1334SerfsX13",
    "Yes, new variant added",
    "c.3999delG",
    "CF-causing",
    "1",
    "c.3999del"
  ],
  "c.3999delG": [
    "4.7369567894801664e-06",
    "p.Lys1334SerfsX13",
    "Yes, new variant added",
    "c.3999delG",
    "CF-causing",
    "1",
    "c.3999del"
  ],
  "c.3999del": [
    "4.7369567894801664e-06",
    "p.Lys1334SerfsX13",
    "Yes, new variant added",
    "c.3999delG",
    "CF-causing",
    "1",
    "c.3999del"
  ],
  "c.4036dup": [
    "4.7369567894801664e-06",
    "c.4036dup",
    "Yes, new variant added",
    "c.4036dupC",
    "CF-causing",
    "1",
    "p.Leu1346ProfsX13"
  ],
  "c.4036dupC": [
    "4.7369567894801664e-06",
    "c.4036dup",
    "Yes, new variant added",
    "c.4036dupC",
    "CF-causing",
    "1",
    "p.Leu1346ProfsX13"
  ],
  "p.Leu1346ProfsX13": [
    "4.7369567894801664e-06",
    "c.4036dup",
    "Yes, new variant added",
    "c.4036dupC",
    "CF-causing",
    "1",
    "p.Leu1346ProfsX13"
  ],
  "c.4037_4041del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.4037_4041del",
    "4168delCTAAG",
    "p.Leu1346ProfsX11"
  ],
  "4168delCTAAG": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.4037_4041del",
    "4168delCTAAG",
    "p.Leu1346ProfsX11"
  ],
  "p.Leu1346ProfsX11": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.4037_4041del",
    "4168delCTAAG",
    "p.Leu1346ProfsX11"
  ],
  "p.Val1360PhefsX20": [
    "4.7369567894801664e-06",
    "p.Val1360PhefsX20",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.4078delG",
    "c.4078del"
  ],
  "c.4078delG": [
    "4.7369567894801664e-06",
    "p.Val1360PhefsX20",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.4078delG",
    "c.4078del"
  ],
  "c.4078del": [
    "4.7369567894801664e-06",
    "p.Val1360PhefsX20",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.4078delG",
    "c.4078del"
  ],
  "p.Leu1369ArgfsX16": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Leu1369ArgfsX16",
    "4237-4242delinsAGAA",
    "CF-causing",
    "1",
    "c.4105_4110delinsAGAA"
  ],
  "4237-4242delinsAGAA": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Leu1369ArgfsX16",
    "4237-4242delinsAGAA",
    "CF-causing",
    "1",
    "c.4105_4110delinsAGAA"
  ],
  "c.4105_4110delinsAGAA": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Leu1369ArgfsX16",
    "4237-4242delinsAGAA",
    "CF-causing",
    "1",
    "c.4105_4110delinsAGAA"
  ],
  "p.Leu1388ProfsX5": [
    "p.Leu1388ProfsX5",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "c.4163_4167del",
    "1",
    "c.4163_4167delTAAAA"
  ],
  "c.4163_4167del": [
    "p.Leu1388ProfsX5",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "c.4163_4167del",
    "1",
    "c.4163_4167delTAAAA"
  ],
  "c.4163_4167delTAAAA": [
    "p.Leu1388ProfsX5",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "c.4163_4167del",
    "1",
    "c.4163_4167delTAAAA"
  ],
  "c.43dupC": [
    "4.7369567894801664e-06",
    "c.43dupC",
    "Yes, new variant added",
    "c.43dup",
    "CF-causing",
    "1",
    "p.Leu15ProfsX30"
  ],
  "c.43dup": [
    "4.7369567894801664e-06",
    "c.43dupC",
    "Yes, new variant added",
    "c.43dup",
    "CF-causing",
    "1",
    "p.Leu15ProfsX30"
  ],
  "p.Leu15ProfsX30": [
    "4.7369567894801664e-06",
    "c.43dupC",
    "Yes, new variant added",
    "c.43dup",
    "CF-causing",
    "1",
    "p.Leu15ProfsX30"
  ],
  "p.Met150IlefsX3": [
    "4.7369567894801664e-06",
    "p.Met150IlefsX3",
    "Yes, new variant added",
    "c.450delG",
    "CF-causing",
    "1",
    "c.450del"
  ],
  "c.450delG": [
    "4.7369567894801664e-06",
    "p.Met150IlefsX3",
    "Yes, new variant added",
    "c.450delG",
    "CF-causing",
    "1",
    "c.450del"
  ],
  "c.450del": [
    "4.7369567894801664e-06",
    "p.Met150IlefsX3",
    "Yes, new variant added",
    "c.450delG",
    "CF-causing",
    "1",
    "c.450del"
  ],
  "583delC": [
    "4.7369567894801664e-06",
    "583delC",
    "Yes, new variant added",
    "p.Gln151ArgfsX2",
    "c.451del",
    "CF-causing",
    "1"
  ],
  "p.Gln151ArgfsX2": [
    "4.7369567894801664e-06",
    "583delC",
    "Yes, new variant added",
    "p.Gln151ArgfsX2",
    "c.451del",
    "CF-causing",
    "1"
  ],
  "c.451del": [
    "4.7369567894801664e-06",
    "583delC",
    "Yes, new variant added",
    "p.Gln151ArgfsX2",
    "c.451del",
    "CF-causing",
    "1"
  ],
  "c.560delA": [
    "4.7369567894801664e-06",
    "c.560delA",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "p.Asn187ThrfsX2",
    "c.560del"
  ],
  "p.Asn187ThrfsX2": [
    "4.7369567894801664e-06",
    "c.560delA",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "p.Asn187ThrfsX2",
    "c.560del"
  ],
  "c.560del": [
    "4.7369567894801664e-06",
    "c.560delA",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "p.Asn187ThrfsX2",
    "c.560del"
  ],
  "c.576del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.576del",
    "CF-causing",
    "p.Asp192GlufsX23",
    "1",
    "708delT"
  ],
  "p.Asp192GlufsX23": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.576del",
    "CF-causing",
    "p.Asp192GlufsX23",
    "1",
    "708delT"
  ],
  "708delT": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.576del",
    "CF-causing",
    "p.Asp192GlufsX23",
    "1",
    "708delT"
  ],
  "c.650_659del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "c.650_659del",
    "1",
    "p.Glu217GlyfsX11"
  ],
  "p.Glu217GlyfsX11": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "c.650_659del",
    "1",
    "p.Glu217GlyfsX11"
  ],
  "p.Leu24X": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Leu24X",
    "CF-causing",
    "1",
    "c.71_72delinsA",
    "c.71_72delTGinsA"
  ],
  "c.71_72delinsA": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Leu24X",
    "CF-causing",
    "1",
    "c.71_72delinsA",
    "c.71_72delTGinsA"
  ],
  "c.71_72delTGinsA": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Leu24X",
    "CF-causing",
    "1",
    "c.71_72delinsA",
    "c.71_72delTGinsA"
  ],
  "p.Gly239TrpfsX19": [
    "4.7369567894801664e-06",
    "p.Gly239TrpfsX19",
    "845_846insA",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.713_714insA"
  ],
  "845_846insA": [
    "4.7369567894801664e-06",
    "p.Gly239TrpfsX19",
    "845_846insA",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.713_714insA"
  ],
  "c.713_714insA": [
    "4.7369567894801664e-06",
    "p.Gly239TrpfsX19",
    "845_846insA",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.713_714insA"
  ],
  "p.Ser271LeufsX14": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Ser271LeufsX14",
    "CF-causing",
    "c.811del",
    "1",
    "c.811delT"
  ],
  "c.811del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Ser271LeufsX14",
    "CF-causing",
    "c.811del",
    "1",
    "c.811delT"
  ],
  "c.811delT": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "p.Ser271LeufsX14",
    "CF-causing",
    "c.811del",
    "1",
    "c.811delT"
  ],
  "c.865_869delAGACA": [
    "4.7369567894801664e-06",
    "c.865_869delAGACA",
    "Yes, new variant added",
    "CF-causing",
    "p.Arg289AsnfsX17",
    "c.865_869del",
    "1"
  ],
  "p.Arg289AsnfsX17": [
    "4.7369567894801664e-06",
    "c.865_869delAGACA",
    "Yes, new variant added",
    "CF-causing",
    "p.Arg289AsnfsX17",
    "c.865_869del",
    "1"
  ],
  "c.865_869del": [
    "4.7369567894801664e-06",
    "c.865_869delAGACA",
    "Yes, new variant added",
    "CF-causing",
    "p.Arg289AsnfsX17",
    "c.865_869del",
    "1"
  ],
  "c.912delinsGG": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.912delinsGG",
    "p.Tyr304X",
    "CF-causing",
    "1",
    "c.912delCinsGG"
  ],
  "c.912delCinsGG": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.912delinsGG",
    "p.Tyr304X",
    "CF-causing",
    "1",
    "c.912delCinsGG"
  ],
  "c.937_938del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.937_938del",
    "p.Ser313ArgfsX50",
    "CF-causing",
    "1",
    "c.937_938delTC"
  ],
  "p.Ser313ArgfsX50": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.937_938del",
    "p.Ser313ArgfsX50",
    "CF-causing",
    "1",
    "c.937_938delTC"
  ],
  "c.937_938delTC": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.937_938del",
    "p.Ser313ArgfsX50",
    "CF-causing",
    "1",
    "c.937_938delTC"
  ],
  "c.942delG": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "c.942delG",
    "c.942del",
    "1",
    "p.Phe315SerfsX13"
  ],
  "c.942del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "c.942delG",
    "c.942del",
    "1",
    "p.Phe315SerfsX13"
  ],
  "p.Phe315SerfsX13": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "c.942delG",
    "c.942del",
    "1",
    "p.Phe315SerfsX13"
  ],
  "c.972delC": [
    "4.7369567894801664e-06",
    "c.972delC",
    "Yes, new variant added",
    "p.Tyr325MetfsX3",
    "CF-causing",
    "1",
    "c.972del"
  ],
  "p.Tyr325MetfsX3": [
    "4.7369567894801664e-06",
    "c.972delC",
    "Yes, new variant added",
    "p.Tyr325MetfsX3",
    "CF-causing",
    "1",
    "c.972del"
  ],
  "c.972del": [
    "4.7369567894801664e-06",
    "c.972delC",
    "Yes, new variant added",
    "p.Tyr325MetfsX3",
    "CF-causing",
    "1",
    "c.972del"
  ],
  "c.991_995del": [
    "c.991_995del",
    "4.7369567894801664e-06",
    "p.Ile331ProfsX31",
    "Yes, new variant added",
    "CF-causing",
    "1"
  ],
  "p.Ile331ProfsX31": [
    "c.991_995del",
    "4.7369567894801664e-06",
    "p.Ile331ProfsX31",
    "Yes, new variant added",
    "CF-causing",
    "1"
  ],
  "p.Leu1227X": [
    "4.7369567894801664e-06",
    "p.Leu1227X",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.3678del",
    "c.3678delA"
  ],
  "c.3678del": [
    "4.7369567894801664e-06",
    "p.Leu1227X",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.3678del",
    "c.3678delA"
  ],
  "c.3678delA": [
    "4.7369567894801664e-06",
    "p.Leu1227X",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.3678del",
    "c.3678delA"
  ],
  "c.1530_1531del": [
    "4.7369567894801664e-06",
    "c.1530_1531del",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.1530_1531delTT",
    "p.Ser511LeufsX2"
  ],
  "c.1530_1531delTT": [
    "4.7369567894801664e-06",
    "c.1530_1531del",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.1530_1531delTT",
    "p.Ser511LeufsX2"
  ],
  "p.Ser511LeufsX2": [
    "4.7369567894801664e-06",
    "c.1530_1531del",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.1530_1531delTT",
    "p.Ser511LeufsX2"
  ],
  "c.2538delG": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.2538delG",
    "p.Trp846X",
    "CF-causing",
    "1",
    "c.2538del"
  ],
  "c.2538del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.2538delG",
    "p.Trp846X",
    "CF-causing",
    "1",
    "c.2538del"
  ],
  "3089insTC": [
    "3089insTC",
    "4.7369567894801664e-06",
    "c.2959_2960dup",
    "Yes, new variant added",
    "p.Pro988CysfsX13",
    "CF-causing",
    "1"
  ],
  "c.2959_2960dup": [
    "3089insTC",
    "4.7369567894801664e-06",
    "c.2959_2960dup",
    "Yes, new variant added",
    "p.Pro988CysfsX13",
    "CF-causing",
    "1"
  ],
  "p.Pro988CysfsX13": [
    "3089insTC",
    "4.7369567894801664e-06",
    "c.2959_2960dup",
    "Yes, new variant added",
    "p.Pro988CysfsX13",
    "CF-causing",
    "1"
  ],
  "1474delA": [
    "1474delA",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.1342del",
    "CF-causing",
    "1",
    "p.Ile448X"
  ],
  "c.1342del": [
    "1474delA",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.1342del",
    "CF-causing",
    "1",
    "p.Ile448X"
  ],
  "p.Ile448X": [
    "1474delA",
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.1342del",
    "CF-causing",
    "1",
    "p.Ile448X"
  ],
  "1784insATCAT": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1784insATCAT",
    "1",
    "p.Gln552SerfsX9",
    "c.1652_1653insATCAT"
  ],
  "p.Gln552SerfsX9": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1784insATCAT",
    "1",
    "p.Gln552SerfsX9",
    "c.1652_1653insATCAT"
  ],
  "c.1652_1653insATCAT": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1784insATCAT",
    "1",
    "p.Gln552SerfsX9",
    "c.1652_1653insATCAT"
  ],
  "c.1982del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.1982del",
    "2114delT",
    "p.Ile661ThrfsX2"
  ],
  "2114delT": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.1982del",
    "2114delT",
    "p.Ile661ThrfsX2"
  ],
  "p.Ile661ThrfsX2": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.1982del",
    "2114delT",
    "p.Ile661ThrfsX2"
  ],
  "c.2337del": [
    "4.7369567894801664e-06",
    "c.2337del",
    "p.Gly780ValfsX23",
    "Yes, new variant added",
    "CF-causing",
    "c.2337delA",
    "1"
  ],
  "p.Gly780ValfsX23": [
    "4.7369567894801664e-06",
    "c.2337del",
    "p.Gly780ValfsX23",
    "Yes, new variant added",
    "CF-causing",
    "c.2337delA",
    "1"
  ],
  "c.2337delA": [
    "4.7369567894801664e-06",
    "c.2337del",
    "p.Gly780ValfsX23",
    "Yes, new variant added",
    "CF-causing",
    "c.2337delA",
    "1"
  ],
  "c.2341delC": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.2341delC",
    "c.2341del",
    "CF-causing",
    "p.Gln781ArgfsX22",
    "1"
  ],
  "c.2341del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.2341delC",
    "c.2341del",
    "CF-causing",
    "p.Gln781ArgfsX22",
    "1"
  ],
  "p.Gln781ArgfsX22": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.2341delC",
    "c.2341del",
    "CF-causing",
    "p.Gln781ArgfsX22",
    "1"
  ],
  "c.264_268delATATT": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.264_268delATATT",
    "p.Leu88PhefsX21",
    "c.264_268del"
  ],
  "p.Leu88PhefsX21": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.264_268delATATT",
    "p.Leu88PhefsX21",
    "c.264_268del"
  ],
  "c.264_268del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "c.264_268delATATT",
    "p.Leu88PhefsX21",
    "c.264_268del"
  ],
  "c.2789delG": [
    "4.7369567894801664e-06",
    "c.2789delG",
    "p.Gly930AspfsX12",
    "Yes, new variant added",
    "CF-causing",
    "c.2789del",
    "1"
  ],
  "p.Gly930AspfsX12": [
    "4.7369567894801664e-06",
    "c.2789delG",
    "p.Gly930AspfsX12",
    "Yes, new variant added",
    "CF-causing",
    "c.2789del",
    "1"
  ],
  "c.2789del": [
    "4.7369567894801664e-06",
    "c.2789delG",
    "p.Gly930AspfsX12",
    "Yes, new variant added",
    "CF-causing",
    "c.2789del",
    "1"
  ],
  "3012delT": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "3012delT",
    "p.Met961CysfsX7",
    "c.2880del",
    "CF-causing",
    "1"
  ],
  "p.Met961CysfsX7": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "3012delT",
    "p.Met961CysfsX7",
    "c.2880del",
    "CF-causing",
    "1"
  ],
  "c.2880del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "3012delT",
    "p.Met961CysfsX7",
    "c.2880del",
    "CF-causing",
    "1"
  ],
  "p.Ala1067ProfsX16": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "p.Ala1067ProfsX16",
    "c.3199del",
    "1",
    "c.3199delG"
  ],
  "c.3199del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "p.Ala1067ProfsX16",
    "c.3199del",
    "1",
    "c.3199delG"
  ],
  "c.3199delG": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "p.Ala1067ProfsX16",
    "c.3199del",
    "1",
    "c.3199delG"
  ],
  "p.Val1212AlafsX16": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "p.Val1212AlafsX16",
    "1",
    "c.3635del",
    "c.3635delT"
  ],
  "c.3635del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "p.Val1212AlafsX16",
    "1",
    "c.3635del",
    "c.3635delT"
  ],
  "c.3635delT": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "p.Val1212AlafsX16",
    "1",
    "c.3635del",
    "c.3635delT"
  ],
  "p.His139LeufsX15": [
    "4.7369567894801664e-06",
    "p.His139LeufsX15",
    "Yes, new variant added",
    "CF-causing",
    "c.415_416insTA",
    "1",
    "547insTA"
  ],
  "c.415_416insTA": [
    "4.7369567894801664e-06",
    "p.His139LeufsX15",
    "Yes, new variant added",
    "CF-causing",
    "c.415_416insTA",
    "1",
    "547insTA"
  ],
  "547insTA": [
    "4.7369567894801664e-06",
    "p.His139LeufsX15",
    "Yes, new variant added",
    "CF-causing",
    "c.415_416insTA",
    "1",
    "547insTA"
  ],
  "c.4187del": [
    "4.7369567894801664e-06",
    "c.4187del",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "p.Thr1396LysfsX2",
    "c.4187delC"
  ],
  "p.Thr1396LysfsX2": [
    "4.7369567894801664e-06",
    "c.4187del",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "p.Thr1396LysfsX2",
    "c.4187delC"
  ],
  "c.4187delC": [
    "4.7369567894801664e-06",
    "c.4187del",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "p.Thr1396LysfsX2",
    "c.4187delC"
  ],
  "c.583del": [
    "c.583del",
    "4.7369567894801664e-06",
    "c.583delC",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "p.Ala196HisfsX19"
  ],
  "c.583delC": [
    "c.583del",
    "4.7369567894801664e-06",
    "c.583delC",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "p.Ala196HisfsX19"
  ],
  "p.Ala196HisfsX19": [
    "c.583del",
    "4.7369567894801664e-06",
    "c.583delC",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "p.Ala196HisfsX19"
  ],
  "c.88_89del": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.88_89del",
    "CF-causing",
    "c.88_89delCA",
    "1",
    "p.Gln30AlafsX14"
  ],
  "c.88_89delCA": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.88_89del",
    "CF-causing",
    "c.88_89delCA",
    "1",
    "p.Gln30AlafsX14"
  ],
  "p.Gln30AlafsX14": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "c.88_89del",
    "CF-causing",
    "c.88_89delCA",
    "1",
    "p.Gln30AlafsX14"
  ],
  "c.895del": [
    "4.7369567894801664e-06",
    "c.895del",
    "Yes, new variant added",
    "p.Ala299GlnfsX4",
    "CF-causing",
    "1027delG",
    "1"
  ],
  "p.Ala299GlnfsX4": [
    "4.7369567894801664e-06",
    "c.895del",
    "Yes, new variant added",
    "p.Ala299GlnfsX4",
    "CF-causing",
    "1027delG",
    "1"
  ],
  "1027delG": [
    "4.7369567894801664e-06",
    "c.895del",
    "Yes, new variant added",
    "p.Ala299GlnfsX4",
    "CF-causing",
    "1027delG",
    "1"
  ],
  "c.1592_1593delinsG": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "c.1592_1593delinsG",
    "1",
    "S531X",
    "p.Ser531X"
  ],
  "S531X": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "c.1592_1593delinsG",
    "1",
    "S531X",
    "p.Ser531X"
  ],
  "p.Ser531X": [
    "4.7369567894801664e-06",
    "Yes, new variant added",
    "CF-causing",
    "c.1592_1593delinsG",
    "1",
    "S531X",
    "p.Ser531X"
  ],
  "c.863_869+2del": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "c.863_869+2del",
    "CF-causing",
    "1",
    "994del9"
  ],
  "994del9": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "c.863_869+2del",
    "CF-causing",
    "1",
    "994del9"
  ],
  "c.1579_1584+11del": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "c.1579_1584+11del",
    "1",
    "1710del17bp"
  ],
  "1710del17bp": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "c.1579_1584+11del",
    "1",
    "1710del17bp"
  ],
  "875insTACA": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "875insTACA",
    "c.743_743+1insTACA",
    "CF-causing",
    "1"
  ],
  "c.743_743+1insTACA": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "875insTACA",
    "c.743_743+1insTACA",
    "CF-causing",
    "1"
  ],
  "c.2T>G": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "c.2T>G",
    "CF-causing",
    "1",
    "M1R"
  ],
  "M1R": [
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "c.2T>G",
    "CF-causing",
    "1",
    "M1R"
  ],
  "c.273+7982del18652": [
    "c.273+7982del18652",
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "405+7982del18652"
  ],
  "405+7982del18652": [
    "c.273+7982del18652",
    "4.7369567894801664e-06",
    "p.?",
    "Yes, new variant added",
    "CF-causing",
    "1",
    "405+7982del18652"
  ],
  "1419delC": [
    "1419delC",
    "No",
    "CF-causing",
    "c.1287del",
    "0",
    "p.Phe430SerfsX12"
  ],
  "c.1287del": [
    "1419delC",
    "No",
    "CF-causing",
    "c.1287del",
    "0",
    "p.Phe430SerfsX12"
  ],
  "0": [
    "1419delC",
    "No",
    "CF-causing",
    "c.1287del",
    "0",
    "p.Phe430SerfsX12"
  ],
  "p.Phe430SerfsX12": [
    "1419delC",
    "No",
    "CF-causing",
    "c.1287del",
    "0",
    "p.Phe430SerfsX12"
  ],
  "CF-causing (now renamed 1812-1G->C)": [
    "CF-causing (now renamed 1812-1G->C)",
    "IVS11-1G->C",
    "(CF-causing under new name)",
    "No, but renamed"
  ],
  "IVS11-1G->C": [
    "CF-causing (now renamed 1812-1G->C)",
    "IVS11-1G->C",
    "(CF-causing under new name)",
    "No, but renamed"
  ],
  "(CF-causing under new name)": [
    "IVSI-5842_IVS4+401del",
    "(CF-causing under new name)",
    "CF-causing (now renamed CFTRdele2-4)",
    "No, but renamed"
  ],
  "No, but renamed": [
    "IVSI-5842_IVS4+401del",
    "(CF-causing under new name)",
    "CF-causing (now renamed CFTRdele2-4)",
    "No, but renamed"
  ],
  "CF-causing (now renamed 3165dupA)": [
    "CF-causing (now renamed 3165dupA)",
    "c.3033dup",
    "No, but renamed",
    "(CF-causing under new name)"
  ],
  "CF-causing (now renamed 3539del16)": [
    "CF-causing (now renamed 3539del16)",
    "(CF-causing under new name)",
    "3407_3422del16",
    "No, but renamed"
  ],
  "c.3407_3422del16": [
    "CF-causing (now renamed 3539del16)",
    "(CF-causing under new name)",
    "No, but renamed",
    "c.3407_3422del16"
  ],
  "CFTRdelePr-1": [
    "CFTRdelePr-1",
    "CF-causing (now renamed CFTRdele1)",
    "No, but renamed",
    "(CF-causing under new name)"
  ],
  "CF-causing (now renamed CFTRdele1)": [
    "CFTRdelePr-1",
    "CF-causing (now renamed CFTRdele1)",
    "No, but renamed",
    "(CF-causing under new name)"
  ],
  "CF-causing (now renamed CFTRdele17a,17b)": [
    "CF-causing (now renamed CFTRdele17a,17b)",
    "3121-977_3499+248del2515",
    "No, but renamed",
    "(CF-causing under new name)"
  ],
  "3121-977_3499+248del2515": [
    "CF-causing (now renamed CFTRdele17a,17b)",
    "3121-977_3499+248del2515",
    "No, but renamed",
    "(CF-causing under new name)"
  ],
  "IVSI-5842_IVS4+401del": [
    "IVSI-5842_IVS4+401del",
    "(CF-causing under new name)",
    "CF-causing (now renamed CFTRdele2-4)",
    "No, but renamed"
  ],
  "CF-causing (now renamed CFTRdele2-4)": [
    "IVSI-5842_IVS4+401del",
    "(CF-causing under new name)",
    "CF-causing (now renamed CFTRdele2-4)",
    "No, but renamed"
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

def suggest_mutations(partial_input):
    if not partial_input:
        return []
    return sorted([m for m in eligible_mutations if partial_input.lower() in m.lower()])

st.title("Trikafta Eligibility Checker")
st.write("Enter your patient's two CFTR mutations. Matching eligible mutations will be suggested as you type.")

mutation1 = st.text_input("Enter First Mutation:")
suggestions1 = suggest_mutations(mutation1)
if suggestions1:
    st.write("Suggestions:", suggestions1)

mutation2 = st.text_input("Enter Second Mutation:")
suggestions2 = suggest_mutations(mutation2)
if suggestions2:
    st.write("Suggestions:", suggestions2)

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

st.markdown("---")
st.caption("Built for CF clinics – 2025")
