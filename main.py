#!/usr/bin/env python3
import sqlite3
import os
import sys
import readline
def rlinput(prompt, prefill=''):
   readline.set_startup_hook(lambda: readline.insert_text(prefill))
   try:
      return raw_input(prompt)
   finally:
      readline.set_startup_hook()


#******************************** Get DATA *******************************
i=0
ITEM_ID = str()
ITEM_NAME_VALUE = str()
ITEM_CATEGORY = str()
ITEM_BEGIN = str()
ITEM_EXPIRE = str()
ITEM_QUANTITY = str()
ITEM_UNIT = str()
ITEM_PLACE = str()
REC_ID = str()
REC_NAME_VALUE = str()
REC_CATEGORY = str()
REC_ING = {"ingredients":[], "amounts":[], "units":[]}
REC_INS = str()
REC_TIME = str()
REC_UNIT = str()
REC_PLACE = str()
RI_ING = str()
THE_ING = str()
RI_AMOUNT = str()
THE_AMOUNT = str()
RI_UNIT = str()
THE_UNIT = str()

argv_len = len(sys.argv)

#conn  = sqlite3.connect('test.db')
#c = conn.cursor()

def Get_data(subarg):
	global i
	global j
	i=1
	conn  = sqlite3.connect('test.db')
	c = conn.cursor()
	#global c
	if subarg == "id":
		cursor = conn.execute("SELECT * FROM Things") 
	if subarg == "nam":
		cursor = conn.execute("SELECT * FROM Things ORDER BY item_name ASC")
	if subarg == "cat":
		cursor = conn.execute("SELECT * FROM Things ORDER BY item_category ASC")
	if subarg == "beg":
		cursor = conn.execute("SELECT * FROM Things ORDER BY item_begin ASC")
	if subarg == "exp":
		cursor = conn.execute("SELECT * FROM Things ORDER BY item_expire ASC")
	if subarg == "qua":
		cursor = conn.execute("SELECT * FROM Things ORDER BY item_quantity ASC")
	if subarg == "uni":
		cursor = conn.execute("SELECT * FROM Things ORDER BY item_unit ASC")
	if subarg == "pla":
		cursor = conn.execute("SELECT * FROM Things ORDER BY item_place ASC")
	print(    "{: >3} {: >20} {: >10} {: >11} {: >11} {: >5} {: >5} {: >10}\n".format("ID","NAME","CATEGORY","BEGIN","EXPIRE","QUANT","UNIT","PLACE"))
	for row in cursor: 
		print("{: >3} {: >20} {: >10} {: >11} {: >11} {: >5} {: >5} {: >10}\n".format(*row))
		#print(row)

def Insert_data():
	conn  = sqlite3.connect('test.db')
	c = conn.cursor()
	global ITEM_ID

	conn  = sqlite3.connect('test.db')
	c = conn.cursor()	
	i = 1
	try:
		cursor = conn.execute("SELECT * FROM Things") 
		for row in cursor: 
			i = i + 1
		ITEM_ID = i
	except:
		pass
	c.execute('CREATE TABLE IF NOT EXISTS Things (item_id text,item_name text,item_category text,item_begin text,item_expire text,item_quantity text,item_unit text,item_place text)')
	conn.commit()
	c.execute("INSERT INTO Things (item_id,item_name,item_category,item_begin,item_expire,item_quantity,item_unit,item_place) VALUES(?, ?, ?, ?, ?, ?, ?, ? )", (ITEM_ID , ITEM_NAME_VALUE , ITEM_CATEGORY , ITEM_BEGIN , ITEM_EXPIRE , ITEM_QUANTITY , ITEM_UNIT , ITEM_PLACE))
	#c.execute("INSERT INTO stock VALUES ( ITEM_ID , ITEM_NAME_VALUE , ITEM_CATEGORY , ITEM_BEGIN , ITEM_EXPIRE , ITEM_QUANTITY , ITEM_UNIT , ITEM_PLACE )")
	conn.commit()

