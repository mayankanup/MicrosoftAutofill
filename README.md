# MicrosoftAutofill
https://chrome.google.com/webstore/detail/microsoft-autofill/fiedbfgcleddlbcmgdigjgdfcggjcion

This utility project helps to convert exported files from other password managers to Microsot Autofill Extension

**Prerequisites**  

* Python 3.x is installed on your PC.
* Conversion scripts are downloaded on your PC in some folder e.x. C:\utils

1. **Bitwarden**
   
   C:\utils>python BitwardenToMicrosoft.py bitwarden_export.json
   
   Sample output
   
   Reading : bitwarden_export_20201218164115.json
   
   Login not found in BangaloreTravel
   
   Output written : MicrosoftAutofill.csv
  
  
2. **LastPass**

   C:\utils>python LastPassToMicrosoft.py lastpass_export.csv

   Sample output

   Reading : lastpass_export.csv

   Reading header values

   Output written : MicrosoftAutofill.csv
   
3. **Dashlane**

   Coming soon

For any feedback and issues please feel free to reach me at <anup.mayank@outlook.com>
