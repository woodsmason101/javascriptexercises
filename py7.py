# Create a mapping of state to abbreviation
# Add Oklahoma and Texas to the end of the list.
states = {'Oregon': 'OR',
          'Florida': 'FL',
          'California': 'CA',
          'New York': 'NY',
          'Michigan': 'MI'}
states['Oklahoma'] = 'OK'
states['texas'] = 'TX'
cities = {'CA': 'San Francisco',
          'MI': 'Detroit', 
          'FL': 'Jacksonville'}  
#add the rest of the cities here including Oklahoma and Texas

cities ['NY'] = 'New York'
cities ['OR'] = 'Portland'
cities ['CA'] = 'San Fransico'
cities ['MI'] = 'Detroit'
cities ['OK'] = 'Tulsa'
cities ['TX'] = 'Houston'
cities ['FL'] = 'Jacksonville'
# Print out all the cities
print ('-' * 20)
print ("NY State has: ", cities['NY'])
print ("CA State has: ", cities['CA'])
print ("OK State has: ", cities['OK'])
print ("OR State has: ", cities['OR'])
print ("MI State has: ", cities['MI'])
print ("TX State has: ", cities['TX'])
print ("FL State has: ", cities['FL'])
# Print out all the states
print ('-' * 20)
print ("Michigan's abbreviation is: ", states['Michigan'])
print ("Oklahoma's abbreviation is: ", states['Oklahoma'])
print ("New York's abbreviation is: ", states['New York'])
print ("California's abbreviation is: ", states['California'])
print ("Michigan's abbreviation is: ", states['Michigan'])
print ("Florida's abbreviation is: ", states['Florida'])
print ("Oregon's abbreviation is: ", states['Oregon'])
