import ftplib
from datetime import datetime, timedelta


def ftp_upload(project_path,file):
    try:
        hostname = '10.128.16.210'
        user = 'admin'
        pwd = '1234'

        #hostname = '192.168.100.11'
        #user = 'test'
        #pwd = '1234'

        now = datetime.now()
        date_file_name = f'{str(now.date())}_{str(now.time()).split(".")[0].replace(":","_")}'
        year,month,date = mfg_date()

        upload_path = f"/{project_path}/{year}/{month}/{date}/TYLALOND_{date_file_name}.csv"

        session = ftplib.FTP(hostname,user,pwd)

        session.mkd(f'{project_path}/{year}')
        session.mkd(f'{project_path}/{year}/{month}')
        session.mkd(f'{project_path}/{year}/{month}/{date}')

        session.storbinary(f'STOR {upload_path}', file) 

        file.close()                                
        session.quit()
        
        return {"result":"ok",'code':'-'}
    except Exception as e: 
        return {"result":"error",'code':e}

def mfg_date():
    mfg_date = datetime.now() - timedelta(hours=7)
    year = mfg_date.year
    month = mfg_date.month
    date = mfg_date.day

    if len(str(year)) == 1:
        year = '0'+str(year)
    if len(str(month)) == 1:
        month = '0'+str(month)
    if len(str(date)) == 1:
        date = '0'+str(date)
    return year,month,date
