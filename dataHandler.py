import sqlite3


def createDatabase():

	db = sqlite3.connect('database.db')

	cursor = db.cursor()

	cursor.execute("""

			CREATE TABLE dictionaries
			(
				Dictionaries text
			)

		""")

	db.commit()

	cursor.execute("""

			CREATE TABLE current_dictionary
			(
				c_dictionary text
			)

		""")

	db.commit()

	cursor.execute("""

			CREATE TABLE track_language
			(
				dictionary text,
				primary_language text,
				learning_language text
			)

		""")

	db.commit()

	db.close()


def createCounterTable():

	db = sqlite3.connect('database.db')

	cursor = db.cursor()

	cursor.execute("""

			CREATE TABLE counter
			(
				opened INTEGER
			)

		""")

	db.commit()

	cursor.execute("""

			INSERT INTO counter VALUES(1)

		""")

	db.commit()
	db.close()


def checkCounterTable():

	db = sqlite3.connect('database.db')

	cursor = db.cursor()

	cursor.execute("""

			SELECT * FROM counter

		""")

	data = cursor.fetchall()

	db.close()


def addDictionary(language):

	db = sqlite3.connect('database.db')

	cursor = db.cursor()

	cursor.execute("""

			INSERT INTO dictionaries VALUES (?)

		""", (language,))


	db.commit()
	db.close()


def checkDictionaries():

	db = sqlite3.connect('database.db')

	cursor = db.cursor()

	cursor.execute("""

			SELECT * FROM dictionaries

		""")

	data = cursor.fetchall()

	db.close()
	return data


def addTrackLanguage(language, primary_lan, learning_lan):

	maximum_dictionary = 3

	if len(checkDictionaries()) <= maximum_dictionary:

		db = sqlite3.connect('database.db')

		cursor = db.cursor()

		cursor.execute("""

				INSERT INTO track_language VALUES(?,?,?)

			""", (language, primary_lan, learning_lan))

		db.commit()
		db.close()


def checkTrackLanguage():

	db = sqlite3.connect('database.db')

	cursor = db.cursor()

	cursor.execute("""

			SELECT * FROM track_language

		""")

	data = cursor.fetchall()

	db.close()
	return data


def createDictionaryData():

	maximum_dictionary = 3

	if len(checkDictionaries()) <= maximum_dictionary:

		db = sqlite3.connect('database.db')

		cursor = db.cursor()

		if len(checkDictionaries()) == 1:

			cursor.execute("""

					CREATE TABLE dictionary1

					(
						words text,
						meanings text
					)

				""")

			db.commit()

		elif len(checkDictionaries()) == 2:

			cursor.execute("""

					CREATE TABLE dictionary2
					(
						words text,
						meanings text
					)

				""")

			db.commit()

		if len(checkDictionaries()) == 3:

			cursor.execute("""

					CREATE TABLE dictionary3
					(
						words text,
						meanings text
					)

				""")

			db.commit()

		db.close()

	else:
		pass


def addCurrentDictionary(language):

	db = sqlite3.connect('database.db')

	cursor = db.cursor()

	cursor.execute("""

			INSERT INTO current_dictionary VALUES (?)

		""", (language,))

	db.commit()
	db.close()


def checkCurrentDictionary():

	db = sqlite3.connect('database.db')

	cursor = db.cursor()

	cursor.execute("""

			SELECT * FROM current_dictionary

		""")

	data = cursor.fetchall()

	db.close()
	return data


def addDataToDictionary(word, meaning):

	db = sqlite3.connect('database.db')

	cursor = db.cursor()

	if checkCurrentDictionary()[-1][-1] == 'dictionary1':

		cursor.execute("""

				INSERT INTO dictionary1 VALUES (?,?)

			""", (word,meaning))

		db.commit()

	if checkCurrentDictionary()[-1][-1] == 'dictionary2':

		cursor.execute("""

				INSERT INTO dictionary2 VALUES (?,?)

			""", (word,meaning))

		db.commit()

	if checkCurrentDictionary()[-1][-1] == 'dictionary3':

		cursor.execute("""

				INSERT INTO dictionary3 VALUES (?,?)

			""", (word,meaning))

		db.commit()

	db.close()