def Update_data():
	conn  = sqlite3.connect('test.db')
	c = conn.cursor()
	#global c
	c.execute('UPDATE Things SET item_name = ?, item_category = ?, item_begin = ?,item_expire = ?, item_quantity = ?,item_unit = ?,item_place = ? WHERE item_id = ?', (ITEM_NAME_VALUE , ITEM_CATEGORY , ITEM_BEGIN , ITEM_EXPIRE , ITEM_QUANTITY , ITEM_UNIT , ITEM_PLACE,  ITEM_ID))
	conn.commit()

def Delete_data():
	conn  = sqlite3.connect('test.db')
	c = conn.cursor()
	#global c
	c.execute('delete from Things where item_id = ?',( ITEM_ID))
	try:
		c.execute('create table temp_Things as select item_id,item_name,item_category,item_begin,item_expire,item_quantity,item_unit,item_place from Things order by item_id')
	except:
		pass
	c.execute('drop table Things')
	c.execute('CREATE TABLE IF NOT EXISTS Things (item_id text,item_name text,item_category text,item_begin text,item_expire text,item_quantity text,item_unit text,item_place text)')
	c.execute("INSERT INTO Things (item_id,item_name,item_category,item_begin,item_expire,item_quantity,item_unit,item_place) select rowid,item_name,item_category,item_begin,item_expire,item_quantity,item_unit,item_place from temp_Things order by rowid")
	conn.commit()

#********************************************** RECIPRES

def Get_recipe(subarg):
	global i
	global j
	i=1
	conn  = sqlite3.connect('test.db')
	c = conn.cursor()
	#global c
	if subarg == "id":
		cursor = conn.execute("SELECT * FROM Recipes") 
	if subarg == "nam":
		cursor = conn.execute("SELECT * FROM Recipes ORDER BY item_name ASC")
	if subarg == "cat":
		cursor = conn.execute("SELECT * FROM Recipes ORDER BY item_category ASC")
	#if subarg == "beg":
	#	cursor = conn.execute("SELECT * FROM Recipes ORDER BY item_begin ASC")
	#if subarg == "exp":
	#	cursor = conn.execute("SELECT * FROM Recipes ORDER BY item_expire ASC")
	#if subarg == "qua":
	#	cursor = conn.execute("SELECT * FROM Recipes ORDER BY item_quantity ASC")
	#if subarg == "uni":
	#	cursor = conn.execute("SELECT * FROM Recipes ORDER BY item_unit ASC")
	#if subarg == "pla":
	#	cursor = conn.execute("SELECT * FROM Recipes ORDER BY item_place ASC")
	#print(    "{: >3} {: >20} {: >10} {: >11} {: >11} {: >5} {: >5} {: >10}\n".format("ID","NAME","CATEGORY","BEGIN","EXPIRE","QUANT","UNIT","PLACE"))
	for row in cursor: 
		#print("{: >3} {: >20} {: >10} {: >11} {: >5} {: >5} {: >10}\n".format(*row))
		print(row)

