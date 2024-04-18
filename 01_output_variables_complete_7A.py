import csv
import sqlite3

def process_csv(file_name):
    
    manufacture_list_to_include = ["MSI", "ASUS"]
    
    
    # with the file open
 
    
    
    with open(file_name, newline='', encoding='utf-8-sig') as csvfile:
        
        reader = csv.DictReader(csvFile)
        # delete all laptops
        query = "DELETE FROM laptops where 1"
        
        try:
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            cursor = execute(query)
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print(f"ERROR : {e}")
                    
        for row in reader:
            try:
                
                
                # if laptop is empty or
                #      inventory = 0 or
                #       manufacturer not in manufacture_list_to_include
                
                #    continue
                
                # get all the ratings.
                ratings = [float(row["CPU_RATING"]), float(row["GPU_RATING"]) ]

                # calculate value rating using algorithm in task sheet
                
                # value_rating = .... one of good / great / outstanding
                #  min_val = min(ratings)
                # max_val = max(rating)
                
                
                # ADD ROW TO DB
                # first values are attribute names from database 
                query = "INSERT INTO LAPTOP (LAPTOP, MANUFACTURER, INVENTORY, PRICE, CPU, GPU, " \
                        " MEMORY_DDR ) VALUES (?,?,? ...)
            
                # same number of question marks as table attributes
                data = [row['LAPTOP'], row['MANUFACTURER'] .... ]
                
                try:
                    conn = sqlite3.connect("database.db")
                    cursor = conn.cursor()
                    cursor = execute(query, data)
                    conn.commit()
                    conn.close()
                except sqlite3.Error as e:
                    print(f"ERROR : {e}")
                    
                    
                
                
            except KeyError as e:
                print("Key Error")