def getDictionary():

	db = sqlite3.connect('database.db')

	cursor = db.cursor()

	if checkCurrentDictionary()[-1][-1] == 'dictionary1':

		cursor.execute("""

				SELECT * FROM dictionary1

			""")

		data = cursor.fetchall()
		return data

	elif checkCurrentDictionary()[-1][-1] == 'dictionary2':

		cursor.execute("""

				SELECT * FROM dictionary2

			""")

		data = cursor.fetchall()
		return data

	elif checkCurrentDictionary()[-1][-1] == 'dictionary3':

		cursor.execute("""

				SELECT * FROM dictionary3

			""")

		data = cursor.fetchall()
		return data

	db.close()


def getDictionaryWords():

    wordsToShow = []

    db = sqlite3.connect('database.db')
    cursor = db.cursor()

    if checkCurrentDictionary()[-1][-1] == 'dictionary1':

	    cursor.execute("""

	            SELECT words FROM dictionary1

	        """)

	    word_data = cursor.fetchall()

	    for word in word_data:
	        wordsToShow.append(word[0])

	    db.close()

	    if len(wordsToShow) >= 1:
	        words = '\n'.join(wordsToShow)

	    else:
	        words = 'Add Your First Word'
	    return words

    elif checkCurrentDictionary()[-1][-1] == 'dictionary2':

	    cursor.execute("""

	            SELECT words FROM dictionary2

	        """)

	    word_data = cursor.fetchall()

	    for word in word_data:
	        wordsToShow.append(word[0])

	    db.close()

	    if len(wordsToShow) >= 1:
	        words = '\n'.join(wordsToShow)

	    else:
	        words = 'Add Your First Word'
	    return words

    elif checkCurrentDictionary()[-1][-1] == 'dictionary3':

	    cursor.execute("""

	            SELECT words FROM dictionary3

	        """)

	    word_data = cursor.fetchall()

	    for word in word_data:
	        wordsToShow.append(word[0])

	    db.close()

	    if len(wordsToShow) >= 1:
	        words = '\n'.join(wordsToShow)

	    else:
	        words = 'Add Your First Word'
	    return words


def getDictionaryMeanings():

    meaningsToShow = []

    db = sqlite3.connect('database.db')
    cursor = db.cursor()

    if checkCurrentDictionary()[-1][-1] == 'dictionary1':

	    cursor.execute("""

	            SELECT meanings FROM dictionary1

	        """)

	    meaning_data = cursor.fetchall()

	    for meaning in meaning_data:
	        meaningsToShow.append(meaning[0])

	    db.close()

	    if len(meaningsToShow) >= 1:
	        meanings = '\n'.join(meaningsToShow)

	    else:
	        meanings = 'Add Your First Meaning'

	    return meanings

    elif checkCurrentDictionary()[-1][-1] == 'dictionary2':

	    cursor.execute("""

	            SELECT meanings FROM dictionary2

	        """)

	    meaning_data = cursor.fetchall()

	    for meaning in meaning_data:
	        meaningsToShow.append(meaning[0])

	    db.close()

	    if len(meaningsToShow) >= 1:
	        meanings = '\n'.join(meaningsToShow)

	    else:
	        meanings = 'Add Your First Meaning'

	    return meanings

    elif checkCurrentDictionary()[-1][-1] == 'dictionary3':

	    cursor.execute("""

	            SELECT meanings FROM dictionary3

	        """)

	    meaning_data = cursor.fetchall()

	    for meaning in meaning_data:
	        meaningsToShow.append(meaning[0])

	    db.close()

	    if len(meaningsToShow) >= 1:
	        meanings = '\n'.join(meaningsToShow)

	    else:
	        meanings = 'Add Your First Meaning'

	    return meanings


