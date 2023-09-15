import os 
from datetime import datetime


class nextclade:

    def nextclade_new_version(outdir):
        os.system(f'curl -fsSL "https://github.com/nextstrain/nextclade/releases/latest/download/nextclade-x86_64-unknown-linux-gnu" -o {outdir}"/nextclade" && chmod +x {outdir}/nextclade')

    def Downloaddataset (outdir):
        os.system(f"package/nextclade/nextclade dataset get --name 'MPXV' --output-dir {outdir}")
    
    def run_nextclade(datasets,input,output):
        print('\n\n> Running Nextclade analysis pipeline ... [ '+str(datetime.now())+" ]")
        os.system(f"package/nextclade/nextclade run   --input-dataset {datasets}   --output-tsv {output}  {input}")

        print('\033[1;32m \n\n> Done ... [ '+str(datetime.now())+" ] \n\n"+'\033[0m')

