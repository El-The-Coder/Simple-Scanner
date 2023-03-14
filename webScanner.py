import wappalyzer

#buat ngidentifikasi tehnologi apa yang digunakan dalam suatu website
#install pip dulu dengan menjalakan perintah ; pip install wappalyzer


# Get user input for website URL
url = input("Enter website URL: ")

# Perform Wappalyzer scan on website
technologies = wappalyzer.analyze(url)

# Print technologies used on website
print(f"Technologies used on {url}:")
for technology in technologies:
    print(f"- {technology}")
