# ETL_Pipeline_spotify_playlist
An ETL pipeline created using python to extract, transform and load cleaned csv into postgres db, schedule to run later today by 4pm.

# STEPS
1. Create Github repo "ETL_Pipeline_spotify_playlist"
2. Run gitbash  - cd to desktop, cd to week 12
- git clone ssh
3. Navigate - cd "ETL_Pipeline_spotify_playlist"
4. mkdir script,  mkdir data
5. cd data 
6. mkdir raw , mkdir processed
7. open vs code, folder, user "ETL_Pipeline_spotify_playlist"
8. in script- ingest.py, transform.py, Automation.sh
9.windows shell
unix user vera,  12345
crontab -l
crontab-e in a nano proram

10. writing scheduler in a nano page
ctrl x -exit
windows r
wsl
capital c to [mnt/c]
11. create 
cronjobs_product_etl_pipeline
mkdir Data
script
logs

12. in script inest.py   load.py transform.py etl_automation.sh
13. Now check the path of etl_automataion.sh,  copy it
14. windows r
wsl
14. crontab -e

15.  #013***/bin/bash/mnt/c/users/user/Desktop/volts/week 12/ cronjob_production_etl_pipeline/script/etl_automation.sh

16. paste in nano
ctrl o +enter
ctrl x + enter
17. ls
18. cd into etl dir
chmod+x etl_automation.sh
bash etl_automation.sh
nano etl_automation.sh
bash etl_automation.sh