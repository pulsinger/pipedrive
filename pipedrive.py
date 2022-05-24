def getData(limit,start=0, df=pd.DataFrame()):
       
       url_api = 'https://bbcsystems.pipedrive.com/v1/'+str(endpoint)+'?start='+str(start)+'&limit='+str(limit)+'&api_token='+str(api_pd_token)                   # creating url string
              
       res = requests.get(url_api)               # response
       content = json.loads(res.content)         # convert JSON response to python DICT

       if len(content['data']) == 0:
              print("No data present")
       else:  
              data = content['data']                                                                                                 # use only data field as dataframe
                                                      
              temp_df = pd.DataFrame(data)                                                                                           # create first dataframe to append to
              df = df.append(temp_df,ignore_index=True)                                                                              # appending new dataframe for each request                     
                       
              #df.to_csv("Data_test.csv",mode='a',index=False,header=False) 
                                                                                                     
              if len(content['data']) >0 and content['additional_data']['pagination']['more_items_in_collection'] == True:
                    df = df.append(getData(limit+500, content['additional_data']['pagination']['next_start'],df))                              # next start adds 500 entries automatically and appends to dataframe

                  
       return df                                  # return the appended dataframe
             
