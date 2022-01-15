#create list
Grocery_list = ["Milk", "Eggs", "Flour","CC"]
#print(Grocery_list)
#add sugar
Grocery_list.append("sugar")
#print(Grocery_list)
#add vanilla
Grocery_list.append("Vanilla")
#print(Grocery_list)
#Substitute butterscotch chips for CC
Grocery_list[3] = "Butterscotch chips"
#print(Grocery_list)

counties = ["Arapahoe","Denver","Jefferson"]
#if counties[1] == 'Denver':
#    print(counties[1])
#if counties[3] != 'Jefferson':
#    print(counties[2])
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")
    if "Arapahoe" in counties or "El Paso" in counties:
        print("Arapahoe and El Paso are in the list of counties.")
    else:
        print("Arapahoe and El Paso is not in the list of counties.")
for county in counties:
    print(county)
    
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#for county in counties_dict.keys(): 
    #print(county)

#for voters in counties_dict.values():
    #print(voters)

#for county in counties_dict:
    #print(counties_dict[county])

#for key, value in counties_dict.items():
    #print(key, value)

for key, value in counties_dict.items():
    print(key, "county has", value, "registered voters.")
    #HAHAYEAH MOTHERFUCKERS!
    
voting_data = [{'county': 'Arapahoe', 'registered_voters': 422829},
 {'county': 'Denver', 'registered_voters': 463353}, 
 {'county': 'Jefferson', 'registered_voters': 432438}]
 
#for county_dict in voting_data:
    #print(county_dict)

for i in range(len(voting_data)):
    print(voting_data[i]['county'])

#for county_dict in voting_data:
    #for value in county_dict.values():
        #print(value)

#for county_dict in voting_data:
    #for key, value in county_dict.items():
        #print(county_dict['county'])

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#for county, registered_voters in voting_data:
    #print(f"{county} county has {registered_voters} registered voters.")

#print(f"{voting_data[county]} county has {voting_data[registered_voters]} registered voters.")