# pybrreg

This package serves as a utility to process information to and from notifications of change which are transmitted to The  Brønnøysund Register Centre.

## Howto: Build pyxb files
The package utilizes multiple machine-generated Python script files. The files are generated from XSD files from The 
Brønnøysund Register Centre, using the tool `pyxbgen` from the PyPI package `pyxb`

**pybrreg/xml/generated**
This is the bulk of the machine-generated files.

``` bash
# Files need to be generated from within pybrreg/xml/generated
cd pybbreg/xml/generated
# Rename the current files to avoid overwriting
rename .py .py.bak *.py
mv __init__.py.bak __init__.py
# TODO: Find a simple expression for avoiding moving __init__.py

# This generates a ton of binding.py-files
pyxbgen xsd/*.xsd
# Replace the absolute pathname for the bindings with a relative pathname
sed "s|$PWD/||g" -i binding*

# Rename the new files which have autogenerated filenames
# NOTE: The order of these binding files is correct at the time of writing but might change in the future
# You should make sure that the files at least somewhat resemble their backup counterparts before calling it a day
mv binding.py applikasjonskvittering.py
mv binding_2.py frivintVerifisertMelding.py
mv binding_3.py vedtak.py
mv binding_4.py manifest.py
mv binding_5.py melding.py
mv binding_.py recipients.py

# When the new files have been verified, the old files can be deleted
rm *.bak

# And go back to where we started
cd ../../..
```

**pybrreg/models/xsd**
``` bash
cd pybbreg/models/xsd
mv hentRoller.py hentRoller.py.bak

# Generate binding-file
pyxbgen *.xsd
# Replace the absolute pathname for the bindings with a relative pathname
sed "s|$PWD/||g" -i binding.py

mv binding.py hentRoller.py

# When the new file has been verified, the old files can be deleted
rm *.bak

# And go back to where we started
cd ../../..
```

**pybrreg/brreg_report_changes/pyxb_tools**
``` bash
cd pybrreg/brreg_report_changes/pyxb_tools
mv integrasjonPYXB.py integrasjonPYXB.py.bak

# Generate binding-file
pyxbgen *.xsd
# Replace the absolute pathname for the bindings with a relative pathname
sed "s|$PWD/||g" -i binding.py

mv binding.py integrasjonPYXB.py

# When the new file has been verified, the old files can be deleted
rm *.bak

# And go back to where we started
cd ../../..
```

# About
Developed by Unicornis AS for use in the membership management system HyperSys and for use as reference code by other integrators.

This code is part of a simplification project with The Norwegian Register Centre ("Brønnøysundregistra"). The project goal was to create specifications and open up the central registry for direct submissions from membership management systems used by non-profit organisations (NGOs) to report changes of the board and other central information directly without use of normal registry submission channels like Altinn.

Note that the code is to be used as a reference for developers to understand the use of APIs, and not intended to be directly used in production systems.
