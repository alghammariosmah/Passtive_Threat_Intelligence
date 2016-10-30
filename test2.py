import pythonwhois
import urllib2
from BeautifulSoup import BeautifulSoup
import os

directory1 = "C:\Users\osamahal-ghammari\PycharmProjects\Normshield\Verbose_DB"# set your desired directory
directory2 = "C:\Users\osamahal-ghammari\PycharmProjects\Normshield\All_Blacklist_domains_DB"# set your desired directory


def get_whois_domain(url, name):
    domain= pythonwhois.get_whois(url)
    # outputting the whole file in a text file
    f = open("%s_whoisINFO.txt" %name,"w")
    f.write("%s" %domain)
    f.close()
    return domain

def get_Registrant_emails(url, name):
    pattern = "%s_Registrant_emails" %name
    completeName = os.path.join(directory1, pattern+".txt")
    domain= pythonwhois.get_whois(url)
    if not os.path.exists(directory1):
        os.makedirs(directory1)
        f2 = open(completeName,"w")
        f2.write("%s Registrant Emails:\n" %name)

        Registrant_emails=[]
        for i in range(len(domain['contacts'].values())-1):
            emails = domain['contacts'].values()[i]['email']
            abuse_email= domain['emails'][0]
            if emails not in Registrant_emails:
                Registrant_emails.append(emails)
                f2.write("%s \n" %emails)
                if abuse_email not in Registrant_emails:
                    Registrant_emails.append(abuse_email)
                    f2.write("%s \n" %abuse_email)
                else:
                    continue
            else:
                continue
        verbose = domain['contacts']['registrant']
        f2.write("\n%s Verbose:\n" %name)
        for info, jnfo in zip(verbose.keys(), verbose.values()):
            f2.write("%s : %s\n" %(info, jnfo))
        f2.close()
        return Registrant_emails
    else:
        if not os.path.exists(completeName):
            f5 = open(completeName,"w")
            f5.write("%s Registrant Emails:\n" %name)
            Registrant_emails=[]
            for i in range(len(domain['contacts'].values())-1):
                emails = domain['contacts'].values()[i]['email']
                abuse_email= domain['emails'][0]
                if emails not in Registrant_emails:
                    Registrant_emails.append(emails)
                    f5.write("%s \n" %emails)
                    if abuse_email not in Registrant_emails:
                        Registrant_emails.append(abuse_email)
                        f5.write("%s \n" %abuse_email)
                    else:
                        continue
                else:
                    continue
            verbose = domain['contacts']['registrant']
            f5.write("\n%s Verbose:\n" %name)
            for info, jnfo in zip(verbose.keys(), verbose.values()):
                f5.write("%s : %s\n" %(info, jnfo))
            f5.close()
            return Registrant_emails




def get_all_domains(url, name):
    pattern = "%s_All_blacklist_domains"%name
    completeName = os.path.join(directory2, pattern+".txt")
    if not os.path.exists(directory2):
        os.makedirs(directory2)
        f3 = open(completeName, "w")
        Registrant_emails= get_Registrant_emails(url, name) # getting the domain names for each given email
        if Registrant_emails == None:
            pass
        else:
            table_list=[]
            for email in Registrant_emails:
                start = urllib2.urlopen("http://viewdns.info/reversewhois/?q=+%s" % email)# parsing the website and inputting each email individually
                soup = BeautifulSoup(start.read())
                general=soup.findAll('table',attrs={'border':'1'})
                for te in general:
                    td = te.findAll("td")# getting the row content of the table
                    for t in td:
                        table_list.append(t.text)
            for i in xrange(0,len(table_list),3):
                f3.write("%s \n" %table_list[i])# getting only the domain name
            f3.close()
            return "%s Blacklist Domains Database has been created in the directory %s" %(name,completeName)

    else:
        if not os.path.exists(completeName):
            f4 = open(completeName, "w")
            Registrant_emails= get_Registrant_emails(url, name) # getting the domain names for each given email
            if Registrant_emails == None:
                pass
            else:
                table_list=[]
                for email in Registrant_emails:
                    start = urllib2.urlopen("http://viewdns.info/reversewhois/?q=+%s" % email)# parsing the website and inputting each email individually
                    soup = BeautifulSoup(start.read())
                    general=soup.findAll('table',attrs={'border':'1'})
                    for te in general:
                        td = te.findAll("td")# getting the row content of the table
                        for t in td:
                            table_list.append(t.text)
                for i in xrange(0,len(table_list),3):
                    f4.write("%s \n" %table_list[i])# getting only the domain name
                f4.close()
                return "%s Blacklist Domains Database has been created in the directory %s" %(name,completeName)



database = open("domain_database.txt", "r").readlines()
for web in database:
    website= web.split()[0]
    filing= website.split(".")[0]
    print get_whois_domain(website,filing)
    print get_all_domains(website, filing) # by calling this func, it will create all the data set in a separate directory.






