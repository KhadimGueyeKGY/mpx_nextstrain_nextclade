import requests, os , io
import pandas as pd 



class DownData:
    BASE_PORTAL_API_SEARCH_URL = 'https://www.ebi.ac.uk/ena/portal/api/search'
    BASE_PORTAL_API_SEARCH_FASTA = 'https://www.ebi.ac.uk/ena/browser/api/fasta/'
    ena_searches = {
       'search_fields': ['accession'], 'result_type': 'sequence', 'data_portal': 'ena' , 'result_type': 'sequence'
        }
    # &format=tsv
    def __init__(self):
        pass
    def get_url(taxon):
        url = ''.join([
            DownData.BASE_PORTAL_API_SEARCH_URL,
            '?',
            'dataPortal=' + DownData.ena_searches["data_portal"],
            '&',
            'fields=' + '%2C'.join(DownData.ena_searches["search_fields"]),
            '&',
            'query=tax_tree('+str(taxon)+')',
            '&',
            'result=' + DownData.ena_searches["result_type"],
            '&format=tsv&limit=0' 
        ])
        return url
    
    def downdata(taxon, output):
        url = DownData.get_url(taxon)
        response = requests.get(url)
        data = pd.read_csv(io.StringIO(response.content.decode('UTF-8')), sep="\t", low_memory=False)
        #data.to_csv(output+'/metadata.tsv', sep="\t", index=False)
        accession = data['accession']

        for i in accession:
            os.system('curl "'+DownData.BASE_PORTAL_API_SEARCH_FASTA+i+'?download=true" --output '+output+'/'+i+'.fasta')
    

        #-------------------- fata frep
    def fataprep(input_dir, output_dir):
        fasta_files = [file for file in os.listdir(input_dir) if file.endswith('.fasta')]
        with open(os.path.join(output_dir, 'sequences.fasta'), 'w') as output:
            for fasta_file in fasta_files:
                with open(os.path.join(input_dir, fasta_file), 'r') as input_file:
                    for line in input_file:
                        if line.startswith('>'):
                            sequence_id = line.split('|')[1]
                            output.write('>' + sequence_id + '\n')
                        else:
                            output.write(line)



    


   