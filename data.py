import xml.etree.ElementTree as ET
import pandas as pd
import csv

# Parse the XML file
tree = ET.parse('SteelData.xml')
root = tree.getroot()

# Open the CSV file for writing
with open('myfile.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(['FinInstrmGnlAttrbts.Id', 'FinInstrmGnlAttrbts.FullNm', 'FinInstrmGnlAttrbts.ClssfctnTp', 'FinInstrmGnlAttrbts.CmmdtyDerivInd', 'FinInstrmGnlAttrbts.NtnlCcy', 'Issr'])

   # Loop through the FinancialInstrument elements and write the data rows
    for termntd_rcrd in root.findall('.//{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}TermntdRcrd'):

        id = termntd_rcrd.find('.//{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}Id').text
        full_nm = termntd_rcrd.find('.//{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}FullNm').text
        clssfctn_tp = termntd_rcrd.find('.//{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}ClssfctnTp').text
        cmmdty_deriv_ind = termntd_rcrd.find('.//{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}CmmdtyDerivInd').text
        ntnl_ccy = termntd_rcrd.find('.//{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}NtnlCcy').text
        issr = termntd_rcrd.find('.//{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}Issr').text
        writer.writerow([id, full_nm, clssfctn_tp, cmmdty_deriv_ind, ntnl_ccy, issr])