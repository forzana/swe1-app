[![Build Status](https://app.travis-ci.com/forzana/swe1-app.svg?token=DmD1Wzzxg64ktDYLxKH1&branch=main)](https://app.travis-ci.com/forzana/swe1-app)
# SWE-1 Django App
Polls app built on Django.

## Testing on local
```
black .
flake8 .
python manage.py test
python -m coverage run --source=mysite,polls manage.py test
```