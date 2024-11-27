import math

import hashlib
import json

#from terminalplot import plot
import asciichartpy as acp

import plotext as plt
import yfinance as yf

import os
import random

import pyxel

import bitcoin

class Currency:
    def __init__(self, name, value, total_shares, currency_id, is_real = False):
        pass


class Mines(self):
    #le minijeu mines et diamands en pyxel
    def __init__(self, name, player):
        pass

class Dice(self):
    #le minijeu de des en pyxel
    def __init__(self, name, player):
        pass

        

class Utilisateur:
    def __init__(self, name, surname, password, age, user_id, permissions = 1, balance = 0, wallet = {}, loans = {}, can_delete = False, code):
        self.name = name
        self.password = password
        self.age = age
        self.user_id = user_id
        self.permissions = permissions
        self.balance = balance
        self.wallet = wallet
        self.loans = loans
        self.can_delete = can_delete
        self.code = code

        self.trust = 100

    def check_delete(self):
        return self.balance == 0 and self.wallet == {}
            

    def delete(self):
        pass
        
    def change_password(self):
        pass
    


class Bank:
    def __init__(self):
        self.users = []
        with open("credentials.json", "w") as file:
            users = json.load(file)
        for user in users:
            self.users.append(Utilisateur(user["name"], user["surname"], user["password"], user["user_id"], user["permissions"], user["permissions"], user["balance"], user["wallet"], user["loans"], user["can_delete"], user["code"])
                              
            
            
        

    def main(self):
        pass
        
    def create_user(self):
        name = input("Entrez votre nom : ", end = "\r")
        surname = input("Entrez votre prenom : ", end = "\r")
        pwd = input("Entrez votre mot de passe (6 chiffres) : ", end = "\r")
        while len(pwd) != 6 or type(pwd) != "int":
            pwd = input("Entrez votre mot de passe (6 chiffres!) : ", end = "\r")
            
        conf_pwd = input("Confirmez votre mot de passe : ", end = "\r")
        
        while pwd != conf_pwd:
            pwd = input("Les mots de passe ne correspondent pas! Entrez votre mot de passe : ", end = "\r")
            conf_pwd = input("Confirmez votre mot de passe : ", end = "\r")

        email = input("Entrez votre mail : ", end = "\r")
        age = input("Entrez votre age: ", end = "\r")
        if age > 13 and age < 123:
            
            

            enc = conf_pwd.encode()
            hash1 = hashlib.md5(enc).hexdigest()

            user_id = name[0] + str(random.randint(1000000, 9999999) + surname[-1]
            code = random.randint(1000,9999)
    
            # On sauvegarde les données dans un fichier JSON
            user_data = {
                "name": name,
                "surname": surname,
                "password": hash1,
                "user_id": user_id,
                'trust_level': 100,
                'permissions': 'user',
                "balance" = 0,
                "wallet" = {},
                "loans" = {},
                "age" = age,
                "can_delete" = True,
                "code" = code
                                         
            }
            # On lit les utilisateurs existants
            if os.path.exists("credentials.json"):
                with open("credentials.json", "r") as file:
                    users = json.load(file)
            else:
                users = []
    
            # On ajoute le nouvel utilisateur à la liste
            users.append(user_data)
    
            # On sauvegarde à nouveau le fichier JSON avec les nouveaux utilisateurs
            with open("credentials.json", "w") as file:
                json.dump(users, file, indent=4)
                
            print("Vous êtes inscrit avec succès !", end = "\r")

        else:
            print("Vous n'avez pas l'age requis pour un compte, revenez plus tard!", end = "\r")
            

        

        
    def login(self):
        pass
        #a faire
            
        
    def loan(self, user):
        pass
        
    def check_persmissions(self, user):
        pass

    def minigame(self):
        pass
        
                                              
                                                              
Bank()                                                            
