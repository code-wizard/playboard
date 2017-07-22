#!/bin/bash


git pull origin master
supervisorctl reload
/etc/init.d/celeryd restart