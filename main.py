import requests
from rich.console import Console
from rich.table import Table



url="https://restcountries.com/v2/all"

res = requests.get(url)

data = res.json()

text_art = r"""
███╗  ██╗███╗   ██╗ ██████╗ ██╗    ██╗    ███████╗██╗   ██╗███████╗██████╗ ██╗   ██╗████████╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
███║ ██╔╝████╗  ██║██╔═══██╗██║    ██║    ██╔════╝██║   ██║██╔════╝██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██║████╗  ██║██╔════╝ 
██████╔╝ ██╔██╗ ██║██║   ██║██║ █╗ ██║    █████╗  ██║   ██║█████╗  ██████╔╝ ╚████╔╝    ██║   ███████║██║██╔██╗ ██║██║  ███╗
███╔═██╗ ██║╚██╗██║██║   ██║██║███╗██║    ██╔══╝  ╚██╗ ██╔╝██╔══╝  ██╔══██╗  ╚██╔╝     ██║   ██╔══██║██║██║╚██╗██║██║   ██║
███║  ██╗██║ ╚████║╚██████╔╝╚███╔███╔╝    ███████╗ ╚████╔╝ ███████╗██║  ██║   ██║      ██║   ██║  ██║██║██║ ╚████║╚██████╔╝
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚══╝╚══╝     ╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                                                                          
"""
print(text_art)
print(" ")
country = input("enter your country name to fetch its details:")
country=country.capitalize()

for i in data:

    if i["name"]==country:

        print("")
        print(''' **** congratulation your country is present in our database ****
            |--- press 0 for exit
            |--- press 1 for view domain of this nation ----|
            |--- press 2 for view capital of this nation ----|
            |--- press 3 for view region of this nation ----|
            |--- press 4 for view subregion of this nation ----|
            |--- press 5 for view total population of this nation ----|
            |--- press 6 for view total area of this nation in km square ----|
            |--- press 7 for view timezone of this nation ----|
            |--- press 8 for view share border of this nation ----|
            |--- press 9 for view currency of this nation ----|
            |--- press 10 for view languages spoken in this nationie ----|
            |--- press 11 for view regionalBlocs of this nation ----|
            |--- press 12 for view nativeName of this nation ----|
            ''')
        while True:
            print(" ")
            choice=int(input("enter your choice :"))
            if choice==1:
                x=i['topLevelDomain']
                domain = "domain of {} is :{}".format(country,x)
                print(domain)
            elif choice==2:
                x=i['capital']
                capital = "capital of {} is :{}".format(country,x)
                print(capital)
            elif choice==3:
                x=i['region']
                region = "region of {} is :{}".format(country,x)
                print(region)
            elif choice==4:
                x=i['subregion']
                subregion = "subregion of {} is :{}".format(country,x)
                print(subregion)
            elif choice==5: 
                x=i['population']
                population = "population of {} is :{}".format(country,x)
                print(population)
            elif choice==6:
                x=i['area']
                area = "The total area of {} is :{} in km square".format(country,x)
                print(area)
            elif choice==7:
                x=i['timezones']
                timezone = "timezone of {} is :{}".format(country,x)
                print(timezone)
            elif choice==8:
                x=i['borders']
                sharedBorders = "shared border of {} with these countries :{}".format(country,x)
                print(sharedBorders)
                print(sharedBorders)
            elif choice==9:
                x=i['currencies']
                currency = "currency of {} is :{}".format(country,x)
                print(currency)
            elif choice==10:
                x=i['languages']
                language = "languages spoken in {} is :{}".format(country,x)
                print(language)
            elif choice==11:
                x=i['regionalBlocs']
                regionalBlocs = "regionalBlocs of  {} is :{}".format(country,x)
                print(regionalBlocs)
            elif choice==12:
                x=i['nativeName']
                nativeName = "nativeName {} is :{}".format(country,x)
                print(nativeName)
            elif choice==0:
                exit()
            elif choice == 99:
                
                x=i['topLevelDomain']
                domain = "domain of {} is :{}".format(country,x)
                
                x=i['capital']
                capital = "capital of {} is :{}".format(country,x)
                
                x=i['region']
                region = "region of {} is :{}".format(country,x)
                
                x=i['subregion']
                subregion = "subregion of {} is :{}".format(country,x)
                
                x=i['population']
                population = "population of {} is :{}".format(country,x)
                
                x=i['area']
                area = "The total area of {} is :{} in km square".format(country,x)
                
                x=i['timezones']
                timezone = "timezone of {} is :{}".format(country,x)
                
                x=i['borders']
                sharedBorders = "shared border of {} with these countries :{}".format(country,x)
                
                x=i['currencies']
                currency = "currency of {} is :{}".format(country,x)
                
                x=i['languages']
                language = "languages spoken in {} is :{}".format(country,x)
                
                x=i['regionalBlocs']
                regionalBlocs = "regionalBlocs of  {} is :{}".format(country,x)
                
                x=i['nativeName']
                nativeName = "nativeName {} is :{}".format(country,x)
                
                table = Table(title="Country's Info")

                table.add_column("Domain", justify="right", style="cyan")
                table.add_column("Capital", style="magenta")
                table.add_column("Region", justify="right", style="green")
                table.add_column("Sub-region", justify="right", style="cyan")
                table.add_column("Population", style="magenta")
                table.add_column("Area", justify="right", style="green")
                table.add_column("Timezone", justify="right", style="cyan")
                table.add_column("Shared Border", style="magenta")
                table.add_column("Currency", justify="right", style="green")
                table.add_column("Languages", justify="right", style="cyan")
                table.add_column("Region Blocs", style="magenta")
                table.add_column("Native Name", justify="right", style="green")

                table.add_row(domain, capital, region, subregion, population, area, timezone, sharedBorders, currency, language, regionalBlocs, nativeName)
                #table.expand(True)

                console = Console()
                console.print(table)
            else:
                print("enter a valid input")


print("sorry this api did not have this country details")