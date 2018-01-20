import urllib2

url = "https://l.facebook.com/l.php?u=https%3A%2F%2Fsft.tk%2FrkdQ8m2Ez&h=ATO1h8GQW2GBm-u9IQGg8-t_oDwiVn1Gi8HBLAXcFpLo5bEF8HrXL9ozHzAHLslSqIzhEKtqNy9tDh9F2hW0PdCvZDrmYh_z47ylPH-IXHdB10nPipwSw2cN38r-oFyi2keSKhRUX8twmahl-cp6YuNEyDNe6dHoEpXrg8rn46YbVNwPGraj2_IaQPOmsy_g96jUaqzhGuyxOTI7-TlOCj66eQlsuaYeHdB-MyVsIhSI_rIIqNQDgrYFivlReWTmEO_434WRBvt1FIUK-7t7PenswJ9M3q2FeLDVXVCH2R3mlfMfcpg"
req = urllib2.Request(url)
response = urllib2.urlopen(req)
the_page = response.read()

