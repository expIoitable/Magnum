import requests
import socket
import json
import sys
import Keys
import os

from os import system, name
from Keys import *

Logo = f"""
888b     d888
8888b   d8888
88888b.d88888
888Y88888P888  8888b.   .d88b.  88888b.  888  888 88888b.d88b.
888 Y888P 888     "88b d88P"88b 888 "88b 888  888 888 "888 "88b     Version: 1.0
888  Y8P  888 .d888888 888  888 888  888 888  888 888  888  888     For Contact:
888   "   888 888  888 Y88b 888 888  888 Y88b 888 888  888  888     vivid@fbi.systems
888       888 "Y888888  "Y88888 888  888  "Y88888 888  888  888     vivid#6221
                            888
                       Y8b d88P
                        "Y88P"

"""

print(Logo)

class Recon:

    if MailboxLayer == None:
        print("(-) Error Using MailboxLayer API Key. Please Use A Valid One.")
        exit()
    else:
        print("(+) MailboxLayer API Key Connected.")

    Target = input(str("(>) Enter Your Target Email Address: "))
    Conf = input(str("\n(!) Warning: Alt Finder Will Use Alot Of Your API Key.\n(>) Enable Alt-Finder: ")).lower()

    Verif = requests.get(f"http://apilayer.net/api/check?access_key={MailboxLayer}&email={Target}&smtp=1&format=1").text
    MLoad = json.loads(Verif)

    MLoadSMTP = MLoad["smtp_check"]

    if MLoadSMTP == True:
        print("(+) Email Successfully Verified.")
    else:
        print("(-) Please Use A Valid Email Address.")
        exit()

    MailboxGraph = f"""
Data From MailboxLayer
Data From MailboxLayer Written To Target.txt.

Email:              {MLoad["email"]}
User:               {MLoad["user"]}
Domain:             {MLoad["domain"]}
Format Valid:       {MLoad["format_valid"]}
MX Found:           {MLoad["mx_found"]}
SMTP check:         {MLoad["smtp_check"]}
Catch All:          {MLoad["catch_all"]}
Role:               {MLoad["role"]}
Disposable:         {MLoad["disposable"]}
Score:              {MLoad["score"]}
    """
    print(MailboxGraph)
    File = open("Target.txt", "w")
    File.write(MailboxGraph)

    if Conf[0] == "y":
        print("\nRunning Alt-Finder. This Process May Take A While.")
        EmailAlt1 = MLoad["user"] + "1@" + MLoad["domain"]
        EmailAlt2 = MLoad["user"] + "2@" + MLoad["domain"]
        EmailAlt3 = MLoad["user"] + "alt@" + MLoad["domain"]
        EmailAlt4 = MLoad["user"] + "alt1@" + MLoad["domain"]

        VerifAlt1 = requests.get(f"http://apilayer.net/api/check?access_key={MailboxLayer}&email={EmailAlt1}&smtp=1&format=1").text

        VerifAlt2 = requests.get(f"http://apilayer.net/api/check?access_key={MailboxLayer}&email={EmailAlt2}&smtp=1&format=1").text

        VerifAlt3 = requests.get(f"http://apilayer.net/api/check?access_key={MailboxLayer}&email={EmailAlt3}&smtp=1&format=1").text

        VerifAlt4 = requests.get(f"http://apilayer.net/api/check?access_key={MailboxLayer}&email={EmailAlt4}&smtp=1&format=1").text

        AltLoad1 = json.loads(VerifAlt1)
        AltLoadSMTP1 = AltLoad1["smtp_check"]

        AltLoad2 = json.loads(VerifAlt2)
        AltLoadSMTP2 = AltLoad2["smtp_check"]

        AltLoad3 = json.loads(VerifAlt3)
        AltLoadSMTP3 = AltLoad3["smtp_check"]

        AltLoad4 = json.loads(VerifAlt4)
        AltLoadSMTP4 = AltLoad4["smtp_check"]

        if AltLoadSMTP1 == True:
            print("(+) Email Found")
            AltLogo1 = f"""
Data From MailboxLayer
Data From MailboxLayer Written To Target.txt.

Email:              {AltLoad1["email"]}
User:               {AltLoad1["user"]}
Domain:             {AltLoad1["domain"]}
Format Valid:       {AltLoad1["format_valid"]}
MX Found:           {AltLoad1["mx_found"]}
SMTP check:         {AltLoad1["smtp_check"]}
Catch All:          {AltLoad1["catch_all"]}
Role:               {AltLoad1["role"]}
Disposable:         {AltLoad1["disposable"]}
Score:              {AltLoad1["score"]}
            """
            print(AltLogo1)
            File.write("\n\n\n" + AltLogo1)
        else:
            print(f"(-) {EmailAlt1} Invalid.")

        if AltLoadSMTP2 == True:
            print("(+) Email Found")
            AltLogo2 = f"""
Data From MailboxLayer
Data From MailboxLayer Written To Target.txt.

Email:              {AltLoad2["email"]}
User:               {AltLoad2["user"]}
Domain:             {AltLoad2["domain"]}
Format Valid:       {AltLoad2["format_valid"]}
MX Found:           {AltLoad2["mx_found"]}
SMTP check:         {AltLoad2["smtp_check"]}
Catch All:          {AltLoad2["catch_all"]}
Role:               {AltLoad2["role"]}
Disposable:         {AltLoad2["disposable"]}
Score:              {AltLoad2["score"]}
            """
            print(AltLogo2)
            File.write("\n\n\n" + AltLogo2)
        else:
            print(f"(-) {EmailAlt2} Invalid.")

        if AltLoadSMTP3 == True:
            print("(+) Email Found")
            AltLogo3 = f"""
Data From MailboxLayer
Data From MailboxLayer Written To Target.txt.

Email:              {AltLoad3["email"]}
User:               {AltLoad3["user"]}
Domain:             {AltLoad3["domain"]}
Format Valid:       {AltLoad3["format_valid"]}
MX Found:           {AltLoad3["mx_found"]}
SMTP check:         {AltLoad3["smtp_check"]}
Catch All:          {AltLoad3["catch_all"]}
Role:               {AltLoad3["role"]}
Disposable:         {AltLoad3["disposable"]}
Score:              {AltLoad3["score"]}
            """
            print(AltLogo3)
            File.write("\n\n\n" + AltLogo3)
        else:
            print(f"(-) {EmailAlt3} Invalid.")

        if AltLoadSMTP4 == True:
            print("(+) Email Found")
            AltLogo4 = f"""
Data From MailboxLayer
Data From MailboxLayer Written To Target.txt.

Email:              {AltLoad4["email"]}
User:               {AltLoad4["user"]}
Domain:             {AltLoad4["domain"]}
Format Valid:       {AltLoad4["format_valid"]}
MX Found:           {AltLoad4["mx_found"]}
SMTP check:         {AltLoad4["smtp_check"]}
Catch All:          {AltLoad4["catch_all"]}
Role:               {AltLoad4["role"]}
Disposable:         {AltLoad4["disposable"]}
Score:              {AltLoad4["score"]}
            """
            print(AltLogo4)
            File.write("\n\n\n" + AltLogo4)
        else:
            print(f"(-) {EmailAlt4} Invalid.")

    else:
        print("(>) Process Finished. Alt-Finder Was Not Enabled.")
