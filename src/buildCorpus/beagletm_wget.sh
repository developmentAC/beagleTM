# Date: 7 Dec 2020
# Reference: data from ncbi: ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/

# keep a log of the download
mkdir log
wget ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/comm_use.A-B.xml.tar.gz 1>log/ab_out.1 2>log/ab_download.1 &
#wget ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/non_comm_use.A-B.xml.tar.gz 1>log/ab_nonComm_out.1 2>log/ab_nonComm_download.1 &

wget ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/comm_use.C-H.txt.tar.gz  1>log/ch_out.1 2>log/ch_download.1 &
#wget ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/non_comm_use.C-H.xml.tar.gz 1>log/ch_nonComm_out.1 2>log/ch_nonComm_download.1 &

wget ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/comm_use.I-N.txt.tar.gz 1>log/in_out.1 2>log/in_download.1 &
#wget ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/non_comm_use.I-N.xml.tar.gz 1>log/in_nonComm_out.1 2>log/in_nonComm_download.1 &

wget  ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/comm_use.O-Z.xml.tar.gz 1>log/oz_out.1 2>log/oz_download.1 &
#wget  ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/non_comm_use.O-Z.xml.tar.gz 1>log/oz_nonComm_out.1 2>log/oz_nonComm_download.1 &
ls -l log/