def Insert_recipe():
	#global REC_ID
	conn  = sqlite3.connect('test.db')
	c = conn.cursor()
	#global c

	conn  = sqlite3.connect('test.db')
	c = conn.cursor()	
	i = 1
	try:
		cursor = conn.execute("SELECT * FROM Recipes") 
		for row in cursor: 
			i = i + 1
		REC_ID = i
	except:
		pass
	c.execute('CREATE TABLE IF NOT EXISTS Recipes (rec_id text,rec_name text,rec_category text,rec_ingredients text,rec_instruction text,rec_time text,rec_unit text,rec_place text)')
	c.execute('CREATE TABLE IF NOT EXISTS Rec_Ing (rec_id text, ri_ing text, ri_amount text, ri_unit)')
	c.execute('CREATE TABLE IF NOT EXISTS Ings (ri_ing text, the_ing text)')
	c.execute('CREATE TABLE IF NOT EXISTS Amounts (ri_amount text, the_amount text)')
	c.execute('CREATE TABLE IF NOT EXISTS Units (ri_unit text, the_unit text)')
	conn.commit()

	c.execute("INSERT INTO Recipes (rec_id,rec_name,rec_category,rec_instruction,rec_time,rec_unit,rec_place) VALUES(?, ?, ?, ?, ?, ?, ? )", (REC_ID , REC_NAME_VALUE , REC_CATEGORY , REC_INS , REC_TIME , REC_UNIT , REC_PLACE))
	
	for indexing, ing_row in enumerate(REC_ING["ingredients"]):
		RI_ING = REC_ING["ingredients"][indexing]
		RI_AMOUNT = REC_ING["amounts"][indexing]
		RI_UNIT = REC_ING["units"][indexing]
		c.execute("INSERT INTO Rec_ing (rec_id, ri_ing, ri_amount, ri_unit) VALUES(?, ?, ?, ? )", (REC_ID, RI_ING, RI_AMOUNT, RI_UNIT))
	
	for indexing, ing_row in enumerate(REC_ING["ingredients"]):
		RI_ING = REC_ING["ingredients"][indexing]
		c.execute("INSERT INTO Ings (ri_ing, the_ing) VALUES(?, ? )", (RI_ING, THE_ING))
	
	for indexing, ing_row in enumerate(REC_ING["amounts"]):
		RI_AMOUNT = REC_ING["amounts"][indexing]
		c.execute("INSERT INTO Amounts (ri_amount, the_amount) VALUES(?, ? )", (RI_AMOUNT, THE_AMOUNT))
	
	for indexing, ing_row in enumerate(REC_ING["units"]):
		RI_UNIT = REC_ING["units"][indexing]
		c.execute("INSERT INTO Units (ri_unit, the_unit) VALUES(?, ? )", (RI_UNIT, THE_UNIT))
	
	
	
	
	
	#####
	#c.execute("INSERT INTO stock VALUES ( ITEM_ID , ITEM_NAME_VALUE , ITEM_CATEGORY , ITEM_BEGIN , ITEM_EXPIRE , ITEM_QUANTITY , ITEM_UNIT , ITEM_PLACE )")
	conn.commit()

def Update_recipe():
	conn  = sqlite3.connect('test.db')
	c = conn.cursor()
	#global c
	c.execute('UPDATE Recipes SET rec_name = ?,rec_category = ?,rec_ingredients = ?,rec_instruction = ?,rec_time = ?,rec_unit = ?,rec_place = ? WHERE item_id = ?', (ITEM_NAME_VALUE , ITEM_CATEGORY , ITEM_BEGIN , ITEM_EXPIRE , ITEM_QUANTITY , ITEM_UNIT , ITEM_PLACE,  ITEM_ID))
	conn.commit()

def Delete_recipe():
	global REC_ID
	conn  = sqlite3.connect('test.db')
	c = conn.cursor()
	#global c
	
	cursor = conn.execute("SELECT * FROM Recipes")
	check = 0
	RI_ING = str()
	RI_AMOUNT = str()
	RI_UNIT = str()
	for index,row in enumerate(cursor): 
		for index2, column in enumerate(row):
			
			#print(index2)
			if index2 == 0:
				if column == REC_ID:
					check = 1
			if index2 == 1:
				if check == 1:
					RI_ING = column
			if index2 == 2:
				if check == 1:
					RI_AMOUNT = column
			if index2 == 3:
				if check == 1:
					RI_UNIT = column
				check = 0



	c.execute('delete from Ings where ri_ing = ?',( [RI_ING]))
	try:
		c.execute('create table temp_Ings as select ri_ing, the_ing from Ings order by ri_ing')
	except:
		pass
	c.execute('drop table Ings')
	c.execute('CREATE TABLE IF NOT EXISTS Ings (ri_ing text, the_ing text)')
	c.execute("INSERT INTO Ings (ri_ing, the_ing) VALUES(?, ? )", (RI_ING, THE_ING))


	c.execute('delete from Amounts where ri_amount = ?',( [RI_AMOUNT]))
	try:
		c.execute('create table temp_Units as select ri_amount, the_amount from Ings order by ri_amount')
	except:
		pass
	c.execute('drop table Amounts')
	c.execute('CREATE TABLE IF NOT EXISTS Amounts (ri_amount text, the_amount text)')
	c.execute("INSERT INTO Amounts (ri_amount, the_amount) VALUES(?, ? )", (RI_AMOUNT, THE_AMOUNT))


	c.execute('delete from Units where ri_unit = ?',( [RI_UNIT]))
	try:
		c.execute('create table temp_Units as select ri_ing, the_ing from Ings order by ri_ing')
	except:
		pass
	c.execute('drop table Units')
	c.execute('CREATE TABLE IF NOT EXISTS Units (ri_unit text, the_unit text)')
	c.execute("INSERT INTO Units (ri_unit, the_unit) VALUES(?, ? )", (RI_UNIT, THE_UNIT))

