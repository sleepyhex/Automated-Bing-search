import pyautogui
import time
import random
import os

# --- 1. SETUP & LOAD DATA ---
script_dir = os.path.dirname(__file__) 
file_path = os.path.join(script_dir, "search-list.txt")

# Load file with UTF-8 to handle special characters
with open(file_path, "r", encoding="utf-8") as file:
    search_list = [line.strip() for line in file.readlines() if line.strip()]

# Check if list is empty
if not search_list:
    print("Error: Your search-list.txt is empty!")
    exit()

# --- 2. USER INPUTS ---
# Ask which browser
browser = input("\n Which Browser: ").lower().strip()

# Ask for number of searches
try:
    searchs = int(input(" How many search: "))
    # Cap the searches to the number of words available
    if searchs <= 0:
        searchs = 0
except ValueError:
    print("\n Search value error, exiting.")
    exit()

# Shuffle the list so we get unique random orders
random.shuffle(search_list)

# --- 3. OPEN BROWSER & START ---
print(f"\n Launching {browser}...")
pyautogui.hotkey('ctrl', 'esc')
time.sleep(0.2)
pyautogui.write(browser)
pyautogui.press('enter')
time.sleep(3) # Wait for browser to open

# Go to Bing
pyautogui.write("bing.com")
pyautogui.press('enter')
time.sleep(3.0) # Wait for Bing to load

# --- 4. START THE SEARCH LOOP ---
for i in range(searchs):

    if i == searchs:
        pyautogui.press('/')
        if browser == "zen":
            time.sleep(5.5)
        pyautogui.write('Done')

    # Pick the next unique word from our shuffled list
    search_query = search_list[i]
    print(f" Searching ({i+1}/{searchs}): {search_query}")

    # LOGIC: First search vs Repeat searches
    if i == 0:
        None
    else:
        pyautogui.press('/')
        if browser == "zen":
            time.sleep(5.5)

        # Clear the old text
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.2)
        pyautogui.press('delete')           

    # Type and Enter
    pyautogui.write(search_query, interval=0.2)
    pyautogui.press('enter')

    # Wait before the next search (unless it's the last one)
    if i < searchs - 1:
        wait_time = random.uniform(3.5, 5.5)
        time.sleep(wait_time)

print(f"\n Task done. Performed {searchs} searches.")

exit()