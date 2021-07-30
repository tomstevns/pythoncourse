#!/bin/bash
for url in 'https://api.github.com/repositories/596892/contributors?page=1' 'https://api.github.com/repositories/596892/contributors?page=2' 'https://api.github.com/repositories/596892/contributors?page=3' 'https://api.github.com/repositories/596892/contributors?page=4' 'https://api.github.com/repositories/596892/contributors?page=5' 'https://api.github.com/repositories/596892/contributors?page=6' 'https://api.github.com/repositories/596892/contributors?page=7' 'https://api.github.com/repositories/596892/contributors?page=8' 'https://api.github.com/repositories/596892/contributors?page=9' 'https://api.github.com/repositories/596892/contributors?page=10' 'https://api.github.com/repositories/596892/contributors?page=11' 'https://api.github.com/repositories/596892/contributors?page=12' 'https://api.github.com/repositories/596892/contributors?page=13' 'https://api.github.com/repositories/596892/contributors?page=14'

do
    echo "Started python ./hard_work.py ${url}"
    nohup python ./hard_work.py ${url} </dev/null >> output.log 2>&1 &
done