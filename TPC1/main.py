from collections import defaultdict


def read_dataset(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = lines[0].strip().split(',')
    data = [line.strip().split(',') for line in lines[1:]]
    return headers, data

def get_modalities(data):
    modalities = sorted(set(row[8] for row in data))
    return modalities

def get_aptitude_percentages(data):
    total = len(data)
    aptos = sum(1 for row in data if row[12].lower() == 'true')
    inaptos = total - aptos
    return aptos / total * 100, inaptos / total * 100

def get_age_distribution(data):
    age_distribution = defaultdict(int)
    for row in data:
        age = int(row[5])
        lower_bound = (age // 5) * 5
        upper_bound = lower_bound + 4
        category = f'[{lower_bound}-{upper_bound}]'
        age_distribution[category] += 1
    
    return dict(age_distribution)

def write_results(file_path, modalities, aptos_pct, inaptos_pct, age_distribution):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("Modalidades desportivas:\n")
        for modality in modalities:
            file.write(f"- {modality}\n")
        
        file.write("\nPercentagens de atletas aptos e inaptos para a prática desportiva:\n")
        file.write(f"Percentagem de atletas aptos: {aptos_pct:.2f}%\n")
        file.write(f"Percentagem de atletas inaptos: {inaptos_pct:.2f}%\n")
        
        file.write("\nDistribuição de atletas por escalão etário:\n")
        for category, count in sorted(age_distribution.items()):
            file.write(f"{category}: {count} atletas\n")

def main():
    input_file_path = 'emd.csv'
    output_file_path = 'out.txt'
    
    headers, data = read_dataset(input_file_path)
    
    modalities = get_modalities(data)
    aptos_pct, inaptos_pct = get_aptitude_percentages(data)
    age_distribution = get_age_distribution(data)
    
    write_results(output_file_path, modalities, aptos_pct, inaptos_pct, age_distribution)

if __name__ == "__main__":
    main()