###
	c.execute('CREATE TABLE IF NOT EXISTS Rec_Ing (rec_id text, ri_ing text, ri_amount text, ri_unit)')
	c.execute('delete from Rec_Ing where rec_id = ?',( REC_ID))
	try:
		c.execute('create table temp_Rec_Ings as select rec_id text, ri_ing text, ri_amount text, ri_unit from Ings order by rec_id')
	except:
		pass
	c.execute('drop table Rec_Ing')
	c.execute('CREATE TABLE IF NOT EXISTS Rec_Ing (rec_id text, ri_ing text, ri_amount text, ri_unit)')
	c.execute("INSERT INTO Rec_Ing (rec_id, ri_ing, ri_amount, ri_unit) VALUES(?, ?, ?, ?)", (REC_ID, RI_ING, RI_AMOUNT, RI_UNIT))

	
	c.execute('delete from Recipes where rec_id = ?',( REC_ID))
	try:
		c.execute('create table temp_Recipes as select rec_id,rec_name,rec_category,rec_instruction,rec_time,rec_unit,rec_place from Recipes order by rec_id')
	except:
		pass
	c.execute('drop table Recipes')
	c.execute('CREATE TABLE IF NOT EXISTS Recipes (rec_id text,rec_name text,rec_category text,rec_instruction text,rec_time text,rec_unit text,rec_place text)')
	c.execute("INSERT INTO Recipes (rec_id,rec_name,rec_category,rec_instruction,rec_time,rec_unit,rec_place) select rowid,rec_name,rec_category,rec_instruction,rec_time,rec_unit,rec_place from temp_Recipes order by rowid")
	
	
	
	
	#####
	#c.execute("INSERT INTO stock VALUES ( ITEM_ID , ITEM_NAME_VALUE , ITEM_CATEGORY , ITEM_BEGIN , ITEM_EXPIRE , ITEM_QUANTITY , ITEM_UNIT , ITEM_PLACE )")
	conn.commit()


###
	c.execute('delete from Recipes where rec_id = ?',( REC_ID))
	try:
		c.execute('create table temp_Recipes as select rec_id,rec_name,rec_category,rec_ingredients,rec_instruction,rec_time,rec_unit,rec_place from Recipes order by rec_id')
	except:
		pass
	c.execute('drop table Recipes')
	c.execute('CREATE TABLE IF NOT EXISTS Recipes (rec_id text,rec_name text,rec_category text,rec_ingredients text,rec_instruction text,rec_time text,rec_unit text,rec_place text)')
	c.execute("INSERT INTO Recipes (rec_id,rec_name,rec_category,rec_instruction,rec_time,rec_unit,rec_place) select rowid,rec_name,rec_category,rec_instruction,rec_time,rec_unit,rec_place from temp_Recipes order by rowid")
	conn.commit()


