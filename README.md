# make_dataset_with_rtsp
---

## Techno

---

![python](https://img.shields.io/badge/python-3.10%2B-blue)

## Launch


---
```bash
docker compose up -d
```

## Environment variables


---
- `PATH_API` - path to api
- `PASSWORD_API` - password to api
- `TIMEOUT_PICTURE` - timeout between pictures

### CITY ENVIRONMENT VARIABLES

- go to `city.py`
- add city name for [0]
- add city ip and port for [1]
- add city user name for [2]
- add city password for [3]

## LINT

---

```bash
py -m flake8 .
```

