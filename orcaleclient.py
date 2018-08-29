import os
os.chdir("C:\\Oracle\\instantclient_12_2")
import cx_Oracle
# ORACLE_CONNECT = "mathewg/mathewg@egts-qadb01.eagan.tshmg.com:1521:QATI05"
conn_str = u'smoke_ti8/smoke_ti8@egts-qadb01.eagan.tshmg.com:1521/QATI05'
# orcl = cx_Oracle.connect('mathewg/mathewg@egts-qadb01.eagan.tshmg.com::1521/QATI05')
orcl = cx_Oracle.connect(conn_str)
print("Connected to Oracle: " + orcl.version)
print("Done")