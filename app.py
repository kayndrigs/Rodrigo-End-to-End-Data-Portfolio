#creating data pipeline
import sys
import json
import time
import schedule
import pandas as pd
from os import environ, remove
from pathlib import Path
from ftplib import FTP_TLS

def get_ftp() -> FTP_TLS:
    
    # Get FTP details
    FTPHOST = environ["FTPHOST"] # will return the ftp object that we can use to authenticate and access our ftp server
    FTPUSER = environ["FTPUSER"]
    FTPPASS = environ["FTPPASS"]
    FTPPORT = environ["FTPPORT"]
    
    print(f"test: {FTPHOST}")
    
    # Return authenticated FTP
    ftp = FTP_TLS(FTPHOST, FTPUSER, FTPPASS)
    ftp.prot_p()
    
    return ftp

def upload_to_ftp(ftp: FTP_TLS, file_source: Path):
    with open(file_source, "rb") as fp:
        ftp.storbinary(f"STOR {file_source.name}", fp)
    
def delete_file(file_source: str | Path):
    remove(file_source)
    
def read_csv(config: dict) -> pd.DataFrame:
    url = config["URL"]
    params = config["PARAMS"]
    return pd.read_csv(url, **params)

def pipeline():
    # Load source configuration
    with open ("config.json","rb") as fp:  #rb = read binary format of json for parsing into dictionary  in pandas
        config = json.load(fp)
        
    # Loop thorugh each configuration to get the source_name and its corresponding configuration
    
    for source_name, source_config in config.items():
        file_name = source_name + ".CSV"
        df = read_csv(source_config)
        df.to_csv(file_name, index=False)
        
        ftp = get_ftp()
        
        for source_name, source_config in config.items():
            file_name = Path(source_name + ".CSV")
            df = read_csv(source_config)
            df.to_csv(file_name, index=False)
            
            print(f"File {file_name} has been downloaded.")
            
            upload_to_ftp(ftp, file_name)
            print(f"File {file_name} has been uploaded to FTP.")
            
            delete_file(file_name)
            print(f"File {file_name} has been deleted.")
    
if __name__ == "__main__":
    
    param = sys.argv[1]
    
    if param == "manual":
        pipeline()
    elif param == "schedule":
        schedule.every().day.at("18:44").do(pipeline)
        
        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Invalid paramter. The app will not run.")
    
