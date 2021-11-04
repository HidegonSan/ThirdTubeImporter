import bs4
import csv
import glob
import os
import re
import requests


def read_csv(file_name):
	with open(file_name, "r") as fr:
		csv_data = list(csv.reader(fr))
		del csv_data[0], csv_data[-1]
	return csv_data


def convert_to_json(channels):
	# [ [id, url, icon_url, name, subscription_count_str], [id, url, ...] ... ]
	converted_json = {}
	converted_json["version"] = 0
	converted_json["channels"] = []
	
	for channel in channels:
		converted_json["channels"].append(
			{
				"id": channel[0],
				"url":  channel[1].replace("://www.", "s://m."), # http -> https
				"icon_url": channel[2],
				"name": channel[3],
				"subscriber_count_str": channel[4]
			}
		)
	converted_json = str(converted_json).replace("'", '"') # Can't use json.dumps
	return converted_json


def get_youtube_data(channel_id):	
	try:
		headers = {"User-Agent": ""}
		res = requests.get("https://www.youtube.com/channel/" + channel_id, headers=headers)
		soup = bs4.BeautifulSoup(res.text, "html.parser")
		scripts = soup.find_all("script")
		
		for script in scripts:
			if re.search("window\\[['\\\"]ytInitialData['\\\"]]\\s*=\\s*['\\{]", script.get_text()) or \
				re.search("ytInitialData\\s*=\\s*['\\{]", script.get_text()):
				target_script = script.string[4:].replace("true", "True").replace("false", "False")
				break
		
		exec(target_script)
		initial_data = locals()["ytInitialData"]
		icons = initial_data["header"]["c4TabbedHeaderRenderer"]["avatar"]["thumbnails"]
		max_width = -1
		
		for icon in icons:
			cur_width = icon["width"]
			if cur_width > 1024:
				continue
			
			if max_width < cur_width:
				max_width = cur_width
				icon_url = icon["url"]
	except:
		icon_url = "https://example.com"
	
	try:
		subscription_count_str = "チャンネル登録者数 " + initial_data["header"]["c4TabbedHeaderRenderer"]["subscriberCountText"]["simpleText"][10:]
	except:
		subscription_count_str = "チャンネル登録者数 取得失敗"
	
	return (icon_url, subscription_count_str)


def main():
	print("YouTube subscription csv to ThirdTube converter")
	files = [i for i in glob.glob("./*.csv")]
	print("\n" + "\n".join([f"{i + 1} : {j[2:]}" for i, j in enumerate(files)]) + "\n\n")
	
	try:
		select_file = files[int(input(">> ")) - 1]
	except:
		print("\nInvalid file number." + "\n\n" + "="*50 + "\n\n")
		return
	
	channels = []
	read_csv_data = read_csv(select_file)
	
	for csv_channel_data in read_csv_data:
		channel_data = []
		youtube_scrape_data = get_youtube_data(csv_channel_data[0])
		channel_data.append(csv_channel_data[0]) # ID
		channel_data.append(csv_channel_data[1]) # URL
		channel_data.append(youtube_scrape_data[0]) # ICON URL
		channel_data.append(csv_channel_data[2].replace("'", "${apostrophe}").replace('"', "${quotation}")) # NAME
		channel_data.append(youtube_scrape_data[1]) # SUBSCRIPTION COUNT
		channels.append(channel_data)

	converted_data = convert_to_json(channels)
	
	choice = "n"
	
	if os.path.exists("subscription.json"):
		choice = input("Are you sure you want to overwrite subscription.json?\n\ny or n >> ")
		if choice == "y":
			with open("subscription.json", "w") as fw:
				fw.write(converted_data.replace("${apostrophe}", "'").replace("${quotation}", '”'))
	else:
		with open("subscription.json", "w") as fw:
			fw.write(converted_data.replace("${apostrophe}", "'").replace("${quotation}", '”'))
	
	print("\n\n" + "="*50 + "\n\n")


if __name__ == "__main__":
	while True:
		main()