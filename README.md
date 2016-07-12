# IC-Codes

A tiny server exposes SIC and NAICS code correlations.

## Data source

- https://github.com/CompileInc/sic-codes
- https://github.com/CompileInc/naics-codes



## INSTALL

```
pip install requirements.txt
```

## RUN

```
python server.py
```

This will fetch the dataset first time you run the server.
If you want to reload the dataset, just delete the file 
```./data/industry-codes.json``` and re-run the server.

## Changing download location

If you wish to change the download location to of sic-codes, naics-codes,
change them at ```data/locations.py```.

eg: If you wish to use glean/sic-codes change the download link in as
```sic_file = 'https://github.com/glean/sic-codes/archive/master.zip'```


