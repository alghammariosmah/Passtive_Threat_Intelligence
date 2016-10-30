The program works as follows:
Assuming that you have a database for the websites that you want to get:
	1- Whois information of the domain 
	2- e-mail addresses in the whois record 
	3- all domain names ofthe Registrant Name or Email Address (by parsing http://viewdns.info/reversewhois/)
So, the program creates a text file for each website given in the domain database file. 
There are some libraries that Python provides in order to run this program properly which are:
	* pythonwhois
	* urllib2
	* BeautifulSoup
Pythonwhois: provides a well organized whois inquiry. 
urllib2: a tool for parsing any website
Beautifulsoup: a tool to parse an HTML website in a practical easy way. 


*Problem-solution adjustment:
Probelm: Registered e-mail contains same e-mail addresses, so it creates duplicate or more records as seen in cargill domains:
Solution: All duplicate emails have been terminated.

problem: The script should take parameters like companyname, verbose  ...
Solution: All company details are saved in a separate directory. 

Probelm: Output of a domain should go under a folder, at the end there will be lots of files under this folders!
Solution: According to the directory that you will give, the directory and the database will be created by the program.

problem: abuse contact e-mail may not be in the first order, be careful while terminating it.
Solution: Abuse e-mail has been added along with the other e-mails.

**Note: make sure to add your desired directory, I put it in the begginning of the codes so you can put it. 