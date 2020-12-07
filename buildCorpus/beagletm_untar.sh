# Date: 7 Dec 2020
# Reference: data from ncbi: ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/

mkdir corpus
cd corpus
mkdir log
#untar a file in the background

tar -zxvf ../comm_use.A-B.xml.tar.gz 1>log/tar_ab_commUse_out.1 2>log/tar_ab_commUse_err.1 &
tar -zxvf ../comm_use.C-H.txt.tar.gz 1>log/tar_ch_commUse_out.1 2>log/tar_ch_commUse_err.1 &
tar -zxvf ../comm_use.I-N.txt.tar.gz 1>log/tar_in_commUse_out.1 2>log/tar_in_commUse_err.1 &
tar -zxvf ../comm_use.O-Z.xml.tar.gz 1>log/tar_oz_commUse_out.1 2>log/tar_oz_commUse_err.1 &
