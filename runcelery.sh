#! /bin/bash

celery -A core worker --beat --loglevel=info