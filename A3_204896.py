import psycopg2, random, time, uuid, array, math, sys, string

#operation 1  ✔
def drop_tables():
    try:
        cur.execute("""DROP TABLE IF EXISTS \"Course\"""")
        cur.execute("""DROP TABLE IF EXISTS \"Professor\"""")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    conn.commit()
    
#operation 2  ✔
def create_tables():
    
    commands = (
        """
        CREATE TABLE \"Professor\" (
            id INT PRIMARY KEY,
            name CHAR(50) NOT NULL,
            address CHAR(50) NOT NULL,
            age INT,
            height FLOAT
        )
        """,
        """
        CREATE TABLE \"Course\" (
                cid CHAR(25) PRIMARY KEY NOT NULL,
                title CHAR(50) NOT NULL,
                area CHAR(30) NOT NULL,
                instructor INT REFERENCES \"Professor\"(id) ON DELETE CASCADE
        )
        """,
    )
    
    try:
        for command in commands:
            cur.execute(command)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    conn.commit()

#operation 3  ✔
def insert_professor():
    query = "INSERT INTO \"Professor\" (id, name, address, age, height) VALUES(%s, %s, %s, %s, %s)"
    
    tuple = [
        0,
        "gigi",
        "gigi",
        20,
        180,
    ]
    
    #ID
    #array_id = [1] * times
    for i in range(times):
        array_id[i]= i
    random.shuffle(array_id)
    
    #NAME
    stringLength = 5
    #array_name = ["x"]*times
    for i in range(times):
        letters = string.ascii_lowercase
        array_name[i]=''.join(random.choice(letters) for i in range(stringLength))
    
    #ADDRESS
    #using same array as NAME
    
    #AGE
    array_age = [1.1] * times
    for i in range(times):
        array_age[i]= random.randint(25, 80)
    
    #HEIGHT
    height = 120
    array_height = [1.1] * times
    for i in range(times):
        array_height[i]= height + (0.0001*i)
    random.shuffle(array_height)
    array_height[times-1] = 185
    
    try:
        for i in range(times):
            tuple[0] = array_id[i]
            tuple[1] = array_name[i]
            tuple[2] = array_name[times-i-1]
            tuple[3] = array_age[i]
            tuple[4] = array_height[i]
            cur.executemany(query, (tuple,))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    conn.commit()
    return(array_name)

#operation 4  ✔
def insert_course():
    query = "INSERT INTO \"Course\"(cid, title, area, instructor) VALUES(%s, %s, %s, %s)"
              
    tuple = [
        "gigi",
        "gigino",
        "gigetto",
        0,
    ]
    
    #CID
    array_cid = ["x"] * times
    for i in range(times):
        array_cid[i]= str(i)
    random.shuffle(array_cid)
    
    #TITLE
    #using same array as NAME
        
    #AREA 
    #using same array as NAME
    random.shuffle(array_name)
    
    #INSTRUCTOR
    #using same array as ID
    random.shuffle(array_id)

    try:
        for i in range(times):
            tuple[0] = array_cid[i]
            tuple[1] = array_name[i] #array_title
            tuple[2] = array_name[i] #array_area
            tuple[3] = array_id[i]   #array_instructor
            
            cur.executemany(query, (tuple,)) 
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
         
    conn.commit()

#operation 5  ✔
def print_professor1():
    try:
        sql = "SELECT id FROM \"Professor\""
        cur.execute(sql)
        records = cur.fetchall()
        
        for row in records:
            sys.stderr.write(str(row[0]) + "\n")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    conn.commit()

#operation 6  ✔
def update_height1():
    try:
        sql = """UPDATE \"Professor\"
                SET height = %s
                WHERE height = %s"""
        cur.execute(sql, (200, 185))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    conn.commit()
    
#operation 7  ✔
def print_professor3():
    try:
        sql = "SELECT id, address FROM \"Professor\""
        cur.execute(sql)
        sql = cur.fetchall()
        
        for row in sql:
            print(row[0], row[1],file=sys.stderr)
          
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    conn.commit()
    
