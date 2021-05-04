import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import MoveTargetOutOfBoundsException
from selenium.webdriver.common.action_chains import ActionChains

b = webdriver.Chrome(executable_path='C:\Selenium Drivers\chromedriver_win32\chromedriver.exe')

#url = "https://www.bodybuilding.com/exercises/finder/?muscle=chest,forearms,lats,middle-back,lower-back,neck,quadriceps,hamstrings,calves,triceps,traps,shoulders,abdominals,glutes,biceps,adductors,abductors"
url = "https://www.bodybuilding.com/exercises/finder/"
b.get(url)
b.maximize_window()
actions = ActionChains(b)
time.sleep(1)
print("Starting...")
start = datetime.now()
estimated_exercises = 15
sample = 0
while True:
    time.sleep(1)
    locate = b.find_element_by_class_name("ExLoadMore")
    coords = locate.location
    sizes = locate.size
    b.execute_script("arguments[0].scrollIntoView();", locate)
    try:
        btn = b.find_element_by_class_name("ExLoadMore")
        time.sleep(1)
        actions.move_to_element_with_offset(btn, 76, 26)
        actions.click().perform()
        time.sleep(1)
        estimated_exercises += 15
        print("Estimate: " + str(estimated_exercises) + " exercises collected.")
        sample += 1
        html = b.page_source
    except MoveTargetOutOfBoundsException:
        print("(hopefully) Clicked every button...")
        html = b.page_source
        break
time.sleep(1)

page = requests.get(url)
soup = BeautifulSoup(html, 'html.parser')

exercise_name = []
exercise_muscle = []

exercise_name_list = soup.find_all('h3', class_='ExHeading ExResult-resultsHeading')
for exercise in exercise_name_list:
    if exercise.find('a'):
        original_exercise = exercise.find('a').text
        trimmed_exercise = original_exercise.strip()
        print(trimmed_exercise)
        exercise_name.append(str(trimmed_exercise))

exercise_muscle_list = soup.find_all('div', class_='ExResult-details ExResult-muscleTargeted')
for muscle in exercise_muscle_list:
    if muscle.find('a'):
        original_muscle = muscle.find('a').text
        trimmed_muscle = original_muscle.strip()
        exercise_muscle.append(trimmed_muscle)

loaded_name_list = soup.find_all('div', class_='ExResult-details ExResult-muscleTargeted')

both_txt = open("Exercises with muscles NEW 2.txt", "w+")
exercise_txt = open("Exercises NEW 2.txt", "w+")
muscle_txt = open("Muscles NEW 2.txt", "w+")

list_size = len(exercise_muscle)
counter = 0
while counter < list_size:
    both_txt.write(str(exercise_name[counter]) + " - " + str(exercise_muscle[counter]) + "\n")
    exercise_txt.write(str(exercise_name[counter]) + "\n")
    muscle_txt.write(str(exercise_muscle[counter]) + "\n")
    counter += 1

both_txt.close()
exercise_txt.close()
muscle_txt.close()

print("Web scraper was successful!")
print(str(len(exercise_name)) + " exercises collected.")
end = datetime.now()
print("Run time: " + str(end-start))