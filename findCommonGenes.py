# -*- coding: cp1255 -*-
import re

def define_transcription_sites():
    """Define transcription binding sites."""
    oct4 = "ATTTGCAT"
    sox2 = "ATTTGCAT"
    klf4 = "CACCC"
    myc = "CAC[GA]TC"
    e2f1 = "TTTC[CG]CGC"
    nanog = "TTTC[CG]CGC"
    nanog1 = "[CG][GA][CG]C[GC]ATTAN[GC]"
    return [oct4, sox2, klf4, myc, e2f1, nanog, nanog1]

def process_header(line):
    """Extract name from the header line."""
    _, _, b = line.partition('_')
    _, _, e = b.partition('_')
    name, _, _ = e.partition(' ')
    return name

def process_sequence(line, seq):
    """Append the sequence line."""
    return seq + line

def search_transcription_sites(name, seq, transcription_sites, results):
    """Search for transcription sites in the sequence."""
    for i, site in enumerate(transcription_sites):
        if re.search(site, seq):
            if i == 0:
                results["Oct4"].append(name)
            elif i == 1:
                results["Sox2"].append(name)
            elif i == 2:
                results["Klf4"].append(name)
            elif i == 3:
                results["Myc"].append(name)
            elif i == 4:
                results["E2f1"].append(name)
            elif i in [5, 6]:
                results["Nanog"].append(name)

def write_results_to_file(results, output_file):
    """Write the results to a file."""
    with open(output_file, 'w') as t:
        for key, value in results.items():
            t.write(f"{key}: {len(value)} {value}\n")

def main(input_file, output_file):
    """Main function to process the input file."""
    transcription_sites = define_transcription_sites()
    results = {"Oct4": [], "Sox2": [], "Klf4": [], "Myc": [], "E2f1": [], "Nanog": []}
    seq = ""
    name = ""

    with open(input_file, 'r') as f:
        line = f.readline().strip()
        if line.startswith('>'):
            name = process_header(line)

        while True:
            line = f.readline().strip()
            if not line:
                break
            if line.startswith('>'):
                search_transcription_sites(name, seq, transcription_sites, results)
                name = process_header(line)
                seq = ""
            else:
                seq = process_sequence(line, seq)

        # Final check for the last sequence
        search_transcription_sites(name, seq, transcription_sites, results)

    write_results_to_file(results, output_file)

# Run the script
if __name__ == "__main__":
    main('datashort.txt', 'genes.txt')
