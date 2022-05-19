api_pd_token = ''
endpoint = 'organizations'

def getData(limit,start=0):
       
       url_api = 'https://bbcsystems.pipedrive.com/v1/'+str(endpoint)+'?start='+str(start)+'&limit='+str(limit)+'&api_token='+str(api_pd_token)
              
       res = requests.get(url_api)               # response
       content = json.loads(res.content)         # convert JSON response to python DICT

       data=[]                                   # create empty list
       

       if len(content['data']) == 0:
              print("No more data")
       else:  
              data = content['data']
              for i in range(len(data)): 
                     df = pd.DataFrame(data)                                       # convert do pandas dataframe
                     df.to_csv("Data_"+df['name'][0]+".csv")                       # export each page to separate .csv
                            
              
              #print(df['name'][0])
              print(len(data))
              print(url_api)
              #df = pd.DataFrame(data)
              
              if len(content['data']) >0 and content['additional_data']['pagination']['more_items_in_collection'] == True:
                     data.append(getData(limit+500, content['additional_data']['pagination']['next_start']))                                               #  next start adds 500 automatically

                  
       
       #print(len(df))

       return df
