def getUserResults(Username,marks1,marks2,Tied):
    "creatiing the database"
    import mysql.connector
    from prettytable import from_db_cursor

#open database connection with a dictionary
    conDict={"host":"localhost","user":"root","database":"gamedata","password":""}

    db=mysql.connector.connect(**conDict)
    
#prepare a cusor object using cursor()method
    cursor=db.cursor()
    cursor.execute("SELECT * FROM gameresults")
    gameplay=from_db_cursor(cursor)
    print(gameplay)
    
#styling the html table and setting the html attributes    
    data=gameplay.get_html_string(attributes={"name":"gameResults","class":"table"},format=True)
    
#open and record the data to an html file
    f=open("Result.html","w")
    f.write(data)
    

#execute sql query using execute()method
    updateText="INSERT INTO gameresults VALUES ('"+Username+"','"+marks1+"','"+marks2+"','"+Tied+"')"
    cursor.execute(updateText)
    
#commit the change    
    db.commit()
    
#disconnect from the server    
    db.close()
    return