if __name__=='__main__':
	#Get_data()
	#global c
	#conn  = sqlite3.connect('test.db')
	#c = conn.cursor()	
	#c.execute('CREATE TABLE IF NOT EXISTS RecordONE (item_id text,item_name text,item_category text,item_begin text,item_expire text,item_quantity text,item_Unit text,item_place text))')
	#try:
	#	c.execute('''CREATE TABLE stocks
	#		(item_id text,item_name text,item_category text,item_begin text,item_expire text,item_quantity text,item_Unit text,item_place text)''')
	#except:
	#	pass
	#conn.commit
	#conn.close
	dblength = i
	for x in range(0, argv_len):
		if sys.argv[x] == "-f":
			CLI_filename = sys.argv[x+1]
			filename = CLI_filename
			filenames.append(filename)
			filecheck = True
		if sys.argv[x] == "-h":
			print ('-h for help\n-f file\n-l list items\n-a add item\n-u update\n-d delete')
		if sys.argv[x] == "-a":
			ITEM_ID = str(dblength+1)
			try:
				ITEM_NAME_VALUE = input("Name of the item:")
				ITEM_CATEGORY = input("Category of the item:")
				ITEM_BEGIN = input("Start date:")
				ITEM_EXPIRE = input("Expiring date:")
				ITEM_QUANTITY = input("Quantity:")
				ITEM_UNIT = input("Unit:")
				ITEM_PLACE = input("Place:")
			except:
				ITEM_NAME_VALUE = raw_input("Name of the item:")
				ITEM_CATEGORY = raw_input("Category of the item:")
				ITEM_BEGIN = raw_input("Start date:")
				ITEM_EXPIRE = raw_input("Expiring date:")
				ITEM_QUANTITY = raw_input("Quantity:")
				ITEM_UNIT = raw_input("Unit:")
				ITEM_PLACE = raw_input("Place:")
			Insert_data()			
		if sys.argv[x] == "-d":
			ITEM_ID = sys.argv[x+1]  
			Delete_data()
		if sys.argv[x] == "-u":
			ITEM_ID = sys.argv[x+1]
			
			
			conn  = sqlite3.connect('test.db')
			cursor = conn.execute("SELECT * FROM Things") 
			c = conn.cursor()
			for index, row in enumerate(cursor): 
				nr = int(sys.argv[x+1])
				if index == (nr-1):
					for index2, cell in enumerate(row):
						if index2 == 1:					
							ITEM_NAME_VALUE = rlinput("Name of the item:",cell)
						if index2 == 2:
							ITEM_CATEGORY = rlinput("Category of the item:",cell)
						if index2 == 3:
							ITEM_BEGIN = rlinput("Start date:",cell)
						if index2 == 4:
							ITEM_EXPIRE = rlinput("Expiring date:",cell)
						if index2 == 5:
							ITEM_QUANTITY = rlinput("Quantity:",cell)
						if index2 == 6:
							ITEM_UNIT = rlinput("Unit:",cell)
						if index2 == 7:
							ITEM_PLACE = rlinput("Place:",cell)

			Update_data()
		if sys.argv[x] == "-l":
			subarg = str("id")
			try:
				if sys.argv[x+1] == "nam":
					subarg = str("nam")
				if sys.argv[x+1] == "cat":
					subarg = str("cat")
				if sys.argv[x+1] == "beg":
					subarg = str("beg")
				if sys.argv[x+1] == "exp":
					subarg = str("exp")
				if sys.argv[x+1] == "qua":
					subarg = str("qua")
				if sys.argv[x+1] == "uni":
					subarg = str("uni")
				if sys.argv[x+1] == "pla":
					subarg = str("pla")								
			except:
				pass
			Get_data(subarg)

		if sys.argv[x] == "-ra":
			ITEM_ID = str(dblength+1)
			try:
				count = 0 
				REC_NAME_VALUE = input("Name of the recipe:")
				REC_CATEGORY = input("Category of the recipe:")
				print("Ingredients:")
	        
				while 1:
					a_ing = input("name of ingredient" + str(count))	
					if a_ing == "" :
					  break
					REC_ING["ingredients"].append(a_ing)
					a_amount = input("amount of ingredient" + str(count))
					REC_ING["amounts"].append(a_amount)
					a_unit = input("unit of ingredient" + str(count))
					REC_ING["units"].append(a_unit)
					count += 1
	
				#REC_ING = input("Ingredients:")
				REC_INS = input("Instructions")
				REC_TIME = input("Quantity:")
				REC_UNIT = input("Unit:")
				REC_PLACE = input("Place:")
			except:
				REC_NAME_VALUE = raw_input("Name of the recipe:")
				REC_CATEGORY = raw_input("Category of the recipe:")
				print("Ingredients:")
	        
				while 1:
					a_ing = raw_input("name of ingredient" + str(count))	
					if a_ing == "" :
						break
					REC_ING["ingredients"].append(a_ing)
					a_amount = raw_input("amount of ingredient" + str(count))
					REC_ING["amounts"].append(a_amount)
					a_unit = raw_input("unit of ingredient" + str(count))
					REC_ING["units"].append(a_unit)
					count += 1
				#REC_ING = raw_input("Start date:")
				REC_INS = raw_input("Expiring date:")
				REC_TIME = raw_input("Quantity:")
				REC_UNIT = raw_input("Unit:")
				REC_PLACE = raw_input("Place:")
			Insert_recipe()			
		if sys.argv[x] == "-rd":
			REC_ID = sys.argv[x+1]  
			Delete_recipe()
		if sys.argv[x] == "-ru":
			ITEM_ID = str(dblength+1)
			try:
				count = 0 
				REC_NAME_VALUE = input("Name of the recipe:")
				REC_CATEGORY = input("Category of the recipe:")
				print("Ingredients:")
	        
				while 1:
					a_ing = input("name of ingredient" + str(count))	
					if a_ing == "" :
					  break
					REC_ING["ingredients"].append(a_ing)
					a_amount = input("amount of ingredient" + str(count))
					REC_ING["amounts"].append(a_amount)
					a_unit = input("unit of ingredient" + str(count))
					REC_ING["units"].append(a_unit)
					count += 1
	
				#REC_ING = input("Ingredients:")
				REC_INS = input("Instructions")
				REC_TIME = input("Quantity:")
				REC_UNIT = input("Unit:")
				REC_PLACE = input("Place:")
			except:
				REC_NAME_VALUE = raw_input("Name of the recipe:")
				REC_CATEGORY = raw_input("Category of the recipe:")
				print("Ingredients:")
	        
				while 1:
					a_ing = raw_input("name of ingredient" + str(count))	
					if a_ing == "" :
						break
					REC_ING["ingredients"].append(a_ing)
					a_amount = raw_input("amount of ingredient" + str(count))
					REC_ING["amounts"].append(a_amount)
					a_unit = raw_input("unit of ingredient" + str(count))
					REC_ING["units"].append(a_unit)
					count += 1
				#REC_ING = raw_input("Start date:")
				REC_INS = raw_input("Expiring date:")
				REC_TIME = raw_input("Quantity:")
				REC_UNIT = raw_input("Unit:")
				REC_PLACE = raw_input("Place:")
			Insert_recipe()			
	if sys.argv[x] == "-rl":
		subarg = str("id")
		try:
			if sys.argv[x+1] == "nam":
				subarg = str("nam")
			if sys.argv[x+1] == "cat":
				subarg = str("cat")
			if sys.argv[x+1] == "beg":
				subarg = str("beg")
			if sys.argv[x+1] == "exp":
				subarg = str("exp")
			if sys.argv[x+1] == "qua":
				subarg = str("qua")
			if sys.argv[x+1] == "uni":
				subarg = str("uni")
			if sys.argv[x+1] == "pla":
				subarg = str("pla")								
		except:
			pass
		Get_recipe(subarg)
	
