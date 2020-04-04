# WEB Crawler

## Installing 

```
pip install -r requirements.txt
```

## Configuring

Add your queries in a json file under queries dir.

File format:

```
{
  "urls": [],
  "selectors": {
    "title": "#productTitle"
  }
}
```


## Running

```
python3 crawler
```
