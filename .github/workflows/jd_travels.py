name: jd_travel_shop_task

on:
    workflow_dispatch:
    schedule:
        - cron: "25 8 * * *"
    watch:
        types: [started]
    repository_dispatch:
        types: jd_travels

jobs:
    build:
        runs-on: ubuntu-latest
        if: github.event.repository.owner.id == github.event.sender.id
        steps:
          - name: Checkout
            uses: actions/checkout@v2

          - name: 'Set up Python'
            uses: actions/setup-python@v1
            with:
              python-version: 3.7

          - name: 'Install requirements'
            run: pip install -r ./requirements.txt
            
                  
          - name: run
            run: |             
             sed -i "15c/${{ secrets.JD_COOKIE1 }}" ./config.yaml
             sed -i "16c/${{ secrets.JD_COOKIE2 }}" ./config.yaml
             sed -i "17c/${{ secrets.JD_COOKIE3 }}" ./config.yaml
             sed -i "18c/${{ secrets.JD_COOKIE4 }}" ./config.yaml
             sed -i "19c/${{ secrets.JD_COOKIE5 }}" ./config.yaml
             sed -i "15,19s/^/  - /g" ./config.yaml
             sed -i "s/aaa/${{ secrets.TG_BOT_TOKEN }}/g" ./config.yaml
             sed -i "s/bbb/${{ secrets.TG_USER_ID }}/g" ./config.yaml
             sed -i "s/weixin/${{ secrets.WECHAT_WORK }}/g" ./config.yaml
             sed -i "s/default=0/default=1/g" ./db/model.py
             mkdir conf 
             mv ./config.yaml ./conf/config.yaml        
             python3 jd_travels.py                 
