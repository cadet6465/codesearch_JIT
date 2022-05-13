

def _read_tsv(input_file):
    """Reads a tab separated value file."""
    with open(input_file, "r", encoding='ISO-8859-1', errors='ignore') as f:
        lines = []
        for line in f.readlines():
            line = line.strip().split('<CODESPLIT>')
            if len(line) != 5:
                continue
            lines.append(line)
        return lines


def main():
    file_path = './codesearch_data/train_valid/test/train1.txt'

if __name__ == "__main__":
    main()
