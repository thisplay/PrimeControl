  # -*- coding: utf-8 -*-

import requests
import json
import csv
import sys

URL_BASE = "https://api.clashroyale.com/v1"


class ClashRoyale(object):
    
    def __init__(self):
        self._result = ''
        
    def get_headers(self):
        try:
            with open("MyKey.txt") as f_key:
                my_key = 'Bearer ' + f_key.read().rstrip("\n")
    
            headers = {
                    'Content-Type':'Content-Type: "application/json"',
                    'Authorization':my_key
                }
            return headers
        except:
            print("Erro na leitura da Chaveda Api. Por favor, verifique se o arquivo da chave está nop diretório.")

    def get_ClanByName(self, clanName):
        
        endpoint = "/clans?name=" + clanName
        url = URL_BASE + endpoint
        req = requests.get(url,headers=self.get_headers())
        json_r = req.json()

        if bool(json_r['items']):
            self._result = json_r
        else:
            self._result = []

    def filter_Clans(self, tag,loc):
        return [obj for obj in self._result['items'] if obj['location']['name'] == loc and obj['tag'].startswith(tag)]

    def get_Members(self,tag):
        endpoint = "/clans/" + tag + "/members"
        url = URL_BASE + endpoint
        req = requests.get(url,headers=self.get_headers())
        json_r = req.json()

        if bool(json_r['items']):
            return json_r
        else:
            return []

    def save_InfosClan(self, obj):
        with open('Infos_ClashRoyale.csv', 'w', encoding="utf-8") as arquivo_csv:

            cols = ['Nome','Level','Trofeus','Papel']
            writer = csv.DictWriter(arquivo_csv, fieldnames=cols, delimiter=',', lineterminator='\n')
            writer.writeheader()

            for item in obj["items"]:
                writer.writerow({'Nome': item["name"], 'Level':  item["expLevel"], 'Trofeus': item["trophies"], 'Papel': item["role"]})

        print("Arquivo Salvo com sucesso!")

    def BuscarMembros(self, nameClan,clanTag, clanLocation):
        self.get_ClanByName(nameClan)
        result = self.filter_Clans(clanTag, clanLocation)
        members = self.get_Members(result[0]['tag'].replace("#","%23"))
        self.save_InfosClan(members)

