import requests

# Sostituisci ACCESS_TOKEN con il tuo token di accesso Instagram valido
ACCESS_TOKEN = "your_access_token"

# Nome utente di Jakidale
jakidale_username = "jakidale"

# Ottieni i follower di Jakidale
jakidale_followers_url = f"https://api.instagram.com/v1/users/{jakidale_username}/followed-by?access_token={ACCESS_TOKEN}"
jakidale_followers_response = requests.get(jakidale_followers_url).json()
jakidale_followers = [follower["username"] for follower in jakidale_followers_response["data"]]

# Ottieni i tuoi follower
your_followers_url = f"https://api.instagram.com/v1/users/self/followed-by?access_token={ACCESS_TOKEN}"
your_followers_response = requests.get(your_followers_url).json()
your_followers = [follower["username"] for follower in your_followers_response["data"]]

# Verifica se c'è un'intersezione tra i follower di Jakidale e i tuoi follower
intersection = set(jakidale_followers) & set(your_followers)

if intersection:
    print("C'è almeno una persona tra i follower di Jakidale che è anche tra i tuoi follower:")
    print(intersection)
else:
    print("Non c'è alcuna persona che è seguita da entrambi Jakidale e te.")