#operation 8  ✔
def Btree():
    try:
        sql = "CREATE INDEX name ON \"Professor\" USING btree (height);"
        cur.execute(sql)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    conn.commit()
    
#operation 9  ✔
def print_professor4():
    try:
        sql = "SELECT id FROM \"Professor\""
        cur.execute(sql)
        records = cur.fetchall()
        
        for row in records:
            print(row[0], file=sys.stderr)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    conn.commit()

#operation 10 ✔
def update_height2():
    try:
        sql = """UPDATE \"Professor\"
                SET height = %s
                WHERE height = %s"""
        cur.execute(sql, (210, 200))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    conn.commit()
      
#operation 11 ✔
def print_professor5():
    try:
        sql = "SELECT id, address FROM \"Professor\" WHERE height = 210"
        cur.execute(sql)
        sql = cur.fetchall()
        
        for row in sql:
            print(row[0], row[1], file=sys.stderr)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    conn.commit()

if __name__ == '__main__':
    
    #-----------CONNECTION TO THE POSTGRE DATABASE SERVER-------------#
    
    conn = None
    try:
        # PostgreSQL
        #params = {'host': 'sci-didattica.unitn.it', 'database': 'db_197', 'user': 'db_197', 'password': 'secret_197'}
        
        #LOCAL
        params = {'host': 'localhost', 'database': 'postgres', 'user': 'postgres', 'password': 'Softair10'}
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    #-----------------------------------------------------------------#
    
    times = 1000000
    
    array_id = [1] * times
    array_name = ["x"] * times
    
    #cronometri
    start_time = time.time_ns()
    end_time = time.time()
    
    #------------------------------START------------------------------#
    
    #operation 1
    drop_tables()
    sys.stdout.write("Step 1 needs " + (str(time.time_ns() - start_time)) + " ns" + "\n")
    start_time = time.time_ns()
    
    #operation 2
    create_tables()
    sys.stdout.write("Step 2 needs " + (str(time.time_ns() - start_time)) + " ns" + "\n")
    start_time = time.time_ns()
    
    #operation 3
    insert_professor()
    sys.stdout.write("Step 3 needs " + (str(time.time_ns() - start_time)) + " ns" + "\n")
    start_time = time.time_ns()
    
    #operation 4
    insert_course()
    sys.stdout.write("Step 4 needs " + (str(time.time_ns() - start_time)) + " ns" + "\n")
    start_time = time.time_ns()
    
    #operation 5
    print_professor1()
    sys.stdout.write("Step 5 needs " + (str(time.time_ns() - start_time)) + " ns" + "\n")
    start_time = time.time_ns()
    
    #operation 6
    update_height1()
    sys.stdout.write("Step 6 needs " + (str(time.time_ns() - start_time)) + " ns" + "\n")
    start_time = time.time_ns()
    
    #operation 7
    print_professor3()
    sys.stdout.write("Step 7 needs " + (str(time.time_ns() - start_time)) + " ns" + "\n")
    start_time = time.time_ns()
    
    #operation 8
    Btree()
    sys.stdout.write("Step 8 needs " + (str(time.time_ns() - start_time)) + " ns" + "\n")
    start_time = time.time_ns()
    
    #operation 9
    print_professor4()
    sys.stdout.write("Step 9 needs " + (str(time.time_ns() - start_time)) + " ns" + "\n")
    start_time = time.time_ns()
    
    #operation 10
    update_height2()
    sys.stdout.write("Step 10 needs " + (str(time.time_ns() - start_time)) + " ns" + "\n")
    start_time = time.time_ns()
    
    #operation 11
    print_professor5()
    sys.stdout.write("Step 11 needs " + (str(time.time_ns() - start_time)) + " ns" + "\n")
    start_time = time.time_ns()
    
    #-------------------------------END-------------------------------#
    
    #REQUIRED TIME TO RUN THE WHOLE PROGRAM
    #sys.stdout.write("\n" + "\n" + "il tempo totale richiesto è " + (str(time.time() - end_time)) + " secondi" + "\n" + "\n" + "\n")
    
    #-----------------------------------------------------------------#
    
    cur.close()
    conn.close()
    
    #-----------------------------------------------------------------#
