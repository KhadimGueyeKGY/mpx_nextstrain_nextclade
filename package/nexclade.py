import os 
from datetime import datetime


class nextclade:

    def Downloaddataset (outdir):
        os.system(f"nextclade dataset get --name 'MPXV' --output-dir {outdir}")
    
    def run_nextclade(datasets,input,output):
        print('\n\n> Running Nextclade analysis pipeline ... [ '+str(datetime.now())+" ]")
        os.system(f"nextclade run   --input-dataset {datasets}   --output-tsv {output}  {input}")

        print('\033[1;32m \n\n> Done ... [ '+str(datetime.now())+" ] \n\n"+'\033[0m')

