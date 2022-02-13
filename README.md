# e-valuator

Simple python3 script for checking SPF & DMARC records.

## Description

Email spoofing is one of the most effective techniques to get initial access or harvest credentials. A lot of organizations mess up their spf records or misconfigure their DMARC record. This is a simple script that fetches that info and gives you information on whether the domain emails can be effectively spoofed or not.

## Platform

Works on windows or linux with python3.

## Installing
```
git clone https://github.com/keocol/e-valuator
pip install -r requirements.txt
python3 e-valuator.py
```

## License

This project is licensed under the [MIT] License - see the LICENSE.md file for details

## Acknowledgment

I have found the below script while researching email security, very similar to what we're doing here but it's written in python2.

https://github.com/BishopFox/spoofcheck
