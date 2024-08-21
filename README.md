# First End-to-End-Data-Portfolio by Kayne

Good day team! This repository is established as a part of the First End-to-End Data Portfolio series of JoshDev, still valid as of March 2024.

![426374220_352790397631613_2113406517611894463_n](https://github.com/kayndrigs/Rodrigo-End-to-End-Data-Portfolio/assets/103131412/74b74919-36f1-413c-8870-e32ca9dfcded)

reference: Josh Valdeleon. (2024, March 3). BUILDING YOUR FIRSTEND-TO-END DATA PORTFOLIO [Video]. YouTube. https://www.youtube.com/watch?v=S9mVrof-bR8

According to JoshDev, this is a series that empowers any data enthusiast to leverage their knowledge and skills in doing data-engineering tasks such as creating data pipelines using Python, SQL, and configuring FTP servers using Linux distro. Beyond that, it also encompasses the creation of dashboards, data analysis, and machine learning model training, which overall covers all data-related specialization. 

# Instructions
1. Clone this repository
2. Create virtual environment with: `python -m venv env`
   - note: `.gitignore` added to avoid git push of environment into the repository. 
3. Activate environment (assuming that the directory is loaded in the terminal)
   - `env\Scripts\activate.bat` (windows command prompt)
   - `env\Scripts\activate.ps1` (powershell)
   - `source env/Scripts/activate` (git bash)
4. Install the packages with: `pip install -r .\requirements.txt`

5. **If incase you forgot to create a requirements.txt**
   - `pip install pip-chill`
   - `pip-chill requirements.txt`

# Episode 1: Introduction and Project Overview

- Preparation of necessary software tools (pre-requisite)
  - Python skills
  - Visual Studio Code: https://code.visualstudio.com/
  - SQL Server 2022 (Developer)
    - Visual Studio: https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16
    - SQL Server Data Tools (SSDT) for Visual Studio: https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver16
    - PostgreSQL: https://www.postgresql.org/
    - PowerBI Desktop: https://powerbi.microsoft.com/en-us/desktop/
  - Git: https://git-scm.com/

  YT Link: https://www.youtube.com/watch?v=S9mVrof-bR8&t=242s

# Episode 2: Version control and virtual environment essentials
- Review of git and github usage for uploading projects to repositories
- Commonly used Git commands: (git must be installed)
  - git init . # dot for current directory
  - git add . # dot for all changes
  - git commit -m "Added new message"
  - git rm <filename.file> # remove files
  - git push
  - git pull
  - git fork # forks a repository
- note: always create a unique sub-branch when working with organizational repository
- assigns github account and push changes to GitHub Repository

YT Link: [https://www.youtube.com/watch?v=S9mVrof-bR8&list=PLtomnyC4qhTwqcZ3DzBhewMNjM_4rHqnO&index=1](https://www.youtube.com/watch?v=F5M4WZifOu0&t=5567s)

# Episode 3: Extracting data from web to FTP using Python
- Performed setup of WSL (Windows Subsystem for Linux) and using Ubuntu as the distro.
- Installed vsftpd for FTP (port 21) server for unix systems with configured settings.
- Created another python environment suitable for creating FTP servers in linux.
- Using the environment, performed the connection to FTP server and established an SSH-encrypted connection.
- Established a data pipeline for data extraction and upload.
- Created an automated python CSV generator functions used on dataset links from Office of Foreign Assets Control (OFAC).
- Uploaded the generated the csv file to the FTP server, and deleted from the local filesystem.
- Created a script for manual or scheduled tasks based on their keyword as parameter.
  - **error handling**:
    - case 1:  User is not in Sudoers File. This incident will be reported - https://www.youtube.com/watch?v=dmClYPXko9k
      
YT Link: https://www.youtube.com/watch?v=j7fNG-V4aGE&t=6324s
   
# Episode 4: Loading CSV files from FTP to PostgreSQL using SSIS (Continuation of the previous repository)
**"We need to wear the hats pf business analyst."**
- Discussion of ETL Concepts
  - ETL can be interchangeable to ELT or EL
- Transferred Vsftpd Flat Files to Local Directory
- Created ODBC Connection for Postgresql in ODBC Data Source Administrator
- Loaded local Flat Files to Postgresql DB through SSIS
- Created 3 tables for CONS_OFAC dataset (PRIM, ALT, ADD)
- Built and Deployed SSIS Package to SSMS
- (pending) deployment to SQL Server Agent
  
YT Link: https://www.youtube.com/watch?v=m2DD-RvT-nA&t=1783s



Github Link of EP 4: https://github.com/kayndrigs/Rodrigo_FtpToPostgre

![Screenshot 2024-03-08 153435](https://github.com/kayndrigs/Rodrigo_FtpToPostgre/assets/103131412/5ed7184e-067e-411b-9830-1bf543d16f91)


![image](https://github.com/user-attachments/assets/f54b1c7a-3fbf-432b-9d38-5ad799cc0124)
