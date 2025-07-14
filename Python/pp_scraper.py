import os
import json
import csv

def get_pp(directory):
    results = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if 'rank_001' in file and file.endswith('.json'):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r') as f:
                    data = json.load(f)
                
                pTM_score = data.get('ptm', 'N/A')
                pLDDT_scores = data.get('plddt', [])
                
                if pLDDT_scores:
                    mean_pLDDT = sum(pLDDT_scores) / len(pLDDT_scores)
                else:
                    mean_pLDDT = 'N/A'
                
                if len(pLDDT_scores) < 400:
                    pLDDT_scores.extend(['N/A'] * (400 - len(pLDDT_scores)))
                elif len(pLDDT_scores) > 400:
                    pLDDT_scores = pLDDT_scores[:400]
                
                row = [os.path.basename(root), pTM_score, mean_pLDDT] + pLDDT_scores
                results.append(row)
    
    with open('pp_scrapped.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Folder Name', 'pTM Score', 'Mean pLDDT'] + [f'pLDDT_{i+1}' for i in range(400)])
        csvwriter.writerows(results)

process_json_files('C:\\Users\\User\\Desktop\\fyp_data\\raw_ColabFold_JSON')