def sortedDictionary():

	wordsToShow = []
	meaningsToShow = []

	db = sqlite3.connect('database.db')
	cursor = db.cursor()

	if checkCurrentDictionary()[-1][-1] == 'dictionary1':

		cursor.execute("""

	            SELECT * FROM dictionary1
	            ORDER BY words COLLATE NOCASE

	        """)

		data = cursor.fetchall()

		for word in data:
			wordsToShow.append(word[0])

		for meaning in data:
			meaningsToShow.append(meaning[1])

		db.close()

		return wordsToShow, meaningsToShow

	if checkCurrentDictionary()[-1][-1] == 'dictionary2':

		cursor.execute("""

	            SELECT * FROM dictionary2
	            ORDER BY words COLLATE NOCASE

	        """)

		data = cursor.fetchall()

		for word in data:
			wordsToShow.append(word[0])

		for meaning in data:
			meaningsToShow.append(meaning[1])

		db.close()

		return wordsToShow, meaningsToShow

	if checkCurrentDictionary()[-1][-1] == 'dictionary3':

		cursor.execute("""

	            SELECT * FROM dictionary3
	            ORDER BY words COLLATE NOCASE

	        """)

		data = cursor.fetchall()

		for word in data:
			wordsToShow.append(word[0])

		for meaning in data:
			meaningsToShow.append(meaning[1])

		db.close()

		return wordsToShow, meaningsToShow


def deleteWord(word):

	db = sqlite3.connect('database.db')

	cursor = db.cursor()

	if checkCurrentDictionary()[-1][-1] == 'dictionary1':

		cursor.execute("""

				DELETE from dictionary1 WHERE words = (?)

			""",(word,))
		db.commit()

	elif checkCurrentDictionary()[-1][-1] == 'dictionary2':

		cursor.execute("""

				DELETE from dictionary2 WHERE words = (?)

			""",(word,))
		db.commit()

	elif checkCurrentDictionary()[-1][-1] == 'dictionary3':

		cursor.execute("""

				DELETE from dictionary3 WHERE words = (?)

			""",(word,))
		db.commit()


	db.close()


def changeWord(new_word, meaning):

	db = sqlite3.connect('database.db')

	cursor = db.cursor()

	if checkCurrentDictionary()[-1][-1] == 'dictionary1':

		cursor.execute("""

				UPDATE dictionary1 SET words = (?) WHERE meanings = (?)

			""", (new_word, meaning))
		db.commit()

	elif checkCurrentDictionary()[-1][-1] == 'dictionary2':

		cursor.execute("""

				UPDATE dictionary2 SET words = (?) WHERE meanings = (?)

			""", (new_word, meaning))
		db.commit()

	elif checkCurrentDictionary()[-1][-1] == 'dictionary3':

		cursor.execute("""

				UPDATE dictionary3 SET words = (?) WHERE meanings = (?)

			""", (new_word, meaning))
		db.commit()


	db.close()


def changeMeaning(new_meaning, word):

	db = sqlite3.connect('database.db')

	cursor = db.cursor()

	if checkCurrentDictionary()[-1][-1] == 'dictionary1':

		cursor.execute("""

				UPDATE dictionary1 SET meanings = (?) WHERE words = (?)

			""", (new_meaning, word))
		db.commit()

	elif checkCurrentDictionary()[-1][-1] == 'dictionary2':

		cursor.execute("""

				UPDATE dictionary2 SET meanings = (?) WHERE words = (?)

			""", (new_meaning, word))
		db.commit()

	elif checkCurrentDictionary()[-1][-1] == 'dictionary3':

		cursor.execute("""

				UPDATE dictionary3 SET meanings = (?) WHERE words = (?)

			""", (new_meaning, word))
		db.commit()


	db.close()


def dictionaryLanguages(dictionary):

	db = sqlite3.connect('database.db')

	cursor = db.cursor()

	cursor.execute("""


			SELECT primary_language, learning_language
			FROM track_language
			WHERE dictionary = (?)



		""", (dictionary,))

	data = cursor.fetchall()
	db.close()
	return data