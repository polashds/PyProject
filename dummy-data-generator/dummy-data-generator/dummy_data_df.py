from faker import Faker 
import pandas as pd 

fake = Faker() 

# Generate a list of fake profiles
profiles = [fake.simple_profile() for i in range(10)] 

#Generate a dataframe using pandas 
df = pd.DataFrame(profiles) 
print(df) 